# Stage 1: ressl/gemma-4-31B-it-uncensored

Original: `google/gemma-4-31B-it`

Verdict: **consistent with re-save noted**

Revisions: modified `b7e5c931eaa8920d34d990c5f83d43bb04effc83`; original `3548789868c5356dbf307c98e6f609007b82b3eb`.

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

## Explained by re-save: `template.default`

Original file: `chat_template.jinja@68abe480`.

Modified file: `chat_template.jinja`.

The template equals the original repository's own later revision 68abe480 (2026-07-15, "fix: chat template — null handling, reasoning preservation, turn-tag balance, input validation (#118)"), and the fixed conversation renders identically.

The `default` template source differs beyond line endings and trailing whitespace.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: directional-per-layer.
