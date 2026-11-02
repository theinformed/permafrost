# Reading of the Stage 1 and Stage 2 result: Bahushruth/gemma-4-31B-it-abliterated against google/gemma-4-31B-it (2026-11-02)

Measured on Blueback, round 26 piece 1. The pull carries the measurements and the sweep record and no job log.
Modified revision `46f66413` (one commit, a squash of 2026-07-31 at 09:17Z; the repository was created on 07-29 at
19:31Z), original pinned at `842da379` (07-20), the revision current when the repository was created. The card
describes the maker's own arbitrary-rank ablation: a local optimisation at each steerable matrix (the attention
output projection and the feed-forward down projection, "all 60 layers") solved by L-BFGS with a strong-Wolfe line
search, a loss that preserves harmless outputs while pulling harmful outputs toward harmless ones and away from the
original, row norms "preserved exactly by reparameterization (grimjim method)", an Optuna search of 60 trials, the
maker's own harmful set of 7,356 prompts; it reports 4.0 percent refusals against 96 for the original and a KL
divergence of 0.283, and says direction abliteration stopped at 18 percent on this model. The `base_model` field
names the original.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 132 flags, on the
cluster and after re-scoring at home. On reading, the copy is the card's method on a window the card does not give,
with the card's preservation claim holding to a tenth of a percent.

- 66 of 1,188 tensors changed: the attention output and the down projection of layers 17 to 49, 33 of the 60 layers
  the card names. Nothing else moved; the largest relative change outside the changed set is exactly 0 and 1,122
  tensors equal the original. Layers 0 to 16 and 50 to 59 are untouched.
- Many directions per matrix. The first share is 0.34 to 0.79 and the eighth cumulative share 0.70 to 0.93, so
  the leading direction carries half the change and seven more carry a further 0.14 to 0.37; the relative change is
  0.032 to 0.120, two to five times a shared projection's. A solved matrix, not a projection.
- No shared direction. The two writers of a layer agree at 0.002 to 0.13, and across layers each kind agrees with
  its median at 0.02 to 0.45.
- The input side, over-reflected: along each matrix's leading input direction the copy keeps -0.84 to -2.46 of the
  original's action (past a reflection on 65 of 66), and along the leading output direction 0.36 to 0.99; the left
  above the right on 66 of 66.
- Rows moved by at most 0.00073: the reparameterization preserves them, as the card says, where every Heretic
  copy that claims the step leaves 0.005 to 0.008 (finding 22).

| Layer | Attention output: change, E1, E8, left kept, right kept | Down projection: change, E1, E8, left kept, right kept | Within-layer cosine | Row norms |
| --- | --- | --- | --- | --- |
| 17 | 0.060, 0.48, 0.81, 0.76, -1.91 | 0.044, 0.59, 0.83, 0.98, -2.46 | 0.043 | 0.0002, 0.0004 |
| 20 | 0.120, 0.45, 0.81, 0.87, -2.13 | 0.039, 0.57, 0.86, 0.97, -2.15 | 0.023 | 0.0005, 0.0002 |
| 25 | 0.052, 0.37, 0.75, 0.62, -1.52 | 0.036, 0.43, 0.74, 0.89, -1.43 | 0.024 | 0.0002, 0.0002 |
| 33 | 0.045, 0.41, 0.74, 0.66, -1.07 | 0.038, 0.50, 0.75, 0.89, -1.43 | 0.014 | 0.0002, 0.0002 |
| 41 | 0.045, 0.61, 0.84, 0.97, -1.96 | 0.036, 0.47, 0.74, 0.65, -1.75 | 0.016 | 0.0001, 0.0001 |
| 44 | 0.071, 0.79, 0.93, 0.94, -1.35 | 0.032, 0.38, 0.71, 0.85, -1.44 | 0.010 | 0.0003, 0.0001 |
| 49 | 0.065, 0.56, 0.85, 0.60, -2.05 | 0.034, 0.40, 0.70, 0.95, -1.32 | 0.020 | 0.0003, 0.0001 |

The full table (66 rows) is in the report. The fingerprint shares no measured field with the thirteen earlier
reports on this original's weight file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster; "consistent with re-save noted" at home. Under transformers 5.22.1
`text_config.moe_intermediate_size` (null in a 5.14.1 save against a 5.5.0.dev0 original) closes by the default
rule, and what remains is the version strings. The template is Google's 18,683-byte Canonical file and the fixed
conversation renders identically.

## For the recipe library

No entry fits a solved edit: the per-layer entry flags every matrix's first share and every layer's cosine, and
both are the method's nature rather than a departure from it. An entry for a solved or arbitrary-rank edit would
read the spectrum beyond the eighth direction, the side, the row bound and the window, and count none here. Two
readings the card does not carry: the window is layers 17 to 49, not all 60, and the kept fractions on the input
side run past a reflection. The pull copy keeps the direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/blueback26/measurements/pair-1/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
