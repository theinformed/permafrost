# Stage 1: treadon/gemma4-E2B-it-abliterated

Original: `google/gemma-4-E2B-it`

Verdict: **consistent with re-save noted**

Revisions: modified `e0b7d84d77088647c7076b19fe98f5c44b64861f`; original `b4a601102c3d45e2b7b50e2057a6d5ec8ed4adcf`.

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

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_match. Nearest recipe: directional-per-layer-selected.
