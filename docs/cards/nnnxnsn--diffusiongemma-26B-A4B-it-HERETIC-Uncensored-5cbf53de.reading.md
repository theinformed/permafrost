# Reading of the Stage 1 and Stage 2 result: nnnxnsn/diffusiongemma-26B-A4B-it-HERETIC-Uncensored against google/diffusiongemma-26B-A4B-it (2026-10-31)

Measured on Wheat, round 30 piece 8 (probe job 386940, download job 386942, compare job 386950, 1,451 seconds, sweep
386951), without the container image, under a standalone Python 3.11.18. Modified revision `5f412797` (one commit,
2026-06-22 at 09:09Z, "Duplicate from edwixx/diffusiongemma-26B-A4B-it-HERETIC-Uncensored"; the README is
edwixx's of that date, 4,090 bytes, before the 06-25 and 07-16 edits), original pinned at `0f28bc42` (2026-06-10).
The weight file is edwixx's under the parent's LFS checksums (`3b78a288` to `f86b80dd`), eleven days after the
parent's weights went up; the card is edwixx's and the `base_model` field names the original.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection`, 68 flags, on the cluster and
`directional-per-layer-selected`, 86 flags, after re-scoring at home with the `decoder.` names read, the same as
pair 7. The report equals pair 7's in every field of all 1,047 tensors, every singular value, every direction
cosine and every per-expert block (469 of 469 compared fields, the violation list equal entry for entry), the two
compares having run on the same machine kind with the same sketch. The reading is pair 7's: 67 changed tensors
(attention outputs 5 to 29, down projections 7 to 29, all 128 experts of layers 11 to 29), 20 at the round-trip
floor, rank one along one direction per layer on the 47 edited, output side with weights 1.03 to 1.31 on the down
projections, expert rows within 0.0013. Pair 7 is the first measurement of edwixx's file and this one confirms
it.

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home: the two version strings (5.8.0.dev0 to 5.11.0) and
nothing else, as pair 7. The fixed conversation renders identically.

## For the recipe library

Nothing new on the weights: a hub duplicate of edwixx's copy. The hub's listing gave the parent's checksums before
the download; the pinner's duplicate check (finding 38) would have filed pair 7 alone. The pull copy keeps the
direction vectors at `/opt/ai/hpc-packages/pulls/model-audit/wheat30/measurements/pair-8/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
