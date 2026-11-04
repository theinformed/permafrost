# Pair 2 digest

## Pair
- modified: coder3101/gemma-4-19b-a4b-it-REAP-heretic @ ae672f47463866e7772ae9701e5f88eebc77c966
- original: 0xSero/Gemma-4-19B @ e9678c288b656d38c84515831b92056f1c026f69
- receipt: pair 2, measurement_sha256 0f9c5b33
- job, node, seconds: not carried

## Metadata
- verdict: consistent with re-save noted
- differences: 2 (explained by re-save 2)
  - generation.transformers_version: 5.5.0 -> 5.5.0.dev0
  - config.transformers_version: 5.5.0 -> 5.5.0.dev0
- limitation: This metadata audit does not certify the absence of hidden behavior.
- card headings: ## Explained by re-save: `generation.transformers_version`, ## Explained by re-save: `config.transformers_version`

## Weights assessment
- summary: assessment recipe_violations, matched_tensors 1013, max_relative_difference_outside_changed_set 0.0009872, max_relative_difference_outside_recipe_set 0, min_first_singular_energy_share 0.005929
- threshold: 0.001
- nearest recipe: directional-per-layer-selected, matched false
  - directional-per-layer-selected: matched false, 10 violations
  - single-projection-selected: matched false, 21 violations
  - directional-per-layer: matched false, 92 violations
  - single-projection: matched false, 103 violations
- schema_version 1; scope: Weight differences alone cannot certify the absence of hidden behavior.

## Changed tensors
| kind | changed/total | layers | relative change | first share | positive fraction |
| --- | --- | --- | --- | --- | --- |
| attention_output | 10/30 | 14-23 | 0.001052 / 0.001496 / 0.05758 | 0.005929 / 0.009081 / 0.9566 | 0.02733 / 0.05611 / 0.3533 |
- unchanged kinds: other 0/686, attention_key 0/30, attention_query 0/30, attention_value 0/25, embedding 0/1, expert_down 0/30, expert_gate_up 0/30, feed_forward_down 0/30, feed_forward_gate 0/30, feed_forward_up 0/30, final_normalization 0/1, input_normalization 0/30, post_attention_normalization 0/30
- exactly-0 changed tensors: none

## Directions
| group | count | median cosine | min cosine | median_direction_defined |
| --- | --- | --- | --- | --- |
| attention_output:2816 | 10 | 0.1144 | 0.04846 | true |
- svd: seed 0, top_k 8, sketch_columns 12, power_iterations 4
- unused_shared_kv 0, original_only 0, modified_only 0, dropped_towers 0, dropped_statistics 0

## Oddities
- none
