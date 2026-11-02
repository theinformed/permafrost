# Reading of the Stage 1 and Stage 2 result: RumiaChannel/gemma-4-12B-it-uncensored-ara-Refusals4 against google/gemma-4-12B-it (2026-11-02)

Measured on Wheat, round 41 piece 1 (download job 387195, compare job 387196, sweep 387203; the pull carries the
measurements and the sweep record and no job log). Modified revision `16a8322f` (created 2026-06-05 06:36Z, seven
minutes after the maker's Refusals2 and eight before Refusals9, the card revised at 07:02Z, the template and the
tokenizer configuration updated on 07-21), original pinned at `5926caa4` of 06-04. The card is Heretic 1.2.0's
arbitrary-rank branch: `start_layer_index` 24, `end_layer_index` 37, `preserve_good_behavior_weight` 0.1819,
`steer_bad_behavior_weight` 0.0001, `overcorrect_relative_weight` 0.7372, `neighbor_count` 13, a KL divergence of
0.0090 and 4 refusals in 100 against 91 in 100. It is the maker's third 12B search in the census, after Refusals9
(round 25) and Refusals2 (round 38), the three uploaded within sixteen minutes of one morning.

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 52 flags (26 first shares, 26
within-layer cosines), on the cluster and after re-scoring at home. On reading, the copy is the arbitrary-rank
branch on both writers of the card's window, 21 edits on the input side and five down projections left as
residues.

- 26 of 677 tensors changed: both writers of layers 24 to 36, the card's `start_layer_index` 24 to
  `end_layer_index` 37. Nothing else moved; the largest relative change outside the changed set is exactly 0 on
  all 651 other tensors.
- Twenty-one edits, a few directions each: first shares 0.586 to 0.966. Five residues (finding 58): the down
  projections of layers 25, 27, 30, 32 and 34, changes of 0.0012 to 0.0018 with first shares of 0.002 to 0.006
  and both kept fractions at 1.00, the branch's small correction left where the search placed no weight. The two
  writers of a layer are unrelated (0.004 to 0.27).
- Input side on all 21 edits: one minus the right kept fraction is 0.47 to 1.71 on the attention outputs and
  0.98 to 1.15 on the down projections, the left side keeping 0.79 to 0.99. Rows moved 0.0049 to 0.0079 on the
  edits, finding 22's band, and 0.0007 to 0.0008 on the residues. Relative changes 0.0104 to 0.0307 on the edits.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Down projection: change, E1, left kept, right kept | Weight | Rows |
| --- | --- | --- | --- | --- | --- |
| 24 | 0.0204, 0.966, 0.89, -0.39 | 1.39 | 0.0166, 0.703, 0.92, -0.10 | 1.10 | 0.0077, 0.0074 |
| 25 | 0.0182, 0.966, 0.92, 0.07 | 0.93 | 0.0017, 0.006, 1.00, 1.00 | 0.00 | 0.0079, 0.0007 |
| 26 | 0.0177, 0.941, 0.86, -0.06 | 1.06 | 0.0127, 0.909, 0.83, -0.10 | 1.10 | 0.0070, 0.0072 |
| 28 | 0.0182, 0.935, 0.82, -0.03 | 1.03 | 0.0120, 0.929, 0.90, -0.08 | 1.08 | 0.0069, 0.0069 |
| 30 | 0.0190, 0.759, 0.87, 0.01 | 0.99 | 0.0018, 0.002, 1.00, 1.00 | 0.00 | 0.0079, 0.0007 |
| 31 | 0.0136, 0.947, 0.94, 0.53 | 0.47 | 0.0183, 0.586, 0.79, -0.12 | 1.12 | 0.0077, 0.0073 |
| 33 | 0.0193, 0.930, 0.94, 0.14 | 0.86 | 0.0115, 0.916, 0.80, -0.13 | 1.13 | 0.0076, 0.0049 |
| 34 | 0.0177, 0.867, 0.93, -0.24 | 1.24 | 0.0012, 0.004, 1.00, 1.00 | 0.00 | 0.0076, 0.0007 |
| 35 | 0.0121, 0.922, 0.99, 0.49 | 0.51 | 0.0104, 0.927, 0.85, -0.15 | 1.15 | 0.0072, 0.0069 |
| 36 | 0.0307, 0.916, 0.99, -0.71 | 1.71 | 0.0166, 0.601, 0.87, 0.02 | 0.98 | 0.0077, 0.0074 |

The full table (13 rows) is in the report.

Directions. Against twenty-eight saved vectors of other measurements of the 12B, the leading directions stand at
0.957 on the left and 0.993 on the right to the maker's Refusals2 on all 26 shared names (0.98 on the attention
outputs, 0.92 on the down projections; the three down projections under 0.9 are layers 24, 31 and 36 at 0.62 to
0.87, and the two residues at 0.09), at 0.937 and 0.981 to the maker's Refusals9 (26 shared; the residues on
either side at 0.02 to 0.39, the edits at 0.74 to 0.99), at 0.55 to llmfan46's 12B edit and its duplicate (13)
and 0.54 to coder3101's (26), finding 99's distance from the English-prompted searches, and at 0.19 or less to
everything else: 0.17 to huihui-ai's, 0.16 to the kernel passes (3MPER0RR's, MoonRide's, BinxNet's,
prithivMLmods's), 0.11 to TrevorJS's and its four re-uploads, 0.047 to Sabomako's of this round, 0.03 to
AEON-7's. By byte range the layer 30 attention output is 0.0190 from Google's, 0.0075 from Refusals2's and 0.0094
from Refusals9's (the two siblings 0.0046 apart), and the layer 31 down projection 0.0183 from Google's, 0.0114
from Refusals2's and 0.0119 from Refusals9's (the siblings 0.0095 apart). The one shard (`3a32d140`) matches no
measured file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster on five fields, "consistent with re-save noted" at home: the home
judgement closed the template and four configuration fields. The copy's 18,683-byte template is byte-equal to
Google's 12B revision `711c1368` of 07-15 ("fix: chat template"), carried in by the copy's 07-21 update of
`chat_template.jinja` and `tokenizer_config.json`, six weeks after the weights; the pin of 06-04 serves 17,466
bytes. The four fields (`audio_config.audio_samples_per_token`, `audio_config.hidden_size`,
`audio_config.output_proj_dims`, `vision_config.model_patch_size`) are absent on one side and load as the same
value under transformers 5.22.1. What remains is the version strings (5.10.0.dev0 to 5.10.2) and the
sub-configuration data types the cluster had already explained. The tokenizer, the token ids (`eos_token_id`
`[1, 106]`, generation `[1, 106, 50]`, `bos_token_id` 2, `pad_token_id` 0) and the generation settings are the
pin's.

## For the recipe library

An arbitrary-rank entry would read the copy as its card with the five residues named; the window is the card's
to the layer. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat41/measurements/pair-1/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
