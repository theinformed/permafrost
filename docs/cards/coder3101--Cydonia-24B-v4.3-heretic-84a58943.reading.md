# Reading of the Stage 1 and Stage 2 result: coder3101/Cydonia-24B-v4.3-heretic against TheDrummer/Cydonia-24B-v4.3

Measured on Nautilus, round 44 piece 1 (sweep job 4180457; the pull, card 5853, carries the measurements and the
sweep record and no job log, so the download and compare job ids, the node and the seconds are not recorded).
Modified revision `8f537a2d`, created on 2025-12-20 at 18:56, four minutes before the maker's second pass of the same
parent (pair 2), and last revised on 2025-12-21 at 19:10, a minute before that pass. Parent pinned at `db0426d3`
(2025-12-17), the latest commit at or before the copy's creation. TheDrummer's Cydonia v4.3 is a fine-tune whose field
names mistralai/Mistral-Small-3.2-24B-Instruct-2506, with the 40 layers and the 5,120 width of Mistral Small. The
copy's own card was not read in this pass, so no kernel table is set against the weights here. The parent counts as
neither an original nor a copy (finding 117); the maker's passes of Magidonia v4.3 are findings 144 and 160 and its
pass of Mistral Small 3.2 is finding 159.

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 15 flags (first shares of 0.891 to
0.990 under the 0.99 floor), with the same assessment and nearest recipe on the cluster and after re-scoring at home.
The other candidates read 49 (`single-projection-selected`), 58 (`directional-per-layer`) and 92
(`single-projection`). On reading, the copy is a directional pass with one direction per layer on the two writers.

- 37 of 363 tensors changed: the attention outputs of layers 24 to 29 and the down projections of layers 9 to 39,
  each run unbroken. Every other tensor is exactly 0: the queries, keys, values, gates and up projections of all 40
  layers, the attention outputs of the other 34 layers, the down projections of layers 0 to 8, the embedding and the
  81 norms. The largest change outside the changed set is 0.
- Relative changes 0.0035 to 0.0261 on the attention outputs (median 0.0136) and 0.0141 to 0.0260 on the down
  projections (median 0.0155).
- Within a layer the two writers share one direction: 1.000 at the median and 0.9973 at the least on the six layers
  that carry both. Between layers they do not: 0.457 at the median and 0.050 at the least.
- First shares: the least is 0.8911, and 15 of the 37 sit under the 0.99 floor. No changed matrix keeps its row norms
  (0 of 6 attention outputs, 0 of 31 down projections).
- Every tensor pairs by name: none on one side only, no unused shared projection, no dropped tower or statistic.

| Kind | Changed | Layers | Exactly 0 | Relative change, least | Median | Most |
| --- | --- | --- | --- | --- | --- | --- |
| attention output | 6 of 40 | 24 to 29 | 34 | 0.0035 | 0.0136 | 0.0261 |
| down projection | 31 of 40 | 9 to 39 | 9 | 0.0141 | 0.0155 | 0.0260 |
| query, key, value, gate, up | 0 of 200 | none | 200 | - | - | - |

| Direction group | Matrices | Median cosine to the group | Least |
| --- | --- | --- | --- |
| attention outputs, width 5,120 | 6 | 0.9540 | 0.9118 |
| down projections, width 5,120 | 31 | 0.7388 | 0.3266 |
| across the two kinds | 37 | 0.7947 | 0.0501 |

The down projections carry the spread: their directions turn from layer to layer (0.739 at the median to the group),
while the six attention outputs of layers 24 to 29 stand near one another (0.954), and within each of those layers
the attention output takes the down projection's direction.

Directions. The saved vectors were not placed against earlier measurements in this pass; that comparison (finding
66's check) is owed against the maker's three later Cydonia passes (pairs 2 to 4), its two Magidonia passes, its
Mistral Small 3.2 pass and the other Mistral Small 24B measurements. What the summaries give: this pass has one
direction per layer, as the maker's first Magidonia pass (finding 144) and its Mistral Small 3.2 pass (finding 159)
do, and the maker's second pass of this parent four minutes later has one shared direction (pair 2), the order of
the two Magidonia passes six minutes apart (finding 160).

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home, with two differences: the version strings of
`config.json` and `generation_config.json` move from 4.57.1 to 4.57.3, the save version of the maker's second
Magidonia pass. No other compared field differs, and the fixed conversation renders the same with the `default`
template. The home judgement under transformers 5.22.1 changed no field.

## For the recipe library

A per-layer kernel entry with a heights line would read this pass from its card's table once the card is read; the
`directional-per-layer-selected` entry charges 15 first shares under its floor on a pass whose changes reach 0.0261
of the weight at most. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus44/measurements/pair-1/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
