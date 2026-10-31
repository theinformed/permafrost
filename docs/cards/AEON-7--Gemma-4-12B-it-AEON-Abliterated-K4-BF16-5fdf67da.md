# Stage 1: AEON-7/Gemma-4-12B-it-AEON-Abliterated-K4-BF16

Original: `google/gemma-4-12B-it`

Verdict: **unexplained differences**

Revisions: modified `a8ac2860301dd24a53de42282694f809f7d033db`; original `66bc78a7534d523aa32004652cb02cc2e6354c62`.

Changed fields:

- `config.audio_config.audio_samples_per_token` (unexplained)
- `config.audio_config.dtype` (unexplained)
- `config.audio_config.hidden_size` (unexplained)
- `config.audio_config.output_proj_dims` (unexplained)
- `config.text_config.max_position_embeddings` (unexplained)
- `config.vision_config.dtype` (unexplained)
- `config.vision_config.model_patch_size` (unexplained)

## Explained by re-save: `config.text_config.dtype`

Original file: `config.json`.

Modified file: `config.json`.

The sub-configuration repeats the data type the top-level configuration already declares.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: directional-per-layer-selected.
