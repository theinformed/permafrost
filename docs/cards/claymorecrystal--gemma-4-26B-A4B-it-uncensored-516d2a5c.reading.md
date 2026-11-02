# Reading of the Stage 1 and Stage 2 result: claymorecrystal/gemma-4-26B-A4B-it-uncensored against google/gemma-4-26B-A4B-it (2026-11-02)

Measured on Blueback, round 29 piece 4. The pull carries the measurements and the sweep record and no job log.
Modified revision `b6c448d5` (one commit, 2026-06-20 at 12:32Z, "Duplicate from TrevorJS/gemma-4-26B-A4B-it-uncensored";
the README is TrevorJS's of that week, 4,538 bytes), original pinned at `20da991a` (06-03). The card is the source's:
norm-preserving biprojected abliteration on the attention output, the shared feed-forward down projection and the
packed expert down projection of every layer. The repository's `base_model` field names Google.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer`, 31 flags, on the cluster and
after re-scoring at home: the 30 packed expert tensors, which carry no singular values and so no first share, and
the within-layer cosine of layer 29. The weight files are TrevorJS's: the hub lists the same LFS checksums
(`4b988df4e5` and `3d2388e809`) on the two shards in both repositories, and every measured field of all 1,013
tensors equals the parent's second pass
(`results/weights/TrevorJS-gemma-4-26B-A4B-it-uncensored.pass-2.json`): 90 changed, three writers in each of the
30 layers, one direction per layer (within-layer cosine 0.949 to 0.9997), the left kept fraction -0.001 to 0.52
and the right 0.45 to 0.88, first share 0.88 to 0.996 on the 60 dense matrices, rows moved by at most 0.0012, 923
tensors equal to the original. The layer table and the reading are in
`TrevorJS--gemma-4-26B-A4B-it-uncensored-*.reading.md`; this is the fourth repository known to carry those files.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, one field. The template is the earlier-revision case through
a re-upload: TrevorJS's files carry Google's 12,045-byte file of the 04-10 revision under a pin of 06-03 whose
template is 17,466 bytes, the pin chosen because the copy was created on 06-20. The fixed conversation renders
identically under both.

## For the recipe library

Nothing new on the weights: a byte-identical re-upload of TrevorJS's 26B-A4B copy made with the hub's duplicate
function. The pinner's duplicate check (finding 38) would have paired it with its parent by the LFS checksums
before any download.

Weight differences alone cannot certify the absence of hidden behavior.
