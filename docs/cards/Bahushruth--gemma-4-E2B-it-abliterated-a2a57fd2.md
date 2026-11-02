# Stage 1: Bahushruth/gemma-4-E2B-it-abliterated

Original: `google/gemma-4-E2B-it`

Verdict: **consistent with re-save noted**

Revisions: modified `fbdbee529c32260fc016ae4922b260a307000490`; original `3e22461f65e89153144f8adb70e3b8c2cc9845a7`.

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
