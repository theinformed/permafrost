# Stage 1: Madras1/Gemma-4-E4B-Abliterated-Uncensored

Original: `google/gemma-4-E4B-it`

Verdict: **unexplained differences**

Revisions: modified `b7a3f3ae60fa8a961f09ed786dad78c6c1adbd2d`; original `ee0ef6023621cff504d758262d4e04895a5af4a2`.

Changed fields:

- `special_tokens.tokenizer_config.json:eos_token` (unexplained)
- `special_token_ids.eos_token_id` (unexplained)
- `special_token_ids.pad_token_id` (unexplained)
- `config.eos_token_id` (unexplained)
- `config.pad_token_id` (unexplained)
- `config.text_config.per_layer_config` (unexplained)
- `config.unsloth_fixed` (unexplained)
- `template.default` (unexplained)

## Explained by re-save: `generation.transformers_version`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The saved version string changed.

## Explained by re-save: `config.text_config.global_head_dim`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.6.2.

## Explained by re-save: `config.text_config.moe_intermediate_size`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.6.2.

## Explained by re-save: `config.text_config.num_global_key_value_heads`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.6.2.

## Explained by re-save: `config.transformers_version`

Original file: `config.json`.

Modified file: `config.json`.

The saved version string changed.

The `default` template source differs beyond line endings and trailing whitespace.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: single-projection-selected.
