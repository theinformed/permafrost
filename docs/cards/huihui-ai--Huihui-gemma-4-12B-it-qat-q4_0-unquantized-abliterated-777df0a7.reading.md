# Reading of the Stage 1 and Stage 2 result: huihui-ai/Huihui-gemma-4-12B-it-qat-q4_0-unquantized-abliterated against google/gemma-4-12B-it-qat-q4_0-unquantized (2026-11-01)

Measured on Nautilus, round 32 piece 4 (download job 4145233, compare job 4145237, 715 seconds, sweep 4145242).
Modified revision `5201f482` (eight commits from 2026-06-08 05:34Z to 06-09 15:28Z: the weights at 06:13Z on the
first day by the large-folder tool, a README created before them and edited five times after), original pinned
at `58540658`, the revision current when the repository was created. The original is the checkpoint Google
extracted from quantisation-aware training of the 12B instruct model, published in bfloat16 under a name that
ends in `-qat-q4_0-unquantized`; this is the first measurement on it. The card names the method as abliteration
with the remove-refusals code and says layers 23 to 36 were treated. The `base_model` field names the QAT
checkpoint.

## Weights (Stage 2)

The tool's assessment was "recipe match", recipe `directional-per-layer-selected`, 0 flags, on the cluster and
after re-scoring at home. On reading, the footprint is the card's window, the weight is 1.0, and the edit is the
maker's 12B method on a longer window.

- 28 of 677 tensors changed: the attention output and the down projection of layers 23 to 36, the card's
  fourteen layers. Nothing else moved; the largest relative change outside the changed set is exactly 0 and 649
  tensors equal the original.
- One direction per matrix (first share 0.992 to 0.997), the two writers of each layer agreeing at 1.000. Layers
  27 to 36 share one direction (cosine 1.000 to the group reference); layers 23 to 26 take up a second at 0.66
  to 0.71 to the first, with the two writers of each of those layers still at 1.000.
- The left kept fraction is -0.005 to 0.005 on all 28, a weight of 1.00; the right is 0.49 to 0.97 and the left
  is below the right on 28 of 28, an output-side edit.
- Rows moved by 0.016 to 0.17 (0.17 on the attention output of layer 34), the unrestored leftover of a plain
  projection.
- Relative changes of 0.016 to 0.027.

| Layer | Attention output: change, E1, E4, left kept, right kept | Down projection: change, E1, E4, left kept, right kept | Weight read | Cross-layer cosine | Row norms |
| --- | --- | --- | --- | --- | --- |
| 23 | 0.0231, 0.996, 0.997, 0.00, 0.91 | 0.0223, 0.996, 0.996, 0.00, 0.64 | 1.00/1.00 | 0.66/0.66 | 0.0593, 0.0581 |
| 24 | 0.0217, 0.996, 0.996, 0.00, 0.84 | 0.0243, 0.996, 0.997, 0.00, 0.82 | 1.00/1.00 | 0.66/0.66 | 0.0603, 0.0597 |
| 25 | 0.0196, 0.996, 0.996, 0.00, 0.84 | 0.0232, 0.996, 0.996, 0.00, 0.82 | 1.00/1.00 | 0.66/0.66 | 0.0597, 0.0610 |
| 26 | 0.0270, 0.997, 0.997, -0.00, 0.85 | 0.0240, 0.996, 0.996, -0.00, 0.82 | 1.00/1.00 | 0.71/0.71 | 0.0726, 0.0707 |
| 27 | 0.0173, 0.994, 0.994, -0.00, 0.77 | 0.0195, 0.994, 0.995, -0.00, 0.69 | 1.00/1.00 | 1.00/1.00 | 0.0298, 0.0284 |
| 28 | 0.0180, 0.994, 0.994, -0.00, 0.79 | 0.0175, 0.993, 0.993, -0.00, 0.54 | 1.00/1.00 | 1.00/1.00 | 0.0307, 0.0216 |
| 29 | 0.0157, 0.992, 0.992, -0.00, 0.67 | 0.0184, 0.994, 0.994, -0.00, 0.55 | 1.00/1.00 | 1.00/1.00 | 0.0161, 0.0375 |
| 30 | 0.0169, 0.993, 0.993, -0.00, 0.64 | 0.0186, 0.994, 0.994, -0.00, 0.71 | 1.00/1.00 | 1.00/1.00 | 0.0333, 0.0426 |
| 31 | 0.0172, 0.993, 0.993, -0.00, 0.70 | 0.0196, 0.994, 0.995, -0.00, 0.79 | 1.00/1.00 | 1.00/1.00 | 0.0415, 0.0433 |
| 32 | 0.0234, 0.996, 0.996, -0.00, 0.91 | 0.0217, 0.995, 0.995, -0.00, 0.79 | 1.00/1.00 | 1.00/1.00 | 0.0559, 0.0549 |
| 33 | 0.0266, 0.997, 0.997, -0.00, 0.90 | 0.0197, 0.994, 0.995, -0.00, 0.78 | 1.00/1.00 | 1.00/1.00 | 0.0537, 0.0463 |
| 34 | 0.0218, 0.995, 0.996, -0.00, 0.90 | 0.0175, 0.993, 0.993, -0.00, 0.61 | 1.00/1.00 | 1.00/1.00 | 0.1737, 0.0427 |
| 35 | 0.0209, 0.995, 0.995, -0.00, 0.93 | 0.0164, 0.992, 0.993, -0.00, 0.49 | 1.00/1.00 | 1.00/1.00 | 0.0505, 0.0413 |
| 36 | 0.0203, 0.995, 0.995, -0.00, 0.97 | 0.0165, 0.992, 0.993, -0.00, 0.63 | 1.00/1.00 | 1.00/1.00 | 0.0474, 0.0456 |

The weight column reads one minus the left kept fraction on both writers.

The fingerprint stands alone on this original. Against the maker's copy of the instruct 12B (round 13: layers 23
to 28, weight 1.00, rows 0.016 to 0.079), this one reaches eight layers further at the same weight, which is the
seventh weight read on a seventh base from the maker's one script (finding 21), and the first to carry a card
whose window matches the edit on a QAT checkpoint.

## Token and configuration side (Stage 1)

"Consistent" on the cluster and at home: no compared field differs. The configuration, the generation settings
and the token files equal the original's field for field, the version strings included (5.10.0.dev0 on both
sides), and the fixed conversation renders identically. The first Gemma 4 copy in the census whose token side
is the original's to the byte.

## For the recipe library

The maker's shared projection at weight 1.0 on the QAT-unquantized 12B, on the card's window, with nothing else
moved: the `directional-per-layer-selected` entry matches with no flag. The QAT checkpoints are a new set of
originals (three entered the census this round, finding 48), and this copy shows the maker's script treats them
as it treats the instruct files, with a different layer choice. The pull copy keeps the direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus32/measurements/pair-4/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
