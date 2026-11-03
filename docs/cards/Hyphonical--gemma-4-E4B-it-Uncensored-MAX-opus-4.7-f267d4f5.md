# Stage 1: Hyphonical/gemma-4-E4B-it-Uncensored-MAX-opus-4.7

Original: `prithivMLmods/gemma-4-E4B-it-Uncensored-MAX`

Verdict: **unexplained differences**

Revisions: modified `af78a5292cdd704257e02540dbb9bcb0b769820a`; original `a236367acd38efb74098113aff9590ccc6b037b7`.

Changed fields:

- `special_token_ids.pad_token_id` (unexplained)
- `generation` (unexplained)
- `config.dtype` (unexplained)
- `config.model_name` (unexplained)
- `config.pad_token_id` (unexplained)
- `config.torch_dtype` (unexplained)
- `config.transformers_version` (unexplained)
- `config.unsloth_version` (unexplained)
- `template_source.tokenizer_config` (unexplained)

## Explained by re-save: `special_tokens.added_tokens_decoder (24 entries)`

Original file: `tokenizer.json`.

Modified file: `tokenizer_config.json`.

The entry repeats the added-token record, with its ID and flags, of the tokenizer.json both sides share.

## Explained by re-save: `added_tokens.decoder`

Original file: `tokenizer.json`.

Modified file: `tokenizer_config.json`.

Every entry of the map repeats an added-token record of the tokenizer.json both sides share.

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

Missing evidence:

- modified: generation_config.json missing

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: single-projection.
