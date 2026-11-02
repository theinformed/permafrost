# Stage 1: nguyenthilaitrieulong/gemma-4-31B-it-abliterated

Original: `google/gemma-4-31B-it`

Verdict: **unexplained differences**

Revisions: modified `1b2830377ea87db051d0e4f227a66e9490887d99`; original `842da3794eaa0b77d5f08bae87a17459d91ff475`.

Changed fields:

- `generation.bad_words_ids` (unexplained)
- `template.default` (unexplained)

## Explained by re-save: `generation.transformers_version`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The saved version string changed.

## Explained by re-save: `config.text_config.moe_intermediate_size`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.22.1.

## Explained by re-save: `config.transformers_version`

Original file: `config.json`.

Modified file: `config.json`.

The saved version string changed.

The `default` template source differs beyond line endings and trailing whitespace.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: directional-per-layer-selected.
