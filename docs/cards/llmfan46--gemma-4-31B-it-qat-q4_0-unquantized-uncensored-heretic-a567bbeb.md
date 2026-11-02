# Stage 1: llmfan46/gemma-4-31B-it-qat-q4_0-unquantized-uncensored-heretic

Original: `google/gemma-4-31B-it-qat-q4_0-unquantized`

Verdict: **unexplained differences**

Revisions: modified `ce415cf3ceaee8f1bdf57563b4dac279da83fcd3`; original `4f926903562062220b3e54c1385c5ef2cd40bfd1`.

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
