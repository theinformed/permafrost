# Stage 1: tvall43/gemma-4-E2B-it-heretic-v0

Original: `google/gemma-4-E2B-it`

Verdict: **consistent with re-save noted**

Revisions: modified `39472f8532d0a854cf82f608c002a26b74e33dee`; original `4742fe843cc01b9aed62122f6e0ddd13ea48b3d3`.

## Explained by re-save: `config.text_config.moe_intermediate_size`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side and loads as this same default in transformers 5.22.1.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_match. Nearest recipe: single-projection-selected.
