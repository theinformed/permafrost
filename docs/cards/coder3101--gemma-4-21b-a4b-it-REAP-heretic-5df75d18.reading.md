# Reading of the Stage 1 and Stage 2 result: coder3101/gemma-4-21b-a4b-it-REAP-heretic against 0xSero/Gemma-4-21B (2026-11-02)

Measured on Wheat, round 47 piece 5 (download job 387398, compare job 387403, sweep 387407; the pull carries the
measurements and the sweep record and no job log). Modified revision `a9408009` (created 2026-04-09 09:59Z, the
weights uploaded at 10:41Z), parent pinned at `e5921d70` of 2026-04-08, 0xSero's REAP pruning of
google/gemma-4-26b-a4b-it, 25 of the 128 experts of each layer removed by Cerebras's router-weighted expert
activation pruning (103 left, eight active per token, 21.34B parameters), which the card's `base_model` field
names as 0xSero/gemma-4-21b-a4b-it-REAP, a name the hub resolves to this repository. The card is Heretic 1.2.0's
arbitrary-rank table with row-norm preservation: `start_layer_index` 11, `end_layer_index` 30,
`preserve_good_behavior_weight` 0.8146, `steer_bad_behavior_weight` 0.0025, `overcorrect_relative_weight` 0.2042,
`neighbor_count` 15, a KL divergence of 0.0605 and 14 refusals in 100 against 100. The maker's edit of 0xSero's
30-percent pruning (90 experts, coder3101/gemma-4-19b-a4b-it-REAP-heretic, made two hours earlier, `start_layer_index`
14, `end_layer_index` 25, `neighbor_count` 7) is on the hub and is not measured; no measurement of it is in
`results/` or in any pull copy, so the two REAP edits are compared below by byte range. The parent counts as
neither an original nor a copy (finding 117).

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 19 flags (first shares 0.391 to
0.919 under the 0.99 floor), on the cluster and after re-scoring at home. On reading, the copy is the branch on
the attention outputs of the card's window to the layer, every edit on the input side, with the rows in the band.

- 19 of 1,013 tensors changed: the attention outputs of layers 11 to 29, the card's window (`end_layer_index` 30
  is one past the last layer). The experts, the dense feed-forward layers, the routers, the vision tower and every
  other tensor read exactly 0.
- One direction per matrix (agreement between layers 0.038 at the median), first shares 0.391 to 0.919.
- Input side on all 19: one minus the right kept fraction 0.59 to 1.34 (1.34 at layer 17, 1.25 at 20), the left
  side at 0.66 to 0.99; no kept fraction is above 1.
- Relative changes 0.0064 to 0.0406; rows moved 0.0061 to 0.0077, finding 22's band on every matrix, under a card
  that names row-norm preservation.

| Layer | Change | E1 | Left kept | Right kept | Weight (one minus right kept) | Rows |
| --- | --- | --- | --- | --- | --- | --- |
| 11 | 0.0100 | 0.847 | 0.98 | -0.09 | 1.09 | 0.0074 |
| 14 | 0.0180 | 0.799 | 0.89 | -0.10 | 1.10 | 0.0071 |
| 17 | 0.0137 | 0.826 | 0.99 | -0.34 | 1.34 | 0.0070 |
| 19 | 0.0406 | 0.391 | 0.96 | -0.14 | 1.14 | 0.0061 |
| 20 | 0.0355 | 0.663 | 0.96 | -0.25 | 1.25 | 0.0076 |
| 23 | 0.0064 | 0.826 | 0.99 | 0.41 | 0.59 | 0.0075 |
| 25 | 0.0146 | 0.898 | 0.97 | 0.35 | 0.65 | 0.0077 |
| 29 | 0.0109 | 0.919 | 0.97 | -0.01 | 1.01 | 0.0075 |

The full table (19 rows) is in the report.

Directions. The attention outputs of the pruned checkpoint keep the 26B-A4B's shape (2,816 by 4,096), and against
the saved vectors of the thirty-three 26B-A4B measurements the direction stands on the left at 0.898 to the maker's
own 26B-A4B edit (19 names, minimum 0.646), to SubMaroon's merge body, which is that edit (finding 118), and to
SassyDiffusion's search (17 names), 0.890 to llmfan46's MeroMero 26B-A4B edit (11 names), 0.862 to llmfan46's April
26B-A4B edit, 0.858 to Vortex5's Chimera-X edit, 0.841 and 0.825 to the two makers' QAT edits, 0.758 to Vortex5's
Moonlight-Dusk edit, 0.663 to OS-Software's Japanese-prompted search, and 0.20 or less to every kernel pass and
projection (TrevorJS's 0.168, huihui-ai's 0.056). By byte range 0xSero's 21B and 19B checkpoints carry Google's
attention outputs byte for byte on layers 12, 15, 20, 24 and 27, so the edit stands on the attention outputs of
google/gemma-4-26b-a4b-it at `4d7ae498`. The maker's 19B edit reads by byte range as a rank-one change on layers 17
and 19 to 21 (0.0157 to 0.0576 from Google's, first shares 0.911 to 0.957) with the other layers of its window left
as rewrites of 0.0011 to 0.0017 with no leading component, the residues finding 22 read on the maker's 31B edit, and
layers 12 and 27 outside its window byte-equal to Google's; on the four layers both edits change, the leading
directions stand at 0.35 to 0.65 on the left and 0.55 to 0.78 on the right, two searches with different windows and
weights on two prunings of one checkpoint, against the 0.898 this edit reads to the maker's edit of the unpruned one.

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home: the version strings in the configuration and the
generation file, 5.5.0 on the parent's side (its 04-08 commit titled "bump") and 5.5.0.dev0 on the copy's. The
template (12,045 bytes, Google's release revision), the `tokenizer.json` and the processor file are the parent's by
object id. The token ids are the instruct checkpoint's through the parent (`eos_token_id` `[1, 106]`, generation
`[1, 106, 50]`, `bos_token_id` 2, `pad_token_id` 0) and the vocabulary is 262,144.

## For the recipe library

An arbitrary-rank entry with a components line would read the copy; the per-layer entry charges its first shares.
The pinner should queue the maker's 19B edit against 0xSero's 19B checkpoint so that both prunings are read. The
direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat47/measurements/pair-5/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
