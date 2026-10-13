# metadata.py -- Collect pinned small files and write a Stage 1 finding card.
# Created by LT Sean Egan, PhD 2026-10-13
# Modified: SDE 2026-10-13  compare tokenizer files and packed-file headers.
# Modified: SDE 2026-10-13  show re-save findings and reuse pinned evidence on reruns.
import json
import hashlib
import re
import shutil
from pathlib import Path
from types import SimpleNamespace

import requests

from .compare import RESAVE, compare_documents, snapshot, token_content, token_ids
from .gguf import RangeReader, parse_header
from .hub import BudgetExpired, FILE_LIMIT, SMALL_FILES, Hub, safe_name, write_json

LIMITATION = "This metadata audit does not certify the absence of hidden behavior."
CACHE_ROOT = "data/metadata-cache"
CACHE_LIMIT = 2 * 1024 ** 3
REPO_LIMIT = 256 * 1024 ** 2


def cache_usage(path):
    """Count this command's cache, leaving other audit caches alone."""
    return sum(file.stat().st_size for file in Path(path).rglob("*") if file.is_file())


def superseded(directory):
    """Only revision directories owned by this reader are cleanup candidates."""
    return [path for path in directory.parent.iterdir() if path.is_dir()
            and re.fullmatch(r"[0-9a-f]{40}", path.name) and path != directory] if directory.parent.exists() else []


def collect(hub, repo, cache_root, evidence=None):
    """Pin the revision once and record unavailable files rather than replacing them."""
    try:
        if evidence is None:
            info = hub.info(repo)
        else:
            info = SimpleNamespace(sha=evidence["sha"], siblings=[
                SimpleNamespace(rfilename=name, size=record["bytes"])
                for name, record in evidence["manifest"].items()])
    except Exception as error:
        if getattr(getattr(error, "response", None), "status_code", None) == 429:
            raise
        return {"repo": repo, "sha": None, "documents": {}, "manifest": {},
                "missing": [f"catalog unavailable: {type(error).__name__}: {error}"],
                "gguf_header": None, "gguf_only": False}
    directory = Path(cache_root) / safe_name(repo) / info.sha
    documents, missing, manifest = {}, [], {}
    files = {file.rfilename: file for file in info.siblings or []}
    for name in SMALL_FILES:
        if name not in files:
            continue
        try:
            if files[name].size is not None and files[name].size > FILE_LIMIT:
                raise ValueError("metadata file exceeds 64 MiB")
            local = directory / name
            if local.exists():
                if local.stat().st_size > FILE_LIMIT:
                    raise ValueError("cached metadata file exceeds 64 MiB")
                raw = local.read_bytes()
            else:
                available = min(FILE_LIMIT, REPO_LIMIT - cache_usage(directory),
                                CACHE_LIMIT - cache_usage(cache_root))
                if available <= 0:
                    raise ValueError("metadata cache budget exhausted (2 GiB total; 256 MiB per repo)")
                raw = hub.small_file(repo, info.sha, name, directory, max_bytes=available)
            digest = hashlib.sha256(raw).hexdigest()
            if evidence and digest != evidence["manifest"][name]["sha256"]:
                raise ValueError("metadata checksum differs from pinned evidence")
            text = raw.decode("utf-8")
            documents[name] = text if name.endswith(".jinja") else json.loads(text)
            manifest[name] = {"bytes": len(raw), "sha256": digest}
        except requests.HTTPError as error:
            if error.response.status_code == 429:
                raise
            missing.append(f"{name}: HTTP {error.response.status_code}")
        except (BudgetExpired, ValueError, UnicodeError, requests.RequestException) as error:
            missing.append(f"{name}: {type(error).__name__}: {error}")
    gguf_names = sorted(name for name in files if name.lower().endswith(".gguf"))
    native_weights = (not evidence["gguf_only"] if evidence else
                     any(name.lower().endswith((".safetensors", ".bin", ".pt", ".pth")) for name in files))
    header = evidence.get("gguf_header") if evidence else None
    if gguf_names and not native_weights:
        name = gguf_names[0]
        try:
            header = parse_header(RangeReader(hub, repo, info.sha, name))
            header["file"] = name
        except requests.HTTPError as error:
            if error.response.status_code == 429:
                raise
            missing.append(f"{name}: HTTP {error.response.status_code}")
        except (BudgetExpired, ValueError, UnicodeError, requests.RequestException) as error:
            missing.append(f"{name}: {type(error).__name__}: {error}")
    if not missing and evidence is None:
        for old in superseded(directory):
            shutil.rmtree(old)
    return {"repo": repo, "sha": info.sha, "documents": documents,
            "manifest": manifest, "missing": missing, "gguf_header": header,
            "gguf_only": evidence["gguf_only"] if evidence else bool(gguf_names) and not native_weights}


def compare_gguf(header, original):
    """Compare fields with direct tokenizer counterparts; keep other header fields."""
    metadata = header["metadata"]
    template = metadata.get("tokenizer.chat_template")
    documents = {"chat_template.jinja": template} if isinstance(template, str) else {}
    config = {}
    ids = token_ids(original)
    reverse = {identifier: token for token, identifier in ids.items()}
    tokens = metadata.get("tokenizer.ggml.tokens")
    if tokens is not None:
        vocab = {token: index for index, token in enumerate(tokens)}
        documents["tokenizer.json"] = {"model": {"vocab": vocab}}
    differences, missing, rendered = compare_documents(documents, original)
    # File layout changes in this format are not token changes. Compare the
    # shared fields below, and report fields without a counterpart as missing.
    differences = [d for d in differences if d["path"].startswith(("template.", "rendered_template."))]
    missing = [m for m in missing if "template" in m]

    def add(path, a, b):
        """Header fields without an exception are unexplained when they differ."""
        if a != b:
            differences.append({"path": path, "original": a, "modified": b, "class": "unexplained"})

    tokenizer_config = original.get("tokenizer_config.json", {})
    special_map = original.get("special_tokens_map.json", {})
    for role in ("bos", "eos", "pad", "unk"):
        key = f"tokenizer.ggml.{role}_token_id"
        declared = special_map.get(role + "_token", tokenizer_config.get(role + "_token"))
        expected = original.get("config.json", {}).get(role + "_token_id")
        if expected is None and declared is not None:
            expected = ids.get(token_content(declared))
        if key not in metadata:
            if declared is not None or expected is not None:
                missing.append(f"GGUF: {key} missing")
            continue
        identifier = metadata[key]
        config[role + "_token_id"] = identifier
        add(f"special_token_ids.{role}_token_id", expected, identifier)
        if tokens is None or identifier < 0 or identifier >= len(tokens):
            missing.append(f"GGUF: token text unavailable for {key}")
        elif declared is not None:
            add(f"special_token_text.{role}", token_content(declared), tokens[identifier])
    if tokens is None:
        missing.append("GGUF: tokenizer.ggml.tokens missing")
    else:
        # Text inventories may use a different byte encoding. A mismatch is
        # evidence for review, not a claim that a token has changed meaning.
        expected_tokens = [reverse.get(i) for i in range(max(reverse, default=-1) + 1)]
        add("vocabulary_size.with_added", len(expected_tokens), len(tokens))
        changes = [{"id": i, "original": reverse.get(i), "modified": token}
                   for i, token in enumerate(tokens) if reverse.get(i) != token]
        if changes:
            differences.append({"path": "gguf.token_text", "original": "tokenizer.json",
                                "modified": changes, "class": "unexplained"})
    # Header special tokens supply the context used by the rendering comparison.
    documents["tokenizer_config.json"] = {role + "_token": tokens[identifier]
        for role, identifier in ((key.removesuffix("_token_id"), value) for key, value in config.items())
        if tokens is not None and 0 <= identifier < len(tokens)}
    again, render_missing, rendered = compare_documents(documents, original)
    differences = [d for d in differences if not d["path"].startswith("rendered_template.")]
    differences.extend(d for d in again if d["path"].startswith("rendered_template."))
    missing = [m for m in missing if "render failed" not in m]
    missing.extend(m for m in render_missing if "render failed" in m)
    missing.append("GGUF: full config, added-token declarations and generation settings have no complete header counterpart")
    return differences, missing, rendered


def verdict(differences, missing):
    """Known unexplained changes take precedence over incomplete coverage."""
    if any(d["class"] not in ("expected", RESAVE) for d in differences):
        return "unexplained differences"
    if missing:
        return "undecided"
    return "consistent with re-save noted" if any(d["class"] == RESAVE for d in differences) else "consistent"


def card_text(report):
    """Keep the card short; full values and template diffs live in the JSON."""
    lines = [f"# Stage 1: {report['modified']['repo']}", "",
             f"Original: `{report['original']['repo']}`", "",
             f"Verdict: **{report['verdict']}**", "",
             f"Revisions: modified `{report['modified']['sha']}`; original `{report['original']['sha']}`.", ""]
    differences = report["differences"]
    ordinary = [d for d in differences if d["class"] != RESAVE]
    if ordinary:
        lines.append("Changed fields:")
        lines.append("")
        lines.extend(f"- `{d['path']}` ({d['class']})" for d in ordinary)
        lines.append("")
    elif not differences:
        lines.extend(["No compared field differs.", ""])
    for change in differences:
        if change["class"] == RESAVE:
            lines.extend([f"## Explained by re-save: `{change['path']}`", ""])
            for side in ("original", "modified"):
                names = ", ".join(f"`{name}`" for name in change["files"][side])
                lines.extend([f"{side.capitalize()} file: {names}.", ""])
            lines.extend([change["reason"], ""])
    if report["missing"]:
        lines.extend(["Missing evidence:", ""])
        lines.extend(f"- {item}" for item in report["missing"])
        lines.append("")
    for name, values in report["rendered"].items():
        change = next((d for d in differences if d["path"] == f"template.{name}"), None)
        if change and change.get("resave_normalized_equal") is False:
            lines.extend([f"The `{name}` template source differs beyond line endings and trailing whitespace.", ""])
        if len(values) == 2:
            result = "identically" if values["original"] == values["modified"] else "differently"
            lines.extend([f"The fixed conversation renders {result} with the `{name}` template.", ""])
    lines.extend([LIMITATION, ""])
    return "\n".join(lines)


def metadata_diff(args):
    """Write JSON evidence and a Markdown card after both sides are collected."""
    hub = Hub(args.delay, max_seconds=45)
    prior = None
    if getattr(args, "from_evidence", None):
        prior = json.loads(Path(args.from_evidence).read_text())
        if prior["modified"]["repo"] != args.repo or prior["original"]["repo"] != args.original:
            raise ValueError("evidence repository pair differs from requested pair")
        if prior["missing"] or any(prior[side]["missing"] for side in ("original", "modified")):
            raise ValueError("pinned rerun requires complete saved evidence")
    if args.cache_dry_run:
        for side, repo in (("modified", args.repo), ("original", args.original)):
            revision = prior[side]["sha"] if prior else hub.info(repo).sha
            directory = Path(CACHE_ROOT) / safe_name(repo) / revision
            print(f"{repo}: retain {revision}")
            if prior:
                continue
            for old in superseded(directory):
                print(f"  superseded: {old} ({cache_usage(old) / 1024 ** 2:.1f} MiB)")
        return
    modified = collect(hub, args.repo, CACHE_ROOT, prior["modified"] if prior else None)
    original = collect(hub, args.original, CACHE_ROOT, prior["original"] if prior else None)
    if modified["missing"] or original["missing"]:
        differences, missing, rendered = [], ["Comparison deferred until requested metadata can be read."], {}
    elif modified["gguf_only"] and modified["gguf_header"]:
        differences, missing, rendered = compare_gguf(modified["gguf_header"], original["documents"])
    else:
        differences, missing, rendered = compare_documents(modified["documents"], original["documents"])
    missing.extend("modified: " + m for m in modified["missing"])
    missing.extend("original: " + m for m in original["missing"])
    # Raw vocabularies are already saved at their pinned revisions. Reports need
    # the measured fields and checksums, not another copy of every token string.
    evidence = [{**{k: v for k, v in side.items() if k != "documents"},
                 "snapshot": snapshot(side["documents"])} for side in (modified, original)]
    report = {"schema_version": 1, "modified": evidence[0], "original": evidence[1],
              "differences": differences, "missing": sorted(set(missing)), "rendered": rendered,
              "limitation": LIMITATION}
    report["verdict"] = verdict(differences, missing)
    write_json(args.out, report)
    card = Path("docs/cards") / (safe_name(args.repo) + ".md")
    card.parent.mkdir(parents=True, exist_ok=True)
    card.write_text(card_text(report))
    print(card_text(report))
    print(f"Evidence: {args.out}\nCard: {card}")
