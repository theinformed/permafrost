# Stage 1: Ilya626/gemma-4-E4B-it-SDFT_Heretic_RP

Original: `google/gemma-4-E4B-it`

Verdict: **unexplained differences**

Revisions: modified `c07b5f9b6dd05a43f8c263dab73737cd6b36aa2a`; original `83df0a889143b1dbfc61b591bbc639540fd9ce4c`.

Changed fields:

- `config.audio_config.dtype` (unexplained)
- `config.dtype` (unexplained)
- `config.text_config.dtype` (unexplained)
- `config.vision_config.dtype` (unexplained)
- `template.default` (unexplained)

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

Weights: recipe_violations. Nearest recipe: single-projection.
