# Reading of the Stage 1 and Stage 2 result: tpls/gemma-4-12B-coder-fable5-composer2.5-v1-sft-v5-abliterated against tpls/gemma-4-12B-coder-fable5-composer2.5-v1-sft-v5

Measured on Nautilus, round 46 piece 4 (download job 4184047, compare jobs 4184048 to 4184055 for the round's eight
pieces, sweep job 4184056; the pull, card 5854, carries the measurements and the sweep record and no job log, so the
node and the seconds are not recorded). Modified revision `0b752c7b`, created on 2026-06-26 at 00:00 and last
revised at 13:58. Parent pinned at `3cd205a2` (2026-06-25 at 16:18), the last of the parent's fourteen commits
before the copy was created. The parent is tpls's own fine-tune of yuxinlu1's coding fine-tune of Gemma 4 12B (its
field names yuxinlu1's), new to the census; tpls's abliteration of yuxinlu1's fine-tune itself was measured in
round 45 (finding 127). The copy's own card was not read in this pass. The parent counts as neither an original nor
a copy (finding 117).

## Weights (Stage 2)

The tool's assessment was violations against `single-projection-selected`, 6 flags (first shares of 0.971 to 0.989
on the down projections of layers 39 to 42 and the attention outputs of 45 and 46, under the 0.99 floor), with the
same assessment and nearest recipe on the cluster and after re-scoring at home. `directional-per-layer-selected`
also reads 6, `single-projection` 95 and `directional-per-layer` 95. On reading, the copy is one direction on seven
late matrices, a direction none of the measured edits of the coding fine-tune carries.

- 7 of 677 tensors changed: the down projections of layers 39 to 42 and the attention outputs of 45 to 47. Layers
  43 and 44 are exactly 0 on both writers, as are the queries, keys, values, gates and up projections of all 48
  layers, the 12 embeddings and the 289 norms. The largest change outside the changed set is 0.
- Relative changes: down projections 0.0062 to 0.0069, median 0.0065; attention outputs 0.0093, 0.0115 and 0.0131
  on layers 45, 46 and 47, rising to the last layer.
- One direction: 0.9938 to the group at the median on the down projections (0.9900 at the least) and 0.9955 on the
  attention outputs (0.9735); between layers 0.9837 at the median (0.9531 at the least); the cross-kind least
  0.9531. No layer carries two edits.
- First shares 0.9707 to 0.9905; six of seven under the floor. No changed matrix keeps its row norms (0 of 7).
- Every tensor pairs by name: none on one side only, no unused shared projection, no dropped tower or statistic.

| Kind | Changed | Layers | Exactly 0 | Relative change, least | Median | Most |
| --- | --- | --- | --- | --- | --- | --- |
| attention output | 3 of 48 | 45 to 47 | 45 | 0.0093 | 0.0115 | 0.0131 |
| down projection | 4 of 48 | 39 to 42 | 44 | 0.0062 | 0.0065 | 0.0069 |
| query, key, value | 0 of 136 | none | 136 | - | - | - |
| gate, up | 0 of 96 | none | 96 | - | - | - |

| Direction group | Matrices | Median cosine to the group | Least |
| --- | --- | --- | --- |
| attention outputs, width 3,840 | 3 | 0.9955 | 0.9735 |
| down projections, width 3,840 | 4 | 0.9938 | 0.9900 |
| between layers | 7 | 0.9837 | 0.9531 |

Against the edits of the grandparent. The saved vectors were placed against the earlier measurements on yuxinlu1's
coding fine-tune (finding 66's check). On the seven shared names the copy stands on the output side at 0.048 at the
median to the maker's own abliteration of that fine-tune (0.063 at the most), 0.059 to richardyoung's Heretic pass
and 0.052 to llmfan46's pass (pair 2), and at 0.064, 0.110 and 0.078 on the input side; huihui-ai's projection
shares no name with it. Those three stand at 0.90 to 0.96 to one another on the same fine-tune. The maker's second
edit, one training later, is not the maker's first direction.

## Token and configuration side (Stage 1)

"Undecided" on the cluster and at home, 2 differences, both explained by re-save: the version strings of
`config.json` and `generation_config.json`, from the parent's 5.13.0.dev0 to the copy's 5.12.1, an earlier release
than the parent's development build. The template fails to render on both sides (an unknown `generation` tag), so
the fixed conversation is not compared.

## For the recipe library

The selected entries read the pass at 6 flags each, all first shares between 0.971 and 0.989 on matrices moved by
0.006 to 0.013 of their norm. A first-share floor read against the size of the change would separate a small
selected pass from a pass that leaves a second component. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus46/measurements/pair-4/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
