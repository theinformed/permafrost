# compare.py -- Compare declarations, template text, and rendered conversations.
# Created by LT Sean Egan, PhD 2026-10-13
# Modified: SDE 2026-10-13  classify metadata changes with a short exception table.
# Modified: SDE 2026-10-13  check token and template content before noting a re-save.
import difflib
import json
import re
import subprocess
import sys

from jinja2.sandbox import ImmutableSandboxedEnvironment

EXPECTED = {"config.model_type", "config._name_or_path", "config.name_or_path"}
RESAVE = "explained by re-save"
TOKEN_KEYS = ("bos_token", "eos_token", "pad_token", "unk_token", "additional_special_tokens")
CONVERSATION = [
    {"role": "system", "content": "You are a careful assistant."},
    {"role": "user", "content": "What is two plus two?"},
    {"role": "assistant", "content": "Four."},
    {"role": "user", "content": "Write that as a word."},
]


def normalize_template(text):
    """Collapse whitespace for a first comparison; keep the exact text too."""
    return re.sub(r"\s+", " ", text).strip()


def classify(path):
    """Allow only the names in the exception table."""
    return "expected" if path in EXPECTED else "unexplained"


def resave_template(text):
    """Ignore line endings and line tails, keeping spaces inside text intact."""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    return "\n".join(line.rstrip(" \t") for line in text.split("\n")).rstrip("\n")


def token_records(documents, content):
    """Read every declaration; merging dictionaries would hide conflicting IDs."""
    records = []
    for token in documents.get("tokenizer.json", {}).get("added_tokens", []):
        if token.get("content") == content:
            records.append(token)
    decoder = documents.get("tokenizer_config.json", {}).get("added_tokens_decoder", {})
    for identifier, token in decoder.items():
        if token.get("content") == content:
            records.append({**token, "id": int(identifier)})
    mapping = documents.get("added_tokens.json", {})
    if content in mapping:
        records.append({"content": content, "id": mapping[content]})
    vocab = documents.get("tokenizer.json", {}).get("model", {}).get("vocab", {})
    if isinstance(vocab, dict) and content in vocab:
        records.append({"content": content, "id": vocab[content]})
    elif isinstance(vocab, list):
        records.extend({"content": content, "id": i} for i, token in enumerate(vocab)
                       if token[0] == content)
    return records


def same_declaration(declaration, reference, original, modified):
    """Match role, ordered strings, IDs and the flags that were written out."""
    values = declaration["value"]
    values = values if isinstance(values, list) else [values]
    other = reference["value"]
    other = other if isinstance(other, list) else [other]
    if [token_content(v) for v in values] != [token_content(v) for v in other]:
        return False
    if declaration["ids"] != reference["ids"] or len(declaration["ids"]) != len(values):
        return False
    for value, old, identifier in zip(values, other, declaration["ids"]):
        content = token_content(value)
        if not isinstance(content, str) or type(identifier) is not int:
            return False
        records = token_records(original, content) + token_records(modified, content)
        if not records or any(type(record["id"]) is not int or record["id"] != identifier for record in records):
            return False
        flags = value if isinstance(value, dict) else {}
        old_flags = old if isinstance(old, dict) else {}
        for key in (flags.keys() | old_flags.keys()) - {"content", "id"}:
            known = [record[key] for record in records if key in record]
            known.extend([old_flags[key]] if key in old_flags else [])
            if key in flags:
                if not known or any(flag != flags[key] for flag in known):
                    return False
            elif key in old_flags and (not known or any(flag != old_flags[key] for flag in known)):
                return False
    return True


def added_mapping(documents):
    """Use the internal added-token records as the counterpart of a moved file."""
    tokenizer = documents.get("tokenizer.json", {}).get("added_tokens", [])
    decoder = documents.get("tokenizer_config.json", {}).get("added_tokens_decoder", {})
    maps = [{token["content"]: token["id"] for token in tokenizer}] if tokenizer else []
    if decoder:
        maps.append({token["content"]: int(identifier) for identifier, token in decoder.items()})
    return maps[0] if maps and all(mapping == maps[0] for mapping in maps) else None


def explain_resaves(differences, original, modified, rendered):
    """Mark the three re-save cases only after their counterparts agree."""
    views = {"original": snapshot(original), "modified": snapshot(modified)}
    docs = {"original": original, "modified": modified}

    def explain(change, original_files, modified_files, reason):
        """Keep the compared file names beside the rule in JSON and on the card."""
        change.update({"class": RESAVE, "files": {"original": original_files,
                       "modified": modified_files}, "reason": reason})

    relocation = None
    for source, target in (("original", "modified"), ("modified", "original")):
        inline = docs[source].get("tokenizer_config.json", {}).get("chat_template")
        standalone = docs[target].get("chat_template.jinja")
        retained = docs[target].get("tokenizer_config.json", {}).get("chat_template")
        values = rendered.get("default", {})
        if ("chat_template.jinja" not in docs[source] and isinstance(inline, str)
                and isinstance(standalone, str) and (retained is None or retained == inline)
                and resave_template(inline) == resave_template(standalone)
                and set(values) == {"original", "modified"}
                and values["original"] == values["modified"]):
            relocation = {source: ["tokenizer_config.json"], target: ["chat_template.jinja"]}

    for change in differences:
        path = change["path"]
        if path in ("config.transformers_version", "generation.transformers_version"):
            if all(isinstance(change[side], str) for side in ("original", "modified")):
                filename = "config.json" if path.startswith("config.") else "generation_config.json"
                explain(change, [filename], [filename], "The saved version string changed.")
        elif path in ("template_source.tokenizer_config", "template.default") and relocation:
            explain(change, relocation["original"], relocation["modified"],
                    "The template moved; line endings and trailing whitespace normalize equally, "
                    "and the fixed conversation renders identically.")
        elif path.startswith(("special_tokens.special_tokens_map.json:",
                              "special_tokens.tokenizer_config.json:")):
            # An existing declaration changing in place needs its own explanation.
            absent = [side for side in docs if not change.get(side + "_present", True)]
            if len(absent) != 1:
                continue
            source = absent[0]
            target = "modified" if source == "original" else "original"
            filename, role = path.removeprefix("special_tokens.").split(":", 1)
            counterpart = ("tokenizer_config.json" if filename == "special_tokens_map.json"
                           else "special_tokens_map.json")
            reference = views[source]["special_tokens"].get(counterpart + ":" + role)
            source_files = [counterpart, "tokenizer.json"]
            if reference is None and filename == "special_tokens_map.json" and role != "additional_special_tokens":
                identifier = docs[source].get("config.json", {}).get(role + "_id")
                tokens = [token for token, number in token_ids(docs[source]).items() if number == identifier]
                if type(identifier) is int and len(tokens) == 1:
                    reference = {"value": tokens[0], "ids": [identifier]}
                    source_files = ["config.json", "tokenizer.json"]
            declaration = change[target]
            if reference and same_declaration(declaration, reference, original, modified):
                files = {source: source_files, target: [filename]}
                explain(change, files["original"], files["modified"],
                        "The same token strings and IDs were declared in a separate file.")
        elif path == "added_tokens.file":
            absent = [side for side in docs if "added_tokens.json" not in docs[side]]
            if len(absent) != 1:
                continue
            source = absent[0]
            target = "modified" if source == "original" else "original"
            mapping = change[target]
            if (not isinstance(mapping, dict) or not mapping
                    or mapping != added_mapping(docs[source]) or mapping != added_mapping(docs[target])):
                continue
            if all(type(identifier) is int and all(type(record["id"]) is int and record["id"] == identifier
                   for record in token_records(original, token) + token_records(modified, token))
                   for token, identifier in mapping.items()):
                files = {source: ["tokenizer.json", "tokenizer_config.json"], target: ["added_tokens.json"]}
                explain(change, files["original"], files["modified"],
                        "The added-token file repeats the existing strings and IDs.")


def token_content(value):
    """Token objects carry flags as well as text; resolve IDs from their text."""
    return value.get("content") if isinstance(value, dict) else value


def token_ids(documents):
    """Combine vocabulary and added-token IDs without loading a tokenizer."""
    tokenizer = documents.get("tokenizer.json", {})
    vocab = tokenizer.get("model", {}).get("vocab", {})
    ids = dict(vocab) if isinstance(vocab, dict) else {entry[0]: i for i, entry in enumerate(vocab)}
    for token in tokenizer.get("added_tokens", []):
        ids[token["content"]] = token["id"]
    ids.update(documents.get("added_tokens.json", {}))
    return ids


def templates(documents):
    """Keep named templates instead of silently selecting the first one."""
    result = {}
    config = documents.get("tokenizer_config.json", {})
    value = config.get("chat_template")
    if isinstance(value, str):
        result["default"] = value
    elif isinstance(value, list):
        result.update({v["name"]: v["template"] for v in value})
    elif isinstance(value, dict):
        result.update(value)
    if "chat_template.jinja" in documents:
        result["default"] = documents["chat_template.jinja"]
    return result


def snapshot(documents):
    """Keep token declarations from every file so conflicting claims stay visible."""
    ids = token_ids(documents)
    declarations = {}
    for filename in ("tokenizer_config.json", "special_tokens_map.json"):
        document = documents.get(filename, {})
        for key in TOKEN_KEYS:
            if key not in document:
                continue
            value = document[key]
            contents = value if isinstance(value, list) else [value]
            declarations[f"{filename}:{key}"] = {
                "value": value, "ids": [ids.get(token_content(token)) for token in contents],
            }
    tokenizer = documents.get("tokenizer.json", {})
    decoder = documents.get("tokenizer_config.json", {}).get("added_tokens_decoder", {})
    for token in tokenizer.get("added_tokens", []):
        if token.get("special"):
            declarations[f"tokenizer.json:{token['id']}"] = token
    for identifier, token in decoder.items():
        if token.get("special"):
            declarations[f"added_tokens_decoder:{identifier}"] = token
    vocab = tokenizer.get("model", {}).get("vocab")
    config = documents.get("config.json", {})
    return {"templates": templates(documents), "special_tokens": declarations,
            "special_token_ids": {k: v for k, v in config.items() if k.endswith("_token_id")},
            "added_tokens": {"tokenizer": tokenizer.get("added_tokens"),
                             "decoder": decoder or None, "file": documents.get("added_tokens.json")},
            "vocabulary_size": {"base": len(vocab) if vocab is not None else None,
                                "with_added": len(ids) if ids else None,
                                "config": config.get("vocab_size")},
            "generation": documents.get("generation_config.json"), "config": config}


def exact_diff(original, modified):
    """Keep line endings in the source values and readable lines in the diff."""
    return "".join(difflib.unified_diff(original.splitlines(True), modified.splitlines(True),
                                        fromfile="original", tofile="modified"))


def render_inline(template, documents):
    """Use tokenizer-style optional fields in a sandbox with bounded output."""
    environment = ImmutableSandboxedEnvironment(trim_blocks=True, lstrip_blocks=True)
    if len(template) > 1024 * 1024:
        raise ValueError("template source exceeds 1 MiB")

    def raise_exception(message):
        """Let a template reject a conversation with its own error text."""
        raise ValueError(message)

    environment.globals.update(raise_exception=raise_exception, strftime_now=lambda fmt: "2000-01-01")
    environment.filters["tojson"] = lambda value, **kwargs: json.dumps(value, ensure_ascii=False, **kwargs)
    config = {**documents.get("special_tokens_map.json", {}),
              **documents.get("tokenizer_config.json", {})}
    context = {key: token_content(config.get(key)) or "" for key in TOKEN_KEYS[:-1]}
    context.update(messages=CONVERSATION, add_generation_prompt=True, tools=None,
                   documents=None, enable_thinking=False)
    import signal

    def expired(signum, frame):
        """A hostile loop should cost a few seconds, not the morning."""
        raise ValueError("template rendering exceeded 2 seconds")

    previous = signal.signal(signal.SIGALRM, expired)
    signal.setitimer(signal.ITIMER_REAL, 2)
    try:
        result, length = [], 0
        for part in environment.from_string(template).generate(**context):
            length += len(part)
            if length > 1024 * 1024:
                raise ValueError("rendered template exceeds 1 MiB")
            result.append(part)
        return "".join(result)
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous)


def render(template, documents):
    """Keep arbitrary template expressions inside a small, short-lived process."""
    config = {**documents.get("special_tokens_map.json", {}),
              **documents.get("tokenizer_config.json", {})}
    tokens = {key: config.get(key) for key in TOKEN_KEYS[:-1]}
    result = subprocess.run([sys.executable, "-m", "audit.template_worker"],
                            input=json.dumps({"template": template, "tokens": tokens}),
                            text=True, capture_output=True, timeout=4)
    if result.returncode:
        raise ValueError("template worker exceeded its resource budget")
    reply = json.loads(result.stdout)
    if "error" in reply:
        raise ValueError(reply["error"])
    return reply["rendered"]


def compare_documents(modified, original):
    """Report changes and missing evidence separately so absence cannot pass."""
    left, right = snapshot(original), snapshot(modified)
    differences, missing = [], []

    def add(path, a, b, **extra):
        """Attach the values and the rule to each changed field."""
        if a != b or extra.get("original_present") != extra.get("modified_present"):
            differences.append({"path": path, "original": a, "modified": b,
                                "class": classify(path), **extra})

    def fields(path, a, b):
        """Descend config dictionaries, keeping absent keys distinct from null."""
        for key in sorted(a.keys() | b.keys()):
            if key in a and key in b and isinstance(a[key], dict) and isinstance(b[key], dict):
                fields(f"{path}.{key}", a[key], b[key])
            else:
                add(f"{path}.{key}", a.get(key), b.get(key),
                    original_present=key in a, modified_present=key in b)

    for key in ("special_tokens", "special_token_ids", "added_tokens", "vocabulary_size", "generation", "config"):
        a, b = left[key], right[key]
        if isinstance(a, dict) and isinstance(b, dict):
            if key in ("config", "generation"):
                fields(key, a, b)
            else:
                for field in sorted(a.keys() | b.keys()):
                    add(f"{key}.{field}", a.get(field), b.get(field),
                        original_present=field in a, modified_present=field in b)
        else:
            add(key, a, b)
    rendered = {}
    original_declared = original.get("tokenizer_config.json", {}).get("chat_template")
    modified_declared = modified.get("tokenizer_config.json", {}).get("chat_template")
    if "chat_template.jinja" in original or "chat_template.jinja" in modified:
        add("template_source.tokenizer_config", original_declared, modified_declared)
    for name in sorted(left["templates"].keys() | right["templates"].keys()):
        a, b = left["templates"].get(name), right["templates"].get(name)
        if a is None or b is None:
            missing.append(f"template {name} absent on one side")
            add(f"template.{name}", a, b)
            continue
        add(f"template.{name}", a, b, normalized_equal=normalize_template(a) == normalize_template(b),
            resave_normalized_equal=resave_template(a) == resave_template(b),
            exact_diff=exact_diff(a, b))
        values = {}
        for side, text, docs in (("original", a, original), ("modified", b, modified)):
            try:
                values[side] = render(text, docs)
            except Exception as error:
                missing.append(f"{side} template {name} render failed: {type(error).__name__}: {error}")
        rendered[name] = values
        if len(values) == 2:
            add(f"rendered_template.{name}", values["original"], values["modified"],
                exact_diff=exact_diff(values["original"], values["modified"]))
    for side, docs, view in (("original", original, left), ("modified", modified, right)):
        for file in ("config.json", "tokenizer_config.json", "tokenizer.json", "generation_config.json"):
            if file not in docs:
                missing.append(f"{side}: {file} missing")
        if not view["templates"]:
            missing.append(f"{side}: chat template missing")
        if "tokenizer.json" in docs and view["vocabulary_size"]["base"] is None:
            missing.append(f"{side}: vocabulary unavailable in tokenizer.json")
        for name, declaration in view["special_tokens"].items():
            values = declaration.get("value")
            values = values if isinstance(values, list) else [values]
            if "ids" in declaration and any(identifier is None and token_content(value) is not None
                                             for value, identifier in zip(values, declaration["ids"])):
                missing.append(f"{side}: token ID unresolved for {name}")
    explain_resaves(differences, original, modified, rendered)
    return differences, missing, rendered
