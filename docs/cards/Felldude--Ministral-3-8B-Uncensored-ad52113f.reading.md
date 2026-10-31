# Reading of the Stage 1 and Stage 2 result: Felldude/Ministral-3-8B-Uncensored against mistralai/Ministral-3-8B-Base-2512 (2026-10-31)

Measured on Nautilus, round 16 piece 5 (push card 5433, round card 5434, download job 4120061, compare job 4120066 on
the background queue, sweep 4120069; pulled home by card 5467). Modified revision `43981c56` (2026-05-25, a README
commit; the repository was created on 2026-05-23 at 18:48Z and the weights uploaded at 18:54Z), original pinned at
`d4883f9b` (2026-01-15), the pretrained base the copy's `base_model` field names. The maker's card is titled
"Ministral 3 8B Instruct Uncensored", calls the copy a "full finetune" trained "for VL and LLM task related to NSFW
subjects", tags it fp32, bf16 and fp16, and points to a desktop interface on another site; it gives no training
settings.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection`, 312 flags, on the cluster and after
re-scoring at home: 174 unexpected changes, 69 first energy shares, 68 cross-layer cosines and one cross-kind
direction. On reading, the copy is dense training of the whole language model at 5 to 11 percent, saved in float32,
and no ablation; the flags are the single-projection envelope failing on a copy that claims no projection.

- 243 of 531 tensors changed: the query, key, value, attention output, gate, up and down projections of all 34 layers
  (238), the token embedding (0.064 of its norm), the output head (0.096), the two linear maps of the multimodal
  projector (0.077 and 0.081) and layer 0's input normalisation (0.0044). The 218 tensors of the vision tower, the
  projector's normalisation and patch merger, and the other 67 normalisation vectors are unchanged (largest relative
  difference 0.00037 on a post-attention normalisation, 0.000005 in the vision tower).
- Every tensor is float32 in the copy against bfloat16 in the original; the vision tower's 0.000005 is the size of
  that cast and nothing else.
- The change is training in every matrix: relative change 0.050 to 0.110 per projection (medians 0.071 to 0.084 by
  kind), first-value shares 0.001 to 0.070, first eight 0.009 to 0.25, the first singular value 1.0 to 1.7 times the
  second, 0.77 to 1.13 of the original's action kept along the leading directions, leading directions unrelated
  across layers (cosine 0.03 to 0.61, medians 0.13 to 0.35), row norms moved by 0.033 to 0.078. Nothing in it is
  rank one and no direction is shared, so there is no ablation to read under it.
- The token embedding's row-norm error reads 1.4e12: rows that are exactly zero in the original (unused vocabulary
  entries) are nonzero in the copy, which is what training with a dense gradient on the embedding does.
- The change is four to ten times ccharnkij's adapter training on the Reasoning sibling of this base (0.006 to 0.018
  per projection, round 8, finding 17), and it reaches the embedding, the head and the projector, which that copy
  left alone. The two copies stand on different original files and share no equal field.

| Kind | Changed | Relative change | E1 | E8 | Left, direction 1 | Right, direction 1 | Row norms | Cross-layer cosine |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Query | 34 of 34 | 0.056 to 0.096 | 0.006 to 0.070 | 0.031 to 0.208 | 0.82 to 0.96 | 0.96 to 0.99 | 0.038 to 0.077 | 0.09 to 0.23 |
| Key | 34 of 34 | 0.050 to 0.094 | 0.008 to 0.058 | 0.040 to 0.252 | 0.86 to 1.00 | 0.90 to 1.00 | 0.036 to 0.078 | 0.04 to 0.27 |
| Value | 34 of 34 | 0.056 to 0.110 | 0.004 to 0.025 | 0.023 to 0.107 | 0.86 to 0.97 | 0.82 to 0.96 | 0.035 to 0.055 | 0.09 to 0.25 |
| Attention output | 34 of 34 | 0.065 to 0.107 | 0.002 to 0.020 | 0.014 to 0.085 | 0.93 to 1.04 | 0.82 to 1.05 | 0.036 to 0.040 | 0.03 to 0.50 |
| Gate | 34 of 34 | 0.072 to 0.098 | 0.003 to 0.006 | 0.017 to 0.033 | 0.77 to 1.13 | 0.97 to 1.03 | 0.039 to 0.067 | 0.11 to 0.27 |
| Up | 34 of 34 | 0.072 to 0.085 | 0.003 to 0.014 | 0.015 to 0.037 | 0.81 to 1.08 | 0.96 to 1.01 | 0.038 to 0.059 | 0.12 to 0.17 |
| Down | 34 of 34 | 0.068 to 0.087 | 0.001 to 0.008 | 0.009 to 0.028 | 0.91 to 0.99 | 0.77 to 0.95 | 0.033 to 0.038 | 0.03 to 0.61 |
| Token embedding | 1 of 1 | 0.064 | 0.011 | 0.033 | 0.94 | 0.97 | zero rows filled | |
| Output head | 1 of 1 | 0.096 | 0.064 | 0.151 | 0.97 | 0.90 | 0.115 | |
| Projector linear 1, 2 | 2 of 2 | 0.077, 0.081 | 0.027, 0.061 | 0.131, 0.241 | 0.85, 0.90 | 0.80, 0.92 | 0.057, 0.073 | |
| Vision tower | 0 of 218 | at most 0.000005 | | | | | | |
| Normalisations | 1 of 69 | 0.0044 (layer 0 input); others at most 0.00037 | | | | | | |

## Token and configuration side (Stage 1)

The cluster's card read "unexplained differences" in 1,011 fields and the home judgement keeps them (the
later-revision rule does not run when one side has no template), so the committed card reads "unexplained
differences"; the reading sorts them by hand into one real change and a re-save.

- `template.default`: the base has no chat template and the copy carries one of 7,759 bytes that begins "You are
  Ministral-3-8B-Instruct-2512, a Large Language Model (LLM) created by Mistral AI". It equals
  mistralai/Ministral-3-8B-Instruct-2512's `chat_template.jinja` byte for byte at that repository's first three
  revisions (`dbbffa0e` of 2025-12-02 through `aae06a21` of 2026-06-30; Mistral replaced it on 2026-07-15 with an
  11,912-byte file, after this copy was made). A real difference from the stated original, and the instruct
  lineage marker of finding 8: the file came from the instruct repository, or from a model made from it.
- `config.tie_word_embeddings` false, added: the instruct repository's `config.json` carries the same key and value
  and the base's omits it; the text and vision configurations are otherwise equal to both. `config.dtype` float32:
  the saved precision, a real change in the file and the 5 to 11 percent change in the weights is not an artefact of
  it.
- `special_tokens.added_tokens_decoder:0` to `:999` (1,000 fields), `added_tokens.decoder` and
  `special_tokens.tokenizer_config.json:additional_special_tokens`: the copy's `tokenizer_config.json` has no
  `added_tokens_decoder` block (the base's lists 1,000 control tokens) and its `additional_special_tokens` is null;
  and the copy has no `special_tokens_map.json` (five fields). The token ids, the vocabulary and `tokenizer.json`
  are unchanged, so the declarations moved into `tokenizer.json` and the files that repeat them were not written: a
  re-save by a tool that writes the fast tokenizer alone. `config.vision_config.rope_theta` absent on the copy: a
  default the loader restores (finding 11's rule). The generation settings are equal.

## For the recipe library

Not an ablation and not consistent with the stated original: the weights carry dense training at 5 to 11 percent of
every language-model matrix, and the template and configuration carry the instruct model's files, so the copy is a
fine-tune of Ministral-3-8B-Instruct-2512, or of a model made from it, declared against the pretrained base. The
one comparison that would say how much of the 5 to 11 percent is Mistral's instruction tuning and how much the
maker's is against the instruct weights, owed to the next batch with the 3MPER0RR pair of finding 8. The saved
direction vectors are not committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/nautilus16/measurements/pair-5/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
