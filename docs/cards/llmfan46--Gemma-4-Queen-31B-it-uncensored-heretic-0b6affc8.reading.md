# Reading of the Stage 1 and Stage 2 result: llmfan46/Gemma-4-Queen-31B-it-uncensored-heretic against aifeifei798/Gemma-4-Queen-31B-it (2026-11-02)

Measured on Nautilus, round 42 piece 3 (download job 4171128, compare job 4171131, sweep 4171137; the pull carries
the measurements and the sweep record and no job log). Modified revision `368f8275` (created 2026-04-12 18:50Z,
the folder uploaded at 19:20Z, the card at 21:08Z and revised twice that evening, the template deleted on 05-04
and re-uploaded on 05-05), parent pinned at `58bee46f` of 04-10, aifeifei798's fine-tune of google/gemma-4-31B-it
in sixty-five shards (created 04-10 18:54Z, its card a set of reasoning tests against larger models). The card is
Heretic 1.2.0's arbitrary-rank table under pull request 211: `start_layer_index` 26, `end_layer_index` 56,
`preserve_good_behavior_weight` 0.8555, `steer_bad_behavior_weight` 0.0005, `overcorrect_relative_weight` 0.9911,
a KL divergence of 0.0707 and 12 refusals in 100 against 99. The copy is measured against the fine-tune its card
names and not against Google, so the pair reads the edit alone; it is the maker's earliest export in the round,
two days after the parent.

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 30 flags (first shares 0.911 to
0.986 under the 0.99 floor), on the cluster and after re-scoring at home. On reading, the copy is the
arbitrary-rank branch on the attention outputs of the card's window with every layer inside edited on the input
side, one of them amplified by 6.71.

- 30 of 1,188 tensors changed: the attention outputs of layers 26 to 55, every layer inside the window; the card's
  window runs to 56, where the attention output is untouched. Nothing else moved; the largest relative change
  outside the changed set is exactly 0 on all 1,158 other tensors, the parent's fine-tuned layers included.
- A few directions per matrix (first shares 0.91 to 0.99) and no direction shared across layers; the down
  projections untouched.
- Input side on all 30: one minus the right kept fraction is 1.19 to 3.70 on 28 matrices (3.08 at 45, 2.95 at 46,
  3.70 at 52), 0.26 at layer 48, and at layer 50 the right kept fraction is 6.71, the component multiplied by
  6.71 rather than removed, at a relative change of 0.1205, the largest input-side reading in the census.
  Relative changes 0.0157 to 0.1205.
- Rows moved 0.0006 to 0.197, through and over finding 22's band, the layer 50 row at 0.197 under the 6.71 and
  the layers 37, 45, 46 and 48 rows at 0.026 to 0.048.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Rows |
| --- | --- | --- | --- |
| 26 | 0.0210, 0.977, 0.83, -0.63 | 1.63 | 0.0045 |
| 30 | 0.0339, 0.971, 0.87, -1.55 | 2.55 | 0.0132 |
| 37 | 0.0407, 0.963, 0.94, -1.78 | 2.78 | 0.0409 |
| 45 | 0.0666, 0.975, 0.95, -2.08 | 3.08 | 0.0256 |
| 46 | 0.0716, 0.976, 0.91, -1.95 | 2.95 | 0.0478 |
| 48 | 0.0592, 0.969, 1.00, 0.74 | 0.26 | 0.0349 |
| 50 | 0.1205, 0.918, 1.03, 6.71 | -5.71 | 0.1968 |
| 52 | 0.0540, 0.961, 0.98, -2.70 | 3.70 | 0.0197 |
| 55 | 0.0263, 0.944, 0.98, -0.38 | 1.38 | 0.0233 |

The full table (30 rows) is in the report.

Directions. Against thirty saved vectors of other measurements of the 31B, the Google-rooted family standing in
for the parent, the directions stand at 0.993 on the left and 0.991 on the right to the maker's own April 31B
edit on all 18 shared names (minimum 0.443), 0.968 to MoonRide's search (24), 0.964 to coder3101's (30), 0.953 to
MoonRide's custom-prompt search, 0.932 and 0.915 to the maker's and coder3101's QAT searches, 0.84 to wnfldchen's
merged search, 0.78 to Bahushruth's, 0.556 to Jim-darby's Japanese-weighted search (finding 108's distance), 0.39
to OS-Software's, 0.20 or less to every kernel pass and projection on the base and 0.012 to cosmicoptima's;
against the maker's MeroMero edit of this round it stands at 0.887 on 19 names and at 0.145 to bgg1996's pass. By
byte range the layer 50 attention output is 0.1195 from the parent's, 0.1195 from Google's and 0.1195 from the
maker's April edit, which leaves layer 50 byte-equal to Google's (the parent 0.0032 from Google's), and the layer
45 attention output 0.0665 from the parent's, 0.0665 from Google's and 0.0187 from the maker's April edit (which
is 0.0745 from Google's at that layer): the two edits of one maker nearer each other than either is to its
parent where both edit the layer. The two shards (`4dac5c0f`, `30d9f3d8`) match no measured file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home on `template.default`: the copy's 17,344-byte template is
the maker's own, carried in by the delete and re-upload of 05-04 and 05-05 three weeks after the weights, the day
the maker's own 31B repository first carried it, in place of the parent's 12,045-byte template, Google's release
revision `419b2efe` of 04-02; the fixed conversation renders identically under both. The version strings, the
token ids (`eos_token_id` `[1, 106]`, generation `[1, 106, 50]`, `bos_token_id` 2, `pad_token_id` 0) and the
generation settings are the parent's.

## For the recipe library

An arbitrary-rank entry with a components line would read the copy as its card with layer 56's absence called
out, and a weight line that allows a kept fraction above 1 would print the layer 50 amplification, which no entry
has a word for. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus42/measurements/pair-3/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
