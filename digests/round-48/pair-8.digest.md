# Pair 8 digest

## Pair
- modified: vulture3/G4-WanaMeroQueen-v3-31B-heretic @ e3a6f1b2f81b089e767d6dbb37be25354195db6d
- original: vulture3/G4-WanaMeroQueen-v3-31B @ 1827fe36b30e467b048b470d66b5ccfc2354cd94
- receipt: pair 8, measurement_sha256 7cf96f99
- job, node, seconds: not carried

## Metadata
- verdict: unexplained differences
- differences: 6 (explained by re-save 2, unexplained 4)
  - generation.transformers_version: 5.5.0.dev0 -> 5.17.0
  - config.text_config.global_head_dim: 512 -> null
  - config.text_config.num_global_key_value_heads: 4 -> null
  - config.text_config.per_layer_config: null -> {'05': {'head_dim': 512, 'num_key_value_heads': 4}, '11':...
  - config.transformers_version: 5.12.1 -> 5.17.0
  - config.vision_config.rope_parameters.rope_type: default -> axial
- limitation: This metadata audit does not certify the absence of hidden behavior.
- card headings: ## Explained by re-save: `generation.transformers_version`, ## Explained by re-save: `config.transformers_version`

## Weights assessment
- summary: assessment recipe_violations, matched_tensors 1188, max_relative_difference_outside_changed_set 0, max_relative_difference_outside_recipe_set 0, min_first_singular_energy_share 0.9878
- threshold: 0.001
- nearest recipe: directional-per-layer-selected, matched false
  - directional-per-layer-selected: matched false, 1 violations
  - single-projection-selected: matched false, 29 violations
  - directional-per-layer: matched false, 94 violations
  - single-projection: matched false, 122 violations
- schema_version 1; scope: Weight differences alone cannot certify the absence of hidden behavior.

## Changed tensors
| kind | changed/total | layers | relative change | first share | positive fraction |
| --- | --- | --- | --- | --- | --- |
| attention_output | 18/60 | 42-59 | 0.01515 / 0.01815 / 0.02073 | 0.9903 / 0.9927 / 0.9944 | 0.3415 / 0.3658 / 0.3766 |
| feed_forward_down | 9/60 | 39-47 | 0.01347 / 0.01755 / 0.02043 | 0.9878 / 0.9929 / 0.9944 | 0.3204 / 0.35 / 0.3643 |
- unchanged kinds: other 0/656, attention_key 0/60, attention_query 0/60, attention_value 0/50, embedding 0/1, feed_forward_gate 0/60, feed_forward_up 0/60, final_normalization 0/1, input_normalization 0/60, post_attention_normalization 0/60
- exactly-0 changed tensors: none

## Directions
| group | count | median cosine | min cosine | median_direction_defined |
| --- | --- | --- | --- | --- |
| feed_forward_down:5376 | 9 | 0.8517 | 0.6503 | true |
| attention_output:5376 | 18 | 0.7727 | 0.3828 | true |
- svd: seed 0, top_k 8, sketch_columns 12, power_iterations 4
- unused_shared_kv 0, original_only 0, modified_only 0, dropped_towers 0, dropped_statistics 0

## Oddities
- none
