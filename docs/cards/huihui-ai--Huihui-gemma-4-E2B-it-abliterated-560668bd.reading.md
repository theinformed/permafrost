# Reading of the Stage 1 and Stage 2 result: huihui-ai/Huihui-gemma-4-E2B-it-abliterated against google/gemma-4-E2B-it (2026-10-31)

Measured on Blueback, round 13 piece 2 (push card 5404, download job 3400579, compare job 3400581; pulled home by
card 5530). Modified revision `3d1e3d50` (the repository was created on 2026-04-08 at 11:16Z and the weights
uploaded at 16:08Z), original pinned at `4742fe84` (2026-04-02, the release commit). The card says the copy was made
with the maker's remove-refusals script, that both thinking modes were abliterated, and that "the first 10 layers
have not been abliterated, which may result in some refusals".

## Weights (Stage 2)

The tool's assessment was "recipe match", recipe `single-projection-selected`, 0 flags, on the cluster and after
re-scoring at home.

- 50 of 2,011 tensors changed: the attention output and the down projection of layers 10 to 34, exactly the layers
  the card leaves in. Layers 0 to 9 equal the original, the largest relative change outside the changed set is
  exactly 0, and 1,961 tensors are unchanged.
- One shared direction: cross-layer cosine 1.000 on all 50 matrices and 0.99999 between the two kinds. First-value
  share 0.995 to 0.997, relative change 0.025 to 0.028.
- The kept fraction along the leading left direction is −0.005 to −0.003 on all 50, a weight of 1.00; the right is
  0.19 to 0.85 and the left is below the right on 50 of 50, an output-side edit.
- Row norms moved by 0.006 to 0.026, the leftover of a plain projection with no restoration step, as on the maker's
  other copies.

| Layer | Attention output: change, E1, E8, left kept, right kept | Down projection: change, E1, E8, left kept, right kept | Weight read | Cross-layer cosine | Row norms |
| --- | --- | --- | --- | --- | --- |
| 10 | 0.0257, 0.996, 0.996, 0.00, 0.62 | 0.0265, 0.996, 0.997, 0.00, 0.68 | 1.00/1.00 | 1.00/1.00 | 0.0164, 0.0133 |
| 11 | 0.0275, 0.997, 0.997, 0.00, 0.74 | 0.0257, 0.996, 0.997, 0.00, 0.62 | 1.00/1.00 | 1.00/1.00 | 0.0202, 0.0111 |
| 12 | 0.0256, 0.996, 0.996, 0.00, 0.72 | 0.0257, 0.996, 0.996, 0.00, 0.61 | 1.00/1.00 | 1.00/1.00 | 0.0133, 0.0126 |
| 13 | 0.0253, 0.996, 0.997, 0.00, 0.73 | 0.0250, 0.996, 0.996, 0.00, 0.71 | 1.00/1.00 | 1.00/1.00 | 0.0110, 0.0063 |
| 14 | 0.0264, 0.996, 0.997, 0.00, 0.46 | 0.0256, 0.996, 0.996, 0.00, 0.36 | 1.00/1.00 | 1.00/1.00 | 0.0097, 0.0080 |
| 15 | 0.0262, 0.996, 0.997, 0.00, 0.60 | 0.0280, 0.997, 0.997, 0.00, 0.62 | 1.00/1.00 | 1.00/1.00 | 0.0148, 0.0173 |
| 16 | 0.0280, 0.997, 0.997, 0.00, 0.64 | 0.0281, 0.997, 0.997, 0.00, 0.40 | 1.00/1.00 | 1.00/1.00 | 0.0212, 0.0160 |
| 17 | 0.0255, 0.996, 0.996, 0.00, 0.56 | 0.0281, 0.997, 0.997, 0.00, 0.33 | 1.00/1.00 | 1.00/1.00 | 0.0085, 0.0088 |
| 18 | 0.0249, 0.996, 0.996, 0.00, 0.66 | 0.0267, 0.997, 0.997, 0.00, 0.40 | 1.00/1.00 | 1.00/1.00 | 0.0099, 0.0067 |
| 19 | 0.0256, 0.996, 0.996, 0.00, 0.59 | 0.0256, 0.996, 0.996, 0.00, 0.31 | 1.00/1.00 | 1.00/1.00 | 0.0133, 0.0065 |
| 20 | 0.0254, 0.996, 0.996, 0.00, 0.61 | 0.0256, 0.996, 0.996, 0.00, 0.30 | 1.00/1.00 | 1.00/1.00 | 0.0091, 0.0085 |
| 21 | 0.0249, 0.996, 0.996, 0.00, 0.73 | 0.0254, 0.996, 0.996, 0.00, 0.29 | 1.00/1.00 | 1.00/1.00 | 0.0136, 0.0096 |
| 22 | 0.0246, 0.996, 0.996, 0.00, 0.65 | 0.0254, 0.996, 0.996, 0.00, 0.29 | 1.00/1.00 | 1.00/1.00 | 0.0102, 0.0073 |
| 23 | 0.0231, 0.995, 0.996, 0.00, 0.68 | 0.0251, 0.996, 0.996, 0.00, 0.28 | 1.00/1.00 | 1.00/1.00 | 0.0159, 0.0066 |
| 24 | 0.0246, 0.996, 0.996, 0.00, 0.58 | 0.0256, 0.996, 0.996, 0.00, 0.27 | 1.00/1.00 | 1.00/1.00 | 0.0097, 0.0077 |
| 25 | 0.0252, 0.996, 0.996, 0.00, 0.64 | 0.0255, 0.996, 0.996, 0.00, 0.19 | 1.00/1.00 | 1.00/1.00 | 0.0112, 0.0091 |
| 26 | 0.0259, 0.996, 0.997, 0.00, 0.82 | 0.0254, 0.996, 0.996, 0.00, 0.21 | 1.00/1.00 | 1.00/1.00 | 0.0111, 0.0084 |
| 27 | 0.0248, 0.996, 0.996, 0.00, 0.74 | 0.0258, 0.996, 0.996, 0.00, 0.27 | 1.00/1.00 | 1.00/1.00 | 0.0059, 0.0092 |
| 28 | 0.0262, 0.996, 0.997, 0.00, 0.72 | 0.0259, 0.996, 0.997, 0.00, 0.20 | 1.00/1.00 | 1.00/1.00 | 0.0098, 0.0113 |
| 29 | 0.0259, 0.996, 0.997, 0.00, 0.75 | 0.0252, 0.996, 0.996, 0.00, 0.20 | 1.00/1.00 | 1.00/1.00 | 0.0086, 0.0104 |
| 30 | 0.0269, 0.997, 0.997, 0.00, 0.85 | 0.0253, 0.996, 0.996, 0.00, 0.20 | 1.00/1.00 | 1.00/1.00 | 0.0189, 0.0095 |
| 31 | 0.0254, 0.996, 0.997, 0.00, 0.68 | 0.0256, 0.996, 0.996, 0.00, 0.23 | 1.00/1.00 | 1.00/1.00 | 0.0104, 0.0112 |
| 32 | 0.0260, 0.996, 0.997, 0.00, 0.76 | 0.0254, 0.996, 0.996, 0.00, 0.24 | 1.00/1.00 | 1.00/1.00 | 0.0115, 0.0110 |
| 33 | 0.0249, 0.996, 0.996, 0.00, 0.60 | 0.0255, 0.996, 0.996, 0.00, 0.24 | 1.00/1.00 | 1.00/1.00 | 0.0075, 0.0113 |
| 34 | 0.0261, 0.996, 0.997, 0.00, 0.47 | 0.0258, 0.996, 0.997, 0.00, 0.30 | 1.00/1.00 | 1.00/1.00 | 0.0259, 0.0212 |

The fingerprint settles round 18's open question. prithivMLmods/gemma-4-E2B-it-Uncensored-MAX, measured on this
same original file in round 18, equals this copy in every field of all 2,011 tensors and in every singular value;
the two modified shards differ in checksum (`90daa0b2` here) because the repositories were saved separately, and
the weights they carry are the same edit. The prithivMLmods card names this copy as its source, and the weights
agree.

## Token and configuration side (Stage 1)

"Consistent" on the cluster and at home. Every small file equals Google's pinned file except the template, which
is Google's release template with carriage-return line endings (12,188 bytes, `ec192bdb`), and the fixed
conversation renders identically.

## For the recipe library

Consistent with the card: the one shared direction at weight 1.00 on both writers of layers 10 to 34, output side,
with rows left unrestored. The layer set is the card's, and the maker's statement about the first ten layers is
exactly what the weights show. The saved direction vectors are not committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/blueback13/measurements/pair-2/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
