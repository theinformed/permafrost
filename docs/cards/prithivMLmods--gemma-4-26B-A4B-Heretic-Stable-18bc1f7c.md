# Stage 1: prithivMLmods/gemma-4-26B-A4B-Heretic-Stable

Original: `google/gemma-4-26B-A4B-it`

Verdict: **unexplained differences**

Revisions: modified `f675892e7feda2b95e6d678c59ffed2bc50f650c`; original `b2a81a03d25f927590a91d84ba43f96e8ef7349f`.

Changed fields:

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

Weights: recipe_match. Nearest recipe: single-projection-selected.
