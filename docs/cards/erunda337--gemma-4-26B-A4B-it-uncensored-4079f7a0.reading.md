# Reading of the Stage 1 and Stage 2 result: erunda337/gemma-4-26B-A4B-it-uncensored against google/gemma-4-26B-A4B-it (2026-10-31)

Measured on Wheat, round 30 piece 2 (probe job 386940, download job 386942, compare job 386944, 1,633 seconds, sweep
386951), without the container image, under a standalone Python 3.11.18. Modified revision `c8ffe79e` (one commit,
2026-04-12 at 04:58Z, "Duplicate from TrevorJS/gemma-4-26B-A4B-it-uncensored"; the README is the same 4,523-byte file
pair 1 carries), original pinned at `7d4c97e5` (2026-04-10), one revision later than pair 1's pin because the
repository was created after Google's 04-10 commit. The card is TrevorJS's; the `base_model` field names Google.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer`, 31 flags, on the cluster and
after re-scoring at home. The weight file is TrevorJS's under the parent's LFS checksums (`4b988df4e5`,
`3d2388e809`), the original's two shards carry the same checksums under both pins (`11276849`, `aab47033`), and the
report equals pair 1's in every field of all 1,013 tensors, every singular value and every direction cosine (630 of
630 compared fields, the violation list equal entry for entry), the two compares having run on the same machine kind
with the same sketch. The reading is pair 1's and TrevorJS's: 90 changed tensors, one direction per layer on three
writer kinds including all 128 experts of every layer, output side, rows restored within 0.0012.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster, one field, and the same at home. The two version strings (5.5.0.dev0 to
5.5.0) close as a re-save. The open field is the template: the copy carries Google's 12,045-byte file of 04-02
(`2dfbfc7d`), the file TrevorJS's repository holds and the one pair 1's pin has, where the 04-10 pin's template is a
16,448-byte revision (`85a08664`); the tokenizer configuration grew by 27 bytes in the same commit. The earlier-revision
case through a re-upload, as Justbackup's 12B copy in round 19 and TimelessSoul's in round 14, the seventh in the
census; the fixed conversation renders identically under both files. The rule that reads the original's later
commits cannot close it, because the copy's file is the original's earlier one; closed by hand.

## For the recipe library

Nothing new on the weights: the same file as pair 1, duplicated four days later under another account. Two
measurements of one weight file in one round, 103 GB of downloads and two compare jobs, for a result the hub's
listing gave; the pinner's duplicate check (finding 38) would have filed neither. The pull copy keeps the direction
vectors at `/opt/ai/hpc-packages/pulls/model-audit/wheat30/measurements/pair-2/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
