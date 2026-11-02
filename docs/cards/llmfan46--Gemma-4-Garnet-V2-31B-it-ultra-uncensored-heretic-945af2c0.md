# Stage 1: llmfan46/Gemma-4-Garnet-V2-31B-it-ultra-uncensored-heretic

Original: `ConicCat/Gemma4-GarnetV2-31B`

Verdict: **unexplained differences**

Revisions: modified `3ab379e5074fcea4c1304ee2c85f6a0423858507`; original `74f74a1bea824d89bf26a558aa2072e41eb91d82`.

Changed fields:

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
