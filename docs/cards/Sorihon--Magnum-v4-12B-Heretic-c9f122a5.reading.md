# Reading of the Stage 1 and Stage 2 result: Sorihon/Magnum-v4-12B-Heretic against anthracite-org/magnum-v4-12b (2026-11-02)

Measured on Wheat, round 43 piece 4 (download job 387204, compare job 387208, sweep 387213; the pull carries the
measurements and the sweep record and no job log). Modified revision `a91b91cf` (created 2026-05-13), parent
pinned at `3200513f` of 2024-11-25, anthracite-org's fine-tune of Mistral Nemo Instruct (created 2024-10-20,
`_name_or_path` mistralai/Mistral-Nemo-Instruct-2407). The card prints "Refusals 8/100" and "KL Divergence
0.0129" and nothing else of the run; Heretic is named in the repository name alone. The copy is measured against
the fine-tune its card names, so the pair reads the edit alone; the fine-tune's own distance from Nemo Instruct is
read by byte range below.

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 34 flags (first shares 0.867 to
0.989 under the 0.99 floor), on the cluster and after re-scoring at home. On reading, the copy is a kernel pass
with one shared direction on both writers, the output side, the down kernel rising from the seventh layer to the
twenty-ninth and the attention kernel scattered.

- 63 of 363 tensors changed: the down projections of layers 7 to 39 and the attention outputs of 10 to 39. Nothing
  moved on the other 300 tensors, the embeddings and the `lm_head` included. The largest relative change outside
  the changed set is exactly 0.
- One direction (first shares 0.867 to 0.995) shared across layers and writers: median agreement 0.998 (minimum
  0.977), cross-kind 0.936.
- Output side on all 63: one minus the left kept fraction rises on the down projections from 0.19 at layer 7
  through 0.50 at 15 and 0.81 at 22 to 1.03 at 29 and falls to 0.67 at 39, the smoothest kernel of the round; on
  the attention outputs it scatters from 0.33 (layer 39) to 1.28 (layers 27 and 31), with 0.85 at 10 beside 0.56
  at 14 and 0.49 at 34. Relative changes 0.0031 to 0.0217.
- Rows moved 0.0013 to 0.0137, through and over finding 22's band.
- The last layer's attention output reads left kept 0.67 and right kept 0.63, the one copy of the six whose last
  layer stays inside the kernel.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Down projection: change, E1, left kept, right kept | Weight | Rows (attention, down) |
| --- | --- | --- | --- | --- | --- |
| 7 | - | - | 0.0031, 0.867, 0.81, 0.89 | 0.19 | -, 0.0013 |
| 10 | 0.0152, 0.990, 0.15, 0.73 | 0.85 | 0.0049, 0.929, 0.71, 0.81 | 0.29 | 0.0053, 0.0022 |
| 15 | 0.0204, 0.994, 0.08, 0.72 | 0.92 | 0.0088, 0.973, 0.50, 0.78 | 0.50 | 0.0137, 0.0051 |
| 18 | 0.0217, 0.994, -0.07, 0.61 | 1.07 | 0.0105, 0.980, 0.35, 0.61 | 0.65 | 0.0120, 0.0058 |
| 22 | 0.0206, 0.994, 0.16, 0.51 | 0.84 | 0.0126, 0.986, 0.19, 0.48 | 0.81 | 0.0050, 0.0058 |
| 27 | 0.0196, 0.994, -0.28, 0.55 | 1.28 | 0.0140, 0.988, 0.03, 0.35 | 0.97 | 0.0051, 0.0056 |
| 29 | 0.0191, 0.993, 0.32, 0.52 | 0.68 | 0.0149, 0.989, -0.03, 0.35 | 1.03 | 0.0056, 0.0053 |
| 34 | 0.0177, 0.992, 0.51, 0.55 | 0.49 | 0.0121, 0.984, 0.17, 0.48 | 0.83 | 0.0045, 0.0074 |
| 39 | 0.0180, 0.993, 0.67, 0.63 | 0.33 | 0.0101, 0.979, 0.33, 0.55 | 0.67 | 0.0049, 0.0040 |

The full table (33 rows) is in the report.

Directions. Against the saved vectors of the round's other Nemo edits and the two measured edits of Nemo Instruct,
the direction stands at 0.707 on the left and 0.692 on the right to the maker's Celeste edit on all 35 shared
names, 0.656 and 0.611 to grimjim's block-wise pass (59 names), 0.605 and 0.617 to the maker's Dans edit, 0.514
and 0.531 to the DARKNESS edit, 0.500 and 0.517 to the NemoMix edit, 0.455 and 0.423 to the EtherealAurora edit,
0.116 to DuoNeural's projection and 0.026 or less to the controls. By byte range the layer 24 attention output is
0.0198 from the parent's, 0.0246 from Nemo Instruct's, 0.0435 from Nemo Base's, 0.0250 from DuoNeural's and
0.0254 from grimjim's (the parent 0.0146 from Instruct's and 0.0386 from Base's), the layer 24 down projection
0.0132 from the parent's, 0.0209 from Instruct's and 0.0425 from Base's (the parent 0.0162 from Instruct's), and
the layer 1 attention output and query projection byte-equal to the parent's, which stand 0.0166 and 0.0107 from
Instruct's. The copy's `tokenizer.json` shares its object id with the maker's DARKNESS edit.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster on 1,019 fields and at home on 1,018, the home judgement closing
`config.rope_parameters` (the 5.x form of `rope_theta`). The copy is a transformers 5.8.0 save of a 4.45.0.dev0
parent: the 1,000 added-token declarations and the `special_tokens_map.json` are dropped (finding 44's case),
`tokenizer_config.json` comes to 442 bytes, the `pad_token` changes from `<pad>` (id 10) to `</s>` (id 2), the
template moves to a 1,053-byte `chat_template.jinja` whose spacing differs from the parent's and renders the
fixed conversation differently (`[INST] What is two plus two?[/INST] Four.` against `[INST]What is two plus
two?[/INST]Four.`), `use_cache` false to true, `torch_dtype` to `dtype`. The token ids are Mistral's on both
sides (`bos_token_id` 1, `eos_token_id` 2) and the vocabulary is 131,072 on both sides.

## For the recipe library

A single-direction entry on both writers with a kernel line would read the copy as a kernel pass and print the
down kernel's rise to 1.03 at layer 29; the template that renders differently is the token side's one reading of
substance. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat43/measurements/pair-4/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
