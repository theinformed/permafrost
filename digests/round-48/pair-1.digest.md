# Pair 1 digest

## Pair
- modified: DavidAU/gemma-3-12b-it-vl-Gemini-3-Pro-Preview-Heretic-Uncensored-Thinking @ 01d242541984ea885529c7d9d3bc307ce5fb5f87
- original: DreamFast/gemma-3-12b-it-heretic @ af1227e134900b3b031498d1034cf6668b51ff40
- receipt: pair 1, measurement_sha256 85d323fc
- job, node, seconds: not carried

## Metadata
- verdict: consistent with re-save noted
- differences: 2 (explained by re-save 2)
  - generation.transformers_version: 4.57.3 -> 4.57.6
  - config.transformers_version: 4.57.3 -> 4.57.6
- limitation: This metadata audit does not certify the absence of hidden behavior.
- card headings: ## Explained by re-save: `generation.transformers_version`, ## Explained by re-save: `config.transformers_version`

## Weights assessment
- summary: assessment recipe_violations, matched_tensors 1065, max_relative_difference_outside_changed_set 0, max_relative_difference_outside_recipe_set 0.04259, min_first_singular_energy_share 0.1688
- threshold: 0.001
- nearest recipe: single-projection, matched false
  - single-projection: matched false, 433 violations
  - single-projection-selected: matched false, 433 violations
  - directional-per-layer: matched false, 576 violations
  - directional-per-layer-selected: matched false, 576 violations
- schema_version 1; scope: Weight differences alone cannot certify the absence of hidden behavior.

## Changed tensors
| kind | changed/total | layers | relative change | first share | positive fraction |
| --- | --- | --- | --- | --- | --- |
| attention_key | 48/48 | 0-47 | 0.001425 / 0.004911 / 0.01101 | 0.1688 / 0.4671 / 0.8946 | 0.1622 / 0.2979 / 0.3768 |
| attention_output | 48/48 | 0-47 | 0.003436 / 0.007724 / 0.01286 | 0.3872 / 0.6276 / 0.8932 | 0.2673 / 0.365 / 0.4154 |
| attention_query | 48/48 | 0-47 | 0.003306 / 0.008018 / 0.04259 | 0.2313 / 0.6138 / 0.9546 | 0.2607 / 0.3738 / 0.4241 |
| attention_value | 48/48 | 0-47 | 0.001712 / 0.004408 / 0.006932 | 0.2481 / 0.7107 / 0.9078 | 0.1714 / 0.286 / 0.355 |
| feed_forward_down | 48/48 | 0-47 | 0.005344 / 0.01031 / 0.01954 | 0.3315 / 0.737 / 0.9336 | 0.3226 / 0.3863 / 0.4267 |
| feed_forward_gate | 48/48 | 0-47 | 0.004339 / 0.01143 / 0.01854 | 0.606 / 0.8972 / 0.9784 | 0.2792 / 0.379 / 0.4217 |
| feed_forward_up | 48/48 | 0-47 | 0.003907 / 0.008112 / 0.0124 | 0.3693 / 0.7803 / 0.9427 | 0.273 / 0.3512 / 0.4017 |
- unchanged kinds: other 0/631, embedding 0/1, final_normalization 0/1, input_normalization 0/48, post_attention_normalization 0/48
- exactly-0 changed tensors: none

## Directions
| group | count | median cosine | min cosine | median_direction_defined |
| --- | --- | --- | --- | --- |
| feed_forward_down:3840 | 48 | 0.391 | 0.05146 | true |
| feed_forward_gate:15360 | 48 | 0.1148 | 0.09902 | true |
| feed_forward_up:15360 | 48 | 0.1156 | 0.09944 | true |
| attention_key:2048 | 48 | 0.12 | 0.05858 | true |
| attention_output:3840 | 48 | 0.337 | 0.00798 | true |
| attention_query:4096 | 48 | 0.1138 | 0.04961 | true |
| attention_value:2048 | 48 | 0.123 | 0.06972 | true |
- svd: seed 0, top_k 8, sketch_columns 12, power_iterations 4
- unused_shared_kv 0, original_only 0, modified_only 0, dropped_towers 0, dropped_statistics 0

## Oddities
- none
