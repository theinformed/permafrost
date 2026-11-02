# Stage 1: richardyoung/zephyr-7b-beta-abliterated

Original: `HuggingFaceH4/zephyr-7b-beta`

Verdict: **unexplained differences**

Revisions: modified `c464d32495613165f05411dd5ee8d17eb9e983d0`; original `892b3d7a7b1cf10c7a701c60881cd93df615734c`.

Changed fields:

- `special_tokens.special_tokens_map.json:bos_token` (unexplained)
- `special_tokens.special_tokens_map.json:eos_token` (unexplained)
- `special_tokens.special_tokens_map.json:pad_token` (unexplained)
- `special_tokens.special_tokens_map.json:unk_token` (unexplained)
- `generation.do_sample` (unexplained)
- `config._name_or_path` (expected)
- `config.dtype` (unexplained)
- `config.torch_dtype` (unexplained)

## Explained by re-save: `added_tokens.file`

Original file: `added_tokens.json`.

Modified file: `tokenizer.json`, `tokenizer_config.json`.

The added-token file repeats the existing strings and IDs.

## Explained by re-save: `generation.transformers_version`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The saved version string changed.

## Explained by re-save: `config.attention_dropout`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 4.56.2.

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

Weights: recipe_violations. Nearest recipe: directional-per-layer-selected.
