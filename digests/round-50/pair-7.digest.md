# Pair 7 digest

## Pair
- modified: grayarea/Mistral-Small-3.2-24B-Instruct-2506-Heretic-v1.2-2 @ 959337d3004f48565a2c805a09c8ca40790656d7
- original: unsloth/Mistral-Small-3.2-24B-Instruct-2506 @ 3ed8d341b53ea3d0e4194689905477688a6cf733
- receipt: pair 7, measurement_sha256 997d082b
- job, node, seconds: not carried

## Metadata
- verdict: unexplained differences
- differences: 10 (explained by re-save 6, unexplained 4)
  - generation.transformers_version: 4.55.4 -> 4.57.3
  - config.dtype: null -> bfloat16
  - config.grayarea: null -> {'url': 'https://huggingface.co/grayarea/Mistral-Small-3....
  - config.text_config.dtype: null -> bfloat16
  - config.text_config.torch_dtype: bfloat16 -> null
  - config.torch_dtype: bfloat16 -> null
  - config.transformers_version: 4.55.4 -> 4.57.3
  - config.vision_config.dtype: null -> bfloat16
  - config.vision_config.torch_dtype: bfloat16 -> null
  - template_source.tokenizer_config: {#- Unsloth template fixes #} {%- set yesterday_day = str... -> null
- limitation: This metadata audit does not certify the absence of hidden behavior.
- card headings: ## Explained by re-save: `generation.transformers_version`, ## Explained by re-save: `config.text_config.dtype`, ## Explained by re-save: `config.text_config.torch_dtype`, ## Explained by re-save: `config.transformers_version`, ## Explained by re-save: `config.vision_config.dtype`, ## Explained by re-save: `config.vision_config.torch_dtype`

## Weights assessment
- summary: assessment recipe_match, matched_tensors 585, max_relative_difference_outside_changed_set 0, max_relative_difference_outside_recipe_set 0, min_first_singular_energy_share 0.9916
- threshold: 0.001
- nearest recipe: single-projection-selected, matched true
  - single-projection-selected: matched true, 0 violations
  - directional-per-layer-selected: matched true, 0 violations
  - single-projection: matched false, 25 violations
  - directional-per-layer: matched false, 25 violations
  - single-projection/mistral-small-3.2-24b: matched false, 48 violations
  - round-1-da75ab7f3d0a: matched false, 81 violations
  - norm-preserving/mistral-small-3.2-24b: matched false, 103 violations
- schema_version 1; scope: Weight differences alone cannot certify the absence of hidden behavior.

## Changed tensors
| kind | changed/total | layers | relative change | first share | positive fraction |
| --- | --- | --- | --- | --- | --- |
| attention_output | 32/40 | 8-39 | 0.01693 / 0.01848 / 0.02135 | 0.9916 / 0.9928 / 0.9945 | 0.3773 / 0.3847 / 0.3932 |
| feed_forward_down | 23/40 | 17-39 | 0.01742 / 0.01837 / 0.01957 | 0.992 / 0.9928 / 0.9935 | 0.3787 / 0.3839 / 0.3894 |
- unchanged kinds: other 0/222, attention_key 0/40, attention_query 0/40, attention_value 0/40, embedding 0/1, feed_forward_gate 0/40, feed_forward_up 0/40, final_normalization 0/1, input_normalization 0/40, output_head 0/1, post_attention_normalization 0/40
- exactly-0 changed tensors: none

## Directions
| group | count | median cosine | min cosine | median_direction_defined |
| --- | --- | --- | --- | --- |
| attention_output:5120 | 32 | 0.9987 | 0.9761 | true |
| feed_forward_down:5120 | 23 | 0.9996 | 0.9967 | true |
- svd: seed 0, top_k 8, sketch_columns 12, power_iterations 4
- unused_shared_kv 0, original_only 0, modified_only 0, dropped_towers 0, dropped_statistics 0

## Oddities
- none
