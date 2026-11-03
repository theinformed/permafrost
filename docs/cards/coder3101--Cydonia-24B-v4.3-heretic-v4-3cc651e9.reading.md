# Reading of the Stage 1 and Stage 2 result: coder3101/Cydonia-24B-v4.3-heretic-v4 against TheDrummer/Cydonia-24B-v4.3

Measured on Nautilus, round 44 piece 4 (sweep job 4180457; the pull, card 5853, carries the measurements and the
sweep record and no job log, so the download and compare job ids, the node and the seconds are not recorded).
Modified revision `d5909f45`, created on 2026-02-15 at 13:36, six minutes after the maker's third pass of the same
parent (pair 3), and last revised at 13:41 the same day. Parent pinned at `db0426d3` (2025-12-17). TheDrummer's
Cydonia v4.3 is a fine-tune whose field names mistralai/Mistral-Small-3.2-24B-Instruct-2506, with the 40 layers and
the 5,120 width of Mistral Small. The copy's own card was not read in this pass. The parent counts as neither an
original nor a copy (finding 117).

## Weights (Stage 2)

The tool's assessment was violations against `single-projection-selected`, 59 flags (58 first shares of 0.852 to
0.990 under the 0.99 floor and one cross-kind direction cosine of 0.9068), with the same assessment and nearest recipe
on the cluster and after re-scoring at home. `directional-per-layer-selected` reads 62, `single-projection` 74 and
`directional-per-layer` 77. On reading, the copy is a nearly shared direction on both writers, the attention edit
stopping one layer short of the last.

- 65 of 363 tensors changed: the attention outputs of layers 10 to 38 and the down projections of layers 4 to 39, each
  run unbroken. The attention outputs of layers 0 to 9 and 39 and the down projections of layers 0 to 3 are exactly 0,
  as are the queries, keys, values, gates and up projections of all 40 layers, the embedding and the 81 norms. The
  largest change outside the changed set is 0.
- Relative changes 0.0027 to 0.0207 on the attention outputs (median 0.0124) and 0.0100 to 0.0167 on the down
  projections (median 0.0112).
- One direction, nearly: 0.9921 and 0.9973 at the median to the two groups' directions, 0.9690 and 0.9807 at the
  least, 0.9068 across the two kinds (the one direction flag). Between layers 0.9910 at the median and 0.9479 at the
  least; within the 29 layers that carry both writers 0.9918 at the median and 0.9357 at the least.
- First shares: the least is 0.8515, and 58 of the 65 sit under 0.99. No changed matrix keeps its row norms (0 of 29,
  0 of 36).
- Every tensor pairs by name: none on one side only, no unused shared projection, no dropped tower or statistic.

| Kind | Changed | Layers | Exactly 0 | Relative change, least | Median | Most |
| --- | --- | --- | --- | --- | --- | --- |
| attention output | 29 of 40 | 10 to 38 | 11 | 0.0027 | 0.0124 | 0.0207 |
| down projection | 36 of 40 | 4 to 39 | 4 | 0.0100 | 0.0112 | 0.0167 |
| query, key, value, gate, up | 0 of 200 | none | 200 | - | - | - |

| Direction group | Matrices | Median cosine to the group | Least |
| --- | --- | --- | --- |
| attention outputs, width 5,120 | 29 | 0.9921 | 0.9690 |
| down projections, width 5,120 | 36 | 0.9973 | 0.9807 |
| across the two kinds | 65 | 0.9958 | 0.9068 |

Against pair 3, made six minutes earlier, the pass trims the attention reach to 10 to 38 and the down reach to 4 to
39, and its direction turns a little more between layers (0.9910 at the median against 0.9972). Of the maker's four
passes it is the only one that leaves the last layer's attention output exactly 0, and the only one with a direction
flag. Its 59 flags are the most of the four on fewer matrices than pair 3's 74.

Directions. The saved vectors were not placed against earlier measurements in this pass; the comparison with pairs 1
to 3, with the maker's Magidonia and Mistral Small 3.2 passes and with the other Mistral Small 24B measurements is owed
(finding 66's check).

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home, with two differences: the version strings of
`config.json` and `generation_config.json` move from 4.57.1 to 4.57.6, as on pair 3. No other compared field differs,
and the fixed conversation renders the same with the `default` template. The home judgement under transformers
5.22.1 changed no field.

## For the recipe library

The cross-kind floor charges the one place where the two writers' directions part by most (0.9068), on a pass whose
within-layer agreement reads 0.9918 at the median; a shared-direction entry that allows the measured turn between
layers would carry both. The first-share floor charges 58 of 65 matrices, the lowest at 0.852. The direction vectors
stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus44/measurements/pair-4/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
