# Reading of the Stage 1 and Stage 2 result: llmfan46/gemma-4-12B-it-uncensored-heretic against google/gemma-4-12B-it (2026-10-31)

Measured on Blueback, round 13 piece 8 (push card 5404, download job 3400579, compare job 3400587; pulled home by
card 5530). Modified revision `cf3bb4a1` (the repository was created on 2026-06-11 at 22:55Z), original pinned at
`5926caa4` (2026-06-04). The card says Heretic v1.2.0 with arbitrary-rank ablation, `o_proj` only, start layer 24,
end layer 40, with the searched objective weights it prints (preserve 0.7201, steer 0.0067, overcorrect 0.9541).

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 15 flags, on the
cluster and after re-scoring at home, all energy shares (0.914 to 0.983 on 15 of 16 matrices).

- 16 of 677 tensors changed: the attention outputs of layers 24 to 39, the card's range with its exclusive end.
  No down projection moved, the largest relative change outside the changed set is exactly 0 and 661 tensors
  equal the original.
- Input side: the left kept fraction is 0.76 to 1.00 and the right −2.63 to 0.68, the left above the right on 16
  of 16; the edit acts on what the matrix reads, as on the maker's other arbitrary-rank copies (finding 12).
- Searched weights per layer, one minus the right kept fraction: 1.26 to 2.64 on layers 24 to 36 and 38, 39;
  3.63 on layer 35 and 0.32 on layer 37. First-value share 0.914 to 0.993 and first-eight 0.957 to 0.997, the
  arbitrary-rank residue beyond one direction.
- Per-layer directions: cross-layer cosine 0.09 to 0.41. Row norms moved by 0.0014 to 0.083, largest where the
  weight is largest.

| Layer | Attention output: change, E1, E8, left kept, right kept | Weight read | Cross-layer cosine | Row norms |
| --- | --- | --- | --- | --- |
| 24 | 0.0319, 0.961, 0.978, 0.84, -0.80 | 1.80 | 0.23 | 0.0035 |
| 25 | 0.0312, 0.960, 0.976, 0.90, -0.66 | 1.66 | 0.19 | 0.0022 |
| 26 | 0.0331, 0.965, 0.977, 0.77, -0.89 | 1.89 | 0.34 | 0.0041 |
| 27 | 0.0310, 0.914, 0.974, 0.90, -0.75 | 1.75 | 0.26 | 0.0070 |
| 28 | 0.0336, 0.963, 0.980, 0.76, -0.79 | 1.79 | 0.41 | 0.0061 |
| 29 | 0.0144, 0.943, 0.957, 0.95, -0.26 | 1.26 | 0.32 | 0.0023 |
| 30 | 0.0234, 0.970, 0.982, 0.90, -0.46 | 1.46 | 0.19 | 0.0032 |
| 31 | 0.0304, 0.959, 0.978, 0.92, -0.72 | 1.72 | 0.16 | 0.0030 |
| 32 | 0.0456, 0.948, 0.985, 0.91, -1.12 | 2.12 | 0.39 | 0.0133 |
| 33 | 0.0648, 0.980, 0.991, 0.87, -1.44 | 2.44 | 0.36 | 0.0337 |
| 34 | 0.0414, 0.958, 0.986, 0.90, -1.04 | 2.04 | 0.22 | 0.0366 |
| 35 | 0.0703, 0.983, 0.995, 0.93, -2.63 | 3.63 | 0.33 | 0.0826 |
| 36 | 0.0244, 0.993, 0.997, 1.00, -1.64 | 2.64 | 0.09 | 0.0043 |
| 37 | 0.0329, 0.966, 0.988, 1.00, 0.68 | 0.32 | 0.13 | 0.0254 |
| 38 | 0.0353, 0.983, 0.990, 0.85, -1.08 | 2.08 | 0.29 | 0.0062 |
| 39 | 0.0153, 0.971, 0.987, 0.99, -0.63 | 1.63 | 0.36 | 0.0014 |

The weight read is one minus the right kept fraction, the input side. Against the six other 12B copies on this
weight file, no changed matrix has an equal measurement in any field; the leading vectors lie about 0.1 inside the
four-dimensional subspace AEON-7's output-side copy removes. This copy is the source of DarkRomeo88's four
single-file quantised checkpoints (round 14 pair 2), which were not measured.

## Token and configuration side (Stage 1)

"Unexplained differences" on seven fields on the cluster and at home: the six class-default fields of finding 11
(the audio and vision sub-configuration values and their repeated data types) in a re-save from 5.10.0.dev0 to
5.10.2, and the template. The template is 21,488 bytes (21,065 characters, no carriage returns) against Google's
17,466 at the pin: Google's file plus the maker's `format_type_argument` macro and `is mapping` and `'key' in
value` guards (157 lines added, 100 removed), the macro identical to the one in the maker's 26B-A4B copy and
without the thought-block patch of finding 23. The fixed conversation renders identically.

## For the recipe library

Consistent with the card: 16 attention outputs on layers 24 to 39, input side, arbitrary rank, searched weights
0.32 to 3.63, the eleventh arbitrary-rank copy (finding 22) and the maker's fifth Gemma 4 size after the E2B, E4B, 26B-A4B and 31B. The saved
direction vectors are not committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/blueback13/measurements/pair-8/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
