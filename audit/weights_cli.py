# weights_cli.py -- Expose checkpoint comparison and the two CPU null controls.
# Created by LT Sean Egan, PhD 2026-10-13
# Modified: SDE 2026-10-13  add revision pins and short null steps.
"""Command-line entry points for tensor measurements and null checkpoints."""

import argparse
import json
import sys

def register_commands(subparsers):
    """Add weight commands to a shared parser without claiming other commands."""
    compare = subparsers.add_parser("compare-weights", help="Compare checkpoint tensors on CPU")
    compare.add_argument("--modified", required=True)
    compare.add_argument("--original", required=True)
    compare.add_argument("--out", required=True)
    compare.add_argument("--threshold", type=float, default=1e-3)
    compare.add_argument("--original-revision", default="main")
    compare.add_argument("--modified-revision", default="main")
    compare.add_argument("--recipes")
    compare.add_argument("--seed", type=int, default=0)
    compare.add_argument("--threads", type=int, choices=(1, 2), default=1)
    compare.set_defaults(handler=run_compare)
    null = subparsers.add_parser("make-null", help="Make rounding and single-direction controls")
    null.add_argument("--model", required=True)
    null.add_argument("--out-dir")
    null.add_argument("--step", choices=("all", "prepare", "rounding", "activations", "project", "compare"), default="all")
    null.add_argument("--batch-index", type=int)
    null.add_argument("--prompts")
    null.add_argument("--threads", type=int, choices=(1, 2), default=1)
    null.set_defaults(handler=run_null)


def run_compare(args):
    """Print the few comparison numbers a person can use."""
    import torch
    from .weights import compare_weights

    torch.set_num_threads(args.threads)
    report = compare_weights(args.modified, args.original, args.out, args.threshold, args.recipes, args.original_revision, args.modified_revision, args.seed)
    summary = report["summary"]
    print(f"{summary['assessment']}: {len(summary['changed_set'])}/{summary['matched_tensors']} tensors changed")
    print(f"Nearest recipe: {report['recipe_matching']['nearest_recipe']}; {len(report['recipe_matching']['violations'])} violations")
    if summary["min_first_singular_energy_share"] is not None:
        print(f"Minimum first-value energy share: {summary['min_first_singular_energy_share']:.9f}")
        cosine = summary["direction_agreement"]["min_cosine"]
        print(f"Minimum direction cosine: {cosine:.9f}" if cosine is not None else "Median direction is undefined")
    print(f"Report: {args.out}")


def run_null(args):
    """Keep the long control run available as small, independent steps."""
    from .nulls import make_null
    import torch

    torch.set_num_threads(args.threads)

    if args.batch_index is not None and args.step != "activations":
        raise ValueError("--batch-index applies only to the activations step")
    result = make_null(args.model, args.out_dir, args.step, args.batch_index, args.prompts)
    if args.step == "compare":
        for name, summary in result.items():
            print(f"{name}: {summary['assessment']}; {len(summary['changed_set'])} changed tensors; energy share {summary['min_first_singular_energy_share']}; cosine {summary['direction_agreement']['min_cosine']}")
    else:
        print(f"Null step complete: {args.step}")
        if args.step == "activations":
            print(json.dumps(result, sort_keys=True))


def main(argv=None):
    """Bound CPU threads before a command gets near checkpoint arithmetic."""
    parser = argparse.ArgumentParser(prog="audit")
    subparsers = parser.add_subparsers(dest="command", required=True)
    register_commands(subparsers)
    args = parser.parse_args(argv)
    try:
        args.handler(args)
    except (ValueError, OSError, KeyError) as error:
        print(f"audit: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
