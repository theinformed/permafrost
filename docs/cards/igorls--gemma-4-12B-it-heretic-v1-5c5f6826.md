# Stage 1: igorls/gemma-4-12B-it-heretic-v1

Original: `google/gemma-4-12B-it`

Verdict: **unexplained differences**

Revisions: modified `192d14f658a5cb274ac280b2d6d5cecaf37c5c6f`; original `66bc78a7534d523aa32004652cb02cc2e6354c62`.

Changed fields:

- `config.audio_config.audio_samples_per_token` (unexplained)
- `config.audio_config.dtype` (unexplained)
- `config.audio_config.hidden_size` (unexplained)
- `config.audio_config.output_proj_dims` (unexplained)
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
