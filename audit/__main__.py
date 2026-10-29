# __main__.py -- Offer the catalog, summary, and metadata comparison commands.
# Created by LT Sean Egan, PhD 2026-10-13
# Modified: SDE 2026-10-13  expose the first two audit stages.
# Modified: SDE 2026-10-13  add streamed weight comparison and CPU null controls.
# Modified: SDE 2026-10-13  rerun metadata comparisons at saved revisions.
# Modified: SDE 2026-10-29  add metadata-reclassify for saved reports.
import argparse
import json
import sys
from pathlib import Path

from .inventory import inventory, read_rows, summary


def main():
    """Keep command errors short and leave detailed evidence in the reports."""
    parser = argparse.ArgumentParser(description="Audit checkpoint metadata and tensor differences.")
    commands = parser.add_subparsers(dest="command", required=True)
    try:
        from .weights_cli import register_commands
    except ModuleNotFoundError as error:
        if error.name != "audit.weights_cli":
            raise
    else:
        register_commands(commands)
    catalog = commands.add_parser("inventory")
    catalog.add_argument("--terms", default="abliterated,uncensored,heretic,abliteration")
    catalog.add_argument("--out", default="data/inventory.jsonl")
    catalog.add_argument("--limit", type=int)
    catalog.add_argument("--delay", type=float, default=0.2)
    catalog.add_argument("--max-seconds", type=float, default=45,
                         help="stop between calls and resume on the next invocation")
    counts = commands.add_parser("inventory-summary")
    counts.add_argument("--input", default="data/inventory.jsonl")
    diff = commands.add_parser("metadata-diff")
    diff.add_argument("--repo", required=True)
    diff.add_argument("--original", required=True)
    diff.add_argument("--out", required=True)
    diff.add_argument("--delay", type=float, default=0.2)
    diff.add_argument("--from-evidence", help="reuse saved revisions and checksums, reading cached small files first")
    diff.add_argument("--cache-dry-run", action="store_true",
                      help="show which cached revisions would be replaced")
    again = commands.add_parser("metadata-reclassify")
    again.add_argument("--report", required=True, help="a saved metadata-diff report")
    again.add_argument("--out", help="write here instead of over the report")
    again.add_argument("--later-revisions", action="store_true",
                       help="read the original repository's later commits to explain a changed template")
    again.add_argument("--delay", type=float, default=0.2)
    again.set_defaults(handler=lambda args: __import__("audit.metadata", fromlist=["metadata_reclassify"]).metadata_reclassify(args))
    args = parser.parse_args()
    if getattr(args, "delay", 0) < 0 or getattr(args, "limit", None) is not None and args.limit < 1:
        parser.error("delay must be nonnegative and limit must be positive")
    if getattr(args, "max_seconds", 45) <= 15:
        parser.error("max-seconds must allow at least one catalog call (over 15)")
    try:
        if hasattr(args, "handler"):
            args.handler(args)
        elif args.command == "inventory":
            inventory(args)
        elif args.command == "inventory-summary":
            ancestry_path = Path(args.input).with_suffix(".ancestry.json")
            ancestry = json.loads(ancestry_path.read_text()).values() if ancestry_path.exists() else ()
            print(summary(read_rows(args.input), ancestry))
        else:
            from .metadata import metadata_diff
            metadata_diff(args)
    except Exception as error:
        print(f"audit: {type(error).__name__}: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
