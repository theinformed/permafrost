# Stage 1: chulcher/gemma-4-e4b-abliterated

Original: `google/gemma-4-E4B`

Verdict: **unexplained differences**

Revisions: modified `627232c914a3b14eff301937af73ef70e4a9ea86`; original `7aa32e6889efd6300124851b164f8b364314c3d8`.

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

- original: chat template missing
- template default absent on one side

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: directional-per-layer-selected.
