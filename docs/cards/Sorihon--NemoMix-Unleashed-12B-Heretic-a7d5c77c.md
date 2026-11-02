# Stage 1: Sorihon/NemoMix-Unleashed-12B-Heretic

Original: `MarinaraSpaghetti/NemoMix-Unleashed-12B`

Verdict: **unexplained differences**

Revisions: modified `900a365f8b886154d36ba1f1c60334c2bf264e1b`; original `74fe434e22b840be8e258f0a810e826026ef5f12`.

Changed fields:

- `special_tokens.special_tokens_map.json:pad_token` (unexplained)
- `special_tokens.tokenizer_config.json:pad_token` (unexplained)
- `generation` (unexplained)
- `config._name_or_path` (expected)
- `config.dtype` (unexplained)
- `config.torch_dtype` (unexplained)
- `template.default` (unexplained)

## Explained by re-save: `config.transformers_version`

Original file: `config.json`.

Modified file: `config.json`.

The saved version string changed.

Missing evidence:

- original: chat template missing
- original: generation_config.json missing
- template default absent on one side

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: single-projection-selected.
