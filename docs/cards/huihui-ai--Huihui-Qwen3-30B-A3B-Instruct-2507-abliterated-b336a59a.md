# Stage 1: huihui-ai/Huihui-Qwen3-30B-A3B-Instruct-2507-abliterated

Original: `Qwen/Qwen3-30B-A3B-Instruct-2507`

Verdict: **unexplained differences**

Revisions: modified `e2f73ec7e99ee316beb8069ca90e4c3cbef8aa0f`; original `0d7cf23991f47feeb3a57ecb4c9cee8ea4a17bfe`.

Changed fields:

- `template_source.tokenizer_config` (unexplained)
- `template.default` (unexplained)

## Explained by re-save: `special_tokens.special_tokens_map.json:additional_special_tokens`

Original file: `tokenizer_config.json`, `tokenizer.json`.

Modified file: `special_tokens_map.json`.

The same token strings and IDs were declared in a separate file.

## Explained by re-save: `special_tokens.special_tokens_map.json:eos_token`

Original file: `tokenizer_config.json`, `tokenizer.json`.

Modified file: `special_tokens_map.json`.

The same token strings and IDs were declared in a separate file.

## Explained by re-save: `special_tokens.special_tokens_map.json:pad_token`

Original file: `tokenizer_config.json`, `tokenizer.json`.

Modified file: `special_tokens_map.json`.

The same token strings and IDs were declared in a separate file.

## Explained by re-save: `added_tokens.file`

Original file: `tokenizer.json`, `tokenizer_config.json`.

Modified file: `added_tokens.json`.

The added-token file repeats the existing strings and IDs.

The `default` template source differs beyond line endings and trailing whitespace.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.
