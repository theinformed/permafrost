# nulls.py -- Make rounding and projection controls on a small CPU checkpoint.
# Created by LT Sean Egan, PhD 2026-10-13
# Modified: SDE 2026-10-13  split activation work into short, repeatable batches.
# Modified: SDE 2026-10-13  share the output-space projection with recipe runners.
"""Build two null checkpoints, using a streamed forward pass for the direction."""

import hashlib
import json
import shutil
from pathlib import Path

import torch
import torch.nn.functional as F
from safetensors import safe_open
from safetensors.torch import save_file

from .weights import ROOT, TensorStore, compare_weights, digest, read_json, resolve_checkpoint, safe_name, tensor_kind, write_json


def prompts(directory):
    """Read exactly 32 instructions per group; empty lines do not count."""
    result = {}
    for group in ("harmful", "harmless"):
        path = Path(directory) / (group + ".txt")
        lines = [line.strip() for line in path.read_text().splitlines() if line.strip()]
        if len(lines) != 32:
            raise ValueError(f"expected 32 {group} prompts, got {len(lines)}")
        result[group] = lines
    return result


def tokenize_instructions(directory, instructions):
    """Use the checkpoint's template and tokenizer, without truncating instructions."""
    from jinja2.sandbox import ImmutableSandboxedEnvironment
    from tokenizers import Tokenizer

    settings = read_json(Path(directory) / "tokenizer_config.json")
    template = settings["chat_template"]
    if not isinstance(template, str):
        raise ValueError("expected a single chat template")
    environment = ImmutableSandboxedEnvironment()

    def raise_exception(message):
        """Keep template errors from turning into quiet token changes."""
        raise ValueError(message)

    environment.globals["raise_exception"] = raise_exception
    renderer = environment.from_string(template)
    tokenizer = Tokenizer.from_file(str(Path(directory) / "tokenizer.json"))
    encoded = []
    for instruction in instructions:
        text = renderer.render(messages=[{"role": "user", "content": instruction}], add_generation_prompt=True,
                               bos_token=settings.get("bos_token", ""), eos_token=settings.get("eos_token", ""))
        ids = tokenizer.encode(text, add_special_tokens=False).ids
        if not ids or len(ids) > 128:
            raise ValueError("instruction must fit within 128 tokens")
        encoded.append(ids)
    lengths = torch.tensor([len(ids) for ids in encoded])
    padded = torch.zeros((len(encoded), int(lengths.max())), dtype=torch.long)
    for row, ids in enumerate(encoded):
        padded[row, :len(ids)] = torch.tensor(ids)
    return padded, lengths


def rms_norm(values, weight, epsilon):
    """Normalize the residual without centering it."""
    return values * torch.rsqrt(values.square().mean(-1, keepdim=True) + epsilon) * weight


def rotate_half(values):
    """Rotate the two channel halves used by the checkpoint's rotary positions."""
    first, second = values.chunk(2, dim=-1)
    return torch.cat((-second, first), dim=-1)


@torch.inference_mode()
def middle_residual(store, config, ids, lengths):
    """Read blocks through the middle-layer input; no logits or decoding are needed."""
    if (config.get("model_type") != "llama" or config.get("hidden_act") != "silu" or config.get("attention_bias") or config.get("mlp_bias")
            or config.get("rope_scaling") or config.get("rope_interleaved") or config.get("pretraining_tp", 1) != 1):
        raise ValueError("null forward supports unscaled, bias-free rotary blocks with silu")
    head_count, kv_count = config["num_attention_heads"], config["num_key_value_heads"]
    head_size = config["hidden_size"] // head_count
    if config.get("head_dim", head_size) != head_size or head_size % 2 or head_count % kv_count:
        raise ValueError("unsupported attention head dimensions")
    count, sequence = ids.shape
    embedding = store.get("model.embed_tokens.weight").float()
    residual = F.embedding(ids, embedding)
    del embedding
    positions = torch.arange(sequence, dtype=torch.float32)
    frequency = config.get("rope_theta", 10000.0) ** (-torch.arange(0, head_size, 2).float() / head_size)
    angle = positions[:, None] * frequency[None, :]
    angle = torch.cat((angle, angle), dim=-1)
    cosine, sine = angle.cos()[None, None], angle.sin()[None, None]
    valid_keys = torch.arange(sequence)[None, :] < lengths[:, None]
    mask = torch.ones((sequence, sequence), dtype=torch.bool).tril()[None, None] & valid_keys[:, None, None, :]
    epsilon = config["rms_norm_eps"]
    for layer in range(config["num_hidden_layers"] // 2):
        prefix = f"model.layers.{layer}."
        normalized = rms_norm(residual, store.get(prefix + "input_layernorm.weight").float(), epsilon)
        query = F.linear(normalized, store.get(prefix + "self_attn.q_proj.weight").float()).view(count, sequence, head_count, head_size).transpose(1, 2)
        key = F.linear(normalized, store.get(prefix + "self_attn.k_proj.weight").float()).view(count, sequence, kv_count, head_size).transpose(1, 2)
        value = F.linear(normalized, store.get(prefix + "self_attn.v_proj.weight").float()).view(count, sequence, kv_count, head_size).transpose(1, 2)
        query = query * cosine + rotate_half(query) * sine
        key = key * cosine + rotate_half(key) * sine
        key = key.repeat_interleave(head_count // kv_count, dim=1)
        value = value.repeat_interleave(head_count // kv_count, dim=1)
        attention = F.scaled_dot_product_attention(query, key, value, attn_mask=mask).transpose(1, 2).reshape(count, sequence, -1)
        residual = residual + F.linear(attention, store.get(prefix + "self_attn.o_proj.weight").float())
        normalized = rms_norm(residual, store.get(prefix + "post_attention_layernorm.weight").float(), epsilon)
        gate = F.silu(F.linear(normalized, store.get(prefix + "mlp.gate_proj.weight").float()))
        up = F.linear(normalized, store.get(prefix + "mlp.up_proj.weight").float())
        residual = residual + F.linear(gate * up, store.get(prefix + "mlp.down_proj.weight").float())
    return residual[torch.arange(count), lengths - 1].double()


def project_tensor(tensor, direction):
    """Remove a unit direction from a matrix that writes to the residual stream."""
    weight = tensor.float()
    if weight.ndim != 2 or weight.shape[0] != len(direction):
        raise ValueError("projection output width differs")
    return weight - direction[:, None] * (direction @ weight)[None, :]


def copy_checkpoint(store, destination, transform):
    """Write one tensor per shard, avoiding a second checkpoint in memory."""
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=True)
    index, total = {}, 0
    for number, name in enumerate(sorted(store.names)):
        tensor = transform(name, store.get(name)).contiguous()
        shard = f"tensor-{number:05d}.safetensors"
        temporary = destination / (shard + ".part")
        save_file({name: tensor}, str(temporary))
        temporary.replace(destination / shard)
        index[name] = shard
        total += tensor.numel() * tensor.element_size()
        del tensor
    for name in ("config.json", "tokenizer.json", "tokenizer_config.json", "special_tokens_map.json", "generation_config.json"):
        source = store.directory / name
        if source.exists():
            shutil.copyfile(source, destination / name)
    config_path = destination / "config.json"
    if config_path.exists():
        config = read_json(config_path)
        config["torch_dtype"] = "float32"
        write_json(config_path, config)
    write_json(destination / "model.safetensors.index.json", {"metadata": {"total_size": total}, "weight_map": index})


def context(model, directory, prompt_directory):
    """Bind saved batches to their checkpoint and exact prompt lists."""
    original, provenance = resolve_checkpoint(model)
    store = TensorStore(original)
    groups = prompts(prompt_directory)
    identity = {"original": provenance, "shards": store.provenance(), "prompts": groups}
    fingerprint = hashlib.sha256(json.dumps(identity, sort_keys=True).encode()).hexdigest()
    work = Path(directory)
    work.mkdir(parents=True, exist_ok=True)
    record = {"fingerprint": fingerprint, "original_directory": str(original), "identity": identity, "middle_layer": read_json(original / "config.json")["num_hidden_layers"] // 2,
              "token_position": "last token of assistant prefix", "precision": "float32 forward, float64 means", "batches": 8, "prompts_per_group_per_batch": 4}
    previous = work / "context.json"
    if previous.exists() and read_json(previous)["fingerprint"] != fingerprint:
        raise ValueError("null directory belongs to a different checkpoint or prompt set")
    write_json(previous, record)
    return store, groups, work, record


@torch.inference_mode()
def make_null(model, directory=None, step="all", batch_index=None, prompt_directory=None):
    """Make controls in separate short steps, or run them all for a tiny fixture."""
    store, groups, work, record = context(model, directory or ROOT / "data/nulls" / safe_name(model), prompt_directory or ROOT / "data/prompts")
    config = read_json(store.directory / "config.json")
    outputs = {}
    if step == "prepare":
        return record
    if step in ("all", "rounding"):
        copy_checkpoint(store, work / "rounding", lambda name, tensor: tensor.to(torch.bfloat16).float())
    if step in ("all", "activations"):
        batches = range(8) if batch_index is None else [batch_index]
        for index in batches:
            if not 0 <= index < 8:
                raise ValueError("batch index must be between 0 and 7")
            instructions = groups["harmful"][index * 4:index * 4 + 4] + groups["harmless"][index * 4:index * 4 + 4]
            ids, lengths = tokenize_instructions(store.directory, instructions)
            residuals = middle_residual(store, config, ids, lengths)
            save_file({"harmful_sum": residuals[:4].sum(0), "harmless_sum": residuals[4:].sum(0)}, str(work / f"activations-{index:02d}.safetensors"), metadata={"fingerprint": record["fingerprint"], "count_per_group": "4"})
            outputs[f"batch_{index}"] = {"max_tokens": int(lengths.max()), "count": 8}
    if step in ("all", "project"):
        harmful = torch.zeros(config["hidden_size"], dtype=torch.float64)
        harmless = torch.zeros_like(harmful)
        for index in range(8):
            with safe_open(work / f"activations-{index:02d}.safetensors", framework="pt") as shard:
                if shard.metadata().get("fingerprint") != record["fingerprint"] or shard.metadata().get("count_per_group") != "4":
                    raise ValueError("activation batch does not match these prompts and weights")
                harmful += shard.get_tensor("harmful_sum")
                harmless += shard.get_tensor("harmless_sum")
        difference = (harmful - harmless) / 32
        length = float(torch.linalg.vector_norm(difference))
        if not length or not torch.isfinite(difference).all():
            raise ValueError("mean activation difference has no finite direction")
        direction = (difference / length).float()
        direction = direction / torch.linalg.vector_norm(direction)
        save_file({"refusal_direction": direction, "harmful_mean": harmful / 32, "harmless_mean": harmless / 32}, str(work / "refusal-direction.safetensors"))

        def project(name, tensor):
            """Remove the direction from matrices that write to the residual stream."""
            weight = tensor.float()
            if tensor_kind(name) in {"attention_output", "feed_forward_down"}:
                if weight.ndim != 2 or weight.shape[0] != len(direction):
                    raise ValueError(f"projection output width differs: {name}")
                weight = project_tensor(tensor, direction)
            return weight

        copy_checkpoint(store, work / "single-projection", project)
        outputs["mean_difference_norm"] = length
        write_json(work / "projection.json", {**record, "mean_difference_norm": length, "direction_file": "refusal-direction.safetensors"})
    if step in ("all", "compare"):
        for name in ("rounding", "single-projection"):
            report = compare_weights(str(work / name), str(store.directory), work / (name + ".json"))
            outputs[name] = report["summary"]
            outputs[name]["recipe_matching"] = report["recipe_matching"]
        write_json(work / "results.json", outputs)
    return outputs
