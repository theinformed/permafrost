# Stage 1: llmfan46/gemma-4-12B-it-qat-q4_0-unquantized-uncensored-heretic

Original: `google/gemma-4-12B-it-qat-q4_0-unquantized`

Verdict: **unexplained differences**

Revisions: modified `556c19b5001fe65366c687f66879c6c4671ff4f0`; original `58540658b6c08edab2ddc1fbde7f28cc9987ced3`.

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
