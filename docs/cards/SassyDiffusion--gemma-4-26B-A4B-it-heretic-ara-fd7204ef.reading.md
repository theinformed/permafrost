# Reading of the Stage 1 and Stage 2 result: SassyDiffusion/gemma-4-26B-A4B-it-heretic-ara against google/gemma-4-26B-A4B-it (2026-11-02)

Measured on Nautilus, round 38 piece 1 (download job 4168771, compare job 4168772, sweep 4168780; the pull carries
the measurements and the sweep record and no job log). Modified revision `328148e9` (seven commits from 2026-04-04
to 05-04, the last "update chat_template.jinja"), original pinned at `47b6801b`. The card (208 bytes) is front
matter alone: the licence, the `base_model` field naming google/gemma-4-26B-A4B-it and the tags `gemma4`,
`heretic-ara`, `gemma`, `google`. No parameter, window, weight or refusal count is printed anywhere; the tag is the
one word on method. The configuration carries `unsloth_fixed: true` and a transformers version of 5.6.0.dev0
against the pin's 5.5.0.dev0.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 61 flags (35 first
shares, 26 within-layer cosines on the 13 layers where both writers are edited), on the cluster and after
re-scoring at home. On reading, the copy is Heretic's arbitrary-rank edit on both writers of a window in the
middle of the model, with the search's selection visible.

- 35 of 1,013 tensors changed: the attention outputs of layers 6, 9 to 22 and 24 to 28 (20) and the dense down
  projections of 6, 8, 9, 11, 12, 15 and 19 to 27 (15). No expert, gate-up or router tensor moved. Twelve more
  tensors sit under the threshold, the largest the down projection of layer 7 at 0.000673, then layer 5's at
  0.000395 and layer 7's attention output at 0.000297, the search's footprint on the matrices it weighted low; the
  largest relative change outside the changed set is 0.000673.
- A few directions per matrix (first shares 0.904 to 0.970 on the attention outputs, 0.894 to 0.989 on the down
  projections; four shares 0.933 to 0.993), each writer its own direction (within-layer cosines 0.016 to 0.063 on
  the 13 shared layers).
- Input side on all 35: the right kept fraction runs from 0.58 down to minus 0.89 and the weight, one minus the
  right kept fraction, 0.42 to 1.78 on the attention outputs and 0.44 to 1.89 on the down projections, with layer 6
  partial on both writers (0.42 and 0.44) and the layer 25 attention output at 0.96. Rows moved 0.0007 to 0.0175 on
  the attention outputs and 0.003 to 0.027 on the down projections, unrestored, under no claim. Relative changes
  0.007 to 0.053.

| Layer | Attention output: change, E1, left kept, right kept | Down projection: change, E1, left kept, right kept | Within-layer cosine | Rows |
| --- | --- | --- | --- | --- |
| 6 | 0.0073, 0.932, 0.94, 0.58 | 0.0241, 0.959, 0.76, 0.56 | 0.061 | 0.0017, 0.0039 |
| 9 | 0.0352, 0.928, 0.77, -0.52 | 0.0347, 0.989, 0.86, -0.59 | 0.021 | 0.0075, 0.0030 |
| 12 | 0.0220, 0.924, 0.84, -0.41 | 0.0336, 0.972, 0.50, -0.56 | 0.051 | 0.0025, 0.0062 |
| 15 | 0.0232, 0.911, 0.90, -0.29 | 0.0340, 0.978, 0.69, -0.15 | 0.063 | 0.0030, 0.0042 |
| 19 | 0.0305, 0.924, 0.86, -0.23 | 0.0526, 0.894, 0.91, -0.79 | 0.020 | 0.0076, 0.0115 |
| 22 | 0.0338, 0.942, 0.50, -0.75 | 0.0393, 0.972, 0.94, -0.52 | 0.024 | 0.0036, 0.0062 |
| 25 | 0.0239, 0.963, 0.62, 0.04 | 0.0523, 0.955, 0.93, -0.89 | 0.016 | 0.0024, 0.0273 |
| 28 | 0.0154, 0.915, 0.94, -0.42 | - | - | 0.0011 |

The full table (35 rows) is in the report.

Directions. Against twenty-four saved vectors of 26B-A4B measurements, the leading directions stand at 0.98 and
0.97 (left and right medians) to llmfan46's instruct edit on 20 shared names and 0.98 and 0.98 to coder3101's on
18, the arbitrary-rank family of this base (finding 82); at 0.93 and 0.85 to coder3101's QAT edit and 0.93 and
0.90 to llmfan46's; at 0.75 and 0.93 to mewse's QAT edit; at 0.59 to OS-Software's Japanese export and 0.56 to the
maker's English v2; and at 0.22 or less to the kernel and projection edits (TrevorJS's, huihui-ai's, DuoNeural's,
xdavxd's, WWTCyberLab's). The second shard (`5c0b909c`) equals WWTCyberLab's second, the layout for the tensors
neither edit touches (finding 71); the first (`87b20ebd`) matches no measured file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home. The home judgement closed one field: the template, 16,934
bytes against the pin's 12,045, is byte-equal to Google's revision `4c55b528` of 04-28 ("fix(chat_template): update
SI and tool call handling"), which the later-revision check matches. What stays open is Unsloth's save (finding
15's shape): `tokenizer_config.json` names `<turn|>` (106) as the end-of-sequence token where the pin names
`<eos>` (1); the configuration's `eos_token_id` is 106 alone where the pin's is `[1, 106]`; `pad_token_id` is 0
where the pin leaves it unset, in the configuration and the special-token summary; and `generation_config.json`
still names `[1, 106, 50]`, so the copy's files disagree about where generation stops. The version strings
(5.5.0.dev0 to 5.6.0.dev0) are the re-save.

## For the recipe library

An arbitrary-rank entry (window, both writers, residues allowed, a few directions per matrix) would read the copy
as a clean match with twelve under-threshold matrices named; there is no card to match it against. The direction
vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus38/measurements/pair-1/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
