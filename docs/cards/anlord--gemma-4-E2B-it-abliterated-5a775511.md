# Stage 1: anlord/gemma-4-E2B-it-abliterated

Original: `google/gemma-4-E2B-it`

Verdict: **unexplained differences**

Revisions: modified `5d584569e3c6ecaf499e46a5e75592444dc69e4a`; original `3e22461f65e89153144f8adb70e3b8c2cc9845a7`.

Changed fields:

- `config.text_config.global_head_dim` (unexplained)
- `config.text_config.num_global_key_value_heads` (unexplained)
- `config.text_config.per_layer_config` (unexplained)
- `config.vision_config.rope_parameters.rope_type` (unexplained)

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
