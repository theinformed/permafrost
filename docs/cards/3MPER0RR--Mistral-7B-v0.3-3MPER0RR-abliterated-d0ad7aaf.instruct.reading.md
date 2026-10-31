# Reading of the Stage 1 and Stage 2 result: 3MPER0RR/Mistral-7B-v0.3-3MPER0RR-abliterated against mistralai/Mistral-7B-Instruct-v0.3 (2026-10-31)

Measured on Blueback, round 14 piece 1 (push card 5421, round card 5423, download job 3401154 finished 2026-10-31
at 00:35Z, compare job 3401155; the sweep 3401163 never ran, and card 5533 pulled the measurements home). Modified
revision `2f2f0b9a`, the revision round 7 measured against the pretrained base the card names; the original here is
mistralai/Mistral-7B-Instruct-v0.3 at `c170c708`, the parent finding 8 said the weights point to. This is the one
further comparison that finding asked for.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection-selected`, 16 flags, on the
cluster and after re-scoring at home: energy shares on the weakest down projections and within-layer cosines where
the two writers' weights differ.

- 49 of 291 tensors changed: the attention outputs of layers 6 to 31 (26) and the down projections of layers 9 to
  31 (23). The other 242 tensors equal the instruct model exactly, the largest relative change outside the changed
  set is 0, and the dense 2 percent change in 226 tensors that round 7 measured against the base is gone. The copy
  is an ablation of the instruct model.
- One shared direction: 44 of 49 matrices in one cluster at cosine 0.98, cross-layer 0.92 to 0.9997, the two
  writers of a layer at 0.92 to 0.998. The leading directions equal round 7's on the same matrices (cosine median
  0.9999, least 0.988): the base comparison had already isolated the ablation's direction, with the fine-tune's
  change beneath it.
- The kernel reads cleanly now. One minus the left kept fraction is 1.10 to 1.35 on the attention outputs of
  layers 6 to 30 and 0.05 at layer 31; on the down projections it rises from 0.11 at layer 9 through 0.52 at 14
  and 1.02 at 20 to 1.32 at layer 24, then falls to 0.74 at layer 31, the per-component schedule finding 8 read
  through the fine-tune. The left is below the right on 48 of 49, an output-side edit.
- First-value share 0.806 (layer 9's down projection, relative change 0.0022) to 0.997; the shares climb with the
  weight, the storage floor on the weakest edits. Row norms moved by 0.001 to 0.011, unrestored.

| Layer | Attention output: change, E1, E8, left kept, right kept | Down projection: change, E1, E8, left kept, right kept | Weight read | Cross-layer cosine | Row norms |
| --- | --- | --- | --- | --- | --- |
| 6 | 0.0215, 0.994, 0.995, -0.19, 0.58 | unchanged | 1.19 | 1.00 | 0.0060 |
| 7 | 0.0217, 0.995, 0.995, -0.10, 0.56 | unchanged | 1.10 | 1.00 | 0.0072 |
| 8 | 0.0217, 0.995, 0.995, -0.18, 0.57 | unchanged | 1.18 | 1.00 | 0.0058 |
| 9 | 0.0222, 0.995, 0.995, -0.21, 0.56 | 0.0022, 0.806, 0.819, 0.89, 0.93 | 1.21/0.11 | 1.00/0.99 | 0.0051, 0.0010 |
| 10 | 0.0222, 0.995, 0.995, -0.21, 0.52 | 0.0036, 0.892, 0.900, 0.81, 0.88 | 1.21/0.19 | 1.00/1.00 | 0.0041, 0.0014 |
| 11 | 0.0228, 0.995, 0.995, -0.25, 0.55 | 0.0051, 0.933, 0.938, 0.73, 0.83 | 1.25/0.27 | 1.00/1.00 | 0.0055, 0.0021 |
| 12 | 0.0250, 0.996, 0.996, -0.27, 0.54 | 0.0070, 0.960, 0.963, 0.64, 0.79 | 1.27/0.36 | 1.00/1.00 | 0.0055, 0.0023 |
| 13 | 0.0267, 0.996, 0.997, -0.27, 0.54 | 0.0090, 0.974, 0.976, 0.55, 0.77 | 1.27/0.45 | 0.99/1.00 | 0.0082, 0.0027 |
| 14 | 0.0288, 0.997, 0.997, -0.30, 0.52 | 0.0106, 0.981, 0.982, 0.48, 0.71 | 1.30/0.52 | 1.00/1.00 | 0.0070, 0.0036 |
| 15 | 0.0274, 0.997, 0.997, -0.32, 0.47 | 0.0122, 0.985, 0.986, 0.38, 0.66 | 1.32/0.62 | 1.00/1.00 | 0.0097, 0.0047 |
| 16 | 0.0276, 0.997, 0.997, -0.22, 0.46 | 0.0142, 0.989, 0.989, 0.30, 0.62 | 1.22/0.70 | 1.00/1.00 | 0.0111, 0.0066 |
| 17 | 0.0246, 0.996, 0.996, -0.21, 0.61 | 0.0144, 0.989, 0.989, 0.22, 0.53 | 1.21/0.78 | 1.00/1.00 | 0.0081, 0.0055 |
| 18 | 0.0237, 0.995, 0.996, -0.09, 0.49 | 0.0150, 0.989, 0.990, 0.13, 0.43 | 1.09/0.87 | 1.00/1.00 | 0.0063, 0.0042 |
| 19 | 0.0230, 0.995, 0.995, -0.01, 0.48 | 0.0153, 0.990, 0.991, 0.06, 0.31 | 1.01/0.94 | 1.00/1.00 | 0.0052, 0.0034 |
| 20 | 0.0226, 0.995, 0.995, -0.21, 0.44 | 0.0165, 0.991, 0.992, -0.02, 0.24 | 1.21/1.02 | 1.00/1.00 | 0.0061, 0.0045 |
| 21 | 0.0211, 0.994, 0.995, -0.28, 0.45 | 0.0175, 0.992, 0.992, -0.08, 0.18 | 1.28/1.08 | 1.00/1.00 | 0.0038, 0.0035 |
| 22 | 0.0242, 0.996, 0.996, -0.30, 0.38 | 0.0187, 0.993, 0.993, -0.17, 0.13 | 1.30/1.17 | 1.00/1.00 | 0.0054, 0.0057 |
| 23 | 0.0220, 0.995, 0.995, -0.21, 0.45 | 0.0199, 0.994, 0.994, -0.25, 0.11 | 1.21/1.25 | 1.00/1.00 | 0.0034, 0.0050 |
| 24 | 0.0217, 0.995, 0.995, -0.34, 0.39 | 0.0208, 0.994, 0.995, -0.32, 0.09 | 1.34/1.32 | 1.00/1.00 | 0.0035, 0.0040 |
| 25 | 0.0228, 0.995, 0.995, -0.35, 0.39 | 0.0196, 0.994, 0.994, -0.24, 0.18 | 1.35/1.24 | 1.00/1.00 | 0.0042, 0.0044 |
| 26 | 0.0212, 0.994, 0.995, -0.32, 0.47 | 0.0185, 0.993, 0.993, -0.16, 0.27 | 1.32/1.16 | 1.00/1.00 | 0.0053, 0.0034 |
| 27 | 0.0211, 0.994, 0.995, -0.23, 0.48 | 0.0169, 0.991, 0.992, -0.08, 0.34 | 1.23/1.08 | 1.00/1.00 | 0.0035, 0.0037 |
| 28 | 0.0213, 0.994, 0.995, -0.26, 0.50 | 0.0159, 0.991, 0.991, 0.00, 0.31 | 1.26/1.00 | 1.00/1.00 | 0.0066, 0.0037 |
| 29 | 0.0212, 0.994, 0.995, -0.32, 0.49 | 0.0148, 0.989, 0.990, 0.07, 0.31 | 1.32/0.93 | 1.00/1.00 | 0.0044, 0.0029 |
| 30 | 0.0214, 0.995, 0.995, -0.20, 0.56 | 0.0135, 0.987, 0.988, 0.21, 0.38 | 1.20/0.79 | 0.99/1.00 | 0.0036, 0.0037 |
| 31 | 0.0245, 0.996, 0.996, 0.95, 0.50 | 0.0126, 0.985, 0.986, 0.26, 0.45 | 0.05/0.74 | 0.92/0.99 | 0.0065, 0.0032 |

Ten largest-absolute-difference fields equal round 7's on the same matrices, the one measure the fine-tune beneath
did not move; every other field differs from the base comparison. Against richardyoung's and evolveon's copies of
the same family, no changed matrix has an equal measurement in any field.

## Token and configuration side (Stage 1)

"Unexplained differences", 775 token fields and a few configuration forms, all a re-save under transformers
5.16.1: the added tokens moved into `tokenizer.json`, the rotary settings moved into `rope_parameters`, `head_dim`
written out (closed at home, it loads as the same default) and `torch_dtype` renamed. The copy's
`chat_template.jinja` of 3,959 bytes (`e16746b4`) is the instruct model's template byte for byte, which against
this original is a moved file and not a foreign one; the fixed conversation renders identically.

## For the recipe library

Consistent with Heretic's per-component schedule on the instruct model: 49 matrices, one shared direction, output
side, a kernel from 0.11 to 1.32 on the down projections and 1.10 to 1.35 on the attention outputs. The card's
stated original is wrong by one fine-tune and the measurement against the right one leaves nothing unexplained in
the weights. The saved direction vectors are not committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/blueback14/measurements/pair-1/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
