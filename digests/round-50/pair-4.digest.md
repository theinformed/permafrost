# Pair 4 digest

## Pair
- modified: Naphula/Quill-v1-abliterated @ 406dfb63ab3ff234495096126751b74e5e6ebe20
- original: sam-paech/Quill-v1 @ 3cab1cac9d3de0d25b48ea86b4533aa220231f20
- receipt: pair 4, measurement_sha256 1134d9bc
- job, node, seconds: not carried

## Metadata
- verdict: undecided
- differences: 0 (none)
- missing: original template default render failed: ValueError: ValueError: System role not supported; modified template default render failed: ValueError: ValueError: System role not supported
- limitation: This metadata audit does not certify the absence of hidden behavior.
- card headings: none

## Weights assessment
- summary: assessment recipe_match, matched_tensors 464, max_relative_difference_outside_changed_set 0, max_relative_difference_outside_recipe_set 0, min_first_singular_energy_share 0.9952
- threshold: 0.001
- nearest recipe: single-projection, matched true
  - single-projection: matched true, 0 violations
  - single-projection-selected: matched true, 0 violations
  - directional-per-layer: matched true, 0 violations
  - directional-per-layer-selected: matched true, 0 violations
- schema_version 1; scope: Weight differences alone cannot certify the absence of hidden behavior.

## Changed tensors
| kind | changed/total | layers | relative change | first share | positive fraction |
| --- | --- | --- | --- | --- | --- |
| attention_output | 42/42 | 0-41 | 0.02282 / 0.02497 / 0.02902 | 0.9952 / 0.996 / 0.9969 | 0.3973 / 0.4024 / 0.4127 |
| feed_forward_down | 42/42 | 0-41 | 0.02353 / 0.02498 / 0.02724 | 0.9955 / 0.9959 / 0.9965 | 0.3966 / 0.4027 / 0.4096 |
- unchanged kinds: other 0/84, attention_key 0/42, attention_query 0/42, attention_value 0/42, embedding 0/1, feed_forward_gate 0/42, feed_forward_up 0/42, final_normalization 0/1, input_normalization 0/42, post_attention_normalization 0/42
- exactly-0 changed tensors: none

## Directions
| group | count | median cosine | min cosine | median_direction_defined |
| --- | --- | --- | --- | --- |
| feed_forward_down:3584 | 42 | 0.9996 | 0.9969 | true |
| attention_output:3584 | 42 | 0.9996 | 0.9969 | true |
- svd: seed 0, top_k 8, sketch_columns 12, power_iterations 4
- unused_shared_kv 0, original_only 0, modified_only 0, dropped_towers 0, dropped_statistics 0

## Oddities
- none
