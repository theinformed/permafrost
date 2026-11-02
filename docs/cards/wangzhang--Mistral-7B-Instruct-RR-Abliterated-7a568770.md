# Stage 1: wangzhang/Mistral-7B-Instruct-RR-Abliterated

Original: `GraySwanAI/Mistral-7B-Instruct-RR`

Verdict: **unexplained differences**

Revisions: modified `180527d8c93a698d3112f70ca58d24cd7042b99a`; original `5b9121dab26cdbf988127a6fd0305520e4a15b92`.

Changed fields:

- `special_tokens.added_tokens_decoder:0` (unexplained)
- `special_tokens.added_tokens_decoder:1` (unexplained)
- `special_tokens.added_tokens_decoder:2` (unexplained)
- `special_tokens.tokenizer_config.json:additional_special_tokens` (unexplained)
- `special_token_ids.pad_token_id` (unexplained)
- `added_tokens.decoder` (unexplained)
- `config._name_or_path` (expected)
- `config.dtype` (unexplained)
- `config.rope_theta` (unexplained)
- `config.torch_dtype` (unexplained)
- `template_source.tokenizer_config` (unexplained)

## Explained by re-save: `special_tokens.special_tokens_map.json:bos_token`

Original file: `special_tokens_map.json`.

Modified file: `tokenizer_config.json`, `tokenizer.json`.

The same token strings and IDs were declared in a separate file.

## Explained by re-save: `special_tokens.special_tokens_map.json:eos_token`

Original file: `special_tokens_map.json`.

Modified file: `tokenizer_config.json`, `tokenizer.json`.

The same token strings and IDs were declared in a separate file.

## Explained by re-save: `special_tokens.special_tokens_map.json:pad_token`

Original file: `special_tokens_map.json`.

Modified file: `tokenizer_config.json`, `tokenizer.json`.

The same token strings and IDs were declared in a separate file.

## Explained by re-save: `special_tokens.special_tokens_map.json:unk_token`

Original file: `special_tokens_map.json`.

Modified file: `tokenizer_config.json`, `tokenizer.json`.

The same token strings and IDs were declared in a separate file.

## Explained by re-save: `generation.transformers_version`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The saved version string changed.

## Explained by re-save: `config.head_dim`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.22.1.

## Explained by re-save: `config.pad_token_id`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 4.56.2.

## Explained by re-save: `config.rope_parameters`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side, and both saved configurations load it as this same value in transformers 5.22.1.

## Explained by re-save: `config.transformers_version`

Original file: `config.json`.

Modified file: `config.json`.

The saved version string changed.

Missing evidence:

- modified template default render failed: ValueError: ValueError: Conversation roles must alternate user/assistant/user/assistant/...
- original template default render failed: ValueError: ValueError: Conversation roles must alternate user/assistant/user/assistant/...

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: single-projection-selected.
