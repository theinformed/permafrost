# Reading of the Stage 1 and Stage 2 result: Naphula/Delirium-v1-abliterated against sam-paech/Delirium-v1

Measured on Wheat, round 52 piece 5 (download job 387662, compare job 387667, sweep 387671; the pull carries the
measurements and the sweep record and no job log). Modified revision `0e69a1d5`, parent pinned at `98dc2dad`.
sam-paech's Delirium v1 is a preference fine-tune of unsloth/gemma-2-9b-it on a Gutenberg and antislop set, and by byte
range it stands 0.00010, 0.00075 and 0.00084 from google/gemma-2-9b-it on the layer 5 query projection and the layer 20
attention output and down projection. The card names no parameters: "My first abliteration attempt, made manually by
testing various scale and layer configurations", 88 percent uncensored, two prefill strings offered to remove the rest
of the refusals, and the tool named as jim-plus's llm-abliteration at commit `4f68fab3`. The copy is the earlier of the
maker's two Gemma 2 projections by three weeks; the later, of sam-paech's Darkest-muse merge, is finding 150. The
parent counts as neither an original nor a copy (finding 117).

## Weights (Stage 2)

The tool's assessment was "recipe match", nearest recipe `single-projection-selected`, 0 flags, on the cluster and
after re-scoring at home. On reading, the copy is one direction projected out of both writers of layers 15 to 40 at a
flat 1.5.

- 52 of 464 tensors changed: the down projections and attention outputs of layers 15 to 40, 26 of the 42 layers.
  Layers 0 to 14 and 41 are unchanged (the layer 10 attention output is the parent's bytes by byte range), and
  everything else is exactly 0, the embedding included.
- One direction serves all 52: 0.9993 at the median, 0.9971 at the least, 0.9957 across the two kinds.
- Output side on all 52. One minus the left kept fraction reads 1.500 to 1.504 on every matrix; first shares 0.995 to
  0.997; relative changes 0.0229 to 0.0290; rows moved 0.0032 to 0.0320 under a card that names no norm.

| Layer | Kind | Change | E1 | Left kept | Right kept | Weight read | Rows |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 15 | attention output | 0.0249 | 0.996 | -0.50 | 0.50 | 1.500 | 0.0125 |
| 22 | attention output | 0.0277 | 0.997 | -0.50 | 0.45 | 1.501 | 0.0253 |
| 29 | attention output | 0.0241 | 0.996 | -0.50 | 0.74 | 1.501 | 0.0083 |
| 35 | attention output | 0.0246 | 0.996 | -0.50 | 0.88 | 1.500 | 0.0240 |
| 40 | attention output | 0.0242 | 0.996 | -0.50 | 0.56 | 1.501 | 0.0070 |
| 15 | down | 0.0253 | 0.996 | -0.50 | 0.36 | 1.501 | 0.0139 |
| 22 | down | 0.0265 | 0.996 | -0.50 | 0.13 | 1.500 | 0.0147 |
| 29 | down | 0.0251 | 0.996 | -0.50 | -0.03 | 1.501 | 0.0088 |
| 40 | down | 0.0242 | 0.996 | -0.50 | -0.03 | 1.500 | 0.0032 |

The full table (52 rows) is in the report.

Directions. Against the saved vectors of the maker's Darkest-muse projection, the only other measurement on the
hidden size of 3,584, the direction stands at 0.9996 on the left and 0.9995 on the right on all 52 shared names (the
least 0.99955 and 0.99939), as close as this copy's own matrices stand to each other. By byte range the two edits'
leading directions on the layer 20 attention output stand at 0.99956 and 0.99954, at relative changes of 0.02516 and
0.02514. The two parents stand 0.0012 to 0.0032 apart on the three matrices read, Delirium within 0.0009 of Google's
checkpoint and Darkest-muse 0.0012 to 0.0032 from it.

## Token and configuration side (Stage 1)

"Undecided" on the cluster and at home: the shared template refuses the fixed conversation's system turn on both sides,
and neither side differs in a compared field beyond `_name_or_path`. The template sits in `tokenizer_config.json`, which
with `tokenizer.json`, the special-token map and the generation file is the parent's by checksum, so every
conversation renders the same through the two.

## For the recipe library

The single-projection entry reads this copy with no flag, a window of layers being the one thing the recipe does not
state. The two Gemma 2 projections give the saved-vector check its first pair on this hidden size. The direction
vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat52/measurements/pair-5/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
