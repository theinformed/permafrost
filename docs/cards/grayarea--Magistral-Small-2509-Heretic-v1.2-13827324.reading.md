# Reading of the Stage 1 and Stage 2 result: grayarea/Magistral-Small-2509-Heretic-v1.2 against mistralai/Magistral-Small-2509 (2026-10-31)

Measured on Nautilus, round 18 piece 8 (push card 5473, round card 5477, download job 4125751, compare job 4125759
on the background queue, sweep 4125760; pulled home by card 5493). Modified revision `f4a54de9` (2026-03-14, the
commit that added `tekken.json`; the repository was created on 2026-03-13 at 13:09Z and the weights uploaded three
minutes later), original pinned at `a31cc96a` (2026-02-23), the same original and the same ten shards as pair 7.
The maker's card names Heretic 1.2.0 with "MPOA enabled (Magnitude-Preserving Orthogonal Ablation)", full row
renormalization, a winsorization quantile of 0.997, a custom dataset and a model-specific configuration; it reports
0 refusals in 108 against 97 for the original and a KL divergence of 0.0182, and perplexity and benchmark figures for
its quantized versions. The copy's `config.json` carries a `grayarea` block that records the configuration and
dataset names as `heretic: loom-v1`.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 13 flags, on the
cluster and after re-scoring at home, all 13 energy shares at the storage floor on the down projections of layers
10 to 23. On reading, the copy is one shared direction projected out of a chosen set of residual writers on the
output side, with a smooth per-layer weight on the down projections and a near-constant one on the attention
outputs, and the row renormalization the card claims reads as three tenths to one percent left on the rows.

- 64 of 585 tensors changed: the attention outputs of layers 6 to 39 (34) and the down projections of layers 10 to
  39 (30). Nothing else moved; the largest relative change outside the changed set is exactly 0 and 521 tensors
  equal the original, the vision tower, the projector and every normalisation among them.
- One shared direction: the leading directions agree across layers at cosine 0.97 to 1.00 (median 0.998 on the
  attention outputs, 0.999 on the down projections) and the two writers of a layer at 0.95 to 1.00 on the 30 layers
  that carry both. Rank one at the floor: first-value share 0.967 to 0.996 on relative changes of 0.008 to 0.025,
  leftover 0.0014 to 0.0016 of the weight norm, every matrix inside the 0.0025 line, the 13 flagged down projections
  being the ones the edit moved by less than 1.55 percent.
- Output side on all 64: the copy keeps −0.39 to 0.49 of the original's action along the direction on the left and
  0.07 to 0.84 on the right, the left below the right in every matrix.
- Two weight profiles. On the attention outputs the kept fraction is −0.24 to −0.35 on 32 of 34 (weight 1.24 to
  1.35) with layer 6 at −0.11 and layer 27 at 0.08 (weights 1.11 and 0.92). On the down projections it follows a
  kernel: 0.49 at layer 10 falling through 0.00 at layer 21 to −0.39 at layers 31 and 32 and rising to −0.13 at
  layer 39, weights 0.51 to 1.39 to 1.13, the rise-and-fall shape finding 8 read on the maker 3MPER0RR's Mistral 7B
  copy (0.11 to 1.32 to 0.74).
- Row norms moved by 0.0026 to 0.0107 relative (median 0.0045) under a claim of full row renormalization: the
  restoration left half a percent, as coder3101's preservation claim leaves seven tenths on every base (finding 22).

| Layer | Attention output: change, E1, left, weight | Down projection: change, E1, left, weight | Row norms |
| --- | --- | --- | --- |
| 6 | 0.020, 0.994, −0.11, 1.11 | | 0.0051 |
| 7 | 0.019, 0.993, −0.27, 1.27 | | 0.0040 |
| 8 | 0.019, 0.993, −0.28, 1.28 | | 0.0046 |
| 9 | 0.020, 0.994, −0.28, 1.28 | | 0.0049 |
| 10 | 0.019, 0.993, −0.27, 1.27 | 0.008, 0.967, 0.49, 0.51 | 0.0038, 0.0030 |
| 11 | 0.020, 0.994, −0.28, 1.28 | 0.009, 0.972, 0.44, 0.56 | 0.0049, 0.0033 |
| 12 | 0.020, 0.994, −0.24, 1.24 | 0.009, 0.975, 0.40, 0.60 | 0.0057, 0.0034 |
| 13 | 0.020, 0.994, −0.26, 1.26 | 0.010, 0.978, 0.36, 0.64 | 0.0051, 0.0042 |
| 14 | 0.021, 0.994, −0.24, 1.24 | 0.011, 0.982, 0.31, 0.69 | 0.0066, 0.0052 |
| 15 | 0.022, 0.995, −0.26, 1.26 | 0.012, 0.985, 0.27, 0.73 | 0.0082, 0.0038 |
| 16 | 0.021, 0.994, −0.31, 1.31 | 0.012, 0.985, 0.22, 0.78 | 0.0037, 0.0033 |
| 17 | 0.025, 0.996, −0.31, 1.31 | 0.013, 0.987, 0.18, 0.82 | 0.0093, 0.0036 |
| 18 | 0.023, 0.995, −0.35, 1.35 | 0.015, 0.989, 0.13, 0.87 | 0.0091, 0.0050 |
| 19 | 0.023, 0.995, −0.34, 1.34 | 0.015, 0.989, 0.09, 0.91 | 0.0063, 0.0041 |
| 20 | 0.024, 0.996, −0.35, 1.35 | 0.015, 0.990, 0.05, 0.95 | 0.0082, 0.0065 |
| 21 | 0.023, 0.995, −0.34, 1.34 | 0.015, 0.989, 0.01, 0.99 | 0.0107, 0.0039 |
| 22 | 0.018, 0.992, −0.31, 1.31 | 0.015, 0.990, −0.04, 1.04 | 0.0041, 0.0044 |
| 23 | 0.021, 0.994, −0.29, 1.29 | 0.016, 0.990, −0.08, 1.08 | 0.0048, 0.0037 |
| 24 | 0.021, 0.994, −0.31, 1.31 | 0.016, 0.991, −0.13, 1.13 | 0.0056, 0.0046 |
| 25 | 0.022, 0.995, −0.33, 1.33 | 0.017, 0.991, −0.16, 1.16 | 0.0060, 0.0040 |
| 26 | 0.022, 0.995, −0.33, 1.33 | 0.017, 0.992, −0.20, 1.20 | 0.0055, 0.0050 |
| 27 | 0.021, 0.995, 0.08, 0.92 | 0.017, 0.992, −0.25, 1.25 | 0.0043, 0.0028 |
| 28 | 0.019, 0.993, −0.27, 1.27 | 0.018, 0.992, −0.27, 1.27 | 0.0041, 0.0027 |
| 29 | 0.020, 0.994, −0.11, 1.11 | 0.018, 0.993, −0.31, 1.31 | 0.0038, 0.0031 |
| 30 | 0.019, 0.993, −0.31, 1.31 | 0.019, 0.993, −0.35, 1.35 | 0.0030, 0.0028 |
| 31 | 0.019, 0.993, −0.35, 1.35 | 0.019, 0.993, −0.39, 1.39 | 0.0041, 0.0031 |
| 32 | 0.018, 0.993, −0.32, 1.32 | 0.019, 0.993, −0.39, 1.39 | 0.0026, 0.0030 |
| 33 | 0.018, 0.993, −0.32, 1.32 | 0.019, 0.993, −0.35, 1.35 | 0.0035, 0.0035 |
| 34 | 0.018, 0.992, −0.28, 1.28 | 0.018, 0.993, −0.32, 1.32 | 0.0034, 0.0047 |
| 35 | 0.018, 0.992, −0.30, 1.30 | 0.018, 0.992, −0.28, 1.28 | 0.0057, 0.0064 |
| 36 | 0.019, 0.993, −0.24, 1.24 | 0.017, 0.992, −0.25, 1.25 | 0.0095, 0.0054 |
| 37 | 0.018, 0.993, −0.30, 1.30 | 0.016, 0.991, −0.21, 1.21 | 0.0056, 0.0043 |
| 38 | 0.017, 0.992, −0.30, 1.30 | 0.016, 0.991, −0.17, 1.17 | 0.0039, 0.0029 |
| 39 | 0.020, 0.993, −0.23, 1.23 | 0.016, 0.991, −0.13, 1.13 | 0.0077, 0.0043 |

"Left" is the fraction of the original's action kept along the leading left direction and the weight is one minus
it; row norms are the largest relative row change of the attention output and the down projection.

Against pair 7's copy of the same original, 48 matrices changed in both and no field is equal in any of them (0 of
288). The two heretics of one base are two methods: one direction per matrix on the input side at searched weights
of 1.69 to 4.71 there, one shared direction on the output side at 0.51 to 1.39 here, with a residue set there and
none here. Against the maker llmfan46's Gemma 4 copies this one shares nothing but the tool's name.

## Token and configuration side (Stage 1)

The cluster's card read "unexplained differences" on 2,027 fields, and the home judgement reads them as pair 7's
cause: the copy stands on the same third party's conversion of the original, and the original has no library
tokenizer to compare it with.

- The original ships its tokenizer as `tekken.json` and no `tokenizer.json`, tokenizer configuration or chat
  template; the tool reports those as missing on the original's side.
- The copy's `tokenizer.json` and `chat_template.jinja` equal unsloth/Magistral-Small-2509's files at its 2025-09-29
  revision (`dcfa8f67`) byte for byte, the template at 4,690 bytes (`817cbd47`); pair 7's template is the same file
  with carriage-return line endings. The 2,010 special-token fields are the 1,000 tokens listed once in
  `tokenizer.json` and once in the tokenizer configuration's decoder block, with the four named tokens and the
  additional-tokens list; the ids (`<s>` 1, `</s>` 2, `<pad>` 11, `<unk>` 0) and the vocabulary of 131,072 are the
  ones the original's own format carries.
- The eight configuration fields: the three token ids written at the top level, `dtype` repeated in the text and
  vision blocks, `unsloth_fixed` true, `transformers_version` 4.56.1 to 4.57.3, and the `grayarea` block above.
  Against pair 7 the copy keeps the original's `rope_theta` form and `tie_word_embeddings` layout, a 4.57 save
  against a 5.3 one of the same conversion.
- The copy's `SYSTEM_PROMPT.txt` (554 bytes) equals pair 7's and differs from the original's current one (566 bytes,
  revised on 2025-12-02); the two copies carry the file as it stood when the conversion was made. The fixed
  conversation renders the same string under the two copies' templates; the original has none to render.

## For the recipe library

Consistent with the card on the weights, with the renormalization claim read at 0.003 to 0.011 on the rows, and a
second case for the shared-direction entry with a per-layer weight that follows a kernel on one writer kind and
holds near 1.3 on the other. The token side closes by naming the conversion, as on pair 7. The saved direction
vectors are not committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/nautilus18/measurements/pair-8/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
