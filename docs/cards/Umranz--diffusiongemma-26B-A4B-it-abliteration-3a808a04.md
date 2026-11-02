# Stage 1: Umranz/diffusiongemma-26B-A4B-it-abliteration

Original: `google/diffusiongemma-26B-A4B-it`

Verdict: **unexplained differences**

Revisions: modified `082d18f9cf07be7f6b52ba7f517fc737e78f9e0c`; original `156b5c867b42d726d32654a8ad505e72c623bbcc`.

Changed fields:

- `generation.return_dict_in_generate` (unexplained)

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
