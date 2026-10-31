# Reading of the Stage 1 and Stage 2 result: null-space/gemma-4-31b-it-abliterated against google/gemma-4-31B-it (2026-10-31)

Measured on Nautilus, round 18 piece 4 (push card 5473, round card 5477, download job 4125751, compare job 4125755
on the background queue, sweep 4125760; pulled home by card 5493). Modified revision `b81077ed` (2026-04-06, the
commit that added the card's Wikitext-2 metrics; the repository was created on 2026-04-03 at 00:42Z and the weights
uploaded six minutes later), original pinned at `419b2efe` (2026-04-02, the release commit). The maker's card
describes the method in detail: refusal directions measured in float32 on 4,634 harmful and 640 harmless prompts,
an SVD of rank 32 per layer, the top 8 directions projected out of `o_proj` and `down_proj` in layers 20 to 59 with
norm preservation and "projected orthogonalization", at a scale per layer of 0.35 to 0.45 on layers 20 to 37, 0.4 to
1.35 on 38 to 51 around a peak at layer 41, and 0.6 to 1.35 on 52 to 59 around a peak at layer 58; the vision tower
copied verbatim. It reports cold refusal 67 to 32 percent, perplexity 1.495 to 1.714, median KL 0.025, and a
key-value cache comparison in which layers 0 to 20 are "bitwise identical".

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 80 flags, on the
cluster and after re-scoring at home, all 80 energy shares. On reading, the flags measure exactly what the card
says: eight directions per matrix, so no first share near 1, and a scale per layer the kept fraction reads to two
decimals.

- 80 of 1,188 tensors changed: the attention output and the down projection of layers 20 to 59, the card's forty
  layers. Nothing else moved; the largest relative change outside the changed set is exactly 0, 1,108 tensors equal
  the original, and the vision tower is Google's. The card's own key-value table calls layers 0 to 20 unmodified
  while its configuration says 20 to 59; the weights say layer 20 is edited (relative change 0.0056 and 0.0058).
- Eight directions: first-value share 0.584 to 0.694 (median 0.66), the first eight 0.937 to 0.996, the first
  singular value 1.7 to 2.8 times the second. The leading direction carries about two thirds of each change and the
  next seven the rest, with a leftover beyond eight of 0.0005 to 0.0025 of the norm.
- The scale reads from the kept fraction. Along the leading direction the copy keeps 0.65 of the original's action on
  layers 20 to 26, 0.60 on 27 and 28, 0.65 on 29 to 35, 0.60 on 36, 0.55 on 37, 0.55 and 0.45 on 38 and 39, −0.10 on
  40, −0.35 on 41, −0.10 on 42, 0.30 to 0.60 rising again from 43 to 51, 0.40 on 52, −0.15 on 53, 0.00 on 54 to 56,
  −0.25 on 57, −0.35 on 58 and −0.15 on 59; one minus each is the card's schedule, 0.35 to 0.45 on 20 to 37, a bell
  to 1.35 at layer 41 and a second to 1.35 at layer 58, on both writers of every layer to the second decimal. The
  left fraction is below the right on all 80, an output-side edit.
- Two direction sets. Layers 20 to 51 share one leading direction (cross-layer cosine 1.000 on all 64 matrices) and
  layers 52 to 59 share another, at cosine 0.18 to the first; within a layer the two writers agree at 0.998 to 1.000.
  The card measures directions per layer and names two peaks, 41 and 58; what the weights carry is the peak layer's
  subspace applied to each block.
- Row norms moved by 0.025 to 0.098 on the 64 matrices of layers 20 to 51 and by 0.0018 to 0.0064 on the 14 of
  layers 52 to 58 (0.0060 and 0.041 on layer 59), under one preservation claim for all: the restoration held on the
  second block and left two to ten percent on the first.

| Layer | Attention output: change, E1, E8, left | Down projection: change, E1, E8, left | Scale read | Direction set | Row norms |
| --- | --- | --- | --- | --- | --- |
| 20 | 0.0056, 0.621, 0.937, 0.65 | 0.0058, 0.654, 0.940, 0.65 | 0.35 | A | 0.030, 0.027 |
| 21 | 0.0059, 0.654, 0.942, 0.65 | 0.0059, 0.668, 0.941, 0.65 | 0.35 | A | 0.029, 0.028 |
| 22 | 0.0059, 0.658, 0.942, 0.65 | 0.0058, 0.658, 0.939, 0.65 | 0.35 | A | 0.029, 0.028 |
| 23 | 0.0058, 0.661, 0.939, 0.65 | 0.0058, 0.660, 0.940, 0.65 | 0.35 | A | 0.030, 0.030 |
| 24 | 0.0058, 0.652, 0.940, 0.65 | 0.0059, 0.659, 0.941, 0.65 | 0.35 | A | 0.030, 0.030 |
| 25 | 0.0059, 0.658, 0.941, 0.65 | 0.0059, 0.661, 0.940, 0.65 | 0.35 | A | 0.029, 0.029 |
| 26 | 0.0059, 0.648, 0.940, 0.65 | 0.0059, 0.665, 0.941, 0.65 | 0.35 | A | 0.029, 0.029 |
| 27 | 0.0067, 0.663, 0.953, 0.60 | 0.0068, 0.674, 0.953, 0.60 | 0.40 | A | 0.033, 0.034 |
| 28 | 0.0072, 0.614, 0.958, 0.60 | 0.0071, 0.610, 0.956, 0.60 | 0.40 | A | 0.037, 0.037 |
| 29 | 0.0060, 0.599, 0.943, 0.65 | 0.0063, 0.586, 0.947, 0.65 | 0.35 | A | 0.033, 0.031 |
| 30 | 0.0061, 0.585, 0.945, 0.65 | 0.0063, 0.594, 0.946, 0.65 | 0.35 | A | 0.032, 0.031 |
| 31 | 0.0063, 0.584, 0.946, 0.65 | 0.0063, 0.617, 0.946, 0.65 | 0.35 | A | 0.032, 0.031 |
| 32 | 0.0061, 0.613, 0.945, 0.65 | 0.0062, 0.636, 0.945, 0.65 | 0.35 | A | 0.031, 0.030 |
| 33 | 0.0063, 0.616, 0.946, 0.65 | 0.0062, 0.643, 0.944, 0.65 | 0.35 | A | 0.030, 0.029 |
| 34 | 0.0060, 0.604, 0.942, 0.65 | 0.0061, 0.649, 0.943, 0.65 | 0.35 | A | 0.030, 0.030 |
| 35 | 0.0061, 0.645, 0.945, 0.65 | 0.0062, 0.641, 0.944, 0.65 | 0.35 | A | 0.030, 0.029 |
| 36 | 0.0075, 0.645, 0.960, 0.60 | 0.0071, 0.637, 0.956, 0.60 | 0.40 | A | 0.035, 0.034 |
| 37 | 0.0079, 0.638, 0.963, 0.55 | 0.0080, 0.640, 0.964, 0.55 | 0.45 | A | 0.038, 0.037 |
| 38 | 0.0101, 0.628, 0.976, 0.45 | 0.0099, 0.642, 0.975, 0.45 | 0.55 | A | 0.049, 0.049 |
| 39 | 0.0115, 0.667, 0.981, 0.35 | 0.0117, 0.662, 0.981, 0.35 | 0.65 | A | 0.055, 0.057 |
| 40 | 0.0209, 0.668, 0.993, −0.10 | 0.0201, 0.659, 0.992, −0.10 | 1.10 | A | 0.094, 0.096 |
| 41 | 0.0216, 0.685, 0.994, −0.35 | 0.0223, 0.680, 0.994, −0.35 | 1.35 | A | 0.078, 0.098 |
| 42 | 0.0179, 0.676, 0.992, −0.10 | 0.0179, 0.694, 0.992, −0.10 | 1.10 | A | 0.065, 0.063 |
| 43 | 0.0116, 0.677, 0.981, 0.30 | 0.0114, 0.692, 0.981, 0.30 | 0.70 | A | 0.029, 0.041 |
| 44 | 0.0110, 0.691, 0.980, 0.35 | 0.0105, 0.690, 0.978, 0.35 | 0.65 | A | 0.029, 0.044 |
| 45 | 0.0101, 0.690, 0.977, 0.40 | 0.0097, 0.690, 0.975, 0.40 | 0.60 | A | 0.048, 0.042 |
| 46 | 0.0092, 0.679, 0.972, 0.45 | 0.0089, 0.684, 0.971, 0.45 | 0.55 | A | 0.049, 0.042 |
| 47 | 0.0083, 0.668, 0.967, 0.50 | 0.0080, 0.679, 0.965, 0.50 | 0.50 | A | 0.050, 0.039 |
| 48 | 0.0073, 0.668, 0.959, 0.55 | 0.0073, 0.681, 0.959, 0.55 | 0.45 | A | 0.049, 0.034 |
| 49 | 0.0067, 0.653, 0.953, 0.60 | 0.0064, 0.675, 0.949, 0.60 | 0.40 | A | 0.035, 0.025 |
| 50 | 0.0065, 0.664, 0.950, 0.60 | 0.0064, 0.675, 0.949, 0.60 | 0.40 | A | 0.040, 0.028 |
| 51 | 0.0065, 0.665, 0.950, 0.60 | 0.0064, 0.671, 0.949, 0.60 | 0.40 | A | 0.034, 0.027 |
| 52 | 0.0111, 0.684, 0.978, 0.39 | 0.0107, 0.655, 0.976, 0.40 | 0.60 | B | 0.0052, 0.0021 |
| 53 | 0.0191, 0.640, 0.992, −0.15 | 0.0199, 0.656, 0.993, −0.15 | 1.15 | B | 0.0035, 0.0018 |
| 54 | 0.0168, 0.641, 0.990, 0.00 | 0.0172, 0.655, 0.990, 0.00 | 1.00 | B | 0.0029, 0.0019 |
| 55 | 0.0176, 0.648, 0.991, 0.00 | 0.0178, 0.662, 0.991, 0.00 | 1.00 | B | 0.0031, 0.0028 |
| 56 | 0.0178, 0.677, 0.991, 0.00 | 0.0181, 0.660, 0.991, 0.00 | 1.00 | B | 0.0029, 0.0025 |
| 57 | 0.0221, 0.644, 0.994, −0.25 | 0.0232, 0.671, 0.994, −0.25 | 1.25 | B | 0.0049, 0.0055 |
| 58 | 0.0267, 0.689, 0.996, −0.35 | 0.0243, 0.668, 0.995, −0.35 | 1.35 | B | 0.0064, 0.0056 |
| 59 | 0.0213, 0.683, 0.994, −0.15 | 0.0212, 0.682, 0.993, −0.15 | 1.15 | B | 0.0060, 0.041 |

"Left" is the fraction of the original's action kept along the leading left direction; the scale is one minus it;
"A" and "B" are the two shared leading directions (cosine 0.18 between them); row norms are the largest relative
row change of the attention output and the down projection.

Against the six other 31B copies measured on this original weight file (shards `eeef8791` and `01891222`), no
changed matrix has an equal measurement in any field but one, a largest absolute difference shared with one of
TrevorJS's matrices, a single bfloat16 value coinciding. Against round 16's aifeifei798 copy, the census's other
edit with more than one direction per matrix (two or three on E2B, first eight at 0.997), this one has eight with
the first eight at 0.94 to 0.996, and its scale schedule is in the card where that copy's was not.

## Token and configuration side (Stage 1)

The cluster's card read "consistent" and the home judgement keeps it: every small file of the copy equals Google's
at the pin byte for byte, the configuration, the tokenizer, the special tokens, the generation settings and the
template included, and the fixed conversation renders identically. The maker edited the shards in place and
uploaded the rest of the repository as it stood.

## For the recipe library

Consistent with the card on both sides, and the card is the most complete in the census for a subspace method: layer
range, direction count, per-layer scale and component list all read back from the weights. A recipe entry for a
rank-k subspace projection would take the first-k energy share (here eight at 0.94 or more), the kept fraction along
the leading direction as the scale, and the row-norm band split by block. The saved direction vectors are not
committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/nautilus18/measurements/pair-4/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
