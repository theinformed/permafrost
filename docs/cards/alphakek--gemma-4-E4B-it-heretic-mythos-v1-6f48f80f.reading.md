# Reading of the Stage 1 and Stage 2 result: alphakek/gemma-4-E4B-it-heretic-mythos-v1 against google/gemma-4-E4B-it (2026-11-02)

Measured on Blueback, round 29 piece 6. The pull carries the measurements and the sweep record and no job log.
Modified revision `c3282d51` (2026-04-08, pushed by the account vvsotnikov), original pinned at `292a7e27`
(04-02). The card names "a private fork of Heretic" with a scoring set the maker calls Mythos, reports a KL
divergence of 0.04 and a Mythos score of 93 percent, and prints no kernel, no layer range and no component. The
`base_model` field names the original.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 68 flags (34 first
shares 0.006 to 0.96, 34 within-layer cosines), on the cluster and after re-scoring at home. On reading, the copy
is a per-matrix directional edit on both writers of 17 layers, with two matrices left as residues.

- 34 of 2,130 tensors changed: the attention output and the down projection of layers 11 to 27. Nothing else
  moved; the largest relative change outside the changed set is exactly 0 and 2,096 tensors equal the original.
- A direction per matrix on 32 of 34: first share 0.51 to 0.97 at relative changes of 0.013 to 0.062. Two down
  projections, layers 16 and 20, changed by 0.0014 and 0.0017 with first shares of 0.030 and 0.006 and kept
  fractions of 0.98 to 1.00 on both sides: a residue with no direction, as if the matrix had been edited and
  nearly restored, or rewritten in a different precision.
- No shared direction: within a layer 0.012 to 0.14, 0.03 to 0.34 against the group medians.
- The input side: along the leading input direction the attention outputs keep -0.04 to -1.04 and the down
  projections -0.77 to 0.01 (the two residues at 0.98 and 1.00); along the leading output direction 0.30 to 0.87;
  the left above the right on 32 of 32 edited matrices.
- Rows moved 0.0057 to 0.0078 on the 32, the band finding 22 reads on every Heretic copy that claims the
  preservation step, under a card that claims nothing; the two residues sit at 0.0007 and 0.0008.

| Layer | Attention output: change, E1, left kept, right kept | Down projection: change, E1, left kept, right kept | Within-layer cosine | Row norms |
| --- | --- | --- | --- | --- |
| 11 | 0.029, 0.95, 0.56, -0.29 | 0.013, 0.95, 0.80, 0.01 | 0.131 | 0.0068, 0.0077 |
| 13 | 0.062, 0.76, 0.68, -0.65 | 0.038, 0.79, 0.74, -0.77 | 0.037 | 0.0071, 0.0076 |
| 15 | 0.041, 0.86, 0.85, -1.04 | 0.033, 0.72, 0.75, -0.65 | 0.012 | 0.0075, 0.0075 |
| 16 | 0.045, 0.92, 0.80, -0.65 | 0.0014, 0.03, 1.00, 0.98 | 0.128 | 0.0075, 0.0007 |
| 20 | 0.021, 0.97, 0.87, -0.04 | 0.0017, 0.006, 1.00, 1.00 | 0.020 | 0.0075, 0.0008 |
| 24 | 0.045, 0.91, 0.30, -0.56 | 0.020, 0.96, 0.79, -0.45 | 0.142 | 0.0075, 0.0077 |
| 27 | 0.032, 0.92, 0.81, -0.53 | 0.020, 0.92, 0.78, -0.53 | 0.026 | 0.0074, 0.0068 |

The full table (34 rows) is in the report. The fingerprint shares no measured field with the other reports on
this original's weight file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster; "consistent with re-save noted" at home. Under transformers 5.22.1
`text_config.moe_intermediate_size` (null in the save) closes by the default rule, and what remains is the version
strings. The template is Google's 11,926-byte file of the pin and the fixed conversation renders identically.

## For the recipe library

A directional edit whose fork the card does not describe: layers 11 to 27, both writers, input side, one
direction per matrix rather than per layer, row norms in Heretic's band. The two residues (layers 16 and 20) are
the mark to look for if the fork publishes: nothing in the public Heretic leaves a matrix changed by a tenth of a
percent with no direction. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/blueback29/measurements/pair-6/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
