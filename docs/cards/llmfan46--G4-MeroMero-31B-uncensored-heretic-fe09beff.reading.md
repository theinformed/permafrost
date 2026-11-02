# Reading of the Stage 1 and Stage 2 result: llmfan46/G4-MeroMero-31B-uncensored-heretic against zerofata/G4-MeroMero-31B (2026-11-02)

Measured on Nautilus, round 42 piece 2 (download job 4171128, compare job 4171130, sweep 4171137; the pull carries
the measurements and the sweep record and no job log). Modified revision `c0add38f` (created 2026-05-15 22:29Z,
the weights and the card uploaded at 22:32Z, the template deleted at 22:49Z and re-uploaded at 23:03Z, the card
revised on 05-26), parent pinned at `35611a07` of 05-02, zerofata's fine-tune of google/gemma-4-31B-it (created
04-30, "A finetune of Gemma 4 31B designed for creative tasks" on the maker's `Gemini-3.1-Pro-GLM5-Characters`
set, a mergekit configuration deleted on 05-01). The card is Heretic 1.2.0's arbitrary-rank table under pull
request 211: `start_layer_index` 28, `end_layer_index` 49, `preserve_good_behavior_weight` 0.5600,
`steer_bad_behavior_weight` 0.0001, `overcorrect_relative_weight` 0.9726, a KL divergence of 0.0100 and 15
refusals in 100 against 99. The copy is measured against the fine-tune its card names and not against Google, so
the pair reads the edit alone.

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 19 flags (first shares 0.892 to
0.967 under the 0.99 floor), on the cluster and after re-scoring at home. On reading, the copy is the
arbitrary-rank branch on the attention outputs of the card's window, every edit on the input side, one layer
absent, one traced and one amplified.

- 19 of 1,188 tensors changed: the attention outputs of layers 28 to 41, 43 to 45, 47 and 48. Layer 42 is
  untouched and layer 46 is rewritten by 0.000003, the largest relative change outside the changed set and the
  round's one non-zero reading inside a window; nothing else moved on the other 1,168 tensors, the parent's
  fine-tuned layers included. The card's window runs to 49, where the attention output is untouched.
- A few directions per matrix (first shares 0.89 to 0.97) and no direction shared across layers (the writers of a
  layer unrelated, the down projections untouched).
- Input side on 18: one minus the right kept fraction is 1.12 at layer 28, 1.55 to 1.73 at 29 to 32, 0.90 at 35,
  1.97 at 40, 1.30 to 1.77 elsewhere; at layer 48 the right kept fraction is 1.34, the component multiplied rather
  than removed, at a relative change of 0.0488, twice any other. Relative changes 0.0125 to 0.0488.
- Rows moved 0.0009 to 0.0245, under and over finding 22's band of 0.005 to 0.008, the layer 48 row at 0.0245.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Rows |
| --- | --- | --- | --- |
| 28 | 0.0199, 0.942, 0.77, -0.12 | 1.12 | 0.0017 |
| 30 | 0.0239, 0.946, 0.92, -0.73 | 1.73 | 0.0042 |
| 35 | 0.0142, 0.920, 0.92, 0.10 | 0.90 | 0.0034 |
| 40 | 0.0266, 0.924, 0.74, -0.97 | 1.97 | 0.0046 |
| 41 | 0.0125, 0.905, 0.87, -0.47 | 1.47 | 0.0009 |
| 44 | 0.0255, 0.951, 0.94, -0.46 | 1.46 | 0.0104 |
| 45 | 0.0260, 0.960, 0.98, -0.77 | 1.77 | 0.0027 |
| 46 | 0.000003, -, -, - | - | - |
| 48 | 0.0488, 0.927, 1.00, 1.34 | -0.34 | 0.0245 |

The full table (19 rows) is in the report.

Directions. Against thirty saved vectors of other measurements of the 31B, the Google-rooted family standing in
for the parent, the directions stand at 0.939 on the left and 0.946 on the right to coder3101's 31B edit on all 19
shared names (minimum 0.240), 0.916 to MoonRide's search (17), 0.899 and 0.891 to coder3101's and the maker's QAT
searches, 0.890 to the maker's own April 31B edit (16; 0.942 on the right), 0.859 to MoonRide's custom-prompt
search, 0.71 to Bahushruth's and wnfldchen's, 0.51 to Jim-darby's Japanese-weighted search, 0.38 to OS-Software's,
0.15 or less to every kernel pass and projection on the base and 0.009 to cosmicoptima's; against the maker's
Queen edit of this round it stands at 0.887 on the left (minimum 0.625) and 0.953 on the right on 19 names, and
at 0.131 to bgg1996's pass. By byte range the layer 40 attention output is 0.0266 from the parent's, 0.0268 from
Google's, 0.0217 from coder3101's and 0.0237 from the maker's April edit (the parent 0.0035 from Google's;
coder3101's and the maker's 0.0138 and 0.0302 from Google's, 0.0226 apart), the layer 48 attention output 0.0487
from the parent's and 0.0488 from Google's (the parent 0.0037 from Google's), and the layer 46 attention output
equal to the parent's to four decimals with the bytes not equal, the trace. The two shards (`80055a88`,
`b41e8051`) match no measured file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home on `template.default`: the copy's 17,344-byte template is
the one the maker's own 31B repository has carried since 05-05 (and carried into the Queen edit of this round the
same day), in place of the parent's 16,934-byte template, Google's 31B revision `145dc250` of 04-28, which
zerofata uploaded on 05-01; the fixed conversation renders identically under both. The version strings read
5.7.0 to 5.8.1 in the configuration and 5.5.0.dev0 to 5.8.1 in the generation file. The token ids (`eos_token_id`
`[1, 106]`, generation `[1, 106, 50]`, `bos_token_id` 2, `pad_token_id` 0) and the generation settings are the
parent's.

## For the recipe library

An arbitrary-rank entry with a components line would read the copy as its card with layer 42's absence and layer
46's trace called out, and a weight line that allows a kept fraction above 1 would print the layer 48
amplification. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus42/measurements/pair-2/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
