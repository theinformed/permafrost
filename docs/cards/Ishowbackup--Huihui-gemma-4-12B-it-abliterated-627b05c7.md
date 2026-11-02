# Stage 1: Ishowbackup/Huihui-gemma-4-12B-it-abliterated

Original: `google/gemma-4-12B-it`

Verdict: **unexplained differences**

Revisions: modified `bbf6560eeec4340e557869d4f28f364d685f4c94`; original `707f0a3b8a3c7ad586ed01e27eafbad8a27dd0f7`.

Changed fields:

- `config.text_config.max_position_embeddings` (unexplained)
- `template.default` (unexplained)

The `default` template source differs beyond line endings and trailing whitespace.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_match. Nearest recipe: directional-per-layer-selected.
