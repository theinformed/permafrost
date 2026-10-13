# test_recipe_smoke.py -- Run one small checkpoint recipe and comparison per test.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  make the four CPU smoke checks repeatable without downloads.
"""Opt-in CPU smoke checks; select one test per command on the shared host."""

import os
import tempfile
import unittest
from pathlib import Path

import torch

from audit.recipes.runner import main
from audit.weights import ROOT, TensorStore, compare_weights, read_json


@unittest.skipUnless(os.environ.get("RECIPE_CPU_BASE"), "set RECIPE_CPU_BASE to the cached small checkpoint")
class SmallCheckpoint(unittest.TestCase):
    """Keep each downloaded-checkpoint run small and discard its derived copy."""

    def check_method(self, method):
        """Build one copy, compare it, then remove only this test's temporary output."""
        base = Path(os.environ["RECIPE_CPU_BASE"]).resolve()
        config = read_json(base / "config.json")
        self.assertEqual(config["hidden_size"], 576)
        self.assertEqual(config["num_hidden_layers"], 30)
        torch.set_num_threads(1)
        (ROOT / ".tmp").mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=ROOT / ".tmp") as temporary:
            out = Path(temporary) / "derived"
            arguments = ["--base", str(base), "--out", str(out), "--device", "cpu",
                         "--train-prompts", "2", "--heldout-prompts", "1", "--max-new-tokens", "2",
                         "--pairs", "2", "--rank", "2", "--learning-rate", "0.001"]
            if method == "plain-lora":
                data = Path(temporary) / "instructions.jsonl"
                data.write_text('{"prompt":"Write a friendly message welcoming a neighbor.","response":"Welcome to the neighborhood."}\n'
                                '{"prompt":"Explain how to study for a school quiz.","response":"Read your notes, then practice a few questions."}\n')
                arguments.extend(["--training-data", str(data)])
            self.assertEqual(main(method, arguments), 0)
            self.assertEqual(read_json(out / "done.json")["status"], "complete")
            card = read_json(out / "recipe-card.json")
            report = compare_weights(str(out), str(base), Path(temporary) / "report.json")
            self.assertFalse(report["original_only"])
            self.assertFalse(report["modified_only"])
            summary = report["summary"]
            if method == "single-projection":
                self.assertEqual(len(card["tensors_touched"]), 60)
                self.assertGreater(summary["min_first_singular_energy_share"], .99)
                self.assertGreater(summary["direction_agreement"]["min_cosine"], .95)
            elif method == "norm-preserving":
                self.assertTrue(all(row["row_norms"]["preserved_equal"] for row in report["tensors"].values() if "row_norms" in row))
            elif method == "single-projection-selected":
                self.assertEqual(len(card["selection"]["candidates"]), 30)
                self.assertEqual(len(card["tensors_touched"]), 2 * len(card["selection"]["selected_layers"]))
            else:
                touched_kinds = {name.rsplit(".", 2)[-2] for name in card["tensors_touched"]}
                self.assertTrue(card["tensors_touched"])
                self.assertLessEqual(touched_kinds, {"q_proj", "v_proj"})

    def test_all_layers(self):
        self.check_method("single-projection")

    def test_selected_layers(self):
        self.check_method("single-projection-selected")

    def test_norm_restoration(self):
        self.check_method("norm-preserving")

    def test_benign_adapter(self):
        self.check_method("plain-lora")


if __name__ == "__main__":
    unittest.main()
