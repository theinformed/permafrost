# Stage 1: Mitchins/gemma-4-26B-A4B-it-qat-q4_0-unquantized-uncensored-heretic

Original: `google/gemma-4-26B-A4B-it-qat-q4_0-unquantized`

Verdict: **unexplained differences**

Revisions: modified `d62fa836581401beafd08fdd624927e31dcac6ee`; original `f1e06dc520982d9b9edd76859fdb7ab209449949`.

Changed fields:

- `generation._from_model_config` (unexplained)
- `generation.do_sample` (unexplained)
- `generation.eos_token_id` (unexplained)
- `generation.top_k` (unexplained)
- `generation.top_p` (unexplained)
- `config.text_config.global_head_dim` (unexplained)
- `config.text_config.num_global_key_value_heads` (unexplained)
- `config.text_config.per_layer_config` (unexplained)

## Explained by re-save: `generation.output_attentions`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The field is absent on the other side and loads as this same default in transformers 4.56.2.

## Explained by re-save: `generation.output_hidden_states`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The field is absent on the other side and loads as this same default in transformers 4.56.2.

## Explained by re-save: `generation.temperature`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The field is absent on the other side and loads as this same default in transformers 4.56.2.

## Explained by re-save: `generation.transformers_version`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The saved version string changed.

## Explained by re-save: `generation.use_cache`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The field is absent on the other side and loads as this same default in transformers 4.56.2.

## Explained by re-save: `config.transformers_version`

Original file: `config.json`.

Modified file: `config.json`.

The saved version string changed.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: directional-per-layer-selected.
