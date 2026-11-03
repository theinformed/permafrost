# Reading of the Stage 1 and Stage 2 result: grayarea/Magidonia-24B-v4.3-heretic-v1.2 against TheDrummer/Magidonia-24B-v4.3

Measured on Wheat, round 51 piece 1 (download job 387623, compare job 387624, sweep 387632; the pull carries the
measurements and the sweep record and no job log). Modified revision `52756d95` (created 2026-03-03 11:30Z, the
weights uploaded at 11:34Z, the card edited at 11:44Z and 12:41Z), parent pinned at `5e5b5e15` of 2025-12-17,
TheDrummer's Magidonia 24B v4.3, the same parent and revision as coder3101's pass of round 49
(`results/weights/coder3101-Magidonia-24B-v4.3-heretic.json`, finding 144). The card names Heretic v1.2.0 with MPOA,
full row renormalization, a winsorization quantile of 0.995 and a customised training dataset, and prints a table
with a fractional `direction_index` of 21.80, an attention-output kernel of 1.16 at 24.83 falling to 0.95 at a
distance of 14.27, and a down-projection kernel of 1.37 at 25.89 falling to 0.46 at a distance of 20.80 (a KL
divergence of 0.0229, 0 refusals in 108 against 76). The parent counts as neither an original nor a copy (finding
117).

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 35 flags (first shares under the
0.99 floor on 21 down projections and 14 attention outputs), on the cluster and after re-scoring at home;
`single-projection-selected` stood second with 36. On reading, the copy is one shared direction over the two
printed kernels' reaches, the down kernel read to within 0.034 and the attention kernel read under its height.

- 63 of 363 tensors changed: the down projections of layers 6 to 39 and the attention outputs of 11 to 39, the two
  kernels' reaches (5.09 to 46.69 and 10.56 to 39.10) cut at the last layer. Everything else is exactly 0, and the
  copy's first shard is the parent's by object id.
- One direction serves every layer and both writers: 0.999 to the common direction at the median, 0.973 at the
  least, 0.945 across kinds, the two writers of a layer at 0.998.
- Output side on all 63. One minus the left kept fraction reads 0.491 to 1.348 on the down projections, within
  0.034 of the printed kernel on all 34 and under it on 32; on the attention outputs it reads 0.779 to 1.075, 0.021
  to 0.098 under the kernel on 27 of 29 and 0.35 and 0.21 under it at layers 27 and 29.
- First shares 0.961 to 0.996; relative changes 0.0071 to 0.0244; rows moved 0.0019 to 0.0159 under "full row
  renormalization".

| Layer | Kind | Change | E1 | Left kept | Right kept | Weight read | Kernel | Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 11 | attention output | 0.0147 | 0.989 | 0.08 | 0.73 | 0.922 | 0.956 | 0.0033 |
| 19 | attention output | 0.0202 | 0.994 | -0.03 | 0.84 | 1.026 | 1.074 | 0.0097 |
| 25 | attention output | 0.0187 | 0.993 | -0.08 | 0.69 | 1.075 | 1.157 | 0.0075 |
| 27 | attention output | 0.0176 | 0.992 | 0.22 | 0.74 | 0.779 | 1.128 | 0.0049 |
| 29 | attention output | 0.0162 | 0.991 | 0.11 | 0.66 | 0.886 | 1.099 | 0.0042 |
| 33 | attention output | 0.0140 | 0.988 | -0.01 | 0.69 | 1.006 | 1.040 | 0.0026 |
| 39 | attention output | 0.0139 | 0.988 | 0.10 | 0.88 | 0.902 | 0.951 | 0.0053 |
| 6 | down | 0.0071 | 0.961 | 0.51 | 0.76 | 0.491 | 0.500 | 0.0023 |
| 13 | down | 0.0123 | 0.985 | 0.22 | 0.59 | 0.780 | 0.806 | 0.0044 |
| 20 | down | 0.0195 | 0.993 | -0.11 | 0.81 | 1.111 | 1.112 | 0.0119 |
| 26 | down | 0.0189 | 0.993 | -0.35 | 0.00 | 1.348 | 1.365 | 0.0045 |
| 30 | down | 0.0160 | 0.991 | -0.16 | 0.18 | 1.159 | 1.190 | 0.0044 |
| 33 | down | 0.0142 | 0.988 | -0.02 | 0.39 | 1.025 | 1.059 | 0.0029 |
| 39 | down | 0.0113 | 0.982 | 0.21 | 0.72 | 0.790 | 0.796 | 0.0033 |

The full table (63 rows) is in the report.

Two makers on one checkpoint. coder3101's pass of round 49 on the same parent at the same revision is Heretic
v1.1.0 with one direction per layer, the down projections of layers 12 to 35 and the attention outputs of 27 to 34,
both kernels read within 0.0050 (finding 144). Against its saved vectors this copy's direction stands at 0.574 on
the left and 0.522 on the right on the 32 shared names (minimum 0.300). By byte range on four matrices both copies
edit, the leading directions of the two changes stand at 0.578 and 0.514 (left and right) on the layer 30 attention
output, 0.651 and 0.569 on the layer 27 attention output, 0.795 and 0.853 on the layer 20 down projection and 0.490
and 0.403 on the layer 33 down projection; the two changes stand at 0.29, 0.37, 0.67 and 0.20 to each other as
matrices, this copy's 1.04 to 1.34 times the size of coder3101's, and the two copies stand 0.0161, 0.0177, 0.0149
and 0.0177 apart where each stands 0.012 to 0.019 from the parent. The layer 5 query projection is the parent's
bytes on both.

Directions. Against the saved vectors of the Mistral Small 24B measurements the direction stands on the left at
0.882 to the maker's Skyfall v4.1 pass of this round (pair 3), 0.829 to coder3101's Skyfall v4.2 pass, 0.774 and
0.691 to the maker's text-only Mistral Small 3.2 and Magistral passes, 0.574 to coder3101's Magidonia pass, 0.551 to
vprilepskii's Harbinger edit and SAIFIINDUSTRIES's Dolphin projection, 0.449 to venkycs's projection, 0.414 to
darkc0de's Mistral Small 3.2 pass of this round (pair 4), 0.39 or less to Pranavz's two Hearthfire measurements and
0.22 or less to huihui-ai's projection and llmfan46's searches.

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home: the version strings move from 4.57.1 to 4.57.3. The
template (4,722 bytes, `4ad87a4f`), `tokenizer_config.json` and `special_tokens_map.json` are the parent's by object
id; `tokenizer.json` is 155 bytes longer than the parent's, a re-save, and the fixed conversation renders the same.
The token ids are Mistral's through the parent (`bos_token_id` 1, `eos_token_id` `[2]`, `pad_token_id` 11) and the
vocabulary is 131,072.

## For the recipe library

A shared-direction kernel entry with a heights line would read the down projections to the third decimal of the
shape and charge the attention outputs at layers 27 and 29, where this copy and darkc0de's pass of Mistral Small
3.2 both fall short of the printed height (finding 154). The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat51/measurements/pair-1/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
