# Reading of the Stage 1 and Stage 2 result: llmfan46/Gemma-4-Gembrain-31B-it-uncensored-heretic against Nimbz/Gemma-4-Gembrain-31B (2026-11-02)

Measured on Wheat, round 47 piece 6 (download job 387398, compare job 387404, sweep 387407; the pull carries the
measurements and the sweep record and no job log). Modified revision `a468d27a` (created 2026-05-17 22:22Z, the
weights and token files uploaded at 22:46Z and 22:47Z, the card edited until 23:05Z), parent pinned at `6c8b9228`
of 2026-05-12, Nimbz's Gembrain 31B, an `arcee_fusion` merge whose card lists google/gemma-4-31B-it, zerofata's
MeroMero, Jackrong's Gemopus, ConicCat's GarnetV2, AuriAetherwiing's Musica, Blazed-Forge's Gemsicle and
trohrbaugh's gemma-4-31b-it-heretic-ara among its sources, published as 27 float32 shards under a configuration
that declares `bfloat16`. The card is Heretic 1.2.0's arbitrary-rank table: `start_layer_index` 5,
`end_layer_index` 60, `preserve_good_behavior_weight` 0.9776, `steer_bad_behavior_weight` 0.0002,
`overcorrect_relative_weight` 1.0158, `neighbor_count` 15, `attn.o_proj` the one target, a KL divergence of 0.0186
and 13 refusals in 100 against 99. It is the maker's fifth second-generation edit in the census after findings
120, 125 and 134. The parent counts as neither an original nor a copy (finding 117).

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 31 flags (first shares 0.905 to
0.972 under the 0.99 floor), on the cluster and after re-scoring at home. On reading, the copy is the branch on 31
attention outputs inside the card's window with thirteen more left as traces, every edit on the input side, and
no layer amplified.

- 31 of 1,188 tensors changed: the attention outputs of layers 21, 26 to 28, 30 to 41, 43 and 45 to 58. Thirteen
  attention outputs of the window (layers 8 to 10, 12 to 15, 17, 19, 20, 24, 25 and 42) moved by 0.00004 to
  0.000176, the largest relative change outside the changed set; layer 59 and the window's other layers read the
  float32 rounding only.
- The copy is a bfloat16 save of a float32 parent, and the recast moves 333 other tensors by at most 0.0000012:
  the merge's values are bfloat16 values on all but a few entries.
- One direction per matrix (agreement between layers 0.025 at the median), first shares 0.905 to 0.972.
- Input side on all 31: one minus the right kept fraction 0.24 to 3.17 (3.17 at layer 52, 2.74 at 37, 2.68 at 57),
  the left side at 0.50 to 0.99; no kept fraction is above 1 on either side.
- Relative changes 0.0124 to 0.0667; rows moved 0.0007 to 0.0355, under, in and over finding 22's band under a
  card that names no row preservation.

| Layer | Change | E1 | Left kept | Right kept | Weight (one minus right kept) | Rows |
| --- | --- | --- | --- | --- | --- | --- |
| 21 | 0.0252 | 0.955 | 0.50 | -0.94 | 1.94 | 0.0013 |
| 30 | 0.0255 | 0.954 | 0.91 | -1.04 | 2.04 | 0.0072 |
| 37 | 0.0331 | 0.951 | 0.95 | -1.74 | 2.74 | 0.0229 |
| 42 | 0.0002 | - | - | - | - | 0.0001 |
| 45 | 0.0310 | 0.964 | 0.98 | -1.62 | 2.62 | 0.0071 |
| 48 | 0.0667 | 0.953 | 0.99 | -0.29 | 1.29 | 0.0355 |
| 50 | 0.0155 | 0.905 | 0.98 | 0.76 | 0.24 | 0.0144 |
| 52 | 0.0464 | 0.919 | 0.98 | -2.17 | 3.17 | 0.0185 |
| 57 | 0.0354 | 0.956 | 0.60 | -1.68 | 2.68 | 0.0065 |

The full table is in the report.

Directions. Against the saved vectors of the thirty-seven other 31B measurements, the direction stands on the left
at 0.908 to the maker's Queen edit (27 names), 0.896 to coder3101's 31B edit (31 names), 0.888 to the maker's
MeroMero edit, 0.886 to the maker's own April edit (16 names) and to coder3101's QAT edit, 0.883 to the maker's QAT
search, 0.868 and 0.865 to MoonRide's two, 0.819 to the maker's Garnet search, 0.746 to Bahushruth's, 0.735 to
densenet's, 0.731 to the maker's Harmonia edit of this round (20 names), 0.723 to wnfldchen's, 0.601 to Jim-darby's
Japanese-weighted search and 0.418 to OS-Software's QAT search, and at 0.21 or less to every kernel pass and
projection; on the right at 0.89 to 0.94 to the maker's four and coder3101's two. By byte range the layer 40 and 48
attention outputs stand 0.0255 and 0.0667 from the parent's (first shares 0.944 and 0.953) and the layer 10
attention output 0.00004; the parent stands 0.0088, 0.0098 and 0.00016 from Google's on those three matrices with
no leading component (first shares 0.040, 0.047 and 0.098), and the edit's leading direction stands at 0.10 or less
to the parent's change from Google's, so on the two layers read the trohrbaugh edit among the merge's sources
left no leading component for the search to find again.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home on two fields, no field closing. The parent publishes no
generation file and the copy adds one (`bos_token_id` 2, `eos_token_id` `[1, 106]`, `pad_token_id` 0), listed as
missing evidence on the parent's side. The template is the maker's: the copy's 17,708-byte `chat_template.jinja`
(`60103108`) is the 17,344-byte file of finding 134 with Windows line endings on its 364 lines, where the parent
carries Google's 16,934-byte revision of 04-28 (`f62ca843`); it went in with the weights on 05-17, and the same file
went onto the maker's April 31B repository on 05-18 at 17:37Z and was replaced there by the 17,344-byte file
fourteen minutes later. The two templates render the fixed conversation identically. The version strings move
from 5.6.2 to 5.8.1. The token ids are the instruct checkpoint's through the parent (`eos_token_id` `[1, 106]` in
the configuration, `bos_token_id` 2, `pad_token_id` 0 in the text configuration) and the vocabulary is 262,144.

## For the recipe library

An arbitrary-rank entry with a components line, a trace line and a weight line that allows a kept fraction under
-1 on the input side would read the copy; a recast line would name the float32 parent. The direction vectors stay
in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat47/measurements/pair-6/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
