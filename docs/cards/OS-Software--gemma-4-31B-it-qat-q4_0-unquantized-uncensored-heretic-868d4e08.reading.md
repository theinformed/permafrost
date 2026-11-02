# Reading of the Stage 1 and Stage 2 result: OS-Software/gemma-4-31B-it-qat-q4_0-unquantized-uncensored-heretic against google/gemma-4-31B-it-qat-q4_0-unquantized (2026-11-02)

Measured on Nautilus, round 36 piece 4 (download job 4167620, compare job 4167624, sweep 4167629; the pull carries
the measurements and the sweep record and no job log). Modified revision `244246e6` (five commits on 2026-09-08
between 03:43Z and 03:48Z: the model, tokenizer, processor and README; the maker's 12B export of piece 5 came the
evening before), original pinned at `1e4d8bee` (07-20, the checkpoint's `response_template` commit, the revision
current when the repository was created). The card (32,499 bytes) is Heretic v2's page: `start_layer_index` 30,
`end_layer_index` 41, `preserve_good_behavior_weight` 1.0, `steer_bad_behavior_weight` 0.0001,
`overcorrect_relative_weight` 1.0, `neighbor_count` 1, `ridge_regularization` 1.36e-06, `transport_rank` 4,
`entropy_regularization` 0.1, `transport` gaussian, `lora_rank` 128, `row_normalization` none,
`target_components` `attn.o_proj, mlp.down_proj`, `covariance_regularization` 0.01, `max_weight_change` 1.0, 0
refusals in 100 against 100, KL divergence 0.0083. The `base_model` field names google/gemma-4-31B-it; the
README's first sentence names the QAT checkpoint, and the pinner paired by the name (finding 48). The maker's
fifth copy in the census and the third rank-four export after the E4B (round 30, finding 42) and the 26B-A4B QAT
(round 32).

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 44 flags (22
first shares of 0.549 to 0.959 and 22 within-layer cosines of 0.003 to 0.147), on the cluster and after
re-scoring at home. On reading, the copy is the maker's rank-four transport edit on a third base, the card's
window on both writers.

- 22 of 1,188 tensors changed: the attention outputs and down projections of layers 30 to 40, the card's window
  with its exclusive end. Nothing else moved; the largest relative change outside the changed set is exactly 0
  and 1,166 tensors equal the original, which places the copy on the QAT checkpoint and not on the instruct
  model its field names (finding 48).
- Rank four exactly: fourth cumulative shares 0.993 to 0.998, where the first share alone is 0.549 to 0.832 on
  the down projections and 0.798 to 0.959 on the attention outputs.
- Input side on all 22 (the left kept fraction above the right on every matrix). Read as weights along the
  leading input direction, 0.86 to 2.05 on the down projections (median 1.63; 0.86 and 0.89 at layers 30 and 31,
  partial removals) and 0.99 to 2.39 on the attention outputs (median 1.61; 2.39 at layer 35).
- The two writers of a layer take unrelated directions (within-layer cosines 0.003 to 0.147) and the layers
  agree at 0.29 to 0.53 with their group reference.
- Rows moved 0.0012 to 0.0066 on the down projections and 0.0041 to 0.0372 on the attention outputs, under the
  card's `row_normalization` none.

| Layer | Writer | Change | E1 | E4 | Left kept | Right kept | Weight read | Rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 30 | down | 0.0182 | 0.832 | 0.993 | 0.91 | 0.14 | 0.86 | 0.0015 |
| 30 | attention | 0.0361 | 0.939 | 0.998 | 0.82 | -0.19 | 1.19 | 0.0082 |
| 33 | down | 0.0203 | 0.645 | 0.994 | 0.84 | -0.55 | 1.55 | 0.0019 |
| 33 | attention | 0.0317 | 0.877 | 0.997 | 0.93 | -0.54 | 1.54 | 0.0065 |
| 35 | down | 0.0228 | 0.685 | 0.995 | 0.91 | -0.60 | 1.60 | 0.0025 |
| 35 | attention | 0.0350 | 0.954 | 0.998 | 0.99 | -1.39 | 2.39 | 0.0286 |
| 40 | down | 0.0250 | 0.661 | 0.996 | 0.93 | -1.05 | 2.05 | 0.0066 |
| 40 | attention | 0.0377 | 0.959 | 0.998 | 0.94 | -1.02 | 2.02 | 0.0372 |

The full table (22 rows) is in the report.

Directions. Against the saved vectors of twenty-three 31B measurements on the shared names, the leading left
vectors stand at 0.56 or less to every edit (Bahushruth's 0.56 on 22 shared, the arbitrary-rank edits 0.37 to
0.41) and the leading right vectors at 0.65 to 0.77 to the five arbitrary-rank edits of the 31B and its QAT
checkpoint (llmfan46's two, coder3101's two, MoonRide's two at 0.66 to 0.68), 0.47 to Bahushruth's and 0.33 to
wnfldchen's, with the kernel and projection edits at 0.23 or less: the rank-four edit's leading input direction
shares two thirds of its cosine with the arbitrary-rank family's, its output direction does not (finding 90).
The thirteen shards (a smaller shard size than the original's two) equal no measured file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, three fields: the 5.16.1 save moved `global_head_dim` 512
and `num_global_key_value_heads` 4 out of `text_config` into a `per_layer_config` map under the ten global layers,
the form finding 39 has read on the 31B since 3MPER0RR's copy, closed by hand; the version strings (5.6.2 to
5.16.1) are a re-save; the template is the pin's 07-20 file and renders identically.

## For the recipe library

The directional-per-layer entry is the nearest and its 44 flags are the four directions per matrix and the
unrelated writers; a rank-stated subspace entry (first-k share with k from the singular values, no within-layer
rule) would read the copy as a clean match, as finding 42 asked. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus36/measurements/pair-4/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
