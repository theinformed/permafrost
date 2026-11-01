# Stage 1: TheUmbraWalker/gemma-4-E4B-it-2-heretic

Original: `google/gemma-4-E4B-it`

Verdict: **consistent with re-save noted**

Revisions: modified `495cb4db396f82409fcde5a5bf6f752dadc88ab4`; original `3555bddc93a623db8887dd2e52123facc45ade77`.

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
