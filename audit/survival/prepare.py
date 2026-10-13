# prepare.py -- Merge an existing published adapter with a staged local base.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  export local copies and retain their source hashes.
"""Merge already-published adapter weights; no optimization or training occurs here."""

import argparse
from pathlib import Path

from audit.recipes.common import Resources, load_runtime, log, save_merged
from audit.weights import TensorStore, digest
from .probe import REGISTRY, load_entry, write_json


def main(argv=None):
    """Prepare a local full checkpoint for the ordinary recipe interfaces."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--entry", required=True)
    parser.add_argument("--registry", type=Path, default=REGISTRY)
    parser.add_argument("--clean", type=Path, required=True)
    parser.add_argument("--artifact", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--storage-budget-gb", type=float, default=64)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    entry = load_entry(args.entry, args.registry)
    if entry["artifact_kind"] != "adapter":
        raise ValueError("this entry is already a full checkpoint")
    clean, artifact, out = (path.resolve() for path in (args.clean, args.artifact, args.out))
    if not clean.is_dir() or not (artifact / "adapter_config.json").is_file():
        raise ValueError("a staged base and published adapter directory are required")
    weights = artifact / "adapter_model.safetensors"
    if not weights.is_file() or weights.stat().st_size > 1_000_000_000:
        raise ValueError("published adapter is absent or exceeds 1 GB")
    size = sum(path.stat().st_size for path in clean.glob("*.safetensors")) / 1e9
    if not 0 < args.storage_budget_gb <= 4096 or 2 * size > args.storage_budget_gb:
        raise ValueError("local merge exceeds its declared storage budget")
    log(f"Local merge: up to {2 * size:.1f} GB; budget {args.storage_budget_gb:.1f} GB; retain until review")
    if args.dry_run:
        return 0
    import shutil
    if shutil.disk_usage(out.parent if out.parent.exists() else clean).free / 1e9 < 2 * size + 12:
        raise ValueError("local merge lacks disk headroom")
    if out.exists():
        raise ValueError("output exists; choose a fresh directory")
    from peft import PeftModel
    with Resources("cuda:0") as resources:
        origin = {"repo": entry["repo"], "revision": entry["revision"],
                  "base_model": entry["base_model"], "base_shards_sha256": TensorStore(clean).provenance(),
                  "adapter_sha256": digest(weights), "adapter_config_sha256": digest(artifact / "adapter_config.json"),
                  "scope": "Adapter and base shard hashes match the pinned public metadata; configuration files are locally hashed."}
        expected = entry["verified_files"]
        if origin["base_shards_sha256"] != expected["clean"]["weights"]:
            raise ValueError("clean shards differ from the pinned base revision")
        if origin["adapter_sha256"] != expected["published"]["weights"]["adapter_model.safetensors"]:
            raise ValueError("adapter differs from the pinned published source")
        runtime, tokenizer = load_runtime(clean, resources)
        log("Load the published adapter without training")
        runtime = PeftModel.from_pretrained(runtime, artifact, local_files_only=True, is_trainable=False)
        runtime = runtime.merge_and_unload(safe_merge=True)
        resources.check()
        log("Save the merged checkpoint in shards no larger than 1 GB")
        out.mkdir(parents=True)
        save_merged(runtime, tokenizer, out, clean)
        origin["merged_shards_sha256"] = TensorStore(out).provenance()
        write_json(out / "survival-origin.json", origin)
    log(f"Local merged copy: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
