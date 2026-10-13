# runner.py -- Dispatch one reference method after validating its arguments.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  add common entry points and import-only checks.
"""Shared command-line dispatch; optional training packages load only when needed."""

import sys
from unittest.mock import patch

from .common import Resources, log, parser, validate


def main(method, argv=None):
    """Run one method, with a short error message and no completion on failure."""
    arguments = parser(method)
    args = arguments.parse_args(argv)
    try:
        validate(args)
        if method.startswith("heretic-"):
            from . import tool as implementation
        elif method in {"projection-plus-healing", "plain-lora"}:
            from . import training as implementation
        else:
            from . import projection as implementation
        if args.check_imports:
            if method.startswith("heretic-"):
                implementation.check_version()
                from heretic.config import Settings
                with patch.object(sys, "argv", ["heretic"]):
                    Settings(model=args.base, device_map=args.device, seed=args.seed)
                if method == "heretic-directional":
                    from heretic import main
            elif method == "projection-plus-healing":
                from trl import DPOConfig, DPOTrainer
                from peft import LoraConfig
            else:
                from transformers import AutoModelForCausalLM
                from peft import LoraConfig
            log(f"Imports checked: {method}")
            return 0
        with Resources(args.device) as resources:
            implementation.run(args, resources, method)
        return 0
    except (ValueError, OSError, RuntimeError, ImportError) as error:
        print(f"recipe: {error}", file=sys.stderr)
        return 1
