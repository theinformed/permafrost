# Pair 3 digest

## Pair
- modified: keithtyser/Gemopus-4-26B-A4B-it-local-abliterated-sota-internal-r7-selected-t34-transfer @ 0e57ea6005a3409ae4f36a37da2f1fcbc39f6bf2
- original: Jackrong/Gemopus-4-26B-A4B-it @ 844a68b6cb54a4377b386bd09615a1dc6e3ce32c
- receipt: pair 3, measurement_sha256 52664057
- job, node, seconds: not carried

## Metadata
- verdict: unexplained differences
- differences: 9 (explained by re-save 4, unexplained 5)
  - generation: null -> {'_from_model_config': True, 'bos_token_id': 2, 'eos_toke...
  - config.dtype: null -> bfloat16
  - config.text_config.dtype: null -> bfloat16
  - config.text_config.torch_dtype: bfloat16 -> null
  - config.torch_dtype: bfloat16 -> null
  - config.transformers_version: null -> 5.6.2
  - config.use_cache: false -> null
  - config.vision_config.dtype: null -> bfloat16
  - config.vision_config.torch_dtype: bfloat16 -> null
- missing: original: generation_config.json missing
- limitation: This metadata audit does not certify the absence of hidden behavior.
- card headings: ## Explained by re-save: `config.text_config.dtype`, ## Explained by re-save: `config.text_config.torch_dtype`, ## Explained by re-save: `config.vision_config.dtype`, ## Explained by re-save: `config.vision_config.torch_dtype`

## Weights assessment
- summary: assessment recipe_violations, matched_tensors 1013, max_relative_difference_outside_changed_set 0.0007392, max_relative_difference_outside_recipe_set 0, min_first_singular_energy_share 0.832
- threshold: 0.001
- nearest recipe: directional-per-layer-selected, matched false
  - directional-per-layer-selected: matched false, 20 violations
  - single-projection-selected: matched false, 52 violations
  - directional-per-layer: matched false, 76 violations
  - single-projection: matched false, 108 violations
- schema_version 1; scope: Weight differences alone cannot certify the absence of hidden behavior.

## Changed tensors
| kind | changed/total | layers | relative change | first share | positive fraction |
| --- | --- | --- | --- | --- | --- |
| attention_output | 17/30 | 12-28 | 0.01976 / 0.02724 / 0.03058 | 0.9882 / 0.9963 / 0.9972 | 0.2945 / 0.36 / 0.3671 |
| feed_forward_down | 18/30 | 12-29 | 0.002075 / 0.008633 / 0.01735 | 0.832 / 0.9749 / 0.9926 | 0.1096 / 0.2669 / 0.3286 |
- unchanged kinds: other 0/686, attention_key 0/30, attention_query 0/30, attention_value 0/25, embedding 0/1, expert_down 0/30, expert_gate_up 0/30, feed_forward_gate 0/30, feed_forward_up 0/30, final_normalization 0/1, input_normalization 0/30, post_attention_normalization 0/30
- exactly-0 changed tensors: none

## Directions
| group | count | median cosine | min cosine | median_direction_defined |
| --- | --- | --- | --- | --- |
| feed_forward_down:2816 | 18 | 0.6635 | 0.3168 | true |
| attention_output:2816 | 17 | 0.6734 | 0.3465 | true |
- svd: seed 0, top_k 8, sketch_columns 12, power_iterations 4
- unused_shared_kv 0, original_only 0, modified_only 0, dropped_towers 0, dropped_statistics 0

## Oddities
- none
