# Reading of the Stage 1 and Stage 2 result, second measurement: Felldude/gemma-4-E4B-uncensored against google/gemma-4-E4B-it (2026-11-02)

Measured on Wheat, round 35 piece 1 (download job 387143, compare job 387144, sweep 387152; the pull carries the
measurements and the sweep record and no job log). Modified revision `8ebbb694` (three commits on 2026-06-22
between 17:04Z and 17:12Z: the weights and the README), the same single weight file (`17cfe3d2`) round 29 measured
against the pretrained base google/gemma-4-E4B that the card's `base_model` field names (finding 62). This pass
pins the instruct model at `fee6332c` (06-03), the revision current when the repository was created, because round
29's byte-range reads placed the copy's norms and scalars on the instruct model byte for byte. The card is the same
499 bytes: "largely uncensored and is suitable for NSFW image captioning", no method, no layer, no component. This
is the reading of record for the copy; the round 29 report
(`results/weights/Felldude-gemma-4-E4B-uncensored.json`) stays as the record of what the field's pin measures.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection-selected`, 304 flags (187
unexpected changes, 58 first shares, 58 direction cosines, one cross-kind), on the cluster and after re-scoring at
home. On reading, the edit is a small training pass over two bands of layers, with no direction and nothing touched
outside the language stack.

- 245 of 2,076 tensors changed, all in the language model: the attention outputs, queries, gates, ups and down
  projections of layers 0 to 14 and 27 to 41, the keys and values of layers 0 to 13 (the layers above 23 share
  theirs), 31 per-layer input gates, 28 per-layer projections and 13 post-per-layer-input norms. The relative
  change is 0.0011 to 0.0069 on the matrices (median 0.003) and 0.099 on layer 0's per-layer input gate. The
  largest change outside the changed set is 0.00099, the threshold: 17 more language tensors sit between 0.0005
  and 0.001, and 169 of the unchanged tensors differ from the original by a nonzero amount under it.
- Layers 15 to 26 are untouched to the fourth decimal: every matrix of those twelve layers differs by 0.0001 or
  less (layer 20's attention output by 0.00003, the number round 29's range read found), and the two towers'
  1,409 tensors, the embeddings and the final norm are equal to the original byte for byte (1,662 tensors at
  exactly 0).
- No direction. The first share is 0.001 to 0.016 on every matrix (the singular values of each difference are
  flat: 0.0151, 0.0151, 0.0149 on the first), the two writers of a layer agree at 0.02 to 0.40 and the kept
  fractions are 0.97 to 1.00 on both sides: the signature of training at a low rate, as in finding 61's
  fine-tune, at a tenth of its size.

| Layer | Attention output | Down projection | Gate | Query | Per-layer input gate |
| --- | --- | --- | --- | --- | --- |
| 0 | 0.0031 | 0.0047 | 0.0033 | 0.0034 | 0.0994 |
| 5 | 0.0046 | 0.0056 | 0.0038 | 0.0039 | 0.0085 |
| 10 | 0.0021 | 0.0045 | 0.0032 | 0.0031 | 0.0056 |
| 14 | 0.0006 | 0.0010 | 0.0010 | 0.0019 | 0.0014 |
| 15 | 0.0001 | 0.0001 | 0.0001 | 0.0001 | 0.0002 |
| 20 | 0.00003 | 0.0001 | 0.00004 | 0.00004 | 0.0001 |
| 26 | 0.0001 | 0.0001 | 0.0001 | 0.0001 | 0.0001 |
| 27 | 0.0007 | 0.0019 | 0.0019 | 0.0020 | 0.0027 |
| 30 | 0.0021 | 0.0040 | 0.0036 | 0.0038 | 0.0058 |
| 35 | 0.0057 | 0.0064 | 0.0039 | 0.0056 | 0.0054 |
| 41 | 0.0046 | 0.0058 | 0.0038 | 0.0056 | 0.0127 |

Relative change by layer; the full table (245 rows) is in the report.

Against round 29. The field's pin read 595 tensors changed at a median of 0.42 (the whole base-to-instruct
training), 680 flags, kept fractions 0.5 to 4.5 and the towers equal; this pin reads 245 at a median of 0.003,
304 flags, kept fractions within 0.03 of 1 and the same towers equal. The round 29 range reads predicted the
numbers this pass measured: layer 0's attention output at 0.0031, layer 30's gate at 0.0036 and up at 0.0032,
layer 41's down projection at 0.0058, all within 0.0001. The saved direction vectors of the two passes share
nothing (median cosine 0.009 on the 58 matrices both record), as they should: the first pass's leading
directions were the instruct training's.

## Token and configuration side (Stage 1)

"Consistent" on the cluster and at home: no compared field differs from google/gemma-4-E4B-it at `fee6332c`,
and the fixed conversation renders identically. Round 29's "unexplained differences" (the generation
configuration's end ids and a 17,336-byte template the base does not ship) were the instruct model's files read
against the base.

## For the recipe library

The copy is training on two bands of layers, a light fine-tune of the instruct model under a card that names the
pretrained base; no ablation entry applies. The pinner's `card_parent` rule reads a README's first sentence and
would not have caught this card, which names no parent in prose; the byte-range read did. The direction vectors
stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat35/measurements/pair-1/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
