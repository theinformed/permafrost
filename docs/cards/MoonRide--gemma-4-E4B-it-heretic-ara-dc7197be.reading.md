# Reading of the Stage 1 and Stage 2 result: MoonRide/gemma-4-E4B-it-heretic-ara against google/gemma-4-E4B-it (2026-11-02)

Measured on Wheat, round 37 piece 6 (download job 387161, compare job 387167, sweep 387170; the pull carries the
measurements and the sweep record and no job log). Modified revision `0327d8e7` (2026-04-11, 10:01Z to 10:33Z),
original pinned at `83df0a88`. The card says Heretic v1.2.0's arbitrary-rank ablation "with row-norm
preservation": `start_layer_index` 21, `end_layer_index` 38, `preserve_good_behavior_weight` 0.5276,
`steer_bad_behavior_weight` 0.0006, `overcorrect_relative_weight` 0.9377, `neighbor_count` 13, KL divergence
0.0162, 4 refusals in 100. Made the day before the maker's 31B copy (piece 5); the `base_model` field names the
instruct model.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 65 flags (33 first
shares, 32 within-layer cosines), on the cluster and after re-scoring at home. On reading, the same shape as the
maker's 31B copy on a smaller model: the card's window, a selection inside it, rows in the band, traces on the
skipped matrices.

- 33 of 2,076 tensors changed above the 0.001 line: the attention outputs of layers 21 to 37 (all 17, the card's
  start 21 and end 38) and the down projections of 21 to 36; the down projection of 37 moved 0.00091, just under
  the line, so the largest change outside the changed set is 0.00091 and 2,042 tensors equal the original. The 54
  shared-key-value tensors of layers 24 to 41 are absent from the save (finding 71). Nothing outside the window
  moved.
- Of the 33, 26 are edits and 7 are residues. The edits are 16 attention outputs (21 to 25 and 27 to 37) and 10
  down projections (21, 25, 27, 28, 30 to 35), relative change 0.0021 to 0.0591, first share 0.46 to 0.98; the
  down projection of 25 is the small one (0.0021, first share 0.46, weight 0.08). The residues are the down
  projections of 22, 23, 24, 26, 29 and 36 and the attention output of 26, relative change 0.0011 to 0.0017 with
  a first share under 0.01, the search's footprint on the matrices it did not edit.
- A few directions per edited matrix (fourth cumulative share 0.93 to 0.99).
- Input side on all 26 edits. Read as weights, one minus the right kept fraction, 0.08 to 2.30 (median 1.67): the
  attention outputs 1.39 to 2.30 (2.30 at layer 32, 2.25 at 29), the down projections 1.48 to 1.92 besides the
  0.08 at layer 25.
- Rows moved 0.0051 to 0.0078 on the 26 edits, inside finding 22's band on 25 and under it (0.0051, the layer 25
  down projection) on one, and 0.0007 to 0.0008 on the residues.
- A direction per matrix: 0.14 to 0.41 to the group reference, 0.006 to 0.47 between the two writers of a layer.

| Layer | Attention output: change, E1, left kept, right kept, weight | Down projection: change, E1, left kept, right kept, weight | Rows |
| --- | --- | --- | --- | --- |
| 21 | 0.0354, 0.911, 0.78, -0.63, 1.63 | 0.0330, 0.902, 0.75, -0.92, 1.92 | 0.0074, 0.0071 |
| 22 | 0.0581, 0.927, 0.46, -0.83, 1.83 | 0.0016, 0.009, residue | 0.0075, 0.0008 |
| 24 | 0.0552, 0.976, 0.10, -0.97, 1.97 | 0.0014, 0.006, residue | 0.0074, 0.0008 |
| 25 | 0.0426, 0.968, 0.49, -0.39, 1.39 | 0.0021, 0.459, 0.99, 0.92, 0.08 | 0.0077, 0.0051 |
| 26 | 0.0016, 0.007, residue | 0.0014, 0.007, residue | 0.0008, 0.0007 |
| 29 | 0.0477, 0.953, 0.91, -1.25, 2.25 | 0.0016, 0.006, residue | 0.0073, 0.0007 |
| 32 | 0.0435, 0.962, 0.70, -1.30, 2.30 | 0.0241, 0.911, 0.75, -0.62, 1.62 | 0.0074, 0.0063 |
| 35 | 0.0224, 0.951, 0.73, -0.71, 1.71 | 0.0260, 0.926, 0.92, -0.59, 1.59 | 0.0069, 0.0075 |
| 37 | 0.0411, 0.964, 0.39, -0.63, 1.63 | under the line, 0.00091 | 0.0077 |

The full table (33 rows) is in the report.

Directions. Against the saved vectors of the measurements of the E4B on the shared changed names, the leading directions
stand at 0.99 on both sides to NullpoLab's Refusals5 (27 shared), 0.99 and 0.98 to coder3101's E4B edit (17),
0.98 and 0.95 to llmfan46's ultra copy, 0.94 and 0.98 to NullpoLab's Refusals8-attn (piece 8, 20 shared), 0.90 and
0.98 to JokeHer's, 0.90 and 0.95 to llmfan46's, 0.84 and 0.94 to alphakek's, 0.76 and 0.91 to coder3101's QAT
edit, 0.63 to Bahushruth's, 0.55 and 0.30 to igorls's QAT edit and 0.35 to OS-Software's E4B: the E4B
arbitrary-rank family of finding 82 with this copy, made 04-11, among its earliest members. The one shard equals
no measured file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster, "consistent with re-save noted" at home: `text_config.moe_intermediate_size`
closed by the default rule under transformers 5.22.1, and the version strings are a re-save. The template is the
pin's file and the fixed conversation renders identically.

## For the recipe library

As for the maker's 31B copy: the directional-per-layer entry is the nearest, an arbitrary-rank entry would read the
26 edits in the band and the eight traces as the search's footprint. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat37/measurements/pair-6/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
