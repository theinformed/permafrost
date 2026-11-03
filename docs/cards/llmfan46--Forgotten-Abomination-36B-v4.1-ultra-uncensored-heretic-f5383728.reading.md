# Reading of the Stage 1 and Stage 2 result: llmfan46/Forgotten-Abomination-36B-v4.1-ultra-uncensored-heretic against ReadyArt/Forgotten-Abomination-36B-v4.1

Measured on Nautilus, round 44 piece 5 (sweep job 4180457; the pull, card 5853, carries the measurements and the
sweep record and no job log, so the download and compare job ids, the node and the seconds are not recorded).
Modified revision `7c494862`, created on 2026-03-25 and last revised on 2026-03-27 at 22:30, the last of three
revisions the maker made to its round 44 copies that evening (pairs 6 and 8 at 21:46 and 19:57). Parent pinned at
`f4f88bf1` (2025-03-20), the latest of nine commits at or before the copy's creation. ReadyArt's Forgotten-Abomination
36B v4.1 names ReadyArt/Forgotten-Safeword-36B-4.1, which names TheDrummer/Skyfall-36B-v2, which names no base. The
stack has 64 layers at a width of 5,120, the width of Mistral Small 24B's 40, and the template renders Mistral's
`[SYSTEM_PROMPT]` and `[INST]` turns. The copy's own card was not read in this pass. The parent counts as neither an
original nor a copy (finding 117).

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 36 flags (first shares of 0.939 to
0.989 under the 0.99 floor), with the same assessment and nearest recipe on the cluster and after re-scoring at home.
`single-projection-selected` reads 77, `directional-per-layer` 125 and `single-projection` 166. On reading, the copy is
a search of the attention outputs alone, one direction per matrix, with relative changes the maker's 24B searches do
not reach (0.0559 at most on pairs 6 and 8).

- 40 of 579 tensors changed, all attention outputs, between layers 17 and 63. Of the other 24 attention outputs, 17
  are exactly 0 and 7 moved under the 0.001 threshold, the largest by 0.00006002, the largest change outside the
  changed set. The queries, keys, values, gates, up and down projections of all 64 layers, the embedding and the 129
  norms are exactly 0.
- Relative changes 0.0494 to 5.5239, median 0.6335. Twenty-one of the 40 are above 0.5: layer 23 at 5.5239, 27 at
  2.7907, 32 at 2.0890, 33 at 1.7827, 24 at 1.3784, 29 at 0.9966, 30 at 0.6601 and 26 at 0.6069 among them, and 13
  more.
- One direction per matrix: 0.1534 at the median to the group's direction and 0.0609 at the least; between layers
  0.0167 at the median and 0.000021 at the least. No layer carries two edits.
- First shares: the least is 0.9390, and 36 of the 40 sit under 0.99. No changed matrix keeps its row norms (0 of 40).
- Every tensor pairs by name: none on one side only, no unused shared projection, no dropped tower or statistic.

| Kind | Changed | Layers | Exactly 0 | Relative change, least | Median | Most |
| --- | --- | --- | --- | --- | --- | --- |
| attention output | 40 of 64 | 17 to 63 | 17 | 0.0494 | 0.6335 | 5.5239 |
| query, key, value | 0 of 192 | none | 192 | - | - | - |
| gate, up, down | 0 of 192 | none | 192 | - | - | - |

| Direction group | Matrices | Median cosine to the group | Least |
| --- | --- | --- | --- |
| attention outputs, width 5,120 | 40 | 0.1534 | 0.0609 |
| between layers | 40 | 0.0167 | 0.000021 |

A relative change of 5.52 is a change five and a half times the norm of the parent's matrix. Two readings fit it.
The search amplified a component rather than removing it, as the maker's 31B Queen search did at layer 50 (finding
120, a component multiplied by 6.71 at a relative change of 0.1205); or the parent's attention outputs on those
layers are nearly empty, as on the fourteen layers Skyfall 31B inserts (finding 143, norms of 0.23 to 0.41 against
9.9 to 20.6), so that an ordinary change reads as a large fraction. The second fits a 64-layer stack at a 40-layer
width whose chain ends at a Skyfall release, and 21 of the 40 edits sit above 0.5 while the other 19 read 0.0494 to
0.5. The parent's tensor norms and a byte-range read of the layer 23 attention output on both sides would decide it.

Directions. The saved vectors were not placed against earlier measurements in this pass; the comparison with the
maker's other Mistral Small searches (pairs 6 and 8, round 52's PaintedFantasy v1 and the four of finding 166) is
owed (finding 66's check), as is a reading of which side the edit is on.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, 1,012 differences. One is expected: `config._name_or_path`,
the parent's ReadyArt/Forgotten-Safeword-36B-4.1, is gone. Five are explained by re-save: the separate declaration of
`additional_special_tokens`, `config.pad_token_id`, `config.rope_parameters` (closed at home), the version string from
4.49.0 to 5.3.0 and the template moved out of `tokenizer_config.json`. The 1,006 unexplained are the 1,000
`added_tokens_decoder` declarations a 5.3.0 save drops, the decoder block that held them, the `pad_token_id` entry
among the special-token ids, a generation file the parent does not publish, `rope_theta` (now inside
`rope_parameters`) and the move from `torch_dtype` to `dtype`. The fixed conversation renders the same with the
`default` template.

## For the recipe library

The `directional-per-layer-selected` entry charges 36 first shares on a search whose first shares (0.939 to 0.989)
sit higher than the maker's 24B searches'. An entry for searches needs a relative-change line read against the
parent's own norms, so that an edit on a near-empty writer is not read as an amplification. The direction vectors
stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus44/measurements/pair-5/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
