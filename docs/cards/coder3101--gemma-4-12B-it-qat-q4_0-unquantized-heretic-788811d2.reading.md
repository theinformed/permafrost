# Reading of the Stage 1 and Stage 2 result: coder3101/gemma-4-12B-it-qat-q4_0-unquantized-heretic against google/gemma-4-12B-it-qat-q4_0-unquantized (2026-11-02)

Measured on Nautilus, round 34 piece 7 (download job 4163806, compare job 4163813, sweep 4163815; the pull of
11-01 21:23Z carries the measurements and the sweep record and no job log). Modified revision `87e95332` (6
commits inside three minutes on 2026-06-06 from 16:52Z), original pinned at `58540658`, the QAT-unquantized
checkpoint. The card (29,501 bytes) is Heretic v1.2.0's page for an arbitrary-rank ablation with row-norm
preservation: start layer 24, end layer 48, preserve 0.3707, steer 0.0010, overcorrect 0.6177, 15 neighbours, KL
divergence 0.0575, refusals 8 of 100 against 99 of 100; it lists no targeted component. The field `base_model`
names the QAT checkpoint. The maker's fifth copy in the census and the second on a QAT checkpoint after the E2B
of round 32 (finding 22); the maker's instruct 12B copy was measured in round 18.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 24 flags, on the
cluster and after re-scoring at home: the first shares of all 24 matrices (0.53 to 0.97). On reading, the copy is
the maker's arbitrary-rank edit on the attention outputs of the top 24 layers, input side, at weights to 2.54,
with the rows put back to the maker's usual 0.007.

- 24 of 677 tensors changed: the attention outputs of layers 24 to 47 of 48, the card's start 24 and end 48. The
  24 down projections in the window read exactly 0, no residues; nothing else moved, and the largest relative
  change outside the changed set is exactly 0, which places the copy on the QAT checkpoint (finding 48).
- Input side on 24 of 24: the right kept fraction is below the left on every matrix. Read as weights (one minus
  the right fraction) the layers run 0.76 to 2.54: 2.54 at layer 35, 2.45 at 37, 2.13 at 42, 1.99 at 44, and
  under one at layers 31, 40 and 43 (0.76, 0.95, 0.94), where the right keeps +0.245, +0.047 and +0.057.
- Several directions per matrix: first shares 0.53 to 0.97, eight-direction shares 0.89 to 0.99; across layers
  the leading directions sit at 0.08 to 0.44 to the group reference.
- Rows moved 0.0070 to 0.0079 on all 24: the band finding 22 reads under this maker's preservation claim on four
  bases, now a fifth.
- Against the maker's instruct 12B edit (round 18, nautilus18 pair 1) the saved leading left vectors stand at
  0.21 to 0.955 on the 21 shared attention outputs (median 0.88; right median 0.92). Against wnfldchen's
  arbitrary-rank edit of the same checkpoint (piece 2) the median is 0.92 on 18 shared; against igorls's kernel
  search 0.11; against huihui-ai's projection 0.04.

| Layer | Attention output: change, E1, E8, left kept, right kept | Weight read (1 − right) | Cross-layer cosine | Rows |
| --- | --- | --- | --- | --- |
| 24 | 0.0187, 0.938, 0.961, 0.82, -0.05 | 1.05 | 0.16 | 0.0070 |
| 25 | 0.0261, 0.850, 0.951, 0.91, -0.17 | 1.17 | 0.08 | 0.0076 |
| 26 | 0.0249, 0.771, 0.927, 0.85, -0.15 | 1.15 | 0.25 | 0.0076 |
| 27 | 0.0295, 0.646, 0.910, 0.80, -0.19 | 1.19 | 0.17 | 0.0075 |
| 28 | 0.0280, 0.709, 0.944, 0.68, -0.12 | 1.12 | 0.30 | 0.0076 |
| 29 | 0.0203, 0.645, 0.889, 0.97, -0.09 | 1.09 | 0.18 | 0.0077 |
| 30 | 0.0269, 0.613, 0.942, 0.91, -0.32 | 1.32 | 0.12 | 0.0077 |
| 31 | 0.0147, 0.955, 0.965, 0.88, 0.24 | 0.76 | 0.16 | 0.0077 |
| 32 | 0.0229, 0.957, 0.972, 0.72, -0.27 | 1.27 | 0.10 | 0.0075 |
| 33 | 0.0226, 0.942, 0.970, 0.94, -0.24 | 1.24 | 0.16 | 0.0077 |
| 34 | 0.0249, 0.765, 0.951, 0.72, -0.36 | 1.36 | 0.21 | 0.0078 |
| 35 | 0.0818, 0.970, 0.987, 0.87, -1.54 | 2.54 | 0.29 | 0.0075 |
| 36 | 0.0152, 0.961, 0.981, 1.00, -0.58 | 1.58 | 0.20 | 0.0078 |
| 37 | 0.0649, 0.529, 0.892, 0.95, -1.45 | 2.45 | 0.14 | 0.0075 |
| 38 | 0.0217, 0.902, 0.969, 0.75, -0.30 | 1.30 | 0.24 | 0.0079 |
| 39 | 0.0196, 0.958, 0.983, 0.99, -0.68 | 1.68 | 0.12 | 0.0077 |
| 40 | 0.0155, 0.969, 0.975, 0.92, 0.05 | 0.95 | 0.16 | 0.0079 |
| 41 | 0.0202, 0.959, 0.980, 0.97, -0.33 | 1.33 | 0.27 | 0.0079 |
| 42 | 0.0249, 0.971, 0.987, 0.99, -1.13 | 2.13 | 0.44 | 0.0077 |
| 43 | 0.0164, 0.954, 0.978, 0.86, 0.06 | 0.94 | 0.20 | 0.0077 |
| 44 | 0.0293, 0.827, 0.976, 0.99, -0.99 | 1.99 | 0.28 | 0.0079 |
| 45 | 0.0305, 0.605, 0.936, 0.65, -0.26 | 1.26 | 0.17 | 0.0076 |
| 46 | 0.0275, 0.912, 0.974, 0.96, -0.67 | 1.67 | 0.25 | 0.0079 |
| 47 | 0.0198, 0.963, 0.970, 0.88, -0.14 | 1.14 | 0.26 | 0.0075 |

The copy's one weight file is `9c4a6df7`, its own; no measured file is equal.

## Token and configuration side (Stage 1)

"Consistent" on the cluster and at home: nothing differs, both files saved by 5.10.0.dev0. The template is the
pin's 17,466-byte file and the fixed conversations render identically.

## For the recipe library

An arbitrary-rank entry (finding 22) with an input-side weight band and a 0.007 row band would match; the
per-layer entry counts the 24 first shares. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus34/measurements/pair-7/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
