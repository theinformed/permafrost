# Stage 1: llmfan46/gemma-4-E2B-it-ultra-uncensored-heretic

Original: `google/gemma-4-E2B-it`

Verdict: **unexplained differences**

Revisions: modified `13d8eefa10175f813a97404b7c9fa4d7f1452880`; original `b4a601102c3d45e2b7b50e2057a6d5ec8ed4adcf`.

Changed fields:

- `template.default` (unexplained)

## Explained by re-save: `generation.transformers_version`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The saved version string changed.

## Explained by re-save: `config.text_config.moe_intermediate_size`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.6.2.

## Explained by re-save: `config.transformers_version`

Original file: `config.json`.

Modified file: `config.json`.

The saved version string changed.

The `default` template source differs beyond line endings and trailing whitespace.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: directional-per-layer-selected.
