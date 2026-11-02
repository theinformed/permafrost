# Reading of the Stage 1 and Stage 2 result, second measurement: Pranavz/Hearthfire-24B-heretic against LatitudeGames/Hearthfire-24B (2026-11-02)

Measured on Wheat, round 35 piece 3 (download job 387143, compare job 387146, sweep 387152; the pull carries the
measurements and the sweep record and no job log). Modified revision `6d3f74c1` (four commits on 2026-05-07
between 05:36Z and 05:41Z), the same ten shards round 29 measured against mistralai/Mistral-Small-3.2-24B-Instruct-2506,
the grandparent the `base_model` field names (finding 61). This pass pins the parent the README's title names,
LatitudeGames/Hearthfire-24B at `1b854cc8` (2025-12-19), a roleplay fine-tune of Mistral Small 3.2 under a ChatML
template. The card is unchanged: Heretic v1.2.0, `direction_index` per layer, the attention outputs at 3.75 centred
on 26.51 falling to 3.06 at distance 8.14, the down projections at 2.66 centred on 14.59 falling to 3.73 at distance
25.63, 2 refusals in 100 against 96, KL 0.5561 against Hearthfire. This is the reading of record for the copy; the
round 29 report (`results/weights/Pranavz-Hearthfire-24B-heretic.json`) stays as the record of what the field's pin
measures.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 2 flags (the
within-layer cosines of layers 27 and 25, 0.946 and 0.955), on the cluster and after re-scoring at home. On
reading, the copy is the Heretic edit its card describes and nothing else.

- 56 of 363 tensors changed: the down projections of all 40 layers and the attention outputs of layers 19 to 34
  (16). The attention kernel reaches 26.51 plus or minus 8.14, layers 19 to 34; the down kernel 14.59 plus or
  minus 25.63, every layer. Both windows read exactly. Hearthfire stores a flat causal model with 363 tensors, as
  the copy does, so no mapping was needed; the largest relative change outside the changed set is exactly 0, and
  the 226 matrices the first pass read at about one percent (the fine-tune) now read 0.
- One direction per layer, as the card says: the two writers of a layer agree at 0.946 to 0.998 and the layers
  mostly do not (between-layer median 0.14; the down projections' directions agree among themselves at a median
  0.59 and the attention outputs' at 0.87). First shares 0.9985 to 0.9995 on all 56, relative change 0.042 to
  0.075.
- The down kernel reads within 0.07 on 16 of 40 layers (3.07 at 3 against 3.14, 3.01 at 6 against 3.02, 2.71
  at 14 against 2.68, 3.59 at 38 against 3.64), within 0.20 on thirteen more, and under by 0.21 to 0.51 on layers
  1, 2, 11, 20, 21, 23 to 26 and 34; layer 0 reads 1.62 against 3.27. The attention heights scatter: 2.74 to 3.22
  on layers 19 and 30 to 33 against 3.11 to 3.45, and 1.13 to 1.86 on layers 20 to 29 and 34 against 3.12 to
  3.71, finding 46's scatter on a Mistral base.
- Rows moved 0.011 to 0.24 under no preservation claim (0.19 at layer 2, 0.24 at layer 35).

| Layer | Attention output: change, E1, left kept, read, kernel | Down projection: change, E1, left kept, read, kernel | Within-layer cosine |
| --- | --- | --- | --- |
| 0 | - | 0.0596, 0.9993, -0.62, 1.62, 3.27 | - |
| 4 | - | 0.0499, 0.9990, -2.08, 3.08, 3.10 | - |
| 9 | - | 0.0491, 0.9989, -1.92, 2.92, 2.89 | - |
| 14 | - | 0.0608, 0.9993, -1.71, 2.71, 2.68 | - |
| 19 | 0.0502, 0.9990, -1.74, 2.74, 3.11 | 0.0449, 0.9987, -1.79, 2.79, 2.84 | 0.998 |
| 22 | 0.0466, 0.9988, -0.60, 1.60, 3.37 | 0.0526, 0.9991, -1.80, 2.80, 2.97 | 0.987 |
| 26 | 0.0734, 0.9995, -0.40, 1.40, 3.71 | 0.0463, 0.9988, -1.72, 2.72, 3.14 | 0.967 |
| 29 | 0.0574, 0.9992, -0.15, 1.15, 3.54 | 0.0438, 0.9986, -2.13, 3.13, 3.26 | 0.954 |
| 31 | 0.0573, 0.9992, -2.22, 3.22, 3.37 | 0.0450, 0.9987, -2.21, 3.21, 3.35 | 0.994 |
| 34 | 0.0423, 0.9985, -0.86, 1.86, 3.12 | 0.0493, 0.9989, -2.26, 3.26, 3.47 | 0.990 |
| 38 | - | 0.0599, 0.9993, -2.59, 3.59, 3.64 | - |
| 39 | - | 0.0609, 0.9993, -2.48, 3.48, 3.68 | - |

The read is one minus the left kept fraction; the kernel is the card's weight at that layer.

Against round 29. The field's pin read 282 of 363 tensors changed (every linear with the embedding and the head),
347 flags and the kernels through the training; this pin reads 56, 2 flags and the kernels alone. Every kept
fraction the first pass read is the kept fraction this pass reads, to the second decimal: the down projections at
-0.61, -2.08, -1.71, -1.79, -1.72, -2.21, -2.27 and -2.60 on layers 0, 4, 14, 19, 26, 31, 34 and 38 then, and
-0.62, -2.08, -1.71, -1.79, -1.72, -2.21, -2.26 and -2.59 now; the attention outputs at -1.74, -0.40, -2.22 and
-0.86 on layers 19, 26, 31 and 34 in both. The saved leading vectors of the two passes agree at 1.000 on all 56
matrices, left and right: the fine-tune, at a median 1.2 percent of each matrix, did not move the leading direction
of a 4 to 7 percent edit by a measurable amount, and the first shares rose from 0.90 to 0.995 in round 29 to 0.9985 to 0.9995
once it left the comparison. The copy's ten shards share no checksum with Hearthfire's, as round 29 found.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, 1,013 fields, 1,000 of them one thing. Hearthfire's
`tokenizer_config.json` (177,216 bytes) declares the 1,000 control tokens of the Mistral vocabulary in its
`added_tokens_decoder`, with `<|im_start|>` (id 998) as an additional special token and a separate
`special_tokens_map.json`; the copy's (376 bytes) declares none of them, and its `tokenizer.json` is 155 bytes
longer than Hearthfire's, so the shared-token-file rule of finding 44 cannot read the dropped declarations against
one shared file. The four special tokens moved into the tokenizer configuration are explained as a re-save, as are
`pad_token_id` on the configuration and the version strings (4.57.1 to 5.8.0); `rope_parameters` closed at home,
where transformers 5.22.1 loads both forms as the same value, and `rope_theta` remains as its mirror. The 292-byte
ChatML template is the same file on both sides and the fixed conversation renders identically. Round 29's 1,027
fields against the Mistral release were the fine-tune's tokenizer against `tekken.json`; against the fine-tune the
differences are the exporter's.

## For the recipe library

The directional-per-layer entry is the right one and its two cosine flags are the solver's, at 0.95 where the rule
asks 0.96. The pair is the clearest case the census has of a fine-tune cancelling out of a comparison: 226
matrices at one percent become exactly 0 and the ablation's numbers do not move. The pinner now records a
`card_parent` from the README's first sentence, which is how this pair was pinned. The direction vectors stay in the
pull copy at `/opt/ai/hpc-packages/pulls/model-audit/wheat35/measurements/pair-3/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
