# Reading of the Stage 1 and Stage 2 result: huihui-ai/Huihui-gemma-4-12B-agentic-fable5-abliterated against yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2 (2026-11-02)

Measured on Wheat, round 45 piece 8 (download job 387355, compare job 387363, sweep 387364; the pull carries the
measurements and the sweep record and no job log). Modified revision `22ec2266` (created 2026-07-11 10:48Z, the
weights uploaded at 11:32Z, the card at 12:45Z), parent pinned at `af644ab1` of 2026-06-30, yuxinlu1's agentic
fine-tune of google/gemma-4-12B-it (created 06-28, the weights uploaded on 06-30), saved in float16, which the
census reads for the first time. The card is the maker's usual one, as on pair 2. The copy is one
`model.safetensors` (`11b24899`) beside the parent's (`5cefca08`); the small files carry the parent's object ids,
which are the coder fine-tune's as well.

## Weights (Stage 2)

The tool's assessment was a clean match to `directional-per-layer-selected`, 0 flags, on the cluster and after
re-scoring at home. On reading, the copy is the maker's projection of pair 2 on the same twelve matrices, with a
direction found again on this fine-tune.

- 12 of 677 tensors changed: the attention outputs and down projections of layers 23 to 28, saved in bfloat16 inside
  a float16 file. The largest relative change outside the changed set is exactly 0.
- One direction on layers 24 to 27 (agreement 0.99999), layers 23 and 28 apart at 0.49 and 0.74, each layer's two
  writers sharing one direction.
- Output side on all 12 at weight 1.00 (left kept fraction -0.0004 to 0.0015), first shares 0.991 to 0.997.
- Relative changes 0.0171 to 0.0269; rows moved 0.024 to 0.071, over finding 22's band on every matrix.

| Layer | Attention output: change, E1, left kept, right kept, rows | Down projection: change, E1, left kept, right kept, rows |
| --- | --- | --- |
| 23 | 0.0196, 0.994, 0.001, 0.91, 0.0388 | 0.0192, 0.993, 0.000, 0.66, 0.0237 |
| 24 | 0.0208, 0.994, 0.000, 0.85, 0.0504 | 0.0233, 0.995, 0.000, 0.84, 0.0501 |
| 25 | 0.0201, 0.994, 0.000, 0.83, 0.0500 | 0.0235, 0.995, 0.000, 0.83, 0.0502 |
| 26 | 0.0269, 0.996, 0.000, 0.87, 0.0501 | 0.0227, 0.995, 0.000, 0.73, 0.0340 |
| 27 | 0.0171, 0.991, 0.000, 0.79, 0.0258 | 0.0195, 0.993, 0.000, 0.71, 0.0265 |
| 28 | 0.0196, 0.993, 0.000, 0.84, 0.0707 | 0.0194, 0.993, 0.000, 0.72, 0.0655 |

Directions. The direction stands at 0.978 on the left and 0.982 on the right (minimum 0.976) to pair 2 and to
huihui-ai's projection of Google's checkpoint on all 12 names, at 0.70 and 0.80 to the maker's QAT projection, at
0.65 to AEON-7's, at 0.48 and 0.45 to richardyoung's Heretic edit of the coder fine-tune, at 0.46 and 0.42 to tpls's
(pair 1), and at 0.15 or less to the kernel passes. By byte range at layer 25 the leading direction of the copy's
change stands at 0.978 to the Google edit's, on the attention output and the down projection alike; the parent
projected along the Google edit's direction leaves 0.32 and 0.33 of the change unexplained, and projected along its
own leading direction 0.07 and 0.08, the bfloat16 rounding of the save, so this direction was found again on the
agentic fine-tune where pair 2's was carried from Google's. The two copies' matrices stand 0.0081 and 0.0097 apart
at layer 25; the two parents stand 0.0049 and 0.0057 apart there and 0.0021 on the layer 5 query projection, and
the agentic fine-tune stands 0.0074, 0.0085 and 0.0038 from Google's on those three matrices, a little farther than
the coder fine-tune does. The layer 30 attention output and the layer 5 query projection are byte-equal to the
parent's.

## Token and configuration side (Stage 1)

"Consistent" on the cluster and at home: no compared field differs. The token ids are the instruct checkpoint's
through the parent (`eos_token_id` `[1, 106]`, generation `[1, 106, 50]`, `bos_token_id` 2, `pad_token_id` 0), the
vocabulary is 262,144, and the 17,466-byte template renders the fixed conversation identically.

## For the recipe library

The per-layer selected entry reads the copy cleanly; beside pair 2 it shows that one maker's projection, on two
fine-tunes of one checkpoint by one fine-tuner, reused the base direction once and recomputed it once. The
direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat45/measurements/pair-8/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
