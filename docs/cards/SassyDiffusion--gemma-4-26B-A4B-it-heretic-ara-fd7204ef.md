# Stage 1: SassyDiffusion/gemma-4-26B-A4B-it-heretic-ara

Original: `google/gemma-4-26B-A4B-it`

Verdict: **unexplained differences**

Revisions: modified `328148e97b97802a15792688fb1a3b68ecd6e500`; original `47b6801b24d15ff9bcd8c96dfaea0be9ed3a0301`.

Changed fields:

- `special_tokens.tokenizer_config.json:eos_token` (unexplained)
- `special_token_ids.eos_token_id` (unexplained)
- `special_token_ids.pad_token_id` (unexplained)
- `config.eos_token_id` (unexplained)
- `config.pad_token_id` (unexplained)
- `config.unsloth_fixed` (unexplained)

## Explained by re-save: `generation.transformers_version`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The saved version string changed.

## Explained by re-save: `config.transformers_version`

Original file: `config.json`.

Modified file: `config.json`.

The saved version string changed.

## Explained by re-save: `template.default`

Original file: `chat_template.jinja@4c55b528`.

Modified file: `chat_template.jinja`.

The template equals the original repository's own later revision 4c55b528 (2026-04-28, "fix(chat_template): update SI and tool call handling (#36)"), and the fixed conversation renders identically.

The `default` template source differs beyond line endings and trailing whitespace.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: directional-per-layer-selected.
