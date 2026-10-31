# Reading of the Stage 1 and Stage 2 result: lemuralabs/Gemma-4-12B-uncensored-bf16 against google/gemma-4-12B-it (2026-10-31)

Measured on Nautilus, round 16 piece 3 (push card 5433, round card 5434, download job 4120061, compare job 4120064 on
the background queue, sweep 4120069; pulled home by card 5467). Modified revision `20201d2b` (2026-08-05, the
repository's one commit; it was created on 2026-06-04), original pinned at `66bc78a7` (2026-06-03; one weight file,
shard `5a84cb31`, the same file round 8 measured two 12B copies against). The maker's card calls the copy a
"full-precision (bf16) abliterated google/gemma-4-12B-it", draws a lineage of one step from Google to this repository
("ablation 1.3.0, directional ablation, Optuna/TPE-optimized over 100 trials, best Pareto trial #55"), reports 12
refusals in 100 against 99 and a KL divergence of 0.053, says "no new capabilities were added", and sets
`base_model_relation` to finetune.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection`, 592 flags, on the cluster and after
re-scoring at home: 457 unexpected changes, 96 first energy shares, 38 cross-layer cosines and one cross-kind
direction. On reading, the copy carries two things, a dense change in every projection and most normalisation
vectors and a shared-direction ablation on top of it, and the dense change is yuxinlu1's coding fine-tune of this
base, which the card does not name.

- 553 of 677 tensors changed: every query (47), key (47), value (40), gate (47), up (47), attention output (48) and
  down projection (48), 32 input normalisations, 35 post-attention normalisations, the final normalisation and 161
  of the per-layer scalars and extra normalisations classed "other". The 124 unchanged tensors are the token
  embedding, the vision tower and normalisation vectors that moved under the 0.001 threshold; the largest relative
  change outside the changed set is 0.00099.
- The dense part is training: the reading-side projections and the gate and up projections moved by 0.18 to 0.36
  percent of their norm with first-value shares of 0.001 to 0.024, leading directions unrelated across layers
  (cosine 0.00 to 0.42) and 0.99 to 1.01 of the original's action kept along them; the normalisation vectors moved
  by up to 8.6 percent.
- The dense part is yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1. Round 8 measured richardyoung's ablation of
  that fine-tune against this same Google file (`results/weights/richardyoung-gemma-4-12B-coder-fable5-composer2.5-v1-heretic.json`),
  and that ablation leaves the normalisation vectors alone (piece 1 of this round, 625 tensors at exactly 0 against
  the parent). All 229 normalisation vectors that changed here have a difference norm equal to the last digit to
  that report's, as do the 110 that stayed under the threshold in both; the token embedding reads 5.3678e-5 in both.
  On the projections the fine-tune's change comes through at 0.28 to 0.85 of its size in float16: the fine-tune was
  saved in float16, this copy in bfloat16, and on the recast three quarters of the entries that had moved return to
  Google's value (the fraction of entries that differ from Google is 0.13 to 0.34 here, median 0.25, against 0.89 to
  0.97 on richardyoung's float16 copy of the same fine-tune).
- The ablation sits on the attention outputs of layers 9 to 47 and the down projections of layers 21 to 47: first
  shares 0.940 to 0.988 there (0.002 to 0.007 on the attention outputs of layers 0 to 8 and the down projections of
  layers 0 to 20, which carry the fine-tune only), the first singular value 8 to 116 times the second, relative
  changes 0.013 to 0.029, one shared direction across layers (cosine 0.89 to 1.00, median 0.97 on both writers). The
  two writers of a layer carry directions a few tens of degrees apart (within-layer cosine 0.42 to 0.90 in layers 21
  to 47), unlike piece 1's method (0.92 to 1.00). Along the leading output direction the copy keeps −0.19 to 0.97 of
  Google's action on the attention outputs (median 0.84) and −0.33 to 0.86 on the down projections (median 0.33),
  with the right fractions 0.21 to 0.90; a weight the remaining fraction does not read, as on piece 1. Row norms on
  the ablated matrices moved by 0.003 to 0.011.
- The ablation is this maker's own, on the fine-tune and not on richardyoung's heretic copy: on the layers both edit
  (attention outputs 15 to 47, down projections 24 to 42) the leading directions agree at cosine 0.75 to 0.93, on the
  layers only one of them edits (attention outputs 9 to 14, down projections 21 to 23 and 43 to 47) they are
  unrelated (0.01 to 0.03), and the relative changes here are smaller than richardyoung's on every shared layer.

The attention outputs:

| Layer | Relative change | E1 | E8 | Left, direction 1 | Right, direction 1 | Row norms | Cross-layer cosine | Within-layer cosine |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0.003 | 0.006 | 0.022 | 1.00 | 1.00 | 0.0008 | 0.01 | 0.238 |
| 1 | 0.002 | 0.003 | 0.012 | 1.00 | 1.00 | 0.0005 | 0.03 | 0.265 |
| 2 | 0.003 | 0.002 | 0.009 | 1.00 | 1.00 | 0.0012 | 0.00 | 0.221 |
| 3 | 0.003 | 0.005 | 0.017 | 1.00 | 1.00 | 0.0019 | 0.01 | 0.196 |
| 4 | 0.003 | 0.003 | 0.015 | 1.00 | 1.00 | 0.0004 | 0.01 | 0.100 |
| 5 | 0.003 | 0.004 | 0.015 | 1.00 | 1.00 | 0.0004 | 0.01 | 0.074 |
| 6 | 0.003 | 0.005 | 0.015 | 1.00 | 1.00 | 0.0015 | 0.01 | 0.107 |
| 7 | 0.002 | 0.003 | 0.014 | 1.00 | 1.00 | 0.0004 | 0.01 | 0.109 |
| 8 | 0.002 | 0.005 | 0.026 | 1.00 | 1.00 | 0.0005 | 0.00 | 0.072 |
| 9 | 0.013 | 0.940 | 0.941 | 0.50 | 0.77 | 0.0075 | 0.90 | 0.297 |
| 10 | 0.013 | 0.944 | 0.945 | 0.39 | 0.78 | 0.0032 | 0.91 | 0.301 |
| 11 | 0.013 | 0.943 | 0.946 | 0.49 | 0.86 | 0.0035 | 0.89 | 0.356 |
| 12 | 0.017 | 0.967 | 0.968 | 0.88 | 0.62 | 0.0037 | 0.99 | 0.255 |
| 13 | 0.020 | 0.975 | 0.978 | 0.94 | 0.59 | 0.0044 | 0.96 | 0.209 |
| 14 | 0.022 | 0.976 | 0.979 | 0.96 | 0.50 | 0.0046 | 0.92 | 0.211 |
| 15 | 0.026 | 0.983 | 0.985 | 0.97 | 0.36 | 0.0034 | 0.89 | 0.166 |
| 16 | 0.023 | 0.979 | 0.980 | 0.95 | 0.56 | 0.0039 | 0.94 | 0.217 |
| 17 | 0.019 | 0.970 | 0.971 | 0.86 | 0.65 | 0.0045 | 0.99 | 0.320 |
| 18 | 0.017 | 0.966 | 0.968 | 0.58 | 0.54 | 0.0035 | 0.99 | 0.276 |
| 19 | 0.017 | 0.966 | 0.968 | 0.73 | 0.56 | 0.0049 | 1.00 | 0.292 |
| 20 | 0.028 | 0.985 | 0.987 | 0.97 | 0.27 | 0.0035 | 0.89 | 0.178 |
| 21 | 0.028 | 0.983 | 0.987 | 0.96 | 0.36 | 0.0057 | 0.90 | 0.348 |
| 22 | 0.023 | 0.979 | 0.984 | 0.92 | 0.45 | 0.0062 | 0.96 | 0.434 |
| 23 | 0.020 | 0.976 | 0.977 | 0.83 | 0.52 | 0.0042 | 0.99 | 0.862 |
| 24 | 0.020 | 0.972 | 0.972 | 0.68 | 0.55 | 0.0042 | 1.00 | 0.549 |
| 25 | 0.019 | 0.976 | 0.978 | 0.60 | 0.68 | 0.0077 | 1.00 | 0.523 |
| 26 | 0.025 | 0.982 | 0.984 | 0.85 | 0.44 | 0.0051 | 0.98 | 0.449 |
| 27 | 0.023 | 0.978 | 0.979 | 0.36 | 0.58 | 0.0071 | 0.99 | 0.527 |
| 28 | 0.023 | 0.980 | 0.981 | 0.33 | 0.48 | 0.0084 | 0.98 | 0.541 |
| 29 | 0.023 | 0.979 | 0.980 | -0.19 | 0.57 | 0.0079 | 0.96 | 0.717 |
| 30 | 0.022 | 0.980 | 0.980 | 0.04 | 0.54 | 0.0071 | 0.97 | 0.582 |
| 31 | 0.023 | 0.978 | 0.979 | 0.08 | 0.54 | 0.0106 | 0.97 | 0.575 |
| 32 | 0.029 | 0.987 | 0.988 | 0.87 | 0.26 | 0.0057 | 0.97 | 0.443 |
| 33 | 0.026 | 0.988 | 0.989 | 0.87 | 0.39 | 0.0049 | 0.98 | 0.451 |
| 34 | 0.026 | 0.986 | 0.986 | 0.79 | 0.37 | 0.0072 | 0.99 | 0.502 |
| 35 | 0.024 | 0.983 | 0.983 | 0.69 | 0.47 | 0.0051 | 1.00 | 0.605 |
| 36 | 0.023 | 0.986 | 0.987 | 0.76 | 0.40 | 0.0037 | 1.00 | 0.500 |
| 37 | 0.021 | 0.981 | 0.981 | -0.05 | 0.45 | 0.0045 | 0.97 | 0.595 |
| 38 | 0.027 | 0.984 | 0.985 | 0.91 | 0.35 | 0.0065 | 0.97 | 0.422 |
| 39 | 0.022 | 0.977 | 0.980 | 0.69 | 0.57 | 0.0088 | 1.00 | 0.490 |
| 40 | 0.022 | 0.980 | 0.980 | 0.36 | 0.47 | 0.0057 | 0.99 | 0.537 |
| 41 | 0.020 | 0.976 | 0.977 | 0.56 | 0.48 | 0.0052 | 1.00 | 0.635 |
| 42 | 0.022 | 0.973 | 0.979 | 0.81 | 0.75 | 0.0065 | 0.99 | 0.439 |
| 43 | 0.019 | 0.971 | 0.975 | 0.16 | 0.90 | 0.0050 | 0.97 | 0.474 |
| 44 | 0.025 | 0.967 | 0.983 | 0.89 | 0.69 | 0.0092 | 0.97 | 0.420 |
| 45 | 0.020 | 0.971 | 0.974 | 0.47 | 0.69 | 0.0096 | 0.99 | 0.540 |
| 46 | 0.019 | 0.971 | 0.972 | 0.60 | 0.64 | 0.0070 | 0.99 | 0.529 |
| 47 | 0.022 | 0.975 | 0.978 | 0.92 | 0.54 | 0.0049 | 0.97 | 0.517 |

The down projections:

| Layer | Relative change | E1 | E8 | Left, direction 1 | Right, direction 1 | Row norms | Cross-layer cosine | Within-layer cosine |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0.003 | 0.003 | 0.013 | 1.00 | 1.00 | 0.0003 | 0.00 | 0.125 |
| 1 | 0.003 | 0.002 | 0.010 | 1.00 | 1.00 | 0.0005 | 0.01 | 0.095 |
| 2 | 0.003 | 0.002 | 0.012 | 1.00 | 1.00 | 0.0006 | 0.00 | 0.050 |
| 3 | 0.003 | 0.003 | 0.016 | 1.00 | 1.00 | 0.0003 | 0.00 | 0.039 |
| 4 | 0.003 | 0.004 | 0.016 | 1.00 | 0.99 | 0.0003 | 0.02 | 0.062 |
| 5 | 0.003 | 0.003 | 0.017 | 1.00 | 1.00 | 0.0003 | 0.01 | 0.070 |
| 6 | 0.003 | 0.003 | 0.014 | 1.00 | 1.01 | 0.0003 | 0.01 | 0.053 |
| 7 | 0.003 | 0.003 | 0.013 | 1.00 | 1.00 | 0.0016 | 0.00 | 0.143 |
| 8 | 0.003 | 0.007 | 0.015 | 1.00 | 0.99 | 0.0002 | 0.00 | 0.032 |
| 9 | 0.003 | 0.007 | 0.054 | 1.00 | 0.99 | 0.0003 | 0.00 | 0.079 |
| 10 | 0.003 | 0.007 | 0.045 | 1.00 | 1.00 | 0.0002 | 0.02 | 0.025 |
| 11 | 0.003 | 0.003 | 0.018 | 1.00 | 1.00 | 0.0004 | 0.00 | 0.103 |
| 12 | 0.003 | 0.006 | 0.012 | 1.00 | 1.01 | 0.0003 | 0.00 | 0.051 |
| 13 | 0.003 | 0.004 | 0.014 | 1.00 | 0.99 | 0.0003 | 0.00 | 0.050 |
| 14 | 0.003 | 0.006 | 0.014 | 1.00 | 0.99 | 0.0003 | 0.35 | 0.017 |
| 15 | 0.003 | 0.004 | 0.014 | 1.00 | 1.01 | 0.0007 | 0.35 | 0.017 |
| 16 | 0.003 | 0.002 | 0.013 | 1.00 | 0.99 | 0.0004 | 0.28 | 0.101 |
| 17 | 0.003 | 0.004 | 0.016 | 1.00 | 1.00 | 0.0002 | 0.34 | 0.020 |
| 18 | 0.003 | 0.005 | 0.012 | 1.00 | 0.99 | 0.0005 | 0.06 | 0.069 |
| 19 | 0.003 | 0.004 | 0.011 | 1.00 | 0.99 | 0.0003 | 0.34 | 0.016 |
| 20 | 0.002 | 0.009 | 0.018 | 1.00 | 1.01 | 0.0005 | 0.35 | 0.013 |
| 21 | 0.023 | 0.980 | 0.982 | 0.86 | 0.21 | 0.0043 | 0.95 | 0.479 |
| 22 | 0.022 | 0.978 | 0.979 | 0.77 | 0.28 | 0.0043 | 0.98 | 0.516 |
| 23 | 0.021 | 0.976 | 0.976 | 0.32 | 0.41 | 0.0045 | 1.00 | 0.896 |
| 24 | 0.023 | 0.980 | 0.981 | 0.68 | 0.34 | 0.0040 | 0.98 | 0.541 |
| 25 | 0.023 | 0.980 | 0.982 | 0.72 | 0.27 | 0.0050 | 0.98 | 0.504 |
| 26 | 0.024 | 0.984 | 0.985 | 0.64 | 0.26 | 0.0039 | 0.97 | 0.484 |
| 27 | 0.026 | 0.984 | 0.984 | 0.25 | 0.39 | 0.0070 | 0.98 | 0.532 |
| 28 | 0.025 | 0.983 | 0.983 | -0.01 | 0.23 | 0.0051 | 0.98 | 0.555 |
| 29 | 0.027 | 0.985 | 0.985 | -0.12 | 0.30 | 0.0092 | 0.99 | 0.709 |
| 30 | 0.025 | 0.984 | 0.984 | 0.10 | 0.25 | 0.0063 | 0.99 | 0.579 |
| 31 | 0.024 | 0.982 | 0.982 | 0.52 | 0.16 | 0.0042 | 0.98 | 0.541 |
| 32 | 0.025 | 0.983 | 0.984 | 0.56 | 0.13 | 0.0055 | 0.99 | 0.533 |
| 33 | 0.025 | 0.984 | 0.985 | 0.53 | 0.04 | 0.0055 | 0.99 | 0.519 |
| 34 | 0.024 | 0.981 | 0.981 | 0.15 | -0.00 | 0.0047 | 1.00 | 0.568 |
| 35 | 0.024 | 0.981 | 0.981 | -0.15 | -0.03 | 0.0044 | 1.00 | 0.670 |
| 36 | 0.024 | 0.982 | 0.982 | -0.23 | -0.06 | 0.0031 | 1.00 | 0.558 |
| 37 | 0.026 | 0.984 | 0.985 | 0.33 | 0.09 | 0.0040 | 1.00 | 0.566 |
| 38 | 0.025 | 0.984 | 0.985 | 0.20 | -0.10 | 0.0029 | 1.00 | 0.538 |
| 39 | 0.024 | 0.980 | 0.981 | -0.33 | 0.02 | 0.0057 | 0.99 | 0.556 |
| 40 | 0.024 | 0.980 | 0.980 | -0.22 | 0.06 | 0.0034 | 0.99 | 0.563 |
| 41 | 0.023 | 0.982 | 0.982 | -0.14 | 0.05 | 0.0044 | 1.00 | 0.671 |
| 42 | 0.023 | 0.981 | 0.981 | -0.02 | 0.17 | 0.0048 | 1.00 | 0.504 |
| 43 | 0.022 | 0.974 | 0.975 | -0.02 | 0.14 | 0.0035 | 1.00 | 0.472 |
| 44 | 0.022 | 0.978 | 0.979 | 0.06 | 0.08 | 0.0045 | 1.00 | 0.546 |
| 45 | 0.022 | 0.979 | 0.979 | -0.12 | 0.09 | 0.0041 | 0.99 | 0.570 |
| 46 | 0.024 | 0.981 | 0.982 | 0.74 | 0.13 | 0.0037 | 0.98 | 0.504 |
| 47 | 0.020 | 0.972 | 0.972 | -0.20 | 0.15 | 0.0033 | 0.96 | 0.702 |

## Token and configuration side (Stage 1)

The cluster's card read "unexplained differences" in six fields and the home judgement keeps them, so the committed
card reads "unexplained differences"; the reading closes them by hand.

- `config.transformers_version` and `generation.transformers_version`: 5.10.0.dev0 on the original, 5.10.1 on the
  copy, and `config.text_config.dtype` written out. Re-save effects, as the tool says.
- `config.audio_config.audio_samples_per_token`, `hidden_size` and `output_proj_dims` (640, 640, 640) and
  `config.vision_config.model_patch_size` (48) absent from the copy, and `audio_config.dtype` and
  `vision_config.dtype` repeated: the four fields are values a 5.10 save omits because they equal the class defaults
  and the loader restores (finding 11's rule; the parent fine-tune's `config.json`, saved under 5.10.2, omits the same
  four), and the two dtype fields are the same re-save. Re-save effects.
- The copy's configuration otherwise equals Google's, `max_position_embeddings` 131072 and bfloat16 included, where
  the fine-tune declares 262144 and float16: the configuration was written from Google's files, the weights from the
  fine-tune's. The template equals Google's byte for byte, the tokenizer, special tokens and generation settings are
  unchanged, and the fixed conversation renders identically.

## For the recipe library

Not consistent with the card on the weight side: the card names Google as the one parent and the weights carry
yuxinlu1's coding fine-tune under the ablation, the second copy (after 3MPER0RR's, finding 8) whose weights carry a
parent its card names nowhere; richardyoung's and prithivMLmods's cards (findings 18 and 9) name theirs in the text.
Consistent on the token side once the six fields are read as a 5.10 re-save. Not an entry: a shared-direction
ablation with per-writer directions and an unread weight on top of a recast fine-tune. The saved direction vectors
are not committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/nautilus16/measurements/pair-3/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
