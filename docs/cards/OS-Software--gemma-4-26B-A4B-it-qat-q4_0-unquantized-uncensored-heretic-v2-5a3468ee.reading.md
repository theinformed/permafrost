# Reading of the Stage 1 and Stage 2 result: OS-Software/gemma-4-26B-A4B-it-qat-q4_0-unquantized-uncensored-heretic-v2 against google/gemma-4-26B-A4B-it-qat-q4_0-unquantized (2026-11-01)

Measured on Nautilus, round 32 piece 8 (download job 4145233, compare job 4145241, 1,350 seconds, sweep 4145242).
Modified revision `06f527f9` (five commits on 2026-09-07 between 23:28Z and 23:33Z: the weights, the tokenizer,
the processor and the README), original pinned at `f1e06dc5`, the revision current when the repository was
created, the QAT-unquantized 26B-A4B checkpoint that piece 5 also stands on. The card prints the Heretic
2.0.0.dev0 record with a custom build: start layer 12, end layer 20, transport rank 4, adapter rank 128, row
normalisation "none", a KL divergence of 0.0101 and 0 refusals in 100 against the original. The `base_model`
field names the plain instruct model; the README's first sentence names the QAT checkpoint, and the pinner
followed the README. The maker's E4B copy, measured in round 30 (finding 42), carries the same record on the
instruct E4B.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 32 flags, on the
cluster and after re-scoring at home: 16 first shares of 0.75 to 0.96 and 16 within-layer cosines of 0.002 to
0.12. On reading, the copy is the maker's rank-four transport edit on a second base: the card's window on both
writers, exactly four directions per matrix, input side, unrelated directions per matrix, rows unrestored.

- 16 of 1,013 tensors changed: the attention outputs and the shared dense down projections of layers 12 to 19,
  the card's window with its exclusive end. The experts, the routers, the other projections and the vision
  tower are unchanged; the largest relative change outside the changed set is exactly 0 and 997 tensors equal
  the original. Measured against the QAT original, nothing of the QAT retraining shows.
- Rank four exactly: the first share is 0.75 to 0.96, the second cumulative share 0.94 to 0.997, the fourth
  0.998 to 0.9995, and the fifth singular value is 0.0015 to 0.004 of the first, a hard cut where the E4B copy's
  was the same (finding 42).
- Input side on all 16: the left kept fraction is 0.70 to 0.97 on the attention outputs and 0.55 to 0.93 on the
  down projections, the right 0.32 to -1.45 and -0.30 to -0.97; the left is above the right on 16 of 16. The
  weights along the leading right direction are 0.68 to 2.45 on the attention outputs (2.45 at layer 17, 2.31 at
  18) and 1.30 to 1.97 on the down projections (1.97 at 18); with four directions per matrix the leading one
  carries 75 to 96 percent of the change, so these are lower bounds on the edit's reach along its subspace.
- The directions agree with the group reference at 0.23 to 0.53 and within a layer at 0.002 to 0.12: per
  matrix, unrelated between the two writers.
- Rows moved by 0.011 to 0.047, unrestored, under the card's "none".
- Relative changes of 0.037 to 0.058 on the attention outputs and 0.054 to 0.076 on the down projections, the
  largest absolute difference 0.22 on the down projection of layer 14.

| Layer | Attention output: change, E1, E2, E4, left kept, right kept | Down projection: change, E1, E2, E4, left kept, right kept | Weight read | Within-layer cosine | Cross-layer cosine | Row norms |
| --- | --- | --- | --- | --- | --- | --- |
| 12 | 0.0372, 0.957, 0.997, 0.998, 0.91, 0.32 | 0.0719, 0.941, 0.995, 0.9995, 0.93, -0.40 | 0.68/1.40 | 0.088 | 0.35/0.32 | 0.0146, 0.0475 |
| 13 | 0.0419, 0.915, 0.997, 0.9985, 0.91, -0.22 | 0.0543, 0.870, 0.991, 0.9991, 0.65, -0.30 | 1.22/1.30 | 0.097 | 0.41/0.37 | 0.0114, 0.0138 |
| 14 | 0.0423, 0.912, 0.994, 0.9985, 0.85, -0.36 | 0.0683, 0.839, 0.994, 0.9994, 0.80, -0.47 | 1.36/1.47 | 0.117 | 0.48/0.43 | 0.0112, 0.0325 |
| 15 | 0.0493, 0.886, 0.986, 0.9989, 0.79, -0.62 | 0.0603, 0.766, 0.971, 0.9992, 0.76, -0.59 | 1.62/1.59 | 0.066 | 0.42/0.33 | 0.0161, 0.0120 |
| 16 | 0.0468, 0.805, 0.987, 0.9988, 0.70, -0.35 | 0.0692, 0.857, 0.986, 0.9994, 0.55, -0.72 | 1.35/1.72 | 0.060 | 0.53/0.29 | 0.0120, 0.0230 |
| 17 | 0.0381, 0.918, 0.987, 0.9982, 0.97, -1.45 | 0.0675, 0.748, 0.970, 0.9994, 0.61, -0.52 | 2.45/1.52 | 0.002 | 0.27/0.31 | 0.0165, 0.0153 |
| 18 | 0.0584, 0.947, 0.980, 0.9992, 0.91, -1.31 | 0.0756, 0.809, 0.973, 0.9995, 0.87, -0.97 | 2.31/1.97 | 0.020 | 0.23/0.28 | 0.0299, 0.0231 |
| 19 | 0.0441, 0.785, 0.937, 0.9987, 0.93, -0.56 | 0.0656, 0.756, 0.950, 0.9994, 0.75, -0.59 | 1.56/1.59 | 0.014 | 0.47/0.28 | 0.0150, 0.0224 |

The weight column reads one minus the right kept fraction along the leading direction on both writers.

The fingerprint shares nothing with mewse's copy on the same original (piece 5) nor with the maker's E4B copy,
which has the same shape (20 matrices, layers 18 to 27, rank four, input side, rows 0.098) on another base.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, three fields, the 5.16 save form (finding 39):
`global_head_dim` 512 and `num_global_key_value_heads` 2 leave the text configuration and return as a
`per_layer_config` map under the five global layers' indices, written by a 5.16.1 save against the QAT original's
5.6.2 file. The sixth copy on this form; closed by hand. The template differs from Google's 18,683-byte file in
line endings alone (19,073 bytes) and the tool closed it; the version strings close as a re-save, and the fixed
conversation renders identically.

## For the recipe library

The second rank-four transport edit, the same maker and the same custom build as finding 42's, now on a QAT
original: the `transport-rank-k` entry round 30 described (a first-k share with k read from the singular values,
input side, no within-layer constraint) would fit this copy with no flags, as it would the E4B one. The
`base_model` field is wrong by one checkpoint, as on mewse's copy (finding 48). The pull copy keeps the direction
vectors at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus32/measurements/pair-8/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
