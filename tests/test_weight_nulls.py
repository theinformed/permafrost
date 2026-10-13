# test_weight_nulls.py -- Check the streamed residual on an analytic attention block.
# Created by LT Sean Egan, PhD 2026-10-13
# Modified: SDE 2026-10-13  test grouped heads and unequal prompt lengths.
"""Check a tiny forward pass whose attention averages preceding tokens."""

import tempfile
import unittest
from pathlib import Path

import torch
from safetensors.torch import save_file

from audit.nulls import middle_residual, prompts
from audit.weights import TensorStore


class NullResidual(unittest.TestCase):
    """Zero queries and keys make the attention answer available on paper."""

    def test_attention_average_and_padding(self):
        torch.set_num_threads(1)
        config = {"model_type": "llama", "hidden_act": "silu", "hidden_size": 4, "num_attention_heads": 2, "num_key_value_heads": 1,
                  "num_hidden_layers": 2, "rms_norm_eps": 1e-5, "rope_theta": 10000}
        embedding = torch.tensor([[1., 2., 3., 4.], [2., 1., 1., 3.], [3., 2., 2., 1.]])
        weights = {"model.embed_tokens.weight": embedding,
                   "model.layers.0.input_layernorm.weight": torch.ones(4), "model.layers.0.post_attention_layernorm.weight": torch.ones(4),
                   "model.layers.0.self_attn.q_proj.weight": torch.zeros(4, 4), "model.layers.0.self_attn.k_proj.weight": torch.zeros(2, 4),
                   "model.layers.0.self_attn.v_proj.weight": torch.eye(4)[:2].contiguous(), "model.layers.0.self_attn.o_proj.weight": torch.eye(4),
                   "model.layers.0.mlp.gate_proj.weight": torch.zeros(8, 4), "model.layers.0.mlp.up_proj.weight": torch.zeros(8, 4), "model.layers.0.mlp.down_proj.weight": torch.zeros(4, 8)}
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parents[1] / ".tmp") as temporary:
            save_file(weights, str(Path(temporary) / "model.safetensors"))
            store = TensorStore(temporary)
            actual = middle_residual(store, config, torch.tensor([[0, 1, 2], [1, 2, 0]]), torch.tensor([3, 2]))
            expected = []
            for tokens in ([0, 1, 2], [1, 2]):
                values = embedding[tokens]
                normalized = values / torch.sqrt(values.square().mean(-1, keepdim=True) + 1e-5)
                average = normalized[:, :2].mean(0)
                expected.append(values[-1] + average.repeat(2))
            torch.testing.assert_close(actual, torch.stack(expected).double(), rtol=1e-6, atol=1e-6)
            single = middle_residual(store, config, torch.tensor([[1, 2]]), torch.tensor([2]))
            torch.testing.assert_close(actual[1], single[0])

    def test_unsupported_position_scaling(self):
        config = {"model_type": "llama", "hidden_act": "silu", "rope_scaling": {"factor": 2}}
        with self.assertRaisesRegex(ValueError, "unscaled"):
            middle_residual(None, config, torch.tensor([[1]]), torch.tensor([1]))

    def test_prompt_count(self):
        directory = Path(__file__).resolve().parents[1] / "data/prompts"
        groups = prompts(directory)
        self.assertEqual(len(groups["harmful"]), 32)
        self.assertEqual(len(groups["harmless"]), 32)
        self.assertEqual(len(set(groups["harmful"] + groups["harmless"])), 64)


if __name__ == "__main__":
    unittest.main()
