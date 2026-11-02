# Stage 1: MoonRide/gemma-4-31B-it-heretic-ara

Original: `google/gemma-4-31B-it`

Verdict: **consistent with re-save noted**

Revisions: modified `cf80d7e7596ddd614764eea7652959f4e7edb46a`; original `439edf5652646a0d1bd8b46bfdc1d3645761a445`.

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

Weights: recipe_violations. Nearest recipe: directional-per-layer-selected.
