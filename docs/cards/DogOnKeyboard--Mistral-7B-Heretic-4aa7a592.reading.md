# Reading of the Stage 1 and Stage 2 result: DogOnKeyboard/Mistral-7B-Heretic against mistralai/Mistral-7B-Instruct-v0.3 (2026-11-01)

Measured on Nautilus, round 20 piece 8 (download job 4143641, compare job 4143649, 409 seconds, sweep 4143650).
Modified revision `40ce32fd` (seven commits from 2025-11-19 14:18Z to 11-20 14:02Z: the weights at 15:12Z on the
first day, the tokenizer, the README, and three README edits), original pinned at `0d4b76e1` (2025-07-08), the
revision current when the repository was created. The card prints the Heretic 1.0.1 record: direction index
17.44, the attention outputs at weight 1.45 centred on layer 23.46 (minimum 1.12, width 12.18), the down
projections at 0.95 centred on 24.84 (minimum 0.59, width 18.53), a KL divergence of 0.12 and 8 refusals in 100
against the original, and a note that the copy is deprecated in favour of a V2. The `base_model` field names
the original.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection-selected`, 23 flags, on the
cluster and after re-scoring at home: first shares of 0.976 to 0.990 on 23 of the 25 down projections, whose
change is 0.95 to 1.6 percent of the norm. On reading, the copy is the card's record as written: every kernel
value reads back from the weights within 0.003.

- 45 of 291 tensors changed: the attention outputs of layers 12 to 31 (20 matrices) and the down projections of
  layers 7 to 31 (25). The attention kernel centred on 23.46 with width 12.18 reaches 11.28 to 35.64 of a
  32-layer model, the down kernel centred on 24.84 with width 18.53 reaches 6.31 to 43.37: layers 12 to 31 and
  7 to 31 exactly. Nothing else moved; the largest relative change outside the changed set is exactly 0 and 246
  tensors equal the original.
- One shared direction: every leading direction agrees with the group reference at cosine 1.000 and within a
  layer at 1.000, the card's one direction at index 17.44. Each change is rank one (first share 0.976 to 0.996).
- Output side on all 45: the left kept fraction is below the right on 45 of 45. The left kept fraction is one
  minus the kernel's weight at that layer: on the attention outputs it runs from -0.141 at layer 12 to -0.440 at
  23 and back to -0.249 at 31, where the card's kernel gives -0.140, -0.438, -0.249; on the down projections
  from 0.398 at layer 7 to 0.054 at 25 and back to 0.170 at 31, where the kernel gives 0.397, 0.053, 0.170.
  The largest gap between the two on any of the 45 matrices is 0.003.
- Rows moved by 0.003 to 0.014, unrestored; the version predates row-norm preservation.
- Relative changes of 0.020 to 0.025 on the attention outputs and 0.0095 to 0.016 on the down projections; the
  largest absolute difference is 0.0035.

| Layer | Attention output: change, E1, left kept, kernel 1-w | Down projection: change, E1, left kept, kernel 1-w | Row norms |
| --- | --- | --- | --- |
| 7 | - | 0.0095, 0.976, 0.398, 0.397 | -, 0.0036 |
| 10 | - | 0.0108, 0.981, 0.339, 0.338 | -, 0.0035 |
| 12 | 0.0205, 0.994, -0.141, -0.140 | 0.0124, 0.985, 0.300, 0.299 | 0.0087, 0.0055 |
| 15 | 0.0236, 0.996, -0.222, -0.221 | 0.0145, 0.989, 0.242, 0.241 | 0.0134, 0.0089 |
| 18 | 0.0224, 0.995, -0.304, -0.302 | 0.0143, 0.989, 0.183, 0.183 | 0.0105, 0.0077 |
| 21 | 0.0203, 0.994, -0.385, -0.383 | 0.0135, 0.987, 0.125, 0.125 | 0.0052, 0.0039 |
| 23 | 0.0228, 0.995, -0.440, -0.438 | 0.0139, 0.988, 0.086, 0.086 | 0.0053, 0.0062 |
| 25 | 0.0231, 0.995, -0.410, -0.408 | 0.0142, 0.988, 0.054, 0.053 | 0.0071, 0.0129 |
| 28 | 0.0209, 0.994, -0.329, -0.327 | 0.0135, 0.987, 0.112, 0.111 | 0.0051, 0.0097 |
| 31 | 0.0202, 0.994, -0.249, -0.246 | 0.0129, 0.986, 0.170, 0.170 | 0.0078, 0.0063 |

The kernel column is one minus the card's weight at that layer, from the four numbers the card prints for each
writer.

The fingerprint shares no measured field with the three earlier reports on this original, all abliterations
(rounds 7 and 11); this is the first Heretic copy of Mistral 7B Instruct v0.3 in the census.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, four fields. Two are one rename: the copy's 4.57.1 save
writes `dtype: bfloat16` where the original's 4.42.0 file wrote `torch_dtype: bfloat16`; the library renamed the
field between those versions, the two declare the same type, and the scorer has no rule for the pair, so both
sides of the rename stay open. Two are one declaration: the copy's tokenizer configuration and special-tokens
map declare `</s>` (id 2) as the pad token where the original declares none, the tool's save of a tokenizer it
had given a pad token for batching. `head_dim` (absent in the original, 128 in the copy) closed by the default
rule, the template moved from `tokenizer_config.json` to `chat_template.jinja` and closed by the existing rule,
and the fixed conversation renders identically. Closed by hand; the rename rule is owed.

## For the recipe library

The second copy in the census whose Heretic kernel reads back from the weights to the third decimal on every
matrix (the first was AISafety-Student's Ministral copy, finding 41), and the first on a Mistral 7B base. The 23
flags are the 0.99 first-share floor on down projections whose kernel weight is 0.59 to 0.95, where the change is
about 1 percent of the norm and bfloat16 leaves a tenth of it off the leading direction; a Heretic 1.0 entry
needs the 0.985 floor finding 41 named, or a floor that scales with the weight. The pull copy keeps the
direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus20/measurements/pair-8/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
