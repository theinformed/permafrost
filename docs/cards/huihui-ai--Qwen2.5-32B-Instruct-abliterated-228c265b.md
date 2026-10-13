# Stage 1: huihui-ai/Qwen2.5-32B-Instruct-abliterated

Original: `Qwen/Qwen2.5-32B-Instruct`

Verdict: **unexplained differences**

Revisions: modified `546fc40530371049c02d9ed8abc95f65a6d69936`; original `5ede1c97bbab6ce5cda5812749b4c0bdf79b18dd`.

Changed fields:

- `special_tokens.special_tokens_map.json:pad_token` (unexplained)
- `special_tokens.tokenizer_config.json:pad_token` (unexplained)

## Explained by re-save: `special_tokens.special_tokens_map.json:additional_special_tokens`

Original file: `tokenizer_config.json`, `tokenizer.json`.

Modified file: `special_tokens_map.json`.

The same token strings and IDs were declared in a separate file.

## Explained by re-save: `special_tokens.special_tokens_map.json:eos_token`

Original file: `tokenizer_config.json`, `tokenizer.json`.

Modified file: `special_tokens_map.json`.

The same token strings and IDs were declared in a separate file.

## Explained by re-save: `added_tokens.file`

Original file: `tokenizer.json`, `tokenizer_config.json`.

Modified file: `added_tokens.json`.

The added-token file repeats the existing strings and IDs.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.
