# Stage 1: mlabonne/gemma-3-27b-it-abliterated

Original: `google/gemma-3-27b-it`

Verdict: **unexplained differences**

Revisions: modified `eaa815dffdf0ea808a0421e4a48891bf52496a16`; original `dfb98f29ff907e391ceed2be3834ca071ea260f1`.

Changed fields:

- `config.text_config.attention_bias` (unexplained)
- `config.text_config.attention_dropout` (unexplained)
- `config.text_config.attn_logit_softcapping` (unexplained)
- `config.text_config.cache_implementation` (unexplained)
- `config.text_config.final_logit_softcapping` (unexplained)
- `config.text_config.hidden_activation` (unexplained)
- `config.text_config.initializer_range` (unexplained)
- `config.text_config.max_position_embeddings` (unexplained)
- `config.text_config.rms_norm_eps` (unexplained)
- `config.text_config.rope_local_base_freq` (unexplained)
- `config.text_config.rope_theta` (unexplained)
- `config.text_config.sliding_window_pattern` (unexplained)
- `config.text_config.torch_dtype` (unexplained)
- `config.text_config.use_cache` (unexplained)
- `config.text_config.vocab_size` (unexplained)
- `config.vision_config.attention_dropout` (unexplained)
- `config.vision_config.hidden_act` (unexplained)
- `config.vision_config.layer_norm_eps` (unexplained)
- `config.vision_config.num_channels` (unexplained)
- `config.vision_config.torch_dtype` (unexplained)

The fixed conversation renders identically with the `default` template.

This metadata audit does not certify the absence of hidden behavior.

Weights: recipe_match. Nearest recipe: single-projection.
