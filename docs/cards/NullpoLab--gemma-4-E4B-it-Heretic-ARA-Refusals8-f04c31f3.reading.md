# Reading of the Stage 1 and Stage 2 result: NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals8 against google/gemma-4-E4B-it (2026-11-02)

Measured on Wheat, round 39 piece 8 (download job 387181, compare job 387189, sweep 387190; the pull carries the
measurements and the sweep record and no job log). Modified revision `c2cf78ab` (created 2026-04-04 14:10Z; the
weights uploaded then, two "Upload folder" commits on 04-11 and 04-29, the last at 11:08Z), original pinned at
`292a7e27`. The card is in Japanese with an English copy beside it: Heretic 1.2.0's arbitrary-rank branch from the
tool's pull request 211, `start_layer_index` 21, `end_layer_index` 35, `preserve_good_behavior_weight` 0.9896,
`steer_bad_behavior_weight` 0.0010, `overcorrect_relative_weight` 0.4414, `neighbor_count` 15, 8 refusals in 100
against 99 in 100, a KL divergence of 0.0216. It is the maker's third E4B export in the census, after Refusals5
(round 29) and Refusals8-attn (round 37, finding 87), the attention-only sibling uploaded the next day.

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 56 flags (28 first shares, 28
within-layer cosines), on the cluster and after re-scoring at home. On reading, the copy is an arbitrary-rank edit
of both writers across the card's window, every matrix edited and none left as a residue.

- 28 of 2,130 tensors changed: both writers of layers 21 to 34, the card's `start_layer_index` 21 to
  `end_layer_index` 35 exactly. Nothing else moved; the largest relative change outside the changed set is exactly
  0 on all 2,102 other tensors.
- Twenty-eight edits, a few directions each: first shares 0.27 to 0.95 on the attention outputs and 0.23 to 0.70 on
  the down projections. The two writers of a layer are unrelated (0.004 to 0.11).
- Input side on all 28: one minus the right kept fraction is 0.83 to 1.26 on the attention outputs and 0.97 to
  1.27 on the down projections, the left side keeping 0.54 to 0.94. Rows moved 0.0011 to 0.0096, at and under
  finding 22's band rather than in it, as the maker's other two exports read (findings 56 and 87). Relative
  changes 0.0194 to 0.0561.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Down projection: change, E1, left kept, right kept | Weight | Rows |
| --- | --- | --- | --- | --- | --- |
| 21 | 0.0561, 0.273, 0.83, -0.16 | 1.16 | 0.0320, 0.351, 0.88, -0.14 | 1.14 | 0.0046, 0.0025 |
| 23 | 0.0268, 0.798, 0.89, -0.21 | 1.21 | 0.0330, 0.381, 0.82, -0.11 | 1.11 | 0.0020, 0.0042 |
| 25 | 0.0373, 0.678, 0.71, -0.01 | 1.01 | 0.0310, 0.297, 0.88, -0.18 | 1.18 | 0.0045, 0.0022 |
| 27 | 0.0236, 0.918, 0.90, -0.20 | 1.20 | 0.0335, 0.255, 0.83, -0.18 | 1.18 | 0.0021, 0.0018 |
| 29 | 0.0243, 0.753, 0.94, -0.21 | 1.21 | 0.0275, 0.453, 0.77, -0.18 | 1.18 | 0.0096, 0.0028 |
| 31 | 0.0399, 0.895, 0.66, 0.07 | 0.93 | 0.0229, 0.476, 0.86, 0.03 | 0.97 | 0.0082, 0.0025 |
| 33 | 0.0225, 0.934, 0.91, 0.17 | 0.83 | 0.0278, 0.278, 0.88, -0.10 | 1.10 | 0.0021, 0.0014 |
| 34 | 0.0362, 0.794, 0.92, -0.15 | 1.15 | 0.0362, 0.230, 0.85, -0.22 | 1.22 | 0.0031, 0.0022 |

The full table (28 rows) is in the report.

Directions. Against thirty-nine saved vectors of measurements of the E4B, the leading directions stand at 0.99 on
the left and 0.96 on the right to the maker's Refusals8-attn on all 20 shared names, 0.94 and 0.99 to coder3101's
edit (14), 0.94 and 0.96 to the maker's Refusals5 (25), 0.93 and 0.97 to llmfan46's ultra edit, 0.90 and 0.96 to
llmfan46's first edit and its three re-uploads, 0.90 and 0.93 to MoonRide's April edit (28), 0.84 and 0.96 to
JokeHer's, 0.83 and 0.92 to alphakek's and 0.82 and 0.98 to SassyDiffusion's: finding 82's E4B family, with the
maker's two Refusals8 searches at its centre. The kernel exports stand apart (0.10 to p-e-w's, lower to sh0ck0r's
and BinxNet's). The one shard (`f2c41792`) matches no measured file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster, "consistent with re-save noted" at home. The home judgement closed
`text_config.moe_intermediate_size` by the default rule under transformers 5.22.1 and the template by the
later-revision check: the copy's 16,804-byte template is byte-equal to Google's revision `c53e9d33` of 04-28
("fix(chat_template): update SI and tool call handling"), carried in by the 04-29 upload the day after Google
published it. What remains is the version strings, a re-save; the tokenizer, the token ids and the generation
settings are the pin's.

## For the recipe library

An arbitrary-rank entry would read the copy as its card. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat39/measurements/pair-8/weights.directions.safetensors`; the sibling's
are under `wheat37/measurements/pair-8/`.

Weight differences alone cannot certify the absence of hidden behavior.
