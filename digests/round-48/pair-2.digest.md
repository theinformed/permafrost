# Pair 2 digest

## Pair
- modified: DavidAU/Gemma-3-4B-VL-it-Gemini-Pro-Heretic-Uncensored-Thinking @ f289c8297e8e2fd570a83658b6a75414e3d95b98
- original: DavidAU/gemma-3-4b-it-heretic-uncensored-abliterated-Extreme @ b2d64d291eb745a5a9783d46a11490de7c4ce1ee
- receipt: pair 2, measurement_sha256 e94f3c67
- job, node, seconds: not carried

## Metadata
- verdict: consistent with re-save noted
- differences: 5 (explained by re-save 5)
  - generation.transformers_version: 5.0.0.dev0 -> 4.57.6
  - config.text_config.rope_local_base_freq: null -> 1e+04
  - config.text_config.rope_scaling: null -> null
  - config.text_config.rope_theta: null -> 1e+06
  - config.transformers_version: 5.0.0.dev0 -> 4.57.6
- limitation: This metadata audit does not certify the absence of hidden behavior.
- card headings: ## Explained by re-save: `generation.transformers_version`, ## Explained by re-save: `config.text_config.rope_local_base_freq`, ## Explained by re-save: `config.text_config.rope_scaling`, ## Explained by re-save: `config.text_config.rope_theta`, ## Explained by re-save: `config.transformers_version`

## Weights assessment
- summary: assessment recipe_violations, matched_tensors 883, max_relative_difference_outside_changed_set 0.0009849, max_relative_difference_outside_recipe_set 0.006194, min_first_singular_energy_share 0.2794
- threshold: 0.001
- nearest recipe: single-projection, matched false
  - single-projection: matched false, 303 violations
  - single-projection-selected: matched false, 303 violations
  - directional-per-layer: matched false, 400 violations
  - directional-per-layer-selected: matched false, 400 violations
- schema_version 1; scope: Weight differences alone cannot certify the absence of hidden behavior.

## Changed tensors
| kind | changed/total | layers | relative change | first share | positive fraction |
| --- | --- | --- | --- | --- | --- |
| attention_key | 30/34 | 0-33 | 0.001052 / 0.001757 / 0.00372 | 0.2794 / 0.4694 / 0.8158 | 0.1291 / 0.1863 / 0.276 |
| attention_output | 34/34 | 0-33 | 0.002708 / 0.005133 / 0.01035 | 0.4807 / 0.8051 / 0.9391 | 0.2276 / 0.3141 / 0.378 |
| attention_query | 34/34 | 0-33 | 0.002334 / 0.003729 / 0.006194 | 0.3206 / 0.6895 / 0.8683 | 0.2163 / 0.2787 / 0.3455 |
| attention_value | 34/34 | 0-33 | 0.001214 / 0.002487 / 0.004271 | 0.3383 / 0.6983 / 0.8589 | 0.1369 / 0.2142 / 0.2894 |
| feed_forward_down | 34/34 | 0-33 | 0.003498 / 0.005317 / 0.009824 | 0.378 / 0.7634 / 0.936 | 0.254 / 0.3106 / 0.3728 |
| feed_forward_gate | 34/34 | 0-33 | 0.00179 / 0.002634 / 0.004379 | 0.3023 / 0.5304 / 0.8598 | 0.1719 / 0.2285 / 0.285 |
| feed_forward_up | 34/34 | 0-33 | 0.002055 / 0.002835 / 0.004387 | 0.2968 / 0.5844 / 0.8124 | 0.1891 / 0.2332 / 0.2854 |
- unchanged kinds: other 0/575, embedding 0/1, final_normalization 0/1, input_normalization 0/34, post_attention_normalization 0/34
- exactly-0 changed tensors: none

## Directions
| group | count | median cosine | min cosine | median_direction_defined |
| --- | --- | --- | --- | --- |
| feed_forward_down:2560 | 34 | 0.5418 | 0.07014 | true |
| feed_forward_gate:10240 | 34 | 0.1356 | 0.1198 | true |
| feed_forward_up:10240 | 34 | 0.1378 | 0.1204 | true |
| attention_key:1024 | 30 | 0.1618 | 0.06586 | true |
| attention_output:2560 | 34 | 0.5348 | 0.07023 | true |
| attention_query:2048 | 34 | 0.1361 | 0.106 | true |
| attention_value:1024 | 34 | 0.1479 | 0.06843 | true |
- svd: seed 0, top_k 8, sketch_columns 12, power_iterations 4
- unused_shared_kv 0, original_only 0, modified_only 0, dropped_towers 0, dropped_statistics 0

## Oddities
- none
