# Reading of the Stage 1 and Stage 2 result: BinxNet/gemma-4-12B-it-heretic against google/gemma-4-12B-it (2026-11-02)

Measured on Wheat, round 33 piece 6 (download job 387105, compare job 387111, sweep 387114; the pull of 11-02
01:02Z carries the measurements and the sweep record and no job log). Modified revision `0802b8f7` (11 commits on
2026-06-21 from 15:54Z to 16:10Z, the model under the unified class, tokenizer, processor, README and
`reproduce/` folder), original pinned at `5926caa4` (06-04). The card is Heretic's generated page (28,975 bytes):
Heretic v1.4.0, direction index 28.91, attention output kernel 1.44 at position 28.65 falling to 0.11 at distance
25.21, down projection kernel 1.48 at 32.22 falling to 0.97 at 5.73, KL divergence 0.0384, refusals 27 of 100
against 99 of 100. The field `base_model` names google/gemma-4-12B, the pretrained base. The maker's third size.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 19 flags (first
shares 0.839 to 0.989), on the cluster and after re-scoring at home. On reading, the copy's windows read to the
layer and its heights do not: the fourth Heretic copy of the 12B that reads finding 46's scatter.

- 55 of 677 tensors changed: the attention outputs of layers 4 to 47 (44) and the down projections of 27 to 37
  (11) of 48. The attention kernel reaches 28.65 plus or minus 25.21, layers 4 to 47 (3.44 to 53.86); the down
  kernel 32.22 plus or minus 5.73, layers 27 to 37 (26.49 to 37.95). Both windows read exactly. Nothing else
  moved; the largest relative change outside the changed set is exactly 0.
- One shared direction: group medians 0.97 and 0.99, 0.58 across the kinds, the two writers of a layer at 0.96 to
  0.998. First shares 0.839 to 0.998.
- The side and the heights scatter. The left kept fraction is below the right on 18 of 44 attention outputs and 6
  of 11 down projections. Read as weights off the left, the attention outputs give 0.10 at layer 4, 0.07 at 12,
  0.03 at 20, 0.71 at 27, 1.44 at 29, 0.13 at 32, 0.78 at 37, 0.50 at 43 and 0.03 at 47, where the kernel runs
  0.14, 0.56, 0.98, 1.35, 1.42, 1.26, 1.00, 0.68 and 0.47: the peak layer reads, its neighbours three layers
  away read near zero. The down projections give 0.58, 1.00, 0.41 and 0.41 at layers 27, 29, 32 and 37 against
  1.02, 1.19, 1.46 and 1.06. The relative changes themselves follow the kernel (0.0022 at layer 4 rising to 0.032
  at 20 and 32, 0.011 at 47), so the edit's size is the kernel's; its measured direction's share of the
  original's action is what scatters, as on MoonRide's, 3MPER0RR's and prithivMLmods's 12B copies and unlike
  Vampelium's.
- Rows moved 0.0010 to 0.0107, Heretic's band; no restoration is claimed.

| Layer | Attention output: change, E1, left kept, right kept, kernel | Down projection: change, E1, left kept, right kept, kernel | Rows |
| --- | --- | --- | --- | --- |
| 4 | 0.0022, 0.839, 0.90, 0.96, 0.14 | | 0.0010 |
| 12 | 0.0121, 0.985, 0.93, 0.77, 0.56 | | 0.0037 |
| 20 | 0.0311, 0.996, 0.97, 0.21, 0.98 | | 0.0040 |
| 27 | 0.0278, 0.997, 0.29, 0.48, 1.35 | 0.0222, 0.995, 0.42, 0.50, 1.02 | 0.0070, 0.0066 |
| 29 | 0.0272, 0.996, -0.44, 0.49, 1.42 | 0.0256, 0.996, 0.00, 0.35, 1.19 | 0.0075, 0.0088 |
| 32 | 0.0324, 0.998, 0.87, 0.17, 1.26 | 0.0278, 0.996, 0.59, 0.05, 1.46 | 0.0064, 0.0060 |
| 37 | 0.0169, 0.992, 0.22, 0.57, 1.00 | 0.0190, 0.993, 0.59, 0.35, 1.06 | 0.0047, 0.0042 |
| 43 | 0.0115, 0.981, 0.50, 0.93, 0.68 | | 0.0066 |
| 47 | 0.0108, 0.980, 0.97, 0.81, 0.47 | | 0.0033 |

The copy's five shards (`00d8ee13`, `ac58e8ec`, `f2f6781c`, `6c287a61`, `d2bc72ec`) are its own, the five-shard
layout of the unified class; no shard equals another copy's. Its saved leading vectors stand 0.03 to 0.98 from
igorls's QAT copy's on the matrices both edit (0.97 and 0.98 on layer 29, under 0.1 on 38 to 43), so the two
copies' directions are their own.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster (four fields) and "consistent with re-save noted" at home: the three
audio fields (`audio_samples_per_token`, `hidden_size`, `output_proj_dims`) and the vision patch size, absent on
one side, load as the same values under transformers 5.22.1 (finding 11), and three repeated `dtype` fields and
the version strings are all that remain. The template is the pin's 17,466-byte file and the fixed conversation
renders identically.

## For the recipe library

The per-layer entry reads the windows and flags 19 first shares, eleven of them on layers 4 to 14 where the
attention kernel runs 0.14 to 0.67 and the edit is 0.002 to 0.014 of the matrix. The 12B remains the base on which
a Heretic entry can carry a window and a direction count and no weight (finding 46): BinxNet's E4B export, from
the same maker four days later with the same tool version, reads its heights within 0.3, and this one does not.
The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat33/measurements/pair-6/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
