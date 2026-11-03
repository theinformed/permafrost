# Reading of the Stage 1 and Stage 2 result: Vortex5/Pantheon-Reasoning-26B-A4B-1.1-heretic against Gryphe/Pantheon-Reasoning-26B-A4B-1.1

Measured on Nautilus, round 44 piece 7 (sweep job 4180457; the pull, card 5853, carries the measurements and the
sweep record and no job log, so the download and compare job ids, the node and the seconds are not recorded).
Modified revision `f1e4c4cf`, created on 2026-07-08 at 21:45 and last revised at 22:31 the same evening. Parent pinned
at `9156318c` (2026-06-08), the latest of six commits at or before the copy's creation. Gryphe's Pantheon-Reasoning 1.1
names google/gemma-4-26B-A4B-it, which names google/gemma-4-26B-A4B; it is one of the five fine-tunes in Vortex5's
Phoenix-X merge, whose per-layer Heretic pass by alexokita is finding 165. The copy's own card was not read in this
pass. The parent counts as neither an original nor a copy (finding 117); the maker's searches of its own Chimera-X and
Moonlight-Dusk merges are finding 119.

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 23 flags (first shares of 0.839 to
0.963 under the 0.99 floor on every edit), with the same assessment and nearest recipe on the cluster and after
re-scoring at home. `single-projection-selected` reads 47, `directional-per-layer` 92 and `single-projection` 116. On
reading, the copy is a search of the attention outputs alone, one direction per matrix, with no expert and no dense
writer touched.

- 23 of 1,014 tensors changed: the attention outputs of layers 7 to 29, the run unbroken to the last layer. The
  attention outputs of layers 0 to 6 are exactly 0, as are the 30 queries, the 30 keys, the 25 values, the 30 gates,
  the 60 up and 60 down tensors of the dense and expert feed-forward blocks, the 4 embedding tensors, the 433 norms and
  the 312 others. The largest change outside the changed set is 0.
- Relative changes 0.0130 to 0.0539, median 0.0261.
- One direction per matrix: 0.2688 at the median to the group's direction and 0.0526 at the least; between layers
  0.0396 at the median and 0.00037 at the least. No layer carries two edits.
- First shares: the least is 0.8393, and all 23 sit under 0.99, the highest 0.963. No changed matrix keeps its row
  norms (0 of 23).
- Every tensor pairs by name: none on one side only, no unused shared projection, no dropped tower or statistic.

| Kind | Changed | Layers | Exactly 0 | Relative change, least | Median | Most |
| --- | --- | --- | --- | --- | --- | --- |
| attention output | 23 of 30 | 7 to 29 | 7 | 0.0130 | 0.0261 | 0.0539 |
| query, key, value | 0 of 85 | none | 85 | - | - | - |
| gate, up, down (dense and expert) | 0 of 150 | none | 150 | - | - | - |
| embedding, norms, others | 0 of 749 | none | 749 | - | - | - |

| Direction group | Matrices | Median cosine to the group | Least |
| --- | --- | --- | --- |
| attention outputs, width 2,816 | 23 | 0.2688 | 0.0526 |
| between layers | 23 | 0.0396 | 0.00037 |

Against finding 165's pass of the merge that contains this parent, the form differs on every count the summaries
give: that pass edited the dense down projections of layers 8 to 29 and the attention outputs of 15 to 29 (37 of
1,013), its two writers sharing a direction within a layer (0.965) and its layers standing at 0.64 to one another,
with first shares of 0.989 to 0.997. This pass edits one writer, its layers stand at 0.040 to one another and its
first shares run 0.839 to 0.963. The maker's two earlier searches read the attention outputs alone as well, layers 6
to 22 of Chimera-X and 9 to 21 of Moonlight-Dusk (17 and 16 of 1,014), so this copy has the maker's form, its run
reaching the last layer where those stopped at 22 and 21.

Directions. The saved vectors were not placed against earlier measurements in this pass; the comparison with the
26B-A4B families (the per-layer Heretic passes of Google's checkpoint, TrevorJS's edit, the maker's two searches,
alexokita's pass of Phoenix-X) is owed (finding 66's check), as is a reading of which side the edit is on.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, 9 differences. Six are explained by re-save: the version
strings from 5.5.0.dev0 and 5.6.0.dev0 to 5.13.0, and the `torch_dtype` to `dtype` move inside `text_config` and
`vision_config`, which repeat the top-level type. Three are unexplained: the same move at the top level (`dtype`
added, `torch_dtype` gone) and the template moved out of `tokenizer_config.json`. The fixed conversation renders the
same with the `default` template, the empty thought channel of the model turn included. The home judgement changed no
field.

## For the recipe library

A search entry with a window line would read this pass once the card's window is known; the
`directional-per-layer-selected` entry charges every first share. The metadata tool reads the `dtype` move as a re-save
inside the sub-configurations and as unexplained at the top level of the same file. The direction vectors stay in the
pull copy at `/opt/ai/hpc-packages/pulls/model-audit/nautilus44/measurements/pair-7/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
