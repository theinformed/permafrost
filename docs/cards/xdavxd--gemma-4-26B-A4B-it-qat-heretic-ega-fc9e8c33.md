# Stage 1: xdavxd/gemma-4-26B-A4B-it-qat-heretic-ega

Original: `google/gemma-4-26B-A4B-it-qat-q4_0-unquantized`

Verdict: **unexplained differences**

Revisions: modified `e4f7ab9009fbf503fb7ed41f45cfca47d48489e6`; original `f1e06dc520982d9b9edd76859fdb7ab209449949`.

Changed fields:

- `config.text_config.global_head_dim` (unexplained)
- `config.text_config.num_global_key_value_heads` (unexplained)
- `config.text_config.per_layer_config` (unexplained)

## Explained by re-save: `config.transformers_version`

Original file: `config.json`.

Modified file: `config.json`.

The saved version string changed.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: directional-per-layer.
