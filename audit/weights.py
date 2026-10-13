# weights.py -- Compare checkpoint tensors without loading a checkpoint at once.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  download limit from the environment; send the hub token.
# Modified: SDE 2026-10-13  measure differences and test the projection envelope.
# Modified: SDE 2026-10-13  hash shards on the compute interpreter too.
# Modified: SDE 2026-10-13  classify residual writers and score selected projections.
# Modified: SDE 2026-10-13  apply measured row-norm limits only to their recorded base.
"""Stream checkpoint pairs, measure their differences, and write a recipe report."""

import hashlib
import json
import math
import os
import re
from pathlib import Path

import requests
import torch
from huggingface_hub import get_token
from safetensors import safe_open
from safetensors.torch import save_file


ROOT = Path(__file__).resolve().parents[1]
# One gigabyte a file on a shared box unless the machine running this says otherwise (PERMAFROST_MAX_DOWNLOAD_GB).
MAX_DOWNLOAD = int(float(os.environ.get("PERMAFROST_MAX_DOWNLOAD_GB", "1")) * 1_000_000_000)


def auth_header():
    """Send the saved hub token when there is one; gated originals need it."""
    token = get_token()
    return {"Authorization": "Bearer " + token} if token else {}


def safe_name(value):
    """Make a directory name; repository slashes stay out of local paths."""
    return re.sub(r"[^A-Za-z0-9_.-]+", "-", value).strip(".-") or "checkpoint"


def read_json(path):
    """Read a small record, separate from the checkpoint bytes."""
    return json.loads(Path(path).read_text())


def write_json(path, record):
    """Replace a complete record, so interrupted writes leave no half report."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".part")
    temporary.write_text(json.dumps(record, indent=2, allow_nan=False) + "\n")
    temporary.replace(path)


def digest(path):
    """Hash a file in small blocks; checkpoint provenance costs no extra copy."""
    with Path(path).open("rb") as stream:
        checksum = hashlib.sha256()
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            checksum.update(block)
        return checksum.hexdigest()


def inside(directory, name):
    """Reject shard paths that would escape the checkpoint directory."""
    path = (directory / name).resolve()
    if not path.is_relative_to(directory.resolve()):
        raise ValueError(f"path outside checkpoint: {name}")
    return path


def resolve_checkpoint(value, revision="main", cache=None):
    """Fetch only weight shards and tokenizer metadata, pinned to one revision."""
    local = Path(value)
    if local.is_dir():
        return local.resolve(), {"source": str(local.resolve()), "revision": None}
    from urllib.parse import quote

    endpoint = f"https://huggingface.co/api/models/{quote(value, safe='/')}/revision/{quote(revision, safe='')}"
    response = requests.get(endpoint, params={"blobs": "true"}, timeout=30)
    response.raise_for_status()
    info = response.json()
    sha = info["sha"]
    directory = Path(cache or ROOT / "data/cache") / safe_name(value) / sha
    selected = []
    metadata = {"config.json", "tokenizer.json", "tokenizer_config.json", "special_tokens_map.json", "generation_config.json", "model.safetensors.index.json"}
    for item in info["siblings"]:
        name = item["rfilename"]
        if (name.endswith(".safetensors") and "/" not in name) or name in metadata:
            size = item.get("size")
            if size is None or size > MAX_DOWNLOAD:
                raise ValueError(f"file size missing or above the download limit ({MAX_DOWNLOAD // 1_000_000_000} GB): {name}")
            selected.append(item)
    if not any(item["rfilename"].endswith(".safetensors") for item in selected):
        raise ValueError("checkpoint has no safetensors shards")
    directory.mkdir(parents=True, exist_ok=True)
    for item in selected:
        path = inside(directory, item["rfilename"])
        checksum = (item.get("lfs") or {}).get("sha256")
        if path.exists() and path.stat().st_size == item["size"] and (not checksum or digest(path) == checksum):
            continue
        temporary = path.with_suffix(path.suffix + ".part")
        url = f"https://huggingface.co/{value}/resolve/{sha}/{item['rfilename']}"
        try:
            with requests.get(url, stream=True, timeout=30, headers=auth_header()) as download:
                download.raise_for_status()
                length = download.headers.get("Content-Length")
                if length and int(length) > MAX_DOWNLOAD:
                    raise ValueError("download exceeds the limit of %d GB" % (MAX_DOWNLOAD // 1_000_000_000))
                total = 0
                with temporary.open("wb") as stream:
                    for block in download.iter_content(1024 * 1024):
                        total += len(block)
                        if total > min(MAX_DOWNLOAD, item["size"]):
                            raise ValueError("download exceeds declared size")
                        stream.write(block)
            if total != item["size"] or (checksum and digest(temporary) != checksum):
                raise ValueError(f"download size or checksum differs: {path.name}")
            temporary.replace(path)
        finally:
            temporary.unlink(missing_ok=True)
    return directory, {"source": value, "revision": sha}


class TensorStore:
    """Keep a name-to-shard map; each read opens only the required shard."""

    def __init__(self, directory):
        self.directory = Path(directory).resolve()
        self.names = {}
        index = self.directory / "model.safetensors.index.json"
        declared = read_json(index).get("weight_map", {}) if index.exists() else None
        paths = sorted({inside(self.directory, name) for name in declared.values()}) if declared is not None else sorted(self.directory.glob("*.safetensors"))
        if not paths:
            raise ValueError(f"no safetensors shards in {directory}")
        for path in paths:
            with safe_open(path, framework="pt", device="cpu") as shard:
                for name in shard.keys():
                    if name in self.names:
                        raise ValueError(f"duplicate tensor name: {name}")
                    self.names[name] = path
        if declared is not None:
            if set(declared) != set(self.names):
                raise ValueError("shard index does not match tensor names")
            for name, shard in declared.items():
                if inside(self.directory, shard) != self.names[name]:
                    raise ValueError(f"wrong shard in index: {name}")

    def get(self, name):
        """Read one tensor, leaving its shard closed when the call returns."""
        with safe_open(self.names[name], framework="pt", device="cpu") as shard:
            return shard.get_tensor(name)

    def provenance(self):
        """Record shard checksums so local comparisons can be repeated exactly."""
        return {str(path.relative_to(self.directory)): digest(path) for path in sorted(set(self.names.values()))}


def recipe_table():
    """Read role patterns and envelopes from the same small table."""
    return read_json(Path(__file__).with_name("recipes.json"))


def strip_prefix(name, recipes):
    """Remove the longest wrapper first; nested wrappers otherwise lose a piece."""
    for prefix in sorted(recipes["tensor_kinds"]["prefixes"], key=len, reverse=True):
        if name.startswith(prefix):
            return name[len(prefix):]
    return name


def tensor_kind(name, recipes=None):
    """Match the matrix's role after removing its optional wrapper."""
    recipes = recipe_table() if recipes is None else recipes
    name = strip_prefix(name, recipes)
    for entry in recipes["tensor_kinds"]["patterns"]:
        if re.fullmatch(entry["pattern"], name):
            return entry["kind"]
    return "other"


def residual_kinds(recipes):
    """Find roles that write to the residual stream, including expert outputs."""
    return {entry["kind"] for entry in recipes["tensor_kinds"]["patterns"] if entry.get("residual_writer")}


def as_float(tensor):
    """Unpack native quantized values; packed integer checkpoints need a decoder."""
    if tensor.is_quantized:
        return tensor.dequantize().float()
    if not tensor.is_floating_point():
        raise ValueError("integer or packed quantized tensor needs a format-specific decoder")
    return tensor.float()


def measure_tensor(original, modified, threshold=1e-3, seed=0):
    """Measure a pair in float32; SVD work is limited to changed matrices."""
    result = {"shape_original": list(original.shape), "shape_modified": list(modified.shape), "dtype_original": str(original.dtype), "dtype_modified": str(modified.dtype)}
    if original.shape != modified.shape:
        return {**result, "status": "shape_mismatch", "changed": True}, None
    base, other = as_float(original), as_float(modified)
    if not torch.isfinite(base).all() or not torch.isfinite(other).all():
        return {**result, "status": "nonfinite", "changed": True}, None
    delta = other - base
    if not torch.isfinite(delta).all():
        return {**result, "status": "nonfinite_difference", "changed": True}, None
    norm = float(torch.linalg.vector_norm(base, dtype=torch.float64))
    diff_norm = float(torch.linalg.vector_norm(delta, dtype=torch.float64))
    relative = diff_norm / norm if norm else (0.0 if not diff_norm else None)
    changed = relative is None or relative > threshold
    result.update(status="ok", changed=changed, original_norm=norm, difference_norm=diff_norm, relative_difference=relative,
                  mean_difference=float(delta.mean()) if delta.numel() else 0.0,
                  max_difference=float(delta.max()) if delta.numel() else 0.0,
                  min_difference=float(delta.min()) if delta.numel() else 0.0,
                  max_absolute_difference=float(delta.abs().max()) if delta.numel() else 0.0,
                  positive_fraction=float((delta > 0).float().mean()) if delta.numel() else 0.0,
                  negative_fraction=float((delta < 0).float().mean()) if delta.numel() else 0.0)
    result["difference_sign"] = "mixed" if result["positive_fraction"] and result["negative_fraction"] else "positive" if result["positive_fraction"] else "negative" if result["negative_fraction"] else "zero"
    vectors = None
    if delta.ndim == 2:
        rows_base = torch.linalg.vector_norm(base, dim=1)
        rows_other = torch.linalg.vector_norm(other, dim=1)
        row_error = (rows_other - rows_base).abs()
        result["row_norms"] = {"preserved_equal": bool(torch.isclose(rows_base, rows_other, rtol=1e-5, atol=1e-7).all()), "rtol": 1e-5, "atol": 1e-7,
                               "max_relative_error": float((row_error / rows_base.clamp_min(1e-30)).max()) if row_error.numel() else 0.0}
        if changed and diff_norm and min(delta.shape):
            # A few extra columns keep the eighth value away from the sketch's edge.
            q = min(12, min(delta.shape))
            with torch.random.fork_rng(devices=[]):
                torch.manual_seed(seed)
                left, singular, right = torch.svd_lowrank(delta, q=q, niter=4)
            values = singular[:8].double()
            energy = values.square().cumsum(0) / (diff_norm ** 2)
            result["singular_values"] = values.tolist() + [0.0] * (8 - len(values))
            shares = energy.clamp(0, 1).tolist()
            result["energy_shares"] = shares + [shares[-1]] * (8 - len(shares))
            result["first_singular_energy_share"] = shares[0]
            pivot = int(left[:, 0].abs().argmax())
            sign = 1.0 if left[pivot, 0] >= 0 else -1.0
            vectors = (left[:, 0].mul(sign).contiguous(), right[:, 0].mul(sign).contiguous())
    return result, vectors


def direction_agreement(rows, vectors, recipes=None):
    """Align SVD signs before taking a coordinate median of unit directions."""
    groups = {}
    for name, pair in vectors.items():
        kind = rows[name]["kind"]
        groups.setdefault((kind, pair[0].numel()), []).append(name)
    summaries = {}
    for (kind, size), names in groups.items():
        matrix = torch.stack([vectors[name][0] for name in names]).double()
        matrix = matrix / torch.linalg.vector_norm(matrix, dim=1, keepdim=True)
        # Use the most central vector as the sign reference, rather than the first layer.
        similarities = (matrix @ matrix.T).abs()
        reference = matrix[similarities.sum(1).argmax()]
        aligned = matrix * torch.where(matrix @ reference < 0, -1.0, 1.0)[:, None]
        median = torch.quantile(aligned, 0.5, dim=0)
        median_norm = float(torch.linalg.vector_norm(median))
        if not median_norm:
            for name in names:
                rows[name]["direction_cosine"] = None
            summaries[f"{kind}:{size}"] = {"count": len(names), "median_direction_defined": False, "median_cosine": None, "min_cosine": None}
            continue
        median = median / median_norm
        cosines = (matrix @ median).abs().clamp(0, 1)
        for name, cosine in zip(names, cosines.tolist()):
            rows[name]["direction_cosine"] = cosine
        summaries[f"{kind}:{size}"] = {"count": len(names), "median_direction_defined": True, "median_cosine": float(torch.quantile(cosines, 0.5)), "min_cosine": float(cosines.min())}
    # Input widths differ, but every residual writer shares the output coordinates.
    writers = residual_kinds(recipe_table() if recipes is None else recipes)
    by_size = {}
    for name, pair in vectors.items():
        if rows[name]["kind"] in writers:
            by_size.setdefault(pair[0].numel(), []).append(pair[0].double())
    cross_kind = []
    for values in by_size.values():
        matrix = torch.stack(values)
        matrix = matrix / torch.linalg.vector_norm(matrix, dim=1, keepdim=True)
        cosines = (matrix @ matrix.T).abs().clamp(0, 1)
        cross_kind.append(float(cosines.min()))
    all_cosines = [row["direction_cosine"] for row in rows.values() if row.get("direction_cosine") is not None]
    return {"groups": summaries, "median_cosine": float(torch.tensor(all_cosines, dtype=torch.float64).quantile(0.5)) if all_cosines else None,
            "min_cosine": min(all_cosines) if all_cosines else None, "cross_kind_min_cosine": min(cross_kind) if cross_kind else None}


def match_recipes(rows, structural, agreement, recipes):
    """List each envelope failure; unmeasured recipes stay out of the ranking."""
    candidates = []
    for name, recipe in recipes.items():
        if recipe.get("status") not in ("measured", "analytic"):
            continue
        violations = list(structural)
        expected = set(recipe["changed_kinds"])
        present = {row["kind"] for row in rows.values()}
        observed = {row["kind"] for row in rows.values() if row["changed"]}
        selected = recipe.get("allow_unchanged_projections", False)
        skipped = []
        if not observed & expected:
            violations.append({"rule": "missing_changed_projection"})
        if not selected:
            for kind in sorted((expected & present) - observed):
                violations.append({"rule": "missing_changed_kind", "kind": kind})
        for tensor, row in rows.items():
            if row["status"] != "ok":
                violations.append({"rule": row["status"], "tensor": tensor})
                continue
            if recipe.get("row_norms_preserved") is True and "row_norms" in row and not row["row_norms"]["preserved_equal"]:
                violations.append({"rule": "row_norms_not_preserved", "tensor": tensor})
            relative = row["relative_difference"]
            if row["kind"] not in expected:
                if relative is None or relative > recipe["unchanged_relative_max"]:
                    violations.append({"rule": "unexpected_change", "tensor": tensor, "value": relative})
            elif not row["changed"]:
                if selected and relative is not None and relative <= recipe["unchanged_relative_max"]:
                    layer = re.search(r"(?:^|\.)layers\.(\d+)\.", tensor)
                    skipped.append({"tensor": tensor, "layer": int(layer[1]) if layer else None, "kind": row["kind"]})
                else:
                    violations.append({"rule": "expected_tensor_unchanged", "tensor": tensor, "value": relative})
            else:
                share = row.get("first_singular_energy_share")
                if share is None or share < recipe["first_energy_min"]:
                    violations.append({"rule": "first_energy_share", "tensor": tensor, "value": share, "minimum": recipe["first_energy_min"]})
                cosine = row.get("direction_cosine")
                if cosine is None or cosine < recipe["direction_cosine_min"]:
                    violations.append({"rule": "direction_cosine", "tensor": tensor, "value": cosine, "minimum": recipe["direction_cosine_min"]})
        cosine = agreement["cross_kind_min_cosine"]
        if cosine is not None and cosine < recipe["direction_cosine_min"]:
            violations.append({"rule": "cross_kind_direction", "value": cosine, "minimum": recipe["direction_cosine_min"]})
        candidates.append({"recipe": name, "matched": not violations, "violations": violations, "skipped_projections": skipped})
    candidates.sort(key=lambda item: (len(item["violations"]), item["recipe"]))
    return {"nearest_recipe": candidates[0]["recipe"] if candidates else None, "matched": candidates[0]["matched"] if candidates else False,
            "violations": candidates[0]["violations"] if candidates else [], "candidates": candidates,
            "skipped_projections": candidates[0]["skipped_projections"] if candidates else [],
            "unmeasured": [name for name, recipe in recipes.items() if "status" in recipe and recipe["status"] not in ("measured", "analytic")]}


def score_report(report, recipes=None):
    """Score recorded tensor measures without fetching weights or changing them."""
    recipes = recipe_table() if recipes is None else recipes
    out_of_scope = []
    applicable = dict(recipes)
    for name, recipe in recipes.items():
        hashes = recipe.get("base_shards_sha256")
        if hashes is not None and hashes != report["original"]["shards_sha256"]:
            out_of_scope.append(name)
            applicable[name] = {**recipe, "status": "outside calibrated base"}
    rows = report["tensors"]
    for name, row in rows.items():
        row["kind"] = tensor_kind(name, recipes)
    structural = [{"rule": "original_only", "tensor": name} for name in report["original_only"]]
    structural += [{"rule": "modified_only", "tensor": name} for name in report["modified_only"]]
    agreement = report["summary"]["direction_agreement"]
    matching = match_recipes(rows, structural, agreement, applicable)
    matching["outside_calibrated_base"] = out_of_scope
    changed = [name for name, row in rows.items() if row["changed"]]
    writers = residual_kinds(recipes)
    outside = [row["relative_difference"] for row in rows.values() if row["kind"] not in writers and row["status"] == "ok"]
    shares = [rows[name]["first_singular_energy_share"] for name in changed if "first_singular_energy_share" in rows[name]]
    report["recipe_matching"] = matching
    report["summary"].update(
        assessment="unchanged" if not changed and not structural else "recipe_match" if matching["matched"] else "recipe_violations",
        matched_tensors=len(rows), changed_set=changed, changed_kinds=sorted({rows[name]["kind"] for name in changed}),
        max_relative_difference_outside_changed_set=max([row["relative_difference"] for row in rows.values() if not row["changed"]], default=0.0),
        max_relative_difference_outside_recipe_set=None if None in outside else max(outside, default=0.0),
        min_first_singular_energy_share=min(shares) if shares else None,
        changed_without_svd=[name for name in changed if "first_singular_energy_share" not in rows[name]])
    return report


def rescore_weights(path, out=None, recipes_path=None):
    """Reassess a saved report; its direction measurements keep their references."""
    report = read_json(path)
    report["rescoring"] = {
        "previous_assessment": report["summary"]["assessment"],
        "previous_nearest_recipe": report["recipe_matching"]["nearest_recipe"],
        "direction_measurements": "Retained from the saved comparison; group references and cross-kind coverage have not been recomputed."}
    score_report(report, read_json(recipes_path) if recipes_path else None)
    write_json(out or path, report)
    return report


@torch.inference_mode()
def compare_weights(modified, original, out, threshold=1e-3, recipes_path=None, original_revision="main", modified_revision="main", seed=0):
    """Compare one pair and save leading vectors separately from its JSON report."""
    if not math.isfinite(threshold) or threshold < 0:
        raise ValueError("threshold must be finite and nonnegative")
    recipes = read_json(recipes_path) if recipes_path else recipe_table()
    original_dir, original_info = resolve_checkpoint(original, original_revision)
    modified_dir, modified_info = resolve_checkpoint(modified, modified_revision)
    base, other = TensorStore(original_dir), TensorStore(modified_dir)
    missing = sorted(base.names.keys() - other.names.keys())
    added = sorted(other.names.keys() - base.names.keys())
    rows, vectors = {}, {}
    for name in sorted(base.names.keys() & other.names.keys()):
        # Nothing in this loop retains the full tensors from the preceding pair.
        first, second = base.get(name), other.get(name)
        row, pair = measure_tensor(first, second, threshold, seed)
        del first, second
        row["kind"] = tensor_kind(name, recipes)
        rows[name] = row
        if pair is not None:
            vectors[name] = pair
    agreement = direction_agreement(rows, vectors, recipes)
    directions_path = Path(out).with_suffix(".directions.safetensors")
    directions_path.parent.mkdir(parents=True, exist_ok=True)
    saved = {}
    for name, pair in vectors.items():
        saved[name + ".left"], saved[name + ".right"] = pair
        rows[name]["directions"] = {"left": name + ".left", "right": name + ".right"}
    save_file(saved, str(directions_path))
    report = {"schema_version": 1, "original": {**original_info, "shards_sha256": base.provenance()}, "modified": {**modified_info, "shards_sha256": other.provenance()},
              "threshold": threshold, "svd": {"seed": seed, "top_k": 8, "sketch_columns": 12, "power_iterations": 4}, "original_only": missing, "modified_only": added,
              "tensors": rows, "directions_file": directions_path.name,
              "summary": {"direction_agreement": agreement},
              "scope": "Weight differences alone cannot certify the absence of hidden behavior."}
    score_report(report, recipes)
    write_json(out, report)
    return report
