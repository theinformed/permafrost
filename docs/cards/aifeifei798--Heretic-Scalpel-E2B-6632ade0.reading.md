# Reading of the Stage 1 and Stage 2 result: aifeifei798/Heretic-Scalpel-E2B against google/gemma-4-E2B-it (2026-10-31)

Measured on Nautilus, round 16 piece 6 (push card 5433, round card 5434, download job 4120061, compare job 4120067 on
the background queue, sweep 4120069; pulled home by card 5467). Modified revision `49bd7340` (2026-09-25, a README
commit; the repository was created on 2026-09-24 and the weight shards uploaded that day, beside a file named
`patch_shared_kv_weights.safetensors`), original pinned at `3e22461f` (2026-07-20; one weight file, shard `2db5482b`,
the file round 8's E2B pair also stood on). The maker's card (35 KB) describes a four-stage pipeline on top of a
Heretic ablation of the original: a "singular value topology surgery" that reconstructs the shared key-value
projections of layers 15 to 34, then three rounds of supervised fine-tuning (one with 70 percent token permutation,
one on physics text, one on causal and "zero-hedging" answers). It gives no ablation parameters and no refusal or
divergence numbers.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection-selected`, 237 flags, on the cluster
and after re-scoring at home: 117 unexpected changes, 62 cross-layer cosines, 57 first energy shares and one
cross-kind direction. On reading, the copy carries a per-layer ablation of rank one to three on the residual writers
of the upper half of the model, a small merged training on every projection, and nothing at all on the shared
key-value tensors the card says it reconstructed.

- 179 of 2,011 tensors changed: 34 attention outputs, 28 down projections, 29 query, 9 key, 15 value, 32 gate and 32 up
  projections. The largest relative change outside the changed set is 0.000998 (26 tensors sit between 0.0009 and
  0.001, the training at the threshold); outside the recipe's set it is 0.0027.
- The ablation: the attention outputs of layers 10 to 34 (relative change 0.021 to 0.058) and the down projections of
  layers 15 to 34 (0.030 to 0.041). Layers 10 to 13 of the attention outputs and 15 to 18 of the down projections are
  rank one (first share 0.980 to 0.997). From layer 14 the attention outputs carry two or three directions: first
  share 0.43 to 0.74 with the first eight at 0.997, singular values such as 2.33, 1.70 and 0.10 at layer 15, 2.28,
  1.93 and 1.09 at layer 25, 2.49, 2.24 and 1.40 at layer 34. The down projections of layers 19 to 29 carry two (first
  share 0.69 to 0.76) and layers 30 to 34 nearly one (0.94 to 0.96). The directions are per layer (cross-layer cosine
  0.03 to 0.71, median 0.28 on the attention outputs and 0.42 on the down projections; within-layer 0.25 to 0.76).
- Along the leading output direction the copy keeps −0.38 to 0.67 of the original's action on the left of the
  attention outputs and −0.24 to 0.01 on the down projections, −0.37 to 0.04 along the second direction where one is
  present and 0.24 to 0.38 along the third: not one weight, as a multi-direction edit need not be. The right
  fractions read −0.04 to 0.70, above the left on 42 of the 45 ablated matrices (output side). Row norms moved by 0.004 to 0.018.
- The training: the attention outputs of layers 0, 1 and 3 to 9, the down projections of layers 7 to 14, and 117
  reading-side, gate and up projections moved by 0.10 to 0.27 percent with first shares of 0.11 to 0.50, first eight
  0.33 to 0.70, 0.99 to 1.01 of the original kept, row norms within 0.0007 (0.014 on one key projection): a small
  merged change, in line with three rounds of fine-tuning.
- The shared key-value tensors: the key and value projections and key normalisations of layers 15 to 34 (71 tensors)
  read a relative difference of exactly 0. The card's first stage reconstructs them from an earlier state; whatever
  it wrote, the published file carries Google's values bit for bit, and the changed key and value projections (9
  and 15) are all in layers 0 to 14, where the model computes its own.

The attention outputs:

| Layer | Relative change | E1 | E8 | Left, direction 1 | Right, direction 1 | Row norms | Cross-layer cosine | Within-layer cosine |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0.001 | 0.329 | 0.443 | 1.00 | 1.00 | 0.0001 | 0.03 | 0.037 |
| 1 | 0.001 | 0.214 | 0.380 | 1.00 | 1.00 | 0.0001 | 0.08 | 0.014 |
| 3 | 0.001 | 0.335 | 0.467 | 1.00 | 1.00 | 0.0001 | 0.08 | 0.385 |
| 4 | 0.001 | 0.276 | 0.411 | 1.00 | 1.00 | 0.0001 | 0.09 | 0.368 |
| 5 | 0.001 | 0.320 | 0.453 | 1.00 | 1.00 | 0.0001 | 0.14 | 0.459 |
| 6 | 0.001 | 0.374 | 0.501 | 1.00 | 1.00 | 0.0001 | 0.05 | 0.481 |
| 7 | 0.001 | 0.237 | 0.450 | 1.00 | 1.00 | 0.0001 | 0.15 | 0.656 |
| 8 | 0.002 | 0.293 | 0.489 | 1.00 | 1.00 | 0.0001 | 0.18 | 0.433 |
| 9 | 0.001 | 0.298 | 0.491 | 1.00 | 1.00 | 0.0001 | 0.15 | 0.545 |
| 10 | 0.032 | 0.995 | 0.996 | -0.19 | 0.49 | 0.0059 | 0.05 | 0.302 |
| 11 | 0.023 | 0.986 | 0.990 | 0.12 | 0.70 | 0.0065 | 0.08 | 0.291 |
| 12 | 0.024 | 0.985 | 0.990 | 0.14 | 0.70 | 0.0083 | 0.04 | 0.253 |
| 13 | 0.021 | 0.980 | 0.986 | 0.51 | 0.67 | 0.0070 | 0.09 | 0.258 |
| 14 | 0.043 | 0.739 | 0.997 | -0.16 | 0.21 | 0.0068 | 0.07 | 0.353 |
| 15 | 0.055 | 0.650 | 0.998 | 0.55 | 0.38 | 0.0104 | 0.15 | 0.555 |
| 16 | 0.050 | 0.546 | 0.997 | -0.31 | 0.36 | 0.0123 | 0.30 | 0.479 |
| 17 | 0.049 | 0.543 | 0.997 | -0.36 | 0.38 | 0.0099 | 0.36 | 0.531 |
| 18 | 0.052 | 0.562 | 0.998 | -0.34 | 0.42 | 0.0145 | 0.36 | 0.491 |
| 19 | 0.056 | 0.587 | 0.998 | -0.35 | 0.36 | 0.0183 | 0.38 | 0.382 |
| 20 | 0.053 | 0.545 | 0.998 | -0.22 | 0.47 | 0.0122 | 0.36 | 0.472 |
| 21 | 0.052 | 0.509 | 0.997 | -0.36 | 0.47 | 0.0087 | 0.42 | 0.561 |
| 22 | 0.058 | 0.505 | 0.997 | -0.00 | 0.46 | 0.0154 | 0.39 | 0.436 |
| 23 | 0.055 | 0.497 | 0.997 | -0.34 | 0.35 | 0.0137 | 0.09 | 0.720 |
| 24 | 0.056 | 0.488 | 0.997 | -0.38 | 0.33 | 0.0133 | 0.37 | 0.704 |
| 25 | 0.053 | 0.512 | 0.997 | -0.15 | 0.38 | 0.0120 | 0.64 | 0.550 |
| 26 | 0.054 | 0.523 | 0.997 | 0.23 | 0.51 | 0.0139 | 0.67 | 0.617 |
| 27 | 0.057 | 0.520 | 0.997 | 0.67 | 0.50 | 0.0116 | 0.62 | 0.682 |
| 28 | 0.056 | 0.486 | 0.997 | 0.50 | 0.54 | 0.0116 | 0.66 | 0.564 |
| 29 | 0.054 | 0.428 | 0.997 | 0.41 | 0.33 | 0.0091 | 0.52 | 0.466 |
| 30 | 0.056 | 0.495 | 0.997 | 0.17 | 0.43 | 0.0096 | 0.63 | 0.547 |
| 31 | 0.053 | 0.476 | 0.997 | -0.31 | 0.53 | 0.0095 | 0.26 | 0.751 |
| 32 | 0.053 | 0.459 | 0.997 | -0.10 | 0.42 | 0.0095 | 0.38 | 0.525 |
| 33 | 0.053 | 0.490 | 0.997 | -0.32 | 0.59 | 0.0096 | 0.46 | 0.448 |
| 34 | 0.048 | 0.469 | 0.996 | -0.16 | 0.37 | 0.0136 | 0.48 | 0.639 |

The down projections:

| Layer | Relative change | E1 | E8 | Left, direction 1 | Right, direction 1 | Row norms | Cross-layer cosine | Within-layer cosine |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | 0.001 | 0.275 | 0.402 | 1.00 | 1.00 | 0.0000 | 0.12 | 0.649 |
| 8 | 0.001 | 0.274 | 0.411 | 1.00 | 1.00 | 0.0001 | 0.14 | 0.492 |
| 9 | 0.001 | 0.321 | 0.438 | 1.00 | 1.00 | 0.0001 | 0.12 | 0.535 |
| 10 | 0.001 | 0.346 | 0.484 | 1.00 | 1.00 | 0.0001 | 0.06 | 0.333 |
| 11 | 0.001 | 0.313 | 0.475 | 1.00 | 1.00 | 0.0001 | 0.11 | 0.339 |
| 12 | 0.002 | 0.339 | 0.512 | 1.00 | 1.00 | 0.0001 | 0.14 | 0.338 |
| 13 | 0.002 | 0.437 | 0.542 | 1.00 | 1.00 | 0.0001 | 0.05 | 0.306 |
| 14 | 0.001 | 0.391 | 0.510 | 1.00 | 1.00 | 0.0001 | 0.09 | 0.365 |
| 15 | 0.031 | 0.996 | 0.997 | -0.01 | 0.28 | 0.0060 | 0.24 | 0.540 |
| 16 | 0.030 | 0.996 | 0.997 | -0.04 | 0.21 | 0.0067 | 0.27 | 0.437 |
| 17 | 0.030 | 0.996 | 0.997 | -0.03 | 0.21 | 0.0083 | 0.29 | 0.551 |
| 18 | 0.033 | 0.997 | 0.997 | -0.09 | 0.36 | 0.0078 | 0.33 | 0.529 |
| 19 | 0.040 | 0.697 | 0.995 | -0.04 | 0.31 | 0.0137 | 0.37 | 0.457 |
| 20 | 0.039 | 0.689 | 0.995 | -0.11 | 0.18 | 0.0090 | 0.43 | 0.504 |
| 21 | 0.037 | 0.717 | 0.995 | -0.13 | 0.11 | 0.0061 | 0.42 | 0.545 |
| 22 | 0.038 | 0.709 | 0.995 | -0.12 | 0.09 | 0.0084 | 0.46 | 0.535 |
| 23 | 0.041 | 0.737 | 0.996 | -0.15 | 0.07 | 0.0094 | 0.55 | 0.714 |
| 24 | 0.039 | 0.709 | 0.995 | -0.16 | 0.09 | 0.0112 | 0.65 | 0.708 |
| 25 | 0.037 | 0.719 | 0.995 | -0.13 | 0.01 | 0.0092 | 0.70 | 0.590 |
| 26 | 0.036 | 0.720 | 0.994 | -0.11 | -0.01 | 0.0092 | 0.71 | 0.635 |
| 27 | 0.037 | 0.730 | 0.995 | -0.07 | -0.00 | 0.0083 | 0.71 | 0.662 |
| 28 | 0.038 | 0.747 | 0.995 | -0.19 | -0.03 | 0.0059 | 0.71 | 0.568 |
| 29 | 0.039 | 0.761 | 0.995 | -0.20 | -0.04 | 0.0069 | 0.71 | 0.417 |
| 30 | 0.035 | 0.937 | 0.996 | -0.24 | -0.03 | 0.0041 | 0.67 | 0.523 |
| 31 | 0.035 | 0.944 | 0.996 | -0.22 | -0.03 | 0.0043 | 0.65 | 0.755 |
| 32 | 0.035 | 0.952 | 0.996 | -0.22 | -0.01 | 0.0047 | 0.59 | 0.553 |
| 33 | 0.035 | 0.959 | 0.996 | -0.19 | -0.02 | 0.0041 | 0.54 | 0.399 |
| 34 | 0.030 | 0.954 | 0.995 | 0.01 | 0.12 | 0.0074 | 0.48 | 0.649 |

Against llmfan46's E2B copy of round 8, on the same original file, no changed matrix has an equal measurement in
any field.

## Token and configuration side (Stage 1)

The cluster's card read "unexplained differences" in 30 fields; the home judgement under transformers 5.6.2 closed
one (`config.text_config.moe_intermediate_size`, the 5.6.2 default, as on round 12's pairs 1 and 2) and keeps the
rest, so the committed card reads "unexplained differences"; the reading closes them by hand as the marks of one
save under an older library.

- `config.transformers_version` absent, `config.dtype` absent with `config.torch_dtype` (the old key) present at
  every level, and `config.text_config.per_layer_config` written out with `head_dim` 512 for layers 4, 9, 14, 19, 24,
  29 and 34: the signature of the loader that round 7 and 8 met on E2B and E4B copies (finding 15), which writes the
  model's resolved configuration back under pre-5 key names. The values are the original's.
- `generation.eos_token_id` [1, 106, 50] on the original, [1, 1, 1, 1, 106, 50] on the copy: the same set with the
  end token repeated, written by the same loader; no token moved.
- `added_tokens.decoder` and the 24 `special_tokens.added_tokens_decoder` fields: the copy's `tokenizer_config.json`
  lists the 24 control tokens in an `added_tokens_decoder` block where Google's does not; the ids and strings equal
  the original's. A re-save of the tokenizer.
- `template_source.tokenizer_config`: the copy carries the template twice, in `chat_template.jinja` and inside
  `tokenizer_config.json`, and both equal Google's pinned template byte for byte (18,567 bytes, Google's 2026-07-15
  template carried unchanged to the pin). The fixed conversation renders identically. A re-save that wrote the
  template into the tokenizer configuration as older libraries do.

## Token side and weights together

Every token-side difference is a save artefact and the template is Google's; the weight side is where the card's
claims are tested, and the one checkable claim (reconstructed shared key-value tensors) reads as no change.

## For the recipe library

Not an entry: a per-layer ablation of rank one to three on the attention outputs of layers 10 to 34 and the down
projections of layers 15 to 34, with a small merged training on every projection. The first multi-direction
ablation in the census, and the energy-share rule reads its second and third directions as violations by design.
The saved direction vectors are not committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/nautilus16/measurements/pair-6/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
