# Pair 6 digest

## Pair
- modified: m-polignano/ANITA-NEXT-24B-Dolphin-Mistral-UNCENSORED-ITA @ 48b961ac080eb69dea8dbc06d4bac617dfef31c8
- original: dphn/Dolphin-Mistral-24B-Venice-Edition @ f1ddeef2824f959898235235992619bf474c80c7
- receipt: pair 6, measurement_sha256 72b2f7e7
- job, node, seconds: not carried

## Metadata
- verdict: unexplained differences
- differences: 10 (explained by re-save 2, unexplained 8)
  - generation.max_new_tokens: null -> 32786
  - generation.pad_token_id: null -> 2
  - generation.temperature: 0.15 -> 0.7
  - generation.top_p: null -> 0.9
  - generation.transformers_version: 4.51.3 -> 4.54.0.dev0
  - config.max_position_embeddings: 32768 -> 40960
  - config.rope_theta: 1e+08 -> 1e+09
  - config.transformers_version: 4.51.3 -> 4.54.0.dev0
  - template_source.tokenizer_config: {%- set today = strftime_now("%Y-%m-%d") %} {%- set defau... -> null
  - template.default: {%- set today = strftime_now("%Y-%m-%d") %} {%- set defau... -> {{- bos_token }}  {%- if messages[0]['role'] == 'system' ...
- limitation: This metadata audit does not certify the absence of hidden behavior.
- card headings: ## Explained by re-save: `generation.transformers_version`, ## Explained by re-save: `config.transformers_version`

## Weights assessment
- summary: assessment recipe_violations, matched_tensors 363, max_relative_difference_outside_changed_set 0.0009519, max_relative_difference_outside_recipe_set 0.001545, min_first_singular_energy_share 0.2214
- threshold: 0.001
- nearest recipe: directional-per-layer-selected, matched false
  - directional-per-layer-selected: matched false, 10 violations
  - single-projection-selected: matched false, 11 violations
  - directional-per-layer: matched false, 87 violations
  - single-projection: matched false, 88 violations
- schema_version 1; scope: Weight differences alone cannot certify the absence of hidden behavior.

## Changed tensors
| kind | changed/total | layers | relative change | first share | positive fraction |
| --- | --- | --- | --- | --- | --- |
| attention_output | 4/40 | 0-30 | 0.001028 / 0.001103 / 0.001679 | 0.2214 / 0.3077 / 0.634 | 0.1268 / 0.1338 / 0.1707 |
| attention_value | 2/40 | 0-2 | 0.001103 / 0.001324 / 0.001545 | 0.4956 / 0.575 / 0.6543 | 0.1233 / 0.1407 / 0.1581 |
- unchanged kinds: attention_key 0/40, attention_query 0/40, embedding 0/1, feed_forward_down 0/40, feed_forward_gate 0/40, feed_forward_up 0/40, final_normalization 0/1, input_normalization 0/40, output_head 0/1, post_attention_normalization 0/40
- exactly-0 changed tensors: none

## Directions
| group | count | median cosine | min cosine | median_direction_defined |
| --- | --- | --- | --- | --- |
| attention_output:5120 | 4 | 0.5503 | 0.2656 | true |
| attention_value:1024 | 2 | 0.009377 | 0.009377 | true |
- svd: seed 0, top_k 8, sketch_columns 12, power_iterations 4
- unused_shared_kv 0, original_only 0, modified_only 0, dropped_towers 0, dropped_statistics 0

## Oddities
- none
