# Reading of the Stage 1 and Stage 2 result: MoonRide/gemma-4-31B-it-heretic-ara against google/gemma-4-31B-it (2026-11-02)

Measured on Wheat, round 37 piece 5 (download job 387161, compare job 387166, sweep 387170; the pull carries the
measurements and the sweep record and no job log). Modified revision `cf80d7e7` (five commits on 2026-04-12
between 10:22Z and 13:35Z), original pinned at `439edf56`. The card (the tool's, with the maker's note on top)
says Heretic v1.2.0's arbitrary-rank ablation "with row-norm preservation": `start_layer_index` 30,
`end_layer_index` 54, `preserve_good_behavior_weight` 0.1997, `steer_bad_behavior_weight` 0.0002,
`overcorrect_relative_weight` 1.0020, `neighbor_count` 11, KL divergence 0.0508, 11 refusals in 100. This is the
maker's first 31B copy, made four weeks before the "custom" copy of 05-07 that round 19 read (finding 42's
neighbour); the `base_model` field names the instruct model.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 84 flags (44 first
shares, 40 within-layer cosines), on the cluster and after re-scoring at home. On reading, the copy is the card's
window with a selection inside it, the rows held within finding 22's band, and a trace left on the matrices the
selection skipped.

- 44 of 1,188 tensors changed above the 0.001 line: the attention outputs of layers 30 to 53 (all 24, the card's
  start 30 and end 54 with the end exclusive) and 20 of the 24 down projections in the window; the four at 31,
  38, 42 and 50 moved 0.00079 to 0.00098, just under the line, so the largest change outside the changed set is
  0.00098 and 1,140 tensors equal the original. Nothing outside the window moved.
- Of the 44, 36 are edits and 8 are residues. The edits are 23 attention outputs (layers 30 to 49 and 51 to 53)
  and 13 down projections (30, 32, 33, 34, 36, 39, 43, 45, 47, 48, 49, 51, 52), relative change 0.0115 to 0.0697,
  first share 0.89 to 0.97. The residues are the down projections of 35, 37, 40, 41, 44, 46 and 53 and the
  attention output of 50, relative change 0.0010 to 0.0018 with a first share of 0.01 or less: a change with no
  direction in it, the same trace the four under the line carry. The optimiser left every matrix in the window
  touched and chose which to edit.
- A few directions per edited matrix (fourth cumulative share 0.93 to 0.99), one per matrix for the residues'
  noise.
- Input side on all 36 edits (left kept 0.39 to 0.97, right kept negative on all 36). Read as weights, one minus
  the right kept fraction, 1.35 to 4.39 (median 2.23): 4.39 at the attention output of layer 48, 3.35 at the down
  projection of 32, 3.01 at the down projection of 39; the down projections 1.80 to 3.35, the attention outputs
  1.35 to 4.39.
- Rows moved 0.0059 to 0.0077 on all 36 edits, inside finding 22's band (0.0057 to 0.0080) on every one, and
  0.0005 to 0.0008 on the eight residues; the preservation holds at a weight of 0.1997 where wnfldchen's 31B
  export at 0.1182 (piece 3) held nothing.
- A direction per matrix: 0.05 to 0.44 to the group reference, 0.002 to 0.17 between the two writers of a layer.

| Layer | Attention output: change, E1, left kept, right kept, weight | Down projection: change, E1, left kept, right kept, weight | Rows |
| --- | --- | --- | --- | --- |
| 30 | 0.0345, 0.962, 0.88, -1.46, 2.46 | 0.0285, 0.951, 0.84, -1.91, 2.91 | 0.0068, 0.0073 |
| 32 | 0.0360, 0.960, 0.88, -1.33, 2.33 | 0.0430, 0.960, 0.76, -2.35, 3.35 | 0.0070, 0.0075 |
| 35 | 0.0188, 0.909, 0.90, -0.35, 1.35 | 0.0012, 0.004, residue | 0.0066, 0.0007 |
| 37 | 0.0448, 0.938, 0.93, -1.87, 2.87 | 0.0012, 0.004, residue | 0.0072, 0.0007 |
| 39 | 0.0305, 0.950, 0.71, -0.73, 1.73 | 0.0301, 0.958, 0.60, -2.01, 3.01 | 0.0072, 0.0071 |
| 42 | 0.0358, 0.941, 0.39, -1.60, 2.60 | under the line, 0.00083 | 0.0071 |
| 45 | 0.0603, 0.966, 0.94, -1.26, 2.26 | 0.0154, 0.947, 0.79, -0.81, 1.81 | 0.0066, 0.0066 |
| 48 | 0.0697, 0.938, 0.97, -3.39, 4.39 | 0.0249, 0.966, 0.94, -1.53, 2.53 | 0.0072, 0.0068 |
| 50 | 0.0018, 0.010, residue | under the line, 0.00079 | 0.0008 |
| 53 | 0.0344, 0.940, 0.97, -1.70, 2.70 | 0.0012, 0.009, residue | 0.0073, 0.0007 |

The full table (44 rows) is in the report.

Directions. Against the saved vectors of twenty 31B measurements on the shared changed names, the leading
directions stand at 0.97 on the left and 0.99 on the right to llmfan46's 31B edit (18 shared), 0.95 and 0.98 to
coder3101's (24), 0.87 and 0.95 to the maker's own custom copy (42, four weeks later, a different window and a
different search), 0.79 and 0.37 to wnfldchen's QAT export (piece 3) and 0.69 and 0.65 to Bahushruth's; the
kernel and projection edits of the 31B stand at 0.23 or less. Finding 82's 31B arbitrary-rank family gains its
earliest member. Neither shard equals a measured file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster, "consistent with re-save noted" at home: `text_config.moe_intermediate_size`
closed by the default rule under transformers 5.22.1, and the two version strings (5.5.0.dev0 to 5.5.3) are a
re-save. The template is the pin's file and the fixed conversation renders identically.

## For the recipe library

The directional-per-layer entry is the nearest and its 84 flags are the few directions per matrix and the two
writers' disagreement; an arbitrary-rank entry would read the 36 edits in the band and the twelve traces (eight
above the line, four under it) as the search's footprint. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat37/measurements/pair-5/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
