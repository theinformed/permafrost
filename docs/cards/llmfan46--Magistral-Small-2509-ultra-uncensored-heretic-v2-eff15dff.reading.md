# Reading of the Stage 1 and Stage 2 result: llmfan46/Magistral-Small-2509-ultra-uncensored-heretic-v2 against mistralai/Magistral-Small-2509 (2026-10-31)

Measured on Nautilus, round 18 piece 7 (push card 5473, round card 5477, download job 4125751, compare job 4125758
on the background queue, sweep 4125760; pulled home by card 5493). Modified revision `5733a332` (2026-03-27, a
README commit; the repository was created on 2026-03-17 at 22:11Z and the weights uploaded four minutes later),
original pinned at `a31cc96a` (2026-02-23, a README commit; the weights date from the 2025-09-17 squash). The
original is the first Mistral reasoning model in the census, a 24B vision-language model whose repository ships its
tokenizer in the maker's own format (`tekken.json` and `params.json`) with no `tokenizer.json`, no tokenizer
configuration and no chat template. The maker's card names the method and its parameters: Heretic 1.2.0 with
Arbitrary-Rank Ablation, start layer 9, end layer 37, preserve weight 0.9362, steer weight 0.0003, overcorrect
weight 0.9861, neighbour count 9; it reports 3 refusals in 100 against 92 for the original and a KL divergence of
0.0493, and it makes no preservation claim. The same original is round 18's pair 8.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 91 flags, on the
cluster and after re-scoring at home: 49 energy shares and 42 within-layer directions. On reading, the footprint is
the arbitrary-rank method on both residual writers, as on this round's coder3101 copy and unlike the maker's four
Gemma 4 copies, which edited attention outputs only.

- 49 of 585 tensors changed: the down projections of layers 9, 10 and 13 to 36 (26) and the attention outputs of
  layers 10 to 21, 24, 25, 27 to 29 and 31 to 36 (23), inside the card's range of 9 to 36 (end index exclusive).
  Seven matrices inside the range were rewritten under the threshold, the attention outputs of layers 9, 22, 23, 26
  and 30 and the down projections of 11 and 12, at 0.00008 to 0.00031 of their norm, so the largest relative change
  outside the changed set is 0.00031, on layer 23's attention output; 529 tensors equal the original, the vision
  tower and the projector among them.
- The arbitrary-rank profile: first-value share 0.841 to 0.971 (median 0.92), first eight values 0.927 to 0.989, on
  relative changes of 0.014 to 0.029 for the down projections and 0.032 to 0.093 for the attention outputs. The
  leftover beyond the first direction is 0.004 to 0.03 of the weight norm.
- The leading direction sits on the input side on all 49: the copy keeps 0.01 to 0.93 of the original's action on
  the left and −3.71 to −0.69 on the right, so the searched weight is 1.69 (layer 34's down projection) to 4.71
  (layer 35's attention output), median 2.1 on the down projections and 2.7 on the attention outputs. The band sits
  above the maker's Gemma 4 copies (1.27 to 4.41) and below coder3101's 31B (10.18).
- The leading directions differ by layer and by writer: cross-layer cosine 0.10 to 0.38 (median 0.17), and the two
  edits of a layer agree at 0.003 to 0.18 on the 21 layers that carry both.
- Row norms moved by 0.0004 to 0.0055 on the down projections and 0.0040 to 0.099 on the attention outputs, under no
  preservation claim, as on the maker's Gemma 4 copies (0.0006 to 0.066).

| Layer | Attention output: change, E1, right, weight | Down projection: change, E1, right, weight |
| --- | --- | --- |
| 9 | residue | 0.023, 0.846, −1.34, 2.34 |
| 10 | 0.052, 0.889, −1.61, 2.61 | 0.029, 0.841, −1.72, 2.72 |
| 11 | 0.068, 0.841, −1.74, 2.74 | residue |
| 12 | 0.048, 0.943, −2.22, 3.22 | residue |
| 13 | 0.042, 0.949, −1.50, 2.50 | 0.022, 0.875, −1.39, 2.39 |
| 14 | 0.058, 0.914, −1.69, 2.69 | 0.017, 0.890, −0.90, 1.90 |
| 15 | 0.040, 0.930, −1.46, 2.46 | 0.014, 0.939, −0.91, 1.91 |
| 16 | 0.042, 0.926, −1.26, 2.26 | 0.014, 0.941, −0.99, 1.99 |
| 17 | 0.044, 0.907, −1.34, 2.34 | 0.016, 0.935, −1.25, 2.25 |
| 18 | 0.062, 0.947, −1.83, 2.83 | 0.015, 0.910, −1.03, 2.03 |
| 19 | 0.032, 0.958, −0.98, 1.98 | 0.015, 0.923, −0.96, 1.96 |
| 20 | 0.047, 0.954, −1.28, 2.28 | 0.016, 0.943, −1.11, 2.11 |
| 21 | 0.041, 0.971, −1.24, 2.24 | 0.016, 0.923, −0.95, 1.95 |
| 22 | residue | 0.016, 0.930, −0.93, 1.93 |
| 23 | residue | 0.020, 0.941, −1.27, 2.27 |
| 24 | 0.055, 0.949, −1.89, 2.89 | 0.016, 0.944, −1.19, 2.19 |
| 25 | 0.050, 0.903, −1.39, 2.39 | 0.023, 0.880, −1.33, 2.33 |
| 26 | residue | 0.017, 0.931, −1.27, 2.27 |
| 27 | 0.066, 0.934, −2.44, 3.44 | 0.018, 0.911, −0.98, 1.98 |
| 28 | 0.056, 0.879, −1.96, 2.96 | 0.019, 0.929, −1.37, 2.37 |
| 29 | 0.079, 0.912, −1.85, 2.85 | 0.022, 0.856, −1.16, 2.16 |
| 30 | residue | 0.018, 0.906, −1.19, 2.19 |
| 31 | 0.054, 0.943, −1.86, 2.86 | 0.017, 0.911, −1.13, 2.13 |
| 32 | 0.069, 0.889, −1.99, 2.99 | 0.019, 0.902, −1.46, 2.46 |
| 33 | 0.058, 0.918, −2.38, 3.38 | 0.024, 0.897, −1.27, 2.27 |
| 34 | 0.048, 0.957, −2.36, 3.36 | 0.014, 0.931, −0.69, 1.69 |
| 35 | 0.093, 0.895, −3.71, 4.71 | 0.020, 0.918, −0.99, 1.99 |
| 36 | 0.058, 0.875, −1.97, 2.97 | 0.016, 0.908, −0.78, 1.78 |

"Right" is the fraction of the original's action kept along the leading right direction and the weight is one minus
it; a residue is a matrix inside the range rewritten under the threshold.

Against the other copy of this original (grayarea, pair 8), measured on the same ten shards (`dac38c5d` to
`651e3b8f`), 48 matrices changed in both and no field is equal in any of them (0 of 288): two methods from one tool
on one base, one direction per matrix on the input side here against one shared direction on the output side there.

## Token and configuration side (Stage 1)

The cluster's card read "unexplained differences" on 1,033 fields, and the home judgement closes two by tool (the
`rope_parameters` blocks of the text and vision configurations, the 5.3.0 form of `rope_theta`) and reads the rest
as one cause: the copy stands on a third party's conversion of the original to the library's format, and the
original has no file to compare it with.

- The original ships `config.json`, `generation_config.json`, `params.json`, `tekken.json` and `SYSTEM_PROMPT.txt`
  and no `tokenizer.json`, `tokenizer_config.json`, `special_tokens_map.json` or `chat_template.jinja`; the tool
  reports those four as missing on the original's side and "template default absent on one side".
- The copy ships them: a `tokenizer.json` of 1,000 special tokens (ids 0 to 999, `<unk>`, `<s>`, `</s>`, `[INST]`,
  `[THINK]`, `[/THINK]`, the `<SPECIAL_n>` placeholders), a tokenizer configuration with `bos_token` `<s>` (1),
  `eos_token` `</s>` (2), `pad_token` `<pad>` (11) and `unk_token` `<unk>` (0), a vocabulary of 131,072, and a
  `chat_template.jinja` whose header reads "Copyright 2025-present the Unsloth team". The template equals
  unsloth/Magistral-Small-2509's template at its 2025-09-29 revision (`dcfa8f67`) line for line with carriage-return
  line endings added (104 of them, 4,794 bytes against 4,690), and the copy's `SYSTEM_PROMPT.txt` (554 bytes) is
  the original's file as it stood before its 2025-12-02 revision; the current one (566 bytes) adds a heading and
  drops the sentence "Use the same language as the input". Pair 8 carries the same 554-byte file.
- The configuration carries the conversion's signature of finding 15: `unsloth_fixed` true, the three token ids
  written at the top level and in the text configuration (`bos_token_id` 1, `eos_token_id` 2, `pad_token_id` 11),
  `tie_word_embeddings` true at the top and false in the text configuration, `dtype` repeated in the text and
  vision blocks, and `transformers_version` 5.3.0 against the original's 4.56.1, which is also the form that moves
  `rope_theta` into a `rope_parameters` block.
- No field names a token the original lacks or an id the original's `tekken.json` assigns differently; the special
  token ids and the vocabulary size are the ones the original's own format carries. The fixed conversation could
  not be rendered on the original's side; rendered with the two copies' templates it is the same string.

## For the recipe library

Consistent with the card on the weights, and the first arbitrary-rank copy on a Mistral base: the entry's component
list gains the down projections for a second maker and its weight band reaches 4.71. On the token side the census
needs a rule for originals that ship no library tokenizer: compare the copy's tokenizer files with the conversion
they were taken from and name it, which here closes every one of the 1,033 fields. The saved direction vectors are
not committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/nautilus18/measurements/pair-7/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
