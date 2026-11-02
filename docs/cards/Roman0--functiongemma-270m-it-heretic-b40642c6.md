# Stage 1: Roman0/functiongemma-270m-it-heretic

Original: `google/functiongemma-270m-it`

Verdict: **unexplained differences**

Revisions: modified `93ba3ac2f806bd7907b3a081f521a56129509af6`; original `ead2a1f9df8d6431408ccff6c9e5e60028addde0`.

Changed fields:

- `special_tokens.added_tokens_decoder:255999` (unexplained)
- `special_tokens.added_tokens_decoder:50` (unexplained)
- `special_tokens.tokenizer.json:255999` (unexplained)
- `special_tokens.tokenizer.json:50` (unexplained)
- `added_tokens.decoder` (unexplained)
- `added_tokens.file` (unexplained)
- `added_tokens.tokenizer` (unexplained)

## Explained by re-save: `config.rope_scaling`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 4.56.2.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_match. Nearest recipe: directional-per-layer-selected.
