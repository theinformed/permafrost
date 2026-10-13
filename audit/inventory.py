# inventory.py -- Build a resumable catalog and count its declared sources.
# Created by LT Sean Egan, PhD 2026-10-13
# Modified: SDE 2026-10-13  collect file metadata and keep search terms visible.
import json
import time
from collections import Counter
from pathlib import Path

from .hub import BudgetExpired, Hub, write_json
from .resolver import declarations, resolve


def file_format(name):
    """Describe weight storage without opening a weight file."""
    suffix = Path(name).suffix.lower()
    return {".safetensors": "safetensors", ".gguf": "gguf", ".bin": "pickle/bin",
            ".pt": "pickle/bin", ".pth": "pickle/bin", ".pkl": "pickle/bin"}.get(suffix, "metadata/other")


def info_row(info, terms):
    """Store card claims beside file sizes and checksums from the catalog."""
    card = info.card_data.to_dict() if info.card_data else {}
    files = []
    for sibling in info.siblings or []:
        lfs = sibling.lfs
        files.append({"name": sibling.rfilename, "size": sibling.size,
                      "format": file_format(sibling.rfilename), "blob_id": sibling.blob_id,
                      "sha256": getattr(lfs, "sha256", None)})
    names = {file["name"] for file in files}
    templates = [name for name in ("chat_template.jinja", "tokenizer_config.json") if name in names]
    return {"id": info.id, "author": info.author or info.id.partition("/")[0],
            "created": info.created_at.isoformat() if info.created_at else None,
            "last_modified": info.last_modified.isoformat() if info.last_modified else None,
            "downloads_30d": info.downloads, "downloads_all_time": getattr(info, "downloads_all_time", None),
            "likes": info.likes, "license": card.get("license"), "tags": info.tags or [],
            "pipeline": info.pipeline_tag, "library": info.library_name, "card_data": card,
            "quantization": (info.config or {}).get("quantization_config", {}).get("quant_method"),
            "base_models": declarations(card, info.tags or []), "files": files,
            "chat_template_sources": templates, "gated": info.gated, "sha": info.sha,
            "terms": sorted(terms)}


def read_rows(path):
    """Read completed lines; a damaged resume file needs a visible repair."""
    if not Path(path).exists():
        return []
    with Path(path).open() as handle:
        return [json.loads(line) for line in handle if line.strip()]


def save_rows(path, rows):
    """Write the resolved catalog beside the original before replacing it."""
    temporary = path.with_suffix(".jsonl.tmp")
    with temporary.open("w") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    temporary.replace(path)


def inventory(args):
    """Round-robin searches so a small sample includes every requested term."""
    hub = Hub(args.delay, max_seconds=args.max_seconds)
    deadline = time.monotonic() + args.max_seconds
    path = Path(args.out)
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = read_rows(path)
    known = {row["id"]: row for row in rows}
    terms = list(dict.fromkeys(t.strip() for t in args.terms.split(",") if t.strip()))
    searches = {term: iter(hub.api.list_models(search=term, sort="downloads",
                          expand=["downloads", "downloadsAllTime"])) for term in terms}
    active = list(terms)
    added = 0
    ancestry_path = path.with_suffix(".ancestry.json")
    ancestry = json.loads(ancestry_path.read_text()) if ancestry_path.exists() else {}
    try:
        while active and time.monotonic() < deadline - 15 and (args.limit is None or len(rows) < args.limit):
            for term in active[:]:
                if time.monotonic() >= deadline - 15:
                    break
                try:
                    item = next(searches[term])
                except StopIteration:
                    active.remove(term)
                    continue
                if item.id in known:
                    known[item.id]["terms"] = sorted(set(known[item.id]["terms"]) | {term})
                    continue
                info = hub.info(item.id)
                matched = {term} | {t for t in terms if t.lower() in item.id.lower()}
                row = info_row(info, matched)
                if row["downloads_all_time"] is None:
                    row["downloads_all_time"] = getattr(item, "downloads_all_time", None)
                rows.append(row)
                known[item.id] = row
                # Append first. An interrupted pass can skip this API call next time.
                with path.open("a") as handle:
                    handle.write(json.dumps(row, ensure_ascii=False) + "\n")
                added += 1
                print(f"{added}: {item.id}", flush=True)
                if args.limit is not None and len(rows) >= args.limit:
                    break
        pending = {p["id"] for row in rows for p in row["base_models"]} - known.keys()
        for depth in range(8):
            next_parents = set()
            for parent in sorted(pending):
                if time.monotonic() >= deadline - 15:
                    break
                if parent not in ancestry:
                    try:
                        ancestor = info_row(hub.info(parent), [])
                        ancestry[parent] = ancestor
                        write_json(ancestry_path, ancestry)
                    except Exception as error:
                        if isinstance(error, BudgetExpired):
                            break
                        if getattr(getattr(error, "response", None), "status_code", None) == 429:
                            raise
                        print(f"Ancestry unavailable: {parent}: {type(error).__name__}")
                        ancestry[parent] = {"id": parent, "unavailable": type(error).__name__, "base_models": []}
                        write_json(ancestry_path, ancestry)
                        continue
                if ancestry[parent].get("unavailable"):
                    continue
                next_parents.update(p["id"] for p in ancestry[parent]["base_models"])
            pending = next_parents - known.keys() - ancestry.keys()
            if not pending or time.monotonic() >= deadline - 15:
                break
    finally:
        save_rows(path, resolve(rows, ancestry.values()))
    print(f"Saved {len(rows)} repos ({added} new) to {path}.")


def summary(rows, ancestry=()):
    """Count observed matches and keep mirror downloads separate."""
    counts = Counter(term for row in rows for term in row["terms"])
    by_id = {row["id"]: row for row in [*ancestry, *rows]}
    source_ids = {row["source_id"] for row in rows if row["source_id"]}
    sources = [by_id[source] for source in source_ids]
    mirrors = Counter()
    for row in rows:
        if row["role"] == "mirror" and row["source_id"]:
            mirrors[row["source_id"]] += row.get("downloads_30d") or 0
    top = sorted(sources, key=lambda row: (row.get("downloads_30d") or 0) + mirrors[row["id"]], reverse=True)[:20]
    creators = Counter(row["author"] for row in rows)
    formats = Counter(fmt for row in rows for fmt in {f["format"] for f in row["files"]}
                      if fmt != "metadata/other")
    lines = [f"Repos: {len(rows)}", "Matches per term (overlap allowed): " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())),
             f"Distinct sources: {len(sources)}; unresolved mirrors: {sum(r['source_id'] is None for r in rows)}",
             f"Resolvable stated originals: {sum(r['stated_original'] is not None for r in rows)}/{len(rows)}",
             "Downloads below cover 30 days; missing counts contribute zero.",
             "Top sources: source downloads + mirror downloads"]
    lines.extend(f"  {row['id']}: {row.get('downloads_30d') or 0:,} + {mirrors[row['id']]:,}" for row in top)
    lines.append("Top creators: " + ", ".join(f"{k}={v}" for k, v in creators.most_common(10)))
    lines.append("Repo formats (overlap allowed): " + ", ".join(f"{k}={v}" for k, v in sorted(formats.items())))
    return "\n".join(lines)
