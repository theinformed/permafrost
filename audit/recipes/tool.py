# tool.py -- Export the pinned public directional method without its menus.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  capture directions, strengths, and the selected trial.
"""Run the published optimizer defaults and retain its selected intervention."""

import importlib.metadata
import math
import os
import sys
from dataclasses import asdict
from pathlib import Path
from unittest.mock import patch

import torch
from safetensors.torch import save_file

from audit.weights import write_json
from .common import TOOL_VERSION, finish, log, prepare, save_merged


def check_version():
    """Reject tool drift; menu and intervention hooks are specific to this release."""
    actual = importlib.metadata.version("heretic-llm")
    if actual != TOOL_VERSION:
        raise ValueError(f"expected public tool {TOOL_VERSION}, found {actual}")
    return actual


def intervention(model, directions, index, parameters):
    """Record the effective direction and strength for every target layer."""
    selected = None
    if index is not None:
        fraction, position = math.modf(index + 1)
        selected = torch.nn.functional.normalize(directions[int(position)].lerp(directions[int(position) + 1], fraction), dim=0)
    tensors, rows = {}, []
    for layer in range(len(model.get_layers())):
        vector = directions[layer + 1] if selected is None else selected
        tensors[f"layer.{layer}"] = vector.detach().float().cpu().contiguous()
        for component in model.get_layer_modules(layer):
            params = parameters[component]
            distance = abs(layer - params.max_weight_position)
            strength = 0.0
            if distance <= params.min_weight_distance:
                strength = params.max_weight + distance / params.min_weight_distance * (params.min_weight - params.max_weight)
            rows.append({"layer": layer, "component": component, "strength": strength})
    return tensors, rows


def run(args, resources, method):
    """Keep default optimization settings and choose the first refusal-sorted trial."""
    actual = check_version()
    directory, out, card = prepare(args, method)
    card["method"]["version"] = actual
    if method == "heretic-arbitrary-rank":
        card.update(status="skipped", reason=f"absent in version {actual}")
        finish(out, card)
        return
    from heretic import main as upstream
    from heretic.config import Settings
    from heretic.model import Model

    work = out / "evidence"
    work.mkdir()
    options = {"model": str(directory), "device_map": str(resources.device), "seed": args.seed,
               "study_checkpoint_dir": str(work / "optimizer"), "max_shard_size": "1GB"}
    if resources.gpu_bytes is not None:
        options["max_memory"] = {str(resources.device.index or 0): f"{resources.gpu_bytes // 1024**2}MiB"}
    # No ambient configuration file or environment should change the published defaults.
    old_cwd = Path.cwd()
    original = Model.abliterate
    state = {}

    class Exported(BaseException):
        """Leave the interactive loop after saving the selected merged checkpoint."""

    def capture(model, directions, index, parameters):
        """Remember only the latest intervention, not every optimization trial."""
        original(model, directions, index, parameters)
        vectors, strengths = intervention(model, directions, index, parameters)
        state.update(model=model, vectors=vectors, strengths=strengths, direction_index=index,
                     parameters={key: asdict(value) for key, value in parameters.items()})

    def choose(message, choices):
        """Answer the two known menus; an unfamiliar prompt needs a code update."""
        if message == "Which trial do you want to use?":
            trial = next(choice.value for choice in choices if hasattr(getattr(choice, "value", None), "user_attrs"))
            card["selected_trial"] = {"number": trial.number, "parameters": trial.params, "attributes": trial.user_attrs}
            return trial
        if message == "What do you want to do with the decensored model?":
            log("Save the chosen trial and its per-layer intervention")
            save_file(state["vectors"], str(work / "directions.safetensors"))
            card["intervention"] = {key: value for key, value in state.items() if key not in {"model", "vectors"}}
            merged = state["model"].get_merged_model()
            save_merged(merged, state["model"].tokenizer, out, directory)
            raise Exported()
        raise RuntimeError(f"unexpected public-tool prompt: {message}")

    try:
        os.chdir(work)
        environment = {key: value for key, value in os.environ.items() if not key.startswith("HERETIC_")}
        with patch.object(sys, "argv", ["heretic"]), patch.dict(os.environ, environment, clear=True):
            settings = Settings(**options)
            card["tool_settings"] = settings.model_dump(mode="json")
            write_json(work / "settings.json", card["tool_settings"])
            log("Run the pinned optimizer with its default trial and data settings")
            with patch.object(upstream, "Settings", return_value=settings), patch.object(Model, "abliterate", capture), patch.object(upstream, "prompt_select", choose):
                upstream.run()
        raise RuntimeError("public tool returned without exporting a checkpoint")
    except Exported:
        card["tool_settings"] = settings.model_dump(mode="json")
        write_json(work / "settings.json", card["tool_settings"])
    finally:
        os.chdir(old_cwd)
    finish(out, card, directory)
