# Stage 1: Tetratype/Gemma-4-26B-A4B-it-heretic-antislop

Original: `coder3101/gemma-4-26B-A4B-it-heretic`

Verdict: **unexplained differences**

Revisions: modified `5a9793e1959cb2d323fa8325478ca2d896f843da`; original `e6d09d5c434a5e91326ce9d779786a91e7aaae35`.

Changed fields:

- `special_token_ids.bos_token_id` (unexplained)
- `special_token_ids.eos_token_id` (unexplained)
- `special_token_ids.pad_token_id` (unexplained)
- `generation.eos_token_id` (unexplained)
- `config.bos_token_id` (unexplained)
- `config.dtype` (unexplained)
- `config.eos_token_id` (unexplained)
- `config.model_name` (unexplained)
- `config.pad_token_id` (unexplained)
- `config.unsloth_version` (unexplained)
- `config.use_cache` (unexplained)

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
