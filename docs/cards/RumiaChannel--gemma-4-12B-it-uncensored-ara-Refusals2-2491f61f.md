# Stage 1: RumiaChannel/gemma-4-12B-it-uncensored-ara-Refusals2

Original: `google/gemma-4-12B-it`

Verdict: **consistent with re-save noted**

Revisions: modified `23484b14d662acf9227dfe20eb97090c9ab36272`; original `5926caa4ec0cac5cbfadaf4077420520de1d5205`.

## Explained by re-save: `generation.transformers_version`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The saved version string changed.

## Explained by re-save: `config.audio_config.audio_samples_per_token`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side, and both saved configurations load it as this same value in transformers 5.22.1.

## Explained by re-save: `config.audio_config.dtype`

Original file: `config.json`.

Modified file: `config.json`.

The sub-configuration repeats the data type the top-level configuration already declares, where the other side left it null.

## Explained by re-save: `config.audio_config.hidden_size`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side, and both saved configurations load it as this same value in transformers 5.22.1.

## Explained by re-save: `config.audio_config.output_proj_dims`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side, and both saved configurations load it as this same value in transformers 5.22.1.

## Explained by re-save: `config.text_config.dtype`

Original file: `config.json`.

Modified file: `config.json`.

The sub-configuration repeats the data type the top-level configuration already declares.

## Explained by re-save: `config.transformers_version`

Original file: `config.json`.

Modified file: `config.json`.

The saved version string changed.

## Explained by re-save: `config.vision_config.dtype`

Original file: `config.json`.

Modified file: `config.json`.

The sub-configuration repeats the data type the top-level configuration already declares, where the other side left it null.

## Explained by re-save: `config.vision_config.model_patch_size`

Original file: `config.json`.

Modified file: `config.json`.

The field is absent on the other side, and both saved configurations load it as this same value in transformers 5.22.1.

## Explained by re-save: `template.default`

Original file: `chat_template.jinja@711c1368`.

Modified file: `chat_template.jinja`.

The template equals the original repository's own later revision 711c1368 (2026-07-15, "fix: chat template — null handling, reasoning preservation, turn-tag balance, input validation (#35)"), and the fixed conversation renders identically.

The `default` template source differs beyond line endings and trailing whitespace.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: directional-per-layer-selected.
