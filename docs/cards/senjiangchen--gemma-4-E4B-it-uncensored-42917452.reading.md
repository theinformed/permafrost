# Reading of the Stage 1 and Stage 2 result: senjiangchen/gemma-4-E4B-it-uncensored against google/gemma-4-E4B-it (2026-11-02)

Measured on Blueback, round 29 piece 7. The pull carries the measurements and the sweep record and no job log.
Modified revision `c31d6234` (one commit, 2026-04-19 at 13:47Z, "Duplicate from TrevorJS/gemma-4-E4B-it-uncensored";
the README is TrevorJS's of that week, 3,944 bytes), original pinned at `83df0a88` (04-10). The card is the
source's: norm-preserving biprojected abliteration on every attention output and down projection. The repository's
`base_model` field names Google.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer`, 6 flags, on the cluster and
after re-scoring at home: the two writers of layers 5, 30 and 33 at within-layer cosines of 0.934 to 0.95. The
weight file is TrevorJS's: the hub lists the same LFS checksum (`37605ec579`) on the `model.safetensors` in both
repositories, and every measured field of all 2,130 tensors equals the round 8 report
(`results/weights/TrevorJS-gemma-4-E4B-it-uncensored.json`): 84 changed, the attention output and the down
projection of all 42 layers, one direction per layer (within-layer cosine 0.934 to 0.998), the left kept fraction
0.01 to 0.77 and the right 0.24 to 0.80, first share 0.991 to 0.996, rows moved by at most 0.0004, 2,046 tensors
equal to the original. The layer table and the reading are in
`TrevorJS--gemma-4-E4B-it-uncensored-*.reading.md`; this is the second repository to carry that file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, two fields. Under transformers 5.22.1
`text_config.moe_intermediate_size` (null in a 5.5.0 save) closes by the default rule. The template is the
earlier-revision case through a re-upload: TrevorJS's files carry Google's 11,926-byte file of the 04-02 revision
under a pin of 04-10 whose template is 16,317 bytes, the pin chosen because the copy was created on 04-19. The fixed
conversation renders identically under both.

## For the recipe library

Nothing new on the weights: a byte-identical re-upload of TrevorJS's E4B copy made with the hub's duplicate
function nine days after the parent's weights were uploaded. The pinner's duplicate check (finding 38) would have
paired it with its parent by the LFS checksum before any download.

Weight differences alone cannot certify the absence of hidden behavior.
