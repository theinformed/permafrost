# Stage 1: bgg1996/Melinoe-Gemma4-31B-VL-heretic

Original: `bgg1996/Melinoe-Gemma4-31B-VL`

Verdict: **consistent with re-save noted**

Revisions: modified `ac6bff067604e3f8314d57cee38ff7ecbb05cf90`; original `26acdef2fad3f56eff343f1f251ccf1668f944aa`.

## Explained by re-save: `generation.transformers_version`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The saved version string changed.

## Explained by re-save: `config.text_config.moe_intermediate_size`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.22.1.

## Explained by re-save: `config.transformers_version`

Original file: `config.json`.

Modified file: `config.json`.

The saved version string changed.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: directional-per-layer-selected.
