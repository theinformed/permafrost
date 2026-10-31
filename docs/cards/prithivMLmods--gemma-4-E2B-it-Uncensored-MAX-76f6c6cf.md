# Stage 1: prithivMLmods/gemma-4-E2B-it-Uncensored-MAX

Original: `google/gemma-4-E2B-it`

Verdict: **unexplained differences**

Revisions: modified `ae5ff12466ca2159e3617211fe7c2439c78766e8`; original `b4a601102c3d45e2b7b50e2057a6d5ec8ed4adcf`.

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

Weights: recipe_match. Nearest recipe: single-projection-selected.
