# Reading of the Stage 1 and Stage 2 result: Sabomako/gemma-4-31B-it-heretic against google/gemma-4-31B-it (2026-11-02)

Measured on Wheat, round 31 batch 3 piece 3 (download job 387097, compare job 387100, sweep 387102; the pull of
11-02 00:22Z carries the measurements and the sweep record and no job log). Modified revision `fe873a11` (five
commits: the folder uploaded 2026-06-08 at 16:49Z, a README created at 16:54Z and edited twice on 06-28), original
pinned at `35487898` (06-03). The card is 683 bytes: "made using Heretic v1.3.0 with custom ORBA abliteration
method", refusals judged by a language model, KL divergence 0.08095, 2 refusals in 100 against 98. No kernel, no
layer, no component. The first 31B copy measured on Wheat, and the first 31B copy from this maker.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 5 flags (first
shares 0.73 to 0.99 on five matrices), on the cluster and after re-scoring at home. On reading, the copy is a
projection on four consecutive layers at weights the census has not seen on a projection with restored rows.

- 8 of 1,188 tensors changed: the attention output and the down projection of layers 31, 32, 33 and 34 of 60.
  Nothing else moved; the largest relative change outside the changed set is exactly 0, the vision tower, the
  embedding and the 56 other layers included.
- One direction per layer, shared by the two writers (within-layer cosines 0.981 to 0.9999) and nearly across the
  four layers (0.86 to 0.91 with the group medians, 0.64 across the two kinds). First shares 0.959 to 0.993 on
  seven matrices and 0.734 on layer 33's down projection, the smallest edit.
- Output side: the left kept fraction below the right on 8 of 8. The weights read off the left: the attention
  outputs keep -0.36, -2.17, 0.58 and -4.36 on layers 31 to 34 (weights 1.36, 3.17, 0.42 and 5.36), the down
  projections -4.32, -0.32, 0.94 and 0.15 (5.32, 1.32, 0.06 and 0.85). Relative changes 0.0011 to 0.090.
- Rows moved 0.0000 to 0.0004 on all eight: the exact restoration, the band TrevorJS's biprojection leaves
  (finding 3) and Heretic's public row normalisation does not (finding 22). The card does not claim it.

| Layer | Attention output: change, E1, left kept, weight | Down projection: change, E1, left kept, weight | Within-layer cosine | Rows |
| --- | --- | --- | --- | --- |
| 31 | 0.023, 0.987, -0.36, 1.36 | 0.090, 0.990, -4.32, 5.32 | 0.9999 | 0.0002, 0.0003 |
| 32 | 0.054, 0.991, -2.17, 3.17 | 0.022, 0.989, -0.32, 1.32 | 0.998 | 0.0003, 0.0002 |
| 33 | 0.007, 0.959, 0.58, 0.42 | 0.0011, 0.734, 0.94, 0.06 | 0.981 | 0.0001, 0.0000 |
| 34 | 0.087, 0.993, -4.36, 5.36 | 0.014, 0.986, 0.15, 0.85 | 0.9995 | 0.0004, 0.0002 |

The copy's two shards: the first (`b4ef9901`) is its own; the second (`2bdb2df0`, layers 48 to 59 and the vision
tower in the library's two-shard layout of this model) equals the second shard of callmegrr's and llmfan46's 31B
exports, since none of the three touched a tensor in it. That is the layout, not a re-upload: the first shards
differ and no measured field equals either copy's.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster (one field) and "consistent with re-save noted" at home:
`text_config.moe_intermediate_size` closes by the default rule, and the two version strings (5.9.0 against
5.5.0.dev0) are all that differ. The template is the pin's 17,466-byte file and the fixed conversation renders
identically.

## For the recipe library

The per-layer entry reads the window and the direction and flags five first shares on edits of 5.3 and 5.4 times
the original's action, where the restoration leaves a second direction. A weight of 5.4 on a restored projection is
the largest in the census on a direction-per-layer edit (finding 65); the arbitrary-rank solvers go higher (finding
22, finding 68) without restoring rows. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat31/measurements/pair-3/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
