# Reading of the Stage 1 and Stage 2 result: coder3101/gemma-4-E2B-it-qat-q4_0-unquantized-heretic against google/gemma-4-E2B-it-qat-q4_0-unquantized (2026-11-01)

Measured on Nautilus, round 32 piece 6 (download job 4145233, compare job 4145239, 363 seconds, sweep 4145242).
Modified revision `81440958` (six commits on 2026-06-06 between 17:39Z and 17:42Z: the weights, the tokenizer,
the README and a preprocessor configuration), original pinned at `d40c88a0`, the revision current when the
repository was created. The original is the checkpoint Google extracted from quantisation-aware training of the
E2B instruct model, published in bfloat16; this is its first measurement. The card prints the Heretic record with
Arbitrary-Rank Ablation: start layer 6, end layer 24, a KL divergence of 0.0056 and 7 refusals in 100 against
the original. The `base_model` field names the QAT checkpoint.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 17 flags, on the
cluster and after re-scoring at home: first shares of 0.012 to 0.021 on eight matrices and 0.938 to 0.966 on nine.
On reading, the copy is the maker's shape on a fifth base: the card's window on the attention outputs alone,
nine of them edited on the input side and eight rewritten at the storage floor, rows within 0.008.

- 17 of 1,951 tensors changed, all attention outputs, layers 7 to 23 of the card's 6-to-24 window. No down
  projection, no other projection, no norm, no embedding and no vision or audio tensor moved; the largest
  relative change outside the changed set is 0.000767, on the attention output of layer 6, the window's first
  layer, which the search weighted to nothing and the threshold leaves as unchanged; 1,934 tensors equal the
  original.
- Nine are edits: layers 9, 12, 15 to 21, relative changes of 0.032 to 0.076, first share 0.938 to 0.966 with
  the fourth cumulative share 0.95 to 0.98 (a leading direction and a short tail). Input side on all nine: the
  left kept fraction is 0.30 to 0.87, the right -0.75 to -2.12, the left above the right on 9 of 9. The weights
  along the right direction are 1.75 to 3.12 (3.12 at layer 19, 2.39 at 16).
- Eight are at the floor: layers 7, 8, 10, 11, 13, 14, 22 and 23 moved by 0.0010 to 0.0014 of their norm with
  first shares of 0.012 to 0.021, kept fractions of 1.00 on both sides and the largest absolute difference 0.0005
  to 0.0010, one bfloat16 step: matrices the search rewrote at a weight near zero (finding 22's residues).
- The directions of the nine edits agree with the group reference at 0.10 to 0.34: unrelated per matrix. There is
  one writer per layer, so no within-layer cosine.
- Rows moved by 0.0073 to 0.0079 on the nine edits, the band the maker's four instruct copies read under the
  row-norm preservation step (0.0057 to 0.0080, finding 22), and by 0.0005 to 0.0052 on the eight floor
  matrices.

| Layer | Attention output: change, E1, E4, left kept, right kept | Weight read | Cross-layer cosine | Row norms |
| --- | --- | --- | --- | --- |
| 7 | 0.0010, 0.016, 0.043, 1.00, 1.00 | 0.00 | 0.03 | 0.0008 |
| 8 | 0.0010, 0.020, 0.069, 1.00, 1.00 | 0.00 | 0.09 | 0.0005 |
| 9 | 0.0363, 0.938, 0.953, 0.87, -1.18 | 2.18 | 0.10 | 0.0074 |
| 10 | 0.0011, 0.017, 0.062, 1.00, 1.00 | 0.00 | 0.05 | 0.0007 |
| 11 | 0.0012, 0.018, 0.064, 1.00, 1.00 | 0.00 | 0.05 | 0.0008 |
| 12 | 0.0425, 0.958, 0.970, 0.65, -1.08 | 2.08 | 0.20 | 0.0077 |
| 13 | 0.0014, 0.018, 0.065, 1.00, 1.00 | 0.00 | 0.06 | 0.0008 |
| 14 | 0.0013, 0.014, 0.034, 1.00, 1.00 | 0.00 | 0.25 | 0.0052 |
| 15 | 0.0395, 0.966, 0.972, 0.43, -0.85 | 1.85 | 0.20 | 0.0075 |
| 16 | 0.0755, 0.965, 0.979, 0.30, -1.39 | 2.39 | 0.34 | 0.0073 |
| 17 | 0.0641, 0.957, 0.967, 0.45, -1.10 | 2.10 | 0.25 | 0.0079 |
| 18 | 0.0376, 0.948, 0.958, 0.65, -0.97 | 1.97 | 0.21 | 0.0075 |
| 19 | 0.0540, 0.951, 0.961, 0.80, -2.12 | 3.12 | 0.32 | 0.0076 |
| 20 | 0.0317, 0.943, 0.953, 0.75, -0.75 | 1.75 | 0.23 | 0.0075 |
| 21 | 0.0417, 0.948, 0.957, 0.74, -1.16 | 2.16 | 0.17 | 0.0076 |
| 22 | 0.0012, 0.021, 0.058, 1.00, 1.00 | 0.00 | 0.00 | 0.0006 |
| 23 | 0.0013, 0.012, 0.040, 1.00, 1.00 | 0.00 | 0.18 | 0.0045 |

The weight column reads one minus the right kept fraction; it is 0.00 on the floor matrices by construction.

The fingerprint stands alone on this original. Against the maker's four instruct copies (E4B, 12B, 26B-A4B,
31B: attention outputs only, the declared window, residues inside it, rows in the 0.006 to 0.008 band), this
one is the same hand on a QAT checkpoint.

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home: the two version strings (5.6.2 to 5.10.2) and
nothing else. The template is Google's pinned file and the fixed conversation renders identically.

## For the recipe library

The maker's one-writer arbitrary-rank shape, the fifth base and the first QAT one, with the residue set inside
the window and one residue under the threshold at the window's first layer. An entry for it would read the
floor matrices as finding 40's were read, set aside before the first-share test, and the nine edits would then
fit the `arbitrary-rank` candidate line. The pull copy keeps the direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus32/measurements/pair-6/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
