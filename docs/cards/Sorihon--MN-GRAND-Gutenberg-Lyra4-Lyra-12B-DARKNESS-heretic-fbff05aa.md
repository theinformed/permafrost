# Stage 1: Sorihon/MN-GRAND-Gutenberg-Lyra4-Lyra-12B-DARKNESS-heretic

Original: `DavidAU/MN-GRAND-Gutenberg-Lyra4-Lyra-12B-DARKNESS`

Verdict: **unexplained differences**

Revisions: modified `f6f51124e3aaa639ea26cf5e710075f784ad89c8`; original `acfc836e8a572b90fceb65f6408084ee40bbb077`.

Changed fields:

- `special_tokens.special_tokens_map.json:pad_token` (unexplained)
- `special_tokens.tokenizer_config.json:pad_token` (unexplained)
- `generation` (unexplained)
- `config._name_or_path` (expected)
- `config.dtype` (unexplained)
- `config.torch_dtype` (unexplained)

## Explained by re-save: `config.transformers_version`

Original file: `config.json`.

Modified file: `config.json`.

The saved version string changed.

## Explained by re-save: `template_source.tokenizer_config`

Original file: `tokenizer_config.json`.

Modified file: `chat_template.jinja`.

The template moved; line endings and trailing whitespace normalize equally, and the fixed conversation renders identically.

Missing evidence:

- original: generation_config.json missing

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: single-projection-selected.
