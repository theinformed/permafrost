# measure.py -- Compare one completed recipe while the memory watcher is active.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  keep the comparison under the same host memory floor.
"""A guarded CPU entry point for the existing weight comparison."""

import argparse
from pathlib import Path

from audit.weights import TensorStore, compare_weights, read_json
from .common import Resources, log


def main(argv=None):
    """Read a completion marker before measuring the derived copy."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True)
    parser.add_argument("--derived", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args(argv)
    card = read_json(Path(args.derived) / "recipe-card.json")
    marker = read_json(Path(args.derived) / "done.json")
    from audit.weights import digest
    if marker["card_sha256"] != digest(Path(args.derived) / "recipe-card.json") or card["status"] != "complete":
        raise ValueError("recipe has no valid completion marker")
    with Resources("cpu"):
        if TensorStore(args.base).provenance() != card["base"]["shards_sha256"]:
            raise ValueError("base shards differ from the recipe card")
        if TensorStore(args.derived).provenance() != card["derived_shards_sha256"]:
            raise ValueError("derived shards differ from the recipe card")
        log("Compare the completed reference against its base")
        report = compare_weights(args.derived, args.base, args.out)
        log(f"Compared {report['summary']['matched_tensors']} tensors")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
