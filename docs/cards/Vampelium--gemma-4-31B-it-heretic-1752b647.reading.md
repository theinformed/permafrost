# Reading of the Stage 1 and Stage 2 result: Vampelium/gemma-4-31B-it-heretic against google/gemma-4-31B-it (2026-11-02)

Measured on Nautilus, round 40 piece 4 (download job 4169647, compare job 4169651, sweep 4169656; the pull carries
the measurements and the sweep record and no job log). Modified revision `88a86a0b` (created 2026-08-30 14:31Z, the
card at 14:53 "produced on 4x A100", the upload at 16:35Z), original pinned at `842da379`. The card carries no
table: "Vampelium's local Gemma 4 31B IT checkpoint after Heretic abliteration", the shards "reassembled from
Google Drive split-download names" with all 1,188 tensors matching the index, saved with transformers 5.6.2.

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 21 flags (19 first shares, 2
within-layer cosines), on the cluster and after re-scoring at home. On reading, the copy is one direction per
layer on the output side of both writers across the last 26 and 21 layers, two kernels the card does not print.

- 47 of 1,188 tensors changed: the attention outputs of layers 34 to 59 (26) and the down projections of 39 to
  59 (21). Nothing else moved; the largest relative change outside the changed set is exactly 0 on all 1,141
  other tensors.
- Rank one on every matrix: first shares 0.992 to 0.996 on the down projections and 0.967 to 0.994 on the
  attention outputs from layer 39 up, falling to 0.79 at layer 34 where the change is 0.0014, the kernel's tail
  (the 19 first-share flags are these small changes). One direction per layer: the two writers of a layer at 0.95
  or better to each other on 20 of the 21 layers that have both, and 0.924 at layer 59 (the 2 flags).
- Output side on all 47: one minus the left kept fraction is 0.04 at layer 34 rising to 1.16 at 50 and falling
  to 0.36 at 59 on the attention outputs, and 1.01 at 39 rising to 1.45 at 56 and 58 on the down projections; the
  right side keeps -0.07 to 0.97. Rows moved 0.0005 to 0.0043 on the attention outputs and 0.0016 to 0.041 on
  the down projections (0.041 on the last), under no claim. Relative changes 0.0014 to 0.0248.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Down projection: change, E1, left kept, right kept | Weight | Rows |
| --- | --- | --- | --- | --- | --- |
| 34 | 0.0014, 0.792, 0.96, 0.97 | 0.04 | - | - | 0.0005, - |
| 36 | 0.0043, 0.934, 0.80, 0.90 | 0.20 | - | - | 0.0017, - |
| 39 | 0.0081, 0.972, 0.54, 0.76 | 0.46 | 0.0171, 0.993, -0.01, 0.31 | 1.01 | 0.0027, 0.0034 |
| 42 | 0.0104, 0.981, 0.25, 0.60 | 0.75 | 0.0165, 0.992, -0.16, 0.15 | 1.16 | 0.0016, 0.0021 |
| 46 | 0.0158, 0.991, -0.08, 0.44 | 1.08 | 0.0179, 0.993, -0.25, 0.04 | 1.25 | 0.0023, 0.0019 |
| 50 | 0.0173, 0.992, -0.16, 0.67 | 1.16 | 0.0197, 0.994, -0.33, 0.40 | 1.33 | 0.0030, 0.0030 |
| 54 | 0.0123, 0.986, 0.12, 0.57 | 0.88 | 0.0206, 0.994, -0.42, -0.01 | 1.42 | 0.0020, 0.0017 |
| 56 | 0.0112, 0.983, 0.28, 0.70 | 0.72 | 0.0221, 0.995, -0.45, -0.04 | 1.45 | 0.0018, 0.0018 |
| 59 | 0.0076, 0.967, 0.64, 0.77 | 0.36 | 0.0248, 0.996, -0.18, 0.62 | 1.18 | 0.0043, 0.0407 |

The full table (26 rows) is in the report.

Directions. Against twenty-six saved vectors of other measurements of the 31B, the directions stand at 1.000 on
both sides to 3MPER0RR's export on all 41 shared names (minimum 1.000), at 1.000 to germlag's duplicate of
coder3101's second export on all 47 (left minimum 0.983 at layer 34), at 1.000 to callmegrr's heretic-z on 12
(minimum 0.999), at 0.992 and 0.996 to ressl's, 0.958 and 0.969 to TrevorJS's, 0.87 to wangzhang's and
nguyenthilaitrieulong's, and at 0.57 or less to the rest (0.13 to coder3101's first export, 0.012 to
cosmicoptima's). By byte range the copy is 0.0094 from Google on the layer 41 attention output and 0.0017 from
3MPER0RR's, 0.0064 from callmegrr's and 0.0100 from germlag's there; 0.0014 to 0.0035 from the three on the
layer 41 and 50 down projections; and byte-equal to Google and germlag's copy on the layer 10 query projection.
The first seven of the thirteen shards (`78be59e4` to `566b3699`) are byte-equal to 3MPER0RR's, the two
exports touching nothing below layer 34; the other six match no measured file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster, "consistent with re-save noted" at home: the home judgement closed
`text_config.moe_intermediate_size` by the default rule under transformers 5.22.1, leaving the version strings
(5.5.0.dev0 to 5.6.2, as the card says). The tokenizer, the token ids, the generation settings and the
18,683-byte template are the pin's.

## For the recipe library

The per-layer entry with selection reads the copy; a kernel-tail rule (first shares under 0.99 where the change
is under 0.01) would close the 19 flags. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus40/measurements/pair-4/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
