# Stage 1: amkkk/Gemma4_E2B_Abliterated_Baked_HF_Ready

Original: `google/gemma-4-E2B-it`

Verdict: **unexplained differences**

Revisions: modified `9cea12fbe498fe80c6b62b0f605c44e60f961e34`; original `b4a601102c3d45e2b7b50e2057a6d5ec8ed4adcf`.

Changed fields:

- `config.ablation_layers` (unexplained)
- `config.ablation_scope` (unexplained)
- `config.ablation_strength` (unexplained)
- `config.direction_source` (unexplained)
- `config.direction_source_layer` (unexplained)
- `config.export_source_model` (unexplained)
- `config.export_type` (unexplained)
- `config.mlp_down_strength` (unexplained)
- `config.mlp_gate_strength` (unexplained)
- `config.mlp_up_strength` (unexplained)
- `config.self_attn_o_strength` (unexplained)
- `config.target_weights` (unexplained)

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
