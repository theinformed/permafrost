# Reading of the Stage 1 and Stage 2 result: llmfan46/Gemma-4-Garnet-V2-31B-it-ultra-uncensored-heretic against ConicCat/Gemma4-GarnetV2-31B (2026-11-02)

Measured on Wheat, round 45 piece 7 (download job 387355, compare job 387362, sweep 387364; the pull carries the
measurements and the sweep record and no job log). Modified revision `3ab379e5` (created 2026-04-25 22:14Z, the
weights and token files uploaded within four minutes, the template replaced on 05-04 and again on 05-05), parent
pinned at `74f74a1b` of 2026-04-24, ConicCat's GarnetV2 fine-tune of google/gemma-4-31B-it (created 04-21), a merged
rank-64 adapter on every projection of the language model whose adapter the repository also publishes, with
Google's configuration, `tokenizer.json` and 04-10 template by object id. The card is Heretic 1.2.0's
arbitrary-rank table: `start_layer_index` 25, `end_layer_index` 46, `preserve_good_behavior_weight` 0.4482,
`steer_bad_behavior_weight` 0.0002, `overcorrect_relative_weight` 1.0104, `neighbor_count` 10, `attn.o_proj` the one
target, a KL divergence of 0.0167 and 4 refusals in 100 against 99, above an MMLU table. It is the maker's fourth
second-generation edit in the census after findings 120 and 125, and the sixth repository of the maker's in the
census with "ultra" in its name.

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 20 flags (first shares 0.917 to
0.981 under the 0.99 floor), on the cluster and after re-scoring at home. On reading, the copy is the branch on the
attention outputs of layers 25 to 45 with one layer rewritten below the threshold, every edit on the input side,
and no layer amplified.

- 20 of 1,188 tensors changed: the attention outputs of layers 25 to 28 and 30 to 45. Layer 29's attention output
  moved by 0.000116 (1.9 percent of its entries, by at most 0.00098), under the threshold, so the largest relative
  change outside the changed set is 0.000116, inside the window; layer 46, the card's `end_layer_index`, is
  untouched, as are the down projections, the vision tower and the embeddings.
- One direction per matrix (agreement between layers 0.059 at the median), first shares 0.917 to 0.981.
- Input side on all 20: one minus the right kept fraction 1.31 to 2.66 (2.66 at layer 42, 2.25 at 30, 2.14 at 36,
  2.05 at 45), the left side at 0.04 to 0.42; no kept fraction is above 1 on either side, so no component is
  amplified as finding 120 read on the Queen and MeroMero edits.
- Relative changes 0.0101 to 0.0367; rows moved 0.0003 to 0.0377, under finding 22's band on eleven layers, in it
  on two and over it on seven (0.0377 at layer 43, 0.0155 at 42, 0.0142 at 33).

| Layer | Change | E1 | Left kept | Right kept | Weight (one minus right kept) | Rows |
| --- | --- | --- | --- | --- | --- | --- |
| 25 | 0.0267 | 0.953 | 0.75 | -0.54 | 1.54 | 0.0037 |
| 28 | 0.0214 | 0.950 | 0.90 | -0.52 | 1.52 | 0.0024 |
| 29 | 0.0001 | - | - | - | - | 0.0000 |
| 30 | 0.0328 | 0.935 | 0.83 | -1.25 | 2.25 | 0.0077 |
| 33 | 0.0309 | 0.940 | 0.82 | -0.44 | 1.44 | 0.0142 |
| 36 | 0.0222 | 0.952 | 0.71 | -1.14 | 2.14 | 0.0017 |
| 39 | 0.0269 | 0.957 | 0.70 | -0.90 | 1.90 | 0.0061 |
| 42 | 0.0367 | 0.918 | 0.71 | -1.66 | 2.66 | 0.0155 |
| 43 | 0.0260 | 0.951 | 0.72 | -0.79 | 1.79 | 0.0377 |
| 45 | 0.0261 | 0.937 | 0.96 | -1.05 | 2.05 | 0.0094 |

The full table (21 rows) is in the report.

Directions. Against the saved vectors of the thirty-four 31B measurements, the direction stands on the left at
0.875 to the maker's 31B QAT search (10 names), 0.850 to coder3101's QAT edit, 0.807 to the maker's MeroMero edit,
0.804 to coder3101's 31B edit (20 names), 0.802 to the maker's Queen edit, 0.789 and 0.775 to MoonRide's two
searches, 0.781 to the maker's own April edit (16 names), 0.700 to Bahushruth's, 0.678 to wnfldchen's merged
search, 0.623 to densenet's StyleTune edit, 0.549 to Jim-darby's Japanese-weighted search and 0.406 to
OS-Software's QAT search, and at 0.15 or less to every kernel pass and projection (TrevorJS's 0.135, bgg1996's
0.135, huihui-ai's 0.07 to 0.08, cosmicoptima's 0.009); on the right at 0.83 to 0.88 to the maker's four and
coder3101's. By byte range the layer 42 attention output is 0.0367 from the parent's, 0.0507 from Google's, 0.0473
from the maker's April edit and 0.0470 from coder3101's, the parent itself 0.0350 from Google's there (the April edit
0.0214 and coder3101's 0.0326); the layer 10 query projection and the layer 35 down projection are byte-equal to
the parent's and stand 0.035 and 0.027 from Google's, where the April edit and coder3101's are Google's bytes; the
parent's change from Google's has no leading component (first shares 0.12 to 0.32 on the four matrices read).

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster on two fields and at home on one, the home judgement closing
`config.text_config.moe_intermediate_size` (absent on the parent's side and loaded as the same default). The one
field left is the template: the copy's 17,344-byte `chat_template.jinja` (`7fa57f97`) where the parent carries
Google's 16,448-byte revision of 04-10 (`98da08eb`). The copy's history reads the maker's habit of finding 120: at
upload a 16,795-byte template (`fbedf236`), on 05-04 at 01:58Z Google's 16,934-byte revision of 04-28 three minutes
after the same file went onto the maker's April 31B repository, and on 05-05 at 17:01Z the maker's own 17,344-byte
file, three minutes after it went onto the April repository too; the two templates render the fixed conversation
identically. The configuration (`6d6fac89`) is the maker's April repository's file by object id, the version string
5.5.0.dev0 to 5.5.0. The token ids are the instruct checkpoint's through the parent (`eos_token_id` `[1, 106]`,
generation `[1, 106, 50]`, `bos_token_id` 2, `pad_token_id` 0) and the vocabulary is 262,144.

## For the recipe library

An arbitrary-rank entry with a components line and a weight line that allows a kept fraction under -1 on the input
side would read the copy, with layer 29 named as the window's one rewritten layer. The direction vectors stay in
the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat45/measurements/pair-7/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
