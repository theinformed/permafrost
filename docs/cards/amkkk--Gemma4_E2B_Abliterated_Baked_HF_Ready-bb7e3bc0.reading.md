# Reading of the Stage 1 and Stage 2 result: amkkk/Gemma4_E2B_Abliterated_Baked_HF_Ready against google/gemma-4-E2B-it (2026-11-01)

Measured on Nautilus, round 32 piece 7 (download job 4145233, compare job 4145240, 399 seconds, sweep 4145242).
Modified revision `9cea12fb` (four commits on 2026-04-13 between 21:18Z and 22:23Z: the weights at 21:19Z as
"Upload Gemma 4 Step 1 baked release" and two README edits), original pinned at `b4a60110`, the revision current
when the repository was created. The card is unusual in where it puts its numbers: twelve fields in
`config.json` and an `export_manifest.json` beside it carry the edit's parameters, `ablation_layers` (9 to 13, 15
to 32 and 34, twenty-four layers), `self_attn_o_strength` 1.0, `mlp_down_strength` 1.0, `mlp_gate_strength` 1.2,
`mlp_up_strength` 1.2, `direction_source` "module_input_directions", `direction_source_layer`, `ablation_scope`,
`target_weights`, `export_source_model` (the original) and `export_type` "static_baked_step1_module_input". The
README describes a step-one export with the directions baked into the weights. The `base_model` field names the
original.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 136 flags, on the
cluster and after re-scoring at home: 48 unexpected changes on the gate and up projections, 48 within-layer
cosines of 0.11 to 0.71 and 40 first shares of 0.977 to 0.990 on the attention outputs and down projections. On
reading, every number in the configuration reads back from the weights (finding 47).

- 96 of 1,951 tensors changed: the attention output, the down projection, the gate projection and the up
  projection of the twenty-four listed layers, and nothing else: layers 14 and 33, which the list skips, are
  unchanged, as are the queries, the keys and values, every norm, the embeddings and the towers. The
  largest relative change outside the changed set is exactly 0 and 1,855 tensors equal the original.
- The export drops 60 tensors the original carries: the key projection, the value projection and the key norm
  of layers 15 to 34, which share the keys and values of earlier layers and are never read by the model (the
  comparison lists them as `original_only` and `unused_shared_kv`). The copy's first two shards equal
  huihui-ai's E2B file's and aifeifei798's, the library's sharding of the per-layer embeddings, with no measured
  field shared.
- Rank one on all 96: first share 0.977 to 0.994 on the attention outputs and down projections, 0.9966 to
  0.9984 on the gate and up projections.
- Input side on all 96: the left kept fraction is above the right on 96 of 96. The right kept fraction is the
  configuration's strengths: -0.0235 to 0.0077 on the 24 attention outputs and 0.0004 to 0.0072 on the 24 down
  projections, which is one minus a strength of 1.0, and -0.1991 to -0.2004 on the 24 gate projections and
  -0.1993 to -0.2004 on the 24 up projections, which is one minus 1.2. The left runs 0.84 to 1.00 on the
  attention outputs, 0.87 to 0.98 on the down projections, 0.08 to 0.66 on the gate projections and 0.02 to 0.40
  on the up projections, the part of each matrix's output that the removed input direction carried.
- One direction per module input: the gate and up projections of a layer, which read the same input, share
  their direction at 0.92 to 0.97; the attention output and the down projection agree with each other at 0.11
  to 0.71 and with the group reference at 0.09 to 0.40. "module_input_directions", as the configuration says.
- Rows moved by 0.0005 to 0.0054 on the attention outputs, 0.0005 to 0.0016 on the down projections, 0.008 to
  0.049 on the gate projections and 0.006 to 0.038 on the up projections, unrestored.
- Relative changes of 0.009 to 0.019 on the attention outputs, 0.008 to 0.013 on the down projections and 0.027
  to 0.040 on the gate and up projections, the 1.2 strength showing as the larger change.

| Layer | Attention output: change, E1, left kept, right kept | Down projection: change, E1, left kept, right kept | Gate projection: change, E1, left kept, right kept | Up projection: change, E1, left kept, right kept | Gate-up cosine |
| --- | --- | --- | --- | --- | --- |
| 9 | 0.0101, 0.980, 0.97, 0.005 | 0.0125, 0.989, 0.87, 0.002 | 0.0397, 0.998, 0.51, -0.200 | 0.0326, 0.998, 0.35, -0.200 | 0.97 |
| 12 | 0.0132, 0.987, 0.85, 0.002 | 0.0115, 0.988, 0.95, -0.003 | 0.0309, 0.997, 0.59, -0.200 | 0.0306, 0.997, 0.36, -0.200 | 0.95 |
| 15 | 0.0150, 0.990, 0.92, 0.001 | 0.0104, 0.985, 0.90, 0.004 | 0.0318, 0.998, 0.32, -0.200 | 0.0328, 0.998, 0.21, -0.200 | 0.96 |
| 19 | 0.0104, 0.983, 0.98, 0.008 | 0.0105, 0.985, 0.93, 0.003 | 0.0316, 0.998, 0.37, -0.200 | 0.0306, 0.997, 0.19, -0.200 | 0.96 |
| 23 | 0.0122, 0.986, 0.90, 0.001 | 0.0104, 0.986, 0.89, 0.003 | 0.0288, 0.997, 0.38, -0.199 | 0.0286, 0.997, 0.15, -0.200 | 0.94 |
| 27 | 0.0110, 0.987, 0.97, -0.001 | 0.0089, 0.979, 0.91, 0.004 | 0.0281, 0.997, 0.35, -0.200 | 0.0285, 0.997, 0.11, -0.200 | 0.93 |
| 31 | 0.0113, 0.988, 1.00, -0.024 | 0.0092, 0.978, 0.93, 0.005 | 0.0290, 0.997, 0.08, -0.200 | 0.0299, 0.997, 0.02, -0.200 | 0.93 |
| 34 | 0.0109, 0.991, 0.98, -0.002 | 0.0089, 0.985, 0.98, 0.007 | 0.0275, 0.997, 0.35, -0.200 | 0.0273, 0.997, 0.27, -0.200 | 0.95 |

The right kept fraction is one minus the configuration's strength on every row; the full table (24 layers) is in
the report.

The fingerprint shares no measured field with the five earlier reports on the E2B original or with DavidAU's
copy of this round.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster, thirteen fields, twelve at home: the twelve the maker added to
`config.json` to document the edit, which no library writes and no loader reads, and which the weights agree with
in every value. `text_config.moe_intermediate_size` (null in the 5.5.3 save, absent in Google's file) closed by
the default rule at home, where the cluster had counted it. The template is Google's pinned file and the fixed
conversation renders identically. Nothing to close: the fields are the card.

## For the recipe library

The cleanest read-back in the census: a maker who wrote the strengths into the configuration, and a measure that
returns them to the third decimal on 96 matrices of four writers. The recipe table counts 136 flags because no
entry names the gate and up projections as writers or the input side as the side; an entry for a per-module
input-side projection with four writers and a strength per writer would count none, and this copy is its
calibration. A rule that reads a maker's documentation fields in `config.json` as documentation is owed to the
metadata tool. The pull copy keeps the direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus32/measurements/pair-7/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
