# Reading of the Stage 1 and Stage 2 result: coder3101/gemma-4-26B-A4B-it-qat-q4_0-unquantized-heretic against google/gemma-4-26B-A4B-it-qat-q4_0-unquantized (2026-11-02)

Measured on Nautilus, round 36 piece 3 (download job 4167620, compare job 4167623, sweep 4167629; the pull carries
the measurements and the sweep record and no job log). Modified revision `2b4cfd85` (five commits on 2026-06-06
between 18:23Z and 18:27Z: the model, tokenizer and README, then a README edit), original pinned at `641f1844`
(06-05, the release commit of the QAT-unquantized 26B-A4B checkpoint). The card (29,531 bytes, the tool's page)
says Heretic v1.2.0's arbitrary-rank ablation with row-norm preservation: `start_layer_index` 12,
`end_layer_index` 21, `preserve_good_behavior_weight` 0.3106, `steer_bad_behavior_weight` 0.0066,
`overcorrect_relative_weight` 0.7982, `neighbor_count` 14, no targeted component printed, KL divergence 0.0660, 13
refusals in 100 against 100. The `base_model` field names the QAT checkpoint. The maker's ninth copy in the
census and the fifth on a QAT checkpoint; the maker's instruct 26B-A4B edit was measured in round 12.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 9 flags (all
first shares, 0.444 to 0.955), on the cluster and after re-scoring at home. On reading, the copy is the card
exactly.

- 9 of 1,013 tensors changed: the attention outputs of layers 12 to 20, the card's window with its exclusive
  end, every layer of it. No expert, router, shared down projection or tower tensor moved; the largest relative
  change outside the changed set is exactly 0 and 1,004 tensors equal the original, which places the copy on the
  QAT checkpoint (finding 48).
- A few directions per matrix, spread as on the maker's instruct 26B-A4B edit: first shares 0.444 to 0.955
  (0.444 at layer 19, 0.53 at 16), fourth cumulative shares 0.834 to 0.972.
- Input side on all 9 (left kept 0.67 to 0.97, right kept negative on every matrix). Read as weights, one minus
  the right kept fraction, 1.06 to 1.81 (median 1.56), 1.81 at layer 20 and 1.06 at 18.
- Rows moved 0.0067 to 0.0077 on all 9, finding 22's band on every one, under the card's preservation claim.
- A direction per matrix: 0.18 to 0.52 to the group reference.

| Layer | Change | E1 | E4 | Left kept | Right kept | Weight read | Rows |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 12 | 0.0248 | 0.931 | 0.963 | 0.85 | -0.72 | 1.72 | 0.0071 |
| 13 | 0.0266 | 0.942 | 0.966 | 0.86 | -0.51 | 1.51 | 0.0076 |
| 14 | 0.0243 | 0.952 | 0.969 | 0.81 | -0.59 | 1.59 | 0.0072 |
| 15 | 0.0241 | 0.919 | 0.952 | 0.89 | -0.56 | 1.56 | 0.0074 |
| 16 | 0.0368 | 0.530 | 0.863 | 0.67 | -0.45 | 1.45 | 0.0068 |
| 17 | 0.0219 | 0.948 | 0.963 | 0.97 | -0.60 | 1.60 | 0.0077 |
| 18 | 0.0241 | 0.955 | 0.972 | 0.83 | -0.06 | 1.06 | 0.0077 |
| 19 | 0.0431 | 0.444 | 0.834 | 0.82 | -0.36 | 1.36 | 0.0067 |
| 20 | 0.0469 | 0.954 | 0.967 | 0.91 | -0.81 | 1.81 | 0.0073 |

Directions. Against the saved vectors of twenty-two 26B-A4B measurements on the 9 names, the leading directions
stand at 0.991 on the left and 0.900 on the right to llmfan46's QAT edit of the same checkpoint (round 34), at
0.945 and 0.881 to llmfan46's instruct 26B-A4B edit, at 0.936 and 0.881 to the maker's own instruct edit, at
0.928 and 0.854 to SassyDiffusion's, at 0.86 and 0.83 to mewse's QAT edit, at 0.70 and 0.65 to OS-Software's
Japanese-prompt export, at 0.54 and 0.58 to OS-Software's rank-four export and at 0.19 or less to every kernel
and projection edit: the 26B-A4B arbitrary-rank family, the maker's QAT edit on the maker's instruct direction
(findings 72 and 89). The two shards equal no measured file.

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home: the two version strings (5.6.2 to 5.10.0.dev0) and
nothing else; the template is the pin's and renders identically.

## For the recipe library

The directional-per-layer entry is the nearest and its 9 flags are the few directions per matrix; an
arbitrary-rank entry with the card's window would read the copy as a clean match. The direction vectors stay in
the pull copy at `/opt/ai/hpc-packages/pulls/model-audit/nautilus36/measurements/pair-3/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
