# Stage 1: llmfan46/gemma-4-31B-it-uncensored-heretic

Original: `google/gemma-4-31B-it`

Verdict: **unexplained differences**

Revisions: modified `d5bfc0d99e308beb9805440806161ad0233df357`; original `842da3794eaa0b77d5f08bae87a17459d91ff475`.

Changed fields:

- `config.text_config.moe_intermediate_size` (unexplained)
- `template.default` (unexplained)
- `rendered_template.default` (unexplained)

## Explained by re-save: `generation.transformers_version`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The saved version string changed.

## Explained by re-save: `config.transformers_version`

Original file: `config.json`.

Modified file: `config.json`.

The saved version string changed.

The `default` template source differs beyond line endings and trailing whitespace.

The fixed conversation renders differently with the `default` template.

This metadata audit does not certify the absence of hidden behavior.
