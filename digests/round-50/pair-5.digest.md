# Pair 5 digest

## Pair
- modified: nbeerbower/A0l-12B-heretic @ 6fb2dcabd5711eaa52ceea55cba5660202419f8c
- original: nbeerbower/Schreiber-mistral-nemo-12B @ ed0d372a0432cb4e08118911bf572e221955a051
- receipt: pair 5, measurement_sha256 60552b3a
- job, node, seconds: not carried

## Metadata
- verdict: unexplained differences
- differences: 13 (explained by re-save 8, unexplained 5)
  - special_tokens.special_tokens_map.json:bos_token: {'value': {'content': '<s>', 'lstrip': False, 'normalized... -> null
  - special_tokens.special_tokens_map.json:eos_token: {'value': {'content': '<|im_end|>', 'lstrip': False, 'nor... -> null
  - special_tokens.special_tokens_map.json:pad_token: {'value': '<|im_end|>', 'ids': [4]} -> null
  - special_tokens.special_tokens_map.json:unk_token: {'value': {'content': '<unk>', 'lstrip': False, 'normaliz... -> null
  - special_token_ids.pad_token_id: null -> null
  - generation.transformers_version: 4.51.3 -> 5.2.0
  - config.dtype: null -> bfloat16
  - config.pad_token_id: null -> null
  - config.rope_parameters: null -> {'rope_theta': 1000000.0, 'rope_type': 'default'}
  - config.rope_theta: 1e+06 -> null
  - config.torch_dtype: bfloat16 -> null
  - config.transformers_version: 4.51.3 -> 5.2.0
  - template_source.tokenizer_config: {% if not add_generation_prompt is defined %}{% set add_g... -> null
- limitation: This metadata audit does not certify the absence of hidden behavior.
- card headings: ## Explained by re-save: `special_tokens.special_tokens_map.json:bos_token`, ## Explained by re-save: `special_tokens.special_tokens_map.json:eos_token`, ## Explained by re-save: `special_tokens.special_tokens_map.json:pad_token`, ## Explained by re-save: `special_tokens.special_tokens_map.json:unk_token`, ## Explained by re-save: `generation.transformers_version`, ## Explained by re-save: `config.pad_token_id`, ## Explained by re-save: `config.transformers_version`, ## Explained by re-save: `template_source.tokenizer_config`

## Weights assessment
- summary: assessment recipe_violations, matched_tensors 363, max_relative_difference_outside_changed_set 0, max_relative_difference_outside_recipe_set 0.0138, min_first_singular_energy_share 0.08657
- threshold: 0.001
- nearest recipe: single-projection, matched false
  - single-projection: matched false, 361 violations
  - single-projection-selected: matched false, 361 violations
  - directional-per-layer: matched false, 480 violations
  - directional-per-layer-selected: matched false, 480 violations
- schema_version 1; scope: Weight differences alone cannot certify the absence of hidden behavior.

## Changed tensors
| kind | changed/total | layers | relative change | first share | positive fraction |
| --- | --- | --- | --- | --- | --- |
| attention_key | 40/40 | 0-39 | 0.002788 / 0.004878 / 0.008042 | 0.1681 / 0.2918 / 0.6049 | 0.2759 / 0.3308 / 0.3886 |
| attention_output | 40/40 | 0-39 | 0.005482 / 0.02023 / 0.04933 | 0.1586 / 0.869 / 0.9872 | 0.3443 / 0.4276 / 0.4409 |
| attention_query | 40/40 | 0-39 | 0.003996 / 0.005851 / 0.01034 | 0.1916 / 0.3864 / 0.6577 | 0.303 / 0.3492 / 0.3974 |
| attention_value | 40/40 | 0-39 | 0.003436 / 0.006395 / 0.007524 | 0.207 / 0.3614 / 0.7075 | 0.2694 / 0.3525 / 0.379 |
| feed_forward_down | 40/40 | 0-39 | 0.002582 / 0.007678 / 0.02084 | 0.1098 / 0.7182 / 0.9642 | 0.2323 / 0.3545 / 0.4089 |
| feed_forward_gate | 40/40 | 0-39 | 0.004439 / 0.008979 / 0.0138 | 0.09821 / 0.6461 / 0.8403 | 0.3121 / 0.3806 / 0.4115 |
| feed_forward_up | 40/40 | 0-39 | 0.004894 / 0.00727 / 0.008663 | 0.08657 / 0.4089 / 0.5966 | 0.3256 / 0.3689 / 0.3826 |
- unchanged kinds: embedding 0/1, final_normalization 0/1, input_normalization 0/40, output_head 0/1, post_attention_normalization 0/40
- exactly-0 changed tensors: none

## Directions
| group | count | median cosine | min cosine | median_direction_defined |
| --- | --- | --- | --- | --- |
| feed_forward_down:5120 | 40 | 0.4641 | 0.01185 | true |
| feed_forward_gate:14336 | 40 | 0.1291 | 0.106 | true |
| feed_forward_up:14336 | 40 | 0.1285 | 0.1093 | true |
| attention_key:1024 | 40 | 0.122 | 0.0679 | true |
| attention_output:5120 | 40 | 0.6109 | 0.000207 | true |
| attention_query:4096 | 40 | 0.126 | 0.0957 | true |
| attention_value:1024 | 40 | 0.1318 | 0.06658 | true |
- svd: seed 0, top_k 8, sketch_columns 12, power_iterations 4
- unused_shared_kv 0, original_only 0, modified_only 0, dropped_towers 0, dropped_statistics 0

## Oddities
- none
