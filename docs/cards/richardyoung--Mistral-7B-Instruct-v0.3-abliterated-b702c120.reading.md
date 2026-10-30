# Reading of the Stage 1 and Stage 2 result: richardyoung/Mistral-7B-Instruct-v0.3-abliterated against mistralai/Mistral-7B-Instruct-v0.3 (2026-10-30)

Measured on Blueback, round 7 piece 5 (round card 5291, compare jobs 3392878 to 3392885, 4 to 6 minutes each, exit 0;
pulled home by card 5302). Modified revision `cb427700` (2026-09-26, a README commit; the weights were uploaded on
2025-12-15), original pinned at `c170c708` (2025-12-03). The maker's card names Heretic v1.1 and reports 16 refusals in
100 at a KL divergence of 0.317, as one copy in a comparison of abliteration tools.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection-selected`, 21 flags, on the cluster
and after re-scoring at home. All 21 flags are energy shares at the bfloat16 floor. On reading, the footprint matches
the card.

- 48 of 291 tensors changed: the feed-forward down projection in layers 5 to 31 (27 matrices) and the attention
  output in layers 11 to 31 (21 matrices) of 32. Nothing else moved; the largest relative change outside the changed
  set is exactly 0, the embedding included.
- One direction, shared across layers and kinds: cosine 0.99995 or better with the median within each kind, 0.9998
  across kinds, 0.9998 or better within each layer.
- The weight follows the tool's kernel. Along the shared direction the copy keeps -0.31 to -0.24 of the original's
  action on the down projections (a weight of 1.24 to 1.31) and 0.18 to 0.46 on the attention outputs (a weight of
  0.54 to 0.82), the two components tuned apart as the tool's description says.
- Row norms moved by 0.003 to 0.025 relative: a plain projection, no norm restoration in this version of the tool.
- The 21 flags are the storage floor: first-value shares of 0.973 to 0.987 on attention outputs whose relative change
  is 0.009 to 0.013, leftover 0.00145 to 0.00153 of the weight norm. The down projections, changed by 0.019 to
  0.025, clear 0.99.

## Token and configuration side (Stage 1)

The tool's Stage 1 assessment is "unexplained differences" in four fields, before and after the home re-judgment.

- `special_tokens.special_tokens_map.json:pad_token` and `special_tokens.tokenizer_config.json:pad_token`: `</s>`
  (id 2) added in both files where the original declares none. Heretic's model loader sets the pad token to the
  end-of-sequence token when a tokenizer has none; the two files agree and the generation settings carry no pad. A
  real change, made by the tool, harmless for single-prompt use.
- `config.dtype` and `config.torch_dtype`: the copy's library (4.57.3) writes `dtype` where the original's
  (4.42.0.dev0) wrote `torch_dtype`, both bfloat16. Re-save.
- The chat template moved from `tokenizer_config.json` to `chat_template.jinja` and renders identically; the tool
  explains it.

## For the recipe library

Consistent with the stated change on both sides. With piece 3 this gives the single-direction heretic edit two
measured copies on two bases, and the version difference shows in the row norms: 0.003 to 0.025 here (v1.1), 0.0018
to 0.0040 on the later version. The saved direction vectors are not committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/blueback7/measurements/pair-5/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
