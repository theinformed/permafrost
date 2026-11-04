# Pair 4 digest

## Pair
- modified: DavidAU/gemma-3-12b-it-vl-HighIQ-Polaris-Heretic-Uncensored-Thinking @ caab1ea5de9e1837386ff45358b8ea5d4e10ca1d
- original: DreamFast/gemma-3-12b-it-heretic @ af1227e134900b3b031498d1034cf6668b51ff40
- receipt: pair 4, measurement_sha256 83ffb4c4
- job, node, seconds: not carried

## Metadata
- verdict: consistent with re-save noted
- differences: 2 (explained by re-save 2)
  - generation.transformers_version: 4.57.3 -> 4.57.6
  - config.transformers_version: 4.57.3 -> 4.57.6
- limitation: This metadata audit does not certify the absence of hidden behavior.
- card headings: ## Explained by re-save: `generation.transformers_version`, ## Explained by re-save: `config.transformers_version`

## Weights assessment
- summary: assessment recipe_violations, matched_tensors 1065, max_relative_difference_outside_changed_set 0.0009881, max_relative_difference_outside_recipe_set 0.01202, min_first_singular_energy_share 0.1894
- threshold: 0.001
- nearest recipe: single-projection, matched false
  - single-projection: matched false, 432 violations
  - single-projection-selected: matched false, 432 violations
  - directional-per-layer: matched false, 574 violations
  - directional-per-layer-selected: matched false, 574 violations
- schema_version 1; scope: Weight differences alone cannot certify the absence of hidden behavior.

## Changed tensors
| kind | changed/total | layers | relative change | first share | positive fraction |
| --- | --- | --- | --- | --- | --- |
| attention_key | 47/48 | 0-47 | 0.001061 / 0.003125 / 0.005805 | 0.1894 / 0.485 / 0.7984 | 0.1237 / 0.2448 / 0.3335 |
| attention_output | 48/48 | 0-47 | 0.00292 / 0.006027 / 0.009524 | 0.2778 / 0.5967 / 0.8668 | 0.2372 / 0.3342 / 0.3953 |
| attention_query | 48/48 | 0-47 | 0.002269 / 0.005214 / 0.01139 | 0.2839 / 0.5854 / 0.8392 | 0.2135 / 0.3296 / 0.3998 |
| attention_value | 48/48 | 0-47 | 0.001379 / 0.003226 / 0.005016 | 0.3284 / 0.6495 / 0.8176 | 0.1526 / 0.2486 / 0.3181 |
| feed_forward_down | 48/48 | 0-47 | 0.00413 / 0.007766 / 0.01365 | 0.3092 / 0.7512 / 0.9338 | 0.2693 / 0.3543 / 0.4087 |
| feed_forward_gate | 48/48 | 0-47 | 0.003807 / 0.005867 / 0.01202 | 0.4235 / 0.8065 / 0.9509 | 0.2559 / 0.3165 / 0.3909 |
| feed_forward_up | 48/48 | 0-47 | 0.003157 / 0.005154 / 0.009122 | 0.4276 / 0.7351 / 0.9143 | 0.2305 / 0.3034 / 0.3606 |
- unchanged kinds: other 0/631, embedding 0/1, final_normalization 0/1, input_normalization 0/48, post_attention_normalization 0/48
- exactly-0 changed tensors: none

## Directions
| group | count | median cosine | min cosine | median_direction_defined |
| --- | --- | --- | --- | --- |
| feed_forward_down:3840 | 48 | 0.4254 | 0.05951 | true |
| feed_forward_gate:15360 | 48 | 0.1174 | 0.09871 | true |
| feed_forward_up:15360 | 48 | 0.1137 | 0.09911 | true |
| attention_key:2048 | 47 | 0.1134 | 0.0752 | true |
| attention_output:3840 | 48 | 0.3897 | 0.03342 | true |
| attention_query:4096 | 48 | 0.1167 | 0.08186 | true |
| attention_value:2048 | 48 | 0.1149 | 0.05205 | true |
- svd: seed 0, top_k 8, sketch_columns 12, power_iterations 4
- unused_shared_kv 0, original_only 0, modified_only 0, dropped_towers 0, dropped_statistics 0

## Oddities
- none
