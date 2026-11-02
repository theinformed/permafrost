# Reading of the Stage 1 and Stage 2 result: llmfan46/Gemma-4-Harmonia-31B-uncensored-heretic against virtuous7373/Gemma-4-Harmonia-31B (2026-11-02)

Measured on Wheat, round 47 piece 7 (download job 387398, compare job 387405, sweep 387407; the pull carries the
measurements and the sweep record and no job log). Modified revision `944459ac` (created 2026-05-27 13:14Z, the
weights uploaded at 13:18Z, every file deleted at 13:20Z and uploaded again by 13:24Z, the card edited until 05-28),
parent pinned at `874d478b` of 2026-05-22, virtuous7373's Harmonia 31B, a three-stage merge whose
`mergekit_config.yml` takes the maker's unmeasured Ortenzya edit as the base of an `actmat` merge with
LatitudeGames's Equinox, Lambent's Fabled and an intermediate `cabs` merge of the maker's MeroMero edit (weight 0.6)
and the maker's Gembrain edit, pair 6 of this round (weight 0.4), over a `nullspace` merge of ConicCat's GarnetV2
onto Google's pretrained 31B. The card is Heretic 1.2.0's arbitrary-rank table: `start_layer_index` 14,
`end_layer_index` 55, `preserve_good_behavior_weight` 0.7754, `steer_bad_behavior_weight` 0.0001,
`overcorrect_relative_weight` 0.9765, `neighbor_count` 14, `attn.o_proj` the one target, a KL divergence of 0.0047
and 9 refusals in 100 against 97. It is the maker's sixth second-generation edit in the census and the first over a
parent that carries the maker's own edits. The parent counts as neither an original nor a copy (finding 117).

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 22 flags (first shares 0.891 to
0.975 under the 0.99 floor), on the cluster and after re-scoring at home. On reading, the copy is the branch on 22
attention outputs inside the card's window with the rest of the window traced, every edit on the input side, and
no layer amplified.

- 22 of 1,188 tensors changed: the attention outputs of layers 26, 29 to 32, 34, 36, 37, 39 to 41, 43 to 52 and 54.
  The window's other nineteen attention outputs (14 to 25, 27, 28, 33, 35, 38, 42 and 53) moved by 0.0000005 to
  0.000234, the largest at layer 18 and the largest relative change outside the changed set; layers 0 to 13 and 55
  to 59 read exactly 0, as does everything else, so the window is the card's to the layer.
- One direction per matrix (agreement between layers 0.025 at the median), first shares 0.891 to 0.975.
- Input side on all 22: one minus the right kept fraction 0.22 to 2.20 (2.20 at layer 49, 2.15 at 48, 1.98 at 31),
  the left side at 0.62 to 0.99; no kept fraction is above 1 on either side.
- Relative changes 0.0096 to 0.0655; rows moved 0.0008 to 0.0215, under, in and over finding 22's band under a
  card that names no row preservation.

| Layer | Change | E1 | Left kept | Right kept | Weight (one minus right kept) | Rows |
| --- | --- | --- | --- | --- | --- | --- |
| 18 | 0.0002 | - | - | - | - | 0.0000 |
| 26 | 0.0184 | 0.948 | 0.93 | -0.21 | 1.21 | 0.0048 |
| 31 | 0.0360 | 0.912 | 0.92 | -0.98 | 1.98 | 0.0068 |
| 39 | 0.0363 | 0.941 | 0.65 | -0.57 | 1.57 | 0.0062 |
| 43 | 0.0254 | 0.949 | 0.82 | -0.24 | 1.24 | 0.0215 |
| 48 | 0.0655 | 0.976 | 0.95 | -1.15 | 2.15 | 0.0086 |
| 49 | 0.0283 | 0.961 | 0.81 | -1.20 | 2.20 | 0.0067 |
| 50 | 0.0107 | 0.916 | 0.99 | 0.78 | 0.22 | 0.0026 |
| 54 | 0.0246 | 0.940 | 0.63 | -0.75 | 1.75 | 0.0039 |

The full table is in the report.

Directions. Against the saved vectors of the thirty-seven other 31B measurements, the direction stands on the left
at 0.797 to the maker's QAT search (6 names), 0.751 to coder3101's QAT edit, 0.731 to the maker's Gembrain edit of
this round (20 names), 0.713 to the maker's Garnet search, 0.687 to MoonRide's custom search, 0.670 to the maker's
MeroMero edit (15 names), 0.634 to Bahushruth's and to the maker's Queen edit, 0.602 to coder3101's 31B edit and to
the maker's April edit, 0.569 to wnfldchen's, 0.560 to densenet's, 0.557 to MoonRide's other search, 0.447 to
Jim-darby's and 0.383 to OS-Software's QAT search, and at 0.21 or less to every kernel pass and projection; on the
right at 0.72 to 0.85 to the maker's searches. By byte range the parent carries the maker's edit inside it: the
parent stands 0.0818 and 0.0698 from Google's on the layer 40 and 48 attention outputs with a leading component
(first shares 0.41 and 0.20) whose left vector stands at 0.876 and 0.930 to the leading direction of the Gembrain
edit's change at the same layers, and 0.0609 from Google's on the layer 10 attention output with none (0.053). The
copy stands 0.0185 and 0.0655 from the parent at layers 40 and 48 (first shares 0.939 and 0.976) and is byte-equal
at layer 10; its leading direction stands at 0.32 and 0.82 to the parent's leading component and at 0.38 and 0.69 on
the left and 0.79 and 0.77 on the right to the Gembrain edit's.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home on one field, no field closing. The parent publishes no
generation file and the copy adds one (`bos_token_id` 2, `eos_token_id` `[1, 106]`, `pad_token_id` 0), listed as
missing evidence on the parent's side. The parent already carries the maker's 17,344-byte template (`7fa57f97`),
taken in by the merge; the copy carries the same file with Windows line endings (17,708 bytes, `60103108`, as on
pair 6), which the tool reads as equal after line endings, and the fixed conversation renders identically. The
parent replaced its template with an 18,645-byte file on 06-12, after the pin. The version strings move from 5.8.0
to 5.9.0. The token ids are the instruct checkpoint's through the parent (`eos_token_id` `[1, 106]`, `bos_token_id`
2, `pad_token_id` 0) and the vocabulary is 262,144.

## For the recipe library

An arbitrary-rank entry with a components line, a trace line and a weight line that allows a kept fraction under
-1 on the input side would read the copy. The pinner should record a parent whose merge configuration names a
census maker's edits, so that the reading knows which directions the parent already carries. The direction
vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat47/measurements/pair-7/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
