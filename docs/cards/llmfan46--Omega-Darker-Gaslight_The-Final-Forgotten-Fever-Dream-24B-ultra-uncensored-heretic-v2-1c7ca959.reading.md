# Reading of the Stage 1 and Stage 2 result: llmfan46/Omega-Darker-Gaslight_The-Final-Forgotten-Fever-Dream-24B-ultra-uncensored-heretic-v2 against ReadyArt/Omega-Darker-Gaslight_The-Final-Forgotten-Fever-Dream-24B

Measured on Nautilus, round 44 piece 6 (sweep job 4180457; the pull, card 5853, carries the measurements and the
sweep record and no job log, so the download and compare job ids, the node and the seconds are not recorded).
Modified revision `372c0799`, created on 2026-03-20 and last revised on 2026-03-27 at 21:46, between the maker's
revisions of pairs 8 (19:57) and 5 (22:30). Parent pinned at `ed406443` (2025-12-27), the latest of fifteen commits at
or before the copy's creation. ReadyArt's Omega-Darker Gaslight 24B names ReadyArt/Omega-Darker_The-Final-Directive-24B,
which names TheDrummer/Cydonia-24B-v2.1, which names no base; the stack has the 40 layers and 5,120 width of Mistral
Small 24B. The copy is the maker's second version of this pass; the first is not measured. The copy's own card was
not read in this pass. The parent counts as neither an original nor a copy (finding 117).

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 12 flags (first shares of 0.601 to
0.921 under the 0.99 floor on every edit), with the same assessment and nearest recipe on the cluster and after
re-scoring at home. `single-projection-selected` reads 25, `directional-per-layer` 81 and `single-projection` 94. On
reading, the copy is a search of the attention outputs alone, one direction per matrix, the smallest changed set of
the round.

- 12 of 363 tensors changed, all attention outputs, between layers 14 and 31. Of the other 28 attention outputs, 22
  are exactly 0 and 6 moved under the 0.001 threshold, the largest by 0.00005784, the largest change outside the
  changed set. The queries, keys, values, gates, up and down projections of all 40 layers, the embedding and the 81
  norms are exactly 0.
- Relative changes 0.0223 to 0.0559, median 0.0321.
- One direction per matrix: 0.3371 at the median to the group's direction and 0.1198 at the least; between layers
  0.0482 at the median and 0.0012 at the least. No layer carries two edits.
- First shares: the least is 0.6014, and all 12 sit under 0.99, the highest 0.921. No changed matrix keeps its row
  norms (0 of 12).
- Every tensor pairs by name: none on one side only, no unused shared projection, no dropped tower or statistic.

| Kind | Changed | Layers | Exactly 0 | Relative change, least | Median | Most |
| --- | --- | --- | --- | --- | --- | --- |
| attention output | 12 of 40 | 14 to 31 | 22 | 0.0223 | 0.0321 | 0.0559 |
| query, key, value | 0 of 120 | none | 120 | - | - | - |
| gate, up, down | 0 of 120 | none | 120 | - | - | - |

| Direction group | Matrices | Median cosine to the group | Least |
| --- | --- | --- | --- |
| attention outputs, width 5,120 | 12 | 0.3371 | 0.1198 |
| between layers | 12 | 0.0482 | 0.0012 |

Twelve edits inside a span of eighteen layers (14 to 31) leave six of that span's matrices unedited, and the six
traces under the threshold are the form of finding 145 and of the maker's PaintedFantasy v1 search (finding 166),
whose untouched layers of the window read 0.0000044 to 0.0000426. Without the card's window the traces cannot be
placed inside or outside it here. The first shares, 0.601 to 0.921, are the lowest of the round's three searches by
this maker, close to PaintedFantasy v1's 0.591 to 0.933.

Directions. The saved vectors were not placed against earlier measurements in this pass; the comparison with the
maker's other Mistral Small searches (pairs 5 and 8, PaintedFantasy v1 and the four of finding 166, whose input sides
stand at 0.86 to 0.91 to one another) is owed (finding 66's check), as is a reading of which side the edit is on.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, 1,011 differences. Five are explained by re-save: the separate
declaration of `additional_special_tokens`, `config.pad_token_id`, `config.rope_parameters` (closed at home), the
version string from 4.51.1 to 5.3.0 and the template moved out of `tokenizer_config.json`. The 1,006 unexplained are
the 1,000 `added_tokens_decoder` declarations a 5.3.0 save drops, the decoder block that held them, the `pad_token_id`
entry among the special-token ids, a generation file the parent does not publish, `rope_theta` (now inside
`rope_parameters`) and the move from `torch_dtype` to `dtype`. The list is pair 5's field for field, less its expected
`_name_or_path`. The fixed conversation renders the same with the `default` template.

## For the recipe library

A search entry with a window line and a traces line would read this pass once the card's window is
known; the `directional-per-layer-selected` entry charges every first share. The direction vectors stay in the pull
copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus44/measurements/pair-6/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
