# Stage 1: wangzhang/gemma-4-31B-it-abliterated

Original: `google/gemma-4-31B-it`

Verdict: **consistent with re-save noted**

Revisions: modified `d7431183c443443024debb08b222cbcf2e424da7`; original `419b2efe421994fdfd3394e621983d4cc511cd4f`.

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

## Explained by re-save: `template.default`

Original file: `chat_template.jinja@145dc250`.

Modified file: `chat_template.jinja`.

The template equals the original repository's own later revision 145dc250 (2026-04-28, "fix(chat_template): update SI and tool call handling (#86)"), and the fixed conversation renders identically.

The `default` template source differs beyond line endings and trailing whitespace.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: single-projection-selected.
