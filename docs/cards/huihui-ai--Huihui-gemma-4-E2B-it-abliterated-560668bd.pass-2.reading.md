# Reading of the Stage 1 and Stage 2 result, second pass: huihui-ai/Huihui-gemma-4-E2B-it-abliterated against google/gemma-4-E2B-it (2026-11-01)

Measured on Blueback, round 22 piece 2, the second measurement of a pair round 13 measured on the same system
(piece 2 of that round, compare job 3400581). The pull carries the measurements and the sweep record and no job
log. Modified revision `3d1e3d50` (seven commits from 2026-04-08 to 04-09, the weights at 17:55Z on 04-09),
original pinned at `4742fe84` (04-02): the same two revisions as round 13. The batch note of 10-31 17:28Z says the
E2B copy was unmeasured; it was pinned before the duplicate rule (finding 38) and the note was stale, since round
13's result had been committed with the E2B parent read against prithivMLmods's re-upload (finding 9). The card is
the one round 13 read: the first ten layers left alone, the maker's remove-refusals script.

## Weights (Stage 2)

"Recipe match", recipe `single-projection-selected`, 0 flags, on the cluster and at home, as in round 13. Every
measured field of all 2,011 tensors equals the round 13 report
(`results/weights/huihui-ai-Huihui-gemma-4-E2B-it-abliterated.json`) to the last digit, the singular values
included, on the same modified shard (`90daa0b268`) and the same original shard (`2db5482b20`): 50 changed, the
attention output and the down projection of layers 10 to 34, one shared direction (within-layer cosine 1.000,
cross-kind 0.99999), weight 1.00 on the output side (left kept fraction -0.005 to -0.003 on all 50, right 0.19 to
0.85), first share 0.995 to 0.997, relative change 0.023 to 0.028, rows moved 0.006 to 0.026, the largest change
outside the set exactly 0, 1,961 tensors equal to the original. The layer table is in the round 13 reading
(`huihui-ai--Huihui-gemma-4-E2B-it-abliterated-560668bd.reading.md`); nothing in it moves. The report also equals
prithivMLmods/gemma-4-E2B-it-Uncensored-MAX's (round 18) in every field, as round 13's did.

The measure is deterministic on this pair: two runs on one system, nine rounds apart, give the same 50 rows and the same 1,961 equalities. Round 3's second pass settled the same point on
Nautilus for five pairs; this is the first repeat on Blueback.

## Token and configuration side (Stage 1)

"Consistent" on the cluster and at home, as in round 13: every field equal, 5.5.0.dev0 on both sides, the fixed
conversation renders identically.

## For the recipe library

Nothing new on the weights. The pair cost one download of the copy and one compare that the committed report
already held; the pinner's duplicate rule now refuses a copy whose weight files equal a measured copy's, and a
second rule is owed for a copy whose hub id and revision are already in `results/weights/`. The pull copy keeps the
direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/blueback22/measurements/pair-2/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
