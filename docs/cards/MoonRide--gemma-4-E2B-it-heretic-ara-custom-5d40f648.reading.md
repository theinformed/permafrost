# Reading of the Stage 1 and Stage 2 result: MoonRide/gemma-4-E2B-it-heretic-ara-custom against google/gemma-4-E2B-it (2026-11-02)

Measured on Wheat, round 39 piece 7 (download job 387181, compare job 387188, sweep 387190; the pull carries the
measurements and the sweep record and no job log). Modified revision `f607231b` (created 2026-04-09 17:45Z, last
commit 18:55Z, the day after the maker's first E2B export of pair 5), original pinned at `4742fe84`. The card is
Heretic's arbitrary-rank table from the tool's pull request 211 with one line added, "Created and evaluated using
custom system prompt": `start_layer_index` 16, `end_layer_index` 35, `preserve_good_behavior_weight` 0.7603,
`steer_bad_behavior_weight` 0.0002, `overcorrect_relative_weight` 0.3310, `neighbor_count` 7, a KL divergence of
0.0191 and 4 refusals in 100 against 99 in 100.

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 76 flags (38 first shares, 38
within-layer cosines), on the cluster and after re-scoring at home. On reading, the copy is an arbitrary-rank edit
of both writers across the card's window of nineteen layers, with three matrices left as residues and two edited
lightly.

- 38 of 2,011 tensors changed: both writers of layers 16 to 34, the card's `start_layer_index` 16 to
  `end_layer_index` 35 exactly. Nothing else moved; the largest relative change outside the changed set is exactly
  0 on all 1,973 other tensors.
- Thirty-five edits and three residues. The attention outputs carry first shares 0.82 to 0.94 and the down
  projections 0.11 to 0.87, a few directions each; the layer 29 attention output (0.0013, first share 0.049) and
  both writers of layer 31 (0.0017 and 0.0018, first shares 0.005 and 0.003) are rewritten without a direction,
  rows 0.0007 to 0.0009, finding 58's shape; the attention outputs of 32 and 34 are edited lightly (0.0038 and
  0.0046, first shares 0.74 and 0.87). The two writers of a layer are unrelated (0.001 to 0.125).
- Input side on the edits: one minus the right kept fraction is 0.18 to 1.13 on the attention outputs and 0.97 to
  1.30 on the down projections, the left side keeping 0.72 to 0.99. Rows moved 0.0060 to 0.0078 on every edit,
  finding 22's band, the branch's row-norm preservation that the card's table does not name. Relative changes
  0.0038 to 0.0485 on the edits.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Down projection: change, E1, left kept, right kept | Weight | Rows |
| --- | --- | --- | --- | --- | --- |
| 16 | 0.0327, 0.895, 0.72, -0.03 | 1.03 | 0.0179, 0.577, 0.88, -0.20 | 1.20 | 0.0071, 0.0065 |
| 19 | 0.0139, 0.830, 0.93, 0.07 | 0.93 | 0.0155, 0.724, 0.89, -0.16 | 1.16 | 0.0072, 0.0072 |
| 22 | 0.0170, 0.885, 0.87, 0.15 | 0.85 | 0.0128, 0.866, 0.90, -0.11 | 1.11 | 0.0068, 0.0067 |
| 25 | 0.0303, 0.927, 0.78, -0.02 | 1.02 | 0.0134, 0.822, 0.88, -0.18 | 1.18 | 0.0070, 0.0069 |
| 26 | 0.0085, 0.912, 0.95, 0.56 | 0.45 | 0.0143, 0.792, 0.90, 0.04 | 0.97 | 0.0061, 0.0069 |
| 29 | 0.0013, 0.049, 1.00, 1.00 | residue | 0.0253, 0.271, 0.96, 0.03 | 0.97 | 0.0007, 0.0074 |
| 31 | 0.0017, 0.005, 1.00, 1.00 | residue | 0.0018, 0.003, 1.00, 1.00 | residue | 0.0009, 0.0007 |
| 32 | 0.0038, 0.741, 0.99, 0.69 | 0.31 | 0.0485, 0.113, 0.96, -0.30 | 1.30 | 0.0060, 0.0069 |
| 34 | 0.0046, 0.869, 0.99, 0.82 | 0.18 | 0.0136, 0.812, 0.98, -0.25 | 1.25 | 0.0059, 0.0067 |

The full table (38 rows) is in the report.

Directions. Against twenty-two saved vectors of measurements of the E2B, the leading directions stand at 0.87 on
the left and 0.89 on the right to coder3101's edit of the QAT checkpoint (8 shared names), 0.85 and 0.96 to
llmfan46's ultra edit (7), 0.70 to yuna1126's (3), 0.68 and 0.70 to amkkk's (36), 0.61 and 0.64 to Bahushruth's
solver (18), 0.51 and 0.89 to the maker's own export of the day before (14) and 0.49 to anlord's; the one-direction
family (aifeifei798's, TrevorJS's, treadon's, wangzhang's) stands at 0.27 or less. The custom system prompt moved
the search's result: the two exports of one maker on one base a day apart agree at 0.51 on the left, where the
E4B's arbitrary-rank searches agree at 0.9 and better (finding 82). The one shard (`f0a9cf99`) matches no measured
file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster, "consistent with re-save noted" at home. The home judgement closed
`text_config.moe_intermediate_size` by the default rule under transformers 5.22.1; what remains is the version
strings (to 5.5.1), a re-save. The template (12,188 bytes), the tokenizer, the token ids and the generation
settings are the pin's.

## For the recipe library

An arbitrary-rank entry with residues named would read the copy as its card. The direction vectors stay in the pull
copy at `/opt/ai/hpc-packages/pulls/model-audit/wheat39/measurements/pair-7/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
