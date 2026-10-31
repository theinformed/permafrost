# Reading of the Stage 1 and Stage 2 result: TimelessSoul/Huihui-gemma-4-12B-it-abliterated against google/gemma-4-12B-it (2026-10-31)

Measured on Blueback, round 14 piece 8 (push card 5421, download job 3401154, compare job 3401162; pulled home by
card 5533). Modified revision `b4e4d248` (one commit, 2026-10-07 at 03:21Z, "Duplicate from
huihui-ai/Huihui-gemma-4-12B-it-abliterated"; the README is huihui-ai's), original pinned at `707f0a3b`
(2026-07-20). The card is the source's: "Only layers 23-28" abliterated.

## Weights (Stage 2)

The tool's assessment was "recipe match", recipe `directional-per-layer-selected`, 0 flags, on the cluster and after
re-scoring at home. The modified shards share their checksum (`2dd13d86`) with huihui-ai's copy measured in round
13 pair 4, and every measured field is equal: 12 of 677 tensors changed, the attention output and the down
projection of layers 23 to 28, one direction shared at cosine 1.000 on layers 24 to 27, weight 1.00 on the output
side (left kept −0.003 to 0.005, right 0.63 to 0.89), rows moved 0.016 to 0.079, 665 tensors equal to the original.
The weights are the source's weights, uploaded again under another name; the reading is in
`huihui-ai--Huihui-gemma-4-12B-it-abliterated-dad0cb38.reading.md`.

| Layer | Attention output: change, E1, E8, left kept, right kept | Down projection: change, E1, E8, left kept, right kept | Weight read | Cross-layer cosine | Row norms |
| --- | --- | --- | --- | --- | --- |
| 23 | 0.0183, 0.995, 0.996, 0.01, 0.89 | 0.0187, 0.995, 0.995, 0.00, 0.64 | 0.99/1.00 | 0.47/0.47 | 0.0268, 0.0162 |
| 24 | 0.0231, 0.996, 0.997, 0.00, 0.84 | 0.0258, 0.997, 0.997, 0.00, 0.84 | 1.00/1.00 | 1.00/1.00 | 0.0776, 0.0774 |
| 25 | 0.0220, 0.996, 0.997, 0.00, 0.82 | 0.0264, 0.997, 0.997, 0.00, 0.82 | 1.00/1.00 | 1.00/1.00 | 0.0775, 0.0788 |
| 26 | 0.0309, 0.998, 0.998, 0.00, 0.85 | 0.0249, 0.996, 0.997, 0.00, 0.76 | 1.00/1.00 | 1.00/1.00 | 0.0782, 0.0599 |
| 27 | 0.0184, 0.994, 0.995, 0.00, 0.80 | 0.0208, 0.995, 0.995, 0.00, 0.73 | 1.00/1.00 | 1.00/1.00 | 0.0508, 0.0520 |
| 28 | 0.0183, 0.994, 0.994, 0.00, 0.83 | 0.0182, 0.994, 0.994, 0.00, 0.63 | 1.00/1.00 | 0.74/0.74 | 0.0395, 0.0335 |

## Token and configuration side (Stage 1)

"Unexplained differences" on two fields, both the pin's doing. The copy was created on 2026-10-07, so the pin rule
chose Google's `707f0a3b` of 2026-07-20, where the source's pin was `5926caa4` of 06-04; the copy's small files
are the source's, which are Google's of 06-03. So `text_config.max_position_embeddings` reads 262,144 against the
copy's 131,072, and the template reads as Google's 17,466-byte file of 06-03 (`36e3a42e`) against the pin's
18,683-byte "Canonical" template of 07-09. Both are the earlier-revision case; the fixed conversation renders
identically under both templates.

## For the recipe library

Nothing new: a byte-identical re-upload of huihui-ai's 12B copy, the second such pair in the census after
prithivMLmods's E2B copy of the same maker's edit (finding 9). The pinner should pair a repository whose one commit
says "Duplicate from" with that source, where the weights will compare equal, before it pairs it with the stated
original.

Weight differences alone cannot certify the absence of hidden behavior.
