# Stage 1: Vampelium/gemma-4-31B-it-heretic

Original: `google/gemma-4-31B-it`

Verdict: **consistent with re-save noted**

Revisions: modified `88a86a0bbe1d89c25ce1bd8bb6aa647b117e5b97`; original `842da3794eaa0b77d5f08bae87a17459d91ff475`.

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
