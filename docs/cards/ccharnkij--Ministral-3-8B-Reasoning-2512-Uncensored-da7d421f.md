# Stage 1: ccharnkij/Ministral-3-8B-Reasoning-2512-Uncensored

Original: `mistralai/Ministral-3-8B-Reasoning-2512`

Verdict: **consistent with re-save noted**

Revisions: modified `4dca5a4f6ab07e2c66a8e11a581646f5c649cf1e`; original `6c2c4c82a395598a424f3a17555ae0cc19e3f5bb`.

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

Weights: recipe_violations. Nearest recipe: single-projection.
