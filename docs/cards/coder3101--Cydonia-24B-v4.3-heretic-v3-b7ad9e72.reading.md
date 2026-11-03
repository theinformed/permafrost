# Reading of the Stage 1 and Stage 2 result: coder3101/Cydonia-24B-v4.3-heretic-v3 against TheDrummer/Cydonia-24B-v4.3

Measured on Nautilus, round 44 piece 3 (sweep job 4180457; the pull, card 5853, carries the measurements and the
sweep record and no job log, so the download and compare job ids, the node and the seconds are not recorded).
Modified revision `b910f843`, created on 2026-02-15 at 13:30, eight weeks after the maker's first two passes of the
same parent (pairs 1 and 2) and six minutes before its fourth (pair 4); last revised at 13:35 the same day. Parent
pinned at `db0426d3` (2025-12-17), the revision all four passes are measured against. TheDrummer's Cydonia v4.3 is a
fine-tune whose field names mistralai/Mistral-Small-3.2-24B-Instruct-2506, with the 40 layers and the 5,120 width of
Mistral Small. The copy's own card was not read in this pass. The parent counts as neither an original nor a copy
(finding 117).

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 55 flags (first shares of 0.961 to
0.990 under the 0.99 floor), with the same assessment and nearest recipe on the cluster and after re-scoring at home.
`single-projection-selected` reads 56, `directional-per-layer` 61 and `single-projection` 62. On reading, the copy is
a nearly shared direction on both writers of layers 3 to 39, the widest reach of the maker's four passes.

- 74 of 363 tensors changed: the attention outputs and the down projections of layers 3 to 39, both runs unbroken
  to the last layer. Layers 0 to 2 are exactly 0 on both writers, as are the queries, keys, values, gates and up
  projections of all 40 layers, the embedding and the 81 norms. The largest change outside the changed set is 0.
- Relative changes 0.0071 to 0.0150 on the attention outputs (median 0.0107) and 0.0103 to 0.0200 on the down
  projections (median 0.0155).
- One direction, nearly: 0.9978 and 0.9988 at the median to the two groups' directions, 0.9728 and 0.9912 at the
  least, 0.9382 across the two kinds. Between layers 0.9972 at the median and 0.9834 at the least; within the 37
  layers that carry both writers 0.9966 at the median and 0.9554 at the least. Pair 2 reads 0.99999 between layers,
  so this pass's direction moves from layer to layer by a small, measured amount that pair 2's does not.
- First shares: the least is 0.9614, the highest floor of the four passes, and 55 of the 74 still sit under 0.99.
  No changed matrix keeps its row norms (0 of 37, 0 of 37).
- Every tensor pairs by name: none on one side only, no unused shared projection, no dropped tower or statistic.

| Kind | Changed | Layers | Exactly 0 | Relative change, least | Median | Most |
| --- | --- | --- | --- | --- | --- | --- |
| attention output | 37 of 40 | 3 to 39 | 3 | 0.0071 | 0.0107 | 0.0150 |
| down projection | 37 of 40 | 3 to 39 | 3 | 0.0103 | 0.0155 | 0.0200 |
| query, key, value, gate, up | 0 of 200 | none | 200 | - | - | - |

| Direction group | Matrices | Median cosine to the group | Least |
| --- | --- | --- | --- |
| attention outputs, width 5,120 | 37 | 0.9978 | 0.9728 |
| down projections, width 5,120 | 37 | 0.9988 | 0.9912 |
| across the two kinds | 74 | 0.9985 | 0.9382 |

Against the maker's December passes, this one starts both writers at layer 3, where pair 1 started its down edit at
9 and pair 2 its attention edit at 7, and it is the only one of the four whose two reaches begin on the same layer.
Its flags (55) are first shares on a pass where every first share is at least 0.961, so the count grows with the
changed set (74 matrices) more than with any departure from rank one.

Directions. The saved vectors were not placed against earlier measurements in this pass; the comparison with pairs 1,
2 and 4, with the maker's Magidonia and Mistral Small 3.2 passes and with the other Mistral Small 24B measurements is
owed (finding 66's check). Whether the small turn between layers (0.9972) is an interpolated index, an orthogonalised
direction or a per-layer setting is for the card's table to say.

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home, with two differences: the version strings of
`config.json` and `generation_config.json` move from 4.57.1 to 4.57.6, where the December passes saved under 4.57.3.
No other compared field differs, and the fixed conversation renders the same with the `default` template. The home
judgement under transformers 5.22.1 changed no field.

## For the recipe library

A shared-direction kernel entry with a heights line, and a tolerance for a direction that turns by 0.003 at the
median between layers, would read this pass; the floor charges 55 first shares of 0.961 to 0.990, the case round 52
read on the maker's other passes as bfloat16 storage of small edits; the leftover line is owed for this one. The
direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus44/measurements/pair-3/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
