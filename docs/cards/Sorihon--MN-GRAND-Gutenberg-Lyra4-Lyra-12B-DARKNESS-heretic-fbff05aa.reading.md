# Reading of the Stage 1 and Stage 2 result: Sorihon/MN-GRAND-Gutenberg-Lyra4-Lyra-12B-DARKNESS-heretic against DavidAU/MN-GRAND-Gutenberg-Lyra4-Lyra-12B-DARKNESS (2026-11-02)

Measured on Wheat, round 43 piece 3 (download job 387204, compare job 387207, sweep 387213; the pull carries the
measurements and the sweep record and no job log). Modified revision `f6f51124` (created 2026-03-04 20:30Z),
parent pinned at `acfc836e` of 2025-07-28, DavidAU's merge of Mistral Nemo 12B fine-tunes (created 2024-10-11,
`_name_or_path` a local Nemo Instruct folder, no declared base). The card is an image and a `base_model` field;
Heretic is named in the repository name alone, with no table and no settings. The copy is measured against the
merge its card names and not against Mistral, so the pair reads the edit alone; the merge's own distance from Nemo
Instruct and Nemo Base is read by byte range below.

## Weights (Stage 2)

The tool's assessment was violations against `single-projection-selected`, 54 flags (53 first shares of 0.972 to
0.989 under the 0.99 floor and 1 cross-kind direction), on the cluster and after re-scoring at home. On reading,
the copy is a kernel pass with one shared direction on both writers of layers 3 to 39, the output side, with a
smooth down kernel and a scattered attention kernel.

- 73 of 363 tensors changed: the attention outputs of layers 3 to 39 and the down projections of 4 to 39. Nothing
  moved on the other 290 tensors, the embeddings and the `lm_head` (131,072 by 5,120 on both sides) included. The
  largest relative change outside the changed set is exactly 0.
- One direction (first shares 0.972 to 0.994) shared across layers and across the two writers: median agreement
  0.996 (minimum 0.962), cross-kind 0.894.
- Output side on all 73: one minus the left kept fraction is 0.57 at layer 4, 0.43 at 10 and 11, rising to 0.82 at
  22 to 25 and falling to 0.63 at 39 on the down projections, a kernel readable to the layer; on the attention
  outputs it scatters from 0.07 (layer 39) to 1.20 (layer 27), with 1.12 at 26 and 1.08 at 31 (the component
  reversed) beside 0.18 at 14 and 0.25 at 3. Relative changes 0.0086 to 0.0213.
- Rows moved 0.0030 to 0.0135, through and over finding 22's band.
- The last layer's attention output reads apart: left kept 0.93, right kept 0.71, relative change 0.0137.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Down projection: change, E1, left kept, right kept | Weight | Rows (attention, down) |
| --- | --- | --- | --- | --- | --- |
| 3 | 0.0086, 0.972, 0.75, 0.84 | 0.25 | - | - | 0.0041, - |
| 4 | 0.0090, 0.974, 0.62, 0.82 | 0.38 | 0.0086, 0.972, 0.43, 0.67 | 0.57 | 0.0042, 0.0030 |
| 10 | 0.0122, 0.985, 0.58, 0.77 | 0.42 | 0.0102, 0.979, 0.57, 0.64 | 0.43 | 0.0065, 0.0066 |
| 14 | 0.0161, 0.991, 0.82, 0.76 | 0.18 | 0.0130, 0.986, 0.47, 0.70 | 0.53 | 0.0064, 0.0081 |
| 18 | 0.0213, 0.994, 0.22, 0.63 | 0.78 | 0.0129, 0.987, 0.27, 0.56 | 0.73 | 0.0135, 0.0063 |
| 24 | 0.0203, 0.994, 0.61, 0.46 | 0.39 | 0.0121, 0.984, 0.18, 0.41 | 0.82 | 0.0046, 0.0063 |
| 27 | 0.0188, 0.993, -0.20, 0.55 | 1.20 | 0.0114, 0.983, 0.22, 0.46 | 0.78 | 0.0059, 0.0050 |
| 31 | 0.0169, 0.992, -0.08, 0.57 | 1.08 | 0.0107, 0.980, 0.28, 0.57 | 0.72 | 0.0056, 0.0069 |
| 35 | 0.0149, 0.989, 0.31, 0.63 | 0.69 | 0.0099, 0.978, 0.34, 0.56 | 0.66 | 0.0055, 0.0050 |
| 39 | 0.0137, 0.988, 0.93, 0.71 | 0.07 | 0.0100, 0.978, 0.37, 0.56 | 0.63 | 0.0043, 0.0050 |

The full table (37 rows) is in the report.

Directions. Against the saved vectors of the round's other Nemo edits and the two measured edits of Nemo Instruct,
the direction stands at 0.904 on the left and 0.905 on the right to the maker's NemoMix edit on all 67 shared
names (minimum 0.897), 0.549 and 0.488 to grimjim's block-wise pass on Nemo Instruct (69 names), 0.514 and 0.531
to the maker's Magnum edit, 0.370 to the maker's Dans edit, 0.365 to the Celeste edit, 0.335 to the EtherealAurora
edit, 0.094 to DuoNeural's difference-of-means projection on Nemo Instruct and 0.027 or less to the controls on
Mistral Small. By byte range the layer 24 attention output is 0.0203 from the parent's, 0.0299 from Nemo
Instruct's, 0.0415 from Nemo Base's, 0.0302 from DuoNeural's and 0.0329 from grimjim's (the parent 0.0220 from
Instruct's and 0.0360 from Base's; Instruct 0.0362 from Base; DuoNeural's 0.0043 and grimjim's 0.0161 from
Instruct's), the layer 24 down projection 0.0121 from the parent's, 0.0211 from Instruct's and 0.0364 from
Base's (the parent 0.0174 from Instruct's), and the layer 1 attention output and query projection byte-equal to
the parent's, which stand 0.0067 and 0.0042 from Instruct's and 0.0425 and 0.0303 from Base's, the merge's own
change. The copy's `tokenizer.json` is a 17 MB re-save whose object id it shares with the maker's Magnum edit.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home on the same fields: a `pad_token` `</s>` (id 2) added to
`tokenizer_config.json` and `special_tokens_map.json` where the parent declared none, a `generation_config.json`
written from the configuration (`_from_model_config`, `bos_token_id` 1, `eos_token_id` 2) where the parent had
none, `torch_dtype` to `dtype` and the version string 4.43.3 to 4.57.6; the template moved from
`tokenizer_config.json` to a 1,053-byte `chat_template.jinja`, the same bytes the maker's Magnum and NemoMix
edits carry, and renders the fixed conversation identically. The token ids are Mistral's on both sides
(`bos_token_id` 1, `eos_token_id` 2) and the vocabulary is 131,072 on both sides.

## For the recipe library

A single-direction entry on both writers with a kernel line on the down projections and a scatter line on the
attention outputs (finding 46's shape) would read the copy as a kernel pass with no card to read it against. The
direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat43/measurements/pair-3/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
