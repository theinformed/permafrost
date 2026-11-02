# Reading of the Stage 1 and Stage 2 result: NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals8-attn against google/gemma-4-E4B-it (2026-11-02)

Measured on Wheat, round 37 piece 8 (download job 387161, compare job 387169, sweep 387170; the pull carries the
measurements and the sweep record and no job log). Modified revision `fa08a885` (2026-04-29): the repository was
made on 04-05 at 12:53Z and the weight file (`107e31e8`) uploaded at 12:56Z; the commits of 04-11 and 04-29 changed
`chat_template.jinja` (12,188 to 16,317 to 16,934 to 16,804 bytes) and `tokenizer_config.json` and nothing else.
Original pinned at `292a7e27` (04-02, 2,130 tensors). The card (a Japanese README with an English copy) says
Heretic v1.2.0's arbitrary-rank ablation from the pull request 211 branch at commit `3b70fe5` (the L-BFGS
optimiser), with `target_components = ["attn.o_proj"]`, "attention outputs only", stated twice;
`start_layer_index` 17, `end_layer_index` 42, `preserve_good_behavior_weight` 0.9217,
`steer_bad_behavior_weight` 0.0010, `overcorrect_relative_weight` 0.7196, `neighbor_count` 15, KL divergence
0.0151, 8 refusals in 100 against 99. The maker's siblings on the hub are Refusals8 (both writers; start 21, end
35, preservation 0.9896), Refusals6-attn (attention only by its card; start 21, end 41, preservation 0.8666, 6
refusals in 100) and Refusals3; Refusals5 is in the census (round 27). This pair is the method's check on its own
writer count: a card that names one writer, measured on both.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 45 flags (25 first
shares, 20 within-layer cosines), on the cluster and after re-scoring at home. On reading, the down projections
are edited.

- 25 of 2,130 tensors changed: the attention outputs of layers 17 to 25 and 27 to 31 (14) and the down projections
  of 18, 21 and 23 to 31 (11), relative change 0.016 to 0.049. The down projections are edits by every measure the
  attention outputs pass: first share 0.40 to 0.94 (0.40, 0.45 and 0.54 at 18, 21 and 26, where the fourth
  cumulative share is 0.74 to 0.89), input side on all 11, weights 1.23 to 1.51, rows 0.0008 to 0.0032. Five more
  tensors moved under the line (the down projections of 17, 19 and 20 at 0.00011 to 0.00013, 22 at 3e-6, the
  attention output of 26 at 2e-6), so the largest change outside the changed set is 0.00013, and 2,100 tensors
  equal the original. The window reaches layer 31 against the card's end of 42; nothing from 32 to 41 moved.
- A few directions per matrix on the attention outputs (first shares 0.75 to 0.97), more on the three down
  projections above.
- Input side on all 25. Read as weights, one minus the right kept fraction: the attention outputs 1.15 to 1.84
  (median 1.32, 1.84 at layer 29), the down projections 1.23 to 1.51.
- Rows moved 0.0017 to 0.0142 on the attention outputs (0.014 at layer 31, 0.011 at 29) and 0.0008 to 0.0032 on
  the down projections, under no preservation claim in the card's parameters (the branch had none).
- A direction per matrix: 0.18 to 0.42 to the group reference, 0.006 to 0.15 between the two writers of a layer.

| Layer | Attention output: change, E1, left kept, right kept, weight | Down projection: change, E1, E4, left kept, right kept, weight | Rows |
| --- | --- | --- | --- | --- |
| 17 | 0.0232, 0.912, 0.87, -0.40, 1.40 | under the line, 0.00012 | 0.0017 |
| 18 | 0.0352, 0.953, 0.84, -0.53, 1.53 | 0.0340, 0.398, 0.740, 0.89, -0.34, 1.34 | 0.0027, 0.0021 |
| 21 | 0.0284, 0.750, 0.82, -0.26, 1.26 | 0.0335, 0.446, 0.799, 0.86, -0.29, 1.29 | 0.0022, 0.0023 |
| 24 | 0.0379, 0.956, 0.36, -0.39, 1.39 | 0.0186, 0.937, 0.963, 0.79, -0.45, 1.45 | 0.0046, 0.0008 |
| 26 | under the line, 0.000002 | 0.0255, 0.537, 0.885, 0.85, -0.32, 1.32 | 0.0012 |
| 28 | 0.0283, 0.935, 0.77, -0.46, 1.46 | 0.0226, 0.800, 0.928, 0.80, -0.32, 1.32 | 0.0017, 0.0016 |
| 29 | 0.0384, 0.889, 0.94, -0.84, 1.84 | 0.0225, 0.846, 0.952, 0.72, -0.51, 1.51 | 0.0114, 0.0019 |
| 31 | 0.0491, 0.932, 0.63, -0.20, 1.20 | 0.0159, 0.943, 0.964, 0.82, -0.30, 1.30 | 0.0142, 0.0010 |

The full table (25 rows) is in the report.

Directions. Against the saved vectors of the measurements of the E4B on the shared changed names, the leading directions
stand at 0.99 on both sides to coder3101's E4B edit (10 shared), 0.98 and 0.99 to the maker's Refusals5 (21
shared, nine of them down projections, the lowest 0.81 and 0.91), 0.97 and 0.99 to alphakek's, 0.97 and 0.97 to
llmfan46's ultra copy, 0.94 and 0.98 to MoonRide's E4B copy (piece 6), 0.91 and 0.95 to llmfan46's E4B, 0.87 and
0.98 to JokeHer's and 0.89 and 0.91 to coder3101's QAT edit, finding 82's E4B family; the per-layer edits
(TheUmbraWalker, TrevorJS) stand at 0.33 and 0.21. The direction on the down projections is the family's down
projection direction, which is how an unasked writer came to be edited along it.

Byte-range reads against the hub confirm the reading on the sibling. On the down projection of layer 28 the
Refusals6-attn copy differs from Google's by 0.0233 and this copy by 0.0226, and the two differ from each other by
0.0053; on the down projection of 24, 0.0207 and 0.0186 and 0.0057 between them; on the attention output of 28,
0.0272 and 0.0283 and 0.0066; on the down projection of 33, Refusals6-attn differs by 0.0140 where this copy is
byte-equal to Google's, as the measurement says. Both "attn" copies edit down projections; the tool's branch at
`3b70fe5` applied the ablation to both writers whatever `target_components` said, and the cards report the
setting rather than the effect.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster, "consistent with re-save noted" at home: `text_config.moe_intermediate_size`
closed by the default rule under transformers 5.22.1, and the template is byte-equal to Google's later revision
`c53e9d33` of 04-28 ("fix(chat_template): update SI and tool call handling"), which the later-revision check now
matches; the maker followed Google's template fixes on an unchanged weight file.

## For the recipe library

The directional-per-layer entry is the nearest and its 45 flags are the few directions per matrix and the two
writers' disagreement. An arbitrary-rank entry fed the card's `target_components` would flag the eleven down
projections as outside the declared set, which is the right reading. The direction vectors stay in the pull copy
at `/opt/ai/hpc-packages/pulls/model-audit/wheat37/measurements/pair-8/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
