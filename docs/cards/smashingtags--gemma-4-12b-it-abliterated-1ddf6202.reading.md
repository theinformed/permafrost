# Reading of the Stage 1 and Stage 2 result: smashingtags/gemma-4-12b-it-abliterated against google/gemma-4-12B-it-qat-q4_0-unquantized (2026-11-02)

Measured on Nautilus, round 34 piece 6 (download job 4163806, compare job 4163812, sweep 4163815; the pull of
11-01 21:23Z carries the measurements and the sweep record and no job log). Modified revision `b9eda38b` (4
commits inside four minutes on 2026-06-14 from 17:28Z: "EOS-225: abliterated Gemma 4 12B (Google QAT base; text
decoder; vision/audio intact)", a processor configuration, the card), original pinned at `58540658`, the
QAT-unquantized checkpoint. The repository is named after the instruct model and the card (519 bytes) says
otherwise: an abliterated build of "Google's official QAT gemma-4-12B-it-qat-q4_0-unquantized", "only the text
decoder's o_proj/mlp.down_proj (top 70% of layers) were edited", vision and audio encoders and the tied
embeddings untouched, a smoke test of 3 of 3 refusals to 0 of 3, "Personal use". The field `base_model` names
the QAT checkpoint and the pinner paired by the field.

## Weights (Stage 2)

The tool's assessment was "recipe match", nearest recipe `directional-per-layer-selected`, 0 flags, on the
cluster and after re-scoring at home. On reading, the copy is a plain projection, weight 1.00, of one direction
per layer out of both writers of the top 34 layers, on the QAT checkpoint and not on the instruct model the name
suggests.

- 68 of 677 tensors changed: the attention outputs and down projections of layers 14 to 47 of 48, 34 layers, 70.8
  percent of the stack against the card's "top 70%". Nothing else moved; the largest relative change outside the
  changed set is exactly 0 against the QAT checkpoint. A byte-range read from the hub settles which original the
  copy stands on: layer 0's attention output, below the window, is byte-equal to the QAT checkpoint's and differs
  from google/gemma-4-12B-it's at `5926caa4` by 0.14 of its norm; layer 20's down projection, in the window,
  differs from the QAT checkpoint's by 0.021 and from the instruct model's by 0.74 (finding 48).
- One weight: the left kept fraction is -0.0013 to +0.0026 on all 68, a projection at exactly 1.00 along the
  leading output direction, output side on 68 of 68, first shares 0.990 to 0.999.
- One direction per layer: the two writers of a layer agree at 1.000 on every layer; across layers the directions
  drift, 0.04 at layers 14 and 47 to 0.64 at 37.
- Rows moved 0.0026 to 0.4085, the largest on layer 47's attention output (0.41) and its down projection (0.22);
  no restoration is claimed. Relative changes 0.014 to 0.051.
- Against igorls's kernel search of the same checkpoint (round 33, wheat33 pair 8) the saved leading left vectors
  stand at 0.84 to 0.98 on 56 of the 57 shared matrices (median 0.951; 0.57 at layer 47): a plain projection with
  no search over weights and Heretic's search over kernels found the same per-layer directions. Against
  huihui-ai's QAT edit of this base the median is 0.38 (0.86 on layers 23 to 25, falling to 0.09); against
  huihui-ai's instruct edit 0.62; against Vampelium's instruct edit the cosine climbs from 0.03 at layer 14 to
  0.87 at 33 and 34 and falls to 0.08 at 47.

| Layer | Attention output: change, E1, left kept, right kept | Down projection: change, E1, left kept, right kept | Cross-layer cosine | Rows |
| --- | --- | --- | --- | --- |
| 14 | 0.0442, 0.999, 0.0008, 0.89 | 0.0286, 0.999, 0.0004, 0.91 | 0.038 | 0.1256, 0.1033 |
| 16 | 0.0179, 0.997, 0.0006, 0.91 | 0.0189, 0.997, 0.0000, 0.50 | 0.230 | 0.0303, 0.0118 |
| 18 | 0.0197, 0.997, 0.0005, 0.77 | 0.0212, 0.997, -0.0001, 0.89 | 0.201 | 0.0340, 0.0395 |
| 20 | 0.0226, 0.997, 0.0000, 0.92 | 0.0207, 0.996, 0.0004, 0.82 | 0.223 | 0.0211, 0.0203 |
| 22 | 0.0166, 0.994, 0.0010, 0.81 | 0.0199, 0.995, -0.0005, 0.67 | 0.404 | 0.0126, 0.0153 |
| 24 | 0.0163, 0.993, 0.0004, 0.76 | 0.0188, 0.994, 0.0004, 0.64 | 0.458 | 0.0069, 0.0052 |
| 26 | 0.0226, 0.996, -0.0000, 0.86 | 0.0213, 0.995, 0.0000, 0.70 | 0.418 | 0.0332, 0.0237 |
| 28 | 0.0215, 0.995, 0.0003, 0.79 | 0.0228, 0.996, 0.0003, 0.71 | 0.510 | 0.0936, 0.0998 |
| 30 | 0.0181, 0.993, 0.0007, 0.71 | 0.0193, 0.994, 0.0004, 0.53 | 0.572 | 0.0356, 0.0329 |
| 32 | 0.0263, 0.997, 0.0006, 0.90 | 0.0202, 0.994, 0.0009, 0.71 | 0.603 | 0.0419, 0.0316 |
| 34 | 0.0289, 0.997, -0.0001, 0.87 | 0.0217, 0.995, -0.0000, 0.61 | 0.621 | 0.0993, 0.0968 |
| 36 | 0.0199, 0.994, 0.0004, 0.96 | 0.0172, 0.992, 0.0008, 0.56 | 0.636 | 0.0334, 0.0360 |
| 38 | 0.0368, 0.998, 0.0003, 0.85 | 0.0216, 0.995, -0.0000, 0.72 | 0.619 | 0.1038, 0.0965 |
| 40 | 0.0167, 0.992, 0.0007, 0.64 | 0.0179, 0.993, 0.0004, 0.28 | 0.542 | 0.0036, 0.0026 |
| 42 | 0.0185, 0.993, 0.0003, 0.94 | 0.0174, 0.992, 0.0005, 0.46 | 0.517 | 0.0109, 0.0088 |
| 44 | 0.0264, 0.996, -0.0005, 0.95 | 0.0199, 0.994, 0.0002, 0.63 | 0.485 | 0.0470, 0.0514 |
| 46 | 0.0161, 0.991, 0.0004, 0.66 | 0.0178, 0.993, 0.0004, 0.48 | 0.359 | 0.0026, 0.0030 |
| 47 | 0.0511, 0.999, 0.0016, 0.72 | 0.0137, 0.990, 0.0026, 0.79 | 0.038 | 0.4085, 0.2191 |

The copy's one weight file is `35391191`, its own; no measured file is equal.

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home: the two version strings (5.10.0.dev0 to 5.12.0) are
all that differ. The template is the pin's 17,466-byte file and the fixed conversations render identically.

## For the recipe library

The per-layer entry matches in every measure; the reading adds the weight (1.00) and the parent (the QAT
checkpoint under an instruct-model name). The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus34/measurements/pair-6/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
