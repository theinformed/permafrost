# Reading of the Stage 1 and Stage 2 result: MeFFyLe/gemma-4-12B-it-uncensored-heretic against google/gemma-4-12B-it (2026-10-31)

Measured on Nautilus, round 19 piece 7 (push card 5605, probe card 5616, round card 5626, download job 4142666, compare job 4142673 on the background queue, sweep 4142675; pulled home by card 5647). Modified revision `0a5e69dd` (one commit, 2026-09-12 at 18:03Z, "Duplicate
from llmfan46/gemma-4-12B-it-uncensored-heretic"; the README is llmfan46's, 36,152 bytes, byte for byte),
original pinned at `707f0a3b` (2026-07-20). The card is the source's: Heretic 1.2.0 with arbitrary-rank ablation
on `o_proj` only, start layer 24, end layer 40, 6 refusals in 100, KL 0.1203. The `base_model` field names Google.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 15 flags, on the
cluster and after re-scoring at home, the energy shares llmfan46's report carries (0.914 to 0.983 on 15 of 16
matrices). The weight file is llmfan46's: one `model.safetensors` of 23,919,549,408 bytes under the same LFS
checksum (`4e6ac81d39`) in both repositories, the same shard checksum in the comparison, and every measured field
of all 677 tensors equal to the round 13 report
(`results/weights/llmfan46-gemma-4-12B-it-uncensored-heretic.json`): 16 changed, the attention outputs of layers
24 to 39, input side (left kept 0.76 to 1.00, right −2.63 to 0.68, left above right on 16 of 16), searched
weights 0.32 (layer 37) to 3.63 (layer 35), rows moved 0.0014 to 0.083, 661 tensors equal to the original. The
reading is in `llmfan46--gemma-4-12B-it-uncensored-heretic-*.reading.md`.

| Layer | Attention output: change, E1, E8, left kept, right kept | Weight read | Within-layer cosine | Cross-layer cosine | Row norms |
| --- | --- | --- | --- | --- | --- |
| 24 | 0.0319, 0.961, 0.978, 0.84, -0.80 | 1.80 | - | 0.23 | 0.0035 |
| 25 | 0.0312, 0.960, 0.976, 0.90, -0.66 | 1.66 | - | 0.19 | 0.0022 |
| 26 | 0.0331, 0.965, 0.977, 0.77, -0.89 | 1.89 | - | 0.34 | 0.0041 |
| 27 | 0.0310, 0.914, 0.974, 0.90, -0.75 | 1.75 | - | 0.26 | 0.0070 |
| 28 | 0.0336, 0.963, 0.980, 0.76, -0.79 | 1.79 | - | 0.41 | 0.0061 |
| 29 | 0.0144, 0.943, 0.957, 0.95, -0.26 | 1.26 | - | 0.32 | 0.0023 |
| 30 | 0.0234, 0.970, 0.982, 0.90, -0.46 | 1.46 | - | 0.19 | 0.0032 |
| 31 | 0.0304, 0.959, 0.978, 0.92, -0.72 | 1.72 | - | 0.16 | 0.0030 |
| 32 | 0.0456, 0.948, 0.985, 0.91, -1.12 | 2.12 | - | 0.39 | 0.0133 |
| 33 | 0.0648, 0.980, 0.991, 0.87, -1.44 | 2.44 | - | 0.36 | 0.0337 |
| 34 | 0.0414, 0.958, 0.986, 0.90, -1.04 | 2.04 | - | 0.22 | 0.0366 |
| 35 | 0.0703, 0.983, 0.995, 0.93, -2.63 | 3.63 | - | 0.33 | 0.0826 |
| 36 | 0.0244, 0.993, 0.997, 1.00, -1.64 | 2.64 | - | 0.09 | 0.0043 |
| 37 | 0.0329, 0.966, 0.988, 1.00, 0.68 | 0.32 | - | 0.13 | 0.0254 |
| 38 | 0.0353, 0.983, 0.990, 0.85, -1.08 | 2.08 | - | 0.29 | 0.0062 |
| 39 | 0.0153, 0.971, 0.987, 0.99, -0.63 | 1.63 | - | 0.36 | 0.0014 |

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster on seven fields, five at home: the six configuration fields every 12B
copy saved under transformers 5.10 or later reads against Google's file (here 5.10.0.dev0 to 5.10.2; the two data
types close at home, the four omitted defaults stay under 5.6.2 and close under 5.12.0) and the template. The
template is llmfan46's patched file (21,488 bytes, `16e455bc`), Google's
template plus the maker's `format_type_argument` macro and two guards (finding 19), carried through the duplicate
under a pin whose template is the 18,681-byte "Canonical" file of 07-09; the parent was read against the
17,466-byte file of 06-03 and the patch reads the same either way. The fixed conversation renders identically.

## For the recipe library

Nothing new on the weights: a byte-identical re-upload of llmfan46's 12B copy through the hub's duplicate
function, the fourth re-upload of this round. The maker's patched template is now in a fifth repository, one the
maker does not own.
