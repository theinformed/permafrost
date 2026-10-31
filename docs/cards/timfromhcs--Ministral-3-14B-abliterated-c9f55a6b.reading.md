# Reading of the Stage 1 and Stage 2 result: timfromhcs/Ministral-3-14B-abliterated against mistralai/Ministral-3-14B-Instruct-2512 (2026-10-31)

Measured on Blueback, round 14 piece 5 (push card 5421, download job 3401154, compare job 3401159; pulled home by
card 5533). Modified revision `9cc8b306` (one commit, 2026-10-07 at 07:45Z, "Duplicate from
jenerallee78/Ministral-3-14B-abliterated"; that source repository was created on 2025-12-05 and its usage text
names it), original pinned at `29439f81` (2026-07-15). The card says grimjim's llm-abliteration, norm-preserving
biprojected abliteration, and gives no layers or scale.

## Weights (Stage 2)

The measurement is not a reading of the edit. The original is published in float8 (`float8_e4m3fn` with a
`quantization_config`, 560 tensors of `weight_scale_inv` and `activation_scale` that exist on the original side
only) and the copy in bfloat16; the comparison measured the raw eight-bit codes against bfloat16 values. It reads
280 of 585 matrices changed at relative change 0.999, first-value shares of 0.001 to 0.2, 921 flags and
"recipe violations", the same numbers on the cluster and after re-scoring at home. Finding 7 already named this
pair as one that needs a dequantised original; the batch pinner admitted it anyway, and the download verified the
published checksums of both sides, so the files are what the hub serves. The edit's layers, direction count,
weight and side cannot be read until the original is dequantised at home or on the cluster and the comparison run
again; the saved direction vectors of this run are the leading directions of a quantisation error and are not
used. The pull copy is `/opt/ai/hpc-packages/pulls/model-audit/blueback14/measurements/pair-5/`.

## Token and configuration side (Stage 1)

"Unexplained differences", 1,010 fields: 1,004 special tokens in a 147 KB special-tokens map the copy carries and
the original does not, the `quantization_config` and `tie_word_embeddings` fields absent from the copy, and the
template. The copy's template is 7,754 bytes (`6cc0f8c0`), byte for byte the source repository's file; the
original's was 7,760 bytes (`87e109c9`) from its first visible commit of 2025-12-02 until the pin's commit of
2026-07-15 replaced it with an 11,913-byte file ("update to match mistral-common"). The copy stands on the
2025-12 original, the earlier-revision case with a later edit to the original's template in between; the fixed
conversation renders identically under both.

## For the recipe library

Nothing enters the library from this pair. The pinner should refuse an original whose configuration carries a
`quantization_config`, or pair it only with a dequantised copy of the original, and a copy whose first commit says
"Duplicate from" should be paired with the source it names (jenerallee78's, 2025-12-05) as well as with the maker's
stated original.

Weight differences alone cannot certify the absence of hidden behavior.
