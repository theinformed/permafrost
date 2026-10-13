# test_recipes.py -- Check recipe math, selection, and completion records on CPU.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  test held-out selection, memory checks, and measured pass lines.
"""Small analytic tests; the downloaded checkpoint smoke runs are separate."""

import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import torch
from safetensors.torch import save_file

from audit.nulls import project_tensor
from audit.recipes.common import Resources, finish, parser, refuses, save_merged, validate
from audit.recipes.library import envelope, summarize
from audit.recipes.projection import restore_norms, select_layers
from audit.recipes.runner import main
from audit.recipes.tool import intervention
from audit.recipes.training import read_examples
from audit.weights import ROOT, TensorStore, compare_weights, digest, read_json, recipe_table, score_report, write_json


class RecipeMath(unittest.TestCase):
    """Use small matrices whose projections can be checked directly."""

    def setUp(self):
        torch.set_num_threads(1)

    def test_projection_matches_published_null(self):
        weight = torch.tensor([[1., 2.], [3., 4.], [5., 6.]])
        direction = torch.tensor([1., 2., -1.])
        direction /= direction.norm()
        projected = project_tensor(weight, direction)
        torch.testing.assert_close(direction @ projected, torch.zeros(2), atol=1e-6, rtol=0)
        self.assertLess(float(torch.linalg.svdvals(projected - weight)[1]), 1e-6)

    def test_restored_norms_and_zero_rows(self):
        weight = torch.tensor([[1., 2., 3.], [3., 1., 1.], [0., 0., 0.]])
        direction = torch.tensor([1., 1., 0.]) / 2**0.5
        restored = restore_norms(weight, project_tensor(weight, direction))
        torch.testing.assert_close(restored.norm(dim=1), weight.norm(dim=1))
        self.assertFalse(torch.equal(restored, weight))
        with self.assertRaisesRegex(ValueError, "collapsed"):
            restore_norms(torch.eye(2), project_tensor(torch.eye(2), torch.tensor([1., 0.])))

    def test_dimension_mismatch(self):
        with self.assertRaisesRegex(ValueError, "width"):
            project_tensor(torch.ones(2, 3), torch.ones(3))

    def test_refusal_counter_reads_answer_text(self):
        self.assertTrue(refuses("I'm sorry, I cannot assist with that."))
        self.assertFalse(refuses("Here is a friendly welcome message."))

    def test_layer_selection_keeps_best_ties_and_restores_weights(self):
        layers = []
        for _ in range(3):
            layers.append(SimpleNamespace(self_attn=SimpleNamespace(o_proj=torch.nn.Linear(2, 2, bias=False)),
                                          mlp=SimpleNamespace(down_proj=torch.nn.Linear(2, 2, bias=False))))
        for layer in layers:
            for module in (layer.self_attn.o_proj, layer.mlp.down_proj):
                module.weight.data.copy_(torch.eye(2))
        runtime = SimpleNamespace(model=SimpleNamespace(layers=layers))
        args = SimpleNamespace(max_length=32)
        answers = ["I cannot help", "yes", "I cannot help", "yes"]
        with patch("audit.recipes.projection.load_runtime", return_value=(runtime, None)), patch(
                "audit.recipes.projection.response", side_effect=answers):
            selected, evidence = select_layers(Path("unused"), torch.tensor([1., 0.]), ["heldout"], args, None)
        self.assertEqual(selected, [0, 2])
        self.assertEqual(evidence["baseline_refusals"], 1)
        for layer in layers:
            torch.testing.assert_close(layer.self_attn.o_proj.weight, torch.eye(2))

    def test_zero_refusal_drop_keeps_no_layers(self):
        layer = SimpleNamespace(self_attn=SimpleNamespace(o_proj=torch.nn.Linear(2, 2, bias=False)),
                                mlp=SimpleNamespace(down_proj=torch.nn.Linear(2, 2, bias=False)))
        runtime = SimpleNamespace(model=SimpleNamespace(layers=[layer]))
        with patch("audit.recipes.projection.load_runtime", return_value=(runtime, None)), patch(
                "audit.recipes.projection.response", return_value="yes"):
            selected, _ = select_layers(Path("unused"), torch.tensor([1., 0.]), ["heldout"], None, None)
        self.assertEqual(selected, [])

    def test_intervention_strengths_and_interpolated_directions(self):
        model = SimpleNamespace(get_layers=lambda: [0, 1, 2], get_layer_modules=lambda index: {"attention": []})
        directions = torch.tensor([[1., 0.], [0., 1.], [1., 0.], [0., -1.]])
        parameters = {"attention": SimpleNamespace(max_weight=1., max_weight_position=1., min_weight=.2, min_weight_distance=1.)}
        vectors, rows = intervention(model, directions, None, parameters)
        self.assertEqual([round(row["strength"], 5) for row in rows], [.2, 1., .2])
        torch.testing.assert_close(vectors["layer.1"], directions[2])
        vectors, _ = intervention(model, directions, .5, parameters)
        torch.testing.assert_close(vectors["layer.0"], torch.tensor([1., 1.]) / 2**.5)


class RecipeRecords(unittest.TestCase):
    """Completion and summary tests use tiny safetensors files in the repo."""

    def setUp(self):
        (ROOT / ".tmp").mkdir(exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=ROOT / ".tmp")
        self.root = Path(self.temporary.name)
        torch.set_num_threads(1)

    def tearDown(self):
        self.temporary.cleanup()

    def test_completion_hash_and_exact_touched_set(self):
        base, derived = self.root / "base", self.root / "derived"
        base.mkdir()
        derived.mkdir()
        save_file({"x": torch.ones(2), "y": torch.zeros(2)}, str(base / "model.safetensors"))
        save_file({"x": torch.ones(2), "y": torch.ones(2)}, str(derived / "model.safetensors"))
        card = {"status": "running", "method": {"name": "control"}}
        finish(derived, card, base)
        self.assertEqual(card["tensors_touched"], ["y"])
        marker = json.loads((derived / "done.json").read_text())
        self.assertEqual(marker["card_sha256"], digest(derived / "recipe-card.json"))

    def test_merged_export_keeps_tied_alias_names(self):
        base, derived = self.root / "base", self.root / "derived"
        base.mkdir()
        derived.mkdir()
        weight = torch.ones(2, 3)
        save_file({"embedding": weight, "head": weight.clone()}, str(base / "model.safetensors"))

        def save(directory, **kwargs):
            save_file({"embedding": weight}, str(Path(directory) / "model.safetensors"))

        runtime = SimpleNamespace(save_pretrained=save, state_dict=lambda: {"embedding": weight, "head": weight})
        tokenizer = SimpleNamespace(save_pretrained=lambda directory: None)
        save_merged(runtime, tokenizer, derived, base)
        self.assertEqual(set(TensorStore(derived).names), {"embedding", "head"})
        self.assertEqual(read_json(derived / "model.safetensors.index.json")["metadata"]["total_size"], 48)

    def test_export_name_mismatch_never_completes(self):
        base, derived = self.root / "base", self.root / "derived"
        base.mkdir()
        derived.mkdir()
        save_file({"x": torch.ones(2)}, str(base / "model.safetensors"))
        save_file({"y": torch.ones(2)}, str(derived / "model.safetensors"))
        with self.assertRaisesRegex(ValueError, "names"):
            finish(derived, {"status": "running", "method": {"name": "control"}}, base)
        self.assertFalse((derived / "done.json").exists())

    def test_compare_and_empirical_envelope(self):
        base, derived = self.root / "base", self.root / "derived"
        base.mkdir()
        derived.mkdir()
        name = "model.layers.0.self_attn.o_proj.weight"
        weight = torch.tensor([[1., 2.], [3., 5.]])
        direction = torch.tensor([1., 1.]) / 2**.5
        save_file({name: weight}, str(base / "model.safetensors"))
        save_file({name: project_tensor(weight, direction)}, str(derived / "model.safetensors"))
        card = {"method": {"name": "single-projection"}, "parameters": {"out": str(derived)}, "base": {"revision": "fixture"}}
        write_json(derived / "recipe-card.json", card)
        report = compare_weights(str(derived), str(base), self.root / "report.json")
        record = envelope(report, card)
        self.assertGreater(record["first_energy_min"], .999)
        self.assertFalse(record["row_norms_preserved"])
        self.assertEqual(record["changed_kinds"], ["attention_output"])
        table = {"tensor_kinds": recipe_table()["tensor_kinds"], "control": record}
        score_report(report, table)
        self.assertTrue(report["recipe_matching"]["matched"])
        table["control"]["row_norms_preserved"] = True
        score_report(report, table)
        self.assertIn("row_norms_not_preserved", [item["rule"] for item in report["recipe_matching"]["violations"]])
        table["control"]["base_shards_sha256"] = {"different": "hash"}
        score_report(report, table)
        self.assertEqual(report["recipe_matching"]["outside_calibrated_base"], ["control"])
        self.assertIsNone(report["recipe_matching"]["nearest_recipe"])

    def test_summary_distinguishes_pending_skipped_and_unchanged(self):
        write_json(self.root / "heretic-arbitrary-rank.envelope.json", {"status": "skipped", "reason": "absent in version 1.3.0"})
        write_json(self.root / "single-projection-selected.envelope.json", {"status": "no measurable change", "changed_kinds": [],
                   "first_energy_min": None, "direction_cosine_min": None, "row_norms_preserved": None})
        summarize(self.root, self.root / "summary.md")
        text = (self.root / "summary.md").read_text()
        self.assertIn("absent in version 1.3.0", text)
        self.assertIn("single-projection-selected | none", text)
        self.assertIn("single-projection | pending", text)

    def test_training_data_needs_distinct_answers(self):
        path = self.root / "pairs.jsonl"
        path.write_text(json.dumps({"prompt": "Hello", "chosen": "Hi", "rejected": "Hi"}) + "\n")
        with self.assertRaisesRegex(ValueError, "identical"):
            read_examples(path, True)
        path.write_text(json.dumps({"prompt": "Hello", "response": "Hi"}) + "\n")
        self.assertEqual(len(read_examples(path, False)), 1)


class RecipeResources(unittest.TestCase):
    """Exercise memory and allocation checks without allocating device memory."""

    def test_low_memory_stops_before_loading(self):
        with patch("audit.recipes.common.available_memory", return_value=11 * 1024**3):
            with self.assertRaisesRegex(MemoryError, "12 GB"):
                Resources("cpu").check()

    def test_device_fraction_is_a_quarter(self):
        with patch("audit.recipes.common.available_memory", return_value=32 * 1024**3), patch(
                "torch.cuda.is_available", return_value=True), patch("torch.cuda.set_device"), patch(
                "torch.cuda.set_per_process_memory_fraction") as fraction, patch(
                "torch.cuda.get_device_properties", return_value=SimpleNamespace(total_memory=128 * 1024**3)):
            with Resources("cuda:0") as resources:
                fraction.assert_called_once_with(.25, 0)
                self.assertEqual(resources.gpu_bytes, 32 * 1024**3)

    def test_invalid_split_and_negative_rank(self):
        args = parser("plain-lora").parse_args(["--base", "unused", "--out", "unused", "--train-prompts", "32"])
        with self.assertRaisesRegex(ValueError, "32-prompt"):
            validate(args)
        args = parser("plain-lora").parse_args(["--base", "unused", "--out", "unused", "--rank", "0"])
        with self.assertRaisesRegex(ValueError, "positive"):
            validate(args)

    def test_optional_runners_parse_without_loading_weights(self):
        for method in ("heretic-directional", "heretic-arbitrary-rank", "projection-plus-healing"):
            with patch("audit.recipes.runner.Resources") as resources:
                with contextlib.redirect_stdout(io.StringIO()), self.assertRaises(SystemExit) as error:
                    main(method, ["--help"])
                self.assertEqual(error.exception.code, 0)
                resources.assert_not_called()


if __name__ == "__main__":
    unittest.main()
