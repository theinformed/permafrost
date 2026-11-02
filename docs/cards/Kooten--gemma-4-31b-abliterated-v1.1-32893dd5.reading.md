# Reading of the Stage 1 and Stage 2 result: Kooten/gemma-4-31b-abliterated-v1.1 against google/gemma-4-31B-it (2026-11-02)

Measured on Wheat, round 35 piece 4 (download job 387143, compare job 387147, sweep 387152; the pull carries the
measurements and the sweep record and no job log). Modified revision `4b215fad` (three commits on 2026-04-07:
created 17:59Z, the folder at 18:01Z, the README at 20:01Z), original pinned at `419b2efe` (04-02), the revision
current when the repository was created. The card (1,248 bytes) says "Uncensored using Heretic", 929 trials, 26
refusals in 100, KL 0.3687, and that the previous version "had some artifacts"; it prints no kernel, no layer and
no direction index. The repository carries the tool's trial record (`Heretic Checkpoint/google--gemma-4-31B-it.jsonl`,
4.1 MB) beside the two shards. The copy's configuration is a 5.6.0.dev0 save of the pin's 5.5.0.dev0 file, and its
vision tower is stored without the `.linear.` segment that Google's file puts inside every encoder linear
(`model.vision_tower.encoder.layers.N.self_attn.q_proj.weight` against `...q_proj.linear.weight`), the first copy
in the census paired through the in-tower mapping: the comparison's `name_mapping` block records the infix
`.linear.` carried by the original and 189 names renamed, and all 1,188 tensors matched.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection-selected`, 211 flags (189
unexpected changes, 22 first shares), on the cluster and after re-scoring at home. On reading, the copy is two
things: a Heretic linear-kernel edit of the language stack whose kernel reads back from the weights to the second
decimal, and a vision tower whose 189 linear matrices are fresh random draws.

- The language stack: 67 of the 832 language tensors changed, the down projections of layers 20 to 59 (40) and the
  attention outputs of 24 to 50 (27), nothing else, exactly 0 outside them. One direction on all 67 (within-layer
  cosines 0.9999, group cosines 0.99998), first shares 0.981 to 0.996, output side on 67 of 67 (right kept 0.28 to
  0.95). The weight read as one minus the left kept fraction is a straight line on each writer: on the attention
  outputs 0.71 at layer 24 rising by 0.058 a layer to 1.47 at 37 and falling at the same slope to 0.70 at 50; on
  the down projections 0.69 at 20 rising by 0.0135 a layer to 1.15 at 54 and falling to 1.08 at 59, where the
  stack ends. That is Heretic's linear kernel with its four numbers per writer read off the weights: attention
  1.47 at position 37 falling to 0.70 at distance 13, down projection 1.15 at position 54 falling to 0.69 at
  distance 34, which the card does not print (finding 59's kernel records, this time with no record to check
  against). Rows moved 0.004 to 0.087 on 66 of 67 and 0.53 on layer 59's down projection; no restoration is
  claimed.
- The vision tower: all 189 encoder linears (queries, keys, values, attention outputs, gates, ups and downs of 27
  layers) differ from Google's by 1.205 to 1.208 of the norm on the six square and tall kinds and 1.642 to 1.644
  on the down projections, with no leading direction (first shares 0.005 to 0.175), cosine 0.000 to the original
  and kept fractions at 0. The 167 other vision tensors (the six norms of each layer, the patch embedder's projection and position
  table, the two input scalars and the embedding projection) are equal to Google's byte for byte. A byte-range read of
  three of the 189 from the hub (`tools/hub_range_read.py`, the copy's names against Google's at `419b2efe` and at
  `842da379`) gives the copy's values a standard deviation of 0.0199, 0.0199 and 0.0199 (layer 0's query, layer
  13's down projection, layer 26's up projection) against Google's 0.0295, 0.0152 and 0.0295, a mean within
  0.00001 of zero, cosines of -0.0005, 0.0001 and 0.0003 to Google's, 62 distinct values per block of 64 and 0.6
  percent exact zeros. One scale for every shape, 0.02, is the library's default initialisation, and the
  relative differences follow from it alone: the square root of one plus the squared ratio of the scales is
  1.206 where Google's deviation is 0.0295 and 1.643 where it is 0.0152. The tower was not edited; it was drawn.
  Finding 63 read the same thing on Ilya626's E4B copy, whose card called the model multimodal; here the only
  change in the copy's files that touches the tower is the dropped `.linear.` segment, and a loader that does not
  know the segment initialises the weights it cannot find.

| Layer | Attention output: change, E1, left kept, read | Down projection: change, E1, left kept, read | Rows |
| --- | --- | --- | --- |
| 20 | - | 0.0103, 0.985, 0.31, 0.69 | -, 0.009 |
| 24 | 0.0106, 0.985, 0.29, 0.71 | 0.0116, 0.987, 0.26, 0.74 | 0.016, 0.014 |
| 28 | 0.0158, 0.993, 0.06, 0.94 | 0.0133, 0.990, 0.20, 0.80 | 0.034, 0.035 |
| 32 | 0.0202, 0.995, -0.18, 1.18 | 0.0139, 0.991, 0.15, 0.85 | 0.058, 0.037 |
| 37 | 0.0222, 0.996, -0.47, 1.47 | 0.0141, 0.991, 0.08, 0.92 | 0.056, 0.035 |
| 42 | 0.0166, 0.993, -0.18, 1.18 | 0.0131, 0.990, 0.01, 0.99 | 0.046, 0.008 |
| 46 | 0.0122, 0.988, 0.06, 0.94 | 0.0136, 0.990, -0.04, 1.04 | 0.052, 0.026 |
| 50 | 0.0089, 0.981, 0.30, 0.70 | 0.0141, 0.991, -0.09, 1.09 | 0.009, 0.045 |
| 54 | - | 0.0150, 0.992, -0.15, 1.15 | -, 0.047 |
| 59 | - | 0.0137, 0.991, -0.08, 1.08 | -, 0.528 |

The copy's two shards (`698fc8ad`, `080e6a6c`) share no checksum with Google's or with any measured copy, as a
two-shard save of a four-shard original cannot. Against the saved vectors of the eleven other 31B edits, the
direction stands at 0.55 to huihui-ai's first version and 0.58 to the second (one number each, since both sides
carry one direction), 0.82 to Sabomako's on the eight matrices both reach, and 0.28 or less to the rest.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster, "consistent with re-save noted" at home: `text_config.moe_intermediate_size`
closed by the default rule under transformers 5.22.1, and the two version strings (5.5.0.dev0 to 5.6.0.dev0) are a
re-save. The template is the pin's 12,045-byte file and the fixed conversation renders identically. Nothing on the
token side says anything about the tower.

## For the recipe library

Two entries for one copy. The language edit is the single-projection recipe with a kernel the reading recovers in
full; the 22 first-share flags (0.981 to 0.990 on the low-weight ends of both windows and on four down projections
in between, where the rule asks 0.99) are the kernel's shoulders. The tower is finding 63's case again and wants its own rule: a changed set whose
first shares sit near 1 over the matrix size, whose kept fractions are 0 and whose relative differences are the
square root of one plus a squared scale ratio is a fresh draw, and the card should be read as describing a
text-only model. The infix mapping did what it was built to do: it paired the 189 and measured them, where a name
comparison would have reported 189 missing and 189 added. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat35/measurements/pair-4/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
