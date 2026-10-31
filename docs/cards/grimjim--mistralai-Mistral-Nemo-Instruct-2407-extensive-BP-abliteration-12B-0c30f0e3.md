# Stage 1: grimjim/mistralai-Mistral-Nemo-Instruct-2407-extensive-BP-abliteration-12B

Original: `mistralai/Mistral-Nemo-Instruct-2407`

Verdict: **unexplained differences**

Revisions: modified `6f0527c3ee3ed06d139087a1478c9b53925f3084`; original `04d8a90549d23fc6bd7f642064003592df51e9b3`.

Changed fields:

- `config.dtype` (unexplained)
- `config.torch_dtype` (unexplained)

## Explained by re-save: `generation.transformers_version`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The saved version string changed.

## Explained by re-save: `config.transformers_version`

Original file: `config.json`.

Modified file: `config.json`.

The saved version string changed.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: directional-per-layer-selected.
