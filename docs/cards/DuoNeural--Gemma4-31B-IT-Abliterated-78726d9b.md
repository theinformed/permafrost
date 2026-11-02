# Stage 1: DuoNeural/Gemma4-31B-IT-Abliterated

Original: `google/gemma-4-31B-it`

Verdict: **consistent with re-save noted**

Revisions: modified `0e5a5b43b316aeae06617c1a6ef2f3805f90225b`; original `3548789868c5356dbf307c98e6f609007b82b3eb`.

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

Weights: recipe_violations. Nearest recipe: directional-per-layer.
