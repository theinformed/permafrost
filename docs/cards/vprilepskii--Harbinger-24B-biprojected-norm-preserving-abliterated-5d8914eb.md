# Stage 1: vprilepskii/Harbinger-24B-biprojected-norm-preserving-abliterated

Original: `LatitudeGames/Harbinger-24B`

Verdict: **unexplained differences**

Revisions: modified `8f9eee63326825024c57e7ec4935299bb5aae83f`; original `0ded8c1fd6d6d45ee9ca7a85291ce783f6d40c6a`.

Changed fields:

- `config._name_or_path` (expected)
- `config.dtype` (unexplained)
- `config.torch_dtype` (unexplained)

## Explained by re-save: `generation.transformers_version`

Original file: `generation_config.json`.

Modified file: `generation_config.json`.

The saved version string changed.

## Explained by re-save: `config.transformers_version`

Original file: `config.json`.

Modified file: `config.json`.

The saved version string changed.

## Explained by re-save: `template_source.tokenizer_config`

Original file: `tokenizer_config.json`.

Modified file: `chat_template.jinja`.

The template moved; line endings and trailing whitespace normalize equally, and the fixed conversation renders identically.

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: single-projection-selected.
