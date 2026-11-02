# Stage 1: NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals8

Original: `google/gemma-4-E4B-it`

Verdict: **consistent with re-save noted**

Revisions: modified `c2cf78ab967c4d4fcb107bf580503e381a2811a0`; original `292a7e278a400932df35f9fd4b1501edd04133a5`.

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

Original file: `chat_template.jinja@c53e9d33`.

Modified file: `chat_template.jinja`.

The template equals the original repository's own later revision c53e9d33 (2026-04-28, "fix(chat_template): update SI and tool call handling (#28)"), and the fixed conversation renders identically.

The `default` template source differs beyond line endings and trailing whitespace.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: directional-per-layer-selected.
