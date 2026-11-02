# Stage 1: Sorihon/Dans-PersonalityEngine-V1.3.0-12B-Heretic

Original: `PocketDoc/Dans-PersonalityEngine-V1.3.0-12b`

Verdict: **unexplained differences**

Revisions: modified `eda0adf1237575dea8b86696eafe6b6cebb146ae`; original `62004ca4b58a2f27b8f390cc1f64b9055464ab21`.

Changed fields:

- `config.dtype` (unexplained)
- `config.torch_dtype` (unexplained)
- `config.use_cache` (unexplained)

## Explained by re-save: `generation.transformers_version`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The saved version string changed.

## Explained by re-save: `config.transformers_version`

Original file: `config.json`.

Modified file: `config.json`.

The saved version string changed.

## Explained by re-save: `template_source.tokenizer_config`

Original file: `tokenizer_config.json`.

Modified file: `chat_template.jinja`.

The template moved; line endings and trailing whitespace normalize equally, and the fixed conversation renders identically.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: directional-per-layer-selected.
