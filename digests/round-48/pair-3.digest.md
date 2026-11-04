# Pair 3 digest

## Pair
- modified: DavidAU/Gemma-3-27b-it-vl-SuperBrain7x-High-Reasoning-ULTRAMIND-Heretic-Uncensored @ b514c7186d36d0887a501701a3ff888f116904e2
- original: coder3101/gemma-3-27b-it-heretic @ b944979784c4795b9adb30a88d51a54b53111017
- receipt: pair 3, measurement_sha256 d35bf3b1
- job, node, seconds: not carried

## Metadata
- verdict: consistent with re-save noted
- differences: 2 (explained by re-save 2)
  - generation.transformers_version: 4.57.3 -> 4.57.6
  - config.transformers_version: 4.57.3 -> 4.57.6
- limitation: This metadata audit does not certify the absence of hidden behavior.
- card headings: ## Explained by re-save: `generation.transformers_version`, ## Explained by re-save: `config.transformers_version`

## Weights assessment
- summary: assessment recipe_violations, matched_tensors 1247, max_relative_difference_outside_changed_set 0, max_relative_difference_outside_recipe_set 0.01305, min_first_singular_energy_share 0.2615
- threshold: 0.001
- nearest recipe: single-projection, matched false
  - single-projection: matched false, 559 violations
  - single-projection-selected: matched false, 559 violations
  - directional-per-layer: matched false, 744 violations
  - directional-per-layer-selected: matched false, 744 violations
- schema_version 1; scope: Weight differences alone cannot certify the absence of hidden behavior.

## Changed tensors
| kind | changed/total | layers | relative change | first share | positive fraction |
| --- | --- | --- | --- | --- | --- |
| attention_key | 62/62 | 0-61 | 0.00109 / 0.003001 / 0.006517 | 0.2615 / 0.5901 / 0.8714 | 0.1187 / 0.2285 / 0.3067 |
| attention_output | 62/62 | 0-61 | 0.004437 / 0.006483 / 0.0125 | 0.3969 / 0.6905 / 0.9251 | 0.2794 / 0.3385 / 0.4052 |
| attention_query | 62/62 | 0-61 | 0.00247 / 0.005708 / 0.01048 | 0.3273 / 0.7563 / 0.9471 | 0.1923 / 0.3153 / 0.3948 |
| attention_value | 62/62 | 0-61 | 0.001582 / 0.003131 / 0.005926 | 0.3972 / 0.6863 / 0.8792 | 0.1507 / 0.2327 / 0.3103 |
| feed_forward_down | 62/62 | 0-61 | 0.004337 / 0.008056 / 0.07654 | 0.4837 / 0.8629 / 0.9847 | 0.2644 / 0.3373 / 0.4168 |
| feed_forward_gate | 62/62 | 0-61 | 0.003715 / 0.006949 / 0.01305 | 0.6119 / 0.9009 / 0.9737 | 0.2348 / 0.319 / 0.3846 |
| feed_forward_up | 62/62 | 0-61 | 0.003427 / 0.005208 / 0.009274 | 0.5871 / 0.8556 / 0.9414 | 0.2252 / 0.29 / 0.3623 |
- unchanged kinds: other 0/687, embedding 0/1, final_normalization 0/1, input_normalization 0/62, post_attention_normalization 0/62
- exactly-0 changed tensors: none

## Directions
| group | count | median cosine | min cosine | median_direction_defined |
| --- | --- | --- | --- | --- |
| feed_forward_down:5376 | 62 | 0.4326 | 0.01091 | true |
| feed_forward_gate:21504 | 62 | 0.09919 | 0.08403 | true |
| feed_forward_up:21504 | 62 | 0.09873 | 0.0803 | true |
| attention_key:2048 | 62 | 0.1002 | 0.04601 | true |
| attention_output:5376 | 62 | 0.3492 | 0.003862 | true |
| attention_query:4096 | 62 | 0.09871 | 0.06312 | true |
| attention_value:2048 | 62 | 0.1033 | 0.04286 | true |
- svd: seed 0, top_k 8, sketch_columns 12, power_iterations 4
- unused_shared_kv 0, original_only 0, modified_only 0, dropped_towers 0, dropped_statistics 0

## Oddities
- none
