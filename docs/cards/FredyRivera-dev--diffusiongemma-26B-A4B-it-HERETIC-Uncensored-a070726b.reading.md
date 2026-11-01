# Reading of the Stage 1 and Stage 2 result: FredyRivera-dev/diffusiongemma-26B-A4B-it-HERETIC-Uncensored against google/diffusiongemma-26B-A4B-it (2026-10-31)

Measured on Wheat, round 30 piece 7 (probe job 386940, download job 386942, compare job 386949, 1,401 seconds, sweep
386951), without the container image, under a standalone Python 3.11.18. Modified revision `9fd63a1d` (2026-06-29
at 20:59Z; the repository was created at 20:03Z, the files uploaded at 20:20Z "using upload-large-folder tool",
then four README edits), original pinned at `0f28bc42` (2026-06-10). The weights are edwixx's: the hub lists the
11 shards under the same LFS checksums (`3b78a288` to `f86b80dd`) as edwixx/diffusiongemma-26B-A4B-it-HERETIC-
Uncensored, uploaded 2026-06-11 at 15:22Z, and the README says so ("All credit to edwixx..., this repo only
includes the processor_config.json"); the one added file is a 1,689-byte `processor_config.json` so the copy
loads through AutoProcessor. edwixx's card describes the first abliteration of DiffusionGemma with Heretic and
custom patches: expert-granular ablation over all 128 `experts.down_proj` slices of the packed `[128, 2816, 704]`
parameter, a weight-tying fix because the encoder and decoder share tensors, forward hooks on the encoder layers
for the refusal direction, 200 trials with the best at 89, 13 refusals in 100 against 100, KL 0.4909. No kernel
parameters are printed. This is the first measurement of edwixx's file; pair 8 (nnnxnsn) is the same file under
a hub duplicate and confirms it in every field.

## Weights (Stage 2)

The tool's assessment was "recipe violations" on the cluster, nearest recipe `single-projection`, 68 flags (67
unexpected changes of kind "other" and one missing projection, the diffusion naming the cluster tool did not know;
see pair 6), and "recipe violations" at home with the `decoder.` names read, nearest recipe
`directional-per-layer-selected`, 86 flags: 67 first shares (25 attention outputs, 23 down projections, 19 expert
tensors) and 19 within-layer cosines. On reading, the copy is a per-layer directional edit on three writer kinds
of layers 11 to 29, including every expert of every edited layer, with a floor of round-trip residue on the
attention outputs and down projections of layers 5 to 10, and the original's layout read for the first time.

- 67 of 1,047 tensors changed: the attention outputs of layers 5 to 29 (25), the down projections of layers 7 to
  29 (23) and the packed expert down projections of layers 11 to 29 (19, all 128 experts of each). Below layer 5
  eight matrices (attention outputs of 1 to 4, down projections of 3 to 6) differ by 0.0002 to 0.00095 and count
  as unchanged under the 0.001 line; 972 tensors equal the original. No embedding, expert gate-up, vision or
  encoder tensor changed.
- Twenty of the 67 are at the floor: the attention outputs of 5 to 15 and 25 to 29 and the down projections of
  7 to 10 moved by 0.0011 to 0.0040 with first shares of 0.002 to 0.018 and kept fractions of 1.00
  on both sides, the bfloat16 round trip of a tensor the merge touched without an edit (finding 3).
- The 47 edited matrices and expert blocks are rank one: first share 0.957 to 0.989 on the dense matrices
  (attention outputs 16 to 24, down projections 11 to 29) and 0.989 to 0.992 at the median expert (0.971 at the
  worst), with the second singular value 0.01 to 0.07 of the first.
- Output side on 29 of the 48 dense entries: the down projections of 11 to 29 read −0.31 to 0.13 on the left and
  0.66 to 0.84 on the right (weights 0.87 to 1.31, above one on 11 to 15 and 17 to 25 and largest at 24), the
  attention outputs of 16 to 24 read −0.22 to 0.49 on the left (weights 0.51 to 1.22), and the experts keep 0.01 to 0.38 at the median on the
  left and 0.82 to 0.87 on the right (weights 0.62 to 0.99). Weights above one on the down projections, as
  Heretic's search allows.
- The directions agree with the group reference at 0.28 on layer 11, rising to 0.80 to 0.82 on 19 to 22 and
  falling to 0.24 at 29, and the home report flags the within-layer cosine on all 19 edited layers below the
  entry's 0.9: one direction per layer shared loosely by the three writers, drifting with depth. Experts within a
  layer agree at 0.95 to 0.999 on the left.
- Rows moved by 0.006 to 0.040 on the dense edited matrices (largest on the down projection of layer 29) and by
  0.0005 to 0.0013 at the median expert, the expert edit the smallest the census has measured on a Gemma 4
  mixture (TrevorJS's biprojection kept rows within 0.0012 with a restoration step; this one needs none at a
  relative change of 0.02).
- Relative changes of 0.021 to 0.041 on the dense matrices and 0.019 to 0.022 at the median expert.

| Layer | Attention output: change, E1, E8, left kept, right kept | Down projection: change, E1, E8, left kept, right kept | Experts: median change, median E1, worst E1, median left kept | Weight read | Within-layer cosine | Cross-layer cosine | Row norms |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | 0.0011, 0.012, 0.057, 1.00, 1.00 | - | - | 0.00/- | - | 0.14/- | 0.0002, - |
| 6 | 0.0016, 0.012, 0.065, 1.00, 1.00 | - | - | 0.00/- | - | 0.13/- | 0.0003, - |
| 7 | 0.0020, 0.011, 0.060, 1.00, 1.00 | 0.0010, 0.013, 0.060, 1.00, 1.00 | - | 0.00/0.00 | - | 0.11/0.06 | 0.0005, 0.0004 |
| 8 | 0.0022, 0.008, 0.048, 1.00, 1.00 | 0.0012, 0.018, 0.055, 1.00, 1.00 | - | 0.00/-0.00 | - | 0.02/0.02 | 0.0004, 0.0003 |
| 9 | 0.0024, 0.016, 0.057, 1.00, 1.00 | 0.0015, 0.012, 0.038, 1.00, 1.00 | - | 0.00/-0.00 | - | 0.12/0.11 | 0.0005, 0.0006 |
| 10 | 0.0025, 0.012, 0.056, 1.00, 1.00 | 0.0016, 0.005, 0.026, 1.00, 1.00 | - | 0.00/0.00 | - | 0.13/0.04 | 0.0006, 0.0005 |
| 11 | 0.0028, 0.011, 0.038, 1.00, 0.99 | 0.0206, 0.987, 0.988, -0.09, 0.84 | 0.0207, 0.990, 0.977, 0.08 | 0.00/1.09/0.92 | - | 0.11/0.28/0.28 | 0.0006, 0.0146, 0.0008 |
| 12 | 0.0030, 0.009, 0.047, 1.00, 1.00 | 0.0222, 0.987, 0.988, -0.10, 0.80 | 0.0205, 0.989, 0.971, 0.08 | 0.00/1.10/0.92 | - | 0.13/0.38/0.38 | 0.0007, 0.0212, 0.0007 |
| 13 | 0.0031, 0.008, 0.034, 1.00, 1.00 | 0.0226, 0.984, 0.985, -0.10, 0.76 | 0.0208, 0.989, 0.973, 0.03 | 0.00/1.10/0.97 | - | 0.11/0.40/0.41 | 0.0007, 0.0224, 0.0006 |
| 14 | 0.0033, 0.008, 0.029, 1.00, 1.00 | 0.0226, 0.984, 0.984, -0.07, 0.75 | 0.0217, 0.990, 0.980, 0.04 | 0.00/1.07/0.96 | - | 0.12/0.54/0.54 | 0.0008, 0.0125, 0.0008 |
| 15 | 0.0035, 0.009, 0.032, 1.00, 1.00 | 0.0212, 0.981, 0.982, -0.03, 0.77 | 0.0200, 0.990, 0.977, 0.03 | 0.00/1.03/0.97 | - | 0.13/0.62/0.62 | 0.0009, 0.0120, 0.0007 |
| 16 | 0.0209, 0.964, 0.966, 0.29, 0.61 | 0.0217, 0.980, 0.981, 0.13, 0.76 | 0.0199, 0.990, 0.980, 0.03 | 0.71/0.87/0.97 | - | 0.69/0.69/0.70 | 0.0160, 0.0135, 0.0007 |
| 17 | 0.0213, 0.964, 0.965, 0.08, 0.57 | 0.0232, 0.981, 0.981, -0.06, 0.78 | 0.0194, 0.990, 0.972, 0.38 | 0.92/1.06/0.62 | - | 0.75/0.75/0.74 | 0.0181, 0.0163, 0.0006 |
| 18 | 0.0227, 0.967, 0.968, 0.02, 0.52 | 0.0230, 0.978, 0.979, -0.09, 0.78 | 0.0188, 0.990, 0.983, 0.14 | 0.98/1.09/0.86 | - | 0.77/0.75/0.77 | 0.0107, 0.0161, 0.0005 |
| 19 | 0.0274, 0.976, 0.977, 0.49, 0.47 | 0.0265, 0.982, 0.982, -0.17, 0.73 | 0.0196, 0.990, 0.985, 0.01 | 0.51/1.17/0.99 | - | 0.79/0.78/0.80 | 0.0168, 0.0208, 0.0006 |
| 20 | 0.0279, 0.977, 0.977, -0.10, 0.51 | 0.0266, 0.982, 0.982, -0.19, 0.67 | 0.0195, 0.991, 0.984, 0.11 | 1.10/1.19/0.89 | - | 0.80/0.79/0.81 | 0.0122, 0.0131, 0.0009 |
| 21 | 0.0281, 0.976, 0.977, -0.22, 0.43 | 0.0262, 0.981, 0.981, -0.23, 0.68 | 0.0192, 0.991, 0.984, 0.16 | 1.22/1.23/0.84 | - | 0.81/0.79/0.82 | 0.0116, 0.0113, 0.0011 |
| 22 | 0.0235, 0.967, 0.968, 0.06, 0.50 | 0.0265, 0.980, 0.981, -0.15, 0.70 | 0.0191, 0.991, 0.988, 0.05 | 0.94/1.15/0.95 | - | 0.79/0.76/0.80 | 0.0104, 0.0100, 0.0011 |
| 23 | 0.0204, 0.957, 0.958, 0.12, 0.54 | 0.0252, 0.978, 0.979, -0.23, 0.69 | 0.0186, 0.991, 0.985, 0.02 | 0.88/1.23/0.98 | - | 0.73/0.71/0.75 | 0.0105, 0.0073, 0.0006 |
| 24 | 0.0212, 0.957, 0.958, 0.08, 0.48 | 0.0256, 0.978, 0.978, -0.31, 0.66 | 0.0188, 0.991, 0.987, 0.03 | 0.92/1.31/0.97 | - | 0.71/0.65/0.69 | 0.0077, 0.0062, 0.0010 |
| 25 | 0.0039, 0.004, 0.023, 1.00, 0.99 | 0.0259, 0.979, 0.979, -0.29, 0.74 | 0.0189, 0.992, 0.989, 0.01 | 0.00/1.29/0.99 | - | 0.03/0.58/0.63 | 0.0013, 0.0076, 0.0007 |
| 26 | 0.0039, 0.006, 0.023, 1.00, 0.99 | 0.0325, 0.986, 0.987, 0.08, 0.65 | 0.0201, 0.992, 0.977, 0.02 | 0.00/0.92/0.98 | - | 0.00/0.50/0.54 | 0.0011, 0.0095, 0.0006 |
| 27 | 0.0038, 0.018, 0.034, 1.00, 0.99 | 0.0368, 0.989, 0.989, 0.07, 0.69 | 0.0192, 0.992, 0.986, 0.10 | 0.00/0.93/0.90 | - | 0.01/0.46/0.51 | 0.0009, 0.0188, 0.0006 |
| 28 | 0.0037, 0.002, 0.013, 1.00, 1.00 | 0.0350, 0.987, 0.988, 0.07, 0.73 | 0.0189, 0.992, 0.990, 0.14 | 0.00/0.93/0.86 | - | 0.10/0.38/0.43 | 0.0009, 0.0127, 0.0006 |
| 29 | 0.0034, 0.003, 0.018, 1.00, 1.00 | 0.0414, 0.987, 0.992, -0.01, 0.77 | 0.0195, 0.990, 0.976, 0.13 | 0.00/1.01/0.87 | - | 0.03/0.24/0.30 | 0.0007, 0.0398, 0.0013 |

The experts column gives the median expert's relative change, the median and worst first share and the median
expert's kept fraction on the left; the weight column reads one minus the left kept fraction for the attention
output, the down projection and the median expert.

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home: the two version strings (5.8.0.dev0 to 5.11.0) and
nothing else. The configuration is the original's in every other field, the template is the original's
17,466-byte file, and the fixed conversation renders identically. The added `processor_config.json` is outside the
compared set.

## For the recipe library

The first diffusion-variant edit read with its roles: Heretic's per-layer directional edit carried onto the packed
expert tensor by iterating the 128 slices, which the measure reads as 128 rank-one edits along one direction per
layer with rows nearly unchanged. The `directional-per-layer-selected` entry fits the shape and fails on two
numbers the diffusion edit sets lower, the first-share floor (0.957 to 0.989 against 0.99) and the within-layer
cosine (0.24 to 0.82 against 0.9); an entry for the LoRA-merged Heretic form would set the floor at 0.95 and
allow the cosine to drift with depth. edwixx's own repository holds this file under the same checksums and needs
no measurement. The pull copy keeps the direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/wheat30/measurements/pair-7/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
