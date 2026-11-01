# Stage 1: MeFFyLe/gemma-4-12B-it-uncensored-heretic

Original: `google/gemma-4-12B-it`

Verdict: **unexplained differences**

Revisions: modified `0a5e69dd7ffdeb592f9f2e86c23f6c898508b136`; original `707f0a3b8a3c7ad586ed01e27eafbad8a27dd0f7`.

Changed fields:

- `config.audio_config.audio_samples_per_token` (unexplained)
- `config.audio_config.hidden_size` (unexplained)
- `config.audio_config.output_proj_dims` (unexplained)
- `config.vision_config.model_patch_size` (unexplained)
- `template.default` (unexplained)

## Explained by re-save: `generation.transformers_version`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The saved version string changed.

## Explained by re-save: `config.audio_config.dtype`

Original file: `config.json`.

Modified file: `config.json`.

The sub-configuration repeats the data type the top-level configuration already declares, where the other side left it null.

## Explained by re-save: `config.text_config.dtype`

Original file: `config.json`.

Modified file: `config.json`.

The sub-configuration repeats the data type the top-level configuration already declares.

## Explained by re-save: `config.transformers_version`

Original file: `config.json`.

Modified file: `config.json`.

The saved version string changed.

## Explained by re-save: `config.vision_config.dtype`

Original file: `config.json`.

Modified file: `config.json`.

The sub-configuration repeats the data type the top-level configuration already declares, where the other side left it null.

The `default` template source differs beyond line endings and trailing whitespace.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: directional-per-layer-selected.
