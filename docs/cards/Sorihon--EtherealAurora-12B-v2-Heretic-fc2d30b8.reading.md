# Reading of the Stage 1 and Stage 2 result: Sorihon/EtherealAurora-12B-v2-Heretic against yamatazen/EtherealAurora-12B-v2 (2026-11-02)

Measured on Wheat, round 43 piece 8 (download job 387204, compare job 387212, sweep 387213; the pull carries the
measurements and the sweep record and no job log). Modified revision `b8613fc8` (created 2026-03-18), parent
pinned at `f218cef0` of 2025-06-19, yamatazen's SLERP of the maker's EtherealAurora-12B with natong19's
abliterated Nemo Instruct at t 0.25, 0.3, 0.5, 0.3, 0.25 under a ChatML template (created 2025-03-12), the one
parent of the six that already carries an abliteration in its merge. The card is an image and a `base_model`
field; Heretic is named in the repository name alone. The copy is measured against the merge its card names, so
the pair reads the edit alone.

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 40 flags (32 first shares of
0.923 to 0.989 under the 0.99 floor and 8 direction cosines), on the cluster and after re-scoring at home. On
reading, the copy is a per-layer pass on both writers of layers 4 to 39, the output side, with the loosest
agreement between layers of the six and the attention weights scattered from 0.12 to 1.27.

- 68 of 363 tensors changed: the attention outputs of layers 4 to 39 and the down projections of 8 to 39.
  Nothing moved on the other 295 tensors. The largest relative change outside the changed set is exactly 0.
- One direction per layer (first shares 0.923 to 0.995): agreement between adjacent layers 0.861 at the median,
  0.164 between the first and the last, 0.001 at the minimum over all pairs of layers; the two writers of a layer
  agree at 0.83 or more within the layer and the cross-kind agreement is 0.0009 across layers.
- Output side on all 68: one minus the left kept fraction scatters on the attention outputs from 0.12 (layer 39)
  and 0.14 (36) to 1.27 (26 and 27), 1.21 (17) and 1.15 (31); on the down projections it rises from 0.19 at layer
  8 through 0.54 at 17 to 0.81 at 28 to 30 and falls to 0.41 at 36 and 0.53 at 39. Relative changes 0.0045 to
  0.0236 inside the window.
- Rows moved 0.0013 to 0.0218, through and over finding 22's band.
- The last layer's attention output reads apart: left kept 0.88, right kept 0.55, relative change 0.0318, rows
  0.0218 (the largest of the pair).

| Layer | Attention output: change, E1, left kept, right kept | Weight | Down projection: change, E1, left kept, right kept | Weight | Rows (attention, down) |
| --- | --- | --- | --- | --- | --- |
| 4 | 0.0161, 0.990, 0.61, 0.65 | 0.39 | - | - | 0.0033, - |
| 8 | 0.0185, 0.993, 0.46, 0.69 | 0.54 | 0.0045, 0.923, 0.81, 0.88 | 0.19 | 0.0051, 0.0021 |
| 13 | 0.0230, 0.995, 0.75, 0.59 | 0.25 | 0.0082, 0.970, 0.75, 0.79 | 0.25 | 0.0039, 0.0034 |
| 17 | 0.0202, 0.994, -0.21, 0.66 | 1.21 | 0.0087, 0.973, 0.46, 0.77 | 0.54 | 0.0074, 0.0045 |
| 21 | 0.0236, 0.995, 0.80, 0.56 | 0.20 | 0.0096, 0.977, 0.41, 0.62 | 0.59 | 0.0108, 0.0046 |
| 24 | 0.0223, 0.994, 0.82, 0.49 | 0.18 | 0.0101, 0.979, 0.32, 0.56 | 0.68 | 0.0165, 0.0070 |
| 27 | 0.0190, 0.993, -0.27, 0.59 | 1.27 | 0.0109, 0.981, 0.21, 0.54 | 0.79 | 0.0087, 0.0057 |
| 29 | 0.0195, 0.993, 0.16, 0.60 | 0.84 | 0.0117, 0.983, 0.19, 0.52 | 0.81 | 0.0107, 0.0077 |
| 36 | 0.0230, 0.995, 0.86, 0.54 | 0.14 | 0.0104, 0.979, 0.59, 0.60 | 0.41 | 0.0094, 0.0065 |
| 39 | 0.0318, 0.995, 0.88, 0.55 | 0.12 | 0.0116, 0.982, 0.47, 0.65 | 0.53 | 0.0218, 0.0094 |

The full table (36 rows) is in the report.

Directions. Against the saved vectors of the round's other Nemo edits and the two measured edits of Nemo Instruct,
the directions stand at 0.696 on the left and 0.609 on the right to the maker's Celeste edit on all 35 shared
names, 0.664 and 0.613 to the Dans edit (47), 0.455 and 0.423 to the Magnum edit, 0.430 and 0.282 to grimjim's
block-wise pass (64), 0.335 to the DARKNESS edit, 0.327 to the NemoMix edit, 0.089 to DuoNeural's projection and
0.015 or less to the controls. By byte range the layer 24 attention output is 0.0223 from the parent's, 0.0391 from natong19's abliterated Instruct, 0.0400 from Nemo Instruct's, 0.0477 from Nemo Base's, 0.0402 from DuoNeural's and 0.0409 from grimjim's (the parent 0.0324 from natong19's and 0.0330 from Instruct's; natong19's 0.0156 from Instruct's), the layer 24 down projection 0.0101 from the parent's and 0.0372 from Instruct's, and the layer 1 attention output and query projection byte-equal to the parent's (0.0473 and 0.0269 from Instruct's).

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home on the same fields: a `generation_config.json` written from
the configuration (`_from_model_config`, `bos_token_id` 1, `eos_token_id` 2) where the parent had none,
`use_cache` false to true, `torch_dtype` to `dtype`, the version string 4.49.0 to 4.57.6; the template moved from
`tokenizer_config.json` to a 291-byte ChatML `chat_template.jinja` (the bytes the maker's Celeste edit carries)
and renders the fixed conversation identically. The token ids are Mistral's on both sides (`bos_token_id` 1,
`eos_token_id` 2) and the vocabulary is 131,072 on both sides.

## For the recipe library

A per-layer entry on both writers with a scatter line would read the copy; a merge whose parent already carries
an abliteration gives the pass a second direction to find, and the saved vectors place this one at 0.09 to
natong19's kin (DuoNeural's projection on the same checkpoint). The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat43/measurements/pair-8/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
