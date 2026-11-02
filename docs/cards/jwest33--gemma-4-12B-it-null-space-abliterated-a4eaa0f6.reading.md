# Reading of the Stage 1 and Stage 2 result: jwest33/gemma-4-12B-it-null-space-abliterated against google/gemma-4-12B-it (2026-11-02)

Measured on Nautilus, round 38 piece 4 (download job 4168771, compare job 4168775, sweep 4168780; the pull carries
the measurements and the sweep record and no job log). Modified revision `9763daf7` (two commits on 2026-06-10,
13:39Z and 13:54Z), original pinned at `5926caa4`. The card (3,046 bytes) describes the maker's own toolkit
(github.com/jwest33/abliterator): orthogonal projection with null-space constraints, winsorisation at the 99.5th
percentile, Gaussian per-layer weighting "focusing on middle-to-later layers", Frobenius-norm preservation, 5,000
harmful and 1,226 harmless prompts, a directional multiplier of 1.10, and preservation prompts chosen through
Gemma Scope 2 features. The repository ships the run's `abliteration_config.json`, `refusal_directions.pt` (per-layer
directions and a `mean_direction`) and `null_space_projectors.pt`. The `base_model` field names google/gemma-4-12b-it.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer`, 271 flags (175 first shares
on the readers and writers of the early and late layers, 96 unexpected changes on the gate and up projections), on
the cluster and after re-scoring at home. On reading, the copy is what the card and the shipped configuration say:
one direction projected from every linear map of the model at a Gaussian weight over the layers.

- 329 of 677 tensors changed: the query, key, value, attention output, gate, up and down projections of all 48
  layers (328; the value projections of eight layers sit under the threshold) and the token embedding. Nothing
  else moved; the largest relative change outside the changed set is exactly 0. Relative changes 0.0017 to 0.0224,
  the embedding 0.0212.
- One direction. The leading vectors stand at 0.958 to 1.000 to the file's `mean_direction` on every layer and
  kind (the per-layer saved directions at 0.07 to 0.60, which is what `use_mean_direction: true` means); the
  seven kinds of a layer agree at 0.996 to 1.000 and the layers with each other at a median 0.979; the embedding's
  right vector stands at 1.000 to the mean direction. First shares 0.802 to 0.995, lowest where the weight is
  smallest.
- The writers (attention output, down projection) on the output side and the readers (query, key, value, gate,
  up) on the input side, each kind keeping the complement of the same weight: one minus the kept fraction, averaged
  over the kinds of a layer, is 0.10 on layers 0 to 7, rises through 0.408 (layer 15), 0.770 (20) and 0.985 (24)
  to 1.071 at layer 27, and falls through 0.910 (34), 0.515 (40) to 0.153 at layer 47; the kinds of a layer agree
  to the second decimal (0.722 on every kind of layer 37). The configuration's `adaptive_position_center` 0.6,
  `adaptive_position_sigma` 0.2 and `direction_multiplier` 1.1 give 1.1 times the larger of 0.1 and a Gaussian
  centred on layer 28.8 with a width of 9.6 layers, which fits the 48 read weights within 0.047; the best free fit
  (floor 0.06, height 1.035, centre 28.25, width 9.0) is within 0.034.
- Rows moved 0.0003 to 0.082 (the attention output of layer 34 at 0.0821), under a claim on the Frobenius norm of
  each matrix, which the rows do not measure; the per-row restoration of finding 22's band is not claimed and not
  found.

| Layer | Attention output: change, E1, left kept, right kept | Down projection: change, E1, left kept, right kept | Query: change, E1, left kept, right kept | Gate: change, E1, left kept, right kept | Read weight | Rows (attention output) |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0.0018, 0.832, 0.90, 1.00 | 0.0017, 0.827, 0.90, 0.99 | 0.0019, 0.835, 0.99, 0.90 | 0.0018, 0.837, 0.98, 0.90 | 0.100 | 0.0025 |
| 8 | 0.0019, 0.823, 0.89, 0.97 | 0.0020, 0.832, 0.89, 0.97 | 0.0019, 0.817, 0.99, 0.89 | 0.0019, 0.823, 0.98, 0.89 | 0.109 | 0.0039 |
| 16 | 0.0092, 0.977, 0.51, 0.98 | 0.0085, 0.975, 0.54, 0.78 | 0.0081, 0.971, 0.90, 0.54 | 0.0082, 0.972, 0.93, 0.54 | 0.468 | 0.0109 |
| 24 | 0.0169, 0.992, 0.00, 0.83 | 0.0186, 0.993, -0.01, 0.83 | 0.0162, 0.991, 0.94, 0.02 | 0.0169, 0.992, 0.76, 0.03 | 0.985 | 0.0156 |
| 28 | 0.0173, 0.993, -0.03, 0.69 | 0.0181, 0.993, -0.04, 0.47 | 0.0159, 0.991, 0.82, -0.09 | 0.0198, 0.994, 0.66, -0.08 | 1.067 | 0.0160 |
| 34 | 0.0162, 0.991, 0.04, 0.91 | 0.0143, 0.989, 0.09, 0.54 | 0.0134, 0.988, 0.89, 0.11 | 0.0153, 0.991, 0.52, 0.10 | 0.910 | 0.0821 |
| 40 | 0.0084, 0.974, 0.49, 0.84 | 0.0080, 0.972, 0.49, 0.73 | 0.0080, 0.972, 0.92, 0.48 | 0.0082, 0.973, 0.74, 0.49 | 0.515 | 0.0081 |
| 47 | 0.0032, 0.895, 0.84, 0.99 | 0.0024, 0.863, 0.85, 0.91 | 0.0025, 0.866, 0.97, 0.85 | 0.0027, 0.871, 0.99, 0.85 | 0.153 | 0.0036 |

The full table (329 rows) is in the report. The second kept fraction of the writers (the right, 0.47 to 1.00) and
of the readers (the left, 0.44 to 1.00) is the null-space constraint's second term, largest where the weight is.

Directions. Against thirty-seven saved vectors of 12B measurements, the leading directions stand at 0.58 and 0.62
to MoonRide's, 3MPER0RR's and prithivMLmods's kernel exports, 0.57 and 0.63 to huihui-ai's QAT edit, 0.56 and 0.61
to BinxNet's, 0.55 and 0.64 to huihui-ai's 12B edit and its two duplicates, 0.53 to igorls's, 0.52 to
richardyoung's, 0.50 to JJaguar's, and at 0.49 or less to the arbitrary-rank family (coder3101's, llmfan46's,
RumiaChannel's): a mean-difference direction from the maker's own prompt sets, nearer the other mean-difference
edits than the searched ones and equal to none. The five shards match no measured file.

## Token and configuration side (Stage 1)

"Consistent" on the cluster and at home: no field differs, the copy saved by the same library version as its
original (5.10.0.dev0), the template the pin's 17,466-byte file.

## For the recipe library

An entry for a one-direction projection on every linear map with a per-layer weight (the embedding included) would
read the copy as a clean match and print the schedule; under the per-layer entry it is 271 flags for being what
its card says. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus38/measurements/pair-4/weights.directions.safetensors`, and the
maker's own at `refusal_directions.pt` in the repository.

Weight differences alone cannot certify the absence of hidden behavior.
