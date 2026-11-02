# Stage 1: DogOnKeyboard/Mistral-7B-Heretic

Original: `mistralai/Mistral-7B-Instruct-v0.3`

Verdict: **unexplained differences**

Revisions: modified `40ce32fdd1e8151a5601ff06ebaa5cfb3ccd8049`; original `0d4b76e1efeb5eb6f6b5e757c79870472e04bd3a`.

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
