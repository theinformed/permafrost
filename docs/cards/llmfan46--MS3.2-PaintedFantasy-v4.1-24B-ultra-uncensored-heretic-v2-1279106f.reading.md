# Reading of the Stage 1 and Stage 2 result: llmfan46/MS3.2-PaintedFantasy-v4.1-24B-ultra-uncensored-heretic-v2 against zerofata/MS3.2-PaintedFantasy-v4.1-24B

Measured on Nautilus, round 44 piece 8 (sweep job 4180457; the pull, card 5853, carries the measurements and the
sweep record and no job log, so the download and compare job ids, the node and the seconds are not recorded).
Modified revision `257ae414`, created on 2026-03-22 and last revised on 2026-03-27 at 19:57, the first of the maker's
three revisions of its round 44 copies that evening (pairs 6 and 5 at 21:46 and 22:30). Parent pinned at `f147119f`
(2026-02-19), the revision round 52 measured the maker's first version against (finding 166). zerofata's
PaintedFantasy v4.1 is a fine-tune whose field names mistralai/Magistral-Small-2509, with the 40 layers of Mistral
Small. The copy's own card was not read in this pass. The parent counts as neither an original nor a copy (finding
117).

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 18 flags (first shares of 0.717 to
0.949 under the 0.99 floor on every edit), with the same assessment and nearest recipe on the cluster and after
re-scoring at home. `single-projection-selected` reads 37, `directional-per-layer` 81 and `single-projection` 100. On
reading, the copy is a second search of the same parent's attention outputs, the same count as the first, reaching
the last layer.

- 18 of 363 tensors changed, all attention outputs, between layers 12 and 39. Inside layers 12 to 39 one attention
  output is exactly 0 and nine moved under the 0.001 threshold; of layers 0 to 11, seven are exactly 0 and five moved
  under it. The largest of those fourteen traces is 0.0000903, the largest change outside the changed set. The
  queries, keys, values, gates, up and down projections of all 40 layers, the embedding and the 81 norms are exactly 0.
- Relative changes 0.0260 to 0.0515, median 0.0347.
- One direction per matrix: 0.2196 at the median to the group's direction and 0.1550 at the least; between layers
  0.0216 at the median and 0.0002 at the least. No layer carries two edits.
- First shares: the least is 0.7171, and all 18 sit under 0.99, the highest 0.949. No changed matrix keeps its row
  norms (0 of 18).
- Every tensor pairs by name: none on one side only, no unused shared projection, no dropped tower or statistic.

| Kind | Changed | Layers | Exactly 0 | Relative change, least | Median | Most |
| --- | --- | --- | --- | --- | --- | --- |
| attention output | 18 of 40 | 12 to 39 | 8 | 0.0260 | 0.0347 | 0.0515 |
| query, key, value | 0 of 120 | none | 120 | - | - | - |
| gate, up, down | 0 of 120 | none | 120 | - | - | - |

| Direction group | Matrices | Median cosine to the group | Least |
| --- | --- | --- | --- |
| attention outputs, width 5,120 | 18 | 0.2196 | 0.1550 |
| between layers | 18 | 0.0216 | 0.0002 |

Against the first version on the same parent (finding 166), the two searches edit 18 attention outputs each, both
starting at layer 12. The first stopped at 38 and left layer 39 exactly 0, its card's `end_layer_index` of 39
excluded; this one edits up to layer 39. The first left seventeen layers of its window as traces of 0.0000044 to
0.0000426 and layers 0 to 3 exactly 0; this one leaves fourteen traces, to 0.0000903, five of them below layer 12. The
relative changes run a little higher (0.0260 to 0.0515 against 0.0233 to 0.0429) and so do the first shares (0.717 to
0.949 against 0.591 to 0.933). Both read one direction per matrix, at 0.25 at the median between matrices on the
first and 0.2196 to the group here.

Directions. The saved vectors were not placed against earlier measurements in this pass; the comparison with the
first version layer by layer, with the maker's other Mistral Small searches (pairs 5 and 6 and the four of finding
166, whose input sides stand at 0.86 to 0.91 to the first version) and with the other Mistral Small 24B measurements
is owed (finding 66's check), as is a reading of which side the edit is on.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, 1,006 differences. Four are explained by re-save: the separate
declaration of `additional_special_tokens`, the version strings of `config.json` and `generation_config.json` from
4.57.5 to 5.3.0 and `config.rope_parameters` (closed at home). The 1,002 unexplained are the 1,000
`added_tokens_decoder` declarations a 5.3.0 save drops, the decoder block that held them and `rope_theta`, now inside
`rope_parameters`. The template is not among the differences: the first version carried the parent's template with
Windows line endings on all 51 lines (finding 166), and this one does not differ from the parent's in the compared
field. The fixed conversation renders the same with the `default` template.

## For the recipe library

The input-side search entry with its window line and a traces line, the entry round 52 asked for on the first
version, would need the card's window to place the five traces below layer 12. The direction vectors stay in the pull
copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus44/measurements/pair-8/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
