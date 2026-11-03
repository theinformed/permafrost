# Reading of the Stage 1 and Stage 2 result: grayarea/Skyfall-31B-v4.1-Heretic-v1.2 against TheDrummer/Skyfall-31B-v4.1

Measured on Wheat, round 51 piece 3 (download job 387623, compare job 387626, sweep 387632; the pull carries the
measurements and the sweep record and no job log). Modified revision `f0040036` (created 2026-03-08 22:30Z, every
file uploaded in one commit at 22:33Z), parent pinned at `b41944d3` of 2026-03-05, TheDrummer's Skyfall 31B v4.1,
whose weights date from its upload of 2025-11-13 and whose `base_model` field names mistralai/Magistral-Small-2509.
The card names Heretic v1.2.0 with MPOA, full row renormalization, a winsorization quantile of 0.997, a custom
training dataset and a "model targetted" configuration, with no parameter table (a KL divergence of 0.0053, 0
refusals in 108 against 73). The configuration adds a `grayarea` block naming "heretic: gemma-3-27b-v1" as the
configuration and "heretic: gemma-3-v2" as the dataset. The parent counts as neither an original nor a copy
(finding 117). coder3101's pass of round 49 is on the next version, Skyfall-31B-v4.2 (finding 143).

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 95 flags (every changed matrix's
first share under the 0.99 floor), on the cluster and after re-scoring at home. On reading, the copy is one shared
direction on both writers of the upscale, with the fourteen inserted layers read in line with the forty around
them.

- 95 of 489 tensors changed: the down projections of layers 5 to 53 and the attention outputs of 8 to 53. Everything
  else is exactly 0, and the copy's first and last shards are the parent's by object id.
- One direction serves every layer and both writers: 0.998 to the common direction at the median, 0.967 at the
  least, 0.942 across kinds, the two writers of a layer at 0.997.
- Output side on all 95. One minus the left kept fraction draws two shapes the card does not print: 0.69 at layer
  5 rising to 0.86 at 34 and back to 0.75 at 53 on the down projections, and 0.60 at 8 rising to 1.00 at 40 and
  back to 0.78 at 53 on the attention outputs, with a dip to 0.596 at layer 27. On the fourteen inserted layers
  (28, 29, 31, 32, 34, 35, 37, 38, 40, 41, 43, 44, 46 and 47), whose parent attention outputs have norms of 0.20 to
  0.33 and down projections 0.94 to 0.99 against 9.9 to 20.6 and 36.8 to 47.3 on the others, the attention weight
  reads 0.856 to 0.997, a little above the original layers beside them (0.842 at 30, 0.791 at 33, 0.899 at 36).
- First shares 0.974 to 0.990; relative changes 0.0091 to 0.0154; rows moved 0.0023 to 0.0086 under "full row
  renormalization".

| Layer | Kind | Change | E1 | Left kept | Right kept | Weight read | Rows |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 8 | attention output | 0.0091 | 0.974 | 0.40 | 0.84 | 0.604 | 0.0028 |
| 15 | attention output | 0.0114 | 0.983 | 0.33 | 0.81 | 0.673 | 0.0049 |
| 27 | attention output | 0.0131 | 0.987 | 0.40 | 0.78 | 0.596 | 0.0034 |
| 28 | attention output | 0.0132 | 0.986 | 0.14 | 0.95 | 0.856 | 0.0053 |
| 29 | attention output | 0.0134 | 0.987 | 0.13 | 0.94 | 0.867 | 0.0058 |
| 30 | attention output | 0.0120 | 0.984 | 0.16 | 0.81 | 0.842 | 0.0026 |
| 34 | attention output | 0.0140 | 0.988 | 0.06 | 0.90 | 0.938 | 0.0056 |
| 39 | attention output | 0.0144 | 0.989 | 0.01 | 0.69 | 0.990 | 0.0028 |
| 40 | attention output | 0.0151 | 0.989 | 0.00 | 0.90 | 0.997 | 0.0058 |
| 45 | attention output | 0.0127 | 0.986 | 0.13 | 0.73 | 0.870 | 0.0025 |
| 53 | attention output | 0.0123 | 0.985 | 0.22 | 0.90 | 0.777 | 0.0053 |
| 5 | down | 0.0100 | 0.978 | 0.31 | 0.56 | 0.691 | 0.0031 |
| 20 | down | 0.0130 | 0.986 | 0.22 | 0.74 | 0.784 | 0.0078 |
| 28 | down | 0.0130 | 0.986 | 0.17 | 0.57 | 0.831 | 0.0038 |
| 34 | down | 0.0132 | 0.986 | 0.14 | 0.56 | 0.863 | 0.0048 |
| 39 | down | 0.0113 | 0.982 | 0.18 | 0.48 | 0.815 | 0.0026 |
| 53 | down | 0.0108 | 0.981 | 0.25 | 0.76 | 0.747 | 0.0037 |

The full table (95 rows) is in the report.

Two versions of one upscale. Skyfall v4.1 has the 54-layer layout finding 143 read on v4.2, the forty Magistral
layers in order with seven inserted pairs, and by byte range the two versions stand 0.0202 apart on the layer 5
query projection, 0.0254 and 0.0295 on the layer 27 and 30 attention outputs and 0.0257 on the layer 28 query
projection, while the inserted attention outputs of layers 28 and 29 stand 1.26 apart (first share 0.016): the two
versions carry unrelated near-zero writers in the inserted layers over nearly the same forty. v4.1 stands 0.0139
from Magistral on the layer 5 query projection and 0.0188 from Magistral's layer 28 on its layer 30, and its layers
28 and 29 attention outputs stand 0.074 apart.

Directions. Against the saved vectors of the Mistral Small 24B measurements, matched by layer number on parents with
the same layout, the direction stands at 0.929 on the left and 0.931 on the right to coder3101's v4.2 pass on all
90 shared names (minimum 0.900), and by byte range the leading left directions of the two changes stand at 0.917 to
0.935 on the layer 27, 28, 29 and 30 attention outputs (on the right 0.909 and 0.914 on the original layers and 0.08
on the inserted ones, whose inputs the two versions do not share). It stands at 0.882 to the maker's Magidonia pass
(pair 1), 0.870 and 0.759 to the maker's text-only Mistral Small 3.2 and Magistral passes, 0.588 to vprilepskii's
edit, 0.574 to SAIFIINDUSTRIES's Dolphin projection, 0.533 to coder3101's Magidonia pass, 0.509 to venkycs's
projection, 0.430 to darkc0de's pass (pair 4), 0.44 or less to Pranavz's measurements, 0.225 to huihui-ai's
projection and 0.07 or less to llmfan46's searches.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, for one field: `config.grayarea`, the block the maker adds to
`config.json`. The version strings move from 4.57.1 to 4.57.3. The template (4,725 bytes, `685eca2d`),
`tokenizer.json`, `tokenizer_config.json` and `special_tokens_map.json` are the parent's by object id, and the fixed
conversation renders the same. The token ids are Mistral's through the parent (`bos_token_id` 1, `eos_token_id`
`[2]`, `pad_token_id` 11) and the vocabulary is 131,072.

## For the recipe library

A shared-direction kernel entry with a heights line would read the shape; the per-layer entry charges every first
share between 0.974 and 0.990. A maker's block in `config.json` that names the run is a field the metadata tool
could read as the maker's record. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat51/measurements/pair-3/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
