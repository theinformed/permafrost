# Reading of the Stage 1 and Stage 2 result: Bahushruth/gemma-4-E4B-it-abliterated against google/gemma-4-E4B-it (2026-11-02)

Measured on Blueback, round 26 piece 3. The pull carries the measurements and the sweep record and no job log.
Modified revision `7b714417` (one commit, a squash of 2026-07-31 at 09:17Z, the same minute as the maker's 31B
copy; the repository was created on 07-26 at 18:57Z), original pinned at `ee0ef602` (07-20). The card is the
31B card's twin: the maker's arbitrary-rank ablation by L-BFGS on the attention output and down projection of
"all 42 layers", rows preserved by reparameterization, 60 Optuna trials, 2.7 percent refusals against 98 for the
original and a KL divergence of 0.116; it says direction abliteration stopped near 30 percent on this model
because of its per-layer embeddings and shared keys and values. The `base_model` field names the original.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 48 flags, on the
cluster and after re-scoring at home. On reading, the copy is the 31B's method on 12 of the card's 42 layers.

- 24 of 2,076 tensors changed: the attention output and the down projection of layers 21 to 32. Nothing else
  moved; the largest relative change outside the changed set is exactly 0 and 2,052 tensors equal the original.
  The 54 shared-KV tensors are dropped by the export (finding 14) and mapped without a flag.
- Many directions per matrix: first share 0.19 to 0.45, eighth cumulative share 0.61 to 0.79, relative change
  0.043 to 0.103.
- No shared direction: within a layer 0.004 to 0.14, across layers 0.13 to 0.48 against the median.
- The input side: along the leading input direction the copy keeps -0.19 to -1.18 (past a reflection on 2 of 24),
  along the leading output direction 0.61 to 0.94; the left above the right on 24 of 24.
- Rows moved by at most 0.00047: preserved, as the card says.

| Layer | Attention output: change, E1, E8, left kept, right kept | Down projection: change, E1, E8, left kept, right kept | Within-layer cosine | Row norms |
| --- | --- | --- | --- | --- |
| 21 | 0.069, 0.19, 0.73, 0.89, -0.37 | 0.048, 0.33, 0.68, 0.77, -0.92 | 0.011 | 0.0005, 0.0003 |
| 24 | 0.098, 0.27, 0.67, 0.64, -0.65 | 0.046, 0.26, 0.64, 0.81, -0.99 | 0.028 | 0.0003, 0.0002 |
| 27 | 0.075, 0.30, 0.71, 0.87, -1.18 | 0.044, 0.24, 0.63, 0.76, -0.92 | 0.018 | 0.0004, 0.0001 |
| 29 | 0.070, 0.45, 0.79, 0.90, -0.89 | 0.047, 0.28, 0.67, 0.65, -0.64 | 0.061 | 0.0002, 0.0002 |
| 32 | 0.077, 0.22, 0.65, 0.79, -1.01 | 0.043, 0.24, 0.62, 0.74, -0.67 | 0.045 | 0.0003, 0.0001 |

The full table (24 rows) is in the report. The fingerprint shares no measured field with the nineteen other
reports on this original's weight file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster; "consistent with re-save noted" at home. Under transformers 5.22.1
`text_config.moe_intermediate_size` (null in a 5.14.1 save) closes by the default rule, and what remains is the
version strings. The template is Google's 18,569-byte Canonical file and the fixed conversation renders identically.

## For the recipe library

As the 31B copy: a solved edit that no entry reads, with the window (12 of 42 layers) and the row bound (0.0005) as
the two numbers a card would need to carry. The pull copy keeps the direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/blueback26/measurements/pair-3/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
