# Reading of the Stage 1 and Stage 2 result: OS-Software/gemma-4-E4B-it-uncensored-heretic against google/gemma-4-E4B-it (2026-10-31)

Measured on Wheat, round 30 piece 3 (probe job 386940, download job 386942, compare job 386945, 608 seconds, sweep
386951), without the container image, under a standalone Python 3.11.18. Modified revision `59a70a7b` (2026-09-15 at
04:00Z, the README commit; the repository was created at 03:57Z and the weights uploaded at 04:00Z), original pinned
at `ee0ef602` (2026-07-20). The card names Heretic "v2.0.0.dev0+custom" and prints a parameter table the census has
not seen before: `start_layer_index` 18, `end_layer_index` 28, `transport` gaussian with `transport_rank` 4,
`preserve_good_behavior_weight` 1.0, `steer_bad_behavior_weight` 0.0001, `overcorrect_relative_weight` 1.5,
`neighbor_count` 1, `ridge_regularization` 1e-07, `entropy_regularization` 0.1, `covariance_regularization` 0.01,
`lora_rank` 128, `max_weight_change` 1.0, `row_normalization` none, targets `attn.o_proj` and `mlp.down_proj`. It
reports 0 refusals in 100 against 99 for the original and a KL divergence of 0.0070. The repository's `base_model`
field names the pretrained google/gemma-4-E4B; the card and the pin name the instruct model.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 40 flags, on the
cluster and after re-scoring at home: 20 first shares of 0.587 to 0.883 and 20 within-layer cosines of 0.005 to 0.147,
on every changed matrix. On reading, the copy is a rank-four edit on the attention output and the down projection of
ten layers, input side, with no row restoration, which is the card's table read off the weights.

- 20 of 2,076 tensors changed: the attention outputs and the down projections of layers 18 to 27, the ten layers
  from `start_layer_index` 18 up to and excluding `end_layer_index` 28. Nothing else moved; the largest relative
  change outside the changed set is exactly 0 and 2,056 tensors equal the original. The 54 key and value tensors the
  original carries for layers 24 to 41 and the copy omits are the shared-key-value layers the configuration declares
  (`num_kv_shared_layers` 18), as on Madras1's copy in round 16; they are not flags.
- Rank four exactly: the fourth cumulative share is 0.999 to 1.000 on all 20 matrices and the fifth singular value is
  0 to the sketch's precision, where the first share alone is 0.59 to 0.88 and the first four singular values stand at
  1.0, 0.31 to 0.66, 0.04 to 0.44 and 0.01 to 0.30 of the first. The card's `transport_rank` is 4. The third rank-stated
  subspace edit in the census after null-space's eight directions (finding 29) and AEON-7's four (finding 34), and
  the first whose rank is a hard cut: the fifth singular value is 0 where AEON-7's dropped by 19 to 195 times.
- Input side on all 20: the left kept fraction is 0.49 to 0.94 and the right −0.08 to −1.26, the left above the right
  on every matrix. Along the right direction the copy keeps −0.22 to −1.26 of the original's action on the down
  projections (a weight of 1.08 to 2.26) and −0.22 to 0.50 on the attention outputs (0.50 to 2.02); the weights
  rise with depth on the down projections (1.08 at layer 22 to 2.26 at 26).
- The two writers of a layer take unrelated directions (cosine 0.005 to 0.147), and across layers the directions
  agree at 0.21 to 0.42 with the group reference, a per-matrix transport with no shared direction.
- Rows moved by 0.012 to 0.098, largest on the attention outputs of layers 24 and 27, under `row_normalization`
  none.
- Relative changes of 0.052 to 0.068 on the down projections and 0.088 to 0.142 on the attention outputs, three to
  five times the rank-one Heretic edits of this base (llmfan46's 0.02 to 0.04).
- Tenth measurement on the E4B weight file (shard `cfbd3d2f`, pinned at `ee0ef602` where the eight earlier ones used
  `3555bddc` or earlier revisions of the same shard), saved again in four shards. No changed matrix has an equal
  measurement in any field of the nine others.

| Layer | Attention output: change, E1, E8, left kept, right kept | Down projection: change, E1, E8, left kept, right kept | Weight read | Within-layer cosine | Cross-layer cosine | Row norms |
| --- | --- | --- | --- | --- | --- | --- |
| 18 | 0.1201, 0.841, 1.000, 0.85, -0.22 | 0.0613, 0.778, 0.999, 0.85, -0.51 | 1.22/1.51 | 0.094 | 0.25/0.29 | 0.0639, 0.0179 |
| 19 | 0.0940, 0.821, 1.000, 0.87, 0.50 | 0.0556, 0.765, 0.999, 0.80, -0.42 | 0.50/1.42 | 0.010 | 0.22/0.30 | 0.0587, 0.0121 |
| 20 | 0.0910, 0.751, 1.000, 0.94, 0.21 | 0.0623, 0.781, 0.999, 0.89, -0.80 | 0.79/1.80 | 0.005 | 0.28/0.30 | 0.0472, 0.0171 |
| 21 | 0.0879, 0.668, 1.000, 0.86, 0.26 | 0.0616, 0.781, 0.999, 0.89, -0.31 | 0.74/1.31 | 0.021 | 0.21/0.29 | 0.0371, 0.0240 |
| 22 | 0.1279, 0.820, 1.000, 0.87, 0.48 | 0.0616, 0.883, 0.999, 0.85, -0.08 | 0.52/1.08 | 0.043 | 0.27/0.29 | 0.0789, 0.0430 |
| 23 | 0.0889, 0.793, 1.000, 0.71, -0.55 | 0.0679, 0.844, 0.999, 0.87, -0.22 | 1.55/1.22 | 0.147 | 0.28/0.33 | 0.0446, 0.0270 |
| 24 | 0.1418, 0.807, 1.000, 0.59, -0.59 | 0.0562, 0.761, 0.999, 0.84, -0.95 | 1.59/1.95 | 0.097 | 0.42/0.38 | 0.0961, 0.0199 |
| 25 | 0.1121, 0.688, 1.000, 0.49, -0.49 | 0.0598, 0.637, 0.999, 0.84, -1.22 | 1.49/2.22 | 0.067 | 0.38/0.30 | 0.0521, 0.0260 |
| 26 | 0.1025, 0.850, 1.000, 0.66, -0.40 | 0.0552, 0.615, 0.999, 0.86, -1.26 | 1.40/2.26 | 0.046 | 0.26/0.31 | 0.0532, 0.0230 |
| 27 | 0.1085, 0.846, 1.000, 0.83, -1.02 | 0.0520, 0.587, 0.999, 0.81, -0.98 | 2.02/1.98 | 0.011 | 0.30/0.32 | 0.0983, 0.0118 |

The weight column reads one minus the right kept fraction, the input side.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster, four fields; three at home. The two version strings (5.5.0.dev0 to 5.16.1)
close as a re-save, and `text_config.moe_intermediate_size` closes at home under transformers 5.22.1 (absent on one
side, loading to the same value on both). The three open fields are the 5.16 save form finding 39 met on 3MPER0RR's
31B and 12B copies: `global_head_dim` 512 and `num_global_key_value_heads` leave the text configuration and return
as a `per_layer_config` map under the global layers' indices (5, 11, 17, 23, 29, 35, 41). Closed by hand, the third
time. The template is Google's file at the pin (18,567 bytes rendered, `0a2c8073`) saved again with 386 more bytes
(`c0e1a4e7`), the fixed conversation renders identically, and the tokenizer configuration grew from 3,082 to 3,871
bytes in the same save.

## For the recipe library

A new Heretic method: a rank-four "transport" on a layer window, input side, no row restoration, every parameter in
the card readable from the weights (window, rank, components) except the five regularisation and weighting numbers,
which set the search and not the shape. The `arbitrary-rank` entry's candidate line (input side, one weight per
layer, a tail of weak directions) does not fit: the rank is a hard four, the weights are per matrix, and the two
writers of a layer are unrelated. A `transport-rank-k` entry would say: a window of layers on both writers; first-k
share at least 0.99 with k read from the singular values; left above right; within-layer agreement unconstrained;
rows unrestored. The pull copy keeps the direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/wheat30/measurements/pair-3/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
