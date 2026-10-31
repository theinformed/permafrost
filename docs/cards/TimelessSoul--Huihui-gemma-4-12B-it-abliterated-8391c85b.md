# Stage 1: TimelessSoul/Huihui-gemma-4-12B-it-abliterated

Original: `google/gemma-4-12B-it`

Verdict: **unexplained differences**

Revisions: modified `b4e4d2481d2ec02825165e7a967644c5d2522c26`; original `707f0a3b8a3c7ad586ed01e27eafbad8a27dd0f7`.

Changed fields:

- `config.text_config.max_position_embeddings` (unexplained)
- `template.default` (unexplained)

The `default` template source differs beyond line endings and trailing whitespace.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_match. Nearest recipe: directional-per-layer-selected.
