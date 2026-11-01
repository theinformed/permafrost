# Reading of the Stage 1 and Stage 2 result: MoonRide/gemma-4-31B-it-heretic-ara-custom against google/gemma-4-31B-it (2026-10-31)

Measured on Nautilus, round 19 piece 1 (push card 5605, probe card 5616, round card 5626, download job 4142666, compare job 4142667 on the background queue, sweep 4142675; pulled home by card 5647). Modified revision `7c0ded77` (2026-05-07 at 00:55Z, a README
commit; the repository was created at 00:10Z and the weights uploaded at 00:29Z), original pinned at `145dc250`
(2026-04-28). The maker's card names the method and its parameters: Heretic 1.2.0 with Arbitrary-Rank Ablation and
row-norm preservation, "created and evaluated using custom system prompt", start layer 30, end layer 57, preserve
weight 0.2116, steer weight 0.0001, overcorrect weight 0.9635, neighbour count 15; it reports 16 refusals in 100
against 99 for the original and a KL divergence of 0.0417. The card lists no targeted component.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 90 flags, on the
cluster and after re-scoring at home: 48 energy shares and 42 within-layer directions. On reading, the footprint is
the arbitrary-rank method on both residual writers of the declared range, with the layers the search weighted near
zero left as residues on either side of the threshold.

- 48 of 1,188 tensors changed: the attention outputs of layers 30 to 56, the card's range with its end index
  exclusive, and 21 of the 27 down projections in the same range. The six down projections left out (layers 30,
  31, 38, 42, 50 and 51) were rewritten at 0.00077 to 0.000999 of their norm, just under the 0.001 line, so the
  largest relative change outside the changed set is 0.000999 and sits inside the declared range; 1,134 tensors
  equal the original and the vision tower is Google's.
- 44 of the 48 are edits: 26 attention outputs (layers 30 to 55) and 18 down projections (32 to 37, 40, 41, 43 to
  45, 47 to 49 and 52 to 55), relative change 0.011 to 0.048, first-value energy share 0.862 to 0.973, first eight
  values 0.924 to 0.983. The other four are residues above the line (the attention output of layer 56 at 0.0018,
  the down projections of 39, 46 and 56 at 0.0010 to 0.0011, first share 0.001 to 0.003), the case of coder3101's
  12B copy in round 18.
- The leading direction sits on the input side on all 48: the copy keeps 0.61 to 0.99 of the original's action on
  the left and −1.93 to 0.37 on the right, the left above the right on every matrix. The searched weight, one minus
  the right fraction, runs from 0.63 (layer 50's attention output) to 2.93 (layer 54's down projection), median 1.76
  on the attention outputs and 1.69 on the down projections; the residues read 0.00.
- The two writers of a layer carry unrelated directions (within-layer cosine 0.002 to 0.10 on the 21 layers with
  both), and the directions share little across layers (0.03 to 0.41 to the group reference): one searched
  direction per matrix, as on the method's other copies.
- Row norms moved by 0.0059 to 0.0077 on the 44 edits and 0.0007 to 0.0008 on the residues, under the card's
  preservation claim: the band finding 22 reads on coder3101's four copies (0.0057 to 0.0080), now on a second
  maker's copy of the same release.
- Ninth measurement on the 31B weight file (shards `eeef8791`, `01891222`; wangzhang, llmfan46, coder3101,
  TrevorJS, huihui-ai's second version, prithivMLmods, null-space, this copy and 3MPER0RR's below). No changed
  matrix has an equal measurement in any field of the eight others, apart from one largest absolute difference
  shared with coder3101's copy, a single bfloat16 step.

| Layer | Attention output: change, E1, E8, left kept, right kept | Down projection: change, E1, E8, left kept, right kept | Weight read | Within-layer cosine | Cross-layer cosine | Row norms |
| --- | --- | --- | --- | --- | --- | --- |
| 30 | 0.0250, 0.953, 0.969, 0.93, -0.90 | - | 1.90/- | - | 0.41/- | 0.0071, - |
| 31 | 0.0236, 0.914, 0.948, 0.93, -0.44 | - | 1.44/- | - | 0.36/- | 0.0071, - |
| 32 | 0.0279, 0.940, 0.963, 0.94, -0.70 | 0.0261, 0.915, 0.960, 0.96, -0.64 | 1.70/1.64 | 0.005 | 0.20/0.27 | 0.0074, 0.0076 |
| 33 | 0.0228, 0.943, 0.958, 0.77, -0.36 | 0.0268, 0.900, 0.955, 0.94, -0.90 | 1.36/1.90 | 0.014 | 0.27/0.33 | 0.0071, 0.0059 |
| 34 | 0.0203, 0.950, 0.965, 0.90, -0.71 | 0.0240, 0.952, 0.976, 0.80, -1.50 | 1.71/2.50 | 0.009 | 0.18/0.28 | 0.0069, 0.0073 |
| 35 | 0.0173, 0.900, 0.926, 0.92, -0.30 | 0.0174, 0.956, 0.968, 0.84, -1.09 | 1.30/2.09 | 0.101 | 0.10/0.31 | 0.0067, 0.0064 |
| 36 | 0.0236, 0.906, 0.934, 0.67, -0.84 | 0.0243, 0.887, 0.951, 0.69, -0.98 | 1.84/1.98 | 0.045 | 0.19/0.24 | 0.0073, 0.0063 |
| 37 | 0.0271, 0.933, 0.957, 0.95, -0.99 | 0.0217, 0.907, 0.952, 0.72, -0.86 | 1.99/1.86 | 0.030 | 0.03/0.22 | 0.0070, 0.0063 |
| 38 | 0.0234, 0.939, 0.957, 0.84, -0.27 | - | 1.27/- | - | 0.16/- | 0.0068, - |
| 39 | 0.0237, 0.948, 0.961, 0.74, -0.46 | 0.0011, 0.003, 0.013, 1.00, 1.00 | 1.46/0.00 | 0.091 | 0.17/0.38 | 0.0074, 0.0007 |
| 40 | 0.0208, 0.929, 0.957, 0.80, -0.59 | 0.0151, 0.945, 0.956, 0.86, -0.44 | 1.59/1.44 | 0.048 | 0.16/0.14 | 0.0076, 0.0067 |
| 41 | 0.0191, 0.903, 0.930, 0.91, -0.95 | 0.0208, 0.900, 0.950, 0.74, -0.60 | 1.95/1.60 | 0.057 | 0.14/0.13 | 0.0069, 0.0068 |
| 42 | 0.0267, 0.930, 0.961, 0.61, -1.02 | - | 2.02/- | - | 0.11/- | 0.0077, - |
| 43 | 0.0187, 0.965, 0.973, 0.72, -0.58 | 0.0132, 0.932, 0.964, 0.74, -0.45 | 1.58/1.45 | 0.022 | 0.25/0.19 | 0.0074, 0.0066 |
| 44 | 0.0309, 0.955, 0.975, 0.95, -0.38 | 0.0124, 0.935, 0.967, 0.80, -0.43 | 1.38/1.43 | 0.015 | 0.23/0.17 | 0.0069, 0.0062 |
| 45 | 0.0284, 0.971, 0.983, 0.98, -0.90 | 0.0190, 0.894, 0.960, 0.79, -0.42 | 1.90/1.42 | 0.035 | 0.12/0.17 | 0.0066, 0.0061 |
| 46 | 0.0304, 0.921, 0.962, 0.96, -0.56 | 0.0010, 0.001, 0.008, 1.00, 1.00 | 1.56/0.00 | 0.053 | 0.15/0.38 | 0.0074, 0.0007 |
| 47 | 0.0112, 0.904, 0.924, 0.96, -0.37 | 0.0130, 0.946, 0.958, 0.76, -0.67 | 1.37/1.67 | 0.028 | 0.19/0.15 | 0.0065, 0.0073 |
| 48 | 0.0435, 0.940, 0.974, 0.98, -1.71 | 0.0154, 0.948, 0.972, 0.96, -0.71 | 2.71/1.71 | 0.046 | 0.10/0.18 | 0.0072, 0.0061 |
| 49 | 0.0314, 0.973, 0.982, 0.74, -0.83 | 0.0186, 0.918, 0.969, 0.96, -0.94 | 1.83/1.94 | 0.008 | 0.27/0.11 | 0.0068, 0.0065 |
| 50 | 0.0237, 0.906, 0.976, 0.99, 0.37 | - | 0.63/- | - | 0.11/- | 0.0072, - |
| 51 | 0.0273, 0.955, 0.975, 0.97, -0.81 | - | 1.81/- | - | 0.14/- | 0.0073, - |
| 52 | 0.0478, 0.862, 0.982, 0.97, -1.24 | 0.0229, 0.946, 0.975, 0.94, -1.25 | 2.24/2.25 | 0.002 | 0.14/0.17 | 0.0070, 0.0077 |
| 53 | 0.0274, 0.929, 0.981, 0.98, -1.52 | 0.0247, 0.913, 0.954, 0.94, -0.34 | 2.52/1.34 | 0.066 | 0.20/0.18 | 0.0071, 0.0068 |
| 54 | 0.0396, 0.953, 0.979, 0.95, -0.87 | 0.0333, 0.885, 0.969, 0.94, -1.93 | 1.87/2.93 | 0.038 | 0.16/0.19 | 0.0075, 0.0076 |
| 55 | 0.0233, 0.924, 0.960, 0.98, -0.96 | 0.0207, 0.870, 0.943, 0.91, -0.65 | 1.96/1.65 | 0.025 | 0.24/0.17 | 0.0076, 0.0073 |
| 56 | 0.0018, 0.002, 0.007, 1.00, 1.00 | 0.0011, 0.002, 0.007, 1.00, 1.00 | 0.00/0.00 | 0.065 | 0.13/0.23 | 0.0008, 0.0007 |

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster on one field, `text_config.moe_intermediate_size`, written as null by
the copy's transformers 5.7.0 save where Google's 5.5.0.dev0 file has no such key; it closes by tool at home
(the 5.6.2 class default is null), and the home card reads "consistent with re-save noted" on the two version
strings. The template is the pinned file byte for byte (16,934 bytes, `94899c0f`), the same file wangzhang's copy
carries; the fixed conversation renders identically.

## For the recipe library

The thirteenth arbitrary-rank copy and the third that edits the down projections beside the attention outputs
(after coder3101's 12B and llmfan46's Magistral copies), the second maker to carry the method's preservation step
at 0.006 to 0.008, and the first residue set that straddles the threshold (six under it, four over it) inside the
declared range. The candidate entry's component list and its residue line both widen; the per-layer weights (0.63
to 2.93) sit inside the method's measured band of 0.32 to 10.18.
