# Stage 1: MoonRide/gemma-4-31B-it-heretic-ara-custom

Original: `google/gemma-4-31B-it`

Verdict: **consistent with re-save noted**

Revisions: modified `7c0ded772511b624494ab98dd37e49fbca90d473`; original `145dc2508c480a64b47242f160d286cff94a2343`.

## Explained by re-save: `generation.transformers_version`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The saved version string changed.

## Explained by re-save: `config.text_config.moe_intermediate_size`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.6.2.

## Explained by re-save: `config.transformers_version`

Original file: `config.json`.

Modified file: `config.json`.

The saved version string changed.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: directional-per-layer-selected.
