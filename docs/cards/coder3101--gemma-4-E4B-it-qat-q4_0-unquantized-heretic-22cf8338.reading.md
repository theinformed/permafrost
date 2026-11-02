# Reading of the Stage 1 and Stage 2 result: coder3101/gemma-4-E4B-it-qat-q4_0-unquantized-heretic against google/gemma-4-E4B-it-qat-q4_0-unquantized (2026-11-02)

Measured on Wheat, round 35 piece 7 (download job 387143, compare job 387150, sweep 387152; the pull carries the
measurements and the sweep record and no job log). Modified revision `23d3e30f` (seven commits on 2026-06-06
between 16:22Z and 16:47Z: the weights, the tokenizer, the README twice, then a preprocessor file added twice),
original pinned at `dfc5b925` (06-05), the QAT-unquantized checkpoint of the E4B, one day old when the copy was
made. The card (29,501 bytes, Google's QAT card under the tool's table) says Heretic v1.2.0 with the arbitrary-rank
branch "with row-norm preservation": `start_layer_index` 20, `end_layer_index` 36, `preserve_good_behavior_weight`
0.5805, `steer_bad_behavior_weight` 0.0023, `overcorrect_relative_weight` 0.7764, `neighbor_count` 13, KL 0.0065,
5 refusals in 100 against 98. The `base_model` field names the QAT checkpoint, the inherited header reading right
on a QAT original (findings 67 and 75). The maker's seventh copy in the census and the third on a QAT checkpoint,
after the E2B's (round 32) and the 12B's (round 34).

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 16 flags (all
first shares, 0.455 to 0.969), on the cluster and after re-scoring at home. On reading, the copy is the maker's
arbitrary-rank edit as the census has read it on six other copies.

- 16 of 2,076 tensors changed: the attention outputs of layers 20 to 35, the card's start 20 and end 36 (the end
  exclusive, as on the maker's 12B exports). The down projections of those layers are exactly 0, as on the maker's
  12B QAT export; exactly 0 outside the 16, which places the copy on the QAT checkpoint (finding 48): the QAT
  file differs from the instruct model by 0.155 of layer 20's attention output (round 34's range read).
- Input side on 16 of 16: the right kept fraction is -0.19 to -0.91 (weights 1.19 to 1.91: 1.19 at 25, 1.43 at
  24, 1.80 at 26, 1.84 at 29, 1.91 at 32), the left 0.38 to 0.96. Several directions per matrix: first shares
  0.455 to 0.969 (0.46 at 34, 0.47 at 35, 0.52 at 30), each matrix its own direction (group median 0.25,
  between layers 0.03). Relative change 0.027 to 0.061.
- Rows moved 0.0065 to 0.0078 on all 16 under the card's preservation claim, finding 22's band (0.0070 to 0.0079
  on the maker's 12B QAT export, round 34).

| Layer | Change | E1 | Left kept | Right kept | Weight read | Rows |
| --- | --- | --- | --- | --- | --- | --- |
| 20 | 0.0290 | 0.941 | 0.86 | -0.45 | 1.45 | 0.0078 |
| 22 | 0.0432 | 0.734 | 0.68 | -0.41 | 1.41 | 0.0073 |
| 24 | 0.0391 | 0.969 | 0.38 | -0.43 | 1.43 | 0.0076 |
| 26 | 0.0434 | 0.751 | 0.59 | -0.80 | 1.80 | 0.0076 |
| 28 | 0.0355 | 0.864 | 0.75 | -0.54 | 1.54 | 0.0073 |
| 30 | 0.0565 | 0.522 | 0.38 | -0.62 | 1.62 | 0.0072 |
| 32 | 0.0610 | 0.595 | 0.91 | -0.91 | 1.91 | 0.0078 |
| 34 | 0.0608 | 0.455 | 0.85 | -0.40 | 1.40 | 0.0065 |
| 35 | 0.0437 | 0.468 | 0.96 | -0.77 | 1.77 | 0.0077 |

The weight read is one minus the right kept fraction. The full table (16 rows) is in the report.

Directions. The saved right vectors (the input side the edit acts on) stand at a median 0.91 to the maker's own
instruct E4B edit (round 8, 15 shared matrices, 0.84 to 0.97), the fourth maker whose QAT edit stands on his
instruct edit's directions (finding 72). They stand as high to three other E4B exports from the same branch:
JokeHer's at 0.92, NullpoLab's at 0.92, alphakek's at 0.95, and to llmfan46's two at 0.85 and 0.88. They stand at
0.37 to igorls's LoRA-rank edit of the same QAT checkpoint (pair 8), at 0.07 to prithivMLmods's linear-kernel edit
of it (round 34) and at 0.01 to huihui-ai's instruct edit. The single weight file `7b8f17c1` equals no measured
copy's.

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home: the two version strings are all that differ. The
template is the pin's 16,804-byte file and the fixed conversation renders identically.

## For the recipe library

The directional-per-layer entry is the nearest and its 16 flags are the arbitrary-rank branch's several directions
per matrix, as on the maker's four other exports; an arbitrary-rank entry (finding 22) would read the input-side
weights and the row band and flag nothing. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat35/measurements/pair-7/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
