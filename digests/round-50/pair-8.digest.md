# Pair 8 digest

## Pair
- modified: llmfan46/Omega-Darker-Gaslight_The-Final-Forgotten-Fever-Dream-24B-ultra-uncensored-heretic-v1 @ 62481e372196cf413ceafb782eba1d3ace347941
- original: ReadyArt/Omega-Darker-Gaslight_The-Final-Forgotten-Fever-Dream-24B @ ed40644353a0fbf5ed51f4c1b4b02cbaeb261f55
- receipt: pair 8, measurement_sha256 c142a27c
- job, node, seconds: not carried

## Metadata
- verdict: unexplained differences
- differences: 1011 (explained by re-save 4, unexplained 1007)
  - special_tokens.added_tokens_decoder:0: {'content': '<unk>', 'lstrip': False, 'normalized': False... -> null
  - special_tokens.added_tokens_decoder:1: {'content': '<s>', 'lstrip': False, 'normalized': False, ... -> null
  - special_tokens.added_tokens_decoder:10: {'content': '[IMG]', 'lstrip': False, 'normalized': False... -> null
  - special_tokens.added_tokens_decoder:100: {'content': '<SPECIAL_100>', 'lstrip': False, 'normalized... -> null
  - special_tokens.added_tokens_decoder:101: {'content': '<SPECIAL_101>', 'lstrip': False, 'normalized... -> null
  - special_tokens.added_tokens_decoder:102: {'content': '<SPECIAL_102>', 'lstrip': False, 'normalized... -> null
  - special_tokens.added_tokens_decoder:103: {'content': '<SPECIAL_103>', 'lstrip': False, 'normalized... -> null
  - special_tokens.added_tokens_decoder:104: {'content': '<SPECIAL_104>', 'lstrip': False, 'normalized... -> null
  - special_tokens.added_tokens_decoder:105: {'content': '<SPECIAL_105>', 'lstrip': False, 'normalized... -> null
  - special_tokens.added_tokens_decoder:106: {'content': '<SPECIAL_106>', 'lstrip': False, 'normalized... -> null
  - special_tokens.added_tokens_decoder:107: {'content': '<SPECIAL_107>', 'lstrip': False, 'normalized... -> null
  - special_tokens.added_tokens_decoder:108: {'content': '<SPECIAL_108>', 'lstrip': False, 'normalized... -> null
  - special_tokens.added_tokens_decoder:109: {'content': '<SPECIAL_109>', 'lstrip': False, 'normalized... -> null
  - special_tokens.added_tokens_decoder:11: {'content': '<pad>', 'lstrip': False, 'normalized': False... -> null
  - special_tokens.added_tokens_decoder:110: {'content': '<SPECIAL_110>', 'lstrip': False, 'normalized... -> null
  - special_tokens.added_tokens_decoder:111: {'content': '<SPECIAL_111>', 'lstrip': False, 'normalized... -> null
  - special_tokens.added_tokens_decoder:112: {'content': '<SPECIAL_112>', 'lstrip': False, 'normalized... -> null
  - special_tokens.added_tokens_decoder:113: {'content': '<SPECIAL_113>', 'lstrip': False, 'normalized... -> null
  - special_tokens.added_tokens_decoder:114: {'content': '<SPECIAL_114>', 'lstrip': False, 'normalized... -> null
  - special_tokens.added_tokens_decoder:115: {'content': '<SPECIAL_115>', 'lstrip': False, 'normalized... -> null
  - and 991 more
- missing: original: generation_config.json missing
- limitation: This metadata audit does not certify the absence of hidden behavior.
- card headings: ## Explained by re-save: `special_tokens.tokenizer_config.json:additional_special_tokens`, ## Explained by re-save: `config.pad_token_id`, ## Explained by re-save: `config.transformers_version`, ## Explained by re-save: `template_source.tokenizer_config`

## Weights assessment
- summary: assessment recipe_violations, matched_tensors 363, max_relative_difference_outside_changed_set 0.0001067, max_relative_difference_outside_recipe_set 0, min_first_singular_energy_share 0.9134
- threshold: 0.001
- nearest recipe: directional-per-layer-selected, matched false
  - directional-per-layer-selected: matched false, 11 violations
  - single-projection-selected: matched false, 23 violations
  - directional-per-layer: matched false, 81 violations
  - single-projection: matched false, 93 violations
- schema_version 1; scope: Weight differences alone cannot certify the absence of hidden behavior.

## Changed tensors
| kind | changed/total | layers | relative change | first share | positive fraction |
| --- | --- | --- | --- | --- | --- |
| attention_output | 11/40 | 10-33 | 0.03816 / 0.06771 / 0.1366 | 0.9134 / 0.9421 / 0.9556 | 0.3569 / 0.4119 / 0.4607 |
- unchanged kinds: attention_key 0/40, attention_query 0/40, attention_value 0/40, embedding 0/1, feed_forward_down 0/40, feed_forward_gate 0/40, feed_forward_up 0/40, final_normalization 0/1, input_normalization 0/40, output_head 0/1, post_attention_normalization 0/40
- exactly-0 changed tensors: none

## Directions
| group | count | median cosine | min cosine | median_direction_defined |
| --- | --- | --- | --- | --- |
| attention_output:5120 | 11 | 0.3389 | 0.2128 | true |
- svd: seed 0, top_k 8, sketch_columns 12, power_iterations 4
- unused_shared_kv 0, original_only 0, modified_only 0, dropped_towers 0, dropped_statistics 0

## Oddities
- none
