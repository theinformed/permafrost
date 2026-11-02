# Stage 1: densenet/Gemma-4-31B-StyleTune-heretic-ara

Original: `Gryphe/Gemma-4-31B-StyleTune`

Verdict: **unexplained differences**

Revisions: modified `dd58d6a1f0be22e0d81d368b8248d97f831a322a`; original `5a46842fc6c9f694683d985a275a3adc2973a213`.

Changed fields:

- `config.dtype` (unexplained)
- `config.model_name` (unexplained)
- `config.text_config.use_cache` (unexplained)
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

## Explained by re-save: `generation.transformers_version`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The saved version string changed.

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

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: directional-per-layer-selected.
