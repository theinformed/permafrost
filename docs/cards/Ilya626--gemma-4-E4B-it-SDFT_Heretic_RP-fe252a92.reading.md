# Reading of the Stage 1 and Stage 2 result: Ilya626/gemma-4-E4B-it-SDFT_Heretic_RP against google/gemma-4-E4B-it (2026-11-02)

Measured on Wheat, round 31 batch 3 piece 2 (download job 387097, compare job 387099, sweep 387102; the pull of
11-02 00:22Z carries the measurements and the sweep record and no job log). Modified revision `c07b5f9b` (five
commits on 2026-04-25: the weights at 13:06Z as "Upload Heretic RP merged multimodal HF weights", then three README
edits), original pinned at `83df0a88` (04-10). The card says the repository holds merged weights, not an adapter,
"based on the uncensored Heretic SDFT line, then further tuned for roleplay behavior", built from google/gemma-4-E4B-it;
it describes the roleplay evaluation and names no layer, no component and no method for the uncensoring beyond the
word Heretic. The `base_model` field names Google.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection`, 611 flags (442 unexpected
changes, 84 first shares, 84 direction cosines, one cross-kind), on the cluster and after re-scoring at home. On
reading, the language stack carries a small full fine-tune and no projection, and both towers' linear maps are
freshly initialised matrices.

- 526 of 2,130 tensors changed. In the language stack, 294 of 719: all seven projections of all 42 layers at
  relative changes of 0.0016 to 0.0056 (median 0.0030), full rank (first shares 0.009 to 0.28, fourth cumulative
  shares 0.03 to 0.33), no direction shared across layers, kept fractions 0.99 to 1.02 on both sides of every
  matrix. The embedding, the per-layer embeddings, every normalisation vector and every scalar are unchanged. The
  largest relative change outside the changed set is 0.0000011, the float16 save rounding the smallest values of
  untouched tensors, the case of finding 51's jokernifty copy.
- In the audio tower, 120 of 752: the ten linear maps of each of the 12 conformer layers (the query, key, value
  and output projections, the four feed-forward matrices, the two convolution-module linears) at relative changes
  of 1.19 to 1.71. In the vision tower, 112 of 659: the seven linear maps of each of the 16 encoder layers at 1.14
  to 1.50. The normalisations, the per-dimension scales, the depthwise convolutions, the relative-key projections,
  the quantisation ranges (`input_max`, `input_min` and the output pair on every linear), the subsampling
  convolutions, the output projection and both embedding projections are unchanged.
- The 232 tower matrices carry nothing of the originals. Their leading directions carry 0.5 to 21 percent of the
  change, their kept fractions are -0.11 to 0.00, and three read from the hub by byte range (`tools/hub_range_read.py`)
  have cosine 0.0001 and 0.0004 with Google's: mean within 0.00003 of zero, standard deviation 0.02003 and 0.01999,
  no exact zeros, 64 distinct values in every block of 64, kurtosis 3.000 and 2.9999, and row norms of 0.59 to 0.69
  on 1,024 and 4,096 rows alike. That is a Gaussian draw at the library's default initialiser scale of 0.02. Google's
  own tensors on the same names have 36 to 43 percent exact zeros and four distinct values per block of 64. The
  subsampling input projection, read the same way, equals Google's to the bit.
- No Heretic kernel is in the weights: the attention outputs keep 0.991 to 1.012 along their leading output
  direction and no down projection carries more than 0.28 of its change in one direction. The "Heretic SDFT" the
  card stands on is either a trained model with no projection in it or a projected model whose projection the
  training undid; nothing here says which.
- Rows moved 0.004 to 0.23 in the language stack and 0.42 to 3.9 in the towers.

| Group | Tensors | Changed | Relative change | First share | Left kept |
| --- | --- | --- | --- | --- | --- |
| Language projections | 294 | 294 | 0.0016 to 0.0056 | 0.009 to 0.28 | 0.99 to 1.02 |
| Language vectors and embeddings | 425 | 0 | 0 to 0.0000011 | | |
| Audio conformer linears | 120 | 120 | 1.19 to 1.71 | 0.005 to 0.21 | -0.11 to 0.00 |
| Audio other | 632 | 0 | 0 | | |
| Vision encoder linears | 112 | 112 | 1.14 to 1.50 | 0.005 to 0.21 | -0.08 to 0.00 |
| Vision other | 547 | 0 | 0 | | |

The full table (526 rows) is in the report. The copy is saved in float16 (every tensor `torch.float16` against the
original's bfloat16) in four shards of its own.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster (six fields) and at home (five). `text_config.moe_intermediate_size`
closes by the default rule. What stays: four `dtype` fields that read float16 where the original reads bfloat16,
the save's doing and a true difference in what a loader gets; and the template, an 11,926-byte file against the
pin's 16,317 bytes. The exact diff is Google's own change of 04-10 (the tool-call parameter formatting), so the
copy carries the E4B template of the 04-02 revision under a pin of 04-10, the earlier-revision case of lessans's
and TrevorJS's copies, closed by hand. The fixed conversation renders identically under both. The tokenizer
configuration was re-saved (`8cadfd27` against `90c3a3ba`) with no field moved.

## For the recipe library

Nothing from the language stack: a small fine-tune, as the card says. The towers are the finding (63): a copy whose
vision and audio inputs pass through 232 random matrices while every normalisation and quantisation range around
them is Google's, with a card that says "multimodal" and nothing of the towers. The scorer could name this, since a
relative change above 1 with a kept fraction at 0 on a whole module is a replacement. The direction vectors stay in
the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat31/measurements/pair-2/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
