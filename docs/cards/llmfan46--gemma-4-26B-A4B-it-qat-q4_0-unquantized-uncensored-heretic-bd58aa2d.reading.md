# Reading of the Stage 1 and Stage 2 result: llmfan46/gemma-4-26B-A4B-it-qat-q4_0-unquantized-uncensored-heretic against google/gemma-4-26B-A4B-it-qat-q4_0-unquantized (2026-11-02)

Measured on Nautilus, round 34 piece 1 (download job 4163806, compare job 4163807, sweep 4163815; the pull of
11-01 21:23Z carries the measurements and the sweep record and no job log). Modified revision `33d5581f` (18
commits inside twenty-one minutes on 2026-06-11: a model, tokenizer and README upload at 21:29Z, every file deleted
between 21:31Z and 21:33Z, a second upload of "7 files" and the two shards by 21:41Z, three README edits to 21:50Z),
original pinned at `641f1844` (06-05), the QAT-unquantized checkpoint of the 26B-A4B mixture. The card (36,919
bytes) is Heretic v1.2.0's page for an arbitrary-rank ablation: start layer 11, end layer 23, the attention
output alone as the targeted component, preserve 0.2099, steer 0.0007, overcorrect 0.6386, 15 neighbours, KL
divergence 0.0618, refusals 11 of 100 against 100 of 100, MMLU 80.66 to 80.39. The field `base_model` names the
QAT checkpoint. The maker's sixth Gemma 4 copy in the census and the first on a QAT checkpoint; the maker's
instruct 26B-A4B copy was measured in round 16.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 12 flags, on the
cluster and after re-scoring at home: the first-value shares of all twelve matrices (0.379 to 0.939), below the
rule's 0.99 line because the edit carries several directions per matrix. On reading, the copy is the card's
arbitrary-rank edit on the attention outputs of twelve layers, input side, at weights to 1.70, and nothing else.

- 12 of 1,013 tensors changed: the attention outputs of layers 11 to 22 of 30, the card's start 11 and end 23 on
  the one component it names. No down projection, no expert, no router, no norm and no tower tensor moved; the
  largest relative change outside the changed set is exactly 0, which places the copy on the QAT checkpoint
  (finding 48).
- Input side on 12 of 12: the right kept fraction is below the left on every matrix, -0.70 to -0.10 against 0.61
  to 0.97. Read as a weight along the leading input direction (one minus the right fraction) the layers run 1.10
  to 1.70, the largest on layer 20 (1.70, change 0.044) with layer 19 the largest change (0.050) at the lowest
  first share (0.38).
- Several directions per matrix: first shares 0.38 to 0.94 and eight-direction shares 0.89 to 0.97, the
  arbitrary-rank branch's signature (finding 22). Across layers the leading directions sit at 0.23 to 0.51 to
  the group reference.
- Rows moved 0.0013 to 0.0186, Heretic's band; the card claims no restoration.
- Against the maker's instruct 26B-A4B edit (round 16, nautilus16 pair 2) the saved leading left vectors stand at
  0.85 to 0.98 on the twelve shared matrices (median 0.935): the same directions on the two Google checkpoints.
  Against mewse's QAT edit 0.47 to 0.99 (median 0.79); against eadx's duplicate of huihui-ai's QAT edit 0.03 to
  0.22; against xdavxd's 0.08 to 0.41.

| Layer | Attention output: change, E1, E8, left kept, right kept | Weight read (1 − right) | Rows |
| --- | --- | --- | --- |
| 11 | 0.0122, 0.939, 0.966, 0.91, -0.15 | 1.15 | 0.0013 |
| 12 | 0.0264, 0.706, 0.943, 0.87, -0.43 | 1.43 | 0.0028 |
| 13 | 0.0228, 0.937, 0.965, 0.88, -0.31 | 1.31 | 0.0025 |
| 14 | 0.0212, 0.895, 0.952, 0.84, -0.31 | 1.31 | 0.0023 |
| 15 | 0.0216, 0.921, 0.952, 0.90, -0.38 | 1.38 | 0.0023 |
| 16 | 0.0385, 0.530, 0.924, 0.69, -0.32 | 1.32 | 0.0186 |
| 17 | 0.0248, 0.827, 0.935, 0.97, -0.44 | 1.44 | 0.0039 |
| 18 | 0.0273, 0.827, 0.960, 0.84, -0.10 | 1.10 | 0.0043 |
| 19 | 0.0499, 0.379, 0.892, 0.82, -0.29 | 1.29 | 0.0068 |
| 20 | 0.0442, 0.859, 0.964, 0.93, -0.70 | 1.70 | 0.0151 |
| 21 | 0.0292, 0.665, 0.955, 0.74, -0.32 | 1.32 | 0.0025 |
| 22 | 0.0320, 0.743, 0.963, 0.61, -0.38 | 1.38 | 0.0027 |

The copy's two shards are `f0b14b75` (its own) and `c2c6ab9a`, which equals mewse's second shard: layers 23 to 29
and the towers in the library's two-shard layout for this checkpoint, untouched by either edit (finding 71). No
measured file is equal.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, two fields beside the version strings (5.6.2 to 5.10.2):
the template and the tokenizer file. The template is a 23,077-byte file (sha `24d32be0`, 437 lines against the
pin's 354) that matches no revision of Google's QAT repository (16,934 to 18,683 bytes) or of the instruct
repository (12,045 to 18,683 bytes); it introduces `format_type_argument`, `thinking_gate`, `preserve_thinking`,
`continues_into_next`, `image_url` and `input_audio`, and the fixed conversations render identically to the pin's.
The tokenizer file is 32,169,780 bytes (sha `a2619fe1`) against the original's 32,169,626 (`cc8d3a0c`) and no
field differs when parsed. Each of the maker's six Gemma 4 copies carries a template of its own size (21,488,
17,344, 18,841, 17,229, 16,804 and now 23,077 bytes), the habit finding 19 records.

## For the recipe library

An arbitrary-rank entry (finding 22) would describe the copy: a declared window on one component, several
directions per matrix, input side, no kept-fraction band. The per-layer entry counts the twelve first shares as
violations and reads nothing wrong. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus34/measurements/pair-1/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
