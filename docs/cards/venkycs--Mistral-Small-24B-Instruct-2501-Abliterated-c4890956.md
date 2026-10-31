# Stage 1: venkycs/Mistral-Small-24B-Instruct-2501-Abliterated

Original: `mistralai/Mistral-Small-24B-Instruct-2501`

Verdict: **unexplained differences**

Revisions: modified `dfaba92966388cd594f3fbe606b2228bfe917f50`; original `21b49d4bb2a78a7542629baf33e71e1b92e87fdf`.

Changed fields:

- `special_tokens.special_tokens_map.json:additional_special_tokens` (unexplained)
- `special_tokens.special_tokens_map.json:bos_token` (unexplained)
- `special_tokens.special_tokens_map.json:eos_token` (unexplained)
- `special_tokens.special_tokens_map.json:unk_token` (unexplained)
- `generation.do_sample` (unexplained)
- `template.default` (unexplained)
- `rendered_template.default` (unexplained)

The `default` template source differs beyond line endings and trailing whitespace.

The fixed conversation renders differently with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: single-projection-selected.
