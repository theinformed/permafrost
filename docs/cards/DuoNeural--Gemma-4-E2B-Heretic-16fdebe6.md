# Stage 1: DuoNeural/Gemma-4-E2B-Heretic

Original: `google/gemma-4-E2B-it`

Verdict: **unexplained differences**

Revisions: modified `39221ce2907a82425170a733eebcb86663cbcb3b`; original `6b7e72c67d3c4556f42b56d5a68b4b8e864c63b4`.

Changed fields:

- `template.default` (unexplained)

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

Missing evidence:

- modified: chat template missing
- template default absent on one side

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_match. Nearest recipe: single-projection-selected.
