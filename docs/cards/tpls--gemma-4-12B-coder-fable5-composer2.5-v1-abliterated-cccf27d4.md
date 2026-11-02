# Stage 1: tpls/gemma-4-12B-coder-fable5-composer2.5-v1-abliterated

Original: `yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1`

Verdict: **unexplained differences**

Revisions: modified `6e57830b42b0f79de6c2ed080e8085659b33ea16`; original `237e5d8e72fb70e2c4d5df2676bc95308aad279c`.

Changed fields:

- `config.audio_config.dtype` (unexplained)
- `config.dtype` (unexplained)
- `config.text_config.dtype` (unexplained)
- `config.vision_config.dtype` (unexplained)

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

Weights: recipe_violations. Nearest recipe: single-projection-selected.
