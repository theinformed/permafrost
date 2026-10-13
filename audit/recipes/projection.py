# projection.py -- Build all-layer, selected-layer, and norm-restored copies.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  reuse the null projection with held-out layer selection.
"""Measure one direction and apply it to residual-writing matrices."""

import re

import torch
from safetensors.torch import save_file

from audit.nulls import copy_checkpoint, middle_residual, prompts, project_tensor, tokenize_instructions
from audit.weights import TensorStore, read_json, tensor_kind, write_json
from .common import finish, load_runtime, log, prepare, refuses, release, response


@torch.inference_mode()
def extract(directory, groups, args, resources):
    """Measure the middle-block input at the last assistant-prefix token."""
    config = read_json(directory / "config.json")
    sums = {}
    if config["model_type"] == "llama" and resources.device.type == "cpu":
        store = TensorStore(directory)
        for group, instructions in groups.items():
            values = []
            for instruction in instructions[:args.train_prompts]:
                resources.check()
                ids, lengths = tokenize_instructions(directory, [instruction])
                values.append(middle_residual(store, config, ids, lengths)[0])
            sums[group] = torch.stack(values).mean(0)
    else:
        from .common import instruction_ids
        runtime, tokenizer = load_runtime(directory, resources)
        captured = []

        def capture(module, inputs):
            """Copy just the final residual, rather than retaining a whole forward."""
            captured.append(inputs[0][0, -1].detach().double().cpu())

        handle = runtime.model.layers[config["num_hidden_layers"] // 2].register_forward_pre_hook(capture)
        try:
            for group, instructions in groups.items():
                values = []
                for instruction in instructions[:args.train_prompts]:
                    resources.check()
                    runtime(**instruction_ids(tokenizer, instruction, resources.device, args.max_length), use_cache=False)
                    values.append(captured.pop())
                sums[group] = torch.stack(values).mean(0)
        finally:
            handle.remove()
            del runtime
            release(None)
    difference = sums["harmful"] - sums["harmless"]
    norm = torch.linalg.vector_norm(difference)
    if not torch.isfinite(difference).all() or not norm:
        raise ValueError("activation difference has no finite direction")
    direction = (difference / norm).float()
    return direction / direction.norm(), sums


@torch.no_grad()
def select_layers(directory, direction, heldout, args, resources):
    """Keep the layers with the largest positive drop in individual refusal counts."""
    runtime, tokenizer = load_runtime(directory, resources)
    baseline = sum(refuses(response(runtime, tokenizer, item, args, resources)) for item in heldout)
    scores = []
    try:
        for index, layer in enumerate(runtime.model.layers):
            log(f"Score layer {index + 1}/{len(runtime.model.layers)} on {len(heldout)} held-out prompts")
            modules = [layer.self_attn.o_proj, layer.mlp.down_proj]
            originals = [module.weight.detach().clone() for module in modules]
            try:
                for module in modules:
                    module.weight.copy_(project_tensor(module.weight, direction.to(module.weight.device)).to(module.weight.dtype))
                count = sum(refuses(response(runtime, tokenizer, item, args, resources)) for item in heldout)
            finally:
                for module, weight in zip(modules, originals):
                    module.weight.copy_(weight)
            scores.append({"layer": index, "refusals": count, "reduction": baseline - count})
    finally:
        del runtime
        release(None)
    best = max(item["reduction"] for item in scores)
    selected = [item["layer"] for item in scores if best > 0 and item["reduction"] == best]
    return selected, {"baseline_refusals": baseline, "candidates": scores,
                      "selection": "all ties at maximum positive refusal-count reduction",
                      "selected_layers": selected, "heldout_prompts": heldout, "refusal_counter": "lexical-v1"}


def restore_norms(original, projected):
    """Rescale rows; a collapsed nonzero row cannot be restored by division."""
    before = original.float().norm(dim=1, keepdim=True)
    after = projected.norm(dim=1, keepdim=True)
    if ((before > 0) & (after <= torch.finfo(projected.dtype).tiny)).any():
        raise ValueError("projection collapsed a nonzero row; its norm cannot be restored")
    return projected * before / after.clamp_min(torch.finfo(projected.dtype).tiny)


def build_projection(directory, out, card, args, resources, method):
    """Save a projection checkpoint without converting untouched tensors."""
    groups = prompts(args.prompts)
    log("Measure the difference of mean middle-layer residuals")
    direction, means = extract(directory, groups, args, resources)
    save_file({"refusal_direction": direction, **{key + "_mean": value for key, value in means.items()}},
              str(out / "recipe-direction.safetensors"))
    # Recipe measurements live outside the weight glob used for unindexed checkpoints.
    evidence = out / "evidence"
    evidence.mkdir()
    (out / "recipe-direction.safetensors").replace(evidence / "direction.safetensors")
    layers = None
    if method == "single-projection-selected":
        heldout = groups["harmful"][args.train_prompts:args.train_prompts + args.heldout_prompts]
        layers, selection = select_layers(directory, direction, heldout, args, resources)
        card["selection"] = selection
        write_json(evidence / "selection.json", selection)
    touched = []

    def transform(name, tensor):
        """Apply the same output-space projection as the small null control."""
        resources.check()
        layer = re.search(r"\.layers\.(\d+)\.", name)
        if tensor_kind(name) not in {"attention_output", "feed_forward_down"}:
            return tensor
        if layers is not None and (layer is None or int(layer[1]) not in layers):
            return tensor
        log(f"Project {name}")
        projected = project_tensor(tensor, direction)
        if method == "norm-preserving":
            projected = restore_norms(tensor, projected)
        if not torch.equal(tensor, projected):
            touched.append(name)
        return projected

    copy_checkpoint(TensorStore(directory), out, transform)
    card["tensors_touched"] = touched
    card["direction"] = {"path": "evidence/direction.safetensors",
                         "position": "last assistant-prefix token", "train_prompts_per_group": args.train_prompts}
    card["direction"]["middle_layer"] = read_json(directory / "config.json")["num_hidden_layers"] // 2
    if method == "norm-preserving":
        card["method"]["version"] = "projection-then-row-rescale-v1"
        card["description"] = "Single projection followed by original row-norm restoration; no pre-normalization or biprojection."
    return out


def run(args, resources, method):
    """Build and mark one projection reference."""
    directory, out, card = prepare(args, method)
    build_projection(directory, out, card, args, resources, method)
    finish(out, card)
