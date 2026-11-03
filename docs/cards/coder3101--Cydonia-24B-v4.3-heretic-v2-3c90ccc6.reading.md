# Reading of the Stage 1 and Stage 2 result: coder3101/Cydonia-24B-v4.3-heretic-v2 against TheDrummer/Cydonia-24B-v4.3

Measured on Nautilus, round 44 piece 2 (sweep job 4180457; the pull, card 5853, carries the measurements and the
sweep record and no job log, so the download and compare job ids, the node and the seconds are not recorded).
Modified revision `4e48125d`, created on 2025-12-20 at 19:00, four minutes after the maker's first pass of the same
parent (pair 1), and last revised on 2025-12-21 at 19:11, a minute after it. Parent pinned at `db0426d3`
(2025-12-17), the revision the first pass is measured against. TheDrummer's Cydonia v4.3 is a fine-tune whose field
names mistralai/Mistral-Small-3.2-24B-Instruct-2506, with the 40 layers and the 5,120 width of Mistral Small. The
copy's own card was not read in this pass. The parent counts as neither an original nor a copy (finding 117).

## Weights (Stage 2)

The tool's assessment was violations against `single-projection-selected`, 41 flags (first shares of 0.756 to
0.990 under the 0.99 floor), with the same assessment and nearest recipe on the cluster and after re-scoring at home.
`directional-per-layer-selected` reads the same 41; `single-projection` and `directional-per-layer` read 64 each. On
reading, the copy is one direction applied to both writers across the reach of the pass.

- 57 of 363 tensors changed: the attention outputs of layers 7 to 39 and the down projections of layers 16 to 39,
  each run unbroken to the last layer. The attention outputs of layers 0 to 6 and 15 of the down projections are
  exactly 0, as are the queries, keys, values, gates and up projections of all 40 layers, the embedding and the 81
  norms.
- The one down projection left between, among layers 0 to 15, moved by 0.0005995 of its norm, under the 0.001
  threshold: the largest change outside the changed set, below the down edit's reach.
- Relative changes 0.0119 to 0.0165 on the attention outputs (median 0.0137) and 0.0016 to 0.0192 on the down
  projections (median 0.0111).
- One direction for all 57: 1.0000 at the median to each group's direction, 0.9861 at the least, 0.9853 across the two
  kinds. Between layers 0.99999 at the median and 0.9963 at the least; within the 24 layers that carry both writers
  0.99998 at the median and 0.9855 at the least.
- First shares: the least is 0.7564, and 41 of the 57 sit under the 0.99 floor. No changed matrix keeps its row norms
  (0 of 33, 0 of 24).
- Every tensor pairs by name: none on one side only, no unused shared projection, no dropped tower or statistic.

| Kind | Changed | Layers | Exactly 0 | Relative change, least | Median | Most |
| --- | --- | --- | --- | --- | --- | --- |
| attention output | 33 of 40 | 7 to 39 | 7 | 0.0119 | 0.0137 | 0.0165 |
| down projection | 24 of 40 | 16 to 39 | 15 | 0.0016 | 0.0111 | 0.0192 |
| query, key, value, gate, up | 0 of 200 | none | 200 | - | - | - |

| Direction group | Matrices | Median cosine to the group | Least |
| --- | --- | --- | --- |
| attention outputs, width 5,120 | 33 | 1.0000 | 1.0000 |
| down projections, width 5,120 | 24 | 1.0000 | 0.9861 |
| across the two kinds | 57 | 1.0000 | 0.9853 |

Against pair 1, made four minutes earlier on the same parent, the pass reaches further on the attention outputs (7
to 39 against 24 to 29) and less far on the down projections (16 to 39 against 9 to 39), and it trades one direction
per layer (0.457 between layers) for one shared direction (0.99999). The same maker's two Magidonia passes, six
minutes apart, made the same move (findings 144 and 160), and that parent's second pass reached the attention
outputs of layers 8 to 39 and the down projections of 28 to 39.

Directions. The saved vectors were not placed against earlier measurements in this pass; the comparison with pair 1
layer by layer (where finding 160 found the Magidonia shared direction between the first pass's layer 23 and 24
directions), with pairs 3 and 4, with the maker's Magidonia and Mistral Small 3.2 passes and with the other Mistral
Small 24B measurements is owed (finding 66's check).

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home, with two differences: the version strings of
`config.json` and `generation_config.json` move from 4.57.1 to 4.57.3, as on pair 1 and on the maker's second
Magidonia pass. No other compared field differs, and the fixed conversation renders the same with the `default`
template. The home judgement under transformers 5.22.1 changed no field.

## For the recipe library

A shared-direction kernel entry with a heights line would read both reaches from the card's table; the two
`-selected` entries tie at 41 flags, all of them first shares, on a pass whose smallest down change is 0.0016
of the weight. The single trace below the down reach belongs in the copy's small-outside
line. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus44/measurements/pair-2/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
