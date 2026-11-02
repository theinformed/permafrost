# Stage 1: DuoNeural/Gemma-4-E4B-Heretic

Original: `google/gemma-4-E4B-it`

Verdict: **unexplained differences**

Revisions: modified `3e166f79b03070c843b56217eafae0ce4fb62c88`; original `c53e9d33178b12afbad4a48334d21e19b8c29761`.

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

Weights: recipe_violations. Nearest recipe: single-projection-selected.
