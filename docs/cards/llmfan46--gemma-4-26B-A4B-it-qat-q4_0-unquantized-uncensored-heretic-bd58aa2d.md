# Stage 1: llmfan46/gemma-4-26B-A4B-it-qat-q4_0-unquantized-uncensored-heretic

Original: `google/gemma-4-26B-A4B-it-qat-q4_0-unquantized`

Verdict: **unexplained differences**

Revisions: modified `33d5581f1f060bbe7832f81eca0e6f75e2857d09`; original `641f184470aa8554ae7957599a624badc2bf4e57`.

Changed fields:

- `template.default` (unexplained)

## Explained by re-save: `generation.transformers_version`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The saved version string changed.

## Explained by re-save: `config.transformers_version`

Original file: `config.json`.

Modified file: `config.json`.

The saved version string changed.

The `default` template source differs beyond line endings and trailing whitespace.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: directional-per-layer-selected.
