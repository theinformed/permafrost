# Reading of the Stage 1 and Stage 2 result: BinxNet/gemma-4-E4B-it-heretic against google/gemma-4-E4B-it (2026-11-02)

Measured on Wheat, round 33 piece 5 (download job 387105, compare job 387110, sweep 387114; the pull of 11-02
01:02Z carries the measurements and the sweep record and no job log). Modified revision `e7c50355` (10 commits on
2026-06-25: created 17:31Z, the folder, README, an animation and the `reproduce/` folder at 20:01Z), original
pinned at `fee6332c` (06-03). The card is Heretic's generated page (28,220 bytes): Heretic v1.4.0, direction index
32.21, attention output kernel 1.43 at position 26.52 falling to 0.47 at distance 20.07, down projection kernel 1.45
at 38.29 falling to 0.98 at 12.78, KL divergence 0.0069, refusals 35 of 100 against 100 of 100. The field
`base_model` names google/gemma-4-E4B, the pretrained base. The maker's second size in the census after the
26B-A4B export; the 12B is piece 6.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection-selected`, 14 flags (8 first
shares of 0.976 to 0.989, 5 direction cosines, one cross-kind), on the cluster and after re-scoring at home. On
reading, the copy is a Heretic edit whose two windows read to the layer, with the down kernel's height read within
0.2 and the attention kernel's read low on its shoulders.

- 51 of 2,076 matched tensors changed: the attention outputs of layers 7 to 41 (35) and the down projections of
  26 to 41 (16) of 42. The attention kernel reaches 26.52 plus or minus 20.07, layers 7 to 41 (6.45 to 46.59);
  the down kernel 38.29 plus or minus 12.78, layers 26 to 41 (25.51 to 51.07). Both windows read exactly. The 54
  original-only names are the shared-KV key norms. Nothing else moved; the largest relative change outside the
  changed set is exactly 0.
- One shared direction: group medians 0.97 and 0.99, 0.85 across the kinds, the two writers of a layer at 0.89
  to 0.997. First shares 0.976 to 0.997.
- Output side on 44 of 51 (29 of 35 attention outputs, 15 of 16 down projections). The down projections read 0.93 at layer 26, 1.01 at 30, 1.12 at 35, 1.22 at 38 and
  1.15 at 41 against the kernel's 1.00, 1.15, 1.33, 1.44 and 1.35, within 0.22 and rising to the peak as the
  kernel does. The attention outputs read 0.30 at layer 7, 0.64 at 19, 1.26 at 26, 0.63 at 30, 0.64 at 41
  against 0.50, 1.07, 1.41, 1.26 and 0.74: the peak within 0.15, the shoulders 0.2 to 0.6 short.
- Rows moved 0.0033 to 0.0108, Heretic's band; no restoration is claimed.

| Layer | Attention output: change, E1, left kept, weight, kernel | Down projection: change, E1, left kept, weight, kernel | Rows |
| --- | --- | --- | --- | --- |
| 7 | 0.0097, 0.976, 0.70, 0.30, 0.50 | | 0.0037 |
| 13 | 0.0156, 0.990, 0.48, 0.52, 0.78 | | 0.0052 |
| 19 | 0.0214, 0.994, 0.36, 0.64, 1.07 | | 0.0044 |
| 26 | 0.0274, 0.997, -0.26, 1.26, 1.41 | 0.0202, 0.994, 0.07, 0.93, 1.00 | 0.0055, 0.0057 |
| 30 | 0.0282, 0.997, 0.37, 0.63, 1.26 | 0.0244, 0.996, -0.01, 1.01, 1.15 | 0.0084, 0.0040 |
| 35 | 0.0213, 0.993, 0.21, 0.79, 1.02 | 0.0248, 0.996, -0.12, 1.12, 1.33 | 0.0072, 0.0081 |
| 38 | 0.0175, 0.992, 0.72, 0.28, 0.88 | 0.0278, 0.997, -0.22, 1.22, 1.44 | 0.0059, 0.0086 |
| 41 | 0.0129, 0.986, 0.36, 0.64, 0.74 | 0.0258, 0.996, -0.15, 1.15, 1.35 | 0.0035, 0.0048 |

The copy's four shards: the second and third (`4b42974e`, `21916333`) are its own; the first (`aa3e9d1e`) and
fourth (`8080cb1a`) are the untouched embedding and vision shards of the library's layout, shared with p-e-w's and
sh0ck0r's E4B exports (finding 71). No measured field equals another copy's.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster (one field) and "consistent with re-save noted" at home:
`text_config.moe_intermediate_size` closes by the default rule, and the two version strings are all that differ.
The template is the pin's 17,336-byte file and the fixed conversation renders identically.

## For the recipe library

The selected single-projection entry reads the windows and the side; its flags are the low shoulders of the
attention kernel (first shares 0.976 to 0.989 on layers 7 to 12 and 38 to 41) and five layers whose attention
direction turns 0.89 to 0.95 from the group's. Four E4B Heretic exports of one original in one round (p-e-w,
sh0ck0r, JokeHer and this) give the E4B entry its weight band: the linear kernels read their windows exactly and
their heights within 0.3 at the peak (finding 59). The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat33/measurements/pair-5/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
