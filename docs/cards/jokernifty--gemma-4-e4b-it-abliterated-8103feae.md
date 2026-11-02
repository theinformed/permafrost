# Stage 1: jokernifty/gemma-4-e4b-it-abliterated

Original: `google/gemma-4-E4B-it`

Verdict: **unexplained differences**

Revisions: modified `7f7586e875bb1234c9e3744133fe075ca1b43025`; original `d6436b3d62967e1af08bbb046c6300b2a9ae8e85`.

Changed fields:

- `config.audio_config.dtype` (unexplained)
- `config.dtype` (unexplained)
- `config.text_config.dtype` (unexplained)
- `config.vision_config.dtype` (unexplained)

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

Weights: recipe_match. Nearest recipe: single-projection-selected.
