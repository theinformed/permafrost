# Reading of the Stage 1 and Stage 2 result: sh0ck0r/gemma-4-E4B-it-heretic against google/gemma-4-E4B-it (2026-11-02)

Measured on Wheat, round 33 piece 3 (download job 387105, compare job 387108, sweep 387114; the pull of 11-02
01:02Z carries the measurements and the sweep record and no job log). Modified revision `9bfa9851` (11 commits on
2026-05-24 from 20:45Z to 20:54Z, the model, tokenizer, README and `reproduce/` folder), original pinned at
`d6436b3d` (05-18). The card is Heretic's generated page (27,824 bytes): Heretic v1.3.0, direction index 31.87,
attention output kernel 1.43 at position 36.26 falling to 0.28 at distance 18.20, down projection kernel 1.38 at
26.14 falling to 1.33 at 21.43, KL divergence 0.0080, refusals 39 of 100 against 99 of 100. The field `base_model`
names google/gemma-4-E4B, the pretrained base. The maker's third copy in the census, after the 26B-A4B export and
the Artemis 31B (finding 45).

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection-selected`, 11 flags (8 first
shares of 0.959 to 0.989, 2 direction cosines, one cross-kind), on the cluster and after re-scoring at home. On
reading, the copy is a Heretic edit whose windows read to the layer, with a flat down kernel that reads 0.1 to
0.2 below its printed height.

- 60 of 2,076 matched tensors changed: the attention outputs of layers 19 to 41 (23) and the down projections of
  5 to 41 (37) of 42. The attention kernel reaches 36.26 plus or minus 18.20, layers 19 to 41 (18.06 to 54.46,
  the stack ending at 41); the down kernel 26.14 plus or minus 21.43, layers 5 to 41. Both windows read exactly.
  The 54 original-only names are the shared-KV key norms. Nothing else moved; the largest relative change outside
  the changed set is exactly 0.
- One shared direction: group medians 0.98 and 0.99, 0.86 across the kinds, the two writers of a layer at 0.89
  to 0.998. First shares 0.959 to 0.997.
- Output side on 51 of 60 (the left kept fraction below the right on 18 of 23 attention outputs and 33 of 37 down
  projections). The down projections, under a kernel that
  runs 1.33 to 1.38 across the whole window, read 1.11 to 1.30 (1.11 at layer 5, 1.21 at 19, 1.29 at 26, 1.13
  at 35, 1.16 at 41): flat as the kernel is, 0.1 to 0.2 below it. The attention outputs read 0.20 at layer 19,
  0.69 at 26, 1.01 at 35, 0.98 at 41 against the kernel's 0.34, 0.78, 1.35 and 1.13.
- Rows moved 0.0022 to 0.0123, Heretic's band; no restoration is claimed.

| Layer | Attention output: change, E1, left kept, weight, kernel | Down projection: change, E1, left kept, weight, kernel | Rows |
| --- | --- | --- | --- | --- |
| 5 | | 0.0259, 0.996, -0.11, 1.11, 1.33 | 0.0046 |
| 11 | | 0.0264, 0.996, -0.15, 1.15, 1.34 | 0.0039 |
| 19 | 0.0068, 0.959, 0.80, 0.20, 0.34 | 0.0274, 0.997, -0.21, 1.21, 1.36 | 0.0022, 0.0057 |
| 26 | 0.0152, 0.990, 0.31, 0.69, 0.78 | 0.0278, 0.997, -0.29, 1.29, 1.38 | 0.0044, 0.0048 |
| 30 | 0.0231, 0.995, 0.49, 0.51, 1.03 | 0.0293, 0.997, -0.21, 1.21, 1.37 | 0.0080, 0.0038 |
| 35 | 0.0278, 0.995, -0.01, 1.01, 1.35 | 0.0254, 0.996, -0.13, 1.13, 1.36 | 0.0080, 0.0083 |
| 41 | 0.0196, 0.994, 0.02, 0.98, 1.13 | 0.0257, 0.996, -0.16, 1.16, 1.35 | 0.0046, 0.0048 |

The copy's four shards: the second and third (`432cdf32`, `8aa59b7a`) are its own; the first (`aa3e9d1e`) and
fourth (`8080cb1a`) are the untouched embedding and vision shards of the library's layout, shared with p-e-w's and
BinxNet's E4B exports (finding 71). No measured field equals another copy's.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster (one field) and "consistent with re-save noted" at home:
`text_config.moe_intermediate_size` closes by the default rule, and the two version strings are all that differ.
The template is the pin's 17,336-byte file and the fixed conversation renders identically.

## For the recipe library

The selected single-projection entry reads the windows and the side; its eight first-share flags sit on the
attention kernel's low shoulder (layers 19 to 23, weights 0.20 to 0.4). The flat down kernel is the second in the
census after igorls's QAT copy (finding 69), and both read below the printed height by a tenth or two. The
direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat33/measurements/pair-3/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
