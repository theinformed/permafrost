# Stage 1: AISafety-Student/Ministral-3-8B-Reasoning-2512-heretic

Original: `mistralai/Ministral-3-8B-Reasoning-2512`

Verdict: **consistent with re-save noted**

Revisions: modified `1370bc503bbcb14af1b240dcec77e15165ce0f77`; original `6c2c4c82a395598a424f3a17555ae0cc19e3f5bb`.

## Explained by re-save: `special_tokens.added_tokens_decoder (1,000 entries)`

Original file: `tokenizer_config.json`.

Modified file: `tokenizer.json`.

The entry repeats the added-token record, with its ID and flags, of the tokenizer.json both sides share.

## Explained by re-save: `special_tokens.special_tokens_map.json:additional_special_tokens`

Original file: `special_tokens_map.json`.

Modified file: `tokenizer.json`.

Each listed token is declared special, under the same ID, in the tokenizer.json both sides share.

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

## Explained by re-save: `special_tokens.tokenizer_config.json:additional_special_tokens`

Original file: `tokenizer_config.json`.

Modified file: `tokenizer.json`.

Each listed token is declared special, under the same ID, in the tokenizer.json both sides share.

## Explained by re-save: `added_tokens.decoder`

Original file: `tokenizer_config.json`.

Modified file: `tokenizer.json`.

Every entry of the map repeats an added-token record of the tokenizer.json both sides share.

## Explained by re-save: `generation.transformers_version`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The saved version string changed.

## Explained by re-save: `config.text_config.bos_token_id`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 4.56.2.

## Explained by re-save: `config.text_config.dtype`

Original file: `config.json`.

Modified file: `config.json`.

The sub-configuration repeats the data type the top-level configuration already declares.

## Explained by re-save: `config.text_config.eos_token_id`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 4.56.2.

## Explained by re-save: `config.text_config.pad_token_id`

Original file: `generation_config.json`.

Modified file: `config.json`.

The sub-configuration repeats the value the generation settings already declare.

## Explained by re-save: `config.text_config.tie_word_embeddings`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 4.56.2.

## Explained by re-save: `config.tie_word_embeddings`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 4.56.2.

## Explained by re-save: `config.transformers_version`

Original file: `config.json`.

Modified file: `config.json`.

The saved version string changed.

## Explained by re-save: `config.vision_config.dtype`

Original file: `config.json`.

Modified file: `config.json`.

The sub-configuration repeats the data type the top-level configuration already declares.

## Explained by re-save: `config.vision_config.rope_theta`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 4.56.2.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: directional-per-layer-selected.
