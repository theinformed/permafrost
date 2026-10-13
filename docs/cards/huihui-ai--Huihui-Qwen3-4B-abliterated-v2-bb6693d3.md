# Stage 1: huihui-ai/Huihui-Qwen3-4B-abliterated-v2

Original: `Qwen/Qwen3-4B`

Verdict: **unexplained differences**

Revisions: modified `a494c65b10bf8fdc56c0ff11d36987c1d018f162`; original `1cfa9a7208912126459214e8b04321603b3df60c`.

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

## Explained by re-save: `generation.transformers_version`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The saved version string changed.

## Explained by re-save: `config.transformers_version`

Original file: `config.json`.

Modified file: `config.json`.

The saved version string changed.

The `default` template source differs beyond line endings and trailing whitespace.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.
