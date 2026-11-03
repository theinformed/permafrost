# Reading of the Stage 1 and Stage 2 result: llmfan46/Gemma-4-Garnet-31B-it-uncensored-heretic against ConicCat/Gemma4-Garnet-31B (2026-11-03)

Measured on Wheat, round 49 piece 5 (download job 387515, compare job 387520, sweep 387524; the pull carries the
measurements and the sweep record and no job log). Modified revision `e4da9fb3` (created 2026-04-14 11:50Z, the
weights uploaded at 11:53Z, the card edited to 15:29Z, the template deleted and uploaded again on 05-04 at 01:58Z and
on 05-05 at 17:02Z), parent pinned at `200c398e` of 2026-04-08, ConicCat's Garnet 31B, the first version of the
fine-tune whose second version is the parent of the maker's Garnet V2 search (finding 134). The parent ships its
adapter: rank 32 at alpha 64 on all seven projections of google/gemma-4-31B-it, trained on ConicCat's Gutenberg and
Condor sets, merged to full. The card is Heretic 1.2.0's arbitrary-rank table: `start_layer_index` 26,
`end_layer_index` 46, `preserve_good_behavior_weight` 0.8239, `steer_bad_behavior_weight` 0.0001,
`overcorrect_relative_weight` 1.1479, `neighbor_count` 10, `attn.o_proj` the one target, a KL divergence of 0.0368
and 6 refusals in 100 against 99. The parent counts as neither an original nor a copy (finding 117).

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 16 flags (first shares 0.924 to
0.971 under the 0.99 floor), on the cluster and after re-scoring at home. On reading, the copy is the branch on the
attention outputs of the card's window to the layer, at the largest input-side weights and row movement the maker's
searches have read, with no component amplified.

- 16 of 1,188 tensors changed: the attention outputs of layers 26 to 28, 30 to 34, 36 to 39, 41 and 43 to 45. The
  other four of the window (29, 35, 40 and 42) moved by 0.00000055 to 0.0000034, the largest relative change
  outside the changed set; layers 0 to 25 and 46 to 59 and every tensor that is not an attention output read
  exactly 0.
- One direction per matrix (agreement 0.318 at the median), first shares 0.924 to 0.971.
- Input side on all 16: one minus the right kept fraction reads 1.64 to 3.44 (3.44 at layer 27, 3.21 at 39), the
  left side keeps 0.29 to 0.97. The eight saved components keep at most 1.005 on the left and 1.041 on the right,
  the noise of a minor component, where the maker's Queen and MeroMero edits multiply one component by up to 6.71
  (finding 120); no component is amplified.
- Relative changes 0.0171 to 0.0860; rows moved 0.0017 to 0.3246 under a card that claims no norm (0.3246 at layer
  44, 0.0609 at 37, 0.0469 at 39).

| Layer | Change | E1 | Left kept | Right kept | Weight (one minus right kept) | Rows |
| --- | --- | --- | --- | --- | --- | --- |
| 26 | 0.0271 | 0.946 | 0.81 | -0.64 | 1.64 | 0.0067 |
| 27 | 0.0506 | 0.969 | 0.49 | -2.44 | 3.44 | 0.0194 |
| 31 | 0.0359 | 0.958 | 0.85 | -1.88 | 2.88 | 0.0071 |
| 33 | 0.0436 | 0.955 | 0.55 | -1.56 | 2.56 | 0.0211 |
| 37 | 0.0486 | 0.958 | 0.95 | -1.83 | 2.83 | 0.0609 |
| 39 | 0.0553 | 0.962 | 0.29 | -2.21 | 3.21 | 0.0469 |
| 44 | 0.0860 | 0.971 | 0.68 | -1.93 | 2.93 | 0.3246 |
| 45 | 0.0375 | 0.957 | 0.97 | -1.73 | 2.73 | 0.0077 |

The full table (16 rows) is in the report.

Directions. Against the saved vectors of the thirty-eight other 31B measurements the direction stands on the left at
0.910 to the maker's 31B QAT search (8 names), 0.895 to coder3101's QAT edit, 0.883 to the maker's Garnet V2 search
(16 names, minimum 0.714; 0.914 on the right), 0.867 to coder3101's 31B edit, 0.860 to the MeroMero edit, 0.858 to
the Gembrain search, 0.839 to the Queen edit, 0.835 to MoonRide's search, 0.811 to the maker's April edit, 0.709 to
the Harmonia search, 0.569 to Jim-darby's Japanese-weighted search and 0.18 or less to every kernel pass and
projection. By byte range on three layers both Garnet searches edit, the leading directions of the two changes stand
at 0.923, 0.817 and 0.766 on the left (layers 30, 37 and 44) and 0.933, 0.722 and 0.329 on the right.

The two parents. ConicCat's Garnet 31B and GarnetV2 31B share their configuration (`5f291aa9`), shard index
(`e9bb971a`), processor file and `tokenizer.json` (`1ff9f3e3`) by object id and differ in every weight shard and in
their adapters (rank 32 at alpha 64 against rank 64 at alpha 128, both on google/gemma-4-31B-it). By byte range the
first version stands 0.0291 and 0.0315 from Google's on the layer 10 and 30 attention outputs and 0.0328 on the layer
5 query projection, the second 0.0323 and 0.0286, and the two stand 0.0434, 0.0425 and 0.0491 from each other, with
leading components at 0.03 and 0.24 to each other: two trainings of Google's checkpoint side by side, and not one
over the other.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, four fields, the home judgement closing
`config.text_config.moe_intermediate_size` (absent on one side and loaded as the same default): the version strings
move from 5.5.0.dev0 to 5.5.0, and the template is the maker's 17,344-byte file (`7fa57f97`, the one finding 134
traced on the Garnet V2 copy) over the parent's 12,045 bytes. The copy's template history is that file's: 16,795
bytes at upload, 16,934 bytes from 05-04 at 01:58Z, and the 17,344-byte file from 05-05 at 17:02Z, 24 seconds after
it replaced the Garnet V2 copy's by the same delete and upload. The token ids are the instruct checkpoint's through
the parent (`eos_token_id` `[1, 106]`, generation `[1, 106, 50]`, `bos_token_id` 2, `pad_token_id` 0) and the
vocabulary is 262,144.

## For the recipe library

An arbitrary-rank entry with a trace line would read the copy; the per-layer entry charges its first shares. The
maker's-template rule owed to the metadata tool would name the template here, the seventh of the maker's
repositories in the census to carry the file. The direction vectors stay in
the pull copy at `/opt/ai/hpc-packages/pulls/model-audit/wheat49/measurements/pair-5/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
