# Reading of the Stage 1 and Stage 2 result: mewse/gemma-4-26B-A4B-it-qat-q4_0-unquantized-heretic-ara against google/gemma-4-26B-A4B-it-qat-q4_0-unquantized (2026-11-01)

Measured on Nautilus, round 32 piece 5 (download job 4145233, compare job 4145238, 1,369 seconds, sweep 4145242).
Modified revision `5bb23dbe` (twenty commits from 2026-08-19 08:23Z to 09-13 20:17Z: a first upload at 08:23Z,
the merged bfloat16 weights at 14:40Z as "add full merged bf16 weights (ARA trial #60, alpha/r=1.0)", the
adapter-only files removed at 16:57Z, four pairs of "rate test" commits added and removed the same minute, a
refusal table added to the README twice, and a GGUF added on 08-19 at 19:18Z and deleted on 09-13), original
pinned at `f1e06dc5`, the revision current when the repository was created. The original is the checkpoint Google
extracted from quantisation-aware training of the 26B-A4B instruct model, published in bfloat16; this round's
pieces 5 and 8 are its first two measurements. The card prints the Heretic 1.2.0 record with Arbitrary-Rank
Ablation: start layer 11, end layer 23, trial 60, a KL divergence of 0.1226 and 5 refusals in 100 against the
original. The `base_model` field names the plain instruct model; the README's first sentence names the QAT
checkpoint, and the pinner followed the README.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 25 flags, on the
cluster and after re-scoring at home: 24 within-layer cosines of 0.009 to 0.13 on all twelve layers, counted on
both writers, and one first share of 0.932 on the down projection of layer 20. On reading, the footprint is the
card's window on both writers, and the edits are rank one on the input side along unrelated directions at
searched weights of 1.23 to 4.35.

- 24 of 1,013 tensors changed: the attention outputs and the shared dense down projections of layers 11 to 22,
  the card's window with its exclusive end. The experts, the routers, the other projections and the vision
  tower are unchanged; the largest relative change outside the changed set is exactly 0 and 989 tensors equal
  the original. Measured against the QAT original, nothing of the QAT retraining shows, which is where the copy
  was made.
- Rank one on 22 of 24 (first share 0.991 to 0.999); the down projections of layers 20 and 21 carry a second
  direction (first share 0.932 and 0.991, second cumulative share 0.998 and 0.997).
- Input side on all 24: the left kept fraction is 0.41 to 0.95 on the attention outputs and 0.11 to 0.96 on the
  down projections, the right -0.56 to -3.35 and -0.23 to -1.33; the left is above the right on 24 of 24. The
  weights along the right direction are 1.56 to 4.35 on the attention outputs (4.35 at layer 20, the next 2.45
  at 14) and 1.23 to 2.33 on the down projections (2.33 at 12), inside the 0.51 to 10.18 that finding 22 reads
  across the arbitrary-rank copies, with a median of 1.9.
- The directions agree with the group reference at 0.17 to 0.51 and within a layer at 0.009 to 0.13: unrelated
  per matrix.
- Rows moved by 0.007 to 0.25 (0.245 on the attention output of layer 20, 0.145 and 0.111 on the down
  projections of 11 and 12), unrestored; the card makes no preservation claim.
- Relative changes of 0.033 to 0.113 on the attention outputs and 0.051 to 0.118 on the down projections, the
  largest absolute difference 0.43 on the attention output of layer 20.

| Layer | Attention output: change, E1, E2, left kept, right kept | Down projection: change, E1, E2, left kept, right kept | Weight read | Within-layer cosine | Cross-layer cosine | Row norms |
| --- | --- | --- | --- | --- | --- | --- |
| 11 | 0.0327, 0.998, 0.998, 0.84, -1.38 | 0.1180, 0.999, 1.000, 0.96, -0.58 | 2.38/1.58 | 0.012 | 0.31/0.17 | 0.0072, 0.1452 |
| 12 | 0.0430, 0.998, 0.999, 0.74, -0.88 | 0.0913, 0.999, 1.000, 0.91, -1.33 | 1.88/2.33 | 0.043 | 0.39/0.26 | 0.0101, 0.1110 |
| 13 | 0.0508, 0.999, 0.999, 0.76, -0.91 | 0.0626, 0.999, 0.999, 0.62, -1.30 | 1.91/2.30 | 0.129 | 0.35/0.19 | 0.0127, 0.0235 |
| 14 | 0.0516, 0.999, 0.999, 0.68, -1.45 | 0.0663, 0.998, 0.999, 0.22, -1.27 | 2.45/2.27 | 0.075 | 0.43/0.25 | 0.0215, 0.0230 |
| 15 | 0.0466, 0.998, 0.999, 0.84, -0.79 | 0.0930, 0.999, 1.000, 0.89, -0.23 | 1.79/1.23 | 0.040 | 0.38/0.25 | 0.0128, 0.1040 |
| 16 | 0.0476, 0.999, 0.999, 0.56, -0.86 | 0.0743, 0.998, 1.000, 0.89, -0.66 | 1.86/1.66 | 0.013 | 0.51/0.26 | 0.0258, 0.0588 |
| 17 | 0.0391, 0.998, 0.998, 0.95, -1.40 | 0.0680, 0.999, 0.999, 0.59, -1.08 | 2.40/2.08 | 0.049 | 0.25/0.21 | 0.0103, 0.0257 |
| 18 | 0.0514, 0.999, 0.999, 0.49, -0.56 | 0.0639, 0.999, 0.999, 0.85, -1.06 | 1.56/2.06 | 0.022 | 0.29/0.25 | 0.0180, 0.0178 |
| 19 | 0.0484, 0.999, 0.999, 0.64, -0.69 | 0.0511, 0.999, 0.999, 0.58, -0.82 | 1.69/1.82 | 0.021 | 0.50/0.29 | 0.0216, 0.0126 |
| 20 | 0.1131, 0.997, 0.999, 0.86, -3.35 | 0.0679, 0.932, 0.998, 0.35, -0.73 | 4.35/1.73 | 0.009 | 0.21/0.29 | 0.2454, 0.0275 |
| 21 | 0.0436, 0.998, 0.999, 0.43, -1.27 | 0.0597, 0.991, 0.997, 0.11, -1.04 | 2.27/2.04 | 0.025 | 0.34/0.26 | 0.0130, 0.0732 |
| 22 | 0.0595, 0.999, 0.999, 0.41, -1.33 | 0.0587, 0.997, 0.999, 0.66, -0.38 | 2.33/1.38 | 0.034 | 0.32/0.25 | 0.0180, 0.0257 |

The weight column reads one minus the right kept fraction on both writers.

The fingerprint shares nothing with OS-Software's copy on the same original (piece 8), nor with the thirteen
reports on the instruct 26B-A4B.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, three fields, the 5.16 save form (finding 39):
`global_head_dim` 512 and `num_global_key_value_heads` 2 leave the text configuration and return as a
`per_layer_config` map under the five global layers' indices, written by a 5.15.0 save against the QAT original's
5.6.2 file. The fifth copy on this form; closed by hand. The version strings close as a re-save, the template is
Google's pinned file and the fixed conversation renders identically.

## For the recipe library

The arbitrary-rank shape of finding 22 on a QAT original: the window to the layer on both writers, rank one per
matrix along unrelated directions, input side, searched weights of 1.23 to 4.35, rows unrestored. The
`arbitrary-rank` candidate entry fits it without a flag if the within-layer cosine line is dropped for that
entry. The `base_model` field is wrong by one checkpoint, and a pinner that trusted it would have measured this
copy against the instruct model and read the QAT retraining on top of the edit (finding 48). The pull copy keeps
the direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus32/measurements/pair-5/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
