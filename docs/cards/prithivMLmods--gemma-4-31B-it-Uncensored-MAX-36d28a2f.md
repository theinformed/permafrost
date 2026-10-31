# Stage 1: prithivMLmods/gemma-4-31B-it-Uncensored-MAX

Original: `google/gemma-4-31B-it`

Verdict: **consistent with re-save noted**

Revisions: modified `6a6218c2fea36e9158a7a7626aed6e6936749806`; original `419b2efe421994fdfd3394e621983d4cc511cd4f`.

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

Weights: recipe_violations. Nearest recipe: single-projection.
