# Reading of the Stage 1 and Stage 2 result: 3MPER0RR/gemma-4-12b-it-3MPER0RR-abliterated against google/gemma-4-12B-it (2026-10-31)

Measured on Nautilus, round 18 piece 2 (push card 5473, round card 5477, download job 4125751, compare job 4125753
on the background queue, sweep 4125760; pulled home by card 5493). Modified revision `97d0cfbd` (2026-10-29, the
latest of nine README commits; the repository was created on 2026-09-01 at 09:47Z and the weights uploaded in the
same minute), original pinned at `707f0a3b` (2026-07-20, the commit that added a response template to the tokenizer
configuration). The maker's card says "Trials: [200]" and nothing else of the method, and carries a weight
comparison of its own: 677 tensors compared, 48 modified (7.09 percent), 629 unchanged, 29 layers with changes, no
structural mismatch. The same maker's Mistral 7B copy (round 7) is finding 8.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection-selected`, 5 flags, on the cluster
and after re-scoring at home: two cross-layer directions (layers 20 and 21 at 0.899 and 0.905), two energy shares
(layers 42 and 44 at 0.9897 and 0.980) and one cross-kind direction. On reading, the copy is one shared direction
projected out of a chosen set of residual writers at an irregular per-layer strength, and nothing of the dense
change that covered the maker's Mistral copy.

- 48 of 677 tensors changed: the attention outputs of layers 19 to 47 (29) and the down projections of layers 27 to
  45 (19), the counts of the card's own table to the tensor. The largest relative change outside the changed set is
  exactly 0 and 629 tensors are equal to the original, where the maker's Mistral 7B copy changed every matrix.
- One shared direction: the leading directions agree across layers at cosine 0.90 to 1.00 (median 0.98 on the
  attention outputs, 0.997 on the down projections) and the two writers of a layer agree at 0.90 to 1.00 on the 19
  layers that carry both. The edit is rank one at the storage floor: first-value share 0.980 to 0.997 on relative
  changes of 0.020 to 0.033, leftover 0.0014 to 0.0016 of the weight norm, every matrix inside the 0.0025 line.
- The strength follows no kernel. Along the shared direction the copy keeps −0.20 to 0.96 of the original's action
  on the left and 0.02 to 0.89 on the right, and the left fraction is below the right on 24 of the 48, so the
  measurement reads neither a side nor a weight: a weight of 1.04 to 1.20 on the four matrices under zero, 0.04 to
  0.99 on the rest, moving layer by layer without the rise-and-fall shape of the Heretic kernel finding 8 read on
  the Mistral copy (0.11 to 1.32 to 0.74). The 200 trials of the card are that tool's default; what it left in the
  weights is a per-layer strength the card does not state.
- Row norms moved by 0.0029 to 0.0106 relative (median 0.0057), under no preservation claim.

| Layer | Attention output: change, E1, left, right | Down projection: change, E1, left, right |
| --- | --- | --- |
| 19 | 0.020, 0.994, 0.69, 0.47 | |
| 20 | 0.033, 0.997, 0.96, 0.14 | |
| 21 | 0.033, 0.996, 0.95, 0.26 | |
| 22 | 0.026, 0.993, 0.91, 0.38 | |
| 23 | 0.022, 0.995, 0.81, 0.47 | |
| 24 | 0.021, 0.995, 0.66, 0.51 | |
| 25 | 0.020, 0.994, 0.59, 0.65 | |
| 26 | 0.026, 0.996, 0.85, 0.40 | |
| 27 | 0.023, 0.996, 0.35, 0.56 | 0.026, 0.996, 0.26, 0.39 |
| 28 | 0.023, 0.996, 0.32, 0.47 | 0.025, 0.996, 0.01, 0.24 |
| 29 | 0.023, 0.995, −0.20, 0.57 | 0.026, 0.997, −0.09, 0.32 |
| 30 | 0.021, 0.995, 0.06, 0.54 | 0.024, 0.996, 0.14, 0.27 |
| 31 | 0.022, 0.995, 0.11, 0.55 | 0.023, 0.996, 0.55, 0.19 |
| 32 | 0.029, 0.997, 0.87, 0.27 | 0.024, 0.995, 0.59, 0.17 |
| 33 | 0.025, 0.996, 0.88, 0.42 | 0.023, 0.995, 0.57, 0.08 |
| 34 | 0.024, 0.996, 0.81, 0.40 | 0.023, 0.996, 0.22, 0.05 |
| 35 | 0.022, 0.995, 0.72, 0.50 | 0.022, 0.995, −0.06, 0.03 |
| 36 | 0.022, 0.995, 0.78, 0.44 | 0.022, 0.996, −0.14, 0.02 |
| 37 | 0.020, 0.995, 0.00, 0.48 | 0.023, 0.996, 0.41, 0.18 |
| 38 | 0.026, 0.996, 0.91, 0.36 | 0.022, 0.996, 0.30, 0.02 |
| 39 | 0.022, 0.993, 0.70, 0.58 | 0.021, 0.995, −0.19, 0.12 |
| 40 | 0.022, 0.995, 0.37, 0.47 | 0.021, 0.995, −0.09, 0.15 |
| 41 | 0.021, 0.994, 0.57, 0.48 | 0.021, 0.995, −0.02, 0.14 |
| 42 | 0.022, 0.990, 0.81, 0.75 | 0.021, 0.994, 0.08, 0.24 |
| 43 | 0.020, 0.992, 0.12, 0.89 | 0.020, 0.995, 0.08, 0.21 |
| 44 | 0.027, 0.980, 0.89, 0.66 | 0.021, 0.994, 0.14, 0.15 |
| 45 | 0.021, 0.992, 0.45, 0.65 | 0.020, 0.994, −0.03, 0.16 |
| 46 | 0.020, 0.994, 0.58, 0.61 | |
| 47 | 0.025, 0.994, 0.91, 0.48 | |

Against the five other copies of this base measured on the same weight file (shard `5a84cb31`), no changed matrix
has an equal measurement in any field but two largest absolute differences shared with lemuralabs's report, single
bfloat16 values coinciding. Against the maker's Mistral 7B copy the shared direction is common to both
and the dense change under it is absent here.

## Token and configuration side (Stage 1)

The cluster's card read "unexplained differences" on nine configuration fields beside three version strings, and the
home judgement closes them as one save under a newer library.

- `transformers_version` 5.10.0.dev0 on the original, 5.16.1 on the copy, in both the configuration and the
  generation settings.
- The four class defaults of finding 11 absent (640, 640, 640, 48) and `bfloat16` repeated in the three
  sub-configurations, the 5.10 and later save form, as on this round's pair 1.
- `global_head_dim` 512 and `num_global_key_value_heads` 1 absent from the text configuration and a
  `per_layer_config` map present with those values written under the global layers' indices: the form the 5.16
  library writes for Gemma 4, the per-layer head map that finding 15 met on a loader's save, here from the library
  itself; the copy carries no `unsloth_fixed` field. The map could not be loaded at home because transformers 5.6.2
  has no class for `model_type` gemma4_unified; the values it carries are the original's.
- The template is Google's pinned one byte for byte (18,683 bytes, `ae53464b`), the tokenizer, special tokens and
  generation settings are equal, and the fixed conversation renders identically.

## For the recipe library

Consistent with the card's table on the weights, and a case for the `single-projection-selected` entry with a
strength that varies by layer: the shared direction matches the entry and the kept fractions neither read a weight
nor a side. The saved direction vectors are not committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/nautilus18/measurements/pair-2/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
