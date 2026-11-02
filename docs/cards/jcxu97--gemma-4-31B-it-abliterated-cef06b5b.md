# Stage 1: jcxu97/gemma-4-31B-it-abliterated

Original: `google/gemma-4-31B-it`

Verdict: **consistent with re-save noted**

Revisions: modified `3772316f30c3252ba3347fd1c2ba812e1c9dbb2d`; original `439edf5652646a0d1bd8b46bfdc1d3645761a445`.

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
