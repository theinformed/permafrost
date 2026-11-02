# Reading of the Stage 1 and Stage 2 result: Sorihon/MN-12B-Celeste-V1.9-Heretic against nothingiisreal/MN-12B-Celeste-V1.9 (2026-11-02)

Measured on Wheat, round 43 piece 7 (download job 387204, compare job 387211, sweep 387213; the pull carries the
measurements and the sweep record and no job log). Modified revision `b107bcb0` (created 2026-05-15), parent
pinned at `26ff4e3b` of 2024-08-24, nothingiisreal's fine-tune of Mistral Nemo Instruct under a ChatML template
(created 2024-07-31, `_name_or_path` mistralai/Mistral-Nemo-Instruct-2407). The card prints "Refusals 5/100" and
"KL Divergence 0.0087" and nothing else of the run. The copy is measured against the fine-tune its card names, so
the pair reads the edit alone.

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 9 flags (first shares 0.983 to
0.989 under the 0.99 floor), on the cluster and after re-scoring at home. On reading, the copy is a per-layer
pass on both writers, the output side, the narrowest of the six windows, the down kernel peaking at layer 28.

- 35 of 363 tensors changed: the attention outputs of layers 18 to 39 and the down projections of 22 to 34.
  Nothing moved on the other 328 tensors. The largest relative change outside the changed set is exactly 0.
- One direction per layer (first shares 0.983 to 0.997): agreement between adjacent layers 0.945 at the median,
  0.140 between the first and the last; the two writers of a layer are unrelated (cross-kind 0.140).
- Output side on all 35: one minus the left kept fraction is 0.59 to 1.31 on the attention outputs of layers 18
  to 38 (1.31 at 27, 1.26 at 26, 1.27 at 31; 0.59 at 34, 0.63 at 24) and rises on the down projections from 0.85
  at layer 22 to 1.15 at 28 and falls to 0.81 at 34. Relative changes 0.0168 to 0.0225 on the attention outputs
  of 18 to 38, 0.0117 to 0.0172 on the down projections.
- Rows moved 0.0022 to 0.0111, through and over finding 22's band.
- The last layer's attention output reads apart: left kept 0.92, right kept 0.44, relative change 0.0326 (the
  largest of the pair).

| Layer | Attention output: change, E1, left kept, right kept | Weight | Down projection: change, E1, left kept, right kept | Weight | Rows (attention, down) |
| --- | --- | --- | --- | --- | --- |
| 18 | 0.0224, 0.995, -0.14, 0.60 | 1.14 | - | - | 0.0111, - |
| 22 | 0.0204, 0.994, 0.12, 0.49 | 0.88 | 0.0132, 0.987, 0.15, 0.45 | 0.85 | 0.0052, 0.0042 |
| 24 | 0.0195, 0.993, 0.37, 0.53 | 0.63 | 0.0141, 0.988, 0.05, 0.31 | 0.95 | 0.0061, 0.0037 |
| 27 | 0.0194, 0.993, -0.31, 0.54 | 1.31 | 0.0159, 0.991, -0.10, 0.26 | 1.10 | 0.0039, 0.0036 |
| 28 | 0.0225, 0.995, -0.01, 0.43 | 1.01 | 0.0172, 0.992, -0.15, 0.22 | 1.15 | 0.0057, 0.0040 |
| 31 | 0.0220, 0.995, -0.27, 0.51 | 1.27 | 0.0141, 0.988, 0.02, 0.42 | 0.98 | 0.0047, 0.0033 |
| 34 | 0.0180, 0.992, 0.41, 0.56 | 0.59 | 0.0117, 0.983, 0.19, 0.49 | 0.81 | 0.0030, 0.0022 |
| 37 | 0.0173, 0.992, -0.09, 0.63 | 1.09 | - | - | 0.0031, - |
| 39 | 0.0326, 0.997, 0.92, 0.44 | 0.08 | - | - | 0.0078, - |

The full table (22 rows) is in the report.

Directions. Against the saved vectors of the round's other Nemo edits and the two measured edits of Nemo Instruct,
the directions stand at 0.729 on the left and 0.732 on the right to the maker's Dans edit on all 35 shared names
(minimum 0.617), 0.707 and 0.692 to the Magnum edit, 0.696 and 0.609 to the EtherealAurora edit, 0.675 and
0.632 to grimjim's block-wise pass (33), 0.365 to the DARKNESS edit, 0.353 to the NemoMix edit, 0.118 to
DuoNeural's projection and 0.024 or less to the controls. By byte range the layer 24 attention output is 0.0195 from the parent's, 0.0435 from Nemo Instruct's, 0.0566 from Nemo Base's, 0.0437 from DuoNeural's and 0.0440 from grimjim's (the parent 0.0389 from Instruct's and 0.0530 from Base's), the layer 24 down projection 0.0141 from the parent's and 0.0252 from Instruct's, and the layer 1 attention output and query projection byte-equal to the parent's (0.0432 and 0.0183 from Instruct's).

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster on 1,016 fields and at home on 1,015, the home judgement closing
`config.rope_parameters`. The copy is a transformers 5.8.0 save of a 4.44.0.dev0 parent: the 1,000 added-token
declarations and the `special_tokens_map.json` are dropped (finding 44's case), `tokenizer_config.json` comes to
338 bytes, the template moves to a 291-byte ChatML `chat_template.jinja` (the same bytes the maker's
EtherealAurora edit carries) and renders the fixed conversation identically, `use_cache` false to true,
`torch_dtype` to `dtype`. The token ids are Mistral's on both sides (`bos_token_id` 1, `eos_token_id` 2) and the
vocabulary is 131,072 on both sides.

## For the recipe library

A per-layer entry on both writers with a kernel line would read the copy as its window; the dropped-declarations
rule through `tokenizer.json` would read the token side as a re-save. The direction vectors stay in the pull copy
at `/opt/ai/hpc-packages/pulls/model-audit/wheat43/measurements/pair-7/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
