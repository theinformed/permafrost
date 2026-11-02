# Reading of the Stage 1 and Stage 2 result: sh0ck0r/gemma-4-26B-A4B-it-heretic against google/gemma-4-26B-A4B-it (2026-11-01)

Measured on Nautilus, round 32 piece 1 (download job 4145233, compare job 4145234, 1,367 seconds, sweep 4145242).
Modified revision `39023804` (eleven commits on 2026-05-25 from 02:37Z to 08:49Z: the weights at 02:39Z, the
tokenizer, the README, a `reproduce/` folder with the tool's configuration and trial record, and a folder upload
six hours later), original pinned at `b2a81a03` (05-18), the revision current when the repository was created.
The card prints the Heretic 1.3.0 record: trial 197, the attention outputs at weight 1.48 centred on layer 22.07
(minimum 1.13, width 13.78), the down projections at 1.10 centred on 24.74 (minimum 0.32, width 12.58), a KL
divergence of 0.0701 and 28 refusals in 100 against the original. The `base_model` field names the original.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 19 flags, on the
cluster and after re-scoring at home: seven first shares of 0.967 to 0.988 on the down projections nearest the
window's edge and twelve within-layer cosines of 0.88 to 0.95. On reading, the footprint is the card's two
kernels to the layer, one direction per matrix on the output side, and the kept fractions follow both kernels'
shapes with the read shallower than the card.

- 38 of 1,013 tensors changed: the attention outputs of layers 9 to 29 (21 matrices) and the shared dense down
  projections of layers 13 to 29 (17). The attention kernel centred on 22.07 with width 13.78 reaches 8.29 to
  35.85 of a 30-layer model, the down kernel centred on 24.74 with width 12.58 reaches 12.16 to 37.32: layers 9
  to 29 and 13 to 29 exactly. The 30 packed expert tensors, the routers, the other projections and the vision
  tower are unchanged; the largest relative change outside the changed set is exactly 0 and 975 tensors equal
  the original.
- One direction per matrix: first share 0.967 to 0.998, the two writers of a layer agreeing at 0.88 to 0.98
  (1.000 on layers 9 to 12, where only the attention output is edited), the leading directions drifting across
  layers at 0.26 to 0.82 to the group reference. The per-layer directions of Heretic 1.3.
- Output side on 36 of 38: the left kept fraction is below the right everywhere but on the attention outputs of
  layers 19 and 27, where the left reads 0.64 and 0.52. On the attention outputs the left runs from 0.27 at layer
  9 to -0.39 at 24 and -0.18 at 29, where the kernel's one-minus-weight runs -0.15, -0.43, -0.30: within 0.12
  from layer 17 to 29 and 0.2 to 0.5 shallower on 9 to 13. On the down projections the left runs from 0.65 at
  layer 13 to 0.02 at 24 and 0.44 at 29, where the kernel gives 0.63, -0.05, 0.16: within 0.07 at layers 13, 19,
  24, up to 0.17 across 16 to 25, and 0.20 to 0.28 shallower on 27 to 29. The weights along the leading direction
  are 0.36 to 1.39 on the attention outputs and 0.35 to 0.98 on the down projections.
- Rows moved by 0.004 to 0.040, unrestored.
- Relative changes of 0.025 to 0.036 on the attention outputs and 0.007 to 0.026 on the down projections, the
  down kernel's weight falling to 0.32 at its edge.

| Layer | Attention output: change, E1, left kept, right kept, kernel 1-w | Down projection: change, E1, left kept, right kept, kernel 1-w | Within-layer cosine | Row norms |
| --- | --- | --- | --- | --- |
| 9 | 0.0303, 0.997, 0.27, 0.47, -0.15 | - | - | 0.0161, - |
| 13 | 0.0306, 0.996, -0.03, 0.43, -0.25 | 0.0070, 0.967, 0.65, 0.93, 0.63 | 0.943 | 0.0206, 0.0101 |
| 16 | 0.0298, 0.997, 0.02, 0.46, -0.33 | 0.0100, 0.982, 0.59, 0.89, 0.44 | 0.949 | 0.0134, 0.0109 |
| 19 | 0.0332, 0.998, 0.64, 0.32, -0.40 | 0.0148, 0.990, 0.33, 0.85, 0.26 | 0.901 | 0.0187, 0.0199 |
| 21 | 0.0320, 0.997, -0.37, 0.32, -0.45 | 0.0165, 0.992, 0.22, 0.79, 0.13 | 0.970 | 0.0143, 0.0117 |
| 24 | 0.0313, 0.998, -0.39, 0.21, -0.43 | 0.0201, 0.994, 0.02, 0.77, -0.05 | 0.977 | 0.0086, 0.0101 |
| 25 | 0.0254, 0.996, -0.33, 0.39, -0.41 | 0.0208, 0.994, 0.09, 0.82, -0.08 | 0.984 | 0.0044, 0.0059 |
| 27 | 0.0297, 0.996, 0.52, 0.42, -0.36 | 0.0243, 0.996, 0.26, 0.78, 0.04 | 0.881 | 0.0065, 0.0132 |
| 29 | 0.0249, 0.996, -0.18, 0.32, -0.30 | 0.0258, 0.988, 0.44, 0.88, 0.16 | 0.959 | 0.0066, 0.0404 |

The kernel column is one minus the card's weight at that layer, from the four numbers the card prints for each
writer; the full table (38 rows) is in the report.

The fingerprint shares no measured field with the ten earlier reports on this original or with BinxNet's copy of
this round. Its first two shards equal BinxNet's (`a868d472`, `a3de0db5`) and its first equals SevenOfNine's: the
library's 11-shard layout of the embeddings and the first eight layers, which none of the three edits touches.

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home: the two version strings (5.5.0.dev0 to 5.9.0) and
nothing else. The template is Google's pinned file and the fixed conversation renders identically.

## For the recipe library

The card's windows to the layer, one direction per matrix, output side, and kernels that read back in shape with
the read shallower by 0.04 to 0.12 across the centre of both windows and by up to 0.4 at their edges. The
`directional-per-layer-selected` entry fits the shape; its 0.95 within-layer line counts twelve of the layers,
as it does on about half the layers of every per-layer Heretic copy measured, and the 0.99 first-share floor
counts the down projections whose kernel weight is under 0.5. The pull copy keeps the direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus32/measurements/pair-1/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
