# Reading of the Stage 1 and Stage 2 result: AlekseyCalvin/Lyrical_Translator_ru2en_on_Gemma4_12b_heretic_SFT_Run2 against google/gemma-4-12B-it (2026-11-02)

Measured on Wheat, round 31 batch 3 piece 1 (download job 387097, compare job 387098, sweep 387102; the pull of
11-02 00:22Z carries the measurements and the sweep record and no job log). Modified revision `b1076060` (seventeen
commits on 2026-06-07 and 06-08, the five shards uploaded between 22:53Z and 23:00Z, a processor configuration last),
original pinned at `5926caa4` (06-04). The card is 834 bytes: "LYRICAL POET-TRANSLATOR (Russian-to-English) over
gemma-4-12B-it-heretic", a usage block and nothing else. The `base_model` field names Google's instruct model with
`base_model_relation: finetune`; the heretic the title stands on is not named.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection`, 425 flags (232 unexpected
changes, 96 first shares, 96 direction cosines, one cross-kind), on the cluster and after re-scoring at home. On
reading, the copy is a low-rank fine-tune of every projection in the language stack laid over a Heretic edit, and
the Heretic edit is igorls's.

- 328 of 677 tensors changed: the queries, keys, attention outputs, gates, up projections and down projections of
  all 48 layers, and the value projections of 40, at relative changes of 0.018 to 0.100 (median 0.035). The value
  projections of layers 5, 11, 17, 23, 29, 35, 41 and 47, the eight global-attention layers, are unchanged, as are
  every normalisation vector, every layer scalar, the token embedding, the audio and vision embedding projections
  and the vision patch embedder. The largest relative change outside the changed set is exactly 0.
- The training is of low rank but not rank one: first shares 0.13 to 0.86, fourth cumulative shares 0.34 to 0.99,
  no direction shared across layers (group cosines 0.10 to 0.13 with their medians) and kept fractions of 0.8 to
  1.1 on both sides of the queries, keys, values, gates and up projections.
- The Heretic edit reads through the training on the down projections of layers 23, 27, 28, 29, 32 and 33, which
  keep -0.18, -0.30, -0.37, -0.32, -0.20 and -0.19 of the original's action along their leading output direction,
  and on the attention outputs of layers 29 and 34, which keep 0.48 and 0.31. igorls/gemma-4-12B-it-heretic-v1
  (round 7) keeps -0.18, -0.30, -0.37, -0.38, -0.21 and -0.19 on the same six down projections and 0.46 and 0.30
  on the same two attention outputs. The saved leading directions of the two measurements agree at 1.000 on the
  down projections of layers 23, 27, 28 and 33, at 0.971 to 0.996 on 29 and 32, and at 0.991 and 0.990 on the two
  attention outputs, where the other measured 12B Heretic copies' directions on the same matrices stand at 0.08 to
  0.92 (Vampelium 0.89 to 0.92, MoonRide and prithivMLmods 0.45 to 0.51, BinxNet 0.39 to 0.45, coder3101 0.04 to
  0.57, huihui-ai 0.13 to 0.21). On the other down projections of igorls's window (22, 24 to 26, 30, 31, 34) the
  training's own direction leads and the kept fraction reads 0.94 to 0.98.
- Rows moved 0.003 to 0.45 on the up projections and 0.004 to 4.9 on the keys, where the training filled rows the
  original keeps near zero; the card claims nothing.

| Layer | Down: change, E1, left kept | igorls v1 down: left kept | Attention output: change, E1, left kept | igorls v1 attention output: left kept |
| --- | --- | --- | --- | --- |
| 22 | 0.034, 0.34, 0.68 | -0.08 | 0.027, 0.45, 0.97 | |
| 23 | 0.035, 0.33, -0.18 | -0.18 | 0.023, 0.35, 1.00 | |
| 27 | 0.037, 0.43, -0.30 | -0.30 | 0.025, 0.27, 0.99 | |
| 28 | 0.036, 0.49, -0.37 | -0.37 | 0.028, 0.13, 1.00 | |
| 29 | 0.039, 0.41, -0.32 | -0.38 | 0.023, 0.21, 0.48 | 0.46 |
| 32 | 0.036, 0.38, -0.20 | -0.21 | 0.032, 0.24, 0.93 | 0.41 |
| 33 | 0.034, 0.39, -0.19 | -0.19 | 0.031, 0.20, 0.95 | 0.34 |
| 34 | 0.036, 0.37, 0.96 | -0.16 | 0.030, 0.16, 0.31 | 0.30 |

The full table (328 rows) is in the report. The five shards are the copy's own; no shard equals any measured file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster (five fields) and at home (one). Under transformers 5.22.1 the three audio
fields and the vision patch size close by the default rule (absent in a 5.10.1 save and loading as the original's
values; finding 11), and the three `dtype` repetitions and the two version strings are re-save effects. What stays
is `text_config.max_position_embeddings`: 262,144 in the original and 131,072 in the copy. The training's save
halved the declared context length, and nothing on the card says so. The template is Google's 17,466-byte file of
the pin and the fixed conversation renders identically.

## For the recipe library

A training-over-ablation pair, the kind finding 18 and finding 61 describe, measured against the grandparent the
field names; the difference from those cases is that the parent is identified without a byte-range read, by the
saved direction vectors and the kept fractions on eight matrices (finding 66). The pair belongs on the list against
igorls/gemma-4-12B-it-heretic-v1, where the training would read alone. The direction vectors stay in the pull copy
at `/opt/ai/hpc-packages/pulls/model-audit/wheat31/measurements/pair-1/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
