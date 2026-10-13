# resolver.py -- Follow declared ancestry without inventing missing parents.
# Created by LT Sean Egan, PhD 2026-10-13
# Modified: SDE 2026-10-13  separate quantization copies from weight modifications.


def declarations(card, tags=()):
    """Keep each declared parent and its relation, including tag-only cards."""
    result = []
    relation = card.get("base_model_relation")
    for key, value in card.items():
        if key != "base_model" and not key.startswith("base_model:"):
            continue
        kind = key.partition(":")[2] or relation or "unspecified"
        for parent in value if isinstance(value, list) else [value]:
            if isinstance(parent, str) and "/" in parent:
                result.append({"id": parent, "relation": kind})
    for tag in tags:
        if not tag.startswith("base_model:"):
            continue
        value = tag[len("base_model:"):]
        prefix, separator, parent = value.partition(":")
        if separator and prefix in ("finetune", "quantized", "merge", "adapter"):
            item = {"id": parent, "relation": prefix}
        elif "/" in value:
            item = {"id": value, "relation": relation or "unspecified"}
        else:
            continue
        result.append(item)
    # A specific relation carries more information than the plain parent tag.
    specific = {p["id"] for p in result if p["relation"] != "unspecified"}
    unique = {(p["id"], p["relation"]) for p in result
              if p["relation"] != "unspecified" or p["id"] not in specific}
    return [{"id": parent, "relation": kind} for parent, kind in sorted(unique)]


def mirror_parent(row):
    """Accept a quantization declaration or quantized weights with one parent."""
    parents = row.get("base_models", [])
    quantized = {p["id"] for p in parents if p["relation"] == "quantized"}
    if quantized:
        return next(iter(quantized)) if len(quantized) == 1 else None, True
    weights = {f["format"] for f in row.get("files", [])
               if f["format"] in ("gguf", "safetensors", "pickle/bin")}
    tags = {str(t).lower() for t in row.get("tags", [])}
    quantization = str(row.get("quantization") or "").lower()
    packed = weights == {"gguf"} or bool(weights) and (
        quantization in ("awq", "gptq") or bool(tags & {"awq", "gptq", "quantized:awq", "quantized:gptq"}))
    ids = {p["id"] for p in parents}
    return (next(iter(ids)) if len(ids) == 1 else None), packed


def resolve(rows, ancestry=()):
    """Resolve within the observed catalog; absent ancestors stay explicit."""
    by_id = {row["id"]: row for row in [*ancestry, *rows] if not row.get("unavailable")}
    for row in by_id.values():
        parent, packed = mirror_parent(row)
        row["role"] = "mirror" if packed else "source"
        row["mirror_of"] = parent if packed else None
    for row in rows:
        current, seen = row, set()
        reason = None
        while current["role"] == "mirror":
            if current["id"] in seen:
                reason = "cycle in mirror declarations"
                break
            seen.add(current["id"])
            parent = current.get("mirror_of")
            if parent not in by_id:
                reason = "mirror parent absent or ambiguous"
                break
            current = by_id[parent]
        row["source_id"] = None if reason else current["id"]
        row["source_resolution"] = reason or "resolved"
        chain = []
        original = None
        while not reason:
            if current["id"] in seen:
                reason = "cycle in base declarations"
                break
            seen.add(current["id"])
            parents = {p["id"] for p in current.get("base_models", [])}
            if not parents:
                reason = "no declared original" if not chain else "ancestry ends in catalog"
                if chain:
                    original = current["id"]
                break
            if len(parents) != 1:
                reason = "multiple declared parents"
                break
            parent = next(iter(parents))
            chain.append(parent)
            if parent not in by_id:
                reason = "declared parent outside catalog; ancestry unresolved"
                break
            current = by_id[parent]
        row["stated_original"] = original
        row["original_chain"] = chain
        row["original_resolution"] = reason
    return rows
