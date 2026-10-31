# Reading of the Stage 1 and Stage 2 result: AEON-7/Gemma-4-12B-it-AEON-Abliterated-K4-BF16 against google/gemma-4-12B-it (2026-10-31)

Measured on Blueback, round 13 piece 3 (push card 5404, download job 3400579, compare job 3400582; pulled home by
card 5530). Modified revision `a8ac2860` (2026-10-06, the last of 18 commits; the repository was created on
2026-06-04 at 08:00Z and the weights committed at 08:10Z), original pinned at `66bc78a7` (2026-06-03). The card
describes a "K=4 multi-direction biprojection": four refusal directions measured at layers 24, 37, 39 and 26,
orthonormalised by QR, projected out of `o_proj` and `down_proj` with norm preservation at scale 1.0 on the top
half of the layers by a per-layer refusal score ("top-pct 50"), which it lists as layers 21 to 42, 44 and 45, 48
matrices; the method is forked from TrevorJS's scripts.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 90 flags, on the
cluster and after re-scoring at home: 48 energy shares and 42 within-layer cosines. Both rules assume one direction
per matrix; the card states four, and the weights carry four.

- 48 of 677 tensors changed: the attention output and the down projection of layers 21 to 42, 44 and 45, the card's
  list to the layer (layer 43 is skipped in both). Nothing else moved; the largest relative change outside the
  changed set is exactly 0 and 629 tensors equal the original.
- Four near-equal directions per matrix: first-value share 0.26 to 0.32, the first four 0.9961 to 0.9970, the first
  five 0.9964 to 0.9971; the first singular value is 1.01 to 1.15 times the second and the fourth 19 to 195 times
  the fifth. The rank is four to the digit.
- One four-dimensional subspace across all 48 matrices: stacking the 48 leading left vectors gives singular values
  4.50, 3.65, 2.95, 2.34 and then 0.24, 99.4 percent in four, and 0.984 to 1.000 of each matrix's leading vector
  lies inside that subspace. The card's four directions are applied as one set to every matrix.
- The left kept fraction is −0.00003 to 0.87 (median 0.03 on the down projections, 0.13 on the attention outputs),
  the right 0.26 to 0.89, the left below the right on 47 of 48: an output-side edit. The kept fraction along one
  direction cannot read the scale when four are removed; where the leading vector of the change is one of the four
  the fraction reads 0.00 (layers 35 to 42 on the down projections) and elsewhere it reads the share of that
  direction in the mixture.
- Row norms moved by at most 0.00033: the restoration held.

| Layer | Attention output: change, E1, E8, left kept, right kept | Down projection: change, E1, E8, left kept, right kept | Weight read | Cross-layer cosine | Row norms |
| --- | --- | --- | --- | --- | --- |
| 21 | 0.0326, 0.275, 0.997, 0.87, 0.71 | 0.0332, 0.270, 0.997, 0.40, 0.40 | 0.13/0.60 | 0.46/0.46 | 0.0002, 0.0001 |
| 22 | 0.0312, 0.274, 0.997, 0.67, 0.73 | 0.0338, 0.295, 0.997, 0.23, 0.45 | 0.33/0.77 | 0.39/0.33 | 0.0002, 0.0001 |
| 23 | 0.0313, 0.276, 0.997, 0.32, 0.62 | 0.0345, 0.318, 0.997, 0.04, 0.53 | 0.68/0.96 | 0.21/0.30 | 0.0002, 0.0001 |
| 24 | 0.0310, 0.266, 0.997, 0.18, 0.63 | 0.0342, 0.301, 0.997, 0.16, 0.50 | 0.82/0.84 | 0.10/0.41 | 0.0002, 0.0001 |
| 25 | 0.0300, 0.282, 0.997, 0.11, 0.72 | 0.0336, 0.278, 0.997, 0.13, 0.48 | 0.89/0.87 | 0.23/0.41 | 0.0002, 0.0002 |
| 26 | 0.0327, 0.285, 0.997, 0.38, 0.63 | 0.0343, 0.312, 0.997, 0.20, 0.44 | 0.62/0.80 | 0.12/0.30 | 0.0002, 0.0001 |
| 27 | 0.0308, 0.274, 0.997, 0.16, 0.60 | 0.0336, 0.271, 0.997, 0.17, 0.52 | 0.84/0.83 | 0.29/0.55 | 0.0002, 0.0001 |
| 28 | 0.0322, 0.265, 0.997, 0.05, 0.59 | 0.0333, 0.263, 0.997, 0.09, 0.39 | 0.95/0.91 | 0.54/0.50 | 0.0002, 0.0001 |
| 29 | 0.0322, 0.264, 0.997, 0.03, 0.62 | 0.0331, 0.258, 0.997, 0.06, 0.45 | 0.97/0.94 | 0.90/0.49 | 0.0001, 0.0001 |
| 30 | 0.0322, 0.265, 0.997, 0.10, 0.60 | 0.0333, 0.264, 0.997, 0.38, 0.47 | 0.90/0.62 | 0.42/0.79 | 0.0002, 0.0002 |
| 31 | 0.0330, 0.270, 0.997, 0.13, 0.62 | 0.0325, 0.266, 0.997, 0.08, 0.37 | 0.87/0.92 | 0.33/0.14 | 0.0002, 0.0001 |
| 32 | 0.0328, 0.261, 0.997, 0.28, 0.53 | 0.0332, 0.263, 0.997, 0.05, 0.36 | 0.72/0.95 | 0.24/0.18 | 0.0002, 0.0001 |
| 33 | 0.0334, 0.273, 0.997, 0.15, 0.64 | 0.0329, 0.269, 0.997, 0.02, 0.27 | 0.85/0.98 | 0.29/0.14 | 0.0003, 0.0002 |
| 34 | 0.0319, 0.266, 0.997, 0.13, 0.61 | 0.0327, 0.270, 0.997, 0.01, 0.26 | 0.87/0.99 | 0.89/0.78 | 0.0002, 0.0001 |
| 35 | 0.0319, 0.261, 0.996, 0.10, 0.65 | 0.0326, 0.268, 0.997, 0.00, 0.27 | 0.90/1.00 | 0.90/0.84 | 0.0002, 0.0001 |
| 36 | 0.0325, 0.272, 0.997, 0.47, 0.89 | 0.0323, 0.272, 0.997, 0.00, 0.26 | 0.53/1.00 | 0.29/0.84 | 0.0002, 0.0001 |
| 37 | 0.0328, 0.265, 0.997, 0.03, 0.64 | 0.0326, 0.275, 0.997, 0.00, 0.30 | 0.97/1.00 | 0.88/0.87 | 0.0002, 0.0001 |
| 38 | 0.0334, 0.265, 0.997, 0.41, 0.59 | 0.0328, 0.289, 0.997, 0.00, 0.26 | 0.59/1.00 | 0.91/0.78 | 0.0002, 0.0001 |
| 39 | 0.0324, 0.277, 0.997, 0.02, 0.70 | 0.0332, 0.298, 0.997, 0.00, 0.34 | 0.98/1.00 | 0.76/0.78 | 0.0002, 0.0001 |
| 40 | 0.0326, 0.265, 0.997, 0.00, 0.60 | 0.0326, 0.281, 0.997, 0.00, 0.28 | 1.00/1.00 | 0.41/0.85 | 0.0002, 0.0001 |
| 41 | 0.0322, 0.277, 0.997, 0.01, 0.64 | 0.0322, 0.271, 0.997, 0.01, 0.28 | 0.99/0.99 | 0.85/0.86 | 0.0002, 0.0001 |
| 42 | 0.0322, 0.264, 0.997, 0.05, 0.61 | 0.0318, 0.278, 0.997, 0.01, 0.33 | 0.95/0.99 | 0.70/0.81 | 0.0002, 0.0001 |
| 44 | 0.0321, 0.269, 0.997, 0.33, 0.58 | 0.0323, 0.264, 0.997, 0.01, 0.27 | 0.67/0.99 | 0.88/0.81 | 0.0002, 0.0002 |
| 45 | 0.0323, 0.273, 0.997, 0.02, 0.57 | 0.0324, 0.269, 0.997, 0.01, 0.30 | 0.98/0.99 | 0.80/0.78 | 0.0002, 0.0002 |

"E1" and "E8" are the first-value and first-eight energy shares; the first-four share is 0.996 to 0.997 on every
row and is the number that reads this edit. The weight column is one minus the left kept fraction and is not a
scale here. The cross-layer cosine is against the layer median and reads 0.10 to 0.91 because a leading vector drawn
from a four-dimensional mixture varies from layer to layer.

The subspace reaches other makers' copies. The output-side leading vectors of the other 12B copies on this weight
file lie partly inside it: igorls 0.60 to 0.61, huihui-ai 0.56 to 0.79, 3MPER0RR 0.37 to 0.47, richardyoung 0.34
to 0.49; the input-side copies do not (llmfan46 about 0.1, coder3101 about 0.07). No changed matrix of this copy
has an equal measurement in any field of the six other 12B copies.

## Token and configuration side (Stage 1)

The cluster's card read "unexplained differences" on seven fields and the home judgement keeps them: the six are
the class-default fields of finding 11 (`audio_config.audio_samples_per_token`, `hidden_size`, `output_proj_dims`,
`vision_config.model_patch_size`, and the data type repeated in the audio and vision sub-configurations), and the
seventh is `text_config.max_position_embeddings`, 131,072 at the pin and 262,144 in the copy. The copy's own
history carries that one: its first configuration (commit `d07587bb`, 06-04) said 131,072 and the maker's commit
`593810fc` of 06-07, "Restore native 256k context (max_position_embeddings 131072->262144; RoPE unchanged)",
followed Google's commit `5926caa4` of 06-04 that made the same change. Both sides are at 5.10.0.dev0. The template
equals Google's pinned file byte for byte and the fixed conversation renders identically.

## For the recipe library

Consistent with the card in every stated number: 48 matrices on 24 named layers, rank four with the first four
carrying 0.996 or more, one shared four-dimensional subspace, output side, norm restoration within 0.0004. A recipe
entry for a rank-k projection would read the first-k share and the gap between the k-th and (k+1)-th singular
values, and would not flag the first share or the within-layer cosine. The saved direction vectors are not
committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/blueback13/measurements/pair-3/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
