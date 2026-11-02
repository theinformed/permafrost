# Reading of the Stage 1 and Stage 2 result: Ishowbackup/gemma-4-12B-it-uncensored against google/gemma-4-12B-it (2026-11-01)

Measured on Nautilus, round 20 piece 3 (download job 4143641, compare job 4143644, 664 seconds, sweep 4143650).
Modified revision `d65eeea8` (one commit, 2026-08-18 at 15:34Z, "Duplicate from TrevorJS/gemma-4-12B-it-uncensored";
the README is TrevorJS's, 4,929 bytes, byte for byte), original pinned at `707f0a3b` (07-20). The card is the
source's: norm-preserving biprojected abliteration with one direction per layer on the attention output and the
down projection of layers 15 to 47, 6 refusals in 100, KL 0.0556. The repository's `base_model` field names
Google.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 1 flag, on the
cluster and after re-scoring at home, the flag TrevorJS's report carries: layer 42's attention output at a first
share of 0.9899 on a relative change of 0.0172, inside the storage floor. The weight file is TrevorJS's: the hub
lists one `model.safetensors` of 23,919,549,408 bytes under the same LFS checksum (`dd7fcab672`) in both
repositories and in the two round 19 duplicates (Iambackup, Justbackup), the comparison read the same shard
checksum, and every measured field of all 677 tensors equals the round 8 report
(`results/weights/TrevorJS-gemma-4-12B-it-uncensored.json`): 66 changed, the attention output and the down
projection of layers 15 to 47, one direction per layer (within-layer cosine 0.970 to 0.999), first share 0.990 to
0.996, left kept -0.01 to 0.68 on the attention outputs and 0.00 to 0.41 on the down projections, the left below
the right on 65 of 66, rows within 0.0004 of the original's under the biprojection's restoration, 611 tensors
equal to the original. The layer table and the reading are in `TrevorJS--gemma-4-12B-it-uncensored-*.reading.md`;
this is the fourth repository to carry that file, the third made with the hub's duplicate function, and the same
account duplicated huihui-ai's 12B copy two minutes earlier (piece 4).

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster, seven fields, one at home. The copy was created on 08-18, so the pin
rule chose Google's `707f0a3b` of 07-20 where the parent's pin was `5926caa4` of 06-04; the files are the parent's,
saved on 06-13 by transformers 5.12.0. The 12B family's six fields (four omitted defaults, two sub-configuration
data types) closed by tool under 5.22.1 (finding 39), where round 19's judgement of the same files had left the
four defaults open. What stays is the template: the copy carries Google's 17,466-byte file of 06-03 (`36e3a42e`),
the parent's pin, under a pin whose template is the 18,683-byte Canonical file (`ae53464b`): the earlier-revision
case through a re-upload, the eighth in the census. The fixed conversation renders identically under both.

## For the recipe library

Nothing new on the weights: a byte-identical re-upload of TrevorJS's 12B copy, made with the hub's duplicate
function, under an account named for the purpose, the third such account on this file. The pinner's duplicate
check (finding 38) now refuses a repository whose weight file carries a measured copy's checksum; this batch was
pinned before the check existed, and the desk let it run because the download was already an hour in.

Weight differences alone cannot certify the absence of hidden behavior.
