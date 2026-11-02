# Reading of the Stage 1 and Stage 2 result: NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals5 against google/gemma-4-E4B-it (2026-11-02)

Measured on Blueback, round 29 piece 5. The pull carries the measurements and the sweep record and no job log.
Modified revision `3d74685f` (the last commit, 2026-04-29; the repository was created on 04-04), original pinned
at `292a7e27` (04-02). The card names Heretic 1.2.0 with the arbitrary-rank ablation branch (pull request 211,
commit `3b70fe5`, the L-BFGS solver) and prints the trial: start layer 19, end layer 42, preservation weight
0.7662, steering weight 0.0007, overcorrection weight 0.9544, 15 neighbours, 5 refusals in 100, KL divergence
0.0256. The `base_model` field names the original.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 51 flags (29 first
shares 0.86 to 0.98, 22 within-layer cosines), on the cluster and after re-scoring at home. On reading, the copy
is the card's solver inside the card's window with the solver's own fingerprint.

- 29 of 2,130 tensors changed: the attention outputs of layers 19 to 36 less 26 (17) and the down projections of
  21, 23, 24 and 26 to 34 (12), all inside the card's 19 to 42. Seven more down projections in the window (layers
  19, 20, 22, 25, 26, 35, 36) were rewritten under the change threshold, at 0.00006 to 0.00025, which is why the
  largest change outside the changed set is 0.000251 and not 0: the solver touched them and moved almost
  nothing. Everything else, the 54 shared-KV tensors dropped by the export among it, equals the original.
- Nearly one direction per matrix: first share 0.86 to 0.98, fourth cumulative share 0.95 to 0.99, relative
  change 0.022 to 0.065. The low-rank solution the branch describes.
- No shared direction: within a layer 0.003 to 0.15 on the 12 layers with two writers, 0.11 to 0.37 against the
  group medians.
- The input side, over-reflected: along the leading input direction the copy keeps -0.24 to -1.50 (past a
  reflection on 7 of 29), along the leading output direction 0.01 to 0.93; the left above the right on 29 of 29.
- Rows moved 0.001 to 0.037 (0.037 on layer 29's attention output); the card claims no preservation.

| Layer | Attention output: change, E1, E4, left kept, right kept | Down projection: change, E1, E4, left kept, right kept | Within-layer cosine |
| --- | --- | --- | --- |
| 19 | 0.040, 0.95, 0.97, 0.75, -0.74 | under threshold (0.00008) | |
| 21 | 0.034, 0.94, 0.96, 0.78, -0.64 | 0.035, 0.86, 0.96, 0.76, -0.89 | 0.017 |
| 24 | 0.059, 0.98, 0.98, 0.01, -1.10 | 0.027, 0.97, 0.98, 0.71, -1.08 | 0.141 |
| 29 | 0.053, 0.97, 0.98, 0.92, -1.50 | 0.025, 0.97, 0.98, 0.67, -0.75 | 0.045 |
| 32 | 0.046, 0.97, 0.98, 0.70, -1.46 | 0.023, 0.97, 0.98, 0.73, -0.71 | 0.054 |
| 34 | 0.061, 0.95, 0.97, 0.80, -0.79 | 0.022, 0.96, 0.97, 0.83, -0.64 | 0.011 |
| 36 | 0.053, 0.97, 0.98, 0.64, -0.99 | under threshold (0.00006) | |

The full table (29 rows) is in the report. The fingerprint shares no measured field with the other reports on
this original's weight file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster; "consistent with re-save noted" at home. Under transformers 5.22.1
`text_config.moe_intermediate_size` (null in the save) closes by the default rule, and the template is Google's
16,804-byte file of the 04-28 revision (`c53e9d33`) under a pin of 04-02: the later-revision template, which the
copy's last commit of 04-29 picked up the day after Google published it. The fixed conversation renders
identically under both.

## For the recipe library

The second arbitrary-rank copy on this original after llmfan46's (round 2), and the two solvers leave different
marks: llmfan46's (the same branch, attention outputs only) left 11 matrices at first shares of 0.92 to 0.96 and
rows at 0.0016 to 0.0165; this one leaves 29 at 0.86 to 0.98 plus seven rewritten under the threshold. An
arbitrary-rank entry would read the window, the fourth cumulative share and the under-threshold rewrites, and
count none of the 51 flags. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/blueback29/measurements/pair-5/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
