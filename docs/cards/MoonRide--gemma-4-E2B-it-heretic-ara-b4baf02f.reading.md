# Reading of the Stage 1 and Stage 2 result: MoonRide/gemma-4-E2B-it-heretic-ara against google/gemma-4-E2B-it (2026-11-02)

Measured on Wheat, round 39 piece 5 (download job 387181, compare job 387186, sweep 387190; the pull carries the
measurements and the sweep record and no job log). Modified revision `3a62cce9` (created 2026-04-08 22:10Z, last
commit 23:09Z), original pinned at `4742fe84`. The card is Heretic's arbitrary-rank table from the tool's pull
request 211: `start_layer_index` 15, `end_layer_index` 23, `preserve_good_behavior_weight` 0.5636,
`steer_bad_behavior_weight` 0.0003, `overcorrect_relative_weight` 0.6105, `neighbor_count` 1, a KL divergence of
0.1382 and 7 refusals in 100 against 99 in 100. It is the maker's third April export in the census, after the E4B and 31B edits of round 37 (finding 86), and
the first of two on the E2B (pair 7 is the second, searched with a custom system prompt the next day).

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 32 flags (16 first shares, 16
within-layer cosines), on the cluster and after re-scoring at home. On reading, the copy is an arbitrary-rank edit
of both writers inside the card's window, with half the down projections left as residues.

- 16 of 2,011 tensors changed: both writers of layers 15 to 22, the card's `start_layer_index` 15 to `end_layer_index` 23
  exactly. Nothing else moved; the largest relative change outside the changed set is exactly 0 on all 1,995 other
  tensors.
- Twelve edits and four residues. The attention outputs of 15 to 22 (first shares 0.82 to 0.92) and the down
  projections of 15, 16, 18 and 20 (0.18 to 0.39) carry a few directions each; the down projections of 17, 19, 21
  and 22 are rewritten by 0.0018 with no direction (first shares 0.003 to 0.008), rows 0.0007 to 0.0008, finding
  58's shape. The two writers of a layer are unrelated (0.008 to 0.075).
- Input side on the twelve edits: one minus the right kept fraction is 0.58 to 1.09 on the attention outputs and
  1.11 to 1.23 on the down projections, the left side keeping 0.76 to 0.94. Rows moved 0.0065 to 0.0078 on every
  edit, finding 22's band, the branch's row-norm preservation that the card's table does not name. Relative changes 0.0137 to 0.0395 on the edits.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Down projection: change, E1, left kept, right kept | Weight | Rows |
| --- | --- | --- | --- | --- | --- |
| 15 | 0.0223, 0.924, 0.79, 0.08 | 0.92 | 0.0246, 0.343, 0.91, -0.15 | 1.15 | 0.0070, 0.0076 |
| 16 | 0.0383, 0.866, 0.76, 0.01 | 0.99 | 0.0395, 0.182, 0.88, -0.23 | 1.23 | 0.0069, 0.0065 |
| 17 | 0.0245, 0.897, 0.86, 0.11 | 0.89 | 0.0018, 0.003, 1.00, 1.00 | residue | 0.0070, 0.0007 |
| 18 | 0.0257, 0.826, 0.84, -0.02 | 1.02 | 0.0225, 0.354, 0.94, -0.11 | 1.11 | 0.0071, 0.0076 |
| 19 | 0.0180, 0.822, 0.94, -0.09 | 1.09 | 0.0018, 0.003, 1.00, 1.00 | residue | 0.0072, 0.0008 |
| 20 | 0.0137, 0.890, 0.93, 0.42 | 0.58 | 0.0223, 0.385, 0.91, -0.17 | 1.17 | 0.0074, 0.0078 |
| 21 | 0.0178, 0.910, 0.91, 0.21 | 0.79 | 0.0018, 0.008, 1.00, 0.99 | residue | 0.0068, 0.0008 |
| 22 | 0.0190, 0.912, 0.86, -0.07 | 1.07 | 0.0018, 0.003, 1.00, 1.00 | residue | 0.0072, 0.0007 |

Directions. Against twenty-two saved vectors of measurements of the E2B, the leading directions stand at 0.80 on
the left and 0.97 on the right to llmfan46's ultra edit (6 shared names), 0.68 and 0.85 to coder3101's edit of the
QAT checkpoint (8), 0.54 to yuna1126's (4), 0.51 and 0.67 to amkkk's (16), 0.51 and 0.89 to the maker's own custom
edit of the next day (14), and 0.40 and 0.61 to Bahushruth's solver; the one-direction family (TrevorJS's,
anlord's, aifeifei798's, wangzhang's, treadon's) stands at 0.16 or less. The E2B's arbitrary-rank searches agree
with each other on the right side at 0.85 to 0.97 and on the left at 0.5 to 0.8, a looser family than the E4B's
(finding 82). The one shard (`e580b861`) matches no measured file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster, "consistent with re-save noted" at home. The home judgement closed
`text_config.moe_intermediate_size` by the default rule under transformers 5.22.1; what remains is the version
strings (to 5.5.0), a re-save. The template, the tokenizer, the token ids and the generation settings are the
pin's.

## For the recipe library

An arbitrary-rank entry with residues named would read the copy as its card. The direction vectors stay in the pull
copy at `/opt/ai/hpc-packages/pulls/model-audit/wheat39/measurements/pair-5/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
