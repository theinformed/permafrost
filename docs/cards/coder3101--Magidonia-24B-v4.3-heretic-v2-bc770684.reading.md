# Reading of the Stage 1 and Stage 2 result: coder3101/Magidonia-24B-v4.3-heretic-v2 against TheDrummer/Magidonia-24B-v4.3

Measured on Wheat, round 52 piece 2 (download job 387662, compare job 387664, sweep 387671; the pull carries the
measurements and the sweep record and no job log). Modified revision `d5d406a3`, created six minutes after the
maker's first pass of the same parent (round 49, finding 144); parent pinned at `5e5b5e15`, the revision that first
pass was measured against. The card is Heretic v1.1.0's table with one shared direction: `direction_index` 23.37, an
attention-output kernel of 1.31 at 29.23 falling to 1.08 at a distance of 21.85 and a down-projection kernel of 0.89
at 36.10 falling to 0.30 at a distance of 8.48 (a KL divergence of 0.0031, 20 refusals in 100 against 73). The parent
counts as neither an original nor a copy (finding 117).

## Weights (Stage 2)

The tool's assessment was violations against `single-projection-selected`, 12 flags (first shares of 0.923 to 0.985
on the twelve down projections), on the cluster and after re-scoring at home. On reading, the copy is the card's two
kernels along one direction, read to the third decimal.

- 44 of 363 tensors changed: the attention outputs of layers 8 to 39 and the down projections of layers 28 to 39,
  the kernels' reaches to the layer (7.38 to 51.08 and 27.62 to 44.58, both cut at the last layer). Everything else
  is exactly 0.
- One direction for all 44: 0.99999 at the median, 0.9990 at the least, 0.998 across the two kinds.
- Output side on all 44. One minus the left kept fraction reads 1.082 to 1.303 on the attention outputs, under the
  printed kernel by 0.0036 to 0.0053 on all 32, and 0.319 to 0.884 on the down projections, within 0.0079 of it,
  the largest gap at layer 28 where the kernel starts.
- First shares 0.991 to 0.995 on the attention outputs and 0.923 to 0.985 on the down projections, whose changes
  are the smallest (0.0045 to 0.0122); the part outside the first direction is 0.00125 to 0.00157 of the weight's
  norm, the bfloat16 rounding level. Rows moved 0.0060 to 0.0423 under a card that claims no norm.

| Layer | Kind | Change | E1 | Left kept | Right kept | Weight read | Kernel | Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8 | attention output | 0.0159 | 0.991 | -0.08 | 0.74 | 1.082 | 1.087 | 0.0100 |
| 15 | attention output | 0.0193 | 0.993 | -0.16 | 0.78 | 1.156 | 1.160 | 0.0260 |
| 22 | attention output | 0.0170 | 0.992 | -0.23 | 0.76 | 1.230 | 1.234 | 0.0199 |
| 29 | attention output | 0.0215 | 0.995 | -0.30 | 0.77 | 1.303 | 1.308 | 0.0356 |
| 39 | attention output | 0.0194 | 0.994 | -0.20 | 0.95 | 1.203 | 1.207 | 0.0373 |
| 28 | down | 0.0045 | 0.923 | 0.68 | 0.81 | 0.319 | 0.326 | 0.0066 |
| 32 | down | 0.0081 | 0.969 | 0.40 | 0.70 | 0.603 | 0.605 | 0.0160 |
| 36 | down | 0.0122 | 0.985 | 0.12 | 0.79 | 0.884 | 0.883 | 0.0100 |
| 39 | down | 0.0102 | 0.979 | 0.31 | 0.83 | 0.688 | 0.688 | 0.0084 |

The full table (44 rows) is in the report.

Directions. The copy's one direction stands at 0.990 to the direction the maker's first pass applied at layer 23
and 0.969 to the one it applied at layer 24, falling away on both sides (0.896 at 22, 0.915 at 25, 0.28 at 12, 0.56
at 35): an index of 23.37 interpolates between the per-layer directions of layers 23 and 24, and those directions are
the first pass's. Against the other Mistral Small 24B measurements it stands on the left at 0.851 to grayarea's
MPOA pass of the same parent (41 names, 0.838 to 0.853), where the first pass stood at 0.574 to it; 0.774 to
grayarea's Skyfall pass, 0.753 to the maker's Skyfall v4.2 pass, 0.686 to the first pass on the 16 names they share
(0.558 to 0.813), 0.670 and 0.600 to grayarea's text-only and Magistral passes, 0.50 to vprilepskii's edit and the
Dolphin projection, 0.49 to Pranavz's Hearthfire pass, 0.481 to the maker's per-layer pass of Mistral Small 3.2
(pair 1), 0.41 to venkycs's projection and darkc0de's pass, 0.173 to huihui-ai's projection and 0.09 or less to
llmfan46's searches.

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home: the version strings move from 4.57.1 to 4.57.3. The
template (4,722 bytes), `tokenizer.json`, `tokenizer_config.json` and `special_tokens_map.json` are the parent's by
checksum, as on the first pass.

## For the recipe library

A shared-direction kernel entry with a heights line would read both kernels; the single-projection entry charges
the small down changes under its floor. The pair is the census's first measurement of one maker's two passes of one
parent with the same tool version and two direction modes, and the saved vectors place the shared direction inside
the first pass's per-layer set at the printed index. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat52/measurements/pair-2/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
