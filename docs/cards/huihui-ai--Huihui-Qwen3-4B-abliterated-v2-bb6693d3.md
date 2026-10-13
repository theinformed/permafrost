# Stage 1: huihui-ai/Huihui-Qwen3-4B-abliterated-v2

Original: `Qwen/Qwen3-4B`

Verdict: **unexplained differences**

Revisions: modified `a494c65b10bf8fdc56c0ff11d36987c1d018f162`; original `1cfa9a7208912126459214e8b04321603b3df60c`.

Changed fields:

- `special_tokens.special_tokens_map.json:additional_special_tokens` (unexplained)
- `special_tokens.special_tokens_map.json:eos_token` (unexplained)
- `special_tokens.special_tokens_map.json:pad_token` (unexplained)
- `added_tokens.file` (unexplained)
- `generation.transformers_version` (unexplained)
- `config.transformers_version` (unexplained)
- `template_source.tokenizer_config` (unexplained)
- `template.default` (unexplained)

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.
