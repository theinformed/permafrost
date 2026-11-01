# Stage 1: OS-Software/gemma-4-E4B-it-uncensored-heretic

Original: `google/gemma-4-E4B-it`

Verdict: **unexplained differences**

Revisions: modified `59a70a7b2f4cc5a80af89ab6aabc9c8c8406bdde`; original `ee0ef6023621cff504d758262d4e04895a5af4a2`.

Changed fields:

- `config.text_config.global_head_dim` (unexplained)
- `config.text_config.num_global_key_value_heads` (unexplained)
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

Weights: recipe_violations. Nearest recipe: directional-per-layer-selected.
