# Reading of the Stage 1 and Stage 2 result: llmfan46/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-uncensored-heretic against yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2

Measured on Nautilus, round 46 piece 3 (download job 4184047, compare jobs 4184048 to 4184055 for the round's eight
pieces, sweep job 4184056; the pull, card 5854, carries the measurements and the sweep record and no job log, so the
node and the seconds are not recorded). Modified revision `76e6ccb3`, created on 2026-06-30 at 18:04 and last
revised at 18:33. Parent pinned at `af644ab1` (2026-06-30 at 01:18), seventeen hours before the copy. The copy's
`base_model` field names yuxinlu1's GGUF export of the fine-tune; the pinner paired it with the safetensors
repository. yuxinlu1's agentic fine-tune of google/gemma-4-12B-it is the parent of huihui-ai's projection (finding
128). The copy's own card was not read in this pass. The parent counts as neither an original nor a copy (finding
117).

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 7 flags (six within-layer direction
cosines of 0.792 to 0.932 on the two writers of layers 38, 44 and 47, one first share of 0.9878 on the layer 44
attention output), with the same assessment and nearest recipe on the cluster and after re-scoring at home.
`single-projection-selected` reads 9, `directional-per-layer` 36 and `single-projection` 38. On reading, the copy is
one shared direction on both writers, from layer 9 on the attention outputs and layer 20 on the down projections to
the last layer, the form of the same maker's pass on the coding fine-tune (pair 2) with a shorter reach.

- 67 of 677 tensors changed: the attention outputs of layers 9 to 47 and the down projections of 20 to 47. The
  attention outputs of layers 0 to 8 and the down projections of 0 to 19 are exactly 0, as are the queries, keys,
  values, gates and up projections of all 48 layers, the 12 embeddings and the 289 norms. The largest change
  outside the changed set is 0.
- Relative changes: attention outputs 0.0136 to 0.0286, median 0.0221; down projections 0.0228 to 0.0298, median
  0.0258, higher than on pair 2 (0.0169 and 0.0174).
- One shared direction: 0.9758 to the group at the median on the attention outputs (0.8785 at the least) and 0.9905
  on the down projections (0.9573); between layers 0.9738 at the median (0.6359 at the least); the two writers of a
  layer at 0.9865 at the median over the 28 layers that carry both (0.7925 at the least, layer 44).
- First shares: one under the 0.99 floor (0.9878), the rest to 0.9999. No changed matrix keeps its row norms (0 of
  67).
- Every tensor pairs by name: none on one side only, no unused shared projection, no dropped tower or statistic.

| Kind | Changed | Layers | Exactly 0 | Relative change, least | Median | Most |
| --- | --- | --- | --- | --- | --- | --- |
| attention output | 39 of 48 | 9 to 47 | 9 | 0.0136 | 0.0221 | 0.0286 |
| down projection | 28 of 48 | 20 to 47 | 20 | 0.0228 | 0.0258 | 0.0298 |
| query, key, value | 0 of 136 | none | 136 | - | - | - |
| gate, up | 0 of 96 | none | 96 | - | - | - |

| Direction group | Matrices | Median cosine to the group | Least |
| --- | --- | --- | --- |
| attention outputs, width 3,840 | 39 | 0.9758 | 0.8785 |
| down projections, width 3,840 | 28 | 0.9905 | 0.9573 |
| between layers | 67 | 0.9738 | 0.6359 |

Against other measurements. The saved vectors were placed against the earlier measurements on yuxinlu1's two
fine-tunes (finding 66's check). On the output side the copy stands at 0.963 at the median to the maker's pass on
the coding fine-tune on 67 shared names (0.956 at the least; 0.958 on the input side), at 0.897 to tpls's
abliteration of the coding fine-tune on 48 of its edited names and 0.811 to richardyoung's Heretic pass of it on
52, and at 0.403 to huihui-ai's projection of this same parent on its 12 matrices (0.359 on the input side). The
maker's direction holds across the two fine-tunes at 0.96, as huihui-ai's does on the same two parents, where its
projections carry the maker's Google 12B direction at 1.000 and 0.978 (finding 128); the two makers' directions
stand at 0.40 to 0.46 to each other on both.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, 3 differences. Two are explained by re-save: the version
strings of `config.json` and `generation_config.json`, 5.10.2 to 5.12.1, the same move as on pair 2. The
unexplained one is the template, which differs from the parent's beyond line endings and trailing whitespace in
the same way as pair 2's (a `format_type_argument` macro where the parent opens with `format_parameters`); the fixed
conversation renders the same with the `default` template.

## For the recipe library

As on pair 2, a shared-direction entry with a turn tolerance would read the pass; here the flags fall on the two
writers of three late layers, where they part to 0.79 to 0.93 within the layer. The direction vectors stay in the
pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus46/measurements/pair-3/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
