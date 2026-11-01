# Reading of the Stage 1 and Stage 2 result: 3MPER0RR/gemma-4-31b-it-3MPER0RR-abliterated against google/gemma-4-31B-it (2026-10-31)

Measured on Nautilus, round 19 piece 2 (push card 5605, probe card 5616, round card 5626, download job 4142666, compare job 4142668 on the background queue, sweep 4142675; pulled home by card 5647). Modified revision `5f97708d` (2026-10-27, the latest of six README
commits; the repository was created on 2026-09-01 at 11:04Z and the weights uploaded a minute later as one folder,
with a `checkpoints/google--gemma-4-31B-it.jsonl` record deleted four minutes after that), original pinned at
`842da379` (2026-07-20). The card is 308 bytes: "Experimental modified / abliterated versions", "Trials: [200]",
"Status: Tested and saved", and the maker's name. It names no method, no layer and no component.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 22 flags, on the
cluster and after re-scoring at home: 20 energy shares of 0.981 to 0.986 on the attention outputs, the storage
floor on changes of 0.010 to 0.013, and two within-layer cosines of 0.925 on layer 59. On reading, the copy is one
direction per layer on the top third of the model, output side, at one strength per kind.

- 41 of 1,188 tensors changed: the down projections of layers 39 to 59 (21) and the attention outputs of layers 40
  to 59 (20). Nothing else moved; the largest relative change outside the changed set is exactly 0 and 1,147
  tensors equal the original. The maker's 12B copy (round 18) changed 48 matrices on 29 layers chosen through the
  middle of that model; this one takes a contiguous block at the top.
- Rank one at the floor: first-value share 0.981 to 0.996, the first singular value 26 to 113 times the second,
  leftover 0.0012 to 0.0017 of each norm. Within a layer the two writers share one direction (cosine 0.925 to
  0.999); across layers the directions drift, 0.29 to 0.82 to the group reference, highest at layers 46 to 51.
- Output side on 41 of 41: the left kept fraction is below the right on every matrix. Along the leading direction
  the down projections keep −0.40 to −0.16 of the original's action (−0.34 to −0.40 on layers 41 to 58), a weight
  of 1.16 to 1.40 read as one minus the fraction, and the attention outputs keep 0.18 to 0.66 (0.18 to 0.44 apart
  from layer 52 at 0.66), a weight of 0.34 to 0.82. The two kinds carry two strengths, steady across the block;
  the maker's 12B copy read no side and no strength.
- Rows moved by 0.0016 to 0.0058, and by 0.042 on layer 59's down projection, under no preservation claim.
- Ninth measurement on the 31B weight file, saved again in 13 shards under transformers 5.16.1. No changed matrix
  has an equal measurement in any field of the eight others.

| Layer | Attention output: change, E1, E8, left kept, right kept | Down projection: change, E1, E8, left kept, right kept | Weight read | Within-layer cosine | Cross-layer cosine | Row norms |
| --- | --- | --- | --- | --- | --- | --- |
| 39 | - | 0.0209, 0.995, 0.995, -0.24, 0.15 | -/1.24 | - | -/0.48 | -, 0.0035 |
| 40 | 0.0113, 0.984, 0.985, 0.43, 0.67 | 0.0202, 0.995, 0.995, -0.29, 0.06 | 0.57/1.29 | 0.995 | 0.51/0.55 | 0.0032, 0.0032 |
| 41 | 0.0104, 0.982, 0.983, 0.26, 0.63 | 0.0194, 0.994, 0.994, -0.34, 0.05 | 0.74/1.34 | 0.997 | 0.59/0.62 | 0.0024, 0.0027 |
| 42 | 0.0103, 0.981, 0.982, 0.25, 0.60 | 0.0192, 0.994, 0.994, -0.35, 0.01 | 0.75/1.35 | 0.999 | 0.65/0.68 | 0.0016, 0.0018 |
| 43 | 0.0105, 0.981, 0.982, 0.24, 0.65 | 0.0190, 0.994, 0.994, -0.35, -0.04 | 0.76/1.35 | 0.997 | 0.69/0.71 | 0.0018, 0.0017 |
| 44 | 0.0108, 0.982, 0.983, 0.36, 0.67 | 0.0190, 0.994, 0.994, -0.36, -0.04 | 0.64/1.36 | 0.994 | 0.74/0.76 | 0.0016, 0.0016 |
| 45 | 0.0109, 0.982, 0.983, 0.35, 0.77 | 0.0191, 0.994, 0.994, -0.36, -0.03 | 0.65/1.36 | 0.992 | 0.76/0.78 | 0.0024, 0.0018 |
| 46 | 0.0114, 0.983, 0.984, 0.23, 0.60 | 0.0196, 0.994, 0.994, -0.36, -0.05 | 0.77/1.36 | 0.996 | 0.80/0.80 | 0.0021, 0.0018 |
| 47 | 0.0117, 0.983, 0.985, 0.44, 0.87 | 0.0191, 0.994, 0.994, -0.34, -0.05 | 0.56/1.34 | 0.996 | 0.80/0.81 | 0.0026, 0.0016 |
| 48 | 0.0115, 0.983, 0.985, 0.34, 0.74 | 0.0196, 0.994, 0.994, -0.36, -0.01 | 0.66/1.36 | 0.993 | 0.82/0.82 | 0.0019, 0.0023 |
| 49 | 0.0125, 0.986, 0.987, 0.42, 0.64 | 0.0196, 0.994, 0.994, -0.38, 0.06 | 0.58/1.38 | 0.980 | 0.80/0.82 | 0.0033, 0.0024 |
| 50 | 0.0116, 0.983, 0.985, 0.22, 0.78 | 0.0204, 0.994, 0.995, -0.38, 0.38 | 0.78/1.38 | 0.995 | 0.81/0.80 | 0.0023, 0.0030 |
| 51 | 0.0119, 0.985, 0.986, 0.18, 0.53 | 0.0207, 0.994, 0.995, -0.30, 0.30 | 0.82/1.30 | 0.997 | 0.81/0.78 | 0.0020, 0.0047 |
| 52 | 0.0123, 0.985, 0.986, 0.66, 0.70 | 0.0216, 0.995, 0.995, -0.27, 0.15 | 0.34/1.27 | 0.986 | 0.77/0.77 | 0.0020, 0.0024 |
| 53 | 0.0111, 0.982, 0.983, 0.21, 0.57 | 0.0201, 0.994, 0.994, -0.37, 0.05 | 0.79/1.37 | 0.999 | 0.79/0.77 | 0.0020, 0.0025 |
| 54 | 0.0109, 0.982, 0.983, 0.22, 0.62 | 0.0202, 0.994, 0.994, -0.39, 0.01 | 0.78/1.39 | 0.998 | 0.77/0.75 | 0.0019, 0.0017 |
| 55 | 0.0110, 0.982, 0.983, 0.29, 0.77 | 0.0207, 0.994, 0.995, -0.39, 0.04 | 0.71/1.39 | 0.997 | 0.73/0.71 | 0.0026, 0.0020 |
| 56 | 0.0119, 0.985, 0.986, 0.23, 0.68 | 0.0211, 0.995, 0.995, -0.39, 0.00 | 0.77/1.39 | 0.998 | 0.68/0.67 | 0.0019, 0.0018 |
| 57 | 0.0111, 0.982, 0.984, 0.24, 0.86 | 0.0208, 0.994, 0.995, -0.36, -0.02 | 0.76/1.36 | 0.998 | 0.64/0.63 | 0.0021, 0.0019 |
| 58 | 0.0129, 0.986, 0.987, 0.31, 0.71 | 0.0226, 0.995, 0.995, -0.40, 0.31 | 0.69/1.40 | 0.992 | 0.51/0.51 | 0.0031, 0.0031 |
| 59 | 0.0121, 0.985, 0.986, 0.43, 0.64 | 0.0244, 0.996, 0.996, -0.16, 0.63 | 0.57/1.16 | 0.925 | 0.29/0.34 | 0.0058, 0.0424 |

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster on four `text_config` fields, three at home (5.6.2 closes
`moe_intermediate_size`, written as null). The three are the transformers 5.16 save form met on the maker's 12B
copy in round 18: `global_head_dim` 512 and `num_global_key_value_heads` 4 leave the text configuration and
return as a `per_layer_config` map keyed by the ten global layers (5, 11, 17, 23, 29, 35, 41, 47, 53 and 59),
each with `head_dim` 512 and `num_key_value_heads` 4, the values Google's file states once. The version strings
read 5.5.0.dev0 to 5.16.1 in both files. The template is the pinned file byte for byte (18,681 bytes,
`ae53464b`) and the fixed conversation renders identically. Loaded under 5.12.0 at home, `global_head_dim` closes
as the class default and the two others stay, because 5.12 has no `per_layer_config`.

## For the recipe library

The maker's second copy and the first to read a side: one direction per layer, output side, two strengths (1.16 to
1.40 on the down projections, 0.34 to 0.82 on the attention outputs) on a contiguous top block, under a card that
says nothing. The scorer's floor flags on the attention outputs are the storage case of finding 3 and the entry
needs the `directional-per-layer-selected` line to carry one strength per kind. On the token side the 5.16
per-layer map is now in two of the maker's copies and the metadata tool still closes it by hand.
