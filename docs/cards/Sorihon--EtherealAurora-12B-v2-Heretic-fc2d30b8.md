# Stage 1: Sorihon/EtherealAurora-12B-v2-Heretic

Original: `yamatazen/EtherealAurora-12B-v2`

Verdict: **unexplained differences**

Revisions: modified `b8613fc8cf890c7d61a4fba36cc9fcbc5414f290`; original `f218cef001312aa9b547b992e12dc9e330c3fff8`.

Changed fields:

- `generation` (unexplained)
- `config._name_or_path` (expected)
- `config.dtype` (unexplained)
- `config.torch_dtype` (unexplained)
- `config.use_cache` (unexplained)

## Explained by re-save: `config.transformers_version`

Original file: `config.json`.

Modified file: `config.json`.

The saved version string changed.

## Explained by re-save: `template_source.tokenizer_config`

Original file: `tokenizer_config.json`.

Modified file: `chat_template.jinja`.

The template moved; line endings and trailing whitespace normalize equally, and the fixed conversation renders identically.

Missing evidence:

- original: generation_config.json missing

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_violations. Nearest recipe: directional-per-layer-selected.
