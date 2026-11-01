# Reading of the Stage 1 and Stage 2 result: TheUmbraWalker/gemma-4-E4B-it-2-heretic against google/gemma-4-E4B-it (2026-10-31)

Measured on Wheat, round 30 piece 4 (probe job 386940, download job 386942, compare job 386946, 466 seconds, sweep
386951), without the container image, under a standalone Python 3.11.18. Modified revision `495cb4db` (2026-05-17 at
06:16Z, the README commit; the repository was created at 06:13Z and the weights uploaded at 06:15Z), original pinned
at `3555bddc` (2026-05-07). The card is two Heretic 1.3.0 cards one above the other, each with its kernel and its
numbers, and both name the base as "a model" (the tool's card generator when the model is loaded from a local path).
The lower one ran on the original: per-layer directions, attention output weight 1.31 at position 27.47 falling to
0.82 at distance 24.19, down projection 1.42 at 28.35 falling to 1.38 at distance 22.01, 11 refusals in 100 against
99, KL 0.1487. The upper one ran on that result: attention output 1.49 at 25.80 falling to 1.40 at distance 8.12,
down projection 1.04 at 38.45 falling to 0.53 at distance 10.11, 5 refusals in 100 against 10, KL 0.0676. The name's
"2" is the second pass. The repository's `base_model` field names the pretrained google/gemma-4-E4B; the pin is
the instruct model.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 61 flags, on the
cluster and after re-scoring at home: 29 first shares of 0.504 to 0.860 and 32 within-layer cosines of 0.006 to
0.855, all of them on layers 18 to 33 of the attention outputs and 29 to 41 of the down projections. On reading, the
copy is two per-layer Heretic passes on one base, and the two kernels' windows read off the weights to the layer.

- 73 of 2,076 tensors changed: the attention outputs of layers 4 to 41 (38) and the down projections of layers 7
  to 41 (35). Nothing else moved; the largest relative change outside the changed set is exactly 0 and 2,003
  tensors equal the original. The 54 shared-key-value tensors of layers 24 to 41 are absent from the copy's save,
  as on pair 3.
- The first pass's windows: Heretic's kernel is zero beyond `min_weight_distance`, so the lower card's attention
  output kernel reaches layers 3.3 to 51.7 and its down projection kernel 6.3 to 50.4, which on a 42-layer model
  are layers 4 to 41 and 7 to 41, the changed sets exactly.
- The second pass's windows: the upper card's attention output kernel reaches layers 17.7 to 33.9 and its down
  projection kernel 28.3 to 48.6, layers 18 to 33 and 29 to 41. Those are exactly the matrices that read two
  directions: on the attention outputs of 18 to 33 the first share is 0.50 to 0.70 with the second singular value
  0.65 to 0.99 of the first, and on the down projections of 29 to 41 it is 0.68 to 0.86 with the second value 0.40
  to 0.68 of the first; everywhere else the edit is rank one (first share 0.994 to 0.999, second value 0.00 to 0.04
  of the first). The within-layer cosine is 0.96 to 1.00 on layers 4 to 17 and 34 to 41 and 0.006 to 0.42 on 18 to
  33, where the two passes' directions differ and each writer's leading direction is a different mixture of them.
- Output side on 63 of 73: the left kept fraction is below the right on every matrix but ten attention outputs of
  layers 10 to 13, 37, 38 and 39 and the down projections of 9 and 29, where the two passes' projections along
  nearly opposite directions leave the leading direction's kept fraction unreadable as a weight.
- The weights do not read back from the leading direction, because two projections at different strengths along
  different directions were added: on the rank-one layers the attention outputs keep 0.03 to 0.72 (weight 0.28 to
  0.97) where the lower card implies 0.83 to 1.02, and the down projections of 7 to 18 read 0.83 to 1.34 where the
  card implies 1.38 to 1.39. The kernel read-back a card invites needs the two passes separated, which a rank-two
  decomposition per matrix could do and the leading-direction measure cannot.
- Rows moved by 0.004 to 0.015 under no preservation claim.
- Ninth measurement on the E4B weight file (shard `cfbd3d2f`), saved again in four shards; the first and last
  shards carry the same checksums as pair 3's (`aa3e9d1e`, `8080cb1a`), the library's sharding of blocks neither
  edit touches. No changed matrix has an equal measurement in any field of
  the eight others.

| Layer | Attention output: change, E1, E8, left kept, right kept | Down projection: change, E1, E8, left kept, right kept | Weight read | Within-layer cosine | Cross-layer cosine | Row norms | Card kernel |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | 0.0215, 0.997, 0.997, 0.52, 0.68 | - | 0.48/- | 1.000 | 0.01/- | 0.0092, - | 0.83+0.00 / 0.00+0.00 |
| 5 | 0.0244, 0.997, 0.998, 0.26, 0.62 | - | 0.74/- | 1.000 | 0.04/- | 0.0106, - | 0.85+0.00 / 0.00+0.00 |
| 6 | 0.0253, 0.997, 0.997, 0.34, 0.57 | - | 0.66/- | 1.000 | 0.04/- | 0.0104, - | 0.88+0.00 / 0.00+0.00 |
| 7 | 0.0237, 0.997, 0.997, 0.19, 0.66 | 0.0316, 0.998, 0.998, -0.22, 0.09 | 0.81/1.22 | 0.990 | 0.02/0.05 | 0.0086, 0.0060 | 0.90+0.00 / 1.38+0.00 |
| 8 | 0.0190, 0.995, 0.996, 0.21, 0.67 | 0.0334, 0.997, 0.998, 0.17, 0.47 | 0.79/0.83 | 0.968 | 0.11/0.02 | 0.0078, 0.0085 | 0.92+0.00 / 1.38+0.00 |
| 9 | 0.0215, 0.996, 0.997, 0.17, 0.62 | 0.0337, 0.998, 0.998, 0.18, 0.17 | 0.83/0.82 | 0.976 | 0.17/0.02 | 0.0073, 0.0072 | 0.94+0.00 / 1.38+0.00 |
| 10 | 0.0236, 0.996, 0.997, 0.72, 0.58 | 0.0351, 0.998, 0.998, 0.35, 0.10 | 0.28/0.65 | 0.985 | 0.24/0.11 | 0.0091, 0.0080 | 0.96+0.00 / 1.39+0.00 |
| 11 | 0.0248, 0.996, 0.997, 0.70, 0.49 | 0.0330, 0.998, 0.998, 0.17, 0.08 | 0.30/0.83 | 0.991 | 0.29/0.18 | 0.0095, 0.0121 | 0.98+0.00 / 1.39+0.00 |
| 12 | 0.0238, 0.996, 0.996, 0.60, 0.59 | 0.0318, 0.998, 0.998, -0.07, 0.04 | 0.40/1.07 | 0.986 | 0.31/0.20 | 0.0076, 0.0048 | 1.00+0.00 / 1.39+0.00 |
| 13 | 0.0242, 0.996, 0.996, 0.24, 0.61 | 0.0324, 0.998, 0.998, -0.26, 0.03 | 0.76/1.26 | 0.990 | 0.31/0.22 | 0.0064, 0.0066 | 1.02+0.00 / 1.39+0.00 |
| 14 | 0.0230, 0.996, 0.996, 0.24, 0.68 | 0.0321, 0.998, 0.998, -0.24, 0.02 | 0.76/1.24 | 0.993 | 0.28/0.23 | 0.0082, 0.0048 | 1.04+0.00 / 1.39+0.00 |
| 15 | 0.0235, 0.996, 0.996, 0.37, 0.63 | 0.0339, 0.998, 0.998, -0.29, 0.14 | 0.63/1.29 | 0.989 | 0.25/0.22 | 0.0063, 0.0044 | 1.06+0.00 / 1.40+0.00 |
| 16 | 0.0268, 0.997, 0.997, 0.05, 0.53 | 0.0380, 0.998, 0.998, -0.32, 0.13 | 0.95/1.32 | 0.997 | 0.17/0.21 | 0.0063, 0.0054 | 1.08+0.00 / 1.40+0.00 |
| 17 | 0.0252, 0.996, 0.997, 0.03, 0.58 | 0.0374, 0.998, 0.998, -0.30, 0.27 | 0.97/1.30 | 0.994 | 0.04/0.18 | 0.0045, 0.0065 | 1.10+0.00 / 1.40+0.00 |
| 18 | 0.0363, 0.637, 0.997, 0.12, 0.52 | 0.0363, 0.998, 0.998, -0.34, 0.23 | 0.88/1.34 | 0.352 | 0.11/0.16 | 0.0072, 0.0064 | 1.12+1.40 / 1.40+0.00 |
| 19 | 0.0364, 0.618, 0.997, -0.36, 0.59 | 0.0385, 0.997, 0.998, 0.14, 0.29 | 1.36/0.86 | 0.143 | 0.10/0.12 | 0.0081, 0.0088 | 1.14+1.41 / 1.40+0.00 |
| 20 | 0.0422, 0.601, 0.998, 0.08, 0.67 | 0.0413, 0.999, 0.999, 0.09, 0.19 | 0.92/0.91 | 0.365 | 0.06/0.08 | 0.0114, 0.0092 | 1.16+1.43 / 1.40+0.00 |
| 21 | 0.0456, 0.703, 0.998, -0.07, 0.56 | 0.0365, 0.998, 0.998, 0.51, 0.12 | 1.07/0.49 | 0.417 | 0.02/0.00 | 0.0152, 0.0066 | 1.18+1.44 / 1.41+0.00 |
| 22 | 0.0399, 0.568, 0.997, 0.34, 0.51 | 0.0409, 0.997, 0.999, 0.35, 0.29 | 0.66/0.65 | 0.281 | 0.09/0.05 | 0.0080, 0.0086 | 1.20+1.45 / 1.41+0.00 |
| 23 | 0.0425, 0.580, 0.997, -0.11, 0.36 | 0.0400, 0.998, 0.998, 0.14, 0.07 | 1.11/0.86 | 0.086 | 0.22/0.20 | 0.0085, 0.0125 | 1.22+1.46 / 1.41+0.00 |
| 24 | 0.0453, 0.632, 0.998, 0.07, 0.35 | 0.0325, 0.998, 0.998, -0.17, -0.01 | 0.93/1.17 | 0.117 | 0.30/0.36 | 0.0076, 0.0051 | 1.24+1.47 / 1.41+0.00 |
| 25 | 0.0428, 0.639, 0.997, -0.15, 0.46 | 0.0317, 0.997, 0.998, -0.31, 0.00 | 1.15/1.31 | 0.076 | 0.35/0.42 | 0.0067, 0.0038 | 1.26+1.48 / 1.41+0.00 |
| 26 | 0.0414, 0.628, 0.997, -0.31, 0.55 | 0.0325, 0.998, 0.998, -0.35, 0.13 | 1.31/1.35 | 0.107 | 0.34/0.44 | 0.0073, 0.0042 | 1.28+1.49 / 1.42+0.00 |
| 27 | 0.0407, 0.584, 0.997, -0.33, 0.55 | 0.0315, 0.997, 0.998, -0.37, 0.09 | 1.33/1.37 | 0.170 | 0.34/0.46 | 0.0086, 0.0045 | 1.30+1.48 / 1.42+0.00 |
| 28 | 0.0401, 0.590, 0.997, 0.16, 0.50 | 0.0334, 0.998, 0.998, -0.33, 0.08 | 0.84/1.33 | 0.100 | 0.32/0.52 | 0.0104, 0.0057 | 1.30+1.47 / 1.42+0.00 |
| 29 | 0.0442, 0.555, 0.998, 0.07, 0.54 | 0.0374, 0.860, 0.997, 0.07, 0.00 | 0.93/0.93 | 0.111 | 0.17/0.55 | 0.0130, 0.0082 | 1.28+1.45 / 1.42+0.56 |
| 30 | 0.0436, 0.504, 0.997, 0.40, 0.50 | 0.0336, 0.838, 0.996, -0.19, -0.08 | 0.60/1.19 | 0.855 | 0.22/0.62 | 0.0150, 0.0072 | 1.26+1.44 / 1.42+0.61 |
| 31 | 0.0379, 0.561, 0.997, 0.13, 0.61 | 0.0321, 0.824, 0.996, -0.33, -0.05 | 0.87/1.33 | 0.006 | 0.25/0.66 | 0.0148, 0.0062 | 1.24+1.43 / 1.42+0.66 |
| 32 | 0.0353, 0.600, 0.996, -0.14, 0.58 | 0.0302, 0.803, 0.995, -0.30, -0.02 | 1.14/1.30 | 0.274 | 0.35/0.68 | 0.0110, 0.0065 | 1.22+1.42 / 1.41+0.71 |
| 33 | 0.0404, 0.623, 0.997, 0.28, 0.51 | 0.0312, 0.795, 0.995, -0.21, -0.05 | 0.72/1.21 | 0.033 | 0.24/0.68 | 0.0097, 0.0064 | 1.20+1.41 / 1.41+0.77 |
| 34 | 0.0239, 0.995, 0.996, 0.25, 0.72 | 0.0321, 0.776, 0.995, -0.28, 0.02 | 0.75/1.28 | 0.961 | 0.49/0.68 | 0.0067, 0.0066 | 1.18+0.00 / 1.41+0.82 |
| 35 | 0.0232, 0.995, 0.996, -0.03, 0.59 | 0.0320, 0.735, 0.995, -0.33, 0.07 | 1.03/1.33 | 0.991 | 0.54/0.69 | 0.0054, 0.0061 | 1.16+0.00 / 1.41+0.87 |
| 36 | 0.0240, 0.995, 0.996, 0.29, 0.66 | 0.0337, 0.732, 0.996, -0.17, -0.01 | 0.71/1.17 | 0.979 | 0.56/0.67 | 0.0062, 0.0046 | 1.14+0.00 / 1.41+0.92 |
| 37 | 0.0222, 0.994, 0.995, 0.64, 0.67 | 0.0342, 0.701, 0.996, -0.33, -0.01 | 0.36/1.33 | 0.979 | 0.56/0.65 | 0.0051, 0.0050 | 1.12+0.00 / 1.40+0.97 |
| 38 | 0.0213, 0.994, 0.995, 0.46, 0.76 | 0.0353, 0.688, 0.996, -0.31, -0.04 | 0.54/1.31 | 0.964 | 0.54/0.63 | 0.0054, 0.0051 | 1.10+0.00 / 1.40+1.02 |
| 39 | 0.0211, 0.994, 0.995, 0.52, 0.70 | 0.0353, 0.683, 0.996, -0.35, -0.01 | 0.48/1.35 | 0.961 | 0.52/0.59 | 0.0044, 0.0055 | 1.08+0.00 / 1.40+1.01 |
| 40 | 0.0196, 0.994, 0.994, 0.45, 0.75 | 0.0353, 0.703, 0.996, -0.32, -0.01 | 0.55/1.32 | 0.979 | 0.50/0.56 | 0.0037, 0.0043 | 1.06+0.00 / 1.40+0.96 |
| 41 | 0.0210, 0.994, 0.995, 0.01, 0.62 | 0.0323, 0.698, 0.995, -0.31, 0.14 | 0.99/1.31 | 0.995 | 0.43/0.46 | 0.0049, 0.0047 | 1.04+0.00 / 1.40+0.91 |

The weight column reads one minus the left kept fraction; the card kernel column gives the first pass's weight plus
the second pass's, attention output then down projection, from the two cards' parameters and Heretic's kernel.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster, one field, and "consistent with re-save noted" at home. The two version
strings (5.5.0.dev0 to 5.6.2) close as a re-save, and `text_config.moe_intermediate_size`, written as null by the
5.6.2 save where Google's file omits it, closes at home under transformers 5.22.1, the field round 19's MoonRide copy
closed by the same rule under 5.6.2. The template is the pinned file byte for byte (16,804 bytes, `33204f1a`) and
the fixed conversation renders identically; the tokenizer configuration and generation settings are 5.6.2 re-saves.

## For the recipe library

The first copy in the census made by two Heretic passes, and the kernel windows of both passes read back from the
changed sets and the rank pattern to the layer. The strengths do not: a per-matrix rank-two decomposition that
reports two directions and two kept fractions would read both cards, where the leading-direction measure reads
neither. The `directional-per-layer-selected` entry matched the shape and flagged the overlap window; an entry for
stacked passes would allow rank two where two kernels overlap. The pull copy keeps the direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/wheat30/measurements/pair-4/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
