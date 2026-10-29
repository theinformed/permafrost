# test_weights.py -- Check tensor measures against small matrices with known answers.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  cover rank, row norms, shard names, and streaming.
# Modified: SDE 2026-10-13  test hybrid roles, selected layers, and saved reports.
# Modified: SDE 2026-10-29  the packed expert names of Gemma 4 have their own kinds.
# Modified: SDE 2026-10-29  leftover, row-norm, precedence, optional-kind and MTP-head checks.
"""Small analytic checks for the checkpoint comparison."""

import gc
import json
import math
import tempfile
import unittest
import weakref
from pathlib import Path
from unittest.mock import patch

import torch
from safetensors import safe_open
from safetensors.torch import save_file

from audit.weights import (TensorStore, compare_weights, direction_agreement, match_recipes, measure_tensor, recipe_table,
                           resolve_checkpoint, rescore_weights, tensor_kind)


class TensorMeasures(unittest.TestCase):
    """Separate rank and norm checks; one is no substitute for the other."""

    @classmethod
    def setUpClass(cls):
        torch.set_num_threads(1)

    def test_rank_one(self):
        base = torch.eye(16)
        direction = torch.arange(1, 17).float()
        direction /= direction.norm()
        delta = torch.outer(direction, direction)
        row, vectors = measure_tensor(base, base + delta)
        self.assertAlmostEqual(row["first_singular_energy_share"], 1.0, places=5)
        self.assertEqual(len(row["energy_shares"]), 8)
        self.assertAlmostEqual(abs(float(vectors[0] @ direction)), 1.0, places=5)

    def test_rank_two(self):
        base = torch.eye(16)
        delta = torch.zeros_like(base)
        delta[0, 0] = delta[1, 1] = 1
        row, _ = measure_tensor(base, base + delta)
        self.assertAlmostEqual(row["first_singular_energy_share"], 0.5, places=5)
        self.assertLess(row["first_singular_energy_share"], 0.99)
        self.assertAlmostEqual(row["energy_shares"][1], 1.0, places=5)

    def test_row_rescaled_rank_one(self):
        base = torch.eye(16)
        modified = base.clone()
        modified[0] *= 2
        row, _ = measure_tensor(base, modified)
        self.assertAlmostEqual(row["first_singular_energy_share"], 1.0, places=5)
        self.assertFalse(row["row_norms"]["preserved_equal"])
        self.assertAlmostEqual(row["row_norms"]["max_relative_error"], 1.0)

    def test_equal_row_norms(self):
        base = torch.eye(16)
        row, _ = measure_tensor(base, -base)
        self.assertTrue(row["row_norms"]["preserved_equal"])

    def test_dtype_rounding_and_no_threshold_tuning(self):
        base = torch.linspace(0.01, 1, 100).float()
        row, _ = measure_tensor(base, base.to(torch.bfloat16))
        self.assertGreater(row["relative_difference"], 1e-3)
        self.assertTrue(row["changed"])

    def test_zero_base_and_zero_difference(self):
        row, _ = measure_tensor(torch.zeros(4), torch.ones(4))
        self.assertIsNone(row["relative_difference"])
        self.assertTrue(row["changed"])
        row, vectors = measure_tensor(torch.zeros(4, 4), torch.zeros(4, 4))
        self.assertEqual(row["relative_difference"], 0)
        self.assertIsNone(vectors)

    def test_nonfinite_and_shape_mismatch(self):
        row, _ = measure_tensor(torch.ones(4), torch.ones(5))
        self.assertEqual(row["status"], "shape_mismatch")
        row, _ = measure_tensor(torch.ones(4), torch.full((4,), float("nan")))
        self.assertEqual(row["status"], "nonfinite")

    def test_packed_integer_is_not_a_float(self):
        with self.assertRaisesRegex(ValueError, "format-specific decoder"):
            measure_tensor(torch.ones(4, dtype=torch.int8), torch.ones(4))

    def test_orthogonal_directions_have_undefined_median(self):
        rows = {str(index): {"kind": "attention_output"} for index in range(3)}
        vectors = {str(index): (torch.eye(3)[index], torch.eye(3)[index]) for index in range(3)}
        agreement = direction_agreement(rows, vectors)
        self.assertIsNone(agreement["min_cosine"])
        self.assertFalse(agreement["groups"]["attention_output:3"]["median_direction_defined"])
        json.dumps(agreement, allow_nan=False)

    def test_tensor_kinds_include_nonprojection_changes(self):
        self.assertEqual(tensor_kind("model.layers.0.self_attn.q_proj.weight"), "attention_query")
        self.assertEqual(tensor_kind("model.embed_tokens.weight"), "embedding")
        self.assertEqual(tensor_kind("lm_head.weight"), "output_head")
        self.assertEqual(tensor_kind("unrecognized.weight"), "other")

    def test_role_patterns_with_each_wrapper(self):
        roles = {"self_attn.o_proj": "attention_output", "linear_attn.out_proj": "linear_attention_output",
                 "mlp.down_proj": "feed_forward_down", "mlp.experts.3.down_proj": "expert_down",
                 "mlp.shared_expert.down_proj": "shared_expert_down", "mlp.shared_experts.0.down_proj": "shared_expert_down"}
        for prefix in ("", "model.", "model.language_model.", "transformer."):
            for projection, kind in roles.items():
                with self.subTest(prefix=prefix, projection=projection):
                    self.assertEqual(tensor_kind(f"{prefix}layers.2.{projection}.weight"), kind)
        self.assertEqual(tensor_kind("model.layers.2.linear_attn.out_proj.bias"), "other")
        # Gemma 4 packs its experts into one tensor per layer, named without a weight suffix.
        for prefix in ("", "model.", "model.language_model.", "transformer."):
            self.assertEqual(tensor_kind(f"{prefix}layers.2.experts.down_proj"), "expert_down")
            self.assertEqual(tensor_kind(f"{prefix}layers.2.experts.gate_up_proj"), "expert_gate_up")
        self.assertEqual(tensor_kind("model.layers.2.mlp.experts.3.up_proj.weight"), "feed_forward_up")

    def test_multi_token_prediction_head_takes_ordinary_kinds(self):
        # Qwen3.5 names its multi-token-prediction head under mtp., beside the language model.
        self.assertEqual(tensor_kind("mtp.layers.0.self_attn.o_proj.weight"), "attention_output")
        self.assertEqual(tensor_kind("mtp.layers.0.mlp.down_proj.weight"), "feed_forward_down")
        self.assertEqual(tensor_kind("mtp.layers.0.self_attn.q_proj.weight"), "attention_query")
        self.assertEqual(tensor_kind("mtp.fc.weight"), "other")


class CheckpointComparison(unittest.TestCase):
    """Use separate shards and scrambled names to catch positional matching."""

    def setUp(self):
        torch.set_num_threads(1)
        self.temporary = tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parents[1] / ".tmp")
        self.root = Path(self.temporary.name)
        self.base, self.modified = self.root / "base", self.root / "modified"
        self.base.mkdir()
        self.modified.mkdir()

    def tearDown(self):
        self.temporary.cleanup()

    def put(self, directory, values, file="weights.safetensors"):
        """Write a tiny shard without a framework checkpoint loader."""
        save_file(values, str(directory / file))

    def compare(self):
        """Keep report files beside the synthetic checkpoints."""
        return compare_weights(str(self.modified), str(self.base), self.root / "report.json")

    def projection_pair(self, other_direction=False):
        """Make two layers with a common output direction and unequal input widths."""
        generator = torch.Generator().manual_seed(4)
        base, modified = {}, {}
        for layer in range(2):
            for kind, width in (("self_attn.o_proj", 12), ("mlp.down_proj", 20)):
                name = f"model.layers.{layer}.{kind}.weight"
                weight = torch.randn(12, width, generator=generator)
                direction = torch.zeros(12)
                direction[1 if other_direction and "mlp" in kind else 0] = 1
                base[name] = weight
                modified[name] = weight - torch.outer(direction, direction @ weight)
        base["model.norm.weight"] = modified["model.norm.weight"] = torch.ones(12)
        self.put(self.base, base)
        self.put(self.modified, modified)

    def test_projection_and_saved_directions(self):
        self.projection_pair()
        report = self.compare()
        self.assertTrue(report["recipe_matching"]["matched"])
        self.assertEqual(report["recipe_matching"]["nearest_recipe"], "single-projection")
        self.assertEqual(len(report["summary"]["changed_set"]), 4)
        self.assertGreater(report["summary"]["direction_agreement"]["min_cosine"], 0.99999)
        with safe_open(self.root / report["directions_file"], framework="pt") as directions:
            self.assertEqual(len(list(directions.keys())), 8)
        json.loads((self.root / "report.json").read_text())

    def hybrid_pair(self, selected=False, other_direction=False, extra_changes=False):
        """Mix attention and expert blocks; only their output matrices get projected."""
        generator = torch.Generator().manual_seed(9)
        base, modified = {}, {}
        for layer, attention in enumerate(("self_attn.o_proj", "linear_attn.out_proj")):
            for projection in (attention, "mlp.down_proj", "mlp.experts.0.down_proj", "mlp.shared_expert.down_proj"):
                name = f"model.language_model.layers.{layer}.{projection}.weight"
                weight = torch.randn(12, 16, generator=generator)
                direction = torch.eye(12)[int(other_direction and attention == projection and layer == 1)]
                base[name] = weight
                modified[name] = weight.clone() if selected and layer == 0 else weight - torch.outer(direction, direction @ weight)
        for name in ("model.language_model.embed_tokens.weight", "model.language_model.layers.0.self_attn.q_proj.weight", "unknown.weight"):
            weight = torch.eye(12)
            base[name] = weight
            modified[name] = weight + torch.outer(torch.eye(12)[0], torch.eye(12)[0]) if extra_changes else weight
        self.put(self.base, base)
        self.put(self.modified, modified)

    def test_hybrid_all_layers_match(self):
        self.hybrid_pair()
        report = self.compare()
        self.assertEqual(report["recipe_matching"]["nearest_recipe"], "single-projection")
        self.assertTrue(report["recipe_matching"]["matched"])
        self.assertEqual(len(report["summary"]["changed_set"]), 8)
        self.assertEqual(report["summary"]["changed_without_svd"], [])
        self.assertGreater(report["summary"]["direction_agreement"]["cross_kind_min_cosine"], 0.99999)

    def test_selected_layer_matches_only_selected_envelope(self):
        self.hybrid_pair(selected=True)
        report = self.compare()
        matching = report["recipe_matching"]
        self.assertEqual(matching["nearest_recipe"], "single-projection-selected")
        self.assertTrue(matching["matched"])
        strict = next(item for item in matching["candidates"] if item["recipe"] == "single-projection")
        self.assertFalse(strict["matched"])
        skipped = matching["skipped_projections"]
        self.assertEqual(len(skipped), 4)
        self.assertEqual({item["layer"] for item in skipped}, {0})
        self.assertEqual({item["kind"] for item in skipped}, {"attention_output", "feed_forward_down", "expert_down", "shared_expert_down"})

    def test_changed_matrices_of_every_role_have_svd(self):
        self.hybrid_pair(extra_changes=True)
        report = self.compare()
        self.assertEqual(report["summary"]["changed_without_svd"], [])
        for name in report["summary"]["changed_set"]:
            self.assertIn("first_singular_energy_share", report["tensors"][name])
        self.assertFalse(report["recipe_matching"]["matched"])
        unexpected = {v["tensor"] for v in report["recipe_matching"]["violations"] if v["rule"] == "unexpected_change"}
        # The analytic lines take a changed embedding as an optional writer, so only two changes are unexpected.
        self.assertEqual(unexpected, {"model.language_model.layers.0.self_attn.q_proj.weight", "unknown.weight"})

    def test_hybrid_cross_kind_direction_failure(self):
        self.hybrid_pair(other_direction=True)
        report = self.compare()
        self.assertFalse(report["recipe_matching"]["matched"])
        self.assertIn("cross_kind_direction", {v["rule"] for v in report["recipe_matching"]["violations"]})

    def test_selected_projection_still_requires_rank_one(self):
        self.hybrid_pair(selected=True)
        name = "model.language_model.layers.1.linear_attn.out_proj.weight"
        weights = {key: TensorStore(self.modified).get(key) for key in TensorStore(self.modified).names}
        base = TensorStore(self.base).get(name)
        delta = torch.zeros_like(base)
        delta[0, 0] = delta[1, 1] = 1
        weights[name] = base + delta
        self.put(self.modified, weights)
        report = self.compare()
        self.assertFalse(report["recipe_matching"]["matched"])
        self.assertIn("first_energy_share", {v["rule"] for v in report["recipe_matching"]["violations"]})

    def test_selected_recipe_does_not_match_no_changes(self):
        values = {"model.layers.0.self_attn.o_proj.weight": torch.eye(4)}
        self.put(self.base, values)
        self.put(self.modified, values)
        report = self.compare()
        self.assertEqual(report["summary"]["assessment"], "unchanged")
        self.assertFalse(any(item["matched"] for item in report["recipe_matching"]["candidates"]))

    def test_rescore_needs_only_tensor_records(self):
        self.hybrid_pair(selected=True)
        report = self.compare()
        for row in report["tensors"].values():
            if row["kind"] == "linear_attention_output":
                row["kind"] = "other"
        report["summary"]["assessment"] = "recipe_violations"
        path = self.root / "saved.json"
        path.write_text(json.dumps(report))
        with patch("audit.weights.resolve_checkpoint", side_effect=AssertionError("checkpoint read")), patch("audit.weights.measure_tensor", side_effect=AssertionError("tensor measured")):
            rescored = rescore_weights(path)
        self.assertEqual(rescored["summary"]["assessment"], "recipe_match")
        self.assertEqual(rescored["recipe_matching"]["nearest_recipe"], "single-projection-selected")
        self.assertEqual(rescored["rescoring"]["previous_assessment"], "recipe_violations")
        for name, row in report["tensors"].items():
            for key in ("first_singular_energy_share", "singular_values", "energy_shares", "direction_cosine"):
                self.assertEqual(row.get(key), rescored["tensors"][name].get(key))

    def test_distinct_projection_directions_violate_recipe(self):
        self.projection_pair(other_direction=True)
        report = self.compare()
        self.assertIn("cross_kind_direction", [item["rule"] for item in report["recipe_matching"]["violations"]])

    def test_named_streaming_and_missing_names(self):
        self.put(self.base, {"z": torch.ones(3), "original_only": torch.ones(2)}, "one.safetensors")
        self.put(self.base, {"a": torch.ones(5)}, "two.safetensors")
        self.put(self.modified, {"a": torch.ones(5), "modified_only": torch.ones(2)}, "one.safetensors")
        self.put(self.modified, {"z": torch.ones(3)}, "two.safetensors")
        live = []
        largest = []
        get = TensorStore.get

        def watched(store, name):
            """Count live tensor objects before and after each single-tensor read."""
            gc.collect()
            tensor = get(store, name)
            live.append(weakref.ref(tensor))
            largest.append(sum(reference() is not None for reference in live))
            return tensor

        with patch.object(TensorStore, "get", watched):
            report = self.compare()
        self.assertLessEqual(max(largest), 2)
        self.assertEqual(report["original_only"], ["original_only"])
        self.assertEqual(report["modified_only"], ["modified_only"])
        self.assertEqual(report["tensors"]["a"]["relative_difference"], 0)
        self.assertEqual(report["tensors"]["z"]["relative_difference"], 0)
        self.assertFalse(report["recipe_matching"]["matched"])

    def test_index_and_duplicate_names(self):
        self.put(self.base, {"a": torch.ones(2)}, "one.safetensors")
        (self.base / "model.safetensors.index.json").write_text(json.dumps({"weight_map": {"a": "one.safetensors"}}))
        self.assertEqual(list(TensorStore(self.base).names), ["a"])
        (self.base / "model.safetensors.index.json").unlink()
        self.put(self.base, {"a": torch.ones(2)}, "two.safetensors")
        with self.assertRaisesRegex(ValueError, "duplicate tensor"):
            TensorStore(self.base)

    def test_index_cannot_escape_directory(self):
        (self.base / "model.safetensors.index.json").write_text(json.dumps({"weight_map": {"a": "../escape.safetensors"}}))
        with self.assertRaisesRegex(ValueError, "outside checkpoint"):
            TensorStore(self.base)

    def test_unchanged_checkpoint_has_empty_directions(self):
        self.put(self.base, {"a": torch.ones(3)})
        self.put(self.modified, {"a": torch.ones(3)})
        self.assertEqual(self.compare()["summary"]["assessment"], "unchanged")

    def test_big_remote_file_rejected_before_download(self):
        response = unittest.mock.Mock()
        response.json.return_value = {"sha": "abc", "siblings": [{"rfilename": "model.safetensors", "size": 1_000_000_001}]}
        with patch("audit.weights.requests.get", return_value=response) as get:
            with self.assertRaisesRegex(ValueError, "above the download limit"):
                resolve_checkpoint("owner/checkpoint", cache=self.root / "cache")
        self.assertEqual(get.call_count, 1)


def scored_row(kind, changed=True, relative=0.02, share=0.999, cosine=1.0, row_error=0.0):
    """Build one saved tensor record with only the fields the scorer reads."""
    row = {"kind": kind, "status": "ok", "changed": changed, "relative_difference": relative,
           "row_norms": {"preserved_equal": row_error == 0.0, "max_relative_error": row_error}}
    if changed:
        row.update(first_singular_energy_share=share, direction_cosine=cosine)
    return row


class RecipeRules(unittest.TestCase):
    """Score hand-built records, so each rule is seen apart from the measurement code."""

    line = {"status": "measured", "changed_kinds": ["attention_output"], "allow_unchanged_projections": False,
            "unchanged_relative_max": 0.001, "first_energy_min": 0.98, "direction_cosine_min": 0.999}
    agreement = {"cross_kind_min_cosine": None}

    def score(self, rows, recipes):
        return match_recipes(rows, [], self.agreement, recipes)

    def rules(self, rows, recipe):
        return [item["rule"] for item in self.score(rows, {"line": recipe})["violations"]]

    def test_leftover_rule(self):
        recipe = {**self.line, "residual_relative_max": 0.0025}
        # A 2 percent change with 98.5 percent in its first direction leaves 0.00245; 98.2 percent leaves 0.00268.
        self.assertEqual(self.rules({"a": scored_row("attention_output", share=0.985)}, recipe), [])
        violations = self.score({"a": scored_row("attention_output", share=0.982)}, {"line": recipe})["violations"]
        self.assertEqual([item["rule"] for item in violations], ["residual_relative"])
        self.assertAlmostEqual(violations[0]["value"], 0.02 * math.sqrt(0.018))
        self.assertEqual(violations[0]["maximum"], 0.0025)
        # A row with no energy share gets the energy flag but no leftover flag.
        self.assertEqual(self.rules({"a": scored_row("attention_output", share=None)}, recipe), ["first_energy_share"])
        self.assertEqual(self.rules({"a": scored_row("attention_output", share=0.982)}, self.line), [])

    def test_row_norm_rule(self):
        recipe = {**self.line, "row_norm_max_relative_error_max": 0.001}
        self.assertEqual(self.rules({"a": scored_row("attention_output", row_error=0.0005)}, recipe), [])
        violations = self.score({"a": scored_row("attention_output", row_error=0.005)}, {"line": recipe})["violations"]
        self.assertEqual(violations, [{"rule": "row_norm_change", "tensor": "a", "value": 0.005, "maximum": 0.001}])
        # The older yes-or-no check still applies to a table that asks for it.
        self.assertEqual(self.rules({"a": scored_row("attention_output", row_error=0.0005)}, {**self.line, "row_norms_preserved": True}),
                         ["row_norms_not_preserved"])

    def test_row_norm_line_ranks_first_at_equal_counts(self):
        rows = {"a": scored_row("attention_output", row_error=0.0005)}
        recipes = {"a-plain": self.line, "z-norm": {**self.line, "row_norm_max_relative_error_max": 0.001}}
        self.assertEqual(self.score(rows, recipes)["nearest_recipe"], "z-norm")
        rows["a"]["row_norms"]["max_relative_error"] = 0.005
        self.assertEqual(self.score(rows, recipes)["nearest_recipe"], "a-plain")

    def test_optional_kind_is_scored_only_when_changed(self):
        recipe = {**self.line, "optional_kinds": ["embedding"], "residual_relative_max": 0.0025}
        writer = scored_row("attention_output")
        self.assertEqual(self.rules({"a": writer, "e": scored_row("embedding", changed=False, relative=0.0)}, recipe), [])
        self.assertEqual(self.rules({"a": writer, "e": scored_row("embedding")}, recipe), [])
        self.assertEqual(self.rules({"a": writer, "e": scored_row("embedding", share=0.9)}, recipe), ["first_energy_share", "residual_relative"])
        self.assertEqual(self.rules({"a": writer, "e": scored_row("embedding")}, self.line), ["unexpected_change"])
        # An embedding change alone does not stand in for the projection.
        self.assertIn("missing_changed_projection", self.rules({"e": scored_row("embedding")}, recipe))

    def test_analytic_lines_carry_the_optional_embedding(self):
        table = recipe_table()
        for name in ("single-projection", "single-projection-selected"):
            self.assertEqual(table[name]["optional_kinds"], ["embedding"])
        for name in ("single-projection/mistral-small-3.2-24b", "norm-preserving/mistral-small-3.2-24b"):
            self.assertNotIn("optional_kinds", table[name])


if __name__ == "__main__":
    unittest.main()
