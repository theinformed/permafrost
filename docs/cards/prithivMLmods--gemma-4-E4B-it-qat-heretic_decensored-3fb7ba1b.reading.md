# Reading of the Stage 1 and Stage 2 result: prithivMLmods/gemma-4-E4B-it-qat-heretic_decensored against google/gemma-4-E4B-it-qat-q4_0-unquantized (2026-11-02)

Measured on Nautilus, round 34 piece 4 (download job 4163806, compare job 4163810, sweep 4163815; the pull of
11-01 21:23Z carries the measurements and the sweep record and no job log). Modified revision `2bbaa270` (15
commits: created 2026-06-17 at 06:07Z with a README, the weights, tokenizer and processor on 06-18 between
10:24Z and 10:34Z, nine README edits to 14:15Z), original pinned at `dfc5b925`, the QAT-unquantized checkpoint
of the E4B, the first copy on this original in the census. The card (6,209 bytes) prints Heretic's table:
direction index 33.23, attention output kernel 1.37 at position 32.40 falling to 1.16 at distance 15.15, down
projection kernel 1.23 at 35.47 falling to 0.89 at distance 24.37, KL divergence 0.0140, refusals 40 of 100
against 99 of 100. The field `base_model` names the QAT checkpoint. The maker's sixth copy in the census after
the Heretic-Stable re-save and the four Uncensored-MAX duplicates (finding 9), and the first that is the maker's
own edit.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection-selected`, 3 flags, on the
cluster and after re-scoring at home: two direction cosines (0.939 and 0.943 at layers 38 and 39) and the
cross-kind cosine. On reading, the copy is a Heretic linear-kernel edit whose two windows read to the layer,
whose down kernel reads a tenth or two under its shape and whose attention heights scatter.

- 54 of 2,076 tensors changed: the down projections of layers 12 to 41 (30) and the attention outputs of 18 to
  41 (24) of 42. The attention kernel reaches 32.40 plus or minus 15.15 (17.25 to 47.55), layers 18 to 41; the
  down kernel 35.47 plus or minus 24.37 (11.10 to 59.84), layers 12 to 41. Both windows read exactly. Nothing
  else moved; the largest relative change outside the changed set is exactly 0, which places the copy on the QAT
  checkpoint (finding 48).
- One direction, nearly: the 54 leading vectors stand at 0.94 to 0.998 to the group reference, first shares
  0.992 to 0.997. Output side on 51 of 54; the attention outputs of layers 31, 37 and 39 read the left above the
  right.
- The down kernel reads under its shape. One minus the left kept fraction runs 0.81 at layer 12, 0.82 at 16,
  0.89 at 20, 1.02 at 24, 1.11 at 31 and 32, 0.88 at 36, 1.08 at 40 and 1.02 at 41, where the kernel runs 0.90,
  0.96, 1.01, 1.07, 1.17, 1.18, 1.22, 1.17 and 1.15: the slope is there and the heights sit 0.05 to 0.24 under,
  0.35 under at layer 36.
- The attention heights scatter: 1.09 to 1.19 on layers 24 to 27 and 1.11 at 41 where the kernel runs 1.25 to
  1.30 and 1.25, 1.05 at 35 against 1.33, and 0.44, 0.67, 0.29 and 0.33 at layers 18, 32, 37 and 39 against 1.17,
  1.36, 1.31 and 1.28: finding 46's scatter, on the E4B's QAT checkpoint, where the four E4B exports of round 33
  on the instruct model read their heights within 0.3 at the peak (finding 59).
- Rows moved 0.0034 to 0.0093, Heretic's band; no restoration is claimed.

| Layer | Attention output: change, E1, left kept, right kept, read, kernel | Down projection: change, E1, left kept, right kept, read, kernel | Rows |
| --- | --- | --- | --- |
| 12 | - | 0.0180, 0.992, 0.19, 0.35, 0.81, 0.90 | -, 0.0034 |
| 14 | - | 0.0187, 0.993, 0.25, 0.39, 0.75, 0.93 | -, 0.0037 |
| 16 | - | 0.0192, 0.993, 0.18, 0.44, 0.82, 0.96 | -, 0.0038 |
| 18 | 0.0237, 0.995, 0.56, 0.62, 0.44, 1.17 | 0.0194, 0.993, 0.22, 0.46, 0.78, 0.99 | 0.0065, 0.0046 |
| 20 | 0.0231, 0.995, 0.36, 0.71, 0.64, 1.20 | 0.0199, 0.994, 0.11, 0.45, 0.89, 1.01 | 0.0073, 0.0045 |
| 22 | 0.0246, 0.996, 0.30, 0.59, 0.70, 1.23 | 0.0207, 0.994, 0.19, 0.29, 0.81, 1.04 | 0.0057, 0.0040 |
| 24 | 0.0250, 0.996, -0.09, 0.55, 1.09, 1.25 | 0.0213, 0.995, -0.02, 0.21, 1.02, 1.07 | 0.0053, 0.0035 |
| 26 | 0.0252, 0.996, -0.18, 0.62, 1.18, 1.28 | 0.0221, 0.995, -0.00, 0.27, 1.00, 1.10 | 0.0053, 0.0045 |
| 28 | 0.0261, 0.996, 0.17, 0.61, 0.83, 1.31 | 0.0231, 0.995, 0.05, 0.25, 0.95, 1.13 | 0.0063, 0.0042 |
| 30 | 0.0288, 0.997, 0.35, 0.51, 0.65, 1.34 | 0.0242, 0.996, -0.04, 0.13, 1.04, 1.15 | 0.0085, 0.0053 |
| 31 | 0.0280, 0.996, 0.55, 0.51, 0.45, 1.35 | 0.0239, 0.996, -0.11, 0.13, 1.11, 1.17 | 0.0076, 0.0059 |
| 32 | 0.0254, 0.996, 0.33, 0.65, 0.67, 1.36 | 0.0226, 0.995, -0.11, 0.15, 1.11, 1.18 | 0.0066, 0.0048 |
| 34 | 0.0276, 0.997, 0.30, 0.51, 0.70, 1.35 | 0.0227, 0.995, -0.03, 0.19, 1.03, 1.21 | 0.0054, 0.0058 |
| 35 | 0.0276, 0.996, -0.05, 0.69, 1.05, 1.33 | 0.0226, 0.995, -0.05, 0.30, 1.05, 1.22 | 0.0072, 0.0070 |
| 36 | 0.0275, 0.996, 0.29, 0.59, 0.71, 1.32 | 0.0233, 0.995, 0.12, 0.18, 0.88, 1.22 | 0.0082, 0.0067 |
| 37 | 0.0256, 0.996, 0.71, 0.63, 0.29, 1.31 | 0.0229, 0.995, -0.08, 0.19, 1.08, 1.21 | 0.0075, 0.0056 |
| 38 | 0.0236, 0.995, 0.54, 0.61, 0.46, 1.29 | 0.0230, 0.995, -0.05, 0.19, 1.05, 1.19 | 0.0093, 0.0067 |
| 39 | 0.0250, 0.996, 0.67, 0.63, 0.33, 1.28 | 0.0223, 0.995, -0.09, 0.19, 1.09, 1.18 | 0.0071, 0.0053 |
| 40 | 0.0238, 0.995, 0.69, 0.75, 0.31, 1.26 | 0.0221, 0.995, -0.08, 0.17, 1.08, 1.17 | 0.0069, 0.0053 |
| 41 | 0.0223, 0.995, -0.11, 0.59, 1.11, 1.25 | 0.0219, 0.995, -0.02, 0.21, 1.02, 1.15 | 0.0053, 0.0041 |

The copy's four shards are `62cfc14d`, `cbe428b1`, `28f2bf73` and `8080cb1a`. The fourth is the vision tower
alone in the library's four-shard layout and equals the fourth shard of the seven instruct-model E4B exports
(finding 71), so the QAT checkpoint's vision tower is the instruct model's. A byte-range read from the hub
(`tools/hub_range_read.py`) confirms it: `model.vision_tower.encoder.layers.0.mlp.down_proj.linear.weight` is
byte-equal between google/gemma-4-E4B-it-qat-q4_0-unquantized at `dfc5b925` and google/gemma-4-E4B-it at
`fee6332c`, while layer 20's attention output differs between the two by 0.155 of its norm, and the QAT file's
values sit on a grid (a median 24 distinct values per block of 64, 11 percent exact zeros) where the instruct
file's do not (62 per block, no zeros).

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home: the two version strings (5.6.2 to 5.12.1) are all
that differ. The template is the pin's 16,804-byte file and the fixed conversations render identically.

## For the recipe library

The single-projection entry is the nearest because the 54 directions nearly coincide; the copy is a Heretic
kernel edit whose windows the reading tests and whose heights it reads on the down projections and not on the
attention outputs. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus34/measurements/pair-4/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
