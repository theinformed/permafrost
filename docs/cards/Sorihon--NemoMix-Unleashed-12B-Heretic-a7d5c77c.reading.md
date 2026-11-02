# Reading of the Stage 1 and Stage 2 result: Sorihon/NemoMix-Unleashed-12B-Heretic against MarinaraSpaghetti/NemoMix-Unleashed-12B (2026-11-02)

Measured on Wheat, round 43 piece 6 (download job 387204, compare job 387210, sweep 387213; the pull carries the
measurements and the sweep record and no job log). Modified revision `900a365f` (created 2026-04-07), parent
pinned at `74fe434e` of 2025-02-05, MarinaraSpaghetti's `della_linear` merge on Mistral Nemo Base of Nemo
Instruct, bophades, gutenberg, Lyra-v1 and mini-magnum (created 2024-08-21, `_name_or_path` a local mergekit
folder). The card is an image and a `base_model` field; Heretic is named in the repository name alone. The copy
is measured against the merge its card names, so the pair reads the edit alone.

## Weights (Stage 2)

The tool's assessment was violations against `single-projection-selected`, 40 flags (39 first shares of 0.954 to
0.989 under the 0.99 floor and 1 cross-kind direction), on the cluster and after re-scoring at home. On reading,
the copy is a kernel pass with one shared direction on both writers of layers 6 to 39, the output side, the
down kernel smooth and the attention kernel scattered, at 0.90 to the maker's DARKNESS edit.

- 67 of 363 tensors changed: the down projections of layers 6 to 39 and the attention outputs of 7 to 39. Nothing
  moved on the other 296 tensors. The largest relative change outside the changed set is exactly 0.
- One direction (first shares 0.954 to 0.995) shared across layers and writers: median agreement 0.997 (minimum
  0.964), cross-kind 0.901.
- Output side on all 67: one minus the left kept fraction is 0.41 at layer 6 on the down projections, dipping to
  0.35 at 10 and 11, rising to 0.83 at 24 and falling to 0.48 at 39; on the attention outputs it scatters from
  0.09 (layer 39) to 1.03 (layer 31), 0.22 at 14 beside 0.88 at 7 and 0.93 at 26 and 33. Relative changes 0.0064
  to 0.0228.
- Rows moved 0.0027 to 0.0152, through and over finding 22's band.
- The last layer's attention output reads apart: left kept 0.91, right kept 0.63.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Down projection: change, E1, left kept, right kept | Weight | Rows (attention, down) |
| --- | --- | --- | --- | --- | --- |
| 6 | - | - | 0.0064, 0.954, 0.59, 0.78 | 0.41 | -, 0.0032 |
| 7 | 0.0153, 0.990, 0.12, 0.68 | 0.88 | 0.0069, 0.959, 0.61, 0.76 | 0.39 | 0.0058, 0.0035 |
| 10 | 0.0160, 0.991, 0.44, 0.69 | 0.56 | 0.0083, 0.970, 0.65, 0.72 | 0.35 | 0.0055, 0.0054 |
| 14 | 0.0184, 0.993, 0.78, 0.72 | 0.22 | 0.0117, 0.984, 0.52, 0.74 | 0.48 | 0.0064, 0.0065 |
| 15 | 0.0228, 0.995, 0.39, 0.69 | 0.61 | 0.0125, 0.985, 0.45, 0.73 | 0.55 | 0.0152, 0.0087 |
| 24 | 0.0167, 0.991, 0.70, 0.56 | 0.30 | 0.0121, 0.984, 0.17, 0.41 | 0.83 | 0.0041, 0.0052 |
| 27 | 0.0160, 0.991, -0.02, 0.61 | 1.02 | 0.0109, 0.981, 0.25, 0.48 | 0.75 | 0.0042, 0.0047 |
| 31 | 0.0163, 0.991, -0.03, 0.58 | 1.03 | 0.0095, 0.976, 0.35, 0.61 | 0.65 | 0.0063, 0.0052 |
| 35 | 0.0159, 0.990, 0.30, 0.61 | 0.70 | 0.0082, 0.969, 0.45, 0.63 | 0.55 | 0.0045, 0.0052 |
| 39 | 0.0168, 0.991, 0.91, 0.63 | 0.09 | 0.0074, 0.964, 0.52, 0.67 | 0.48 | 0.0058, 0.0029 |

The full table (34 rows) is in the report.

Directions. Against the saved vectors of the round's other Nemo edits and the two measured edits of Nemo Instruct,
the direction stands at 0.904 on the left and 0.905 on the right to the maker's DARKNESS edit on all 67 shared
names (minimum 0.897), 0.500 and 0.517 to the Magnum edit, 0.391 and 0.417 to grimjim's block-wise pass (63),
0.360 to the Dans edit, 0.353 to the Celeste edit, 0.327 to the EtherealAurora edit, 0.089 to DuoNeural's
projection and 0.020 or less to the controls. The two merges whose edits agree at 0.90 both carry Lyra and
Gutenberg lines (DavidAU's names them in its title; this parent lists Lyra-v1 and gutenberg among its five
sources), the closest lineage of any two parents in the round. By byte range the layer 24 attention output is 0.0167 from the parent's, 0.0266 from Nemo Instruct's, 0.0274 from Nemo Base's, 0.0270 from DuoNeural's and 0.0301 from grimjim's (the parent 0.0208 from Instruct's and 0.0215 from Base's), the layer 24 down projection 0.0121 from the parent's and 0.0247 from Instruct's, the layer 1 attention output and query projection byte-equal to the parent's (0.0240 and 0.0172 from Instruct's), and the copy 0.0275 from the DARKNESS edit at layer 24, the closest of the fifteen pairs of copies.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home on the same fields: a `pad_token` `</s>` (id 2) added to
`tokenizer_config.json` and `special_tokens_map.json` where the parent declared none, a `generation_config.json`
written from the configuration where the parent had none, `torch_dtype` to `dtype`, the version string 4.44.0
to 4.57.6, and a 1,053-byte `chat_template.jinja` (the Mistral template the maker's DARKNESS and Magnum edits
carry) where the parent published no template at all, so the tool has nothing to render on the parent's side.
The token ids are Mistral's on both sides (`bos_token_id` 1, `eos_token_id` 2) and the vocabulary is 131,072 on
both sides.

## For the recipe library

A single-direction entry on both writers with a kernel line and a scatter line would read the copy as the
DARKNESS edit's twin; the missing-template line of round 38 would read the parent's side. The direction vectors
stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat43/measurements/pair-6/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
