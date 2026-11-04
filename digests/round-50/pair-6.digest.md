# Pair 6 digest

## Pair
- modified: nchapman/Ministral-3-8B-Instruct-2512-heretic-BF16 @ 4712e51744bdf4610e22828aa5705af5d76af11c
- original: mistralai/Ministral-3-8B-Base-2512 @ d4883f9b36aa2e5d775730d3fdba3d30de51a8ef
- receipt: pair 6, measurement_sha256 a7f6735f
- job, node, seconds: not carried

## Metadata
- verdict: unexplained differences
- differences: 11 (explained by re-save 9, unexplained 2)
  - generation.transformers_version: 5.0.0.dev0 -> 5.3.0
  - config.text_config.bos_token_id: null -> 1
  - config.text_config.dtype: null -> bfloat16
  - config.text_config.eos_token_id: null -> 2
  - config.text_config.pad_token_id: null -> 11
  - config.text_config.tie_word_embeddings: null -> false
  - config.tie_word_embeddings: null -> false
  - config.transformers_version: 5.0.0.dev0 -> 5.3.0
  - config.vision_config.dtype: null -> bfloat16
  - config.vision_config.rope_theta: 1e+04 -> null
  - template.default: null -> {#- Default system message if no system prompt is passed....
- missing: template default absent on one side; original: chat template missing
- limitation: This metadata audit does not certify the absence of hidden behavior.
- card headings: ## Explained by re-save: `generation.transformers_version`, ## Explained by re-save: `config.text_config.bos_token_id`, ## Explained by re-save: `config.text_config.dtype`, ## Explained by re-save: `config.text_config.eos_token_id`, ## Explained by re-save: `config.text_config.pad_token_id`, ## Explained by re-save: `config.text_config.tie_word_embeddings`, ## Explained by re-save: `config.transformers_version`, ## Explained by re-save: `config.vision_config.dtype`, ## Explained by re-save: `config.vision_config.rope_theta`

## Weights assessment
- summary: assessment recipe_violations, matched_tensors 531, max_relative_difference_outside_changed_set 0.0003683, max_relative_difference_outside_recipe_set 0.09832, min_first_singular_energy_share 0.003087
- threshold: 0.001
- nearest recipe: single-projection, matched false
  - single-projection: matched false, 254 violations
  - single-projection-selected: matched false, 254 violations
  - directional-per-layer: matched false, 413 violations
  - directional-per-layer-selected: matched false, 413 violations
- schema_version 1; scope: Weight differences alone cannot certify the absence of hidden behavior.

## Changed tensors
| kind | changed/total | layers | relative change | first share | positive fraction |
| --- | --- | --- | --- | --- | --- |
| other | 2/222 | n/a | 0.07694 / 0.07893 / 0.08093 | 0.02668 / 0.04367 / 0.06066 | 0.49 / 0.4902 / 0.4903 |
| attention_key | 34/34 | 0-33 | 0.04113 / 0.06468 / 0.08712 | 0.008802 / 0.01319 / 0.07981 | 0.4855 / 0.4882 / 0.4909 |
| attention_output | 34/34 | 0-33 | 0.05862 / 0.07236 / 0.1003 | 0.006027 / 0.05778 / 0.0864 | 0.4877 / 0.4892 / 0.4923 |
| attention_query | 34/34 | 0-33 | 0.04882 / 0.07431 / 0.0908 | 0.007146 / 0.01011 / 0.08693 | 0.4867 / 0.4895 / 0.4911 |
| attention_value | 34/34 | 0-33 | 0.04772 / 0.0706 / 0.09832 | 0.004026 / 0.005665 / 0.02139 | 0.4866 / 0.489 / 0.4917 |
| embedding | 1/1 | n/a | 0.0636 / 0.0636 / 0.0636 | 0.01116 / 0.01116 / 0.01116 | 0.4877 / 0.4877 / 0.4877 |
| feed_forward_down | 34/34 | 0-33 | 0.06084 / 0.07868 / 0.08474 | 0.003346 / 0.07001 / 0.1083 | 0.4877 / 0.4896 / 0.4901 |
| feed_forward_gate | 34/34 | 0-33 | 0.06484 / 0.07836 / 0.09339 | 0.00344 / 0.004464 / 0.00732 | 0.4881 / 0.4899 / 0.4914 |
| feed_forward_up | 34/34 | 0-33 | 0.0651 / 0.0754 / 0.08087 | 0.003087 / 0.004217 / 0.0151 | 0.4883 / 0.4892 / 0.4898 |
| input_normalization | 1/34 | 0-0 | 0.004413 / 0.004413 / 0.004413 | n/a | 0.699 / 0.699 / 0.699 |
| output_head | 1/1 | n/a | 0.09619 / 0.09619 / 0.09619 | 0.0638 / 0.0638 / 0.0638 | 0.4927 / 0.4927 / 0.4927 |
- unchanged kinds: final_normalization 0/1, post_attention_normalization 0/34
- exactly-0 changed tensors: none

## Directions
| group | count | median cosine | min cosine | median_direction_defined |
| --- | --- | --- | --- | --- |
| output_head:131072 | 1 | 1 | 1 | true |
| embedding:131072 | 1 | 1 | 1 | true |
| feed_forward_down:4096 | 34 | 0.9994 | 0.006001 | true |
| feed_forward_gate:14336 | 34 | 0.1564 | 0.1182 | true |
| feed_forward_up:14336 | 34 | 0.1342 | 0.1222 | true |
| attention_key:1024 | 34 | 0.1386 | 0.02752 | true |
| attention_output:4096 | 34 | 0.997 | 0.008836 | true |
| attention_query:4096 | 34 | 0.1317 | 0.0835 | true |
| attention_value:1024 | 34 | 0.1286 | 0.07858 | true |
| other:4096 | 2 | 0.0255 | 0.0255 | true |
- svd: seed 0, top_k 8, sketch_columns 12, power_iterations 4
- unused_shared_kv 0, original_only 0, modified_only 0, dropped_towers 0, dropped_statistics 0

## Oddities
- none
