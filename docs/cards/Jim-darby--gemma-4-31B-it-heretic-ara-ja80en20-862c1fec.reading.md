# Reading of the Stage 1 and Stage 2 result: Jim-darby/gemma-4-31B-it-heretic-ara-ja80en20 against google/gemma-4-31B-it (2026-11-02)

Measured on Nautilus, round 40 piece 5 (download job 4169647, compare job 4169652, sweep 4169656; the pull carries
the measurements and the sweep record and no job log). Modified revision `9c2c9c8f` (created 2026-05-26 14:14Z,
the weights and tokenizer uploaded at 18:50Z, the card revised the next morning), original pinned at `fcf23027`
of 05-18, the first measurement against this revision. The card is Heretic 1.2.0's arbitrary-rank branch with
the maker's own section over it: "Selected optimization run: Trial 82", "Primary optimization languages: Japanese
and English", "Row normalization: none", `start_layer_index` 27, `end_layer_index` 47,
`preserve_good_behavior_weight` 0.7927, `steer_bad_behavior_weight` 0.00012, `overcorrect_relative_weight`
0.0175, `neighbor_count` 10; the direction prompts 400 harmless and 400 harmful at "80 percent Japanese, 20
percent English" from `ChiKoi7/harmful_behaviors_ja`, `ChiKoi7/harmless_alpaca_ja`, `mlabonne/harmful_behaviors`
and `mlabonne/harmless_alpaca`; 0 refusals in 100 against 93 in 100 and a KL divergence of 0.0781 on the harmless
prompts. It is the census's first 31B search on a Japanese-weighted prompt set, after OS-Software's 26B-A4B search
of round 37 (finding 93) and the two E4B and E2B cases of findings 83 and 99.

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 74 flags (38 first shares, 36
within-layer cosines), on the cluster and after re-scoring at home. On reading, the copy is the arbitrary-rank
branch on both writers across the card's window, 32 edits on the input side and six matrices left as residues.

- 38 of 1,188 tensors changed: the attention outputs of layers 27 to 46 (all 20) and the down projections of 18
  of them, the card's `start_layer_index` 27 to `end_layer_index` 47 exactly. Two down projections inside the
  window stayed under the threshold (layer 32 at 0.00068, layer 38 at 0.000983, the largest relative change
  outside the changed set); the other 1,148 tensors are exactly 0.
- Thirty-two edits, a few directions each: first shares 0.29 to 0.91. Six residues (finding 58): the attention
  outputs of layers 27, 28, 29, 32 and 35 and the down projection of 37, changes of 0.0012 to 0.0018 with first
  shares of 0.003 to 0.007, the branch's small correction left where the search placed no weight. The two writers
  of a layer are unrelated (0.0005 to 0.15).
- Input side on all 32 edits: one minus the right kept fraction is 0.66 to 1.10, the left side keeping 0.74 to
  0.99. Rows moved 0.0050 to 0.0078 on the 32 edits, finding 22's band, and 0.0007 to 0.0008 on the six residues:
  the branch's row-norm preservation, read in the rows under a card that says "Row normalization: none":
  whatever the card's line names, the rows carry the band. Relative changes
  0.0041 to 0.0212 on the edits.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Down projection: change, E1, left kept, right kept | Weight | Rows |
| --- | --- | --- | --- | --- | --- |
| 27 | 0.0018, 0.005, 1.00, 1.00 | 0.00 | 0.0099, 0.838, 0.86, 0.07 | 0.93 | 0.0008, 0.0050 |
| 29 | 0.0014, 0.007, 1.00, 1.00 | 0.00 | 0.0154, 0.548, 0.94, 0.12 | 0.88 | 0.0007, 0.0077 |
| 30 | 0.0124, 0.914, 0.96, 0.01 | 0.99 | 0.0114, 0.775, 0.95, 0.18 | 0.82 | 0.0072, 0.0076 |
| 32 | 0.0018, 0.007, 1.00, 1.01 | -0.01 | - | - | 0.0008, - |
| 35 | 0.0015, 0.003, 1.00, 1.00 | 0.00 | 0.0153, 0.445, 0.92, -0.04 | 1.04 | 0.0008, 0.0072 |
| 37 | 0.0132, 0.838, 0.95, 0.04 | 0.96 | 0.0012, 0.004, 1.00, 1.00 | 0.00 | 0.0064, 0.0007 |
| 38 | 0.0136, 0.862, 0.94, 0.03 | 0.97 | - | - | 0.0074, - |
| 39 | 0.0142, 0.832, 0.86, 0.13 | 0.87 | 0.0212, 0.293, 0.84, -0.06 | 1.06 | 0.0073, 0.0065 |
| 43 | 0.0162, 0.498, 0.97, -0.02 | 1.02 | 0.0112, 0.458, 0.84, -0.05 | 1.05 | 0.0072, 0.0060 |
| 46 | 0.0146, 0.786, 0.74, 0.05 | 0.95 | 0.0124, 0.467, 0.82, -0.06 | 1.06 | 0.0073, 0.0055 |

The full table (20 rows) is in the report.

Directions. Against twenty-six saved vectors of other measurements of the 31B, the leading directions stand at
0.64 on the left to llmfan46's QAT edit (9 shared names), 0.62 to coder3101's QAT edit (12), 0.60 and 0.54 to
coder3101's first export (20), 0.54 to Bahushruth's (38), 0.51 and 0.60 to llmfan46's (17), 0.51 and 0.62 to
MoonRide's custom-prompt search (29), 0.46 to OS-Software's QAT edit, 0.41 and 0.57 to MoonRide's first search
(30), and at 0.23 or less to the kernel passes (germlag's, ressl's, TrevorJS's, 3MPER0RR's, Vampelium's), 0.13 to
DuoNeural's, 0.08 to huihui-ai's and 0.011 to cosmicoptima's. The English-prompted 31B arbitrary-rank searches
stand to each other at 0.87 to 0.97 (MoonRide's two at 0.869, MoonRide's custom to coder3101's 0.951 and to
llmfan46's 0.971, coder3101's to llmfan46's 0.943); the Japanese-weighted search stands to all of them at 0.41 to
0.62, the same distance findings 83, 93 and 99 read on the E4B, the 26B-A4B and the E2B. The sixty-five shards
(`ebf478b6` to `a4cc80e4`) match no measured file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home on one field, `template.default`. The home judgement closed
`text_config.moe_intermediate_size` by the default rule under transformers 5.22.1 and left the version strings
(5.5.0.dev0 to 5.9.0); the 16,934-byte template is not the pin's 17,466-byte one and not any later revision's.
Read against the original's history at home, it is byte-equal to Google's revisions `145dc250` of 04-28
("fix(chat_template): update SI and tool call handling") and `ba74f5b6` of 05-07, the template the hub served
until `fcf23027` replaced it on 05-18, eight days before the copy was made: the maker's snapshot of the original
was older than the hub's head, the earlier-revision case of round 31's pairs 2 and 4, round 35's pair 5 and
round 39's pair 6, which the home tool does not yet check. The tokenizer, the token ids and the generation
settings are the pin's.

## For the recipe library

An arbitrary-rank entry would read the copy as its card with the six residues named; a prompt-set line is not
in the weights, only in the direction's distance from the English searches. The direction vectors stay in the
pull copy at `/opt/ai/hpc-packages/pulls/model-audit/nautilus40/measurements/pair-5/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
