# Reading of the Stage 1 and Stage 2 result: llmfan46/gemma-4-12B-coder-fable5-composer2.5-v1-uncensored-heretic against yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1

Measured on Nautilus, round 46 piece 2 (download job 4184047, compare jobs 4184048 to 4184055 for the round's eight
pieces, sweep job 4184056; the pull, card 5854, carries the measurements and the sweep record and no job log, so the
node and the seconds are not recorded). Modified revision `513525a5`, created on 2026-06-21 at 21:30 and last
revised at 23:54. Parent pinned at `237e5d8e` (2026-06-18), the last commit before the copy was created. The copy's
`base_model` field names yuxinlu1's GGUF export of the fine-tune; the pinner paired it with the safetensors
repository the export was made from. yuxinlu1's coding fine-tune of google/gemma-4-12B-it already sits under five
makers' edits in the census (finding 127), richardyoung's Heretic pass among them (finding 18). The copy's own card
was not read in this pass. The parent counts as neither an original nor a copy (finding 117).

## Weights (Stage 2)

The tool's assessment was violations against `single-projection-selected`, 22 flags (20 direction cosines of 0.776
to 0.950, one first share of 0.9826 on the layer 44 attention output, one cross-kind cosine of 0.5058), with the
same assessment and nearest recipe on the cluster and after re-scoring at home. `directional-per-layer-selected`
reads 23, `single-projection` 33 and `directional-per-layer` 34. On reading, the copy is one shared direction on
both writers, from layer 3 on the attention outputs and layer 8 on the down projections to the last layer.

- 85 of 677 tensors changed: the attention outputs of layers 3 to 47 and the down projections of 8 to 47. The
  attention outputs of layers 0 to 2 and the down projections of 0 to 7 are exactly 0, as are the queries, keys,
  values, gates and up projections of all 48 layers, the 12 embeddings and the 289 norms. The largest change
  outside the changed set is 0.
- Relative changes: attention outputs 0.0130 to 0.0273, median 0.0169; down projections 0.0053 to 0.0245, median
  0.0174.
- One shared direction: 0.9671 to the group at the median on the attention outputs (0.8729 at the least) and 0.9884
  on the down projections (0.7764); between layers 0.9632 at the median (0.6963 at the least); the two writers of a
  layer at 0.9737 at the median over the 40 layers that carry both (0.7523 at the least). The 20 direction flags
  are the matrices furthest from the group: the attention outputs of layers 3 to 11, 14 to 16, 20, 21 and 29 and the
  down projections of 9 to 11, 19 and 47.
- First shares: one under the 0.99 floor (0.9826), the rest to 0.9999. No changed matrix keeps its row norms (0 of
  85).
- Every tensor pairs by name: none on one side only, no unused shared projection, no dropped tower or statistic.

| Kind | Changed | Layers | Exactly 0 | Relative change, least | Median | Most |
| --- | --- | --- | --- | --- | --- | --- |
| attention output | 45 of 48 | 3 to 47 | 3 | 0.0130 | 0.0169 | 0.0273 |
| down projection | 40 of 48 | 8 to 47 | 8 | 0.0053 | 0.0174 | 0.0245 |
| query, key, value | 0 of 136 | none | 136 | - | - | - |
| gate, up | 0 of 96 | none | 96 | - | - | - |

| Direction group | Matrices | Median cosine to the group | Least |
| --- | --- | --- | --- |
| attention outputs, width 3,840 | 45 | 0.9671 | 0.8729 |
| down projections, width 3,840 | 40 | 0.9884 | 0.7764 |
| between layers | 85 | 0.9632 | 0.6963 |

Against the other edits of the parent. The saved vectors were placed against the earlier measurements on this
fine-tune (finding 66's check). On the output side the copy stands at 0.957 at the median to tpls's abliteration
on the 59 matrices that edit moved (0.945 at the least; 0.945 on the input side), at 0.899 to richardyoung's Heretic
pass on their 52 shared names (0.875; 0.871 on the input side) and at 0.463 to huihui-ai's projection on its 12
(0.378 on the input side). To the same maker's pass on yuxinlu1's agentic fine-tune (pair 3) it stands at 0.963 on
67 shared names (0.958 on the input side). Of the four passes on this parent compared here, three land in one family at 0.90 to
0.96 and huihui-ai's stands apart, as finding 127 read on tpls's and huihui-ai's.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, 3 differences. Two are explained by re-save: the version
strings of `config.json` and `generation_config.json`, 5.10.2 to 5.12.1. The unexplained one is the template: the
copy's `default` source differs from the parent's beyond line endings and trailing whitespace (the parent's opens
with a `format_parameters` macro that takes a filter argument, the copy's with a `format_type_argument` macro), and
the fixed conversation renders the same with the `default` template.

## For the recipe library

The shared-direction kernel entry with a turn tolerance that round 44 asked for would read this pass; its 20
direction flags are the early attention outputs where the direction turns away from the group's. The direction
vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus46/measurements/pair-2/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
