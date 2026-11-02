# Reading of the Stage 1 and Stage 2 result: Ishowbackup/Huihui-gemma-4-12B-it-abliterated against google/gemma-4-12B-it (2026-11-01)

Measured on Nautilus, round 20 piece 4 (download job 4143641, compare job 4143645, 592 seconds, sweep 4143650).
Modified revision `bbf6560e` (one commit, 2026-08-18 at 15:32Z, "Duplicate from
huihui-ai/Huihui-gemma-4-12B-it-abliterated"; the README is huihui-ai's, 2,822 bytes), original pinned at
`707f0a3b` (07-20). The card is the source's: "Only layers 23-28" abliterated with the remove-refusals code, the
copy re-ablated after the earliest released 12B weights were found faulty. The repository's `base_model` field
names Google.

## Weights (Stage 2)

The tool's assessment was "recipe match", recipe `directional-per-layer-selected`, 0 flags, on the cluster and
after re-scoring at home. The weight file is huihui-ai's: the hub lists the same LFS checksum (`2dd13d8676`) on
the weight file in both repositories and in TimelessSoul's round 14 duplicate, and every measured field of all
677 tensors equals the round 13 report (`results/weights/huihui-ai-Huihui-gemma-4-12B-it-abliterated.json`): 12
changed, the attention output and the down projection of layers 23 to 28, one direction per matrix (first share
0.994 to 0.998) shared by layers 24 to 27 at cosine 1.000 and taken up at 0.47 and 0.74 on the end layers, the
left kept fraction -0.003 to 0.005 (weight 1.00), the right 0.63 to 0.89, the left below the right on 12 of 12,
rows moved 0.016 to 0.079, 665 tensors equal to the original. The layer table and the reading are in
`huihui-ai--Huihui-gemma-4-12B-it-abliterated-*.reading.md`; this is the third repository to carry that file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, two fields. The template is the earlier-revision case
through a re-upload: huihui-ai's files carry Google's 17,466-byte file of 06-03 (`36e3a42e`) under a pin whose
template is the 18,683-byte Canonical file (`ae53464b`), chosen because the copy was created on 08-18. The other
field is huihui-ai's own: `text_config.max_position_embeddings` of 131,072 against Google's 262,144, which the
parent's report has carried open since round 13 and which this copy inherits byte for byte. The fixed
conversation renders identically under both templates.

## For the recipe library

Nothing new on the weights: a byte-identical re-upload of huihui-ai's 12B copy, two minutes before the same
account duplicated TrevorJS's (piece 3). The pinner's duplicate check (finding 38) would have paired it with its
parent by the LFS checksum before any download.

Weight differences alone cannot certify the absence of hidden behavior.
