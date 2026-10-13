# library.py -- Run reference methods in order and collect measured envelopes.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  add serial runs, retained-copy budgets, and a summary table.
"""Run the recipe library, or show its storage plan without loading a checkpoint."""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

from audit.weights import ROOT, TensorStore, digest, read_json, recipe_table, resolve_checkpoint, write_json
from .common import METHODS, Resources, log


def envelope(report, card):
    """Derive pass lines from one reference, retaining the measurement tolerances."""
    rows = report["tensors"]
    if report["original_only"] or report["modified_only"] or any(row["status"] != "ok" for row in rows.values()):
        raise ValueError("reference comparison has structural or nonfinite differences")
    changed = [row for row in rows.values() if row["changed"]]
    matrices = [row for row in rows.values() if "row_norms" in row]
    preserved = all(row["row_norms"]["preserved_equal"] for row in matrices) if matrices else None
    agreement = report["summary"]["direction_agreement"]
    cosines = [value for value in (agreement["min_cosine"], agreement["cross_kind_min_cosine"]) if value is not None]
    status = "no measurable change"
    if changed:
        status = "measured" if report["summary"]["min_first_singular_energy_share"] is not None and cosines else "undefined measurements"
    return {"status": status, "method": card["method"],
            "base": card["base"], "changed_kinds": report["summary"]["changed_kinds"],
            "changed_tensors": report["summary"]["changed_set"],
            "first_energy_min": report["summary"]["min_first_singular_energy_share"],
            "direction_cosine_min": min(cosines) if cosines else None,
            "allow_unchanged_projections": card["method"]["name"] not in {"single-projection", "norm-preserving"},
            "base_shards_sha256": report["original"]["shards_sha256"],
            "row_norms_preserved": preserved, "unchanged_relative_max": report["threshold"],
            "row_norm_tolerance": {"rtol": 1e-5, "atol": 1e-7},
            "card_sha256": digest(Path(card["parameters"]["out"]) / "recipe-card.json"),
            "scope": "One base revision and one run; these are calibration observations, not family-wide confidence bounds."}


def summarize(results, destination):
    """Write measured rows and explicit skips; missing runs never become zeros."""
    lines = ["# Reference recipe measurements", "", "Each row compares a completed reference copy with its recorded base revision.",
             "The pass lines in `envelopes.json` describe this run. Repeated runs are needed to estimate their variation.", "",
             "| Method | Changed kinds | Minimum first-value energy share | Minimum direction cosine | Row norms preserved |",
             "| --- | --- | ---: | ---: | --- |"]
    for method in METHODS:
        path = results / (method + ".envelope.json")
        if not path.exists():
            lines.append(f"| {method} | pending | — | — | — |")
            continue
        record = read_json(path)
        if record["status"] == "skipped":
            lines.append(f"| {method} | {record['reason']} | — | — | — |")
            continue
        share, cosine = record["first_energy_min"], record["direction_cosine_min"]
        share_text = "—" if share is None else f"{share:.9f}"
        cosine_text = "—" if cosine is None else f"{cosine:.9f}"
        norms = {True: "yes", False: "no", None: "undefined"}[record["row_norms_preserved"]]
        kinds = ", ".join(record["changed_kinds"]) or "none"
        lines.append(f"| {method} | {kinds} | {share_text} | {cosine_text} | {norms} |")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text("\n".join(lines) + "\n")


def checked_call(command, logfile):
    """Save a complete log while showing the child process's step lines."""
    with logfile.open("w") as output:
        process = subprocess.Popen(["nice", "-n", "19", *command], cwd=ROOT,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in process.stdout:
            output.write(line)
            output.flush()
            print(line, end="", flush=True)
        code = process.wait()
        if code:
            raise RuntimeError(f"recipe command exited {code}; see {logfile}")


def main(argv=None):
    """Keep each method in a fresh process so one checkpoint leaves before the next."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", default="Qwen/Qwen3-8B")
    parser.add_argument("--revision", default="main")
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--run-dir", default=str(ROOT / "data/library/qwen3-8b"))
    parser.add_argument("--results", default=str(ROOT / "results/library/qwen3-8b"))
    parser.add_argument("--summary", default=str(ROOT / "docs/library-qwen3-8b.md"))
    parser.add_argument("--methods", nargs="+", choices=METHODS, default=list(METHODS))
    parser.add_argument("--expected-base-gb", type=float, default=16)
    parser.add_argument("--storage-budget-gb", type=float, default=256)
    parser.add_argument("--dry-run", action="store_true")
    args, extra = parser.parse_known_args(argv)
    if args.expected_base_gb <= 0 or args.storage_budget_gb <= 0:
        parser.error("storage estimates and budgets must be positive")
    # Include float32 projections, a repair intermediate, and the downloaded base.
    estimate = args.expected_base_gb * (2 + sum(2 if method in {"single-projection", "single-projection-selected", "norm-preserving", "projection-plus-healing"} else 1 for method in args.methods))
    free = shutil.disk_usage(ROOT).free / 1e9
    log(f"Storage plan: at most {estimate:.1f} GB; budget {args.storage_budget_gb:.1f} GB; free {free:.1f} GB")
    log("Retain completed copies until their cards and reports are accepted; remove only the repair intermediate automatically")
    if args.dry_run:
        for method in args.methods:
            log(f"Planned method: {method}")
        return 0
    if estimate > args.storage_budget_gb or estimate + 12 > free:
        raise ValueError("storage plan exceeds the declared budget or disk headroom")
    runs, results = Path(args.run_dir).resolve(), Path(args.results).resolve()
    runs.mkdir(parents=True, exist_ok=True)
    results.mkdir(parents=True, exist_ok=True)
    with Resources("cpu"):
        directory, provenance = resolve_checkpoint(args.base, args.revision)
        store = TensorStore(directory)
        actual_gb = sum(path.stat().st_size for path in set(store.names.values())) / 1e9
        actual_estimate = estimate * actual_gb / args.expected_base_gb
        free = shutil.disk_usage(ROOT).free / 1e9
        if actual_estimate > args.storage_budget_gb or actual_estimate + 12 > free:
            raise ValueError("actual checkpoint size exceeds the storage plan or disk headroom")
        estimate = actual_estimate
        log(f"Storage plan from base shards: {estimate:.1f} GB")
    manifest = {"base": {"repo": args.base, **provenance}, "storage_budget_gb": args.storage_budget_gb,
                "estimated_peak_gb": estimate, "methods": args.methods, "copies": {},
                "retention": "Keep completed copies until acceptance; only the repair intermediate is deleted by its runner."}
    # A new directory binds all results to one base; resume completed runs by their cards.
    previous = results / "manifest.json"
    if previous.exists() and read_json(previous)["base"] != manifest["base"]:
        raise ValueError("library results belong to a different base revision")
    for method in args.methods:
        out = runs / method
        marker = out / "done.json"
        if not marker.exists():
            command = [sys.executable, "-m", "audit.recipes." + method.replace("-", "_"),
                       "--base", str(directory), "--revision", provenance["revision"] or args.revision,
                       "--out", str(out), "--device", args.device, *extra]
            if provenance["revision"] is not None:
                command.extend(["--base-repo", args.base, "--base-revision", provenance["revision"]])
            log(f"Run reference: {method}")
            checked_call(command, results / (method + ".log"))
        card = read_json(out / "recipe-card.json")
        if read_json(marker)["card_sha256"] != digest(out / "recipe-card.json"):
            raise ValueError("completion card checksum differs")
        if card["base"]["revision"] != provenance["revision"] or card["base"]["source"] != provenance["source"]:
            raise ValueError("completed recipe belongs to a different base")
        if card["status"] == "skipped":
            record = {"status": "skipped", "reason": card["reason"], "method": card["method"]}
            write_json(results / (method + ".json"), record)
        else:
            report_path = results / (method + ".json")
            checked_call([sys.executable, "-m", "audit.recipes.measure", "--base", str(directory),
                          "--derived", str(out), "--out", str(report_path)], results / (method + ".compare.log"))
            record = envelope(read_json(report_path), card)
        write_json(results / (method + ".envelope.json"), record)
        manifest["copies"][method] = {"directory": str(out), "card_sha256": digest(out / "recipe-card.json")}
        write_json(previous, manifest)
        summarize(results, Path(args.summary))
    table = {"tensor_kinds": recipe_table()["tensor_kinds"]}
    table.update({method: read_json(results / (method + ".envelope.json")) for method in args.methods})
    write_json(results / "envelopes.json", table)
    log(f"Library table: {args.summary}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
