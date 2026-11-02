# Reading of the Stage 1 and Stage 2 result: p-e-w/gemma-4-E4B-it-heretic against google/gemma-4-E4B-it (2026-11-02)

Measured on Wheat, round 33 piece 2 (download job 387105, compare job 387107, sweep 387114; the pull of 11-02
01:02Z carries the measurements and the sweep record and no job log). Modified revision `02a16f01` (11 commits in
two minutes on 2026-06-11 from 07:10Z: the model, tokenizer and processor, the README and a `reproduce/` folder),
original pinned at `fee6332c` (06-03). The maker is the author of the Heretic tool; this is the author's own E4B
export, and the maker's REPRODUCED re-upload shares these weight files, so this measurement serves both. The card
is the tool's generated page (27,861 bytes): Heretic v1.3.0, direction index 31.26, attention output kernel 0.81 at
position 26.47 falling to 0.44 at distance 15.86, down projection kernel 1.47 at 27.73 falling to 0.55 at 23.71, KL
divergence 0.0072, refusals 42 of 100 against 100 of 100. The field `base_model` names google/gemma-4-E4B, the
pretrained base.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection-selected`, 37 flags (32 first
shares of 0.969 to 0.990, 4 direction cosines, one cross-kind), on the cluster and after re-scoring at home. On
reading, the copy is a textbook Heretic edit whose windows read to the layer and whose heights run under the
kernel.

- 68 of 2,076 matched tensors changed: the attention outputs of layers 11 to 41 (31) and the down projections of
  5 to 41 (37) of 42. The attention kernel reaches 26.47 plus or minus 15.86, layers 11 to 41; the down kernel
  27.73 plus or minus 23.71, layers 5 to 41 (4.02 to 51.44, the stack ending at 41). Both windows read exactly.
  The 54 original-only names are the shared-KV key norms the export drops (finding 24). Nothing else moved; the
  largest relative change outside the changed set is exactly 0.
- One shared direction: group medians 0.97 on the attention outputs and 0.99 on the down projections, 0.85
  across the two kinds, the two writers of a layer at 0.88 to 0.998. First shares 0.969 to 0.998.
- Output side on 57 of 68 (the left kept fraction below the right on 24 of 31 attention outputs and 33 of 37 down
  projections). The weights read off the left follow the kernel's shape and sit below its height: attention
  outputs 0.17 at layer 11, 0.46 at 23, 0.73 at 26, 0.50 at 29, 0.41 at 41, against the kernel's 0.45, 0.73,
  0.80, 0.75 and 0.47; down projections 0.47 at layer 5, 0.96 at 17, 1.34 at 26, 1.14 at 29, 0.86 at 41, against
  0.59, 1.05, 1.40, 1.42 and 0.96. The peak layers read within 0.07; the shoulders fall 0.1 to 0.3 short.
- Rows moved 0.0027 to 0.0086, Heretic's band; no restoration is claimed.

| Layer | Attention output: change, E1, left kept, weight, kernel | Down projection: change, E1, left kept, weight, kernel | Rows |
| --- | --- | --- | --- | --- |
| 5 | | 0.0116, 0.984, 0.53, 0.47, 0.59 | 0.0042 |
| 11 | 0.0089, 0.974, 0.83, 0.17, 0.45 | 0.0162, 0.991, 0.30, 0.70, 0.82 | 0.0027, 0.0042 |
| 17 | 0.0121, 0.985, 0.67, 0.33, 0.59 | 0.0210, 0.994, 0.04, 0.96, 1.05 | 0.0052, 0.0042 |
| 23 | 0.0147, 0.989, 0.54, 0.46, 0.73 | 0.0256, 0.996, -0.08, 1.08, 1.29 | 0.0043, 0.0051 |
| 26 | 0.0155, 0.990, 0.27, 0.73, 0.80 | 0.0285, 0.997, -0.34, 1.34, 1.40 | 0.0050, 0.0043 |
| 29 | 0.0164, 0.991, 0.50, 0.50, 0.75 | 0.0321, 0.998, -0.14, 1.14, 1.42 | 0.0061, 0.0042 |
| 35 | 0.0124, 0.985, 0.54, 0.46, 0.61 | 0.0221, 0.995, 0.00, 1.00, 1.19 | 0.0053, 0.0066 |
| 41 | 0.0081, 0.969, 0.59, 0.41, 0.47 | 0.0183, 0.993, 0.14, 0.86, 0.96 | 0.0033, 0.0051 |

The copy's four shards: the second and third (`78c1ee08`, `2dda6bb6`) are its own; the first (`aa3e9d1e`, the
token embedding alone in the library's four-shard layout of this model) and the fourth (`8080cb1a`, the vision
tower) equal the first and fourth shards of sh0ck0r's and BinxNet's E4B exports and of four earlier copies,
since none touched a tensor in them (finding 71). No measured field equals another copy's.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster (one field) and "consistent with re-save noted" at home:
`text_config.moe_intermediate_size` closes by the default rule, and the two version strings are all that differ.
The template is the pin's 17,336-byte file and the fixed conversation renders identically.

## For the recipe library

The selected single-projection entry reads the windows and the side and flags 32 first shares at 0.969 to 0.990
on an edit whose smallest matrices sit at the kernel's shoulders; a line at 0.95 for the shoulders of a declared
kernel would clear them. The windows read exactly on both writers (finding 59), and the heights follow the kernel's
shape on the E4B where the 12B copies of finding 46 scatter. The
direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat33/measurements/pair-2/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
