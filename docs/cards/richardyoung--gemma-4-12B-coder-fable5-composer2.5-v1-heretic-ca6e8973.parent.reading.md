# Reading of the Stage 1 and Stage 2 result: richardyoung/gemma-4-12B-coder-fable5-composer2.5-v1-heretic against yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1 (2026-10-31)

Measured on Nautilus, round 16 piece 1 (push card 5433, round card 5434, download job 4120061, compare job 4120062 on
the background queue, sweep 4120069; pulled home by card 5467). This is the parent pair owed since round 8, where the
same copy was measured against google/gemma-4-12B-it (the reading beside this one, without the `.parent` suffix);
the maker's card names yuxinlu1's coding fine-tune as its parent in its first line and Google in its `base_model`
field. Modified revision `355963e1` (2026-09-26, "Standardize author sign-off"; the repository was created on
2026-06-24), original pinned at `237e5d8e` (2026-06-18, the parent's one revision after its creation on 06-17; one
weight file, shard `da00c3ea`, float16). The maker's card and its `reproduce/config.toml` name the method and its
parameters: Heretic 1.4.0 with `orthogonalize_direction` on, `row_normalization` "full" at LoRA rank 3, a
winsorisation quantile of 1.0 and a KL target of 0.01, 200 trials with trial 188 chosen (KL 0.058, 7 refusals in 100),
transformers 5.12.1 and peft 0.19.1, on the mlabonne harmless and harmful sets at `02c6a92` and `01cead0`; the card
lists the attention outputs of layers 15 to 47 at weights 1.24 to 1.28 and the down projections of layers 24 to 42 at
1.47 to 1.48.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 8 flags, on the
cluster and after re-scoring at home. All 8 flags are within-layer direction cosines (layers 26, 38, 39 and 42, each
counted on both writers). On reading, the footprint is the ablation alone, and it is exactly what the card lists.

- 52 of 677 tensors changed: the attention outputs of layers 15 to 47 (33) and the down projections of layers 24 to 42
  (19), the card's components to the layer. Nothing else moved; the other 625 tensors, the fine-tune's projections and
  normalisation vectors included, read a relative difference of exactly 0. Against Google in round 8 the same copy
  changed 557 tensors; the 505 that drop out here are the parent's, as finding 18 said.
- Rank one on every matrix: first-value energy share 0.990 to 0.9999 (median 0.999), first eight 0.9999 or more, the
  first singular value 10 to 171 times the second (median 32 on the attention outputs, 57 on the down projections).
- One shared direction: cross-layer cosine 0.90 to 0.998 on the attention outputs and 0.95 to 0.999 on the down
  projections (median 0.985), within-layer cosine 0.918 to 1.000 where both writers carry it.
- The remaining fraction still does not read the card's weights. Along the leading output direction the copy keeps
  −0.09 to 0.95 of the parent's action on the left of the attention outputs (median 0.74) and −0.27 to 0.70 on the
  down projections (median 0.06); the card's 1.24 to 1.28 and 1.47 to 1.48 would read −0.24 to −0.28 and −0.47 to
  −0.48. The right fractions read −0.04 to 0.86, and the left is below the right on only 11 of the 33 attention outputs
  and 9 of the 19 down projections. Directions 2 to 8 keep 0.97 to 1.04 on both sides. Round 8 read the same spread
  against Google and explained it by the fine-tune's change adding to the ablation's; the parent comparison removes
  the fine-tune and the spread is unchanged, so the spread is the edit's own. The configuration names two steps the
  calibrated projection does not have, the "full" row normalisation with its rank-3 correction and the
  orthogonalisation of the direction, and either can move the kept fraction off the card's number; which one does is
  not settled by this measurement.
- Row norms moved by 0.0035 to 0.033 relative on the attention outputs (median 0.0060) and 0.0040 to 0.0095 on the
  down projections. The card's "full" row normalisation leaves the rows about half a percent off, three to five times
  the residue of coder3101's restoration (0.006 to 0.008 read as 0.0059 to 0.0080 on three bases) on the typical
  matrix and up to 0.033 on layer 43.

| Layer | Relative change | E1 | E8 | Left, direction 1 | Right, direction 1 | Row norms | Cross-layer cosine | Within-layer cosine |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15 | 0.043 | 0.999 | 1.000 | 0.95 | 0.02 | 0.0045 | 0.91 | 1.000 |
| 16 | 0.035 | 1.000 | 1.000 | 0.93 | 0.26 | 0.0041 | 0.95 | 1.000 |
| 17 | 0.027 | 1.000 | 1.000 | 0.84 | 0.53 | 0.0052 | 1.00 | 1.000 |
| 18 | 0.023 | 0.999 | 1.000 | 0.57 | 0.40 | 0.0037 | 0.99 | 1.000 |
| 19 | 0.023 | 0.998 | 1.000 | 0.72 | 0.41 | 0.0049 | 1.00 | 1.000 |
| 20 | 0.042 | 0.999 | 1.000 | 0.95 | -0.04 | 0.0040 | 0.91 | 1.000 |
| 21 | 0.041 | 0.999 | 1.000 | 0.95 | 0.11 | 0.0070 | 0.92 | 1.000 |
| 22 | 0.031 | 0.996 | 1.000 | 0.91 | 0.27 | 0.0060 | 0.97 | 1.000 |
| 23 | 0.026 | 0.998 | 1.000 | 0.82 | 0.37 | 0.0059 | 1.00 | 1.000 |
| 24 | 0.023 | 0.999 | 1.000 | 0.72 | 0.44 | 0.0059 | 1.00 | 0.998 |
| 25 | 0.022 | 0.998 | 1.000 | 0.63 | 0.65 | 0.0059 | 0.99 | 0.996 |
| 26 | 0.030 | 0.999 | 1.000 | 0.86 | 0.29 | 0.0038 | 0.99 | 0.950 |
| 27 | 0.027 | 0.998 | 1.000 | 0.22 | 0.59 | 0.0073 | 0.93 | 0.998 |
| 28 | 0.026 | 0.999 | 1.000 | 0.31 | 0.44 | 0.0083 | 0.93 | 0.997 |
| 29 | 0.024 | 0.997 | 1.000 | -0.09 | 0.52 | 0.0068 | 0.90 | 0.995 |
| 30 | 0.023 | 1.000 | 1.000 | 0.12 | 0.51 | 0.0063 | 0.93 | 0.993 |
| 31 | 0.023 | 1.000 | 1.000 | 0.12 | 0.52 | 0.0053 | 0.94 | 0.974 |
| 32 | 0.034 | 0.999 | 1.000 | 0.86 | 0.12 | 0.0039 | 0.96 | 0.967 |
| 33 | 0.029 | 0.999 | 1.000 | 0.88 | 0.37 | 0.0068 | 0.98 | 0.975 |
| 34 | 0.027 | 1.000 | 1.000 | 0.84 | 0.36 | 0.0043 | 1.00 | 0.962 |
| 35 | 0.025 | 0.999 | 1.000 | 0.74 | 0.56 | 0.0035 | 1.00 | 0.962 |
| 36 | 0.024 | 1.000 | 1.000 | 0.79 | 0.58 | 0.0058 | 1.00 | 0.953 |
| 37 | 0.021 | 1.000 | 1.000 | 0.06 | 0.49 | 0.0063 | 0.95 | 0.983 |
| 38 | 0.032 | 0.998 | 1.000 | 0.90 | 0.23 | 0.0060 | 0.98 | 0.918 |
| 39 | 0.026 | 0.992 | 1.000 | 0.71 | 0.63 | 0.0221 | 1.00 | 0.937 |
| 40 | 0.023 | 1.000 | 1.000 | 0.46 | 0.48 | 0.0077 | 0.98 | 0.984 |
| 41 | 0.023 | 0.999 | 1.000 | 0.63 | 0.46 | 0.0049 | 0.99 | 0.978 |
| 42 | 0.026 | 0.990 | 1.000 | 0.82 | 0.75 | 0.0213 | 1.00 | 0.943 |
| 43 | 0.021 | 0.997 | 1.000 | 0.14 | 0.86 | 0.0327 | 0.95 | 1.000 |
| 44 | 0.032 | 0.992 | 1.000 | 0.90 | 0.50 | 0.0177 | 0.97 | 1.000 |
| 45 | 0.023 | 0.997 | 1.000 | 0.53 | 0.59 | 0.0174 | 0.99 | 1.000 |
| 46 | 0.023 | 0.993 | 1.000 | 0.60 | 0.65 | 0.0125 | 0.99 | 1.000 |
| 47 | 0.030 | 0.997 | 1.000 | 0.90 | 0.48 | 0.0085 | 0.97 | 1.000 |

The down projections of layers 24 to 42:

| Layer | Relative change | E1 | E8 | Left, direction 1 | Right, direction 1 | Row norms | Cross-layer cosine | Within-layer cosine |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 24 | 0.030 | 0.999 | 1.000 | 0.66 | 0.14 | 0.0073 | 0.98 | 0.998 |
| 25 | 0.030 | 0.999 | 1.000 | 0.70 | 0.09 | 0.0040 | 0.98 | 0.996 |
| 26 | 0.033 | 0.999 | 1.000 | 0.51 | 0.02 | 0.0048 | 0.95 | 0.950 |
| 27 | 0.033 | 0.997 | 1.000 | 0.01 | 0.24 | 0.0088 | 0.96 | 0.998 |
| 28 | 0.032 | 0.997 | 1.000 | -0.27 | 0.07 | 0.0068 | 0.96 | 0.997 |
| 29 | 0.029 | 1.000 | 1.000 | -0.08 | 0.15 | 0.0077 | 0.97 | 0.995 |
| 30 | 0.028 | 1.000 | 1.000 | -0.01 | 0.07 | 0.0095 | 0.98 | 0.993 |
| 31 | 0.029 | 0.999 | 1.000 | 0.50 | -0.02 | 0.0076 | 0.98 | 0.974 |
| 32 | 0.029 | 0.998 | 1.000 | 0.58 | 0.00 | 0.0086 | 0.99 | 0.967 |
| 33 | 0.028 | 1.000 | 1.000 | 0.57 | -0.05 | 0.0066 | 0.99 | 0.975 |
| 34 | 0.026 | 1.000 | 1.000 | 0.25 | -0.11 | 0.0046 | 1.00 | 0.962 |
| 35 | 0.025 | 1.000 | 1.000 | -0.06 | -0.09 | 0.0060 | 0.99 | 0.962 |
| 36 | 0.024 | 1.000 | 1.000 | -0.13 | 0.21 | 0.0040 | 0.99 | 0.953 |
| 37 | 0.027 | 0.999 | 1.000 | 0.44 | 0.23 | 0.0085 | 0.99 | 0.983 |
| 38 | 0.026 | 1.000 | 1.000 | 0.35 | 0.00 | 0.0048 | 1.00 | 0.918 |
| 39 | 0.024 | 1.000 | 1.000 | -0.26 | 0.04 | 0.0071 | 0.98 | 0.937 |
| 40 | 0.024 | 1.000 | 1.000 | -0.13 | 0.03 | 0.0049 | 0.99 | 0.984 |
| 41 | 0.024 | 1.000 | 1.000 | -0.07 | -0.04 | 0.0056 | 0.99 | 0.978 |
| 42 | 0.024 | 0.999 | 1.000 | 0.06 | 0.18 | 0.0087 | 0.99 | 0.943 |

Against round 8's report on the same copy (a different original, so no equal field was expected), 16 of the 52 changed
tensors carry an equal largest absolute difference and no other field agrees; the two reports name the same 52
matrices as the carriers of the shared direction. Against lemuralabs's copy of piece 3, which stands on the same
fine-tune (its reading), this copy's leading directions agree at cosine 0.75 to 0.93 on the layers both edit.

## Token and configuration side (Stage 1)

The cluster's card read "consistent with re-save noted" and the home judgement under transformers 5.6.2 with the
later-revision rule keeps it, so the committed card reads "consistent with re-save noted".

- `config.transformers_version` and `generation.transformers_version`: 5.10.2 on the parent, 5.12.1 on the copy, the
  version the card names. A re-save effect.
- The template equals the parent's byte for byte and the fixed conversation renders identically; the configuration,
  tokenizer, special tokens and generation settings are otherwise equal, float16 and `max_position_embeddings` 262144
  included, both the parent's choices (round 8 read them as differences from Google).

## For the recipe library

Consistent with the stated change on both sides once measured against the parent the card names. The first copy
measured against both its grandparent and its parent; the parent comparison is the one that reads the edit alone,
and it says the weight of this maker's method is not the card's number even with the fine-tune removed (finding 18,
corrected). The saved direction vectors are not committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/nautilus16/measurements/pair-1/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
