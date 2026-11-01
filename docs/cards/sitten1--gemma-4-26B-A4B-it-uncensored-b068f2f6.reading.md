# Reading of the Stage 1 and Stage 2 result: sitten1/gemma-4-26B-A4B-it-uncensored against google/gemma-4-26B-A4B-it (2026-10-31)

Measured on Wheat, round 30 piece 1 (probe job 386940, download job 386942, compare job 386943, 1,678 seconds, sweep
386951), the first round run without the container image, under a standalone Python 3.11.18 built in the project's
work space. Modified revision `ddbf5076` (one commit, 2026-04-08 at 20:36Z, "Duplicate from
TrevorJS/gemma-4-26B-A4B-it-uncensored"; the README is TrevorJS's of that date, 4,523 bytes, byte for byte, 15 bytes
short of the parent's current file, which fixed a link on 06-13), original pinned at `47b6801b` (2026-04-02), the pin
TrevorJS's own measurement used in round 2. The card is the source's: norm-preserving biprojected abliteration on the
attention output, the shared down projection and all 128 expert down projections of every layer, per-layer refusal
directions, scale 1.0. The repository's `base_model` field names Google.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer`, 31 flags, on the cluster and
after re-scoring at home: 30 energy shares on the packed expert tensors (the worst expert of each layer, 0.881 to
0.990) and one within-layer cosine (layer 29, 0.949), the flags TrevorJS's second-pass report carries. The weight file
is TrevorJS's: the hub lists the two shards of 49,323,334,202 and 2,288,675,130 bytes under the same LFS checksums
(`4b988df4e5`, `3d2388e809`) in the three repositories, the comparison read the same shard checksums, and the
measurement equals the round 3 second pass (`results/weights/TrevorJS-gemma-4-26B-A4B-it-uncensored.pass-2.json`)
in every field that does not depend on the randomised sketch: relative change, difference norm, largest absolute
difference, row norms and sign fractions equal to the last digit on all 90 changed tensors, the 30 per-expert blocks
equal, 923 tensors equal to the original, 0 outside the changed set. The first shares and direction cosines differ
from the second pass by at most 2.3 × 10⁻⁶ and 2.0 × 10⁻⁸, the sketch's seed running on another machine's
arithmetic, and the 30 flagged tensors are the same 30. The reading is in
`TrevorJS--gemma-4-26B-A4B-it-uncensored-*.reading.md`: 90 of 1,013 tensors changed, one direction per layer shared
by the three writers (within-layer cosine 0.949 to 0.998), output side on all 60 dense matrices, remaining fraction
0.02 to 0.28 on the attention outputs and 0.00 to 0.51 on the down projections, every expert of every layer edited
along the layer's direction, rows within 0.0012 under the biprojection's restoration. Pair 2 (erunda337) is the same
file again under another duplicate.

| Layer | Attention output: change, E1, E8, left kept, right kept | Down projection: change, E1, E8, left kept, right kept | Experts: median change, median E1, worst E1, median left kept | Weight read | Within-layer cosine | Cross-layer cosine | Row norms |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0.0291, 0.994, 0.997, 0.08, 0.68 | 0.0219, 0.993, 0.995, 0.03, 0.74 | 0.0191, 0.989, 0.881, 0.20 | 0.92/0.97/0.80 | 0.995 | 0.03/0.03/0.03 | 0.0002, 0.0003, 0.0006 |
| 1 | 0.0275, 0.996, 0.997, 0.10, 0.49 | 0.0213, 0.994, 0.996, 0.07, 0.70 | 0.0185, 0.993, 0.969, 0.07 | 0.90/0.93/0.93 | 0.988 | 0.04/0.03/0.03 | 0.0002, 0.0005, 0.0006 |
| 2 | 0.0247, 0.996, 0.997, 0.14, 0.47 | 0.0186, 0.995, 0.996, 0.03, 0.84 | 0.0197, 0.994, 0.951, 0.03 | 0.86/0.97/0.97 | 0.991 | 0.06/0.07/0.06 | 0.0002, 0.0003, 0.0006 |
| 3 | 0.0254, 0.994, 0.997, 0.20, 0.53 | 0.0185, 0.995, 0.996, 0.02, 0.64 | 0.0201, 0.994, 0.981, 0.03 | 0.80/0.98/0.97 | 0.980 | 0.11/0.12/0.12 | 0.0002, 0.0003, 0.0012 |
| 4 | 0.0301, 0.992, 0.997, 0.25, 0.45 | 0.0214, 0.991, 0.996, 0.11, 0.72 | 0.0196, 0.991, 0.983, 0.05 | 0.75/0.89/0.95 | 0.984 | 0.18/0.18/0.19 | 0.0002, 0.0003, 0.0008 |
| 5 | 0.0254, 0.992, 0.997, 0.20, 0.56 | 0.0212, 0.994, 0.996, 0.07, 0.76 | 0.0196, 0.993, 0.987, 0.05 | 0.80/0.93/0.95 | 0.987 | 0.23/0.21/0.21 | 0.0002, 0.0002, 0.0008 |
| 6 | 0.0285, 0.993, 0.997, 0.24, 0.48 | 0.0197, 0.994, 0.996, 0.05, 0.74 | 0.0200, 0.992, 0.984, 0.04 | 0.76/0.95/0.96 | 0.985 | 0.24/0.23/0.23 | 0.0003, 0.0004, 0.0007 |
| 7 | 0.0235, 0.994, 0.996, 0.23, 0.51 | 0.0181, 0.994, 0.995, 0.04, 0.78 | 0.0203, 0.991, 0.984, 0.04 | 0.77/0.96/0.96 | 0.982 | 0.30/0.27/0.27 | 0.0002, 0.0005, 0.0008 |
| 8 | 0.0247, 0.994, 0.996, 0.22, 0.50 | 0.0189, 0.994, 0.995, 0.03, 0.77 | 0.0205, 0.992, 0.986, 0.02 | 0.78/0.97/0.98 | 0.983 | 0.37/0.34/0.34 | 0.0002, 0.0004, 0.0007 |
| 9 | 0.0246, 0.994, 0.996, 0.28, 0.48 | 0.0214, 0.993, 0.994, 0.34, 0.79 | 0.0206, 0.992, 0.980, 0.09 | 0.72/0.66/0.91 | 0.971 | 0.44/0.41/0.41 | 0.0002, 0.0004, 0.0008 |
| 10 | 0.0284, 0.993, 0.996, 0.27, 0.50 | 0.0190, 0.992, 0.994, -0.00, 0.84 | 0.0222, 0.991, 0.980, 0.01 | 0.73/1.00/0.99 | 0.962 | 0.52/0.50/0.51 | 0.0002, 0.0004, 0.0011 |
| 11 | 0.0232, 0.992, 0.996, 0.25, 0.57 | 0.0189, 0.992, 0.993, 0.04, 0.81 | 0.0203, 0.990, 0.984, 0.06 | 0.75/0.96/0.94 | 0.977 | 0.52/0.51/0.52 | 0.0002, 0.0004, 0.0008 |
| 12 | 0.0235, 0.993, 0.996, 0.24, 0.49 | 0.0184, 0.991, 0.993, 0.04, 0.82 | 0.0206, 0.990, 0.981, 0.07 | 0.76/0.96/0.93 | 0.970 | 0.52/0.52/0.54 | 0.0002, 0.0003, 0.0009 |
| 13 | 0.0231, 0.992, 0.995, 0.15, 0.56 | 0.0188, 0.992, 0.993, 0.06, 0.80 | 0.0210, 0.990, 0.981, 0.09 | 0.85/0.94/0.91 | 0.981 | 0.52/0.52/0.53 | 0.0002, 0.0002, 0.0007 |
| 14 | 0.0219, 0.993, 0.995, 0.07, 0.57 | 0.0198, 0.992, 0.993, 0.08, 0.78 | 0.0217, 0.991, 0.981, 0.04 | 0.93/0.92/0.96 | 0.990 | 0.59/0.57/0.59 | 0.0002, 0.0005, 0.0007 |
| 15 | 0.0222, 0.993, 0.995, 0.06, 0.62 | 0.0187, 0.992, 0.993, 0.10, 0.77 | 0.0204, 0.991, 0.982, 0.02 | 0.94/0.90/0.98 | 0.986 | 0.61/0.58/0.61 | 0.0002, 0.0004, 0.0010 |
| 16 | 0.0221, 0.992, 0.994, 0.10, 0.53 | 0.0187, 0.991, 0.992, 0.25, 0.79 | 0.0201, 0.990, 0.979, 0.02 | 0.90/0.75/0.98 | 0.982 | 0.62/0.58/0.62 | 0.0004, 0.0004, 0.0009 |
| 17 | 0.0205, 0.992, 0.994, 0.06, 0.54 | 0.0193, 0.991, 0.992, 0.14, 0.83 | 0.0195, 0.990, 0.973, 0.28 | 0.94/0.86/0.72 | 0.990 | 0.62/0.60/0.64 | 0.0002, 0.0005, 0.0006 |
| 18 | 0.0197, 0.992, 0.993, 0.20, 0.59 | 0.0189, 0.991, 0.992, 0.16, 0.84 | 0.0188, 0.990, 0.981, 0.14 | 0.80/0.84/0.86 | 0.986 | 0.62/0.58/0.62 | 0.0002, 0.0006, 0.0007 |
| 19 | 0.0212, 0.993, 0.994, 0.16, 0.55 | 0.0206, 0.992, 0.993, 0.08, 0.80 | 0.0192, 0.990, 0.980, 0.12 | 0.84/0.92/0.88 | 0.988 | 0.62/0.59/0.63 | 0.0002, 0.0006, 0.0007 |
| 20 | 0.0198, 0.992, 0.993, 0.06, 0.62 | 0.0204, 0.993, 0.993, 0.07, 0.77 | 0.0194, 0.991, 0.984, 0.06 | 0.94/0.93/0.94 | 0.989 | 0.63/0.59/0.63 | 0.0002, 0.0004, 0.0009 |
| 21 | 0.0216, 0.993, 0.994, 0.02, 0.55 | 0.0196, 0.992, 0.993, 0.08, 0.75 | 0.0191, 0.991, 0.984, 0.12 | 0.98/0.92/0.88 | 0.993 | 0.62/0.60/0.62 | 0.0002, 0.0005, 0.0006 |
| 22 | 0.0200, 0.993, 0.994, 0.09, 0.52 | 0.0193, 0.992, 0.993, 0.15, 0.77 | 0.0192, 0.991, 0.988, 0.10 | 0.91/0.85/0.90 | 0.989 | 0.58/0.56/0.60 | 0.0002, 0.0004, 0.0012 |
| 23 | 0.0188, 0.993, 0.993, 0.15, 0.59 | 0.0192, 0.992, 0.993, 0.07, 0.81 | 0.0187, 0.991, 0.985, 0.01 | 0.85/0.93/0.99 | 0.990 | 0.52/0.53/0.56 | 0.0002, 0.0005, 0.0005 |
| 24 | 0.0219, 0.994, 0.994, 0.03, 0.45 | 0.0191, 0.992, 0.993, 0.06, 0.78 | 0.0190, 0.991, 0.987, 0.09 | 0.97/0.94/0.91 | 0.989 | 0.51/0.51/0.52 | 0.0002, 0.0003, 0.0010 |
| 25 | 0.0181, 0.992, 0.993, 0.04, 0.59 | 0.0192, 0.992, 0.993, 0.14, 0.80 | 0.0190, 0.992, 0.989, 0.04 | 0.96/0.86/0.96 | 0.992 | 0.46/0.47/0.49 | 0.0002, 0.0011, 0.0006 |
| 26 | 0.0218, 0.994, 0.995, 0.03, 0.49 | 0.0226, 0.993, 0.994, 0.51, 0.81 | 0.0195, 0.992, 0.985, 0.01 | 0.97/0.49/0.99 | 0.980 | 0.44/0.43/0.44 | 0.0002, 0.0003, 0.0007 |
| 27 | 0.0197, 0.993, 0.993, 0.14, 0.62 | 0.0256, 0.994, 0.994, 0.22, 0.77 | 0.0192, 0.992, 0.988, 0.17 | 0.86/0.78/0.83 | 0.972 | 0.42/0.41/0.43 | 0.0002, 0.0003, 0.0005 |
| 28 | 0.0195, 0.993, 0.994, 0.02, 0.47 | 0.0248, 0.993, 0.994, 0.22, 0.78 | 0.0187, 0.992, 0.990, 0.04 | 0.98/0.78/0.96 | 0.974 | 0.36/0.38/0.40 | 0.0002, 0.0004, 0.0007 |
| 29 | 0.0192, 0.993, 0.993, 0.08, 0.48 | 0.0287, 0.991, 0.993, 0.25, 0.85 | 0.0203, 0.992, 0.988, 0.52 | 0.92/0.75/0.48 | 0.949 | 0.28/0.31/0.29 | 0.0001, 0.0007, 0.0010 |

The experts column gives the median expert's relative change, the median and worst first share, and the median
expert's kept fraction on the left; the weight column reads the attention output, the down projection and the median
expert.

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home: the two version strings (5.5.0.dev0 to 5.5.0) and
nothing else, as the parent's round 2 report read on the same pin. The template is Google's 12,045-byte file at the
pin (`2dfbfc7d`) byte for byte and the fixed conversation renders identically.

## For the recipe library

Nothing new on the weights: a byte-identical re-upload of TrevorJS's 26B-A4B copy, made with the hub's duplicate
function five days after the parent's weights went up. The pinner should pair a repository whose one commit says
"Duplicate from" with that source before it pairs it with the stated original; the hub's listing gave the parent's
LFS checksums before any download (finding 38). The pull copy keeps the direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/wheat30/measurements/pair-1/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
