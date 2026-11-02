# Reading of the Stage 1 and Stage 2 result: Sorihon/Dans-PersonalityEngine-V1.3.0-12B-Heretic against PocketDoc/Dans-PersonalityEngine-V1.3.0-12b (2026-11-02)

Measured on Wheat, round 43 piece 5 (download job 387204, compare job 387209, sweep 387213; the pull carries the
measurements and the sweep record and no job log). Modified revision `eda0adf1` (created 2026-04-28), parent
pinned at `62004ca4` of 2025-05-23, PocketDoc's fine-tune of mistralai/Mistral-Nemo-Base-2407 (created 05-08),
the one parent of the six trained on the base checkpoint rather than Instruct. The card prints "Refusals 6/100"
and "KL Divergence 0.0235" and nothing else of the run. The copy is measured against the fine-tune its card
names, so the pair reads the edit alone; the copy's first shard (`dff85594`) is byte-equal to the parent's by
object id, the layers below the window.

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 18 flags (first shares 0.950 to
0.989 under the 0.99 floor), on the cluster and after re-scoring at home. On reading, the copy is a per-layer pass
on both writers, the output side, the attention component removed whole on every layer of its window and the
down kernel rising and falling.

- 47 of 363 tensors changed: the attention outputs of layers 11 to 39 and the down projections of 21 to 38.
  Nothing moved on the other 316 tensors. The largest relative change outside the changed set is exactly 0.
- One direction per layer (first shares 0.950 to 0.997): agreement between adjacent layers 0.925 at the median,
  0.055 between the first and the last; against the median direction the attention outputs stand at 0.25 at
  layer 11 rising to 0.95 at 29 and falling after; the two writers of a layer are unrelated (cross-kind 0.039).
- Output side on all 47: one minus the left kept fraction is 0.98 to 1.16 on the attention outputs of layers 11
  to 38 (the left kept fraction between 0.02 and -0.16, the component removed and a little reversed on every
  layer), and rises on the down projections from 0.39 at layer 21 through 0.74 at 25 to 1.08 at 30 and falls to
  0.39 at 38. Relative changes 0.0157 to 0.0213 on the attention outputs of 11 to 38, 0.0060 to 0.0154 on the
  down projections.
- Rows moved 0.0015 to 0.0091, through and over finding 22's band, and 0.0222 on layer 39.
- The last layer's attention output reads apart: left kept 0.93, right kept 0.39, relative change 0.0289 (the
  largest of the pair), rows 0.0222.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Down projection: change, E1, left kept, right kept | Weight | Rows (attention, down) |
| --- | --- | --- | --- | --- | --- |
| 11 | 0.0194, 0.993, -0.01, 0.61 | 1.01 | - | - | 0.0045, - |
| 15 | 0.0201, 0.994, -0.10, 0.69 | 1.10 | - | - | 0.0070, - |
| 18 | 0.0213, 0.995, -0.16, 0.62 | 1.16 | - | - | 0.0064, - |
| 21 | 0.0188, 0.993, -0.14, 0.63 | 1.14 | 0.0060, 0.950, 0.61, 0.76 | 0.39 | 0.0080, 0.0032 |
| 25 | 0.0171, 0.992, -0.10, 0.56 | 1.10 | 0.0108, 0.981, 0.26, 0.50 | 0.74 | 0.0055, 0.0054 |
| 30 | 0.0165, 0.991, -0.09, 0.59 | 1.09 | 0.0154, 0.990, -0.08, 0.38 | 1.08 | 0.0034, 0.0051 |
| 34 | 0.0166, 0.991, 0.01, 0.58 | 0.99 | 0.0107, 0.981, 0.26, 0.53 | 0.74 | 0.0033, 0.0032 |
| 38 | 0.0179, 0.992, -0.09, 0.61 | 1.09 | 0.0066, 0.957, 0.61, 0.73 | 0.39 | 0.0038, 0.0015 |
| 39 | 0.0289, 0.997, 0.93, 0.39 | 0.07 | - | - | 0.0222, - |

The full table (29 rows) is in the report.

Directions. Against the saved vectors of the round's other Nemo edits and the two measured edits of Nemo Instruct,
the directions stand at 0.729 on the left and 0.732 on the right to the maker's Celeste edit on all 35 shared
names (minimum 0.617), 0.664 and 0.613 to the EtherealAurora edit (47), 0.605 and 0.617 to the Magnum edit, 0.524
and 0.503 to grimjim's block-wise pass (44), 0.370 to the DARKNESS edit, 0.360 to the NemoMix edit, 0.114 to
DuoNeural's projection and 0.019 or less to the controls. By byte range the layer 24 attention output is 0.0173 from the parent's, 0.0653 from Nemo Instruct's and 0.0563 from Nemo Base's (the parent 0.0631 from Instruct's and 0.0536 from Base's, farther from both Mistral checkpoints than they are from each other at 0.0362), the layer 24 down projection 0.0097 from the parent's and 0.0651 from Instruct's, and the layer 1 attention output and query projection byte-equal to the parent's, which stand 0.1159 and 0.0377 from Instruct's and 0.1098 and 0.0241 from Base's, the deepest training of the six parents. Against the other five copies at layer 24 the attention output stands 0.0606 to 0.0755 away, the farthest of the six.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home on the same three fields: `use_cache` false to true,
`torch_dtype` to `dtype`, with the version strings 4.51.3 to 4.57.6 in the configuration and the generation
file; the template moved from `tokenizer_config.json` to a 763-byte `chat_template.jinja`, the parent's own
template and not the Mistral one the maker's other edits carry, and renders the fixed conversation identically.
The token ids (`bos_token_id` 1, `eos_token_id` 2, `pad_token_id` 10) are the parent's and the vocabulary is
131,072 on both sides.

## For the recipe library

A per-layer entry on both writers with a kernel line would read the copy; the attention weights of 0.98 to 1.16
on every layer of the window are the branch's "remove the component" with a small overshoot, which no rule
names. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat43/measurements/pair-5/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
