# test_weights.py -- Check tensor measures against small matrices with known answers.
# Created by LT Sean Egan, PhD 2026-10-13
# Modified: SDE 2026-10-13  cover rank, row norms, shard names, and streaming.
"""Small analytic checks for the checkpoint comparison."""

import gc
import json
import tempfile
import unittest
import weakref
from pathlib import Path
from unittest.mock import patch

import torch
from safetensors import safe_open
from safetensors.torch import save_file

from audit.weights import TensorStore, compare_weights, direction_agreement, measure_tensor, resolve_checkpoint, tensor_kind


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


if __name__ == "__main__":
    unittest.main()
