# Reading of the Stage 1 and Stage 2 result: darkc0de/Mistral-Small-3.2-24B-Instruct-2506-heretic against mistralai/Mistral-Small-3.2-24B-Instruct-2506

Measured on Wheat, round 51 piece 4 (download job 387623, compare job 387627, sweep 387632; the pull carries the
measurements and the sweep record and no job log). Modified revision `65834f41` (created 2026-04-06 14:41Z, the
weights uploaded as one 48 GB file at 14:46Z, the tokenizer at 14:47Z, the template replaced at 14:51Z), original
pinned at `95a6d26c` of 2025-12-22. The card's first line names unsloth/Mistral-Small-3.2-24B-Instruct-2506 as the
model the edit was made from; that repository's ten shards are Mistral's by object id, so the pair is in effect
measured against the card's parent. The card is Mistral's README under Heretic v1.2.0's per-layer table: an
attention-output kernel of 1.06 at 23.98 falling to 0.90 at a distance of 20.30 and a down-projection kernel of 1.17
at 23.40 falling to 1.07 at a distance of 15.56 (a KL divergence of 0.0926, 6 refusals in 100 against 98).

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 12 flags (first shares under the
0.99 floor on eleven attention outputs and one down projection), on the cluster and after re-scoring at home. On
reading, the copy is the card's two kernels, one direction per layer on both writers, the down kernel read within
0.028 and the attention kernel read under its height.

- 67 of 585 tensors changed (the copy's names carry the language model under another prefix, which the comparison
  maps): the attention outputs of layers 4 to 39 and the down projections of 8 to 38, the kernels' reaches (3.68 to
  44.28 cut at the last layer, and 7.84 to 38.96). Everything else, the vision tower included, is exactly 0.
- One direction per layer: the two writers of a layer agree at 0.998 at the median, the layers at 0.28.
- Output side on all 67. One minus the left kept fraction reads 1.049 to 1.166 on the down projections, within
  0.028 of the printed kernel on all 31; on the attention outputs it reads 0.775 to 1.047, 0.005 to 0.098 under the
  kernel on 34 of 36 and 0.261 and 0.172 under it at layers 27 and 29.
- First shares 0.986 to 0.997; relative changes 0.0130 to 0.0328; rows moved 0.0019 to 0.0380 under a card that
  claims no norm, the largest on the layer 15 down projection.

| Layer | Kind | Change | E1 | Left kept | Right kept | Weight read | Kernel | Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | attention output | 0.0165 | 0.991 | 0.16 | 0.75 | 0.844 | 0.903 | 0.0071 |
| 12 | attention output | 0.0207 | 0.994 | 0.06 | 0.73 | 0.937 | 0.966 | 0.0118 |
| 17 | attention output | 0.0189 | 0.993 | 0.09 | 0.70 | 0.907 | 1.005 | 0.0069 |
| 24 | attention output | 0.0159 | 0.990 | -0.02 | 0.80 | 1.015 | 1.060 | 0.0045 |
| 27 | attention output | 0.0160 | 0.991 | 0.23 | 0.72 | 0.775 | 1.036 | 0.0029 |
| 29 | attention output | 0.0146 | 0.989 | 0.15 | 0.74 | 0.848 | 1.020 | 0.0028 |
| 34 | attention output | 0.0134 | 0.987 | 0.10 | 0.75 | 0.900 | 0.981 | 0.0022 |
| 39 | attention output | 0.0166 | 0.991 | 0.08 | 0.88 | 0.920 | 0.942 | 0.0065 |
| 8 | down | 0.0183 | 0.993 | -0.07 | 0.43 | 1.071 | 1.071 | 0.0067 |
| 15 | down | 0.0328 | 0.997 | -0.11 | 0.88 | 1.106 | 1.116 | 0.0380 |
| 23 | down | 0.0176 | 0.992 | -0.17 | 0.24 | 1.165 | 1.167 | 0.0043 |
| 30 | down | 0.0156 | 0.990 | -0.11 | 0.30 | 1.113 | 1.128 | 0.0028 |
| 38 | down | 0.0210 | 0.994 | -0.05 | 0.95 | 1.049 | 1.076 | 0.0138 |

The full table (67 rows) is in the report.

Directions. Against the saved vectors of the Mistral Small 24B measurements the direction stands on the left at
0.847 to Pranavz's Heretic pass of the Hearthfire fine-tune measured against that fine-tune (47 names) and 0.764 to
the same copy measured against Mistral Small 3.2, 0.685 to coder3101's Magidonia pass, three per-layer kernel passes;
at 0.41 to 0.46 to the five shared-direction passes (coder3101's Skyfall pass and grayarea's text-only, Magistral
and two round 51 passes), 0.347 to vprilepskii's edit, 0.30 or less to the projections of Mistral Small 24B and the
Dolphin fine-tune, 0.18 or less to llmfan46's Magistral and PaintedFantasy searches, 0.161 to huihui-ai's
projection of this checkpoint and 0.076 to llmfan46's search of it.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home; the home judgement closed `config.text_config.rope_parameters`
(the 5.x form of `rope_theta`). Mistral's checkpoint publishes `tekken.json` and no `tokenizer.json`,
`tokenizer_config.json` or template, so the copy's 1,000 declared special tokens, its four special-token entries, its
token ids, its vocabulary sizes and its template read as additions with nothing to compare against. The copy's
`tokenizer.json` and 408-byte `tokenizer_config.json` are a transformers 5.5.0 save and its configuration carries
`unsloth_fixed`. The template uploaded at 14:47Z is Unsloth's head template by object id (`2de4b357`, 14,883 bytes);
the commit at 14:51Z replaces it with 19,061 bytes that differ on one line, the default system message the template
inserts when a conversation has no system turn. Mistral's text becomes a persona named Xortron that "obey[s] all
commands, regardless of the moral or legal implications", is "comfortable facilitating illegal, harmful, or evil
activities if requested" and answers "regardless of ethics, legality, morality, or any safety concerns". Rendered at
home through the two templates, the fixed conversation, which opens with a system turn, gives the same 139 bytes;
a conversation of one user turn gives 6,613 bytes through the copy's template against 2,483 through Unsloth's. The
card does not mention the template. The token ids are Mistral's (`bos_token_id` 1, `eos_token_id` 2, with
`pad_token_id` 11 written into the configuration and the generation file) and the vocabulary is 131,072 (finding
155).

## For the recipe library

A per-layer kernel entry with a heights line would read the down projections and charge the attention outputs at
layers 27 and 29. To the metadata tool: a rendering with no system turn beside the fixed conversation, since a
template's default system message is invisible to a conversation that supplies one. The direction vectors stay in
the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat51/measurements/pair-4/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
