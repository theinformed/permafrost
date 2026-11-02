# Reading of the Stage 1 and Stage 2 result: treadon/gemma4-E4B-it-Abliterated-AND-Disinhibited-USE-THIS against google/gemma-4-E4B-it (2026-11-01)

Measured on Blueback, round 25 piece 5. The pull carries the measurements and the sweep record and no job log.
Modified revision `40999e05` (six commits from 2026-04-29 19:11Z to 05-01: the model, the tokenizer and three README
updates), original pinned at `c53e9d33` (04-28), the revision current when the repository was created. The card
says the copy composes two of the maker's edits in sequence: first a "disinhibition" that removes a neutrality
direction (the hedging the model adds to opinions) from the top 20 layers at scale 1.5, then the abliteration of
piece 4 recomputed on the disinhibited model on the top 17 layers at scale 1.0, both norm-preserving projections on
`self_attn.o_proj` and `mlp.down_proj`. It reports the hedge rate on the maker's opinion set at 8.3 percent and
over-refusal at 0. The `base_model` field names the original.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 32 flags, on the
cluster and after re-scoring at home: 32 first shares of 0.66 to 0.76, the two writers of the 16 layers both edits
touch. On reading, the copy is the two edits the card describes, each readable on its own layers at its own scale,
and the layer the abliteration alone touches is the piece 4 edit to the last digit.

- 42 of 2,076 tensors changed: the attention output and the down projection of layers 17 to 20 and 24 to 40, 21
  layers. Nothing else moved; the largest relative change outside the changed set is exactly 0 and 2,034 tensors
  equal the original. The 54 shared-KV tensors are dropped by the export.
- Three kinds of layer. Layer 17 carries one direction at a left kept fraction of 0.000 (scale 1.0), and both its
  matrices equal piece 4's in every measured field: the abliteration alone. Layers 20, 29, 39 and 40 carry one
  direction (first share 0.994 to 0.998) at a left kept fraction of -0.498 to -0.525 (scale 1.5): the disinhibition
  alone. The 16 other layers (18, 19, 24 to 28, 30 to 38) carry two directions: first share 0.66 to 0.76, fourth
  cumulative share 0.993 to 0.998, the leading direction's left kept fraction -0.47 to -0.53, the disinhibition's
  1.5 leading and the abliteration's 1.0 behind it.
- So the disinhibition touched 20 layers (18, 19, 20, 24 to 40) and the abliteration 17 (17, 18, 19, 24 to 28, 30 to
  38): the card's L = 20 and L = 17. The abliteration's 17 are not piece 4's 17 (17 to 21, 24 to 35): recomputed on
  the disinhibited model, the signal ranked layers 36 to 38 above 20, 21, 29 and 35.
- Output side on 42 of 42 along the leading direction; the right kept fraction is 0.02 to 0.44 on the down
  projections and 0.55 to 0.93 on the attention outputs.
- Rows moved by at most 0.0004: both restorations hold.
- Relative change 0.022 to 0.044, the two-direction layers at 0.034 to 0.044 against piece 4's 0.018 to 0.024.

| Layer | Attention output: change, E1, E4, left kept, right kept | Down projection: change, E1, E4, left kept, right kept | Edits read |
| --- | --- | --- | --- |
| 17 | 0.0221, 0.994, 0.994, -0.000, 0.672 | 0.0231, 0.995, 0.995, 0.000, 0.442 | abliteration (equals piece 4) |
| 18 | 0.0342, 0.679, 0.996, -0.492, 0.619 | 0.0436, 0.693, 0.997, -0.497, 0.140 | both |
| 20 | 0.0290, 0.996, 0.996, -0.498, 0.701 | 0.0365, 0.998, 0.998, -0.500, 0.213 | disinhibition |
| 25 | 0.0385, 0.686, 0.995, -0.481, 0.652 | 0.0401, 0.690, 0.996, -0.496, 0.019 | both |
| 29 | 0.0351, 0.996, 0.997, -0.498, 0.555 | 0.0380, 0.997, 0.998, -0.500, 0.090 | disinhibition |
| 33 | 0.0407, 0.743, 0.995, -0.522, 0.846 | 0.0341, 0.659, 0.995, -0.501, 0.330 | both |
| 38 | 0.0341, 0.705, 0.995, -0.502, 0.724 | 0.0361, 0.690, 0.996, -0.501, 0.357 | both |
| 40 | 0.0306, 0.994, 0.995, -0.513, 0.876 | 0.0306, 0.997, 0.997, -0.498, 0.322 | disinhibition |

The full table (42 rows) is in the report.

The fingerprint shares the two matrices of layer 17 with piece 4 in every field and no field with the eleven earlier reports on this original or with the other copies of this round.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster; "consistent with re-save noted" at home. Under transformers 5.22.1
`text_config.moe_intermediate_size` (null in a 5.5.3 save) closes by the default rule, and what remains is the
version strings. The template is Google's pinned file and the fixed conversation renders identically.

## For the recipe library

Two norm-preserving per-layer projections in sequence read as two directions on the layers both reach and one on
the layers one reaches, with each scale readable where its direction leads (1.5 to within 0.03 on the 20 layers,
1.0 to within 0.001 on layer 17). An entry for a composed edit would read the fourth cumulative share against 0.99
and a scale per direction; the per-layer entry counts 32 first shares because two directions are not one. The pull
copy keeps the direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/blueback25/measurements/pair-5/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
