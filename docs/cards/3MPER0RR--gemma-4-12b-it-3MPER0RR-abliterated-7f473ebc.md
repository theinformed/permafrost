# Stage 1: 3MPER0RR/gemma-4-12b-it-3MPER0RR-abliterated

Original: `google/gemma-4-12B-it`

Verdict: **unexplained differences**

Revisions: modified `97d0cfbda8300e64f8700f0e2ed3314d94a2c01e`; original `707f0a3b8a3c7ad586ed01e27eafbad8a27dd0f7`.

Changed fields:

- `config.audio_config.audio_samples_per_token` (unexplained)
- `config.audio_config.dtype` (unexplained)
- `config.audio_config.hidden_size` (unexplained)
- `config.audio_config.output_proj_dims` (unexplained)
- `config.text_config.global_head_dim` (unexplained)
- `config.text_config.num_global_key_value_heads` (unexplained)
- `config.text_config.per_layer_config` (unexplained)
- `config.vision_config.dtype` (unexplained)
- `config.vision_config.model_patch_size` (unexplained)

## Explained by re-save: `generation.transformers_version`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The saved version string changed.

## Explained by re-save: `config.text_config.dtype`

Original file: `config.json`.

Modified file: `config.json`.

The sub-configuration repeats the data type the top-level configuration already declares.

## Explained by re-save: `config.transformers_version`

Original file: `config.json`.

Modified file: `config.json`.

The saved version string changed.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: single-projection-selected.
