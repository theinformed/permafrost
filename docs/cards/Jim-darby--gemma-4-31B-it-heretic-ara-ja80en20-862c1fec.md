# Stage 1: Jim-darby/gemma-4-31B-it-heretic-ara-ja80en20

Original: `google/gemma-4-31B-it`

Verdict: **unexplained differences**

Revisions: modified `9c2c9c8fc24df09a10ee88b94c91a1f7b20fd538`; original `fcf2302760ae9c6e528a8dbba9dd636e56848237`.

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
