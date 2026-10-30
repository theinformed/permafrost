# Stage 1: coder3101/gemma-4-E4B-it-heretic

Original: `google/gemma-4-E4B-it`

Verdict: **unexplained differences**

Revisions: modified `24a5d4b1967adfb1421ba8125ce5f05b7214b5ab`; original `292a7e278a400932df35f9fd4b1501edd04133a5`.

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
