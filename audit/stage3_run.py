# stage3_run.py -- Record answers and own the short-lived serving process.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  add fixed decoding, local provenance, and server cleanup.
"""Run one pass against a local HTTP server, optionally starting it here."""

import argparse
import importlib.metadata
import json
import os
import signal
import socket
import subprocess
import sys
import time
from pathlib import Path
from urllib.error import URLError
from urllib.parse import urlsplit

from .stage3_common import (MAX_FILE, SETTINGS, SYSTEM, check_memory, fingerprint,
                            http_json, read_rows, watchdog, write_json)


def local_endpoint(value):
    """Keep answers on the serving host, including when a URL is supplied by hand."""
    parsed = urlsplit(value)
    if parsed.scheme != "http" or parsed.hostname not in ("127.0.0.1", "localhost", "::1"):
        raise ValueError("answer endpoint must be local HTTP")
    return value.rstrip("/")


def checkpoint_provenance(directory, revision):
    """Hash small checkpoint metadata; weight downloads are outside this runner."""
    directory = Path(directory).resolve()
    if not directory.is_dir() or not (directory / "config.json").is_file():
        raise ValueError("serve needs an existing local checkpoint directory with config.json")
    metadata = {}
    for name in ("config.json", "tokenizer_config.json", "generation_config.json", "chat_template.jinja", "model.safetensors.index.json"):
        path = directory / name
        if path.exists():
            if path.stat().st_size > MAX_FILE:
                raise ValueError("checkpoint metadata exceeds 64 MiB")
            metadata[name] = fingerprint(path.read_text())
    versions = {}
    for package in ("vllm", "torch", "transformers"):
        try:
            versions[package] = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            versions[package] = None
    return {"directory": str(directory), "revision": revision, "metadata_sha256": metadata,
            "python": sys.version, "packages": versions, "server_command": server_command(directory)}


def run_pass(prompts, out, label, endpoint, provenance=None):
    """Flush each answer so a stopped pass keeps its completed observations."""
    rows = read_rows(prompts)
    endpoint = local_endpoint(endpoint)
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    settings = {**SETTINGS, "system": SYSTEM}
    manifest = {"label": label, "prompt_sha256": fingerprint(rows), "settings": settings,
                "expected_answers": len(rows), "checkpoint": provenance, "complete": False}
    with out.open("x") as stream:
        write_json(str(out) + ".manifest.json", manifest)
        print(f"Pass {label}: {len(rows):,} prompts", flush=True)
        total = 0
        for index, row in enumerate(rows, 1):
            check_memory()
            body = {**SETTINGS, "messages": [{"role": "system", "content": SYSTEM},
                                              {"role": "user", "content": row["text"]}]}
            response = http_json(endpoint + "/chat/completions", body, timeout=120)
            choices = response["choices"]
            if len(choices) != 1 or not isinstance(choices[0]["message"].get("content"), str):
                raise ValueError("server returned no single text answer")
            answer = choices[0]["message"]["content"]
            if len(answer.encode()) > 32 * 1024:
                raise ValueError("answer exceeds 32 KiB")
            record = {**row, "answer": answer, "label": label,
                      "prompt_sha256": fingerprint(row), "settings_sha256": fingerprint(settings),
                      "finish_reason": choices[0].get("finish_reason"), "usage": response.get("usage")}
            line = json.dumps(record, ensure_ascii=False) + "\n"
            total += len(line.encode())
            if total > MAX_FILE:
                raise ValueError("answer file exceeds 64 MiB")
            stream.write(line)
            stream.flush()
            if index % 100 == 0 or index == len(rows):
                print(f"Pass {label}: {index:,}/{len(rows):,} answers, {total / 1e6:.1f} MB", flush=True)
    manifest["complete"] = True
    write_json(str(out) + ".manifest.json", manifest)
    return manifest


def server_command(directory):
    """Fix the serving budget and disable checkpoint-specific decoding defaults."""
    return ["nice", "-n", "19", sys.executable, "-m", "vllm.entrypoints.openai.api_server",
            "--model", str(directory), "--served-model-name", "audit", "--host", "127.0.0.1",
            "--port", "8010", "--gpu-memory-utilization", "0.25", "--max-model-len", "8192",
            "--max-num-seqs", "8", "--seed", "0", "--generation-config", "vllm", "--enforce-eager"]


def stop_server(process):
    """Stop only our process group, including any serving workers it started."""
    try:
        os.killpg(process.pid, signal.SIGTERM)
    except ProcessLookupError:
        return
    try:
        process.wait(timeout=15)
    except subprocess.TimeoutExpired:
        os.killpg(process.pid, signal.SIGKILL)
        process.wait(timeout=5)


def serve_pass(args):
    """Own startup and teardown; an occupied port belongs to somebody else."""
    provenance = checkpoint_provenance(args.model, args.revision)
    if args.out.exists():
        raise FileExistsError(args.out)
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 8010))
    args.log.parent.mkdir(parents=True, exist_ok=True)
    environment = dict(os.environ, HF_HUB_OFFLINE="1", TRANSFORMERS_OFFLINE="1")
    print(f"Server: starting one checkpoint; available RAM {check_memory() / 1e9:.1f} GB", flush=True)
    with args.log.open("x") as log:
        process = subprocess.Popen(server_command(provenance["directory"]), stdout=log, stderr=log,
                                   start_new_session=True, env=environment)
        try:
            deadline = time.monotonic() + args.startup_minutes * 60
            while True:
                check_memory()
                if process.poll() is not None:
                    raise RuntimeError("server exited during startup; see its log")
                if time.monotonic() > deadline:
                    raise TimeoutError("server startup deadline passed")
                if args.log.stat().st_size > MAX_FILE:
                    raise ValueError("server log exceeds 64 MiB")
                try:
                    reply = http_json("http://127.0.0.1:8010/v1/models", timeout=2)
                    if not any(item["id"] == "audit" for item in reply["data"]):
                        raise ValueError("server did not advertise audit")
                    break
                except URLError:
                    time.sleep(1)
            print("Server: ready on local port 8010", flush=True)
            return run_pass(args.prompts, args.out, args.label, "http://127.0.0.1:8010/v1", provenance)
        finally:
            stop_server(process)
            print("Server: stopped", flush=True)


def main():
    """Run a full or repeat pass, using the same system text and decoding settings."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prompts", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--label", choices=("original", "modified", "repeat"), required=True)
    parser.add_argument("--endpoint", default="http://127.0.0.1:8010/v1")
    parser.add_argument("--serve", action="store_true")
    parser.add_argument("--model", type=Path)
    parser.add_argument("--revision")
    parser.add_argument("--log", type=Path)
    parser.add_argument("--startup-minutes", type=float, default=10)
    args = parser.parse_args()
    if args.serve and (not args.model or not args.revision or not args.log):
        parser.error("--serve requires --model, --revision, and --log")

    def interrupted(signum, frame):
        """Leave the server cleanup to its owner when the memory watch trips."""
        raise SystemExit(f"run interrupted by signal {signum}")

    signal.signal(signal.SIGTERM, interrupted)
    stopped = watchdog([args.log] if args.serve else [])
    try:
        serve_pass(args) if args.serve else run_pass(args.prompts, args.out, args.label, args.endpoint)
    finally:
        stopped.set()


if __name__ == "__main__":
    main()
