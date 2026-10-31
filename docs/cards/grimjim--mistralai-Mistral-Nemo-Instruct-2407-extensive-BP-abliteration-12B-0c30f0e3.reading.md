# Reading of the Stage 1 and Stage 2 result: grimjim/mistralai-Mistral-Nemo-Instruct-2407-extensive-BP-abliteration-12B against mistralai/Mistral-Nemo-Instruct-2407 (2026-10-31)

Measured on Blueback, round 13 piece 6 (push card 5404, download job 3400579, compare job 3400585; pulled home by
card 5530). Modified revision `6f0527c3` (the weights were uploaded on 2025-11-04 at 06:40Z), original pinned at
`04d8a905`. The card is three sentences: "Biprojected abliteration has been applied the majority of layers in this
model, grounded in three particular layer measurements. This model has been abliterated to excess, and exhibits
subtle coherence gaps. More details to follow."

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 34 flags, on the
cluster and after re-scoring at home, all energy shares at the storage floor (0.987 to 0.995).

- 70 of 363 tensors changed: the attention output and the down projection of layers 3 to 37, 35 of 40 layers, the
  card's majority. The largest relative change outside the changed set is 0.000096 (layer 0's gate projection,
  with layer 39's key projection at 0.000094 and its down projection at 0.000002), a few bfloat16 values in three
  matrices the method does not name.
- One direction per matrix at the floor, relative change 0.013 to 0.022.
- Three shared directions by block, the card's "three particular layer measurements": layers 3 to 16 share one
  (28 matrices, within-block cosine 0.9993), layers 17 to 21 a second (10 matrices) and layers 22 to 37 a third
  (32 matrices); the blocks stand at cosine 0.68 to 0.89 to one another, and the two writers of a layer agree at
  1.000.
- The left kept fraction is −0.003 to 0.005 on all 70, a weight of 1.0; the right is 0.36 to 0.94 and the left is
  below the right on 70 of 70, an output-side edit.
- Row norms moved by 0.004 to 0.032. The method's name carries norm preservation and the five TrevorJS copies made
  with the maker's published scripts hold it within 0.0005; this one reads as a plain projection with no restoration
  step.

| Layer | Attention output: change, E1, E8, left kept, right kept | Down projection: change, E1, E8, left kept, right kept | Weight read | Cross-layer cosine | Row norms |
| --- | --- | --- | --- | --- | --- |
| 3 | 0.0166, 0.991, 0.992, 0.01, 0.91 | 0.0142, 0.988, 0.989, 0.00, 0.59 | 0.99/1.00 | 0.68/0.68 | 0.0102, 0.0077 |
| 4 | 0.0158, 0.990, 0.991, 0.00, 0.86 | 0.0142, 0.988, 0.989, 0.00, 0.52 | 1.00/1.00 | 0.68/0.68 | 0.0098, 0.0089 |
| 5 | 0.0156, 0.990, 0.991, 0.00, 0.86 | 0.0143, 0.988, 0.989, 0.00, 0.57 | 1.00/1.00 | 0.68/0.68 | 0.0099, 0.0095 |
| 6 | 0.0151, 0.990, 0.990, 0.00, 0.78 | 0.0146, 0.989, 0.989, 0.00, 0.59 | 1.00/1.00 | 0.68/0.68 | 0.0093, 0.0098 |
| 7 | 0.0155, 0.990, 0.991, 0.00, 0.76 | 0.0154, 0.990, 0.991, 0.00, 0.69 | 1.00/1.00 | 0.68/0.68 | 0.0110, 0.0126 |
| 8 | 0.0160, 0.991, 0.991, 0.00, 0.87 | 0.0157, 0.990, 0.991, 0.00, 0.77 | 1.00/1.00 | 0.68/0.68 | 0.0098, 0.0151 |
| 9 | 0.0154, 0.990, 0.991, 0.00, 0.77 | 0.0160, 0.991, 0.991, 0.00, 0.77 | 1.00/1.00 | 0.68/0.68 | 0.0100, 0.0147 |
| 10 | 0.0171, 0.992, 0.992, 0.00, 0.85 | 0.0164, 0.991, 0.992, 0.00, 0.81 | 1.00/1.00 | 0.68/0.68 | 0.0143, 0.0164 |
| 11 | 0.0184, 0.993, 0.993, 0.00, 0.87 | 0.0172, 0.992, 0.992, 0.00, 0.77 | 1.00/1.00 | 0.68/0.68 | 0.0239, 0.0169 |
| 12 | 0.0184, 0.993, 0.993, 0.00, 0.89 | 0.0183, 0.993, 0.993, 0.00, 0.77 | 1.00/1.00 | 0.68/0.68 | 0.0267, 0.0201 |
| 13 | 0.0201, 0.994, 0.994, 0.00, 0.89 | 0.0197, 0.994, 0.994, 0.00, 0.73 | 1.00/1.00 | 0.68/0.68 | 0.0220, 0.0215 |
| 14 | 0.0198, 0.994, 0.994, 0.00, 0.94 | 0.0203, 0.994, 0.995, 0.00, 0.74 | 1.00/1.00 | 0.68/0.68 | 0.0324, 0.0233 |
| 15 | 0.0223, 0.995, 0.995, 0.00, 0.81 | 0.0202, 0.994, 0.994, 0.00, 0.72 | 1.00/1.00 | 0.68/0.68 | 0.0287, 0.0203 |
| 16 | 0.0180, 0.993, 0.993, 0.00, 0.85 | 0.0186, 0.993, 0.994, 0.00, 0.75 | 1.00/1.00 | 0.68/0.68 | 0.0254, 0.0201 |
| 17 | 0.0181, 0.993, 0.993, 0.00, 0.71 | 0.0169, 0.992, 0.992, 0.00, 0.51 | 1.00/1.00 | 0.89/0.89 | 0.0157, 0.0078 |
| 18 | 0.0191, 0.993, 0.994, 0.00, 0.67 | 0.0163, 0.991, 0.992, 0.00, 0.44 | 1.00/1.00 | 0.89/0.89 | 0.0227, 0.0093 |
| 19 | 0.0156, 0.990, 0.991, 0.00, 0.72 | 0.0161, 0.991, 0.992, 0.00, 0.41 | 1.00/1.00 | 0.89/0.89 | 0.0103, 0.0107 |
| 20 | 0.0143, 0.989, 0.989, 0.00, 0.75 | 0.0156, 0.990, 0.991, 0.00, 0.37 | 1.00/1.00 | 0.89/0.89 | 0.0160, 0.0088 |
| 21 | 0.0166, 0.991, 0.992, 0.00, 0.79 | 0.0148, 0.989, 0.990, 0.00, 0.44 | 1.00/1.00 | 0.89/0.89 | 0.0110, 0.0071 |
| 22 | 0.0171, 0.992, 0.992, 0.00, 0.87 | 0.0153, 0.990, 0.991, 0.00, 0.45 | 1.00/1.00 | 0.79/0.79 | 0.0130, 0.0086 |
| 23 | 0.0172, 0.992, 0.992, 0.00, 0.88 | 0.0151, 0.990, 0.990, 0.00, 0.42 | 1.00/1.00 | 0.79/0.79 | 0.0124, 0.0084 |
| 24 | 0.0161, 0.991, 0.992, 0.01, 0.94 | 0.0144, 0.989, 0.990, 0.00, 0.40 | 0.99/1.00 | 0.79/0.79 | 0.0053, 0.0087 |
| 25 | 0.0158, 0.990, 0.991, 0.00, 0.89 | 0.0143, 0.989, 0.989, 0.00, 0.38 | 1.00/1.00 | 0.79/0.79 | 0.0125, 0.0078 |
| 26 | 0.0141, 0.988, 0.989, 0.00, 0.75 | 0.0140, 0.988, 0.989, 0.00, 0.38 | 1.00/1.00 | 0.79/0.79 | 0.0093, 0.0077 |
| 27 | 0.0141, 0.988, 0.989, 0.00, 0.73 | 0.0138, 0.988, 0.989, 0.00, 0.39 | 1.00/1.00 | 0.79/0.79 | 0.0046, 0.0066 |
| 28 | 0.0172, 0.992, 0.992, 0.00, 0.84 | 0.0141, 0.988, 0.989, 0.00, 0.39 | 1.00/1.00 | 0.79/0.79 | 0.0130, 0.0077 |
| 29 | 0.0142, 0.988, 0.989, 0.00, 0.92 | 0.0133, 0.987, 0.988, 0.00, 0.44 | 1.00/1.00 | 0.79/0.79 | 0.0069, 0.0093 |
| 30 | 0.0139, 0.988, 0.989, 0.00, 0.83 | 0.0133, 0.987, 0.988, 0.00, 0.47 | 1.00/1.00 | 0.79/0.79 | 0.0072, 0.0053 |
| 31 | 0.0154, 0.990, 0.991, 0.00, 0.67 | 0.0134, 0.987, 0.988, 0.00, 0.47 | 1.00/1.00 | 0.79/0.79 | 0.0159, 0.0084 |
| 32 | 0.0133, 0.987, 0.988, 0.00, 0.80 | 0.0133, 0.987, 0.988, 0.00, 0.46 | 1.00/1.00 | 0.79/0.79 | 0.0095, 0.0079 |
| 33 | 0.0141, 0.988, 0.989, 0.00, 0.75 | 0.0131, 0.987, 0.988, 0.00, 0.44 | 1.00/1.00 | 0.79/0.79 | 0.0037, 0.0078 |
| 34 | 0.0144, 0.989, 0.990, 0.00, 0.92 | 0.0133, 0.987, 0.988, 0.00, 0.44 | 1.00/1.00 | 0.79/0.79 | 0.0134, 0.0122 |
| 35 | 0.0137, 0.988, 0.988, 0.00, 0.85 | 0.0132, 0.987, 0.988, 0.00, 0.44 | 1.00/1.00 | 0.79/0.79 | 0.0074, 0.0067 |
| 36 | 0.0156, 0.990, 0.991, 0.00, 0.89 | 0.0137, 0.988, 0.988, 0.00, 0.42 | 1.00/1.00 | 0.79/0.79 | 0.0107, 0.0057 |
| 37 | 0.0133, 0.987, 0.988, 0.00, 0.84 | 0.0138, 0.988, 0.989, 0.00, 0.36 | 1.00/1.00 | 0.79/0.79 | 0.0066, 0.0062 |

The cross-layer cosine column is against the median direction of all 70 and reads the three blocks: 0.68 on layers
3 to 16, 0.89 on 17 to 21, 0.79 on 22 to 37. Against DuoNeural's copy of the same base (pair 7, one shared direction
on all 40 layers at weight 0.3), no changed matrix has an equal measurement in any field.

## Token and configuration side (Stage 1)

"Unexplained differences" on two fields, the renaming of `torch_dtype` to `dtype` in a re-save from 4.43.0.dev0 to
4.57.1; the copy adds a `chat_template.jinja` of 4,032 bytes carrying the original's embedded template. The fixed
conversation renders identically.

## For the recipe library

Consistent with the card's three sentences and more exact than them: 35 layers, both writers, three block
directions, weight 1.0 on the output side. The rows are the one departure from the method's name, moved by up to
0.032 where the norm-preserving copies made with the maker's scripts stay within 0.0005. The saved direction vectors are not committed;
the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/blueback13/measurements/pair-6/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
