# Stage 1: TrevorJS/gemma-4-E2B-it-uncensored

Original: `google/gemma-4-E2B-it`

Verdict: **consistent with re-save noted**

Revisions: modified `7a34581e4d278ccd2aa85e9fa6328060f7370cca`; original `4742fe843cc01b9aed62122f6e0ddd13ea48b3d3`.

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

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: directional-per-layer.
