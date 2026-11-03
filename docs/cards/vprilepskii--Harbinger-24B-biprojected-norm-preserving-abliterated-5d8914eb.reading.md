# Reading of the Stage 1 and Stage 2 result: vprilepskii/Harbinger-24B-biprojected-norm-preserving-abliterated against LatitudeGames/Harbinger-24B (2026-11-03)

Measured on Wheat, round 49 piece 4 (download job 387515, compare job 387519, sweep 387524; the pull carries the
measurements and the sweep record and no job log). Modified revision `8f9eee63` (created 2025-11-25 22:18Z, the
weights uploaded in one commit at 22:22Z), parent pinned at `0ded8c1f` of 2025-05-16, LatitudeGames's Harbinger
24B, a supervised and preference-trained fine-tune of mistralai/Mistral-Small-3.1-24B-Instruct-2503 for text
adventures, trained on ChatML with `<|im_end|>` at token id 999 as its end of sequence. The card is 235 bytes: the
parent and two links, grimjim's posts on projected abliteration and on norm-preserving biprojected abliteration, and
no parameter. The parent counts as neither an original nor a copy (finding 117).

## Weights (Stage 2)

The tool's assessment was violations against `single-projection-selected`, 58 flags (first shares 0.907 to 0.988
under the 0.99 floor on every changed matrix), on the cluster and after re-scoring at home. On reading, the copy is
one direction projected out of both writers of layers 4 to 39 at a smooth weight, with the rows moved.

- 58 of 363 tensors changed: the down projections of layers 4 to 39 and the attention outputs of layers 15 to 36.
  Everything else is exactly 0, and the copy's first shard is the parent's by object id.
- One direction for all 58 matrices: agreement 0.99998 at the median and 0.99996 at the least, the two writers of a
  layer at 0.99998, across kinds 0.9999.
- Output side on all 58: one minus the left kept fraction reads 1.364 at layer 4 rising to 1.443 at 27 and back to
  1.405 at 39 on the down projections, and 0.851 at layer 15 rising to 1.032 at 25 and back to 0.873 at 36 on the
  attention outputs, two smooth shapes the card does not print; the right side keeps -0.07 to 0.97.
- Relative changes 0.0120 to 0.0249; rows moved 0.0031 to 0.0178.

| Layer | Kind | Change | E1 | Weight read | Right kept | Rows |
| --- | --- | --- | --- | --- | --- | --- |
| 15 | attention output | 0.0146 | 0.958 | 0.851 | 0.79 | 0.0097 |
| 21 | attention output | 0.0160 | 0.969 | 0.961 | 0.73 | 0.0123 |
| 27 | attention output | 0.0151 | 0.959 | 1.014 | 0.76 | 0.0090 |
| 36 | attention output | 0.0128 | 0.917 | 0.873 | 0.97 | 0.0124 |
| 6 | down | 0.0193 | 0.981 | 1.371 | 0.32 | 0.0060 |
| 15 | down | 0.0241 | 0.987 | 1.404 | 0.57 | 0.0156 |
| 27 | down | 0.0202 | 0.983 | 1.443 | -0.06 | 0.0041 |
| 33 | down | 0.0195 | 0.982 | 1.424 | 0.25 | 0.0178 |
| 39 | down | 0.0202 | 0.971 | 1.405 | 0.55 | 0.0075 |

The full table (58 rows) is in the report.

The norm-preserving claim. The rows the census reads (each output row's norm) move by 0.0031 to 0.0178, through and
over finding 22's band, as on the edit of finding 130 under the same name. The method in the posts the card links
keeps a norm per input column instead, so the columns were read by byte range on three matrices, the layer 20 and 30
attention outputs and the layer 20 down projection. A plain projection of the parent along the copy's own leading
direction, at the weight the copy reads, rounded to bfloat16, lands 0.0031, 0.0027 and 0.0026 from the copy, against
the copy's 0.0161, 0.0131 and 0.0218 from the parent, and it moves the rows by up to 0.0153, 0.0050 and 0.0088 where
the copy moves them by 0.0148, 0.0041 and 0.0086. The copy's column norms hold within 0.00016 on 90 percent of the
columns and move by up to 0.0063, 0.0075 and 0.0076 on the rest, where the plain projection moves them by up to
0.0037, 0.0023 and 0.0165. So the copy is a plain projection to within 0.12 to 0.21 of its change, the rows are not
restored, and the columns are held no better than a plain projection holds them on the two attention outputs and
better on the down projection.

Directions. Against the saved vectors of the Mistral Small 24B measurements the direction stands at 0.746 to
venkycs's projection of Mistral Small 24B Instruct 2501 (58 names, minimum 0.746), 0.660 and 0.621 to grayarea's
Magistral and text-only passes, 0.586 to coder3101's Skyfall edit of this round, 0.530 to SAIFIINDUSTRIES's Dolphin
projection, 0.383 to coder3101's Magidonia edit, 0.32 and 0.31 to Pranavz's Hearthfire pass, 0.252 to huihui-ai's
Mistral Small 3.2 projection, and 0.08 or less to llmfan46's searches and the PaintedFantasy search. No measurement
stands on Harbinger or on Mistral Small 3.1 Instruct.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, six fields: the version strings move from 4.46.1 to 4.57.1,
`_name_or_path` is dropped, `torch_dtype` is written as `dtype` (the two fields left unexplained, the rename line owed
since round 47), and the template moves from `tokenizer_config.json` into `chat_template.jinja` with the parent's
291-byte ChatML text. `tokenizer.json` and `special_tokens_map.json` are the parent's by object id. The token ids
are the parent's on both sides (`bos_token_id` 1, `eos_token_id` 999 in the configuration and the generation file,
`<|im_end|>` the tokenizer's end of sequence) and the vocabulary is 131,072.

## For the recipe library

A single-projection entry with a lower first-share floor would read the copy; the rows break any row-norm entry,
and a column-norm line would read the method the card links. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat49/measurements/pair-4/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
