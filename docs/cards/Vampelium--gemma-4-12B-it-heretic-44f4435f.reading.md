# Reading of the Stage 1 and Stage 2 result: Vampelium/gemma-4-12B-it-heretic against google/gemma-4-12B-it (2026-11-01)

Measured on Blueback, round 22 piece 4. The pull carries the measurements and the sweep record and no job log.
Modified revision `2e3353f4` (two commits on 2026-08-29: the initial commit at 16:23Z and the weights by the
large-folder tool at 17:04Z), original pinned at `707f0a3b` (07-20), the revision current when the repository was
created. The card is three sentences and a file table: "Vampelium's local Gemma 4 12B IT checkpoint after Heretic
abliteration", five bfloat16 shards, a demo space. It prints no kernel, no trial and no refusal count. The
`base_model` field names the original.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 38 flags, on the
cluster and after re-scoring at home: 38 first shares of 0.79 to 0.99 on the matrices at the edges of both windows,
where the edit is smallest. On reading, the copy is a Heretic kernel pair whose shape the card does not print: one
direction shared across the model, output side, with kept fractions that run smoothly from the window's edge to
its centre and back.

- 75 of 677 tensors changed: the attention outputs of layers 5 to 47 (43) and the down projections of 16 to 47
  (32). Nothing else moved; the largest relative change outside the changed set is exactly 0 and 602 tensors equal
  the original.
- Nearly one direction: the attention outputs agree with their group at a median of 0.996 (minimum 0.951), the
  down projections at 0.998 (0.987), the two kinds at 0.92, and the two writers of a layer at 0.982 to 0.999.
- Output side on 75 of 75, with a schedule. On the attention outputs the left kept fraction runs 0.88 at layer 5,
  0.68 at 10, 0.34 at 16, 0.18 at 19, 0.03 at 22, -0.15 at 26, -0.29 at 30 and 31, -0.16 at 35, 0.07 at 40, 0.31 at
  43 and 0.44 at 47. On the down projections it runs 0.90 at 16, 0.62 at 20, 0.34 at 24, 0.08 at 28, -0.13 at 31,
  -0.35 at 34, -0.41 at 35, -0.33 at 37, -0.12 at 40, 0.15 at 44 and 0.36 at 47. Read as one minus a weight, the
  attention kernel peaks at 1.29 near layer 31 and the down kernel at 1.41 near layer 35, each falling toward 0.1
  at the window's edges: the shape Heretic's four numbers per writer describe.
- Rank one where the edit is large: first share 0.79 at the down projection of layer 16 (relative change 0.0019)
  rising to 0.996 at layer 31 (0.0238) and falling again to 0.98 at 47; the floor of finding 3 explains the fall
  (the leftover is 0.0013 to 0.0017 of the norm throughout).
- Rows moved by 0.0010 to 0.0044 on the attention outputs and 0.0005 to 0.0033 on the down projections.

| Layer | Attention output: change, E1, left kept, right kept | Down projection: change, E1, left kept, right kept | Within-layer cosine | Row norms |
| --- | --- | --- | --- | --- |
| 5 | 0.0025, 0.844, 0.881, 0.979 | - | - | 0.0012, - |
| 10 | 0.0066, 0.960, 0.677, 0.907 | - | - | 0.0020, - |
| 16 | 0.0113, 0.984, 0.344, 0.813 | 0.0019, 0.794, 0.902, 0.965 | 0.992 | 0.0034, 0.0005 |
| 22 | 0.0157, 0.992, 0.025, 0.633 | 0.0089, 0.975, 0.479, 0.682 | 0.999 | 0.0030, 0.0016 |
| 26 | 0.0190, 0.994, -0.154, 0.558 | 0.0135, 0.988, 0.261, 0.480 | 0.998 | 0.0030, 0.0019 |
| 31 | 0.0238, 0.996, -0.293, 0.479 | 0.0192, 0.994, -0.132, 0.213 | 0.997 | 0.0041, 0.0026 |
| 35 | 0.0187, 0.994, -0.162, 0.674 | 0.0233, 0.996, -0.412, 0.028 | 0.995 | 0.0030, 0.0026 |
| 40 | 0.0156, 0.991, 0.072, 0.654 | 0.0187, 0.993, -0.118, 0.192 | 0.996 | 0.0027, 0.0025 |
| 47 | 0.0093, 0.978, 0.443, 0.832 | 0.0106, 0.982, 0.363, 0.546 | 0.982 | 0.0025, 0.0017 |

The full table (75 rows) is in the report.

The fingerprint shares no measured field with the seventeen earlier reports on this original, and one tensor by value
with each of the four copies of TrevorJS's file (a coincidence of rounding on one row, no field).

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, three fields. At home under transformers 5.22.1 the 12B
family's six fields (finding 39) close by tool with the version strings (5.10.0.dev0 to 5.16.1). What stays open
is the 5.16 save form: `global_head_dim` 512 and `num_global_key_value_heads` 1 leave the text configuration and
return as a `per_layer_config` map under the global layers' indices, the seventh copy on this form and the first
12B; closed by hand. The template is Google's pinned file and the fixed conversation renders identically.

## For the recipe library

A Heretic pair on Gemma 4 12B whose kept fractions carry a schedule: the finding 46 reading of three 12B copies
(one shared direction, no weight) does not hold here, and the difference is not in the base. The `directional-per-layer-selected` entry fits the windows and the side and counts 38 first shares at the
windows' edges, where the kernel's weight is under 0.5 and the floor crosses the 0.99 line. The pull copy keeps the direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/blueback22/measurements/pair-4/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
