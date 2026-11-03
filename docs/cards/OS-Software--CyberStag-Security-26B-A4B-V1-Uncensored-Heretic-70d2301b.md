# Stage 1: OS-Software/CyberStag-Security-26B-A4B-V1-Uncensored-Heretic

Original: `google/gemma-4-26b-a4b`

Verdict: **unexplained differences**

Revisions: modified `7f8b6884c9a9053e5fe616bba2c8107c1943ae2a`; original `24548b62aa021d562695c04aaf7758a1ea47990b`.

Changed fields:

- `special_token_ids.audio_token_id` (unexplained)
- `special_token_ids.boa_token_id` (unexplained)
- `special_token_ids.boi_token_id` (unexplained)
- `special_token_ids.bos_token_id` (unexplained)
- `special_token_ids.eoa_token_id` (unexplained)
- `special_token_ids.eoi_token_id` (unexplained)
- `special_token_ids.eos_token_id` (unexplained)
- `special_token_ids.image_token_id` (unexplained)
- `special_token_ids.pad_token_id` (unexplained)
- `special_token_ids.video_token_id` (unexplained)
- `vocabulary_size.config` (unexplained)
- `generation.eos_token_id` (unexplained)
- `config.architectures` (unexplained)
- `config.attention_k_eq_v` (unexplained)
- `config.enable_moe_block` (unexplained)
- `config.eoa_token_id` (unexplained)
- `config.eos_token_id` (unexplained)
- `config.final_logit_softcapping` (unexplained)
- `config.head_dim` (unexplained)
- `config.hidden_size` (unexplained)
- `config.hidden_size_per_layer_input` (unexplained)
- `config.intermediate_size` (unexplained)
- `config.max_position_embeddings` (unexplained)
- `config.model_type` (expected)
- `config.moe_intermediate_size` (unexplained)
- `config.num_attention_heads` (unexplained)
- `config.num_experts` (unexplained)
- `config.num_key_value_heads` (unexplained)
- `config.per_layer_config` (unexplained)
- `config.sliding_window` (unexplained)
- `config.text_config` (unexplained)
- `config.top_k_experts` (unexplained)
- `config.use_bidirectional_attention` (unexplained)
- `config.vision_config` (unexplained)
- `config.vision_soft_tokens_per_image` (unexplained)
- `template.default` (unexplained)

## Explained by re-save: `generation.transformers_version`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The saved version string changed.

## Explained by re-save: `config.attention_bias`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.22.1.

## Explained by re-save: `config.attention_dropout`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.22.1.

## Explained by re-save: `config.audio_config`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.22.1.

## Explained by re-save: `config.audio_token_id`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.22.1.

## Explained by re-save: `config.boa_token_id`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.22.1.

## Explained by re-save: `config.boi_token_id`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.22.1.

## Explained by re-save: `config.bos_token_id`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.22.1.

## Explained by re-save: `config.eoa_token_index`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.22.1.

## Explained by re-save: `config.eoi_token_id`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.22.1.

## Explained by re-save: `config.hidden_activation`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.22.1.

## Explained by re-save: `config.image_token_id`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.22.1.

## Explained by re-save: `config.layer_types`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.22.1.

## Explained by re-save: `config.num_hidden_layers`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.22.1.

## Explained by re-save: `config.num_kv_shared_layers`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.22.1.

## Explained by re-save: `config.pad_token_id`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.22.1.

## Explained by re-save: `config.rms_norm_eps`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.22.1.

## Explained by re-save: `config.rope_parameters`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.22.1.

## Explained by re-save: `config.transformers_version`

Original file: `config.json`.

Modified file: `config.json`.

The saved version string changed.

## Explained by re-save: `config.use_cache`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.22.1.

## Explained by re-save: `config.use_double_wide_mlp`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.22.1.

## Explained by re-save: `config.video_token_id`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.22.1.

## Explained by re-save: `config.vocab_size`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.22.1.

## Explained by re-save: `config.vocab_size_per_layer_input`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.22.1.

Missing evidence:

- original: chat template missing
- template default absent on one side

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: single-projection.
