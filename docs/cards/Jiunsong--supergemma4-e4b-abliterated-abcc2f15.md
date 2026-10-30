# Stage 1: Jiunsong/supergemma4-e4b-abliterated

Original: `google/gemma-4-E4B-it`

Verdict: **unexplained differences**

Revisions: modified `5b76a44bbdede3e5b3c26d5aa8987836224ce69a`; original `83df0a889143b1dbfc61b591bbc639540fd9ce4c`.

Changed fields:

- `special_token_ids.eos_token_id` (unexplained)
- `config.eos_token_id` (unexplained)
- `config.vision_config` (unexplained)
- `template_source.tokenizer_config` (unexplained)
- `template.default` (unexplained)
- `rendered_template.default` (unexplained)

The `default` template source differs beyond line endings and trailing whitespace.

The fixed conversation renders differently with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: single-projection.
