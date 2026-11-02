# Reading of the Stage 1 and Stage 2 result: wangzhang/gemma-4-E2B-it-abliterated against google/gemma-4-E2B-it (2026-11-01)

Measured on Blueback, round 25 piece 6. The pull carries the measurements and the sweep record and no job log.
Modified revision `9b367c29` (nine commits from 2026-04-10 05:33Z to 08-29: two folder uploads, README updates,
"sync tokenizer_config.json from google/gemma-4-E2B-it", a licence and a disclaimer), original pinned at
`b446025c` (04-10, 02:02Z), the revision current when the repository was created. The card describes the maker's
Abliterix tool: direct orthogonal projection of the refusal direction out of the attention query, key, value and
output projections and the down projection ("5 steerable components × 27 effective layers"), row magnitudes
preserved, targets restricted to layers 5 to 30 of 35, a multi-objective Optuna search over 100 trials with trial
60 chosen, 9 refusals in 100 against 99, KL divergence 0.0004, and a page on why short generations undercount
refusals. The `base_model` field names the original.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 5 flags, on the
cluster and after re-scoring at home: five first shares of 0.987 to 0.990 on the queries of layers 16 to 20, the
smallest edits. On reading, the copy is four of the card's five components, each with its own layer window and
its own weight band, one direction per layer shared by every edited matrix of that layer, rows restored.

- 72 of 1,951 tensors changed: the attention outputs of layers 9 to 34 (26), the value projections of 9 to 14
  (6), the down projections of 14 to 34 (21) and the queries of 16 to 34 (19). No key projection changed. Nothing
  else moved; the largest relative change outside the changed set is exactly 0 and 1,879 tensors equal the
  original. The 60 shared-KV tensors of layers 15 to 34 are dropped by the export, so the values of those layers
  do not exist in the copy and could not have been edited.
- The window is layers 9 to 34, not the card's 5 to 30: the lowest edit is at layer 9 and the highest at 34, the
  last layer, on both the attention outputs and the down projections. The card's "27 effective layers" is one more
  than the 26 the attention outputs span.
- One direction per layer: within a layer the edited matrices agree at 0.9994 or better across all four kinds;
  across layers the directions agree at medians of 0.25 to 0.60.
- Four weight bands. On the attention outputs (output side, 26 of 26) the left kept fraction runs -0.91 at layer 9,
  -1.51 at 19, -2.12 at 27 and -1.82 at 34: a weight of 1.91 rising to 3.12 and falling to 2.82. On the value
  projections (input side, 6 of 6) the right kept fraction is -1.31 to -2.02, a weight of 2.31 to 3.02 rising with
  depth. On the down projections (output side, 21 of 21) the left runs 0.28 at layer 14 through 0 at 22 to -0.43 at
  33, a weight of 0.72 to 1.43. On the queries (input side, 19 of 19) the right kept fraction is 0.11 to 0.44, a
  weight of 0.56 to 0.89.
- Rows moved by at most 0.0005 on all 72: restored.
- Rank one everywhere (first share 0.987 to 0.999). Relative change 0.048 to 0.088 on the attention outputs, 0.056
  to 0.081 on the values, 0.020 to 0.039 on the down projections and 0.014 to 0.023 on the queries.

| Layer | Attention output: change, E1, left kept, right kept | Value: change, left kept, right kept | Down projection: change, E1, left kept, right kept | Query: change, E1, left kept, right kept |
| --- | --- | --- | --- | --- |
| 9 | 0.0546, 0.998, -0.913, 0.170 | 0.0602, 0.376, -1.312 | - | - |
| 12 | 0.0569, 0.998, -1.038, 0.309 | 0.0726, 0.589, -1.681 | - | - |
| 14 | 0.0586, 0.999, -1.157, -0.387 | 0.0807, 0.008, -2.020 | 0.0202, 0.993, 0.276, 0.822 | - |
| 18 | 0.0605, 0.998, -1.438, 0.173 | - | 0.0245, 0.994, 0.159, 0.492 | 0.0137, 0.987, 0.941, 0.401 |
| 22 | 0.0773, 0.997, -1.764, 0.612 | - | 0.0280, 0.996, -0.021, 0.272 | 0.0178, 0.992, 0.900, 0.286 |
| 27 | 0.0878, 0.992, -2.121, 0.821 | - | 0.0322, 0.997, -0.272, 0.219 | 0.0202, 0.994, 0.793, 0.141 |
| 31 | 0.0785, 0.997, -1.988, 0.625 | - | 0.0378, 0.998, -0.408, -0.122 | 0.0226, 0.995, 0.775, 0.115 |
| 34 | 0.0675, 0.994, -1.820, -0.329 | - | 0.0363, 0.997, -0.428, 0.123 | 0.0201, 0.993, 0.836, 0.171 |

The full table (72 rows) is in the report.

The fingerprint shares no measured field with the ten earlier reports on this original. The maker's 31B copy
(round 2) edited the queries, keys, values and outputs of every layer; this one adds the down projection, drops
the keys and chooses a window.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster; "consistent with re-save noted" at home. Under transformers 5.22.1
`text_config.moe_intermediate_size` (null in a 5.6.0.dev0 save) closes by the default rule, and what remains is
the version strings. The template is Google's pinned file and the fixed conversation renders identically.

## For the recipe library

Per-layer directions on four kinds of matrix with a weight band per kind, the largest searched output-side weight
in the census on an E2B (3.12 on the attention output of layer 27), rows restored. The per-layer entry fits the two
writers and counts five first shares at the floor on the weakest queries; an Abliterix entry would list the four
kinds, the sides and the bands. The card's window and component count do not read back: layers 9 to 34 against 5
to 30, four components against five. The pull copy keeps the direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/blueback25/measurements/pair-6/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
