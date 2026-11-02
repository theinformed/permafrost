# Reading of the Stage 1 and Stage 2 result: Vortex5/G4-Moonlight-Dusk-26B-A4B-heretic against Vortex5/G4-Moonlight-Dusk-26B-A4B (2026-11-02)

Measured on Nautilus, round 42 piece 4 (download job 4171128, compare job 4171132, sweep 4171137; the pull carries
the measurements and the sweep record and no job log). Modified revision `529622a2` (created 2026-07-15 01:12Z,
the weights, the tokenizer and the card uploaded at 01:17Z, a processor configuration at 01:23Z, the card revised
on 07-16), parent pinned at `fa0ae315` of 07-14, the maker's own mergekit merge (method `nexus`) of four 26B-A4B
fine-tunes, Gryphe's Pantheon-Reasoning 1.1, Locutusque's Esmeralda, Darkhn's Animus V14.1 FFT and zerofata's
MeroMero 26B-A4B (created 07-13, its shard index deleted and two files re-uploaded on 07-14). The card is Heretic
1.2.0's arbitrary-rank table under pull request 211: `start_layer_index` 3, `end_layer_index` 22,
`preserve_good_behavior_weight` 0.6457, `steer_bad_behavior_weight` 0.0003, `overcorrect_relative_weight` 1.0934,
a KL divergence of 0.0389 and 14 refusals in 100 against 100. The copy is measured against the merge its card
names and not against Google, so the pair reads the edit alone.

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 16 flags (first shares 0.002 to
0.976 under the 0.99 floor), on the cluster and after re-scoring at home. On reading, the copy is the
arbitrary-rank branch on the attention outputs of the card's window, thirteen edits on the input side with the
rows in the band and the window's first six layers left as traces.

- 16 of 1,014 tensors changed: the attention outputs of layers 3, 4, 5 and 9 to 21. The attention outputs of 6, 7
  and 8 are rewritten by 0.00088 to 0.00099, under the threshold, the largest relative change outside the changed
  set (0.000987); layer 22, the card's last, is untouched; nothing else moved on the other 995 tensors, the merge's
  128 experts a layer included.
- Thirteen edits at a few directions per matrix (first shares 0.94 to 0.98) and three traces at layers 3 to 5
  (first shares 0.002 to 0.021, both kept fractions at 1.00), finding 58's form at the window's opening.
- Input side on the thirteen: one minus the right kept fraction is 2.07 at layer 9, 1.50 to 1.94 at 10 to 14,
  2.08 at 15, 2.80 and 2.65 at 16 and 17, 1.31 at 18, 1.88 at 19, 2.25 at 20 and 2.96 at 21. Relative changes
  0.0183 to 0.0593 on the edits, 0.0010 to 0.0018 on the traces.
- Rows moved 0.0064 to 0.0077 on the thirteen edits, finding 22's band, and 0.0007 to 0.0068 on the traces.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Rows |
| --- | --- | --- | --- |
| 3 | 0.0010, 0.011, 1.00, 1.00 | - | 0.0007 |
| 4 | 0.0011, 0.021, 1.01, 1.00 | - | 0.0068 |
| 5 | 0.0018, 0.002, 1.00, 1.00 | - | 0.0008 |
| 9 | 0.0387, 0.956, 0.67, -1.07 | 2.07 | 0.0077 |
| 13 | 0.0359, 0.947, 0.79, -0.90 | 1.90 | 0.0073 |
| 16 | 0.0516, 0.965, 0.46, -1.80 | 2.80 | 0.0066 |
| 18 | 0.0344, 0.959, 0.81, -0.31 | 1.31 | 0.0072 |
| 20 | 0.0593, 0.967, 0.87, -1.25 | 2.25 | 0.0073 |
| 21 | 0.0585, 0.976, 0.22, -1.96 | 2.96 | 0.0069 |

The full table (16 rows) is in the report.

Directions. Against twenty-nine saved vectors of other measurements of the 26B-A4B, the Google-rooted family
standing in for the merge, the directions stand at 0.985 on the left and 0.981 on the right to SassyDiffusion's
search on all 13 shared names (minimum 0.869), 0.955 to llmfan46's (15), 0.947 to coder3101's (12), 0.916 and
0.871 to llmfan46's and coder3101's QAT searches, 0.76 to mewse's, 0.75 to Goodoldjam's, 0.70 to OS-Software's
Japanese search, 0.69 to Umranz's, 0.27 to tvall43's, 0.21 or less to every kernel pass and projection on the base
and 0.09 to eadx's; against the round's other 26B-A4B edits it stands at 0.957 to the maker's Chimera-X edit of
four days later (13 names, minimum 0.760) and 0.947 to SubMaroon's body (12). By byte range the layer 16 attention
output is 0.0516 from the merge's, 0.0572 from Google's, 0.0367 from SassyDiffusion's and 0.0402 from llmfan46's
(the merge 0.0246 from Google's; SassyDiffusion's and llmfan46's 0.0266 and 0.0230 from Google's, 0.0082 apart),
and the layer 4 attention output 0.0011 from the merge's and 0.0243 from Google's, the trace over the merge's own
change. The two shards (`a75ec6f9`, `e7032ab3`) match no measured file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home on `generation`: the merge, an Unsloth save, carries no
`generation_config.json` (its configuration names `eos_token_id` 106 alone, `pad_token_id` 0 and `unsloth_fixed`
true), and the copy carries one written from the configuration (`_from_model_config`, `bos_token_id` 2,
`eos_token_id` 106, `pad_token_id` 0), so the tool has nothing to compare it with; the version strings read 5.12.1
to 5.13.1. The tokenizer and the template are the merge's and the fixed conversation renders identically.

## For the recipe library

An arbitrary-rank entry with a components line would read the copy as its card with the three traces and the
three under-threshold layers at the window's opening called out. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus42/measurements/pair-4/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
