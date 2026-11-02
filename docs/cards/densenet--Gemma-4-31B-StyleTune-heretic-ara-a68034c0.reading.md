# Reading of the Stage 1 and Stage 2 result: densenet/Gemma-4-31B-StyleTune-heretic-ara against Gryphe/Gemma-4-31B-StyleTune (2026-11-02)

Measured on Wheat, round 43 piece 2 (download job 387204, compare job 387206, sweep 387213; the pull carries the
measurements and the sweep record and no job log). Modified revision `dd58d6a1` (created 2026-07-09 07:20Z, an
Unsloth save with `unsloth_version` 2026.7.2 and "Trained with Unsloth" commit titles), parent pinned at
`5a46842f` of 06-14, Gryphe's StyleTune of google/gemma-4-31B-it (created 06-10), whose card says one tensor
changed out of 834, the `lm_head` alone. The card is Heretic 1.2.0's arbitrary-rank table under pull request 211
"with row-norm preservation": `start_layer_index` 30, `end_layer_index` 48, `preserve_good_behavior_weight`
0.8437, `steer_bad_behavior_weight` 0.0025, `overcorrect_relative_weight` 0.9644, `neighbor_count` 15, a KL
divergence of 0.0733 and 8 refusals in 100 against 99. The copy is measured against the fine-tune its card names,
so the pair reads the edit alone; by byte range the parent's layers are Google's (below).

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 66 flags (36 direction cosines
and 30 first shares of 0.859 to 0.989), on the cluster and after re-scoring at home. On reading, the copy is the
arbitrary-rank branch on both writers of layers 30 to 47, every edit on the input side, with the largest row
movement in the census under a card that claims the rows were preserved.

- 36 of 1,189 tensors changed: the attention outputs and the down projections of layers 30 to 47. The card's
  window runs to 48, where both writers are untouched; nothing moved on the other 1,153 tensors, the `lm_head`
  the parent trained included. The largest relative change outside the changed set is exactly 0.
- A few directions per matrix (first shares 0.86 to 0.999) and no direction shared across layers (median
  agreement 0.25, minimum 0.05); the two writers of a layer are unrelated (cross-kind agreement 0.0001).
- Input side on all 36: one minus the right kept fraction is 0.84 to 4.36 on the attention outputs (4.36 at layer
  46, 3.34 at 34 and 41, 0.84 at 43) and 2.10 to 3.35 on the down projections. Relative changes 0.055 to 0.279
  (layer 44's attention output 0.2790, layer 46's 0.2453, layer 45's 0.1939, layer 37's 0.1440), the largest
  relative changes of any arbitrary-rank edit in the census.
- Rows moved 0.019 to 0.777: 0.7769 on layer 46's attention output, 0.4769 on 44's, 0.4435 on 37's, 0.3844 on
  43's, 0.2781 on 47's and 0.2247 on 45's; 0.019 to 0.066 on the down projections. The band of 0.005 to 0.008
  (finding 22) is passed on every matrix.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Down projection: change, E1, left kept, right kept | Weight | Rows (attention, down) |
| --- | --- | --- | --- | --- | --- |
| 30 | 0.0847, 0.871, 0.61, -1.33 | 2.33 | 0.0772, 0.950, 0.67, -1.29 | 2.29 | 0.1215, 0.0388 |
| 34 | 0.0940, 0.931, 0.80, -2.34 | 3.34 | 0.0755, 0.943, 0.59, -1.85 | 2.85 | 0.0914, 0.0541 |
| 37 | 0.1440, 0.993, 0.23, -2.19 | 3.19 | 0.0724, 0.916, 0.58, -1.70 | 2.70 | 0.4435, 0.0508 |
| 40 | 0.0780, 0.998, 0.30, -1.17 | 2.17 | 0.0825, 0.954, 0.54, -2.03 | 3.03 | 0.0513, 0.0643 |
| 43 | 0.0891, 0.887, 0.81, 0.16 | 0.84 | 0.0624, 0.909, 0.54, -1.74 | 2.74 | 0.3844, 0.0454 |
| 44 | 0.2790, 0.997, 0.04, -1.84 | 2.84 | 0.0578, 0.859, 0.65, -1.48 | 2.48 | 0.4769, 0.0262 |
| 45 | 0.1939, 0.998, 0.53, -1.66 | 2.66 | 0.0778, 0.952, 0.52, -1.93 | 2.93 | 0.2247, 0.0658 |
| 46 | 0.2453, 0.989, 0.25, -3.36 | 4.36 | 0.0550, 0.871, 0.77, -1.46 | 2.46 | 0.7769, 0.0189 |
| 47 | 0.1230, 0.999, 0.69, -1.65 | 2.65 | 0.0686, 0.932, 0.66, -1.43 | 2.43 | 0.2781, 0.0374 |

The full table (18 rows) is in the report.

Directions. Against the saved vectors of other measurements of the 31B, the Google-rooted family standing in for
the parent, the attention outputs (18 names) stand at 0.951 on the left and 0.738 on the right to wnfldchen's
merged search (minimum 0.179), 0.910 and 0.448 to llmfan46's April 31B edit, 0.875 and 0.446 to
llmfan46's Queen edit of round 42, 0.812 and 0.387 to llmfan46's QAT search, 0.793 and 0.346 to MoonRide's
custom-prompt search, 0.761 and 0.433 to coder3101's 31B edit, 0.758 and 0.428 to Bahushruth's, 0.669 to
llmfan46's MeroMero 31B edit of round 42, 0.539 to MoonRide's arbitrary-rank search, 0.442 to Jim-darby's
Japanese-weighted search, 0.28 or less to every kernel pass and projection on the base, 0.210 to bgg1996's pass
and 0.011 to cosmicoptima's. The left side agrees with the family and the right does not, the two sides of an
arbitrary-rank edit whose right factors carry weights of 2 to 4. By byte range the layer 44 attention output is
0.2750 from the parent's and from Google's, 0.2653 from llmfan46's April 31B edit, 0.2657 from the Queen edit and
0.2619 from coder3101's, the layer 46 attention output 0.2406 from the parent's and from Google's and 0.2143 from
llmfan46's April edit, and the parent's layers 44 and 46 are byte-equal to Google's (llmfan46's April edit 0.0404
and 0.0639 from Google's at 44 and 46, the Queen edit 0.0354 and coder3101's 0.0354 at 44), the layer 44 down projection 0.0576 from the parent's and from Google's, the layer 10 query projection byte-equal to the parent's and to Google's, and the `lm_head` byte-equal to the parent's, the one tensor the fine-tune trained left as it was. The shards
match no measured file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster on 37 fields and at home on 7. The home judgement under transformers
5.22.1 with the parent's later commits closed the 24 `added_tokens_decoder` entries and `added_tokens.decoder`,
which repeat the added-token record of the `tokenizer.json` both sides share, and left `config.dtype`,
`config.torch_dtype`, `config.model_name`, `config.text_config.use_cache`, `config.transformers_version`,
`config.unsloth_version` and `template_source.tokenizer_config`: the Unsloth save wrote `torch_dtype` in place of
`dtype`, `use_cache` false, `model_name` and `unsloth_version` 2026.7.2, dropped the configuration's version
string (5.9.0 to none; the generation file reads 5.9.0 to 5.5.0) and copied the template into
`tokenizer_config.json` (24,234 bytes against the parent's 2,719), the parent's 16,934-byte `chat_template.jinja`
(Google's 31B revision `145dc250` of 04-28) staying byte-equal. The token ids (`eos_token_id` 106, `pad_token_id`
0, generation `[1, 106, 50]`, `bos_token_id` 2) are the parent's, an Unsloth form on both sides.

## For the recipe library

An arbitrary-rank entry with a components line and a weight line allowing a kept fraction above 1 would read the
window and the weights; no rule reads a preservation claim, and finding 84's case (wnfldchen's) now has a second
instance with rows to 0.777. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat43/measurements/pair-2/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
