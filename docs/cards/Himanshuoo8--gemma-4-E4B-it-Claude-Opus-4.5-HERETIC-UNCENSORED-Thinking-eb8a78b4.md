# Stage 1: Himanshuoo8/gemma-4-E4B-it-Claude-Opus-4.5-HERETIC-UNCENSORED-Thinking

Original: `google/gemma-4-E4B-it`

Verdict: **unexplained differences**

Revisions: modified `5b80aaae7832c07d424dbb8188aa74b677e3404c`; original `fa62d88df2e6df5efa9d26ad6b3beaea2765f0cd`.

Changed fields:

- `special_token_ids.pad_token_id` (unexplained)
- `generation` (unexplained)
- `config.dtype` (unexplained)
- `config.model_name` (unexplained)
- `config.pad_token_id` (unexplained)
- `config.torch_dtype` (unexplained)
- `config.transformers_version` (unexplained)
- `config.unsloth_version` (unexplained)
- `template.default` (unexplained)
- `rendered_template.default` (unexplained)

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

The field is absent on the other side and loads as this same default in transformers 5.22.1.

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

The `default` template source differs beyond line endings and trailing whitespace.

The fixed conversation renders differently with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: single-projection-selected.
