# Reading of the Stage 1 and Stage 2 result: coder3101/Mistral-Small-3.2-24B-Instruct-2506-heretic against mistralai/Mistral-Small-3.2-24B-Instruct-2506

Measured on Wheat, round 52 piece 1 (download job 387662, compare job 387663, sweep 387671; the pull, card 5849,
carries the measurements and the sweep record and no job log). Modified revision `1e166c40`, original pinned at
`95a6d26c`, the latest commit at or before the copy was created. The card is Mistral's README under Heretic
v1.1.0's per-layer table: an attention-output kernel of 1.28 at 23.69 falling to 0.06 at a distance of 6.19 and a
down-projection kernel of 1.43 at 24.70 falling to 0.73 at a distance of 22.95 (a KL divergence of 0.1383, 5
refusals in 100 against 97). Its first line names the instruct checkpoint and its `base_model` field, copied from
Mistral's README, names mistralai/Mistral-Small-3.1-24B-Base-2503; the pinner took the card's parent. The copy
publishes two weight files, `model.safetensors` in the transformers layout and `consolidated.safetensors` in
Mistral's own; the comparison read the first.

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 12 flags (first shares under the
0.99 floor on seven attention outputs and five down projections), on the cluster and after re-scoring at home. On
reading, the copy is the card's two kernels, one direction per layer on both writers, read to the third decimal.

- 50 of 585 tensors changed: the down projections of layers 2 to 39 and the attention outputs of layers 18 to 29,
  the two kernels' reaches to the layer (1.75 to 47.65 cut at the last layer, and 17.50 to 29.88). Everything else,
  the vision tower included, is exactly 0.
- One direction per layer: the two writers of a layer agree at 1.000 at the median (0.995 at the least), the layers
  at 0.67.
- Output side on all 50. One minus the left kept fraction reads 0.736 to 1.420 on the down projections, within
  0.0017 of the printed kernel on all 38 and a little under it on every one, and 0.153 to 1.218 on the attention
  outputs, within 0.0025 on 11 of 12 and 0.0060 under it at layer 18, the kernel's edge. At layers 27 and 29 it reads
  0.630 and 0.233 against kernel values of 0.628 and 0.233.
- First shares 0.856 to 0.998, the lowest where the attention kernel falls toward its minimum. The part of each
  change outside its first direction is 0.00105 to 0.00160 of the weight's norm, the bfloat16 rounding the
  calibration single projection of this checkpoint left (0.00151 to 0.00156) or less, inside the calibrated line of
  0.0025; the twelve flags are small edits read against the analytic floor.
- Relative changes 0.0028 to 0.0340; rows moved 0.0029 to 0.0656 under a card that claims no norm.
- By byte range the consolidated file carries the same edit: its layer 24 attention output is the transformers
  file's bytes and 0.0244 from Mistral's consolidated file, and its layer 5 attention output is Mistral's bytes. Both
  consolidated files hold 585 tensors.

| Layer | Kind | Change | E1 | Left kept | Right kept | Weight read | Kernel | Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 18 | attention output | 0.0028 | 0.856 | 0.85 | 0.97 | 0.153 | 0.159 | 0.0029 |
| 20 | attention output | 0.0099 | 0.978 | 0.45 | 0.87 | 0.553 | 0.553 | 0.0074 |
| 24 | attention output | 0.0244 | 0.996 | -0.22 | 0.85 | 1.218 | 1.219 | 0.0514 |
| 27 | attention output | 0.0121 | 0.985 | 0.37 | 0.92 | 0.630 | 0.628 | 0.0215 |
| 29 | attention output | 0.0041 | 0.911 | 0.77 | 0.97 | 0.233 | 0.233 | 0.0063 |
| 2 | down | 0.0119 | 0.985 | 0.26 | 0.75 | 0.736 | 0.738 | 0.0323 |
| 10 | down | 0.0164 | 0.991 | 0.02 | 0.54 | 0.981 | 0.982 | 0.0146 |
| 25 | down | 0.0226 | 0.995 | -0.42 | 0.52 | 1.420 | 1.421 | 0.0552 |
| 33 | down | 0.0164 | 0.991 | -0.18 | 0.36 | 1.175 | 1.177 | 0.0219 |
| 39 | down | 0.0171 | 0.992 | 0.01 | 0.81 | 0.993 | 0.994 | 0.0270 |

The full table (50 rows) is in the report.

Directions. Against the saved vectors of the Mistral Small 24B measurements the direction stands on the left at
0.926 to darkc0de's Heretic 1.2 per-layer pass of the same checkpoint (43 shared names, 0.892 to 0.963 name by name,
0.915 on the right), 0.80 to Pranavz's Hearthfire pass in both of its measurements, 0.672 to the maker's per-layer
pass of Magidonia, 0.481 to the maker's shared-direction pass of Magidonia (pair 2), 0.40 to 0.51 to the five
shared-direction passes on the hidden size, 0.32 or less to vprilepskii's edit and the projections of Mistral Small
24B and the Dolphin fine-tune, 0.23 or less to llmfan46's searches and 0.104 to huihui-ai's projection of this
checkpoint.

## Token and configuration side (Stage 1)

"Undecided" on the cluster and at home. Mistral's repository publishes `tekken.json` and no `tokenizer.json`,
`tokenizer_config.json` or template, and the copy publishes none either, so the tool had no template to render on
either side. The configuration and generation file differ in the saved version string alone (4.52.4 against
5.1.0).

## For the recipe library

A per-layer kernel entry with a heights line would read this copy with no flag on the kernels, and the calibrated
leftover line of the Mistral Small 3.2 calibration would clear the twelve first shares. The pinner read the card's
parent where the field names the pretrained 3.1 base, the header case of finding 67 on a Mistral checkpoint. A
copy that publishes a second weight file in another layout needs the second file read as well; here a byte-range
check of two matrices stands in for it. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat52/measurements/pair-1/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
