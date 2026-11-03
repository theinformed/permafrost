# Stage 1: keithtyser/gemma-4-26B-A4B-it-local-abliterated-sota-internal-t34

Original: `google/gemma-4-26B-A4B-it`

Verdict: **unexplained differences**

Revisions: modified `38b6875ce855a5d664cce543b7e3729af407ada2`; original `4c55b528bdc40b4e79ed7fd4e2f8e46fa5aaed5a`.

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

Weights: recipe_violations. Nearest recipe: directional-per-layer-selected.
