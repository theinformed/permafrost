# Stage 1: OS-Software/gemma-4-31B-it-qat-q4_0-unquantized-uncensored-heretic

Original: `google/gemma-4-31B-it-qat-q4_0-unquantized`

Verdict: **unexplained differences**

Revisions: modified `244246e628015845fc3b1d0bb4e97549d03e625b`; original `1e4d8beecacb8b7590c1d8bedd7335f687bf311f`.

Changed fields:

- `config.text_config.global_head_dim` (unexplained)
- `config.text_config.num_global_key_value_heads` (unexplained)
- `config.text_config.per_layer_config` (unexplained)

## Explained by re-save: `generation.transformers_version`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The saved version string changed.

## Explained by re-save: `config.transformers_version`

Original file: `config.json`.

Modified file: `config.json`.

The saved version string changed.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: directional-per-layer-selected.
