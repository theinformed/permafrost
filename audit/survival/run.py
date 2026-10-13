# run.py -- Supervise serial serving, recipes, probes, and clean comparisons.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  stop child groups on low memory and save partial results.
"""Run on staged local checkpoints; checkpoint downloads are outside this harness."""

import argparse
import contextlib
import json
import os
import shutil
import signal
import socket
import subprocess
import sys
import threading
import time
import uuid
from pathlib import Path

import requests

from .probe import REGISTRY, entry_digest, load_entry, probe, survival, write_json

ROOT = Path(__file__).resolve().parents[2]
METHODS = ("single-projection", "single-projection-selected", "heretic-directional",
           "heretic-arbitrary-rank", "norm-preserving", "projection-plus-healing", "plain-lora")


def log(message):
    """Show one line per operation while the full child output goes to disk."""
    print(f"[{time.strftime('%H:%M:%S', time.gmtime())}] {message}", flush=True)


def available_memory():
    """Use available pages, including reclaimable cache, for the host floor."""
    for line in Path("/proc/meminfo").read_text().splitlines():
        if line.startswith("MemAvailable:"):
            return int(line.split()[1]) * 1024
    raise RuntimeError("host available memory is unknown")


def stop_group(process):
    """Reap the launcher and its workers before another checkpoint can start."""
    try:
        os.killpg(process.pid, signal.SIGTERM)
    except ProcessLookupError:
        pass
    try:
        process.wait(timeout=10)
    except subprocess.TimeoutExpired:
        pass
    # A launcher can exit before its worker processes; drain the entire group.
    try:
        os.killpg(process.pid, signal.SIGKILL)
    except ProcessLookupError:
        pass
    process.wait(timeout=10)


class Supervisor:
    """Watch the host and own every child process started by this run."""

    def __init__(self, step_hours=6):
        self.process = None
        self.failed = threading.Event()
        self.finished = threading.Event()
        self.step_hours = step_hours
        self.thread = None

    def check(self):
        """Stop before starting more work after a low-memory event."""
        if self.failed.is_set() or available_memory() < 12 * 1024**3:
            raise MemoryError("host available memory fell below 12 GB")

    def __enter__(self):
        """Begin watching before a child can load checkpoint files."""
        self.check()

        def watch():
            """Kill the child group, rather than leaving a server orphaned."""
            while not self.finished.wait(1):
                try:
                    self.check()
                except (MemoryError, OSError, RuntimeError):
                    self.failed.set()
                    if self.process is not None:
                        try:
                            os.killpg(self.process.pid, signal.SIGKILL)
                        except ProcessLookupError:
                            pass
                    return

        self.thread = threading.Thread(target=watch, daemon=True)
        self.thread.start()
        return self

    def __exit__(self, *unused):
        """Reap children on normal exits, interrupts, and failed probes."""
        try:
            if self.process is not None:
                stop_group(self.process)
        finally:
            self.finished.set()
            self.thread.join()

    @contextlib.contextmanager
    def child(self, command, logfile):
        """Give each operation its own process group and a bounded log file."""
        if self.process is not None:
            raise RuntimeError("another child is still active")
        self.check()
        logfile = Path(logfile)
        logfile.parent.mkdir(parents=True, exist_ok=True)
        environment = dict(os.environ, OMP_NUM_THREADS="1", MKL_NUM_THREADS="1",
                           HF_HUB_OFFLINE="1", TRANSFORMERS_OFFLINE="1")
        self.process = subprocess.Popen(["nice", "-n", "19", *command], cwd=ROOT,
                                        env=environment, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                        start_new_session=True)

        def capture():
            """Drain output after the log cap; checkpoint files keep their own budget."""
            left = 64 * 1024**2
            with logfile.open("wb") as stream:
                for block in iter(lambda: self.process.stdout.read(65536), b""):
                    stream.write(block[:left])
                    left = max(0, left - len(block))

        reader = threading.Thread(target=capture, daemon=True)
        reader.start()
        try:
            yield self.process
        finally:
            stop_group(self.process)
            reader.join(timeout=10)
            self.process.stdout.close()
            self.process = None

    def run(self, command, logfile):
        """Wait without repeated status requests; the watchdog runs beside the child."""
        with self.child(command, logfile) as process:
            deadline = time.monotonic() + self.step_hours * 3600
            while process.poll() is None:
                self.check()
                if time.monotonic() > deadline:
                    raise TimeoutError("step exceeded its declared time budget")
                self.finished.wait(0.5)
            self.check()
            if process.returncode:
                raise RuntimeError(f"child exited {process.returncode}; see {logfile}")


def server_command(directory, model, port):
    """Fix serving to a quarter of one device and one local checkpoint."""
    return [sys.executable, "-m", "vllm.entrypoints.openai.api_server", "--model", str(directory),
            "--served-model-name", model, "--host", "127.0.0.1", "--port", str(port),
            "--gpu-memory-utilization", "0.25", "--tensor-parallel-size", "1",
            "--max-num-seqs", "1", "--max-model-len", "2048", "--enforce-eager",
            "--generation-config", "vllm"]


def served_probe(supervisor, directory, entry, port, logfile, max_tokens):
    """Verify the fresh server identity before sending either prompt."""
    model = "survival-" + uuid.uuid4().hex
    with socket.socket() as seat:
        seat.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        seat.bind(("127.0.0.1", port))
    endpoint = f"http://127.0.0.1:{port}/v1"
    with supervisor.child(server_command(directory, model, port), logfile) as process:
        deadline = time.monotonic() + 600
        with requests.Session() as session:
            session.trust_env = False
            while True:
                supervisor.check()
                if process.poll() is not None:
                    raise RuntimeError(f"server exited before readiness; see {logfile}")
                if time.monotonic() > deadline:
                    raise TimeoutError("server did not become ready within 10 minutes")
                try:
                    response = session.get(endpoint + "/models", timeout=2, allow_redirects=False)
                    if response.status_code == 200:
                        names = [item["id"] for item in response.json()["data"]]
                        if names != [model]:
                            raise ValueError("server model identity differs")
                        break
                except requests.ConnectionError:
                    pass
                except requests.Timeout:
                    pass
                supervisor.finished.wait(0.5)
        result = probe(entry, endpoint, model, max_tokens)
        supervisor.check()
        return result


def input_identity(directory):
    """Record local shard hashes without resolving a remote repository name."""
    from audit.weights import TensorStore, digest
    directory = Path(directory).resolve()
    if not directory.is_dir() or not (directory / "config.json").is_file():
        raise ValueError("input must be a staged local checkpoint directory")
    return {"directory": str(directory), "config_sha256": digest(directory / "config.json"),
            "shards_sha256": TensorStore(directory).provenance(),
            "origin": json.loads((directory / "survival-origin.json").read_text())
            if (directory / "survival-origin.json").exists() else None}


def validate_inputs(entry, identities):
    """Match local weights to published hashes and bind adapter merges to their base."""
    expected = entry.get("verified_files")
    if expected is None:
        raise ValueError("registry has no verified weight identities")
    if identities["clean"]["shards_sha256"] != expected["clean"]["weights"]:
        raise ValueError("clean shards differ from the pinned base revision")
    if entry["artifact_kind"] == "full-checkpoint":
        if identities["published"]["shards_sha256"] != expected["published"]["weights"]:
            raise ValueError("published shards differ from the pinned source revision")
    elif entry["artifact_kind"] == "adapter":
        origin = identities["published"]["origin"]
        if (not origin or origin["repo"] != entry["repo"] or origin["revision"] != entry["revision"]
                or origin["base_shards_sha256"] != identities["clean"]["shards_sha256"]
                or origin["merged_shards_sha256"] != identities["published"]["shards_sha256"]
                or origin["adapter_sha256"] != expected["published"]["weights"]["adapter_model.safetensors"]):
            raise ValueError("adapter merge origin differs from the pinned source or clean base")
    else:
        raise ValueError("unsupported published artifact kind")


def plan(args):
    """Declare retained copies and a disk budget before any checkpoint is loaded."""
    sizes = []
    for directory in (args.published, args.clean):
        if not directory.is_dir() or not (directory / "config.json").exists():
            raise ValueError("published and clean inputs must be staged local checkpoints")
        sizes.append(sum(path.stat().st_size for path in directory.glob("*.safetensors")))
    if not all(sizes):
        raise ValueError("staged input has no safetensors weights")
    # Float32 projections and the repair intermediate can each double a copy.
    projected = sum(2 if method in {"single-projection", "single-projection-selected", "norm-preserving", "projection-plus-healing"}
                    else 1 for method in args.methods)
    peak = sum(sizes) * (projected + 2) / 1e9
    free = shutil.disk_usage(args.work.parent if args.work.parent.exists() else ROOT).free / 1e9
    log(f"Storage: up to {peak:.1f} GB additional; budget {args.storage_budget_gb:.1f} GB; free {free:.1f} GB")
    log("Keep completed copies for review; remove this run directory explicitly after accepting its reports")
    return {"estimated_peak_gb": peak, "storage_budget_gb": args.storage_budget_gb,
            "free_gb": free, "retention": "Keep this run until its reports are accepted, then remove its named work directory."}


def execute(args, entry, storage):
    """Save every completed step so a failed run cannot look like a negative result."""
    from .detect import card
    if args.record.exists() or args.work.exists():
        raise ValueError("run outputs already exist; choose a fresh work directory and result file")
    if storage["estimated_peak_gb"] > args.storage_budget_gb or storage["estimated_peak_gb"] + 12 > storage["free_gb"]:
        raise ValueError("storage estimate exceeds budget or disk headroom")
    args.work.mkdir(parents=True)
    record = {"schema_version": 1, "entry": entry, "entry_sha256": entry_digest(entry), "status": "running",
              "inputs": {"published": str(args.published), "clean": str(args.clean)}, "storage": storage,
              "recipes": {}, "resources": {"gpu_fraction": 0.25, "host_floor_gb": 12},
              "source_scope": "Original shard hashes match the pinned source metadata. Adapter merges carry their "
                              "source adapter and clean-base hashes. Tokenizer and configuration files are locally hashed."}

    def save():
        """Keep the JSON and reading card in agreement, including failed runs."""
        write_json(args.record, record)
        card(record, args.card)

    try:
        with Supervisor(args.step_hours) as supervisor:
            record["input_identity"] = {name: input_identity(path) for name, path in record["inputs"].items()}
            validate_inputs(entry, record["input_identity"])
            save()
            log("Serve the published checkpoint for the BEFORE control")
            record["before"] = served_probe(supervisor, args.published, entry, args.port, args.work / "before.log", args.max_tokens)
            save()
            if not record["before"]["valid_control"]:
                record.update(status="invalid-before", reason="documented behavior or matched negative control did not reproduce")
                save()
                return 2
            for method in args.methods:
                log(f"Recipe: {method}")
                row = {"status": "running", "survives": None}
                record["recipes"][method] = row
                save()
                for name in ("published", "clean"):
                    destination = args.work / method / name
                    row[name + "_copy"] = str(destination)
                    command = [sys.executable, "-m", "audit.recipes." + method.replace("-", "_"),
                               "--base", record["inputs"][name], "--out", str(destination),
                               "--device", "cuda:0", *args.recipe_arg]
                    supervisor.run(command, args.work / (method + "-" + name + ".log"))
                    info = json.loads((destination / "recipe-card.json").read_text())
                    if info["status"] == "skipped":
                        row.update(status="skipped", reason=info["reason"])
                        break
                if row["status"] == "skipped":
                    save()
                    continue
                log(f"Serve the AFTER copy: {method}")
                row["after"] = served_probe(supervisor, row["published_copy"], entry, args.port,
                                             args.work / (method + "-after.log"), args.max_tokens)
                row["survives"] = survival(record["before"], row["after"])
                save()
                log(f"Compare both recipe pairs: {method}")
                supervisor.run([sys.executable, "-m", "audit.survival.detect", "--record", str(args.record),
                                "--method", method, "--card", str(args.card)], args.work / (method + "-detect.log"))
                measured = json.loads(args.record.read_text())
                row["detection"] = measured["recipes"][method]["detection"]
                row["status"] = "complete"
                save()
            record["status"] = "complete"
            save()
    except BaseException as error:
        record.update(status="failed", error=f"{type(error).__name__}: {error}")
        for row in record["recipes"].values():
            if row["status"] == "running":
                row["status"] = "failed"
        save()
        raise
    log(f"Measurement complete: {args.record}")
    return 0


def main(argv=None):
    """Plan or execute one entry with explicit staged inputs and bounded retention."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--entry", required=True)
    parser.add_argument("--registry", type=Path, default=REGISTRY)
    parser.add_argument("--published", type=Path, required=True)
    parser.add_argument("--clean", type=Path, required=True)
    parser.add_argument("--work", type=Path)
    parser.add_argument("--record", type=Path)
    parser.add_argument("--card", type=Path)
    parser.add_argument("--methods", nargs="+", choices=METHODS, default=list(METHODS))
    parser.add_argument("--recipe-arg", action="append", default=[], help="One extra recipe argument, using = for flags")
    parser.add_argument("--storage-budget-gb", type=float, default=256)
    parser.add_argument("--step-hours", type=float, default=6)
    parser.add_argument("--max-tokens", type=int, default=256)
    parser.add_argument("--port", type=int, default=18920)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    entry = load_entry(args.entry, args.registry)
    for name, default in (("work", ROOT / "data/survival" / entry["id"]),
                          ("record", ROOT / "results/survival" / (entry["id"] + ".json")),
                          ("card", ROOT / "docs/cards" / ("survival-" + entry["id"] + ".md"))):
        setattr(args, name, (getattr(args, name) or default).resolve())
    args.published, args.clean = args.published.resolve(), args.clean.resolve()
    if not 1024 <= args.port <= 65535 or not 0 < args.step_hours <= 24 or not 0 < args.storage_budget_gb <= 4096:
        parser.error("port, time, or storage budget is outside bounds")
    if not 1 <= args.max_tokens <= 2048 or len(set(args.methods)) != len(args.methods):
        parser.error("invalid token budget or repeated methods")
    # Resource, base, and output flags belong to the supervisor, not extra arguments.
    allowed = {"--prompts", "--train-prompts", "--heldout-prompts", "--max-new-tokens", "--max-length",
               "--pairs", "--rank", "--learning-rate", "--seed", "--training-data"}
    if any("=" not in value or value.split("=", 1)[0] not in allowed for value in args.recipe_arg):
        parser.error("extra recipe settings must be allowed --name=value arguments")
    os.nice(max(0, 19 - os.getpriority(os.PRIO_PROCESS, 0)))
    storage = plan(args)
    if args.dry_run:
        for method in args.methods:
            log(f"Planned: {method}, published and clean copies, AFTER probe, weight comparison")
        return 0
    return execute(args, entry, storage)


if __name__ == "__main__":
    def interrupted(signum, frame):
        """Turn a termination signal into the same cleanup path as an interrupt."""
        raise KeyboardInterrupt(f"signal {signum}")
    signal.signal(signal.SIGTERM, interrupted)
    raise SystemExit(main())
