# Stage 1: nchapman/Ministral-3-3B-Instruct-2512-heretic-BF16

Original: `mistralai/Ministral-3-3B-Base-2512`

Verdict: **unexplained differences**

Revisions: modified `ccaf95697ff9505c33b9f844aab636aac8eb6ffc`; original `6f9c4b12a95b139af68670a6713616b757923735`.

Changed fields:

- `template.default` (unexplained)

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

Missing evidence:

- original: chat template missing
- template default absent on one side

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: single-projection.
