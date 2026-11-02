# Stage 1: treadon/gemma4-E4B-it-abliterated

Original: `google/gemma-4-E4B-it`

Verdict: **consistent with re-save noted**

Revisions: modified `8d0b94c9814ecf5655bd13b44a43d5447435388e`; original `83df0a889143b1dbfc61b591bbc639540fd9ce4c`.

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

Weights: recipe_match. Nearest recipe: directional-per-layer-selected.
