# Reading of the Stage 1 and Stage 2 result: prithivMLmods/gemma-4-12B-it-heretic_decensored against google/gemma-4-12B-it (2026-10-31)

Measured on Nautilus, round 19 piece 6 (push card 5605, probe card 5616, round card 5626, download job 4142666, compare job 4142672 on the background queue, sweep 4142675; pulled home by card 5647). Modified revision `6769de51` (2026-06-17, the last of seven README commits;
the repository was created on 2026-06-15 at 19:20Z and the weights uploaded on 06-16 at 23:00Z), original pinned
at `5926caa4` (2026-06-04). The card names Heretic and prints a parameter table in the tool's standard form:
`direction_index` 29.56, `attn.o_proj` maximum weight 1.18 at position 39.94 and minimum weight 0.81 at distance
25.73, `mlp.down_proj` maximum weight 1.37 at position 46.27 and minimum weight 0.97 at distance 21.63; it reports
34 refusals in 100 against 99 for the original and a KL divergence of 0.0366, and points to a trials log in
another account. This is the maker's first measured copy that is not a re-upload of a huihui-ai edit (its four
Uncensored-MAX copies, finding 9).

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection-selected`, 6 flags, on the
cluster and after re-scoring at home: three direction cosines of 0.899 to 0.910 (the attention outputs of layers
15, 20 and 21), two energy shares of 0.980 and 0.989 (layers 44 and 42) and one cross-kind direction at 0.617. On
reading, the copy is one shared direction, rank one, on 56 matrices, and the kept fraction along it reads neither
the card's kernel nor a side.

- 56 of 677 tensors changed: the attention outputs of layers 15 to 47 and the down projections of layers 25 to 47.
  Nothing else moved; the largest relative change outside the changed set is exactly 0 and 621 tensors equal the
  original. The copy's first shard (`a813e9d9`) is byte-equal to the first shard of 3MPER0RR's and igorls's 12B
  copies: the same library sharding of a block none of the three edits touches.
- One shared direction: cosine 0.899 to 0.998 to the group reference (median 0.986 on the attention outputs,
  0.994 on the down projections), the card's single `direction_index`. Rank one: first-value share 0.980 to 0.996,
  the first singular value 8 to 102 times the second.
- The kept fraction along that direction follows no kernel. The card's weights would leave 0.19 to −0.18 of the
  original's action on the attention outputs, falling smoothly to the minimum at layer 40, and 0.03 to −0.37 on
  the down projections with the minimum at 46. The weights read 0.98, 0.96, 0.87, 0.63 and 0.76 on the left of
  layers 15 to 19, 0.37, 0.57, 0.82, 0.16 and 0.89 on 40 to 44, and −0.01 to 0.98 over the 33 attention outputs;
  −0.28 to 0.77 on the down projections, 0.72 at layer 46 where the card's weight peaks. The right fraction is
  0.35 to 0.89 and 0.07 to 0.49. The left is below the right on 11 of 33 and 14 of 23: no side.
- Rows moved by 0.0029 to 0.0100 under no preservation claim.
- Fifteenth measurement of a copy on the 12B weight file (`5a84cb31`). No changed matrix has an equal measurement
  in any field of the others, apart from one largest absolute difference shared with lemuralabs's copy, a single
  bfloat16 step.

| Layer | Attention output: change, E1, E8, left kept, right kept | Down projection: change, E1, E8, left kept, right kept | Within-layer cosine | Cross-layer cosine | Row norms |
| --- | --- | --- | --- | --- | --- |
| 15 | 0.0234, 0.995, 0.997, 0.98, 0.43 | - | - | 0.90/- | 0.0030, - |
| 16 | 0.0204, 0.995, 0.995, 0.96, 0.62 | - | - | 0.95/- | 0.0035, - |
| 17 | 0.0166, 0.992, 0.993, 0.87, 0.70 | - | - | 1.00/- | 0.0041, - |
| 18 | 0.0151, 0.990, 0.992, 0.63, 0.59 | - | - | 0.99/- | 0.0034, - |
| 19 | 0.0152, 0.990, 0.993, 0.76, 0.61 | - | - | 1.00/- | 0.0045, - |
| 20 | 0.0249, 0.995, 0.997, 0.97, 0.35 | - | - | 0.90/- | 0.0034, - |
| 21 | 0.0248, 0.993, 0.997, 0.97, 0.44 | - | - | 0.91/- | 0.0050, - |
| 22 | 0.0202, 0.990, 0.996, 0.93, 0.52 | - | - | 0.97/- | 0.0053, - |
| 23 | 0.0176, 0.993, 0.994, 0.85, 0.59 | - | - | 1.00/- | 0.0042, - |
| 24 | 0.0170, 0.993, 0.994, 0.72, 0.61 | - | - | 1.00/- | 0.0040, - |
| 25 | 0.0160, 0.992, 0.994, 0.66, 0.72 | 0.0187, 0.993, 0.994, 0.77, 0.39 | 0.996 | 1.00/0.98 | 0.0072, 0.0045 |
| 26 | 0.0212, 0.994, 0.996, 0.88, 0.52 | 0.0197, 0.994, 0.995, 0.71, 0.39 | 0.981 | 0.99/0.96 | 0.0044, 0.0039 |
| 27 | 0.0193, 0.995, 0.995, 0.46, 0.64 | 0.0210, 0.995, 0.995, 0.38, 0.49 | 0.997 | 0.98/0.98 | 0.0062, 0.0062 |
| 28 | 0.0192, 0.994, 0.995, 0.42, 0.56 | 0.0204, 0.995, 0.995, 0.17, 0.37 | 0.997 | 0.98/0.99 | 0.0075, 0.0050 |
| 29 | 0.0191, 0.994, 0.994, -0.01, 0.64 | 0.0219, 0.995, 0.996, 0.08, 0.43 | 0.996 | 0.96/0.99 | 0.0093, 0.0083 |
| 30 | 0.0183, 0.994, 0.994, 0.18, 0.61 | 0.0205, 0.995, 0.995, 0.26, 0.38 | 0.994 | 0.96/0.99 | 0.0064, 0.0061 |
| 31 | 0.0192, 0.994, 0.995, 0.22, 0.61 | 0.0198, 0.994, 0.995, 0.61, 0.31 | 0.975 | 0.96/0.98 | 0.0097, 0.0043 |
| 32 | 0.0248, 0.996, 0.997, 0.89, 0.37 | 0.0202, 0.993, 0.995, 0.64, 0.29 | 0.967 | 0.97/0.99 | 0.0057, 0.0055 |
| 33 | 0.0219, 0.995, 0.996, 0.89, 0.49 | 0.0199, 0.994, 0.995, 0.62, 0.21 | 0.977 | 0.99/0.99 | 0.0044, 0.0051 |
| 34 | 0.0217, 0.995, 0.996, 0.82, 0.46 | 0.0194, 0.994, 0.995, 0.32, 0.18 | 0.969 | 1.00/1.00 | 0.0069, 0.0040 |
| 35 | 0.0202, 0.995, 0.995, 0.74, 0.54 | 0.0193, 0.994, 0.994, 0.07, 0.16 | 0.971 | 1.00/1.00 | 0.0050, 0.0034 |
| 36 | 0.0199, 0.994, 0.995, 0.79, 0.48 | 0.0194, 0.994, 0.995, 0.00, 0.15 | 0.965 | 1.00/1.00 | 0.0035, 0.0029 |
| 37 | 0.0190, 0.994, 0.994, 0.05, 0.51 | 0.0207, 0.994, 0.995, 0.46, 0.26 | 0.988 | 0.97/1.00 | 0.0039, 0.0040 |
| 38 | 0.0248, 0.995, 0.997, 0.91, 0.40 | 0.0204, 0.995, 0.995, 0.35, 0.11 | 0.929 | 0.97/1.00 | 0.0064, 0.0032 |
| 39 | 0.0210, 0.993, 0.995, 0.71, 0.59 | 0.0197, 0.994, 0.995, -0.12, 0.17 | 0.954 | 1.00/0.99 | 0.0081, 0.0040 |
| 40 | 0.0214, 0.995, 0.995, 0.37, 0.48 | 0.0205, 0.995, 0.995, -0.06, 0.18 | 0.989 | 0.99/1.00 | 0.0059, 0.0032 |
| 41 | 0.0201, 0.994, 0.995, 0.57, 0.49 | 0.0205, 0.995, 0.995, -0.02, 0.15 | 0.986 | 0.99/1.00 | 0.0054, 0.0042 |
| 42 | 0.0214, 0.989, 0.996, 0.82, 0.76 | 0.0208, 0.995, 0.995, 0.06, 0.23 | 0.956 | 1.00/1.00 | 0.0065, 0.0050 |
| 43 | 0.0190, 0.991, 0.994, 0.16, 0.89 | 0.0213, 0.995, 0.995, 0.03, 0.18 | 0.996 | 0.97/1.00 | 0.0056, 0.0041 |
| 44 | 0.0251, 0.980, 0.997, 0.89, 0.68 | 0.0219, 0.995, 0.996, 0.07, 0.09 | 0.905 | 0.97/1.00 | 0.0100, 0.0040 |
| 45 | 0.0197, 0.992, 0.995, 0.48, 0.67 | 0.0218, 0.995, 0.996, -0.14, 0.08 | 0.988 | 0.99/1.00 | 0.0086, 0.0041 |
| 46 | 0.0188, 0.993, 0.994, 0.60, 0.64 | 0.0251, 0.996, 0.997, 0.72, 0.07 | 0.991 | 0.99/0.97 | 0.0073, 0.0042 |
| 47 | 0.0224, 0.993, 0.996, 0.92, 0.52 | 0.0208, 0.995, 0.995, -0.28, 0.09 | 0.777 | 0.97/0.97 | 0.0055, 0.0029 |

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster on six configuration fields, four at home. The copy's transformers
5.12.1 save lacks the four values Google's 5.10.0.dev0 file carries, the audio tower's `audio_samples_per_token`,
`hidden_size` and `output_proj_dims` (640, 640, 640) and the vision patch size (48), and writes `bfloat16` into
the audio and vision sub-configurations where Google's file has null. The two data types close by tool at home
under the rule added this round (the sub-configuration repeats the top-level data type where the other side left
it null); the four defaults stay as printed because the kit's 5.6.2 cannot load this family's `gemma4_unified`
configuration. Loaded under 5.12.0, both files give 640, 640, 640 and 48 and the second rule added this round
closes them (finding 11, finding 39). The template is the pinned file byte for byte (17,466 bytes, `36e3a42e`)
and the fixed conversation renders identically.

## For the recipe library

The second copy whose kept fraction reads no weight and no side on a rank-one shared direction (3MPER0RR's 12B copy
in round 18 was the first), and the first of the two under a card that states the kernel. What the weights
certify is the direction, the rank, the component list and the layer range; the weights the card prints are not
in the kept fraction, and the census records the disagreement rather than a reading of the schedule.
