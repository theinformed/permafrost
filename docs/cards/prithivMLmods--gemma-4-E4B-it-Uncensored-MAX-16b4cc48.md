# Stage 1: prithivMLmods/gemma-4-E4B-it-Uncensored-MAX

Original: `google/gemma-4-E4B-it`

Verdict: **unexplained differences**

Revisions: modified `19d2605ff3fcec8086c171d8420e84b7c4ba6ca5`; original `83df0a889143b1dbfc61b591bbc639540fd9ce4c`.

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
