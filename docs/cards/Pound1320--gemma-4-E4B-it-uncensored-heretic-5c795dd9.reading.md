# Reading of the Stage 1 and Stage 2 result: Pound1320/gemma-4-E4B-it-uncensored-heretic against google/gemma-4-E4B-it (2026-11-02)

Measured on Blueback, round 26 piece 4. The pull carries the measurements and the sweep record and no job log.
Modified revision `8bc8e3f3` (one commit, 2026-09-07 at 10:19Z, "Duplicate from Titanfrm/gemma-4-E4B-it-uncensored-heretic"),
original pinned at `ee0ef602` (07-20). Titanfrm's repository was itself created that morning at 09:25Z as
"Duplicate from AST-1320/gemma-4-E4B-it-uncensored-heretic", and the hub no longer serves AST-1320's. The README
is llmfan46's 31,743-byte card for the same model name: Heretic 1.2.0 with arbitrary-rank ablation, layers 8 to 36,
the attention output projection only. The repository's `base_model` field names Google.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 11 flags, on the
cluster and after re-scoring at home: the 11 changed matrices at first shares of 0.920 to 0.960. The weight file is
llmfan46's: the hub lists the same LFS checksum (`4967172bea`) on the 15,992,595,884-byte `model.safetensors` in
both repositories, and every measured field of all 2,130 tensors equals the round 2 report and its second pass
(`results/weights/llmfan46-gemma-4-E4B-it-uncensored-heretic.json` and `.pass-2.json`): 11 changed, the attention
outputs of layers 21, 22, 23, 24, 25, 26, 27, 29, 30, 32 and 35, relative change 0.022 to 0.052, the left kept
fraction 0.29 to 0.92 and the right -0.79 to -0.27, rows moved 0.0016 to 0.0165, 0.00008 outside the changed set.
The layer table and the reading are in `llmfan46--gemma-4-E4B-it-uncensored-heretic-*.reading.md`; this is the
third repository known to carry that file, with two more measured as pieces 5 and 6 of this round.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, two fields. Under transformers 5.22.1
`text_config.moe_intermediate_size` (null in a 5.5.0 save) closes by the default rule. The template is the
earlier-revision case through a re-upload, twice removed: llmfan46's files carry Google's 16,804-byte file of the
04-28 revision (`c53e9d33`) under a pin of 07-20 whose template is the 18,569-byte Canonical file, the pin chosen
because the copy was created in September. The fixed conversation renders identically under both.

## For the recipe library

Nothing new on the weights: a byte-identical re-upload of a re-upload of llmfan46's E4B copy made with the hub's
duplicate function. The pinner's duplicate check (finding 38) would have paired it with llmfan46's by the LFS
checksum before any download; the batch was pinned before the rule.

Weight differences alone cannot certify the absence of hidden behavior.
