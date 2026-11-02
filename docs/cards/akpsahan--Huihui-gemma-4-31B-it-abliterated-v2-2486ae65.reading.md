# Reading of the Stage 1 and Stage 2 result: akpsahan/Huihui-gemma-4-31B-it-abliterated-v2 against google/gemma-4-31B-it (2026-11-02)

Measured on Blueback, round 29 piece 3. The pull carries the measurements and the sweep record and no job log.
Modified revision `7db87424` (one commit, 2026-08-04 at 12:25Z, "Duplicate from huihui-ai/Huihui-gemma-4-31B-it-abliterated-v2";
the README is the maker's, 3,623 bytes), original pinned at `842da379` (07-20). The card is the maker's second
version: abliteration with the first five layers left alone. The repository's `base_model` field names Google.

## Weights (Stage 2)

The tool's assessment was "recipe match", nearest recipe `single-projection-selected`, 0 flags, on the cluster and
after re-scoring at home. The weight files are the maker's: the hub lists the same LFS checksums (`9a11eda6e0` and
`bc366b3f1b`) on the two shards in both repositories, and every measured field of all 1,188 tensors equals the
round 12 report (`results/weights/huihui-ai-Huihui-gemma-4-31B-it-abliterated-v2.json`): 110 changed, the attention
output and the down projection of layers 5 to 59, one direction shared by all 110 at cosine 1.000, the copy keeping
-0.497 to -0.501 along it (the weight 1.5), first share 0.994 to 0.997, rows moved by up to 0.64 on the down
projections, 1,078 tensors equal to the original. The layer table and the reading are in
`huihui-ai--Huihui-gemma-4-31B-it-abliterated-v2-*.reading.md`; this is the first re-upload of the maker's second
version to be measured.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, two fields. Under transformers 5.22.1
`text_config.moe_intermediate_size` (null in a 5.5.0 save) closes by the default rule. The template is the
earlier-revision case through a re-upload: the maker's files carry Google's 12,045-byte file of the 04-10
revision under a pin of 07-20 whose template is the 18,683-byte Canonical file, the pin chosen because the copy
was created in August. The fixed conversation renders identically under both.

## For the recipe library

Nothing new on the weights: a byte-identical re-upload made with the hub's duplicate function, measured against a
later Google revision than the parent was and equal to the last digit because Google's revisions never change
the weight shards. The pinner's duplicate check (finding 38) would have paired it with its parent by the LFS
checksums before any download.

Weight differences alone cannot certify the absence of hidden behavior.
