# Reading of the Stage 1 and Stage 2 result: Iambackup/gemma-4-12B-it-uncensored against google/gemma-4-12B-it (2026-10-31)

Measured on Nautilus, round 19 piece 4 (push card 5605, probe card 5616, round card 5626, download job 4142666, compare job 4142670 on the background queue, sweep 4142675; pulled home by card 5647). Modified revision `d26905f1` (one commit, 2026-06-14 at 15:38Z,
"Duplicate from TrevorJS/gemma-4-12B-it-uncensored"; the README is TrevorJS's, 4,929 bytes, byte for byte),
original pinned at `5926caa4` (2026-06-04). The card is the source's: norm-preserving biprojected abliteration with one
direction per layer on the attention output and the down projection of layers 15 to 47, 6 refusals in 100, KL
0.0556. The repository's `base_model` field names Google.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 1 flag, on the
cluster and after re-scoring at home, the flag TrevorJS's report carries: layer 42's attention output at a first
share of 0.9899 on a relative change of 0.0172, inside the storage floor. The weight file is TrevorJS's: the hub
lists one `model.safetensors` of 23,919,549,408 bytes under the same LFS checksum (`dd7fcab672`) in the three
repositories, the comparison read the same shard checksum, and every measured field of all 677 tensors equals the
round 8 report (`results/weights/TrevorJS-gemma-4-12B-it-uncensored.json`): 66 changed, the attention output and
the down projection of layers 15 to 47, one direction per layer (within-layer cosine 0.970 to 0.999), first share
0.990 to 0.996, left kept −0.01 to 0.68 on the attention outputs and 0.00 to 0.41 on the down projections, the
left below the right on 65 of 66, rows within 0.0004 of the original's under the biprojection's restoration,
611 tensors equal to the original. The reading is in `TrevorJS--gemma-4-12B-it-uncensored-*.reading.md`;
Justbackup's copy (piece 5) is the same file again.

| Layer | Attention output: change, E1, E8, left kept, right kept | Down projection: change, E1, E8, left kept, right kept | Weight read | Within-layer cosine | Cross-layer cosine | Row norms |
| --- | --- | --- | --- | --- | --- | --- |
| 15 | 0.0159, 0.995, 0.995, 0.21, 0.70 | 0.0182, 0.996, 0.996, 0.01, 0.46 | 0.79/0.99 | 0.985 | 0.17/0.17 | 0.0002, 0.0001 |
| 16 | 0.0167, 0.995, 0.996, 0.68, 0.69 | 0.0189, 0.996, 0.996, 0.01, 0.50 | 0.32/0.99 | 0.980 | 0.27/0.25 | 0.0002, 0.0001 |
| 17 | 0.0166, 0.994, 0.995, 0.06, 0.70 | 0.0176, 0.995, 0.996, 0.05, 0.46 | 0.94/0.95 | 0.995 | 0.26/0.26 | 0.0001, 0.0001 |
| 18 | 0.0168, 0.995, 0.995, 0.14, 0.57 | 0.0170, 0.995, 0.995, 0.02, 0.48 | 0.86/0.98 | 0.991 | 0.27/0.28 | 0.0002, 0.0001 |
| 19 | 0.0157, 0.993, 0.994, 0.18, 0.69 | 0.0165, 0.994, 0.995, 0.04, 0.42 | 0.82/0.96 | 0.985 | 0.25/0.27 | 0.0002, 0.0002 |
| 20 | 0.0165, 0.994, 0.994, 0.58, 0.63 | 0.0178, 0.995, 0.995, 0.10, 0.40 | 0.42/0.90 | 0.991 | 0.26/0.25 | 0.0002, 0.0002 |
| 21 | 0.0177, 0.993, 0.994, 0.68, 0.76 | 0.0192, 0.994, 0.995, 0.15, 0.47 | 0.32/0.85 | 0.991 | 0.30/0.29 | 0.0004, 0.0001 |
| 22 | 0.0166, 0.993, 0.994, 0.61, 0.65 | 0.0196, 0.994, 0.995, 0.14, 0.47 | 0.39/0.86 | 0.991 | 0.39/0.38 | 0.0002, 0.0001 |
| 23 | 0.0168, 0.993, 0.993, 0.29, 0.62 | 0.0206, 0.994, 0.995, 0.03, 0.52 | 0.71/0.97 | 0.994 | 0.44/0.43 | 0.0001, 0.0001 |
| 24 | 0.0157, 0.992, 0.992, 0.19, 0.65 | 0.0186, 0.994, 0.994, 0.15, 0.49 | 0.81/0.85 | 0.996 | 0.45/0.46 | 0.0002, 0.0001 |
| 25 | 0.0156, 0.992, 0.993, 0.19, 0.76 | 0.0178, 0.993, 0.993, 0.12, 0.52 | 0.81/0.88 | 0.991 | 0.43/0.44 | 0.0002, 0.0002 |
| 26 | 0.0175, 0.993, 0.993, 0.36, 0.64 | 0.0189, 0.993, 0.994, 0.26, 0.46 | 0.64/0.74 | 0.995 | 0.44/0.42 | 0.0002, 0.0001 |
| 27 | 0.0167, 0.992, 0.993, 0.16, 0.66 | 0.0187, 0.993, 0.994, 0.13, 0.48 | 0.84/0.87 | 0.998 | 0.46/0.45 | 0.0002, 0.0001 |
| 28 | 0.0169, 0.992, 0.992, 0.14, 0.63 | 0.0187, 0.993, 0.994, 0.09, 0.38 | 0.86/0.91 | 0.998 | 0.50/0.50 | 0.0003, 0.0001 |
| 29 | 0.0184, 0.993, 0.993, 0.05, 0.64 | 0.0204, 0.994, 0.994, 0.02, 0.47 | 0.95/0.98 | 0.997 | 0.54/0.55 | 0.0001, 0.0001 |
| 30 | 0.0170, 0.992, 0.992, 0.09, 0.64 | 0.0188, 0.993, 0.994, 0.14, 0.44 | 0.91/0.86 | 0.994 | 0.56/0.56 | 0.0002, 0.0001 |
| 31 | 0.0182, 0.993, 0.993, 0.14, 0.62 | 0.0171, 0.992, 0.993, 0.09, 0.41 | 0.86/0.91 | 0.989 | 0.56/0.57 | 0.0002, 0.0001 |
| 32 | 0.0174, 0.992, 0.993, 0.42, 0.55 | 0.0175, 0.992, 0.993, 0.07, 0.38 | 0.58/0.93 | 0.994 | 0.57/0.56 | 0.0002, 0.0001 |
| 33 | 0.0167, 0.991, 0.992, 0.25, 0.67 | 0.0178, 0.993, 0.993, 0.04, 0.25 | 0.75/0.96 | 0.996 | 0.59/0.58 | 0.0002, 0.0001 |
| 34 | 0.0159, 0.991, 0.991, 0.16, 0.59 | 0.0174, 0.992, 0.993, 0.02, 0.24 | 0.84/0.98 | 0.997 | 0.61/0.60 | 0.0002, 0.0001 |
| 35 | 0.0155, 0.990, 0.991, 0.07, 0.62 | 0.0170, 0.992, 0.992, 0.01, 0.25 | 0.93/0.99 | 0.996 | 0.63/0.62 | 0.0001, 0.0001 |
| 36 | 0.0163, 0.990, 0.991, 0.27, 0.81 | 0.0162, 0.991, 0.992, 0.01, 0.25 | 0.73/0.99 | 0.993 | 0.63/0.62 | 0.0002, 0.0001 |
| 37 | 0.0165, 0.991, 0.992, 0.01, 0.57 | 0.0163, 0.991, 0.992, 0.03, 0.34 | 0.99/0.97 | 0.998 | 0.63/0.63 | 0.0002, 0.0001 |
| 38 | 0.0180, 0.992, 0.993, 0.26, 0.61 | 0.0170, 0.992, 0.992, 0.02, 0.32 | 0.74/0.98 | 0.995 | 0.61/0.60 | 0.0002, 0.0001 |
| 39 | 0.0163, 0.991, 0.991, 0.14, 0.68 | 0.0173, 0.992, 0.992, 0.01, 0.30 | 0.86/0.99 | 0.995 | 0.57/0.57 | 0.0002, 0.0001 |
| 40 | 0.0166, 0.991, 0.991, 0.02, 0.59 | 0.0179, 0.992, 0.993, 0.01, 0.27 | 0.98/0.99 | 0.997 | 0.56/0.55 | 0.0002, 0.0001 |
| 41 | 0.0166, 0.991, 0.991, 0.07, 0.62 | 0.0176, 0.992, 0.992, 0.01, 0.33 | 0.93/0.99 | 0.998 | 0.53/0.52 | 0.0001, 0.0001 |
| 42 | 0.0172, 0.990, 0.991, 0.12, 0.85 | 0.0171, 0.992, 0.992, 0.02, 0.35 | 0.88/0.98 | 0.995 | 0.53/0.52 | 0.0002, 0.0001 |
| 43 | 0.0176, 0.991, 0.992, -0.01, 0.74 | 0.0172, 0.992, 0.992, 0.02, 0.42 | 1.01/0.98 | 0.996 | 0.52/0.52 | 0.0002, 0.0001 |
| 44 | 0.0165, 0.991, 0.991, 0.43, 0.70 | 0.0180, 0.992, 0.993, 0.01, 0.34 | 0.57/0.99 | 0.995 | 0.50/0.49 | 0.0002, 0.0001 |
| 45 | 0.0174, 0.992, 0.992, 0.01, 0.64 | 0.0187, 0.993, 0.993, 0.00, 0.33 | 0.99/1.00 | 0.999 | 0.44/0.43 | 0.0002, 0.0001 |
| 46 | 0.0163, 0.991, 0.991, 0.20, 0.65 | 0.0180, 0.992, 0.993, 0.41, 0.30 | 0.80/0.59 | 0.995 | 0.36/0.37 | 0.0002, 0.0001 |
| 47 | 0.0187, 0.992, 0.992, 0.34, 0.64 | 0.0171, 0.991, 0.992, 0.07, 0.43 | 0.66/0.93 | 0.970 | 0.35/0.36 | 0.0001, 0.0003 |

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster, six fields, four at home. The pin is the parent's pin, and the token side reads as the parent's report did in round 8: the two version strings (5.10.0.dev0 to 5.12.0), the three sub-configuration data types the save writes as `bfloat16` (two of them where Google's file has null, closed at home by the rule added this round) and the four class defaults the save omits (640, 640, 640 and 48, finding 11), left as printed under the kit's 5.6.2 and closed under 5.12.0. The template is Google's file at the pin byte for byte (17,466 bytes, `36e3a42e`) and the fixed conversation renders identically.

## For the recipe library

Nothing new on the weights: a byte-identical re-upload of TrevorJS's 12B copy, made with the hub's duplicate
function, under an account named for the purpose. The pinner should pair a repository whose one commit says
"Duplicate from" with that source before it pairs it with the stated original, and the hub's file listing gives
the answer before any download: the LFS checksum of the weight file is the parent's (finding 38).
