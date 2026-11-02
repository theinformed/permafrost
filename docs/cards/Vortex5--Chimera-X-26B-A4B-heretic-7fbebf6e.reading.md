# Reading of the Stage 1 and Stage 2 result: Vortex5/Chimera-X-26B-A4B-heretic against Vortex5/Chimera-X-26B-A4B (2026-11-02)

Measured on Nautilus, round 42 piece 8 (download job 4171128, compare job 4171136, sweep 4171137; the pull carries
the measurements and the sweep record and no job log). Modified revision `ed8fdc07` (created 2026-07-19 19:17Z,
the weights and the tokenizer uploaded at 19:20Z, the card at 19:21Z and revised at 19:31Z and 21:25Z, a
processor configuration at 20:10Z), parent pinned at `44f28aef` of 07-16, the maker's own multi-stage mergekit
merge (two `nearswap` stages on Darkhn's Animus V14.1 FFT and zerofata's MeroMero 26B-A4B and a `karcher` stage)
of Animus, MeroMero, Gryphe's Pantheon-Reasoning 1.1 and the maker's Moonlight-Dusk merge of pair 4 (created
07-16). The card is Heretic 1.2.0's arbitrary-rank table under pull request 211: `start_layer_index` 6,
`end_layer_index` 23, `preserve_good_behavior_weight` 0.0473, `steer_bad_behavior_weight` 0.0002,
`overcorrect_relative_weight` 0.7983, a KL divergence of 0.0392 and 12 refusals in 100 against 100. The copy is
measured against the merge its card names and not against Google, so the pair reads the edit alone; it is the
maker's second export in the round, four days after the Moonlight-Dusk edit.

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 17 flags (first shares 0.704 to
0.965 under the 0.99 floor), on the cluster and after re-scoring at home. On reading, the copy is the
arbitrary-rank branch on the attention outputs of the card's window with every layer inside edited on the input
side and the rows in the band.

- 17 of 1,014 tensors changed: the attention outputs of layers 6 to 22, every layer inside the window; the card's
  window runs to 23, where the attention output is untouched. Nothing else moved; the largest relative change
  outside the changed set is exactly 0 on all 997 other tensors, the merge's 128 experts a layer included.
- A few directions per matrix (first shares 0.70 to 0.97) and no direction shared across layers; the down
  projections untouched.
- Input side on all 17: one minus the right kept fraction is 1.32 at layer 6, 2.03 at 7, 1.54 and 1.56 at 8 and
  9, 1.35 to 1.49 from 10 to 16, 1.64 at 17, 1.10 and 1.11 at 18 and 19, 1.40 and 1.41 at 20 and 21 and 1.53 at
  22. Relative changes 0.0153 to 0.0442.
- Rows moved 0.0058 to 0.0078 on all 17, finding 22's band.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Rows |
| --- | --- | --- | --- |
| 6 | 0.0234, 0.965, 0.79, -0.32 | 1.32 | 0.0075 |
| 7 | 0.0442, 0.882, 0.30, -1.03 | 2.03 | 0.0077 |
| 10 | 0.0367, 0.705, 0.73, -0.43 | 1.43 | 0.0077 |
| 14 | 0.0221, 0.922, 0.85, -0.39 | 1.39 | 0.0072 |
| 17 | 0.0219, 0.927, 0.98, -0.64 | 1.64 | 0.0074 |
| 18 | 0.0257, 0.945, 0.88, -0.10 | 1.10 | 0.0073 |
| 20 | 0.0318, 0.943, 0.93, -0.40 | 1.40 | 0.0058 |
| 22 | 0.0276, 0.910, 0.54, -0.53 | 1.53 | 0.0076 |

The full table (17 rows) is in the report.

Directions. Against twenty-nine saved vectors of other measurements of the 26B-A4B, the Google-rooted family
standing in for the merge, the directions stand at 0.991 on the left and 0.980 on the right to llmfan46's search
on all 17 shared names (minimum 0.910), 0.984 to coder3101's (13), 0.965 to SassyDiffusion's (15), 0.961 and
0.957 to coder3101's and llmfan46's QAT searches, 0.78 to Umranz's, 0.76 to Goodoldjam's, 0.71 to mewse's, 0.66
to OS-Software's Japanese search, 0.32 to tvall43's, 0.24 or less to every kernel pass and projection on the base
and 0.10 to Mitchins's; against the round's other 26B-A4B edits it stands at 0.984 to SubMaroon's body (13 names)
and 0.957 to the maker's Moonlight-Dusk edit (13, minimum 0.760). By byte range the layer 10 attention output is
0.0367 from the merge's, 0.0413 from Google's, 0.0276 from llmfan46's, 0.0273 from the maker's Moonlight-Dusk edit
and 0.0391 from the Moonlight-Dusk merge (the Chimera-X merge 0.0189 from Google's and 0.0135 from the
Moonlight-Dusk merge; llmfan46's 0.0273 from Google's): the two edits of one maker on two merges nearer each other
than either is to its merge. The two shards (`02f203bf`, `0b3208dd`) match no measured file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home on `generation`: the merge carries no
`generation_config.json`, and the copy carries one written from the configuration (`_from_model_config`,
`bos_token_id` 2, `eos_token_id` `[1, 106]`, `pad_token_id` 0), so the tool has nothing to compare it with; the
version strings read 5.12.1 to 5.14.1. The tokenizer, the token ids and the template are the merge's and the fixed
conversation renders identically.

## For the recipe library

An arbitrary-rank entry with a components line would read the copy as its card with layer 23's absence called
out. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus42/measurements/pair-8/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
