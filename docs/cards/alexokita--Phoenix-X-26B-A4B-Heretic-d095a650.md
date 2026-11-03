# Stage 1: alexokita/Phoenix-X-26B-A4B-Heretic

Original: `Vortex5/Phoenix-X-26B-A4B`

Verdict: **unexplained differences**

Revisions: modified `e526f302e200e96af6fe81b677b470f743348314`; original `2ef31dd89f0bc38ed9f312868d979416d381721e`.

Changed fields:

- `generation` (unexplained)
- `config.text_config.per_layer_config` (unexplained)

## Explained by re-save: `config.transformers_version`

Original file: `config.json`.

Modified file: `config.json`.

The saved version string changed.

Missing evidence:

- original: generation_config.json missing

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: directional-per-layer-selected.
