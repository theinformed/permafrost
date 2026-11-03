# Stage 1: Vortex5/Pantheon-Reasoning-26B-A4B-1.1-heretic

Original: `Gryphe/Pantheon-Reasoning-26B-A4B-1.1`

Verdict: **unexplained differences**

Revisions: modified `f1e4c4cf88e380918f473f25935641da989f0918`; original `9156318ccf35249e182e134254dcea0bef9e36cf`.

Changed fields:

- `config.dtype` (unexplained)
- `config.torch_dtype` (unexplained)
- `template_source.tokenizer_config` (unexplained)

## Explained by re-save: `generation.transformers_version`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The saved version string changed.

## Explained by re-save: `config.text_config.dtype`

Original file: `config.json`.

Modified file: `config.json`.

The sub-configuration repeats the data type the top-level configuration already declares.

## Explained by re-save: `config.text_config.torch_dtype`

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

The sub-configuration repeats the data type the top-level configuration already declares.

## Explained by re-save: `config.vision_config.torch_dtype`

Original file: `config.json`.

Modified file: `config.json`.

The sub-configuration repeats the data type the top-level configuration already declares.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: directional-per-layer-selected.
