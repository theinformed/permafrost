# Reading of the Stage 1 and Stage 2 result: llmfan46/Magistral-Small-2509-ultra-uncensored-heretic-v1 against mistralai/Magistral-Small-2509 (2026-11-01)

Measured on Nautilus, round 20 piece 7 (download job 4143641, compare job 4143648, 1,271 seconds, sweep 4143650).
Modified revision `b14b7d44` (eleven commits from 2026-03-17 22:00Z to 03-27 22:51Z: the weights at 22:04Z on the
first day, the tokenizer, the README, six more files at 22:28Z, and six README edits after), original pinned at
`a31cc96a` (2025-09-17), the revision the two copies of round 18 were measured against. The card prints the
Heretic 1.2.0 record with Arbitrary-Rank Ablation: start layer 16, end layer 27, a KL divergence of 0.0274 and 5
refusals in 100 against the original. It is the maker's first Magistral copy; the v2 measured in round 18 came
later and reaches further.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 32 flags, on the
cluster and after re-scoring at home: 18 first shares of 0.75 to 0.96 on every edited matrix and 14 within-layer
cosines of 0.003 to 0.12 on the seven layers with both writers edited, counted on both. On reading, the footprint
is the card's window, the edits are multi-direction on the input side, and the directions are unrelated per
matrix: the shape of the maker's other arbitrary-rank copies (finding 22).

- 18 of 585 tensors changed: the attention outputs of layers 16 to 22 (7 matrices) and the down
  projections of layers 16 to 26 (11), inside the card's 16-to-27 window of a 40-layer model. The largest relative
  change outside the changed set is 0.00029, on the attention outputs of layers 23 to 26, the rest of the
  window on that writer, which the search weighted to nothing and the tool's threshold leaves as unchanged;
  everything outside the window equals the original.
- Not rank one: first share 0.75 to 0.96, fourth cumulative share 0.90 to 0.98, the fifth singular value 0.03 to
  0.16 of the first. A sum of a few directions per matrix.
- Input side on all 18: the left kept fraction is 0.35 to 0.80 on the attention outputs and 0.74 to 0.90 on the
  down projections, the right -0.29 to -1.43 and -0.29 to -1.20; the left is above the right on 18 of 18. The
  weights along the right direction are 1.55 to 2.43 on the attention outputs (2.43 at layer 22) and 1.29 to 2.20
  on the down projections (2.20 at 26).
- The directions agree with the group reference at 0.22 to 0.56 and within a layer at 0.003 to 0.12: unrelated
  per matrix, one search result each.
- Rows moved by 0.003 to 0.027 on the attention outputs and 0.0005 to 0.0018 on the down projections; no
  preservation claim on the card.
- Relative changes of 0.032 to 0.054 on the attention outputs and 0.012 to 0.020 on the down projections.

| Layer | Attention output: change, E1, E4, left kept, right kept | Down projection: change, E1, E4, left kept, right kept | Weight read | Within-layer cosine | Cross-layer cosine | Row norms |
| --- | --- | --- | --- | --- | --- | --- |
| 16 | 0.0325, 0.949, 0.977, 0.60, -0.95 | 0.0124, 0.902, 0.929, 0.89, -0.63 | 1.95/1.63 | 0.110 | 0.31/0.33 | 0.0041, 0.0006 |
| 17 | 0.0392, 0.748, 0.912, 0.56, -0.93 | 0.0137, 0.910, 0.925, 0.90, -0.75 | 1.93/1.75 | 0.110 | 0.51/0.25 | 0.0031, 0.0009 |
| 18 | 0.0375, 0.960, 0.976, 0.66, -0.76 | 0.0181, 0.875, 0.935, 0.83, -0.79 | 1.76/1.79 | 0.120 | 0.42/0.22 | 0.0268, 0.0018 |
| 19 | 0.0327, 0.872, 0.955, 0.58, -0.86 | 0.0121, 0.902, 0.926, 0.85, -0.43 | 1.86/1.43 | 0.096 | 0.40/0.29 | 0.0035, 0.0005 |
| 20 | 0.0406, 0.916, 0.975, 0.58, -0.73 | 0.0146, 0.828, 0.901, 0.82, -0.62 | 1.73/1.62 | 0.039 | 0.56/0.24 | 0.0125, 0.0008 |
| 21 | 0.0317, 0.951, 0.981, 0.80, -0.55 | 0.0132, 0.936, 0.953, 0.84, -0.52 | 1.55/1.52 | 0.003 | 0.45/0.24 | 0.0039, 0.0007 |
| 22 | 0.0540, 0.846, 0.951, 0.35, -1.43 | 0.0168, 0.895, 0.937, 0.79, -0.79 | 2.43/1.79 | 0.014 | 0.24/0.25 | 0.0175, 0.0012 |
| 23 | - | 0.0145, 0.951, 0.964, 0.84, -0.29 | -/1.29 | - | -/0.26 | -, 0.0009 |
| 24 | - | 0.0158, 0.891, 0.933, 0.79, -0.85 | -/1.85 | - | -/0.24 | -, 0.0010 |
| 25 | - | 0.0143, 0.917, 0.938, 0.83, -0.71 | -/1.71 | - | -/0.25 | -, 0.0008 |
| 26 | - | 0.0202, 0.828, 0.916, 0.74, -1.20 | -/2.20 | - | -/0.24 | -, 0.0015 |

The weight column reads one minus the right kept fraction on both writers.

The fingerprint shares no measured field with the two earlier reports on this original. The maker's v2 (round 18)
changed 49 tensors across layers 9 to 36 with weights of 1.69 to 4.71; this v1 changed 18 across 16 to 26 with
1.29 to 2.43, a narrower window and a lighter hand, and none of its values.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster, 1,022 fields, 1,021 at home. The original ships `tekken.json` and no
library tokenizer, configuration or template (finding 31); the copy carries unsloth's conversion of the same
original, as the maker's v2 and grayarea's copy do, and the tool counts the whole added table against nothing:
the 1,000 special tokens, the five special-token fields of the map and the four of the tokenizer configuration,
the three ids at two levels, the vocabulary sizes, the added tokens, the template and the conversion's
`unsloth_fixed`. One field closed by tool at home: `text_config.rope_parameters`, written by a 5.3.0 save and
absent from the 4.56.1 original, loads to the same default under 5.22.1, with `rope_theta` and the two
`tie_word_embeddings` fields it had already closed. `vision_config.rope_parameters` stays open, the same
rename on the vision side, where the rule does not reach. The fixed conversation renders identically with the
conversion's template on both sides, since the original has none of its own.

## For the recipe library

The maker's arbitrary-rank shape on a fourth original: input side, a few directions per matrix, unrelated between
the two writers of a layer, the kernel's window to the layer and its interior weights not in any printed kernel,
with the attention outputs of the window's last four layers touched under the threshold. The `arbitrary-rank`
candidate entry of finding 22 fits it without a flag if the within-layer cosine line is dropped for that entry.
The pull copy keeps the direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus20/measurements/pair-7/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
