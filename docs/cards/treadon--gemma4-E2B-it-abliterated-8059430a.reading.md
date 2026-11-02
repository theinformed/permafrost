# Reading of the Stage 1 and Stage 2 result: treadon/gemma4-E2B-it-abliterated against google/gemma-4-E2B-it (2026-11-01)

Measured on Blueback, round 25 piece 7. The pull carries the measurements and the sweep record and no job log.
Modified revision `e0b7d84d` (eight commits from 2026-04-13 21:51Z to 05-01: the folder upload and six README
updates), original pinned at `b4a60110` (04-10), the revision current when the repository was created. The card
describes the maker's norm-preserving biprojected abliteration on this family: 100 harmful and 100 harmless
prompts, activations winsorised at the 99.5th percentile, a per-layer difference of means biprojected against the
harmless mean, the direction projected out of `self_attn.o_proj` and `mlp.down_proj` on the top 24 of 35 layers
with the row norms restored, scale 1.75, single pass, all projection arithmetic in float32; 0 refusals on the
maker's 200-prompt set and 0 over-refusals on 50. The `base_model` field names the original.

## Weights (Stage 2)

The tool's assessment was "recipe match", recipe `directional-per-layer-selected`, 0 flags, on the cluster and
after re-scoring at home. On reading, the copy is the card's edit to the number: 24 layers, one direction per
layer, scale 1.75 on every matrix, rows restored.

- 48 of 1,951 tensors changed: the attention output and the down projection of layers 9 to 13 and 15 to 33, 24
  layers. Nothing else moved; the largest relative change outside the changed set is exactly 0 and 1,903 tensors
  equal the original. The 60 shared-KV tensors are dropped by the export.
- One direction per layer: the two writers of a layer agree at 1.000, and across layers the directions agree at a
  median of 0.44 (minimum 0.07).
- Scale 1.75 on the output side: the left kept fraction is -0.744 to -0.760 on all 48 (within 0.01 of -0.75 on 46
  of them), the right -0.41 to 0.39 on the down projections and 0.18 to 0.76 on the attention outputs, the left
  below the right on 48 of 48.
- Rows moved by at most 0.0003: restored, as the card says.
- First share 0.997 to 0.999 at relative changes of 0.039 to 0.055, above the floor's reach at this edit size.

| Layer | Attention output: change, E1, left kept, right kept | Down projection: change, E1, left kept, right kept | Within-layer cosine | Row norms |
| --- | --- | --- | --- | --- |
| 9 | 0.0471, 0.998, -0.749, 0.180 | 0.0534, 0.998, -0.749, -0.070 | 1.000 | 0.0002, 0.0002 |
| 12 | 0.0479, 0.997, -0.746, 0.429 | 0.0550, 0.997, -0.747, 0.394 | 1.000 | 0.0002, 0.0002 |
| 16 | 0.0436, 0.997, -0.753, 0.521 | 0.0476, 0.998, -0.747, -0.249 | 1.000 | 0.0003, 0.0002 |
| 22 | 0.0457, 0.997, -0.760, 0.731 | 0.0475, 0.999, -0.750, -0.210 | 1.000 | 0.0003, 0.0001 |
| 27 | 0.0438, 0.997, -0.747, 0.632 | 0.0441, 0.998, -0.752, 0.020 | 1.000 | 0.0002, 0.0001 |
| 30 | 0.0447, 0.998, -0.747, 0.462 | 0.0455, 0.999, -0.750, -0.357 | 1.000 | 0.0002, 0.0001 |
| 33 | 0.0442, 0.998, -0.748, 0.241 | 0.0482, 0.999, -0.749, -0.408 | 1.000 | 0.0003, 0.0001 |

The full table (48 rows) is in the report.

The fingerprint shares no measured field with the ten earlier reports on this original or with the maker's
composed copy of this round (piece 8), which changes the same 48 tensors with no field equal. The layer set is
amkkk's and WWTCyberLab's 24 (round 32 and round 22) with layer 34 traded for layer 33.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster; "consistent with re-save noted" at home. Under transformers 5.22.1
`text_config.moe_intermediate_size` (null in a 5.5.3 save) closes by the default rule, and what remains is the
version strings. The template is Google's pinned file and the fixed conversation renders identically.

## For the recipe library

The `directional-per-layer-selected` entry fits with no flag, and the scale reads back as 1.75 to within 0.01 on
46 of 48 matrices: the shape finding 24 reads on TrevorJS's copies, from another maker, with the scale stated
and read. The pull copy keeps the
direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/blueback25/measurements/pair-7/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
