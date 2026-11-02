# Stage 1: SubMaroon/Gemma-4-26B-A4B-StyleTune-QK-Heretic

Original: `Gryphe/Gemma-4-26B-A4B-StyleTune-V2`

Verdict: **unexplained differences**

Revisions: modified `1c802dffcb8f13b8a5d2779b35e7e6232d350ed4`; original `f34ba405740e0933f9b859c746de559ce1036958`.

Changed fields:

- `special_token_ids.eos_token_id` (unexplained)
- `special_token_ids.pad_token_id` (unexplained)
- `config.eos_token_id` (unexplained)
- `config.pad_token_id` (unexplained)
- `config.unsloth_fixed` (unexplained)
- `template_source.tokenizer_config` (unexplained)
- `template.default` (unexplained)

## Explained by re-save: `generation.transformers_version`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The saved version string changed.

## Explained by re-save: `config.transformers_version`

Original file: `config.json`.

Modified file: `config.json`.

The saved version string changed.

The `default` template source differs beyond line endings and trailing whitespace.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: single-projection-selected.
