# Reading of the Stage 1 and Stage 2 result: treadon/gemma4-E2B-it-Abliterated-AND-Disinhibited-USE-THIS against google/gemma-4-E2B-it (2026-11-01)

Measured on Blueback, round 25 piece 8. The pull carries the measurements and the sweep record and no job log.
Modified revision `9e3f1fd8` (six commits from 2026-04-29 23:11Z to 05-01: the model, the tokenizer and three README
updates), original pinned at `6b7e72c6` (04-28), the revision current when the repository was created. The card
says the copy composes two of the maker's edits in sequence: first a "disinhibition" that removes a neutrality
direction from the top 20 layers at scale 1.5, then the abliteration of piece 7 recomputed on the disinhibited
model on the top 24 layers at scale 1.75, both norm-preserving projections on `self_attn.o_proj` and
`mlp.down_proj`. It reports the hedge rate on the maker's opinion set at 5.8 percent and over-refusal at 0. The
`base_model` field names the original.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 42 flags, on the
cluster and after re-scoring at home: 40 first shares of 0.54 to 0.63 on the two writers of the 20 layers both
edits touch, and the two writers of layer 9 at a within-layer cosine of 0.87. On reading, the copy is the two
edits the card describes: the abliteration at 1.75 on piece 7's 24 layers, the disinhibition at 1.5 on 20 of them.

- 48 of 1,951 tensors changed: the attention output and the down projection of layers 9 to 13 and 15 to 33, the
  same 48 as piece 7. Nothing else moved; the largest relative change outside the changed set is exactly 0 and
  1,903 tensors equal the original. The 60 shared-KV tensors are dropped by the export.
- Two kinds of layer. Layers 10, 12, 13 and 15 carry one direction (first share 0.997 to 0.999) at a left kept
  fraction of -0.746 to -0.749 (scale 1.75): the abliteration alone. The 20 other layers (9, 11, 16 to 33) carry
  two directions: first share 0.54 to 0.63, fourth cumulative share 0.997 to 0.999, the leading direction's left
  kept fraction -0.68 to -0.76, the abliteration's 1.75 leading and the disinhibition's 1.5 behind it.
- So the abliteration touched the 24 layers of piece 7 and the disinhibition 20 of them (9, 11, 16 to 33): the
  card's L = 24 and L = 20. On the E4B composition (piece 5) the recomputed abliteration moved to other layers; here
  it did not, though no matrix equals piece 7's, since the direction was recomputed on the disinhibited model.
- Output side on 48 of 48 along the leading direction; the right kept fraction is -0.41 to 0.36 on the down
  projections and 0.15 to 0.84 on the attention outputs.
- Rows moved by at most 0.0005: both restorations hold.
- Relative change 0.040 to 0.072, the two-direction layers at 0.054 to 0.072 against piece 7's 0.039 to 0.055.

| Layer | Attention output: change, E1, E4, left kept, right kept | Down projection: change, E1, E4, left kept, right kept | Edits read |
| --- | --- | --- | --- |
| 9 | 0.0623, 0.602, 0.998, -0.687, 0.148 | 0.0717, 0.605, 0.998, -0.678, -0.048 | both (within-layer 0.87) |
| 10 | 0.0472, 0.998, 0.998, -0.748, 0.267 | 0.0554, 0.999, 0.999, -0.749, -0.062 | abliteration |
| 13 | 0.0400, 0.997, 0.998, -0.749, 0.575 | 0.0559, 0.998, 0.998, -0.748, 0.315 | abliteration |
| 15 | 0.0433, 0.997, 0.998, -0.746, 0.342 | 0.0504, 0.999, 0.999, -0.749, -0.177 | abliteration |
| 19 | 0.0616, 0.562, 0.998, -0.742, 0.344 | 0.0675, 0.550, 0.998, -0.747, -0.130 | both |
| 22 | 0.0631, 0.538, 0.997, -0.702, 0.789 | 0.0642, 0.542, 0.998, -0.749, -0.235 | both |
| 27 | 0.0580, 0.613, 0.997, -0.754, 0.840 | 0.0572, 0.610, 0.998, -0.752, 0.023 | both |
| 33 | 0.0601, 0.592, 0.998, -0.738, 0.218 | 0.0604, 0.609, 0.998, -0.749, -0.410 | both |

The full table (48 rows) is in the report.

The fingerprint shares no measured field with the ten earlier reports on this original or with piece 7.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster; "consistent with re-save noted" at home. Under transformers 5.22.1
`text_config.moe_intermediate_size` (null in a 5.5.3 save) closes by the default rule, and what remains is the
version strings. The template is Google's pinned file and the fixed conversation renders identically.

## For the recipe library

As piece 5 on the E4B: two per-layer projections in sequence read as two directions where both reach and one
where one reaches, the leading scale readable to within 0.01 on the single-direction layers and to within 0.07 on
the doubled ones. The per-layer entry counts 40 first shares because two directions are not one and two
within-layer cosines on layer 9, where the two writers' leading directions are the two edits' in different proportions.
The pull copy keeps the direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/blueback25/measurements/pair-8/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
