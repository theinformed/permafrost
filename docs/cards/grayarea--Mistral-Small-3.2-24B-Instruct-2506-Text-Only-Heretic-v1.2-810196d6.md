# Stage 1: grayarea/Mistral-Small-3.2-24B-Instruct-2506-Text-Only-Heretic-v1.2

Original: `anthracite-core/Mistral-Small-3.2-24B-Instruct-2506-Text-Only`

Verdict: **unexplained differences**

Revisions: modified `ef3cefbf4fa4aaa3e9a1214a46eab3c6b1f99ca5`; original `c5ac8f3be7d522f4763bcafdb8939fb7527a7925`.

Changed fields:

- `config.dtype` (unexplained)
- `config.torch_dtype` (unexplained)

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
