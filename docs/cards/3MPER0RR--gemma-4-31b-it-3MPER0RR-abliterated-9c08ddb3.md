# Stage 1: 3MPER0RR/gemma-4-31b-it-3MPER0RR-abliterated

Original: `google/gemma-4-31B-it`

Verdict: **unexplained differences**

Revisions: modified `5f97708dbe38795729246bd2ce75e488c3481816`; original `842da3794eaa0b77d5f08bae87a17459d91ff475`.

Changed fields:

- `config.text_config.num_global_key_value_heads` (unexplained)
- `config.text_config.per_layer_config` (unexplained)

## Explained by re-save: `generation.transformers_version`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The saved version string changed.

## Explained by re-save: `config.text_config.global_head_dim`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.6.2.

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

Weights: recipe_violations. Nearest recipe: directional-per-layer-selected.
