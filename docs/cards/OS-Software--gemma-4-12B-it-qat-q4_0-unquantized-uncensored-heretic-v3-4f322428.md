# Stage 1: OS-Software/gemma-4-12B-it-qat-q4_0-unquantized-uncensored-heretic-v3

Original: `google/gemma-4-12B-it-qat-q4_0-unquantized`

Verdict: **unexplained differences**

Revisions: modified `f637e7d3ea30c1b6025c112b5c7cb23315422951`; original `b6ed86275a6a5735884e208bfed95b445a684ca2`.

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
