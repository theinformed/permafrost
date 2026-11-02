# Reading of the Stage 1 and Stage 2 result: Cup4/gemma-4-E4B-it-uncensored-heretic against google/gemma-4-E4B-it (2026-11-02)

Measured on Blueback, round 26 piece 5. The pull carries the measurements and the sweep record and no job log.
Modified revision `0a536a3d` (one commit, 2026-09-07 at 10:40Z, "Duplicate from Titanfrm/gemma-4-E4B-it-uncensored-heretic",
21 minutes after Pound1320's), original pinned at `ee0ef602` (07-20). Titanfrm's repository was created that morning at
09:25Z as "Duplicate from AST-1320/gemma-4-E4B-it-uncensored-heretic", and the hub no longer serves AST-1320's.
The README is llmfan46's 31,743-byte card for the same model name. The repository's `base_model` field names Google.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 11 flags, on the
cluster and after re-scoring at home: the 11 changed matrices at first shares of 0.920 to 0.960. The weight file is
llmfan46's: the hub lists the same LFS checksum (`4967172bea`) on the 15,992,595,884-byte `model.safetensors`, and
every measured field of all 2,130 tensors equals the round 2 report and its second pass
(`results/weights/llmfan46-gemma-4-E4B-it-uncensored-heretic.json` and `.pass-2.json`) and this round's piece 4:
11 changed, the attention outputs of layers 21 to 35 less 28, 31, 33 and 34, the left kept fraction 0.29 to 0.92
and the right -0.79 to -0.27, rows moved 0.0016 to 0.0165, 0.00008 outside the changed set. The layer table and the
reading are in `llmfan46--gemma-4-E4B-it-uncensored-heretic-*.reading.md`; this is the fourth repository known to
carry that file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, two fields, the same two as piece 4: the
`moe_intermediate_size` default closes under 5.22.1 and the template is Google's 16,804-byte file of the 04-28
revision under a pin whose template is the 18,569-byte Canonical file, the earlier-revision case through a
re-upload. The fixed conversation renders identically under both.

## For the recipe library

Nothing new on the weights: the same re-upload as piece 4 under another account name. The pinner's duplicate check
(finding 38) would have paired it with llmfan46's by the LFS checksum before any download.

Weight differences alone cannot certify the absence of hidden behavior.
