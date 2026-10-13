# common.py -- Share resource checks and checkpoint bookkeeping across recipes.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  bound memory use and record completed reference copies.
"""Small helpers for the recipe runners and their provenance cards."""

import argparse
import gc
import importlib.metadata
import os
import re
import threading
from datetime import datetime, timezone
from pathlib import Path

import torch

from audit.weights import ROOT, TensorStore, digest, resolve_checkpoint, write_json

METHODS = ("single-projection", "single-projection-selected", "heretic-directional",
           "heretic-arbitrary-rank", "norm-preserving", "projection-plus-healing", "plain-lora")
TOOL_VERSION = "1.3.0"


def log(message):
    """Print a step while it still matters, including when output is redirected."""
    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S')}] {message}", flush=True)


def available_memory():
    """Read available host memory; free pages alone miss the reclaimable cache."""
    for line in Path("/proc/meminfo").read_text().splitlines():
        if line.startswith("MemAvailable:"):
            return int(line.split()[1]) * 1024
    raise RuntimeError("available host memory is unknown")


class Resources:
    """Cap device allocations and stop the process when host memory gets tight."""

    def __init__(self, device):
        self.device = torch.device(device)
        self.stop = threading.Event()
        self.thread = None
        self.limit = 12 * 1024**3
        self.gpu_bytes = None

    def check(self):
        """Keep the memory floor the same on CPU and accelerator runs."""
        if available_memory() < self.limit:
            raise MemoryError("host available memory fell below 12 GB")

    def __enter__(self):
        """Start the watchdog before any checkpoint is loaded."""
        os.nice(max(0, 19 - os.getpriority(os.PRIO_PROCESS, 0)))
        torch.set_num_threads(1)
        self.check()
        if self.device.type == "cuda":
            if not torch.cuda.is_available():
                raise ValueError("requested device is unavailable")
            index = self.device.index or 0
            torch.cuda.set_device(index)
            torch.cuda.set_per_process_memory_fraction(0.25, index)
            self.gpu_bytes = int(torch.cuda.get_device_properties(index).total_memory * 0.25)
        elif self.device.type != "cpu":
            raise ValueError("device must be cpu or cuda")

        def watch():
            """Exit the whole process; a worker exception would leave training alive."""
            while not self.stop.wait(1):
                try:
                    self.check()
                except (MemoryError, OSError, RuntimeError) as error:
                    log(str(error))
                    os._exit(75)

        self.thread = threading.Thread(target=watch, daemon=True)
        self.thread.start()
        log(f"Resources: 12 GB host floor; device {self.device}; GPU fraction 0.25")
        return self

    def __exit__(self, *unused):
        """Stop the watcher when a runner returns normally or raises."""
        self.stop.set()
        self.thread.join()


def parser(method):
    """Give every runner the same core arguments and small-test settings."""
    result = argparse.ArgumentParser(description=f"Build the {method} reference copy")
    result.add_argument("--base", required=True)
    result.add_argument("--revision", default="main")
    result.add_argument("--base-repo", help="Original repository when --base is a local copy")
    result.add_argument("--base-revision", help="Original resolved revision when --base is local")
    result.add_argument("--out", required=True)
    result.add_argument("--device", default="cuda:0")
    result.add_argument("--prompts", default=str(ROOT / "data/prompts"))
    result.add_argument("--train-prompts", type=int, default=24)
    result.add_argument("--heldout-prompts", type=int, default=8)
    result.add_argument("--max-new-tokens", type=int, default=64)
    result.add_argument("--max-length", type=int, default=256)
    result.add_argument("--pairs", type=int, default=256)
    result.add_argument("--rank", type=int, default=8)
    result.add_argument("--learning-rate", type=float, default=2e-5)
    result.add_argument("--seed", type=int, default=17)
    result.add_argument("--training-data", help="JSONL with prompt/chosen/rejected or prompt/response")
    result.add_argument("--check-imports", action="store_true", help="Check optional packages without loading weights")
    return result


def validate(args):
    """Reject small-test settings that would silently empty a data split."""
    for name in ("train_prompts", "heldout_prompts", "max_new_tokens", "max_length", "pairs", "rank"):
        if getattr(args, name) < 1:
            raise ValueError(f"{name} must be positive")
    if args.train_prompts + args.heldout_prompts > 32:
        raise ValueError("training and held-out prompts must fit the 32-prompt lists")
    if args.learning_rate <= 0:
        raise ValueError("learning rate must be positive")


def prepare(args, method):
    """Refuse mixed or half-finished outputs rather than blessing old shards."""
    validate(args)
    out = Path(args.out).resolve()
    if out.exists() and any(out.iterdir()):
        raise ValueError("output directory is not empty; choose a fresh directory")
    out.mkdir(parents=True, exist_ok=True)
    log("Resolve the base revision")
    directory, provenance = resolve_checkpoint(args.base, args.revision)
    if args.base_repo or args.base_revision:
        if not args.base_repo or not args.base_revision or not Path(args.base).is_dir():
            raise ValueError("local base attribution needs both --base-repo and --base-revision")
        provenance.update(source=args.base_repo, revision=args.base_revision)
    store = TensorStore(directory)
    card = {"schema_version": 1, "base": {"repo": args.base_repo or args.base, **provenance,
            "shards_sha256": store.provenance()}, "method": {"name": method, "version": "1"},
            "date": datetime.now(timezone.utc).isoformat(), "parameters": vars(args).copy(),
            "resources": {"gpu_fraction": 0.25, "host_memory_floor_gb": 12, "threads": 1},
            "versions": versions(), "tensors_touched": [], "status": "running"}
    write_json(out / "recipe-card.json", card)
    return directory, out, card


def versions():
    """Record installed versions as well as the intended dependency pins."""
    result = {}
    for package in ("torch", "transformers", "peft", "trl", "datasets", "accelerate", "heretic-llm", "kernels",
                    "numpy", "safetensors", "requests", "jinja2", "huggingface-hub", "optuna", "bitsandbytes"):
        try:
            result[package] = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            result[package] = None
    return result


def save_merged(runtime, tokenizer, out, base):
    """Retain tied tensor aliases so the comparison sees the same names as the base."""
    runtime.save_pretrained(out, safe_serialization=True, max_shard_size="1GB")
    tokenizer.save_pretrained(out)
    original, derived = TensorStore(base), TensorStore(out)
    missing = set(original.names) - set(derived.names)
    if not missing:
        return
    from safetensors.torch import save_file
    from audit.weights import read_json
    state = runtime.state_dict()
    index_path = Path(out) / "model.safetensors.index.json"
    if index_path.exists():
        index = read_json(index_path)
    else:
        total = 0
        for name in derived.names:
            tensor = derived.get(name)
            total += tensor.numel() * tensor.element_size()
            del tensor
        index = {"metadata": {"total_size": total},
                 "weight_map": {name: path.name for name, path in derived.names.items()}}
    for number, name in enumerate(sorted(missing)):
        if name not in state:
            raise ValueError(f"export lost a base tensor: {name}")
        filename = f"alias-{number:04d}.safetensors"
        tensor = state[name].detach().cpu().contiguous()
        save_file({name: tensor}, str(Path(out) / filename))
        index["weight_map"][name] = filename
        index["metadata"]["total_size"] += tensor.numel() * tensor.element_size()
    write_json(index_path, index)


def finish(out, card, base=None):
    """Only mark completion after the exported weights and card are readable."""
    if card["status"] != "skipped":
        derived = TensorStore(out)
        if base is not None:
            original = TensorStore(base)
            if set(original.names) != set(derived.names):
                raise ValueError("exported tensor names differ from the base")
            card["tensors_touched"] = [name for name in sorted(original.names)
                                       if not torch.equal(original.get(name), derived.get(name))]
        card["derived_shards_sha256"] = derived.provenance()
        card["status"] = "complete"
    write_json(out / "recipe-card.json", card)
    write_json(out / "done.json", {"status": card["status"], "card_sha256": digest(out / "recipe-card.json")})
    log(f"Recipe {card['status']}: {out.name}")


def load_runtime(directory, resources):
    """Load one checkpoint; avoid remote code and automatic device placement."""
    from transformers import AutoModelForCausalLM, AutoTokenizer

    resources.check()
    tokenizer = AutoTokenizer.from_pretrained(directory, local_files_only=True, trust_remote_code=False)
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token
    dtype = torch.float32 if resources.device.type == "cpu" else torch.bfloat16
    runtime = AutoModelForCausalLM.from_pretrained(directory, local_files_only=True,
                                                trust_remote_code=False, dtype=dtype).to(resources.device)
    runtime.eval()
    return runtime, tokenizer


def release(runtime):
    """Release a checkpoint before loading another; allocator cache also counts."""
    del runtime
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()


def instruction_ids(tokenizer, instruction, device, max_length):
    """Use the saved chat template and fail rather than truncate the instruction."""
    text = tokenizer.apply_chat_template([{"role": "user", "content": instruction}],
                                         tokenize=False, add_generation_prompt=True, enable_thinking=False)
    encoded = tokenizer(text, return_tensors="pt", add_special_tokens=False)
    if encoded.input_ids.shape[1] > max_length:
        raise ValueError("instruction exceeds max length")
    return {key: value.to(device) for key, value in encoded.items()}


@torch.inference_mode()
def response(runtime, tokenizer, instruction, args, resources):
    """Decode only the answer; a refusal in the question must not count."""
    resources.check()
    encoded = instruction_ids(tokenizer, instruction, resources.device, args.max_length)
    output = runtime.generate(**encoded, do_sample=False, max_new_tokens=args.max_new_tokens,
                              pad_token_id=tokenizer.pad_token_id)
    return tokenizer.decode(output[0, encoded["input_ids"].shape[1]:], skip_special_tokens=True).strip()


def refuses(text):
    """Use a recorded lexical count; this is a selection score, not a safety grade."""
    return bool(re.search(r"\b(i (?:cannot|can't|won't|will not|am unable)|i'm sorry|i apologize|"
                          r"unable to (?:help|assist)|cannot (?:help|assist)|can't (?:help|assist))\b", text.lower()))
