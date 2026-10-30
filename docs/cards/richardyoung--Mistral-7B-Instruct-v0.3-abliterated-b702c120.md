# Stage 1: richardyoung/Mistral-7B-Instruct-v0.3-abliterated

Original: `mistralai/Mistral-7B-Instruct-v0.3`

Verdict: **unexplained differences**

Revisions: modified `cb427700df6896f0a9fdf2de6f7bd9b4f6dffa88`; original `c170c708c41dac9275d15a8fff4eca08d52bab71`.

Changed fields:

- `special_tokens.special_tokens_map.json:pad_token` (unexplained)
- `special_tokens.tokenizer_config.json:pad_token` (unexplained)
- `config.dtype` (unexplained)
- `config.torch_dtype` (unexplained)

## Explained by re-save: `generation.transformers_version`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The saved version string changed.

## Explained by re-save: `config.head_dim`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 4.56.2.

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

Weights: recipe_violations. Nearest recipe: single-projection-selected.
