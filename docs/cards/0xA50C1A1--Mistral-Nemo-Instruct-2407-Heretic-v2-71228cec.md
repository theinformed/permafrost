# Stage 1: 0xA50C1A1/Mistral-Nemo-Instruct-2407-Heretic-v2

Original: `unsloth/Mistral-Nemo-Instruct-2407`

Verdict: **unexplained differences**

Revisions: modified `bfa85c3d2b16cf0edaa2b0724be6135959930aab`; original `e9976040f42d8a5590ed58cefe973061b3f973b5`.

Changed fields:

- `config._name_or_path` (expected)
- `config.dtype` (unexplained)
- `config.rope_theta` (unexplained)
- `config.torch_dtype` (unexplained)
- `template.default` (unexplained)

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

## Explained by re-save: `config.rope_parameters`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side, and both saved configurations load it as this same value in transformers 5.22.1.

## Explained by re-save: `config.transformers_version`

Original file: `config.json`.

Modified file: `config.json`.

The saved version string changed.

Missing evidence:

- modified template default render failed: ValueError: TemplateSyntaxError: Encountered unknown tag 'generation'. Jinja was looking for the following tags: 'elif' or 'else' or 'endif'. The innermost block that needs to be closed is 'if'.

The `default` template source differs beyond line endings and trailing whitespace.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: single-projection-selected.
