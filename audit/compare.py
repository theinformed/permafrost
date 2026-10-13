# compare.py -- Compare declarations, template text, and rendered conversations.
# Created by LT Sean Egan, PhD 2026-10-13
# Modified: SDE 2026-10-13  classify metadata changes with a short exception table.
import difflib
import json
import re
import subprocess
import sys

from jinja2.sandbox import ImmutableSandboxedEnvironment

EXPECTED = {"config.model_type", "config._name_or_path", "config.name_or_path"}
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
    config = documents.get("tokenizer_config.json", {})
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
    config = documents.get("tokenizer_config.json", {})
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
    return differences, missing, rendered
