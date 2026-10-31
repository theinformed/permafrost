# Stage 1: aifeifei798/Heretic-Scalpel-E2B

Original: `google/gemma-4-E2B-it`

Verdict: **unexplained differences**

Revisions: modified `49bd7340128e22f99f985106c8408ec80962ba2c`; original `3e22461f65e89153144f8adb70e3b8c2cc9845a7`.

Changed fields:

- `special_tokens.added_tokens_decoder:0` (unexplained)
- `special_tokens.added_tokens_decoder:1` (unexplained)
- `special_tokens.added_tokens_decoder:100` (unexplained)
- `special_tokens.added_tokens_decoder:101` (unexplained)
- `special_tokens.added_tokens_decoder:105` (unexplained)
- `special_tokens.added_tokens_decoder:106` (unexplained)
- `special_tokens.added_tokens_decoder:2` (unexplained)
- `special_tokens.added_tokens_decoder:255999` (unexplained)
- `special_tokens.added_tokens_decoder:256000` (unexplained)
- `special_tokens.added_tokens_decoder:258880` (unexplained)
- `special_tokens.added_tokens_decoder:258881` (unexplained)
- `special_tokens.added_tokens_decoder:258882` (unexplained)
- `special_tokens.added_tokens_decoder:258883` (unexplained)
- `special_tokens.added_tokens_decoder:258884` (unexplained)
- `special_tokens.added_tokens_decoder:3` (unexplained)
- `special_tokens.added_tokens_decoder:4` (unexplained)
- `special_tokens.added_tokens_decoder:46` (unexplained)
- `special_tokens.added_tokens_decoder:47` (unexplained)
- `special_tokens.added_tokens_decoder:48` (unexplained)
- `special_tokens.added_tokens_decoder:49` (unexplained)
- `special_tokens.added_tokens_decoder:50` (unexplained)
- `special_tokens.added_tokens_decoder:51` (unexplained)
- `special_tokens.added_tokens_decoder:52` (unexplained)
- `special_tokens.added_tokens_decoder:98` (unexplained)
- `added_tokens.decoder` (unexplained)
- `generation.eos_token_id` (unexplained)
- `config.dtype` (unexplained)
- `config.text_config.per_layer_config` (unexplained)
- `config.torch_dtype` (unexplained)
- `config.transformers_version` (unexplained)
- `template_source.tokenizer_config` (unexplained)

## Explained by re-save: `generation.transformers_version`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The saved version string changed.

## Explained by re-save: `config.audio_config.dtype`

Original file: `config.json`.

Modified file: `config.json`.

The sub-configuration repeats the data type the top-level configuration already declares.

## Explained by re-save: `config.audio_config.torch_dtype`

Original file: `config.json`.

Modified file: `config.json`.

The sub-configuration repeats the data type the top-level configuration already declares.

## Explained by re-save: `config.text_config.dtype`

Original file: `config.json`.

Modified file: `config.json`.

The sub-configuration repeats the data type the top-level configuration already declares.

## Explained by re-save: `config.text_config.moe_intermediate_size`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.6.2.

## Explained by re-save: `config.text_config.torch_dtype`

Original file: `config.json`.

Modified file: `config.json`.

The sub-configuration repeats the data type the top-level configuration already declares.

## Explained by re-save: `config.vision_config.dtype`

Original file: `config.json`.

Modified file: `config.json`.

The sub-configuration repeats the data type the top-level configuration already declares.

## Explained by re-save: `config.vision_config.torch_dtype`

Original file: `config.json`.

Modified file: `config.json`.

The sub-configuration repeats the data type the top-level configuration already declares.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: single-projection-selected.
