# Stage 1: treadon/gemma4-E2B-it-Abliterated-AND-Disinhibited-USE-THIS

Original: `google/gemma-4-E2B-it`

Verdict: **consistent with re-save noted**

Revisions: modified `9e3f1fd8678c86ebf49d07ab86a30f0d46bb0a00`; original `6b7e72c67d3c4556f42b56d5a68b4b8e864c63b4`.

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
