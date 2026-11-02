# Stage 1: sh0ck0r/Artemis-31B-v1.1-heretic

Original: `TheDrummer/Artemis-31B-v1.1`

Verdict: **unexplained differences**

Revisions: modified `b3bdce6acb08be8518bb17fd9a1ff31eb9bd4928`; original `d613e5a4ee45e0fcf1f61ea3e10b6438bbe421cc`.

Changed fields:

- `config.text_config.per_layer_config` (unexplained)

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
