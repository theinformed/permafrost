# Stage 1: wangzhang/gemma-4-E2B-it-abliterated

Original: `google/gemma-4-E2B-it`

Verdict: **consistent with re-save noted**

Revisions: modified `9b367c2995c9529049bf7fa86b68e698136d1242`; original `b446025c61ecea876162774ee247706056963aba`.

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
