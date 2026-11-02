# Reading of the Stage 1 and Stage 2 result: NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals3 against google/gemma-4-E4B-it (2026-11-02)

Measured on Wheat, round 41 piece 3 (download job 387195, compare job 387198, sweep 387203; the pull carries the
measurements and the sweep record and no job log). Modified revision `fdf8dd8e` (created 2026-04-04 13:57Z, the
maker's first export, twelve minutes before Refusals5 and thirteen before Refusals8, the folder uploaded again on
04-11 and twice on 04-29), original pinned at `292a7e27`, the release revision. The card is the maker's
Japanese-language form over Heretic 1.2.0's arbitrary-rank branch from the tool's pull request 211 at commit
`3b70fe5`: `start_layer_index` 19, `end_layer_index` 37, `preserve_good_behavior_weight` 0.8663,
`steer_bad_behavior_weight` 0.0165, `overcorrect_relative_weight` 0.5814, `neighbor_count` 14, a KL divergence of
0.1253 and 3 refusals in 100 against 99 in 100. It is the last of the maker's five E4B exports to be measured
(Refusals5 in round 29, Refusals8-attn in round 37, Refusals8 in round 39, Refusals6-attn in round 40).

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 52 flags (26 first shares, 26
within-layer cosines), on the cluster and after re-scoring at home. On reading, the copy is the arbitrary-rank
branch on both writers of layers 19 to 31, every matrix edited on the input side, the window ending six layers
short of the card's.

- 26 of 2,130 tensors changed: both writers of layers 19 to 31, from the card's `start_layer_index` 19 to six
  layers before its `end_layer_index` 37; the layers 32 to 36 the card's window covers are exactly 0, as the
  maker's Refusals5 (19 to 36 under a card to 42) and Refusals6-attn (21 to 36 under a card to 41) ended short
  of theirs (finding 86's selection). Nothing else moved; the largest relative change outside the changed set
  is exactly 0 on all 2,104 other tensors.
- Every matrix an edit, no residue: a few directions each, first shares 0.236 to 0.951. The two writers of a
  layer are unrelated (0.004 to 0.12).
- Input side on all 26: one minus the right kept fraction is 0.73 to 1.43 on the attention outputs and 0.94 to
  1.39 on the down projections, the left side keeping 0.53 to 0.94. Rows moved 0.0025 to 0.0184 on the
  attention outputs and 0.0011 to 0.0068 on the down projections, through and over finding 22's band at the
  layers of the largest changes, as the maker's four other exports read. Relative changes 0.0158 to 0.0673.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Down projection: change, E1, left kept, right kept | Weight | Rows |
| --- | --- | --- | --- | --- | --- |
| 19 | 0.0266, 0.908, 0.79, -0.36 | 1.36 | 0.0323, 0.356, 0.82, -0.28 | 1.28 | 0.0030, 0.0021 |
| 20 | 0.0470, 0.375, 0.90, -0.43 | 1.43 | 0.0341, 0.348, 0.84, -0.32 | 1.32 | 0.0079, 0.0020 |
| 22 | 0.0604, 0.294, 0.76, -0.41 | 1.41 | 0.0384, 0.312, 0.90, -0.03 | 1.03 | 0.0176, 0.0027 |
| 24 | 0.0531, 0.440, 0.53, -0.11 | 1.11 | 0.0158, 0.890, 0.85, 0.06 | 0.94 | 0.0184, 0.0016 |
| 25 | 0.0358, 0.589, 0.70, -0.00 | 1.00 | 0.0276, 0.383, 0.82, -0.33 | 1.33 | 0.0041, 0.0016 |
| 27 | 0.0440, 0.318, 0.86, -0.33 | 1.33 | 0.0350, 0.250, 0.82, -0.37 | 1.37 | 0.0091, 0.0022 |
| 29 | 0.0167, 0.951, 0.94, 0.27 | 0.73 | 0.0248, 0.475, 0.77, -0.14 | 1.14 | 0.0093, 0.0024 |
| 30 | 0.0673, 0.236, 0.88, -0.01 | 1.01 | 0.0223, 0.508, 0.84, -0.11 | 1.11 | 0.0167, 0.0018 |
| 31 | 0.0578, 0.529, 0.73, -0.18 | 1.18 | 0.0247, 0.361, 0.82, -0.11 | 1.11 | 0.0080, 0.0019 |

The full table (13 rows) is in the report.

Directions. Against thirty-nine saved vectors of other measurements of the E4B, the leading directions stand at
0.982 on the left to the maker's Refusals8 on 22 shared names (0.984 on the attention outputs, 0.955 on the down
projections), 0.955 to Refusals6-attn (21), 0.949 to Refusals8-attn (22) and 0.929 to Refusals5 (21), at 0.87 to
coder3101's E4B edit (11), 0.86 to llmfan46's two and their duplicates (9 and 12), 0.84 to alphakek's, 0.83 to
SassyDiffusion's, 0.81 to JokeHer's and 0.79 to MoonRide's arbitrary-rank search, finding 82's family with the
maker's own exports at its centre, and at 0.68 to Bahushruth's, 0.42 to OS-Software's, 0.37 to TrevorJS's and
its re-upload, 0.35 to TheUmbraWalker's, 0.095 to p-e-w's two exports, 0.093 to ImanolSuarez's of this round and
0.011 to huihui-ai's. By byte range the layer 29 attention output is 0.0167 from Google's, 0.0175 from
Refusals8's and 0.0314 from Refusals6-attn's, and the layer 29 down projection 0.0248 from Google's, 0.0136 from
Refusals8's and 0.0144 from Refusals6-attn's. The one shard (`079aeeb1`) matches no measured file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster on two fields, "consistent with re-save noted" at home: the home
judgement closed the template and `text_config.moe_intermediate_size`. The copy's 16,804-byte template is
byte-equal to Google's E4B revision `c53e9d33` of 04-28 ("fix(chat_template): update SI and tool call
handling"), carried in by the copy's 04-29 upload, as the maker's Refusals8 and Refusals6-attn carried it in
rounds 39 and 40; the release revision serves 11,926 bytes. What remains is the version strings (5.5.0.dev0 to
5.5.0). The tokenizer, the token ids (`eos_token_id` `[1, 106]`, generation `[1, 106, 50]`) and the generation
settings are the pin's.

## For the recipe library

An arbitrary-rank entry would read the copy as its card with the window's end at 31 named against the card's
37. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat41/measurements/pair-3/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
