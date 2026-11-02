# Reading of the Stage 1 and Stage 2 result: RumiaChannel/gemma-4-12B-it-uncensored-ara-Refusals9 against google/gemma-4-12B-it (2026-11-01)

Measured on Blueback, round 22 piece 3. The pull carries the measurements and the sweep record and no job log.
Modified revision `acacd432` (seven commits: the weights, tokenizer and README on 2026-06-05, then "Update
chat_template.jinja" and "Update tokenizer_config.json" on 07-21), original pinned at `5926caa4` (06-04), the
revision current when the repository was created. The card prints the Heretic 1.2.0 arbitrary-rank record: start
layer 14, end layer 44, `preserve_good_behavior_weight` 0.9147, `steer_bad_behavior_weight` 0.0001,
`overcorrect_relative_weight` 0.1317, neighbour count 12, row-norm preservation on, a KL divergence of 0.0066 and 9
refusals in 100 against 91 for the original. The `base_model` field names the original.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 97 flags, on the
cluster and after re-scoring at home: 55 first shares (0.002 to 0.968) and 42 within-layer cosines (0.006 to 0.37).
On reading, the footprint is the card's window with every in-range matrix rewritten: 34 edits, 21 rounding
residues and 5 matrices left under the threshold, the arbitrary-rank shape of finding 22 on both writers.

- 55 of 677 tensors changed, all inside layers 14 to 43 (the card's 14 to 44 with its exclusive end): 27 attention
  outputs and 28 down projections. The five other in-range matrices moved by 0.00084 to 0.00096 of their norm,
  under the 0.001 threshold (the down projection of layer 17 at 0.00096 is the largest change outside the changed
  set); nothing outside the window moved and 617 tensors equal the original.
- 34 edits: the attention outputs of layers 22, 24, 25, 27 to 31, 34, 36, 37, 42 and 43 (13, relative change 0.006
  to 0.018, first share 0.84 to 0.97) and the down projections of 18, 19, 22, 24, 26 to 31 and 33 to 43 (21,
  relative change 0.006 to 0.015, first share 0.49 to 0.94). The fourth cumulative share is 0.87 to 0.98: a leading
  direction with a tail, not rank one.
- 21 residues: 14 attention outputs (layers 14 to 19, 21, 23, 26, 32, 33, 35, 39, 41) and 7 down projections (14,
  16, 20, 21, 23, 25, 32) rewritten at 0.0010 to 0.0018 of their norm with a first share of 0.002 to 0.094, the
  original's action kept at 0.99 to 1.01 on both sides and rows within 0.0009: matrices the search weighted to
  nothing, as coder3101's 31B and 12B copies left them.
- Input side on 34 of 34 edits: the left kept fraction is 0.82 to 0.995 and the right -0.25 to 0.39, so the weight
  along the leading right direction is 0.61 to 1.25. Each matrix has its own direction: the two writers of a layer
  agree at 0.006 to 0.998, under 0.95 on 21 of the 25 layers with two edits, and the groups' medians are 0.19 and
  0.28.
- Rows moved by 0.0053 to 0.0079 on the 34 edits, the band finding 22 reads on every copy that claims the
  preservation step.

| Layer | Attention output: change, E1, E4, left kept, right kept | Down projection: change, E1, E4, left kept, right kept | Within-layer cosine | Row norms |
| --- | --- | --- | --- | --- |
| 14 | 0.0015, 0.030, 0.043, 1.000, 0.993 (residue) | 0.0014, 0.011, 0.018, 1.000, 1.005 (residue) | 0.08 | 0.0008, 0.0007 |
| 18 | 0.0013, 0.016, 0.029, 0.999, 0.996 (residue) | 0.0058, 0.858, 0.870, 0.980, 0.585 | 0.37 | 0.0008, 0.0076 |
| 22 | 0.0104, 0.952, 0.958, 0.948, 0.244 | 0.0090, 0.937, 0.944, 0.906, 0.006 | 0.19 | 0.0078, 0.0065 |
| 24 | 0.0146, 0.959, 0.967, 0.922, -0.045 | 0.0140, 0.686, 0.874, 0.944, 0.122 | 0.27 | 0.0077, 0.0076 |
| 28 | 0.0146, 0.905, 0.920, 0.836, 0.107 | 0.0101, 0.931, 0.943, 0.918, 0.059 | 0.14 | 0.0058, 0.0069 |
| 30 | 0.0125, 0.921, 0.946, 0.935, 0.238 | 0.0147, 0.493, 0.841, 0.898, -0.060 | 0.22 | 0.0078, 0.0077 |
| 36 | 0.0179, 0.959, 0.976, 0.995, -0.253 | 0.0102, 0.840, 0.896, 0.912, 0.182 | 0.998 | 0.0077, 0.0074 |
| 42 | 0.0136, 0.968, 0.974, 0.963, 0.222 | 0.0103, 0.844, 0.888, 0.903, 0.158 | 0.31 | 0.0076, 0.0071 |
| 43 | 0.0109, 0.958, 0.966, 0.881, 0.192 | 0.0098, 0.891, 0.909, 0.926, 0.163 | 0.09 | 0.0077, 0.0077 |

The full table (55 rows) is in the report.

The fingerprint shares no measured field with the seventeen earlier reports on this original. Six tensors equal
coder3101's 12B copy's rows by value and nothing by field: residues that two searches weighted to nothing round the
same way.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, one field. At home under transformers 5.22.1 the 12B family's
six fields (finding 39) close by tool, the four omitted defaults by the default rule and the two sub-configuration
data types by the data-type rule, with the version strings (5.10.0.dev0 to 5.10.2). The template stays open: the
copy carries an 18,682-byte `chat_template.jinja` updated on 07-21, one byte short of the 18,683-byte Canonical
file Google published on 07-20, against a pin of 06-04 that carries the earlier format. The later-revision rule
looks for Google's file and does not find it at one byte's distance. The maker's commit title says what happened:
the template was refreshed from Google's a day after Google changed it.

## For the recipe library

The arbitrary-rank shape on both writers with the preservation claim, the seventeenth copy of the method and the
sixth with the down projections (finding 22): a window to the layer, 34 searched input-side weights of 0.61 to
1.25, 21 residues and 5 matrices under the threshold, rows within 0.008. An `arbitrary-rank` entry that sets the
residues aside and reads one direction per matrix would count no flag; the per-layer entry counts 97 because it
asks for rank one and for the writers of a layer to agree. The pull copy keeps the direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/blueback22/measurements/pair-3/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
