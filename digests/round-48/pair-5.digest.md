# Pair 5 digest

## Pair
- modified: sh0ck0r/heretic-rp-vision-31b @ 5bded82d13dec267cc89c1d1558cf530bf00dcb1
- original: google/gemma-4-31B-it @ 3548789868c5356dbf307c98e6f609007b82b3eb
- receipt: pair 5, measurement_sha256 3762115c
- job, node, seconds: not carried

## Metadata
- verdict: unexplained differences
- differences: 4 (explained by re-save 2, unexplained 2)
  - generation.transformers_version: 5.5.0.dev0 -> 5.6.0.dev0
  - config.text_config.moe_intermediate_size: null -> null
  - config.transformers_version: 5.5.0.dev0 -> 5.10.2
  - template.default: {%- macro format_parameters(properties, required, filter_... -> {%- macro format_parameters(properties, required) -%}    ...
- limitation: This metadata audit does not certify the absence of hidden behavior.
- card headings: ## Explained by re-save: `generation.transformers_version`, ## Explained by re-save: `config.transformers_version`

## Weights assessment
- summary: assessment recipe_violations, matched_tensors 1188, max_relative_difference_outside_changed_set 0, max_relative_difference_outside_recipe_set 0.1396, min_first_singular_energy_share 0.2481
- threshold: 0.001
- nearest recipe: single-projection, matched false
  - single-projection: matched false, 529 violations
  - single-projection-selected: matched false, 529 violations
  - directional-per-layer: matched false, 698 violations
  - directional-per-layer-selected: matched false, 698 violations
- schema_version 1; scope: Weight differences alone cannot certify the absence of hidden behavior.

## Changed tensors
| kind | changed/total | layers | relative change | first share | positive fraction |
| --- | --- | --- | --- | --- | --- |
| attention_key | 60/60 | 0-59 | 0.01356 / 0.01929 / 0.04833 | 0.2481 / 0.6467 / 0.9593 | 0.4256 / 0.4386 / 0.4557 |
| attention_output | 60/60 | 0-59 | 0.01444 / 0.02384 / 0.07059 | 0.3205 / 0.7255 / 0.9947 | 0.4231 / 0.4433 / 0.467 |
| attention_query | 60/60 | 0-59 | 0.01545 / 0.02078 / 0.03506 | 0.3561 / 0.7826 / 0.9463 | 0.4245 / 0.4405 / 0.4589 |
| attention_value | 50/50 | 0-58 | 0.01333 / 0.0195 / 0.1396 | 0.3589 / 0.631 / 0.9792 | 0.4182 / 0.4374 / 0.4536 |
| feed_forward_down | 60/60 | 0-59 | 0.01446 / 0.02652 / 0.04288 | 0.3022 / 0.6601 / 0.9446 | 0.4229 / 0.4443 / 0.4556 |
| feed_forward_gate | 60/60 | 0-59 | 0.01766 / 0.02888 / 0.03636 | 0.464 / 0.9055 / 0.9867 | 0.4273 / 0.4435 / 0.4569 |
| feed_forward_up | 60/60 | 0-59 | 0.01581 / 0.02359 / 0.04223 | 0.4166 / 0.8414 / 0.9704 | 0.417 / 0.4389 / 0.4578 |
- unchanged kinds: other 0/656, embedding 0/1, final_normalization 0/1, input_normalization 0/60, post_attention_normalization 0/60
- exactly-0 changed tensors: none

## Directions
| group | count | median cosine | min cosine | median_direction_defined |
| --- | --- | --- | --- | --- |
| feed_forward_down:5376 | 60 | 0.3229 | 0.03718 | true |
| feed_forward_gate:21504 | 60 | 0.1031 | 0.07864 | true |
| feed_forward_up:21504 | 60 | 0.1018 | 0.06378 | true |
| attention_key:4096 | 50 | 0.1125 | 0.08227 | true |
| attention_output:5376 | 60 | 0.2259 | 0.03538 | true |
| attention_query:8192 | 50 | 0.1133 | 0.09202 | true |
| attention_value:4096 | 50 | 0.1172 | 0.08516 | true |
| attention_key:2048 | 10 | 0.2765 | 0.2412 | true |
| attention_query:16384 | 10 | 0.265 | 0.2593 | true |
- svd: seed 0, top_k 8, sketch_columns 12, power_iterations 4
- unused_shared_kv 0, original_only 0, modified_only 0, dropped_towers 0, dropped_statistics 0

## Oddities
- none
