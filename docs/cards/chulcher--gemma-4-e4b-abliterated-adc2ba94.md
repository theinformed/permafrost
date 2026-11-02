# Stage 1: chulcher/gemma-4-e4b-abliterated

Original: `google/gemma-4-E4B-it`

Verdict: **unexplained differences**

Revisions: modified `627232c914a3b14eff301937af73ef70e4a9ea86`; original `292a7e278a400932df35f9fd4b1501edd04133a5`.

Changed fields:

- `special_token_ids.eos_token_id` (unexplained)
- `generation.eos_token_id` (unexplained)
- `config.eos_token_id` (unexplained)

## Explained by re-save: `generation.transformers_version`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The saved version string changed.

## Explained by re-save: `config.text_config.moe_intermediate_size`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.22.1.

## Explained by re-save: `config.transformers_version`

Original file: `config.json`.

Modified file: `config.json`.

The saved version string changed.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: single-projection.
