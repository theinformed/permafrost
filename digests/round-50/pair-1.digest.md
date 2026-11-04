# Pair 1 digest

## Pair
- modified: darkc0de/gemma-4-31B-it-Claude-Opus-Distill-v2-heretic @ a7a72728f29486658e054711b39819fe0cd7dd20
- original: unsloth/gemma-4-31B-it @ a1c85d1c2db7dcd15c41ad4082955240a9465743
- receipt: pair 1, measurement_sha256 cb213bfa
- job, node, seconds: not carried

## Metadata
- verdict: unexplained differences
- differences: 22 (explained by re-save 7, unexplained 15)
  - special_tokens.tokenizer_config.json:eos_token: {'value': '<turn|>', 'ids': [106]} -> {'value': '<eos>', 'ids': [1]}
  - special_token_ids.bos_token_id: null -> 2
  - generation._from_model_config: null -> true
  - generation.do_sample: true -> null
  - generation.eos_token_id: [1, 106, 50] -> 106
  - generation.temperature: 1 -> null
  - generation.top_k: 64 -> null
  - generation.top_p: 0.95 -> null
  - generation.transformers_version: 5.5.0.dev0 -> 5.8.0
  - generation.use_cache: null -> false
  - config.bos_token_id: null -> 2
  - config.dtype: null -> bfloat16
  - config.model_name: null -> unsloth/gemma-4-31B-it
  - config.text_config.dtype: null -> bfloat16
  - config.text_config.torch_dtype: bfloat16 -> null
  - config.torch_dtype: bfloat16 -> null
  - config.transformers_version: 5.8.0.dev0 -> 5.8.0
  - config.unsloth_version: null -> 2026.4.4
  - config.vision_config.dtype: null -> bfloat16
  - config.vision_config.torch_dtype: bfloat16 -> null
  - and 2 more
- limitation: This metadata audit does not certify the absence of hidden behavior.
- card headings: ## Explained by re-save: `generation.temperature`, ## Explained by re-save: `generation.transformers_version`, ## Explained by re-save: `config.text_config.dtype`, ## Explained by re-save: `config.text_config.torch_dtype`, ## Explained by re-save: `config.transformers_version`, ## Explained by re-save: `config.vision_config.dtype`, ## Explained by re-save: `config.vision_config.torch_dtype`

## Weights assessment
- summary: assessment recipe_violations, matched_tensors 1188, max_relative_difference_outside_changed_set 0.0009847, max_relative_difference_outside_recipe_set 0.004783, min_first_singular_energy_share 0.1268
- threshold: 0.001
- nearest recipe: single-projection-selected, matched false
  - single-projection-selected: matched false, 240 violations
  - single-projection: matched false, 259 violations
  - directional-per-layer-selected: matched false, 377 violations
  - directional-per-layer: matched false, 396 violations
- schema_version 1; scope: Weight differences alone cannot certify the absence of hidden behavior.

## Changed tensors
| kind | changed/total | layers | relative change | first share | positive fraction |
| --- | --- | --- | --- | --- | --- |
| attention_key | 27/60 | 29-59 | 0.001275 / 0.001922 / 0.003364 | 0.3178 / 0.5346 / 0.6956 | 0.1418 / 0.1799 / 0.2395 |
| attention_output | 60/60 | 0-59 | 0.001285 / 0.01461 / 0.02457 | 0.3232 / 0.9836 / 0.9918 | 0.1273 / 0.3203 / 0.3689 |
| attention_query | 27/60 | 33-59 | 0.001227 / 0.002226 / 0.0046 | 0.3894 / 0.6484 / 0.8885 | 0.1368 / 0.1986 / 0.2862 |
| attention_value | 27/50 | 27-58 | 0.001294 / 0.001753 / 0.002482 | 0.3203 / 0.532 / 0.7286 | 0.141 / 0.1798 / 0.2136 |
| feed_forward_down | 41/60 | 19-59 | 0.001407 / 0.01872 / 0.0252 | 0.4001 / 0.9849 / 0.9941 | 0.1382 / 0.3408 / 0.3704 |
| feed_forward_gate | 34/60 | 0-59 | 0.001096 / 0.00343 / 0.004783 | 0.1288 / 0.8029 / 0.8894 | 0.1085 / 0.2375 / 0.2885 |
| feed_forward_up | 35/60 | 0-59 | 0.001082 / 0.003076 / 0.004101 | 0.1268 / 0.7578 / 0.8534 | 0.1117 / 0.2254 / 0.2668 |
- unchanged kinds: other 0/656, embedding 0/1, final_normalization 0/1, input_normalization 0/60, post_attention_normalization 0/60
- exactly-0 changed tensors: none

## Directions
| group | count | median cosine | min cosine | median_direction_defined |
| --- | --- | --- | --- | --- |
| feed_forward_gate:21504 | 34 | 0.1318 | 0.1082 | true |
| feed_forward_up:21504 | 35 | 0.1238 | 0.09894 | true |
| attention_output:5376 | 60 | 0.984 | 0.00888 | true |
| feed_forward_down:5376 | 41 | 0.9928 | 0.00461 | true |
| attention_value:4096 | 27 | 0.1491 | 0.119 | true |
| attention_key:2048 | 6 | 0.3357 | 0.3234 | true |
| attention_query:8192 | 22 | 0.1643 | 0.1365 | true |
| attention_key:4096 | 21 | 0.1627 | 0.1385 | true |
| attention_query:16384 | 5 | 0.3651 | 0.3498 | true |
- svd: seed 0, top_k 8, sketch_columns 12, power_iterations 4
- unused_shared_kv 0, original_only 0, modified_only 0, dropped_towers 0, dropped_statistics 0

## Oddities
- none
