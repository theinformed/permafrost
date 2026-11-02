# Stage 1: Dingdust/ContextPilot-E4B-heretic

Original: `google/gemma-4-E4B-it`

Verdict: **unexplained differences**

Revisions: modified `5bf557de36c7a90716c61df3ca1132fdf9600321`; original `ee0ef6023621cff504d758262d4e04895a5af4a2`.

Changed fields:

- `special_token_ids.bos_token_id` (unexplained)
- `special_token_ids.eos_token_id` (unexplained)
- `special_token_ids.pad_token_id` (unexplained)
- `config.bos_token_id` (unexplained)
- `config.eos_token_id` (unexplained)
- `config.pad_token_id` (unexplained)
- `config.text_config.global_head_dim` (unexplained)
- `config.text_config.num_global_key_value_heads` (unexplained)
- `config.text_config.per_layer_config` (unexplained)
- `template.default` (unexplained)

## Explained by re-save: `generation.transformers_version`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The saved version string changed.

## Explained by re-save: `config.text_config.moe_intermediate_size`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.22.1.

## Explained by re-save: `config.transformers_version`

Original file: `config.json`.

Modified file: `config.json`.

The saved version string changed.

Missing evidence:

- original template default render failed: TimeoutExpired: Command '['/p/work1/sdegan/model-audit/rounds/25/venv/bin/python', '-m', 'audit.template_worker']' timed out after 4 seconds

The `default` template source differs beyond line endings and trailing whitespace.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: single-projection-selected.
