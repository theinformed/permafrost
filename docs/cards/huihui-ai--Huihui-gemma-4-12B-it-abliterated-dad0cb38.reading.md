# Reading of the Stage 1 and Stage 2 result: huihui-ai/Huihui-gemma-4-12B-it-abliterated against google/gemma-4-12B-it (2026-10-31)

Measured on Blueback, round 13 piece 4 (push card 5404, download job 3400579, compare job 3400583; pulled home by
card 5530). Modified revision `060ea173` (the repository's history is a single squash of 2026-06-07 at 08:48Z),
original pinned at `5926caa4` (2026-06-04). The card says "Only layers 23-28" were abliterated, and that the
earliest released google/gemma-4-12B-it weights had issues, so the copy was re-ablated and re-uploaded.

## Weights (Stage 2)

The tool's assessment was "recipe match", recipe `directional-per-layer-selected`, 0 flags, on the cluster and after
re-scoring at home.

- 12 of 677 tensors changed: the attention output and the down projection of layers 23 to 28, the card's six
  layers. Nothing else moved; the largest relative change outside the changed set is exactly 0 and 665 tensors
  equal the original.
- One direction per matrix (first-value share 0.994 to 0.998), shared by layers 24 to 27 at cosine 1.000 and taken
  up at 0.47 and 0.74 on the end layers 23 and 28; the two writers of each layer agree at 1.000.
- The left kept fraction is −0.003 to 0.005, a weight of 1.00; the right is 0.63 to 0.89 and the left is below the
  right on 12 of 12, an output-side edit.
- Row norms moved by 0.016 to 0.079, the unrestored leftover of a plain projection.

| Layer | Attention output: change, E1, E8, left kept, right kept | Down projection: change, E1, E8, left kept, right kept | Weight read | Cross-layer cosine | Row norms |
| --- | --- | --- | --- | --- | --- |
| 23 | 0.0183, 0.995, 0.996, 0.01, 0.89 | 0.0187, 0.995, 0.995, 0.00, 0.64 | 0.99/1.00 | 0.47/0.47 | 0.0268, 0.0162 |
| 24 | 0.0231, 0.996, 0.997, 0.00, 0.84 | 0.0258, 0.997, 0.997, 0.00, 0.84 | 1.00/1.00 | 1.00/1.00 | 0.0776, 0.0774 |
| 25 | 0.0220, 0.996, 0.997, 0.00, 0.82 | 0.0264, 0.997, 0.997, 0.00, 0.82 | 1.00/1.00 | 1.00/1.00 | 0.0775, 0.0788 |
| 26 | 0.0309, 0.998, 0.998, 0.00, 0.85 | 0.0249, 0.996, 0.997, 0.00, 0.76 | 1.00/1.00 | 1.00/1.00 | 0.0782, 0.0599 |
| 27 | 0.0184, 0.994, 0.995, 0.00, 0.80 | 0.0208, 0.995, 0.995, 0.00, 0.73 | 1.00/1.00 | 1.00/1.00 | 0.0508, 0.0520 |
| 28 | 0.0183, 0.994, 0.994, 0.00, 0.83 | 0.0182, 0.994, 0.994, 0.00, 0.63 | 1.00/1.00 | 0.74/0.74 | 0.0395, 0.0335 |

TimelessSoul/Huihui-gemma-4-12B-it-abliterated (round 14 pair 8) is this file: the modified shards share one
checksum (`2dd13d86`) and every measured field is equal. No changed matrix has an equal measurement in any field of
the other 12B copies, and this copy's leading vectors lie 0.56 to 0.79 inside the four-dimensional subspace AEON-7's
copy removes.

## Token and configuration side (Stage 1)

"Unexplained differences" on one field on the cluster and at home: `text_config.max_position_embeddings` is 262,144
at the pin and 131,072 in the copy. The copy's configuration (`e75e44bd`) is byte for byte Google's file at
`66bc78a7` (2026-06-03); Google raised the value in `5926caa4` on 06-04 and the pin rule chose that revision because
the copy's visible history begins on 06-07. The copy carries the earlier original's configuration, the
earlier-revision case. The template equals Google's pinned file byte for byte and the fixed conversation renders
identically.

## For the recipe library

Consistent with the card: six layers, both writers, one direction at weight 1.00, output side, rows unrestored. This
is the first 12B copy to match a recipe with no flag. The saved direction vectors are not committed; the pull copy
is `/opt/ai/hpc-packages/pulls/model-audit/blueback13/measurements/pair-4/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
