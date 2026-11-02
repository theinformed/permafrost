# Stage 1: Paul691/gemma-4-12B-it-abliterated-uncensored

Original: `google/gemma-4-12B-it`

Verdict: **unexplained differences**

Revisions: modified `ad7d2c90e08ddffde4a163bc8de211ab57c01eb3`; original `707f0a3b8a3c7ad586ed01e27eafbad8a27dd0f7`.

Changed fields:

- `config.text_config.max_position_embeddings` (unexplained)
- `template.default` (unexplained)

The `default` template source differs beyond line endings and trailing whitespace.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: single-projection.
