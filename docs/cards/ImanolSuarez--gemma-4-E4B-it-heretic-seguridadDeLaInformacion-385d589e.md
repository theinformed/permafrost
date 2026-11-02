# Stage 1: ImanolSuarez/gemma-4-E4B-it-heretic-seguridadDeLaInformacion

Original: `google/gemma-4-E4B-it`

Verdict: **consistent with re-save noted**

Revisions: modified `50f4cdf9963f0bc2335e77274657f4994244669d`; original `d6436b3d62967e1af08bbb046c6300b2a9ae8e85`.

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

Weights: recipe_violations. Nearest recipe: single-projection-selected.
