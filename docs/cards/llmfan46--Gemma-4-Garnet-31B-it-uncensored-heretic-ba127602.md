# Stage 1: llmfan46/Gemma-4-Garnet-31B-it-uncensored-heretic

Original: `ConicCat/Gemma4-Garnet-31B`

Verdict: **unexplained differences**

Revisions: modified `e4da9fb30e0dad124811d57628fb6e166a199520`; original `200c398e59770f32d3fa4cbe75ded4c4b1b8831f`.

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
