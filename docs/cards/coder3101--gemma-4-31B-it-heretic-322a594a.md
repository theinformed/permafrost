# Stage 1: coder3101/gemma-4-31B-it-heretic

Original: `google/gemma-4-31B-it`

Verdict: **unexplained differences**

Revisions: modified `9a1c7f5d851541f279cd104329e093cb363cd9e7`; original `419b2efe421994fdfd3394e621983d4cc511cd4f`.

Changed fields:

- `template.default` (unexplained)

## Explained by re-save: `config.text_config.moe_intermediate_size`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.6.2.

The `default` template source differs beyond line endings and trailing whitespace.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: directional-per-layer-selected.
