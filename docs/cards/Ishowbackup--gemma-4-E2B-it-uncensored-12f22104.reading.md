# Reading of the Stage 1 and Stage 2 result: Ishowbackup/gemma-4-E2B-it-uncensored against google/gemma-4-E2B-it (2026-11-02)

Measured on Blueback, round 26 piece 8. The pull carries the measurements and the sweep record and no job log.
Modified revision `440ce893` (one commit, 2026-08-18 at 15:35Z, "Duplicate from TrevorJS/gemma-4-E2B-it-uncensored";
the README is TrevorJS's of that week, 3,912 bytes), original pinned at `3e22461f` (07-20). The account made three
duplicates of other makers' copies within three minutes that afternoon. The card is the source's: norm-preserving
biprojected abliteration on every attention output and down projection. The repository's `base_model` field names
Google.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer`, 3 flags, on the cluster and
after re-scoring at home: the down projection of layer 0 at a first share of 0.988 and the two writers of layer 3
at a within-layer cosine of 0.943. The weight file is TrevorJS's: the hub lists the same LFS checksum
(`8237e4818b`) on the 10,246,621,918-byte `model.safetensors` in both repositories, and every measured field of all
2,011 tensors equals the round 13 report (`results/weights/TrevorJS-gemma-4-E2B-it-uncensored.json`) and the
round 22 re-upload under lessans: 70 changed, the attention output and the down projection of all 35 layers, one
direction per layer (within-layer cosine 0.943 to 0.997), the left kept fraction 0.002 to 0.69 and the right 0.16
to 0.74, first share 0.988 to 0.996, rows moved by at most 0.0004, 1,941 tensors equal to the original. The layer
table and the reading are in `TrevorJS--gemma-4-E2B-it-uncensored-*.reading.md`; this is the third repository to
carry that file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, two fields. Under transformers 5.22.1
`text_config.moe_intermediate_size` (null in a 5.5.0 save) closes by the default rule. The template is the
earlier-revision case through a re-upload: TrevorJS's files carry Google's 11,926-byte file of the 04-02 revision
under a pin of 07-20 whose template is the 18,569-byte Canonical file, the pin chosen because the copy was created
in August. The fixed conversation renders identically under both.

## For the recipe library

Nothing new on the weights: a byte-identical re-upload of TrevorJS's E2B copy made with the hub's duplicate
function four months after the parent repository was created, and measured against a later Google revision than
the parent was, to the same numbers, because Google's revisions change templates and configuration and never the
weight shards. The pinner's duplicate check (finding 38) would have paired it with its parent by the LFS checksum
before any download.

Weight differences alone cannot certify the absence of hidden behavior.
