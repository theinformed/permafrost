# Stage 1: claymorecrystal/gemma-4-26B-A4B-it-uncensored

Original: `google/gemma-4-26B-A4B-it`

Verdict: **unexplained differences**

Revisions: modified `b6c448d5f2f4da71d815da02a62ec6970c9ca832`; original `20da991ab4afab98e8f910c4a2e8f4fbefc404ad`.

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

Weights: recipe_violations. Nearest recipe: directional-per-layer.
