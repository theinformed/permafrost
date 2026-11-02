# Reading of the Stage 1 and Stage 2 result: DuoNeural/Gemma-4-E2B-Heretic against google/gemma-4-E2B-it (2026-11-02)

Measured on Nautilus, round 38 piece 6 (download job 4168771, compare job 4168777, sweep 4168780; the pull carries
the measurements and the sweep record and no job log). Modified revision `39221ce2` (seven commits from 2026-05-01
to 06-08, one of them on 05-31 "Fix Heretic v1.2.0 (not v2), add shared-KV missing key note"), original pinned at
`6b7e72c6`. The card (3,112 bytes) says Heretic's LoRA Pareto sweep chose trial 89 with the targets `o_proj` and
`down_proj`, "42 layers each", a KL divergence of 0.0571 and 85 percent compliance; the E2B has 35 layers. It prints
no kernel, weight or window. The repository ships no `chat_template.jinja`.

## Weights (Stage 2)

The tool's assessment was a clean match of `single-projection-selected`, 0 flags, on the cluster and after
re-scoring at home, one of the few copies in the census the recipe table reads without a flag. On reading, the
copy is one direction projected at a kernel-shaped weight from both writers of a window.

- 49 of 1,951 tensors changed: the down projections of layers 6 to 34 (29) and the attention outputs of 15 to 34
  (20). Nothing else moved; the largest relative change outside the changed set is exactly 0. The 60
  shared-key-value tensors are absent from the save, as the maker's commit says.
- One direction for the model: the group cosines are 1.0 on every matrix, the two writers of a layer agree at 1.0
  and the two kinds across the model at 0.99998. First shares 0.994 to 0.998.
- Output side on all 49, with a readable weight: one minus the left kept fraction runs 0.75 at layer 6, rising to
  1.43 at layer 21 and falling to 0.83 at 34 on the down projections, and 1.03 at layer 15 rising to 1.32 at 34 on
  the attention outputs; the right side keeps 0.23 to 0.77 on the attention outputs and minus 0.01 to 0.69 on the
  down projections, near 0 on layers 20 to 22 and 25. Two kernels the card does not print, finding 46's weights
  readable where the 12B passes read none. Rows moved 0.0059 to 0.0207 on the down projections and 0.0069 to
  0.040 on the attention outputs, unrestored, under no claim. Relative changes 0.019 to 0.036.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Down projection: change, E1, left kept, right kept | Weight | Rows |
| --- | --- | --- | --- | --- | --- |
| 6 | - | - | 0.0194, 0.994, 0.25, 0.55 | 0.75 | 0.0125 |
| 10 | - | - | 0.0241, 0.996, 0.06, 0.63 | 0.94 | 0.0154 |
| 15 | 0.0266, 0.997, -0.03, 0.59 | 1.03 | 0.0314, 0.997, -0.17, 0.42 | 1.17 | 0.0170, 0.0177 |
| 20 | 0.0275, 0.997, -0.10, 0.58 | 1.10 | 0.0358, 0.998, -0.40, -0.00 | 1.40 | 0.0132, 0.0172 |
| 25 | 0.0296, 0.997, -0.18, 0.56 | 1.18 | 0.0316, 0.997, -0.25, -0.00 | 1.25 | 0.0106, 0.0122 |
| 30 | 0.0333, 0.998, -0.26, 0.77 | 1.26 | 0.0257, 0.996, -0.02, 0.19 | 1.02 | 0.0127, 0.0115 |
| 34 | 0.0346, 0.998, -0.32, 0.36 | 1.32 | 0.0214, 0.995, 0.17, 0.40 | 0.83 | 0.0400, 0.0106 |

The full table (49 rows) is in the report.

Directions. Against twenty-two saved vectors of measurements of the E2B, the direction stands at 0.925 on both sides to
huihui-ai's E2B edit on all 45 shared names, and with it to Dzluck's second-version re-upload and prithivMLmods's
re-save, the same number on every matrix because both edits carry one direction for the model; the two
mean-difference directions found by two makers on this base meet at 22 degrees. Every other E2B edit stands at
0.08 or less (TrevorJS's, Bahushruth's, MoonRide's, amkkk's, llmfan46's, coder3101's QAT edit). The first two
shards (`9ebcea19`, `b07560fd`) are the E2B library layout shared with huihui-ai's, amkkk's, anlord's,
aifeifei798's and prithivMLmods's exports (finding 71); the third (`f8668ec0`) matches no measured file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home. The home judgement closed `text_config.moe_intermediate_size`
by the default rule under transformers 5.22.1, and the version strings (5.5.0.dev0 to 5.7.0) are a re-save. What
stays open is the template: the repository ships no `chat_template.jinja` and `tokenizer_config.json` carries
none, so a loader applies whatever template it has by default and the fixed conversation cannot be rendered from
the copy's files. The generation configuration is the pin's with its version string.

## For the recipe library

The single-projection entry with selection reads the copy exactly; a kernel line would print the two weight
curves beside it. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus38/measurements/pair-6/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
