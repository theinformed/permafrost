# Reading of the Stage 1 and Stage 2 result: WWTCyberLab/gemma-4-26B-A4B-it-abliterated against google/gemma-4-26B-A4B-it (2026-10-31)

Measured on Nautilus, round 18 piece 5 (push card 5473, round card 5477, download job 4125751, compare job 4125756
on the background queue, sweep 4125760; pulled home by card 5493). Modified revision `3164db09` (2026-04-12, a
citation fix; the repository was created on 2026-04-06 at 07:11Z, the weights were uploaded five minutes later and
replaced on 2026-04-06 at 16:17Z, 2026-04-07 at 22:22Z and 2026-04-08 at 21:17Z, the last commit titled "2-pass +
token suppression"), original pinned at `47b6801b` (2026-04-02, the release commit). The maker's card describes
three stages: a concentrated ablation of layers 16, 18 and 19 at scale 4.0 "with 4 weight types", a second pass on
the re-measured residual directions of the top 10 layers at scale 3.0, and the suppression of 13 "refusal-starting"
token embeddings at strength 5 in `embed_tokens.weight`; it reports 2 hard refusals in 48, 10 in 520 on AdvBench,
and MMLU 65.1 against 64.4 percent.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 51 flags, on the
cluster and after re-scoring at home: 36 energy shares and 15 within-layer directions. On reading, the copy is a
per-layer ablation of one or two directions on the three down-writing matrices of 18 layers, experts included, with
13 rows of the token embedding scaled to one sixth, and the flags are the two-direction layers and the embedding.

- 55 of 1,013 tensors changed: the attention output, the shared down projection and the packed expert down tensor
  (128 experts) of each of layers 9 to 26, and the token embedding. The 30 packed gate-up tensors, the 90 router
  tensors, the reading-side projections, the normalisations and the vision tower are unchanged; the largest
  relative change outside the changed set is exactly 0 and 958 tensors equal the original. The card names three
  layers in the first pass and ten in the second; the weights carry 18.
- One direction in eight layers, two in ten. In layers 9, 10, 11, 14, 15, 21, 23 and 26 the three writers each
  carry a rank-one change (first-value share 0.982 to 0.997, relative change 0.015 to 0.029). In layers 12, 13, 16,
  17, 18, 19, 20, 22, 24 and 25 the first share falls to 0.50 to 0.96 with the first eight at 0.991 to 0.997 and the
  first singular value 1.1 to 5.0 times the second: two directions of comparable size, the shape two passes on one
  layer leave. The card's first-pass layers 16, 18 and 19 are among the ten.
- The experts are reached. In every one of the 18 layers all 128 experts' down projections changed, at a relative
  change of 0.015 to 0.048 per expert (medians 0.018 to 0.025), and the experts of a layer share the leading output
  direction at median cosine 0.98 to 1.00 (minimum 0.46 in layer 19, 0.015 in layer 22, where the two directions
  trade places between experts). The median expert's first share is 0.990 to 0.996 in the rank-one layers and 0.56
  to 0.68 in the two-direction layers, the same split as the dense matrices. After TrevorJS's copy (finding 13) this
  is the second edit of this base to change an expert; the four others left all 3,840 expert matrices alone (finding
  20).
- The weight reads near 1.0. Along the leading direction the copy keeps −0.13 to 0.17 of the original's action on
  the left (median 0.07 on the attention outputs, 0.08 on the shared down projections, −0.002 to 0.15 for the median
  expert) and 0.30 to 0.93 on the right; the left fraction is below the right on all 54 layer matrices, an output
  side edit. The card's scales of 4.0 and 3.0 are not what the kept fraction reads; a scale of 4 would leave −3.
- The directions differ by layer: cross-layer cosine 0.11 to 0.93 on the attention outputs (median 0.42), 0.00 to
  0.74 on the shared down projections, 0.19 to 0.85 on the experts' medians, with the first-pass block (layers 15 to
  20) agreeing at 0.75 to 0.93 and the rest loosely. Within a layer the three writers agree at 0.98 to 1.00 in the
  rank-one layers and 0.34 to 0.99 in the two-direction layers.
- The embedding: relative change 0.0060, first-value share 0.245 with eight near-equal singular values (2.32, 1.51,
  1.38, 1.28, 1.22, 1.19, 1.17, 1.11), and the copy keeps 0.16666 of the original's action along each of the eight
  leading left directions and 0.993 to 1.000 along the right ones: rows scaled by one sixth, the card's strength 5
  read as a division by six, on exactly 13 rows, whose tokens are "While", "Please", "It", "That", "I", "As",
  "Sorry", "However", "Creating", "*(", "Modern", "*" and "***". The largest row-norm change is 0.833, five sixths,
  and the embedding is the one tensor outside the recipe's set (0.0060 reported there).
- Row norms moved by 0.009 to 0.67 on the attention outputs, 0.023 to 0.30 on the shared down projections and 0.06
  to 0.58 on the expert tensors, under no preservation claim.

| Layer | Attention output: change, E1, E8 | Shared down: change, E1, E8 | Experts: change, median expert E1 | Directions | Cross-layer cosine |
| --- | --- | --- | --- | --- | --- |
| 9 | 0.029, 0.997, 0.997 | 0.021, 0.996, 0.996 | 0.019, 0.996 | one | 0.24 |
| 10 | 0.028, 0.997, 0.997 | 0.017, 0.994, 0.995 | 0.020, 0.995 | one | 0.19 |
| 11 | 0.026, 0.996, 0.997 | 0.017, 0.994, 0.995 | 0.019, 0.994 | one | 0.24 |
| 12 | 0.039, 0.784, 0.996 | 0.022, 0.576, 0.993 | 0.024, 0.617 | two | 0.41 |
| 13 | 0.036, 0.785, 0.996 | 0.021, 0.553, 0.992 | 0.025, 0.627 | two | 0.34 |
| 14 | 0.022, 0.995, 0.996 | 0.016, 0.992, 0.993 | 0.017, 0.992 | one | 0.44 |
| 15 | 0.022, 0.995, 0.995 | 0.016, 0.992, 0.993 | 0.019, 0.993 | one | 0.49 |
| 16 | 0.040, 0.775, 0.996 | 0.022, 0.589, 0.992 | 0.026, 0.629 | two | 0.75 |
| 17 | 0.027, 0.666, 0.994 | 0.022, 0.569, 0.992 | 0.024, 0.625 | two | 0.81 |
| 18 | 0.039, 0.816, 0.997 | 0.022, 0.569, 0.992 | 0.023, 0.611 | two | 0.89 |
| 19 | 0.080, 0.956, 0.996 | 0.022, 0.577, 0.992 | 0.025, 0.640 | two | 0.93 |
| 20 | 0.043, 0.890, 0.997 | 0.021, 0.550, 0.991 | 0.025, 0.683 | two | 0.93 |
| 21 | 0.029, 0.995, 0.996 | 0.016, 0.991, 0.992 | 0.017, 0.992 | one | 0.79 |
| 22 | 0.034, 0.727, 0.995 | 0.022, 0.597, 0.992 | 0.024, 0.557 | two | 0.75 |
| 23 | 0.018, 0.993, 0.993 | 0.015, 0.990, 0.991 | 0.015, 0.991 | one | 0.38 |
| 24 | 0.038, 0.709, 0.995 | 0.023, 0.624, 0.992 | 0.025, 0.580 | two | 0.36 |
| 25 | 0.026, 0.620, 0.993 | 0.022, 0.628, 0.992 | 0.023, 0.595 | two | 0.32 |
| 26 | 0.021, 0.994, 0.994 | 0.021, 0.982, 0.995 | 0.019, 0.993 | one | 0.11 |

The cross-layer cosine is the attention output's against the group's median direction.

Against the six earlier measurements on this original weight file (shards `11276849` and `aab47033`: TrevorJS
twice, huihui-ai, coder3101, llmfan46 and prithivMLmods's re-upload), no changed matrix has an equal measurement in
any field. Seven measurements of six makers' copies now stand on one 26B-A4B file; two reach the experts, TrevorJS's
on all 30 layers with one direction per layer applied to every expert, this one on 18 layers with the experts
carrying the same one or two directions as the dense writers beside them.

## Token and configuration side (Stage 1)

The cluster's card read "consistent with re-save noted" and the home judgement keeps it: `transformers_version`
5.5.0.dev0 on the original and 5.5.0 on the copy in the configuration and the generation settings, and nothing else.
The template is Google's release template byte for byte (the pin is the release commit), the tokenizer, special
tokens and the rest of the configuration are equal, and the fixed conversation renders identically. The 13 scaled
rows are in the weights only; no token, template or configuration field refers to them.

## For the recipe library

Consistent with the card in kind on both sides, with the layer count (18 against 13 named) and the scale (near 1.0
against 4.0 and 3.0) read differently from the weights. Two things the library has no entry for: an edit that
reaches a mixture's packed experts with per-layer directions and a rank of one or two, and a token-embedding row
scaling, which the energy-share rule reports as a failed projection on a tensor whose change is 13 rows. The saved
direction vectors are not committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/nautilus18/measurements/pair-5/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
