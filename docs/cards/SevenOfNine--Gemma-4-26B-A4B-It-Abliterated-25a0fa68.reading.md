# Reading of the Stage 1 and Stage 2 result: SevenOfNine/Gemma-4-26B-A4B-It-Abliterated against google/gemma-4-26B-A4B-it (2026-10-31)

Measured on Nautilus, round 19 piece 3 (push card 5605, probe card 5616, round card 5626, download job 4142666, compare job 4142669 on the background queue, sweep 4142675; pulled home by card 5647). Modified revision `07c26ad8` (2026-06-10 at 19:28Z, a documentation commit;
the repository was created at 12:16Z, the weights were committed at 14:18Z as "Heretic abliteration of
google/gemma-4-26B-A4B-it" and the results at 19:26Z), original pinned at `20da991a` (2026-06-03). The card names
the method: Heretic 1.3.0 through the maker's fork (an unattended auto-save mode), 200 TPE trials "abliterating
attn.o_proj + mlp.down_proj across 30 layers", trial 98 selected as the fewest refusals under a KL ceiling of 0.5,
in bfloat16 on one A100; it reports 18 refusals in 100 against 100 for the original and a KL divergence of
0.0845, on the Heretic default datasets. The per-trial parameters are said to be logged in the maker's GGUF
repository and are not on this card.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 8 flags, on the
cluster and after re-scoring at home: the within-layer cosines of layers 16, 18, 19 and 27 (0.949, 0.941, 0.901
and 0.881), counted on both writers. On reading, the copy is one direction per layer on the attention outputs of
26 layers and the shared down projections of 14, output side, at a strength that rises with depth, and it reaches
no expert.

- 40 of 1,013 tensors changed: the attention outputs of layers 4 to 29 and the shared dense down projections
  (2816 by 2112) of layers 16 to 29. Nothing else moved; the largest relative change outside the changed set is
  exactly 0 and 973 tensors equal the original. The 30 packed expert down tensors, the 30 packed gate-up tensors
  and the 30 routers read exactly 0: the sixth edit of this base that leaves all 3,840 expert matrices alone
  (finding 20), from a tool that edits the linear modules a layer exposes and not its packed experts. The card's
  "30 layers" is the model's layer count; the edit touches 26 of them.
- Rank one: first-value share 0.991 to 0.998, the first singular value 14 to 148 times the second. Within a layer
  the two writers agree at 0.88 to 1.00; across layers the directions drift, 0.05 to 0.84 to the group reference,
  rising from layer 4 to a plateau around layers 16 to 22 and falling again.
- Output side on 38 of 40: the left kept fraction is below the right on every matrix but the attention outputs of
  layers 19 and 27, where the left reads 0.62 and 0.49.
- The strength reads as a schedule. Along the leading direction the attention outputs keep −0.07 to 0.13 of the
  original's action on layers 4 to 12 (a weight of 0.87 to 1.07), then −0.09 to −0.40 on layers 13 to 29 (1.09 to
  1.40) apart from the two outliers; the down projections keep 0.00 to 0.25 on 16 to 29 (0.75 to 1.00) with 0.46
  on layer 26. Heretic's kernel, a weight that peaks at a layer and falls with distance, fits the attention
  outputs with the peak near the top of the range; the card does not print the kernel's parameters.
- Rows moved by 0.0044 to 0.048, largest on layers 6 and 29, under no preservation claim.
- Eighth measurement on the 26B-A4B weight file (shards `11276849`, `aab47033`), saved again in 11 shards. No
  changed matrix has an equal measurement in any field of the seven others.

| Layer | Attention output: change, E1, E8, left kept, right kept | Down projection: change, E1, E8, left kept, right kept | Weight read | Within-layer cosine | Cross-layer cosine | Row norms |
| --- | --- | --- | --- | --- | --- | --- |
| 4 | 0.0419, 0.998, 0.999, -0.07, 0.26 | - | 1.07/- | - | 0.05/- | 0.0195, - |
| 5 | 0.0393, 0.997, 0.999, -0.01, 0.31 | - | 1.01/- | - | 0.13/- | 0.0165, - |
| 6 | 0.0467, 0.997, 0.999, 0.05, 0.18 | - | 0.95/- | - | 0.15/- | 0.0379, - |
| 7 | 0.0373, 0.998, 0.999, 0.09, 0.19 | - | 0.91/- | - | 0.17/- | 0.0220, - |
| 8 | 0.0372, 0.998, 0.999, -0.04, 0.24 | - | 1.04/- | - | 0.27/- | 0.0141, - |
| 9 | 0.0377, 0.998, 0.999, 0.10, 0.34 | - | 0.90/- | - | 0.33/- | 0.0164, - |
| 10 | 0.0437, 0.998, 0.999, -0.01, 0.23 | - | 1.01/- | - | 0.43/- | 0.0199, - |
| 11 | 0.0383, 0.996, 0.999, 0.13, 0.38 | - | 0.87/- | - | 0.41/- | 0.0213, - |
| 12 | 0.0369, 0.998, 0.999, -0.04, 0.20 | - | 1.04/- | - | 0.51/- | 0.0132, - |
| 13 | 0.0354, 0.997, 0.998, -0.19, 0.34 | - | 1.19/- | - | 0.51/- | 0.0171, - |
| 14 | 0.0332, 0.998, 0.998, -0.25, 0.37 | - | 1.25/- | - | 0.59/- | 0.0177, - |
| 15 | 0.0346, 0.998, 0.998, -0.09, 0.43 | - | 1.09/- | - | 0.60/- | 0.0145, - |
| 16 | 0.0329, 0.997, 0.998, -0.08, 0.41 | 0.0186, 0.993, 0.994, 0.24, 0.79 | 1.08/0.76 | 0.949 | 0.69/0.54 | 0.0138, 0.0162 |
| 17 | 0.0299, 0.997, 0.998, -0.35, 0.36 | 0.0194, 0.994, 0.995, 0.13, 0.82 | 1.35/0.87 | 0.983 | 0.71/0.63 | 0.0187, 0.0160 |
| 18 | 0.0295, 0.997, 0.997, -0.17, 0.36 | 0.0193, 0.994, 0.994, 0.14, 0.84 | 1.17/0.86 | 0.941 | 0.69/0.69 | 0.0110, 0.0157 |
| 19 | 0.0350, 0.998, 0.998, 0.62, 0.28 | 0.0210, 0.995, 0.995, 0.05, 0.79 | 0.38/0.95 | 0.901 | 0.64/0.78 | 0.0186, 0.0204 |
| 20 | 0.0303, 0.997, 0.998, -0.16, 0.42 | 0.0209, 0.995, 0.995, 0.04, 0.77 | 1.16/0.96 | 0.954 | 0.70/0.79 | 0.0117, 0.0128 |
| 21 | 0.0323, 0.997, 0.998, -0.38, 0.31 | 0.0203, 0.994, 0.995, 0.04, 0.75 | 1.38/0.96 | 0.970 | 0.70/0.84 | 0.0142, 0.0160 |
| 22 | 0.0296, 0.997, 0.997, -0.26, 0.31 | 0.0206, 0.994, 0.995, 0.10, 0.75 | 1.26/0.90 | 0.969 | 0.66/0.84 | 0.0101, 0.0096 |
| 23 | 0.0275, 0.997, 0.997, -0.27, 0.49 | 0.0208, 0.995, 0.995, -0.00, 0.80 | 1.27/1.00 | 0.976 | 0.60/0.82 | 0.0091, 0.0085 |
| 24 | 0.0316, 0.998, 0.998, -0.40, 0.20 | 0.0208, 0.995, 0.995, -0.02, 0.76 | 1.40/1.02 | 0.977 | 0.59/0.79 | 0.0086, 0.0103 |
| 25 | 0.0260, 0.996, 0.997, -0.37, 0.38 | 0.0210, 0.995, 0.995, 0.07, 0.81 | 1.37/0.93 | 0.984 | 0.51/0.72 | 0.0044, 0.0059 |
| 26 | 0.0315, 0.997, 0.998, -0.32, 0.27 | 0.0249, 0.996, 0.997, 0.46, 0.79 | 1.32/0.54 | 0.958 | 0.48/0.66 | 0.0071, 0.0089 |
| 27 | 0.0313, 0.996, 0.998, 0.49, 0.39 | 0.0281, 0.997, 0.997, 0.14, 0.75 | 0.51/0.86 | 0.881 | 0.42/0.62 | 0.0065, 0.0130 |
| 28 | 0.0278, 0.997, 0.997, -0.39, 0.25 | 0.0275, 0.997, 0.997, 0.13, 0.76 | 1.39/0.87 | 0.968 | 0.41/0.57 | 0.0070, 0.0166 |
| 29 | 0.0271, 0.997, 0.997, -0.28, 0.26 | 0.0344, 0.991, 0.998, 0.25, 0.84 | 1.28/0.75 | 0.958 | 0.29/0.42 | 0.0059, 0.0484 |

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home: the two version strings (5.5.0.dev0 to 5.10.2) and
nothing else. The template is the pinned file byte for byte (17,466 bytes, `36e3a42e`) and the fixed conversation
renders identically.

## For the recipe library

A Heretic run read as a per-layer schedule on a mixture, the sixth edit of this base that reaches no expert. The
`directional-per-layer-selected` entry matched the shape; the eight flags are four layers whose two writers agree
at 0.88 to 0.95, under the 0.95 line, and the entry should say when the kind left unchanged on a mixture is the
experts, as finding 20 asks. The strength schedule (0.87 to 1.40 on the attention outputs) is the third Heretic
kernel the census reads from the kept fraction, after llmfan46's and grayarea's.
