# Reading of the Stage 1 and Stage 2 result: TrevorJS/gemma-4-E2B-it-uncensored against google/gemma-4-E2B-it (2026-10-31)

Measured on Blueback, round 13 piece 1 (push card 5404, download job 3400579 finished 2026-10-30 at 22:34Z, compare
job 3400580; the sweep 3400588 never ran, and card 5530 pulled the measurements home). Modified revision `7a34581e`
(2026-06-13, a README link fix; the repository was created on 2026-04-03 at 23:20Z and the weights uploaded two
minutes later), original pinned at `4742fe84` (2026-04-02, the release commit). The card describes grimjim's
norm-preserving biprojected abliteration with per-layer refusal directions, applied through LoRA adapters on
`o_proj` and `mlp.down_proj` in all layers at scale 1.0 and merged before saving; its table says "Layers
abliterated 100%".

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer`, 3 flags, on the cluster and
after re-scoring at home: one energy share (layer 0's down projection at 0.988) and two within-layer cosines (layer
3's two writers at 0.943). The three are the storage floor and a per-layer direction read twice, not a departure
from the card.

- 70 of 2,011 tensors changed: the attention output and the down projection of all 35 layers, the card's 100
  percent. Nothing else moved; the largest relative change outside the changed set is exactly 0 and 1,941 tensors
  equal the original.
- One direction per matrix: first-value share 0.988 to 0.996, the first singular value 13 to 150 times the second.
  Relative change 0.023 to 0.034.
- Per-layer directions, as the card says: the cross-layer cosine runs 0.005 to 0.64 (median 0.31) and the two
  writers of one layer agree at 0.943 to 0.997. Every one of the 35 layers carries its own direction.
- The kept fraction along the leading left direction is 0.002 to 0.69 (median 0.03 on the down projections, 0.11 on
  the attention outputs), the right 0.16 to 0.74; the left is below the right on 34 of 35 matrices of each kind, an
  output-side edit. At scale 1.0 the kept fraction should read 0; it reads near 0 on most layers and 0.24 to 0.69
  on layers 0, 6 and 34, where the per-layer direction is least aligned with the leading singular vector of the
  change.
- Row norms moved by at most 0.00043 on any matrix: the restoration held, the fifth TrevorJS copy on which it has.

| Layer | Attention output: change, E1, E8, left kept, right kept | Down projection: change, E1, E8, left kept, right kept | Weight read | Cross-layer cosine | Row norms |
| --- | --- | --- | --- | --- | --- |
| 0 | 0.0268, 0.992, 0.996, 0.24, 0.60 | 0.0335, 0.988, 0.996, 0.16, 0.52 | 0.76/0.84 | 0.00/0.01 | 0.0003, 0.0002 |
| 1 | 0.0281, 0.994, 0.996, 0.07, 0.64 | 0.0299, 0.995, 0.997, 0.02, 0.38 | 0.93/0.98 | 0.14/0.12 | 0.0004, 0.0002 |
| 2 | 0.0289, 0.996, 0.996, 0.11, 0.51 | 0.0279, 0.996, 0.997, 0.04, 0.47 | 0.89/0.96 | 0.12/0.11 | 0.0002, 0.0001 |
| 3 | 0.0295, 0.993, 0.996, 0.26, 0.64 | 0.0299, 0.995, 0.997, 0.69, 0.53 | 0.74/0.31 | 0.13/0.07 | 0.0003, 0.0003 |
| 4 | 0.0316, 0.996, 0.996, 0.61, 0.50 | 0.0270, 0.996, 0.997, 0.33, 0.43 | 0.39/0.67 | 0.14/0.01 | 0.0002, 0.0001 |
| 5 | 0.0302, 0.994, 0.996, 0.23, 0.62 | 0.0273, 0.996, 0.996, 0.02, 0.29 | 0.77/0.98 | 0.13/0.07 | 0.0003, 0.0001 |
| 6 | 0.0278, 0.995, 0.996, 0.14, 0.59 | 0.0284, 0.996, 0.996, 0.03, 0.32 | 0.86/0.97 | 0.16/0.11 | 0.0003, 0.0002 |
| 7 | 0.0288, 0.995, 0.996, 0.08, 0.56 | 0.0298, 0.996, 0.996, 0.02, 0.34 | 0.92/0.98 | 0.16/0.13 | 0.0002, 0.0001 |
| 8 | 0.0285, 0.995, 0.996, 0.03, 0.54 | 0.0326, 0.996, 0.997, 0.00, 0.39 | 0.97/1.00 | 0.10/0.08 | 0.0003, 0.0001 |
| 9 | 0.0281, 0.996, 0.996, 0.19, 0.46 | 0.0326, 0.996, 0.996, 0.00, 0.42 | 0.81/1.00 | 0.05/0.07 | 0.0002, 0.0002 |
| 10 | 0.0259, 0.995, 0.995, 0.04, 0.59 | 0.0323, 0.996, 0.996, 0.02, 0.40 | 0.96/0.98 | 0.12/0.14 | 0.0002, 0.0001 |
| 11 | 0.0250, 0.995, 0.995, 0.02, 0.67 | 0.0321, 0.996, 0.996, 0.00, 0.50 | 0.98/1.00 | 0.07/0.11 | 0.0002, 0.0002 |
| 12 | 0.0265, 0.995, 0.995, 0.02, 0.67 | 0.0321, 0.995, 0.996, 0.21, 0.65 | 0.98/0.79 | 0.03/0.09 | 0.0002, 0.0002 |
| 13 | 0.0232, 0.994, 0.995, 0.45, 0.62 | 0.0333, 0.996, 0.996, 0.04, 0.63 | 0.55/0.96 | 0.10/0.09 | 0.0002, 0.0002 |
| 14 | 0.0276, 0.996, 0.996, 0.06, 0.34 | 0.0274, 0.996, 0.996, 0.30, 0.34 | 0.94/0.70 | 0.12/0.12 | 0.0002, 0.0001 |
| 15 | 0.0253, 0.994, 0.995, 0.17, 0.62 | 0.0289, 0.996, 0.996, 0.04, 0.34 | 0.83/0.96 | 0.26/0.26 | 0.0003, 0.0003 |
| 16 | 0.0252, 0.995, 0.995, 0.16, 0.56 | 0.0279, 0.996, 0.996, 0.03, 0.27 | 0.84/0.97 | 0.29/0.28 | 0.0002, 0.0002 |
| 17 | 0.0252, 0.995, 0.995, 0.04, 0.56 | 0.0276, 0.996, 0.996, 0.06, 0.25 | 0.96/0.94 | 0.32/0.30 | 0.0002, 0.0001 |
| 18 | 0.0256, 0.994, 0.995, 0.06, 0.64 | 0.0296, 0.996, 0.996, 0.02, 0.38 | 0.94/0.98 | 0.33/0.33 | 0.0002, 0.0001 |
| 19 | 0.0259, 0.995, 0.995, 0.08, 0.59 | 0.0293, 0.996, 0.996, 0.01, 0.38 | 0.92/0.99 | 0.36/0.37 | 0.0003, 0.0001 |
| 20 | 0.0252, 0.995, 0.995, 0.02, 0.59 | 0.0282, 0.996, 0.996, 0.02, 0.27 | 0.98/0.98 | 0.40/0.42 | 0.0003, 0.0001 |
| 21 | 0.0254, 0.995, 0.995, 0.12, 0.61 | 0.0273, 0.996, 0.996, 0.01, 0.23 | 0.88/0.99 | 0.41/0.42 | 0.0003, 0.0001 |
| 22 | 0.0260, 0.994, 0.995, 0.34, 0.70 | 0.0273, 0.996, 0.996, 0.02, 0.23 | 0.66/0.98 | 0.41/0.43 | 0.0002, 0.0001 |
| 23 | 0.0262, 0.994, 0.995, 0.07, 0.58 | 0.0295, 0.996, 0.996, 0.02, 0.23 | 0.93/0.98 | 0.48/0.50 | 0.0002, 0.0001 |
| 24 | 0.0267, 0.994, 0.995, 0.07, 0.55 | 0.0275, 0.996, 0.996, 0.04, 0.23 | 0.93/0.96 | 0.56/0.58 | 0.0002, 0.0001 |
| 25 | 0.0235, 0.994, 0.994, 0.15, 0.63 | 0.0257, 0.995, 0.996, 0.05, 0.20 | 0.85/0.95 | 0.59/0.61 | 0.0003, 0.0002 |
| 26 | 0.0237, 0.994, 0.994, 0.10, 0.64 | 0.0247, 0.995, 0.995, 0.09, 0.18 | 0.90/0.91 | 0.60/0.62 | 0.0003, 0.0001 |
| 27 | 0.0258, 0.994, 0.995, 0.39, 0.70 | 0.0255, 0.995, 0.996, 0.14, 0.20 | 0.61/0.86 | 0.61/0.63 | 0.0002, 0.0001 |
| 28 | 0.0252, 0.994, 0.995, 0.37, 0.74 | 0.0260, 0.996, 0.996, 0.05, 0.18 | 0.63/0.95 | 0.63/0.64 | 0.0003, 0.0001 |
| 29 | 0.0251, 0.995, 0.995, 0.16, 0.53 | 0.0263, 0.996, 0.996, 0.04, 0.19 | 0.84/0.96 | 0.63/0.64 | 0.0002, 0.0001 |
| 30 | 0.0255, 0.995, 0.995, 0.09, 0.58 | 0.0270, 0.996, 0.996, 0.02, 0.19 | 0.91/0.98 | 0.61/0.63 | 0.0002, 0.0001 |
| 31 | 0.0271, 0.995, 0.995, 0.03, 0.65 | 0.0273, 0.996, 0.996, 0.02, 0.18 | 0.97/0.98 | 0.61/0.62 | 0.0002, 0.0001 |
| 32 | 0.0253, 0.995, 0.995, 0.17, 0.57 | 0.0276, 0.996, 0.996, 0.02, 0.19 | 0.83/0.98 | 0.55/0.57 | 0.0002, 0.0001 |
| 33 | 0.0247, 0.995, 0.995, 0.04, 0.59 | 0.0280, 0.996, 0.996, 0.03, 0.16 | 0.96/0.97 | 0.53/0.52 | 0.0002, 0.0001 |
| 34 | 0.0246, 0.995, 0.995, 0.14, 0.48 | 0.0249, 0.995, 0.995, 0.13, 0.25 | 0.86/0.87 | 0.45/0.46 | 0.0002, 0.0002 |

"Left kept" is the fraction of the original's action kept along the leading left direction; the weight read is one
minus it for the attention output and the down projection; the cross-layer cosine is each matrix's leading direction
against the layer median; row norms are the largest relative row change.

Against the four other copies measured on this original weight file (its one shard is `2db5482b` under all three
pinned revisions of the original: huihui-ai, prithivMLmods, aifeifei798 and llmfan46), no changed matrix has an
equal measurement in any field. This is the maker's fifth size, after the E4B, 12B, 26B-A4B and 31B, and the
fingerprint of finding 24 holds: all layers, both writers, per-layer directions, rows within 0.0005.

## Token and configuration side (Stage 1)

The cluster's card read "unexplained differences" on one field, `text_config.moe_intermediate_size`, and the home
judgement closes it: the field is absent on the original and loads as the same default in transformers 5.6.2. What
remains is a re-save, 5.5.0.dev0 to 5.5.0, on the configuration and the generation settings. The template equals
Google's pinned file byte for byte and the fixed conversation renders identically.

## For the recipe library

Consistent with the card on both sides: all layers, both writers, one direction per layer, norm restoration within
0.0005. The three flags are the two known readings of this method (the floor on a weak edit, and a within-layer
cosine below the rule when the two writers of one layer get directions measured at that layer rather than one
shared vector). The saved direction vectors are not committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/blueback13/measurements/pair-1/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
