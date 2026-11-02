# Reading of the Stage 1 and Stage 2 result: anlord/gemma-4-E2B-it-abliterated against google/gemma-4-E2B-it (2026-11-02)

Measured on Blueback, round 26 piece 7. The pull carries the measurements and the sweep record and no job log.
Modified revision `5d584569` (three commits on 2026-10-10 from 09:32Z to 09:35Z), original pinned at `3e22461f`
(07-20). The card describes the maker's own tool (Anlord Abliterator 1.6.0, native backend, "direct steering"):
a refusal direction per component from 400 harmless and 400 harmful prompts (mean method, orthogonalised against
the harmless mean, rank-1 subspace), input-side ablation under a Gaussian decay kernel, winsorisation at the 99.5th
percentile, `row_normalization: full` with a rank-3 correction, a 100-trial multi-objective search at seed 42 whose
trial 16 the repository ships (4 refusals in 100, KL divergence 2.9072, which the card calls "relatively high");
"all 35 decoder layers had their attention/MLP projections projected along the computed refusal direction", the
vision and audio towers untouched. Beside the weights the repository ships `abliteration_reproduction.json` with the
trial's four kernels: `attn.o_proj` 1.757 at position 23.78 falling to 0.676 at distance 2.72; `attn.qkv_in` 1.095
at 20.95 falling to 1.048 at distance 17.65; `mlp.down_proj` 1.766 at 12.61 falling to 0.358 at distance 12.18;
`mlp.gateup_in` 1.566 at 18.10 falling to 1.398 at distance 6.92. The `base_model` field names the original.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 28 flags, on the
cluster and after re-scoring at home: unexpected changes on the 14 gate and 14 up projections, which no entry
lists. On reading, the copy is the shipped record to the third decimal.

- 110 of 1,951 tensors changed: the down projections of layers 1 to 24, the queries of 4 to 34, the keys and
  values of 4 to 14, the gate and up projections of 12 to 25 and the attention outputs of 22 to 26. Nothing else
  moved; the largest relative change outside the changed set is exactly 0 and 1,841 tensors equal the original.
  The 60 shared-KV tensors are dropped by the export, which is why the keys and values stop at layer 14: from
  layer 15 the E2B reads earlier layers' keys and values and has none of its own to edit.
- One direction per matrix (first share 0.996 to 0.999), one direction per layer (every component of a layer agrees
  at 1.000), a direction that turns with the layer (0.05 to 0.93 against the group medians).
- The four kernels read off the kept fractions. Attention outputs (output side, the left kept fraction): -0.547 at
  layer 22, -0.713 at 23, -0.753 at 24 (the record's 1.757 at 23.78), -0.653 at 25, -0.450 at 26; the window is
  five layers because the record's minimum sits 2.72 layers from the peak. Queries, keys and values (input side,
  the right kept fraction, one number per layer on all three): -0.078 at layer 4, -0.095 at 21 (the record's 1.095
  at 20.95), -0.084 at 34, the three kinds equal to the third decimal in every layer. Down projections (output
  side): -0.252 at layer 1, -0.764 at 12 and -0.765 at 13 (the record's 1.766 at 12.61), -0.267 at 24. Gate and up
  projections (input side, equal to the third decimal in every layer): -0.512 at layer 12, -0.566 at 18 (the
  record's 1.566 at 18.10), -0.500 at 25.
- Rows moved by 0.002 to 0.040 (0.040 on layer 1's down projection, 0.028 on layer 25's up projection, 0.026 on
  layer 17's gate): the "full" row normalisation setting does not restore them.

| Layer | Down: change, E1, left kept | Query: change, E1, right kept | Key and value right kept | Gate and up right kept | Attention output: change, E1, left kept |
| --- | --- | --- | --- | --- | --- |
| 1 | 0.037, 0.999, -0.252 | | | | |
| 4 | 0.038, 0.999, -0.455 | 0.029, 0.998, -0.078 | -0.078, -0.078 | | |
| 9 | 0.055, 0.999, -0.705 | 0.027, 0.997, -0.086 | -0.085, -0.086 | | |
| 12 | 0.056, 0.999, -0.764 | 0.028, 0.997, -0.090 | -0.090, -0.089 | -0.512, -0.512 | |
| 14 | 0.047, 0.999, -0.757 | 0.027, 0.997, -0.092 | -0.092, -0.092 | -0.539, -0.539 | |
| 18 | 0.048, 0.999, -0.634 | 0.025, 0.996, -0.095 | | -0.566, -0.566 | |
| 21 | 0.040, 0.998, -0.468 | 0.028, 0.997, -0.095 | | -0.552, -0.552 | |
| 24 | 0.035, 0.998, -0.267 | 0.026, 0.996, -0.095 | | -0.515, -0.515 | 0.046, 0.999, -0.753 |
| 26 | | 0.026, 0.996, -0.093 | | | 0.034, 0.998, -0.450 |
| 34 | | 0.027, 0.997, -0.084 | | | |

The full table (110 rows) is in the report. The fingerprint's first shard (`9ebcea1985`, the embeddings under the
library's three-shard layout) equals the first shard of three earlier copies on this original (aifeifei798's,
amkkk's, prithivMLmods's); the edits share no measured field with any.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home. Under transformers 5.22.1 `text_config.moe_intermediate_size`
(null in a 5.19.0 save) closes by the default rule. What remains is the 5.16 `per_layer_config` form
(`global_head_dim` 512 and `num_global_key_value_heads` 1 moved into a per-layer map), the ninth copy on it and the
first E2B, and `vision_config.rope_parameters.rope_type` written as `axial` where the original says `default`, the
5.19 library's name for the same vision rotary scheme, the first copy to carry it; both closed by hand. The template
is Google's 18,569-byte Canonical file on both sides and the fixed conversation renders identically.

## For the recipe library

An entry naming seven components under four kernels (the attention outputs and down projections on the output
side, the queries, keys and values and the gate and up projections on the input side, one direction per layer)
would count none of the 28 flags and would read every one of the record's eight numbers from the kept fractions,
as this reading does by hand (finding 59). The card's "all 35 decoder layers" is the kernels' reach taken together
(layers 1 to 34); each component has its own window, and the claim of restored rows does not hold. The pull copy
keeps the direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/blueback26/measurements/pair-7/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
