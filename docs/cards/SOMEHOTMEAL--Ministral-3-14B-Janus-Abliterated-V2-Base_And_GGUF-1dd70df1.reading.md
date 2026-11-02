# Reading of the Stage 1 and Stage 2 result: SOMEHOTMEAL/Ministral-3-14B-Janus-Abliterated-V2-Base_And_GGUF against jenerallee78/Ministral-3-14B-abliterated (2026-11-02)

Measured on Wheat, round 45 piece 3 (download job 387355, compare job 387358, sweep 387364; the pull carries the
measurements and the sweep record and no job log). Modified revision `441ab2ad` (created 2026-09-13 16:34Z, one
upload of the folder at 16:48Z with five GGUF files beside six safetensors shards), parent pinned at `0c255ddb` of
2025-12-05, jenerallee78's edit of Ministral 3 14B, whose files timfromhcs's repository carries under the hub's
duplicate function and which round 14 compared with Mistral's float8 checkpoint and could not read (finding 37).
The card is mergekit's: a `dare_linear` merge "using mistralai/Ministral-3-14B-Instruct-2512 as a base" with
jenerallee78's edit at `weight` 0.60 and `density` 0.70, `dtype: bfloat16`, `tokenizer_source: base`, and both
repositories in the `base_model` field. The pair is a second pass over a first edit the census holds only as an
unread measurement, and its base is a checkpoint published in float8.

## Weights (Stage 2)

The tool's assessment was violations against `single-projection`, 345 flags (200 unexpected changes, 80 first
shares, 64 direction cosines, 1 cross-kind cosine), on the cluster and after re-scoring at home. On reading, the
copy's language matrices are Mistral's float8 codes read as weights, with no scales, mixed by the card's recipe.

- 280 of 585 tensors changed: the query, key, value, output, gate, up and down projections of all 40 layers, at
  relative changes of 460 to 4,593 against the parent (rows 489 to 4,874, first shares 0.0006 to 0.11). The
  vision tower, the projector, the token embedding, the `lm_head` and every normalisation vector read exactly 0,
  so the largest relative change outside the changed set is exactly 0.
- By byte range on four matrices (the layer 0 query projection, the attention outputs of layers 20 and 30 and the
  layer 20 down projection), 30.07 to 30.09 percent of each matrix's entries equal the value Mistral's float8
  checkpoint stores for that entry, the raw code before its scale (up to 448), and the other 69.9 percent read
  about 0.136 times that code (0.133 to 0.137 on the two matrices fitted entry by entry), the parent's value
  entering at under one part in a thousand of it; the copy stands 0.72 from the codes on every matrix read. A density of 0.70 drops three entries in
  ten to the base's stored value, which is what the 30 percent read, and the base the merge read was the float8
  tensor without its `weight_scale_inv` (0.00025 to 0.0012 per matrix on the four read).
- The copy carries the parent's 585 tensor names and no scale, and its configuration carries the instruct
  checkpoint's `quantization_config` (`quant_method` fp8, static activations, `dequantize` false), which the
  parent's does not.
- No edit's direction: the saved vectors stand at 0.955 on the left and 0.881 on the right to round 14's
  measurement of timfromhcs's duplicate against the float8 checkpoint, because both differences are dominated by
  the same float8 codes read as weights, and at 0.14 or less to every other Mistral, Nemo and Ministral edit.

The parent read by byte range. jenerallee78's query projections of layers 0 and 20 are byte-equal to
mistralai/Ministral-3-14B-Instruct-2512-BF16 at `bbc49ba0` (2025-12-04, the day before the edit), its first shard
(`a381935a`) is that repository's first shard by object id, and its configuration (`9fb1dd07`) and `tokenizer.json`
(`57757562`) are that revision's; Mistral's float8 checkpoint dequantised with its scales stands 0.027 from the
bfloat16 release on every matrix read, the size of the eight-bit rounding. Against the bfloat16 release the edit
reads on the writers: the layer 20 attention output at 0.0185, the layer 20 down projection at 0.0159 and the
layer 30 attention output at 0.0149, each difference rank one (first shares 0.993, 0.990 and 0.989) on the output
side at a weight of 1.00 (left kept fraction -0.0022 to -0.0002), with the rows moved by up to 0.0184, 0.0105 and
0.0108 under a card that names grimjim's norm-preserving biprojection.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster on 1,021 fields and at home on the same, 10 of them explained by re-save.
The copy's token files are the float8 instruct checkpoint's head (`tokenizer.json` `99cf2742`, the 11,913-byte
template `47d042a0`, the processor file), as `tokenizer_source: base` asks, where the parent's are the bfloat16
release's December files: the parent's 1,000 added-token declarations in a 206,015-byte `tokenizer_config.json`
are absent from the copy's 22,174-byte one, ids 34 and 35 read `[THINK]` and `[/THINK]` on the parent's side and
`<SPECIAL_34>` and `<SPECIAL_35>` on the copy's (Mistral's own replacement of 06-30), and the template moves from
the 7,754-byte file to the 11,913-byte one, the two rendering the fixed conversation identically. The copy
publishes no `generation_config.json`; its configuration writes `bos_token_id` 1, `eos_token_id` 2 and
`pad_token_id` 11 into the text sub-configuration (the values the parent's generation file declares) and adds
`tie_word_embeddings` false and the `quantization_config`; the version string reads 5.0.0.dev0 to 5.5.3. The ids
are Mistral's on both sides and the vocabulary is 131,072 on both sides.

## For the recipe library

No entry reads a matrix whose stored values are codes of another format; the names step that refuses a float8
original (`docs/weights-method.md`) would catch this copy if it also refused a copy whose stored values exceed any
weight of its parent by two orders of magnitude, or whose configuration declares a quantisation its files do not
carry. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat45/measurements/pair-3/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
