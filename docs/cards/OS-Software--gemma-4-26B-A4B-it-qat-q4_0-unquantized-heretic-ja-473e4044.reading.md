# Reading of the Stage 1 and Stage 2 result: OS-Software/gemma-4-26B-A4B-it-qat-q4_0-unquantized-heretic-ja against google/gemma-4-26B-A4B-it-qat-q4_0-unquantized (2026-11-02)

Measured on Wheat, round 37 piece 2 (download job 387161, compare job 387163, sweep 387170; the pull carries the
measurements and the sweep record and no job log). Modified revision `184e64bb` (six commits on 2026-08-02 between
04:51Z and 04:55Z: the weights, the tokenizer, the processor and the README twice), original pinned at `f1e06dc5`
(04-29), the QAT-unquantized 26B-A4B checkpoint, the revision the maker's English `-v2` export of round 32 also
stands on (finding 75: the two Google revisions of this checkpoint carry one weight file). The card (32,718 bytes)
says Heretic v1.4.0 with the arbitrary-rank method "using a LoRA adapter and row-norm preservation":
`start_layer_index` 7, `end_layer_index` 23, `preserve_good_behavior_weight` 1.0000, `steer_bad_behavior_weight`
0.0309, `overcorrect_relative_weight` 0.9557, `neighbor_count` 1, keywords 1 of 100 against 100 of 100, KL
divergence 0.0362, measured on the maker's Japanese prompt sets. The `base_model` field names
google/gemma-4-26B-A4B-it and the first sentence the QAT checkpoint (finding 48); the pinner followed the name and
recorded the QAT checkpoint as `card_parent`. The maker's second copy on this checkpoint after the English `-v2`
(round 32, finding 42), made five weeks earlier.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 64 flags (32 first
shares of 0.39 to 0.94 and 32 within-layer cosines of 0.008 to 0.13), on the cluster and after re-scoring at home.
On reading, the copy is the card's window on the attention outputs and the shared dense down projections, input
side, many directions per matrix, no expert touched.

- 32 of 1,013 tensors changed: the attention outputs and the shared down projections of layers 7 to 22, the card's
  start 7 and end 23 with the end exclusive. The 3,840 packed expert tensors, the routers and the vision tower are
  unchanged; the largest relative change outside the changed set is exactly 0 and 981 tensors equal the original,
  which places the copy on the QAT checkpoint (finding 48).
- Many directions per matrix: first shares 0.39 to 0.94, the fourth cumulative share 0.72 to 0.98 and the eighth
  0.83 to 0.99, where the maker's English export of the same checkpoint cut at exactly rank four (fourth share
  0.998 to 0.9995, finding 42).
- Input side on 32 of 32: the left kept fraction is 0.24 to 0.96 and the right -1.09 to -0.24. Read as weights, one
  minus the right kept fraction, 1.24 to 2.09 (median 1.75), the down projections 1.24 to 2.09 and the attention
  outputs 1.38 to 2.01.
- No shared direction: within a layer 0.008 to 0.13, across layers 0.15 to 0.52 to the group reference.
- Rows moved 0.0012 to 0.0081 under the card's preservation claim: inside finding 22's band (0.0057 to 0.0080) on
  five, under it on 26 and over it by 0.0001 on one.
- Relative changes 0.022 to 0.077, the three largest on the down projections of layers 19 to 21.

| Layer | Attention output: change, E1, E4, left kept, right kept | Down projection: change, E1, E4, left kept, right kept | Weight read | Within-layer cosine | Rows |
| --- | --- | --- | --- | --- | --- |
| 7 | 0.0383, 0.724, 0.90, 0.56, -0.59 | 0.0339, 0.936, 0.98, 0.76, -0.24 | 1.59/1.24 | 0.036 | 0.0053, 0.0022 |
| 10 | 0.0516, 0.454, 0.76, 0.69, -0.69 | 0.0667, 0.791, 0.93, 0.93, -1.09 | 1.69/2.09 | 0.057 | 0.0053, 0.0042 |
| 13 | 0.0436, 0.713, 0.90, 0.79, -0.88 | 0.0576, 0.588, 0.84, 0.51, -0.69 | 1.88/1.69 | 0.100 | 0.0029, 0.0050 |
| 16 | 0.0550, 0.440, 0.78, 0.66, -0.92 | 0.0686, 0.519, 0.80, 0.40, -0.85 | 1.92/1.85 | 0.044 | 0.0060, 0.0050 |
| 19 | 0.0532, 0.386, 0.72, 0.89, -0.74 | 0.0728, 0.537, 0.81, 0.45, -0.90 | 1.74/1.90 | 0.022 | 0.0042, 0.0081 |
| 22 | 0.0582, 0.448, 0.76, 0.89, -0.76 | 0.0698, 0.595, 0.86, 0.43, -0.60 | 1.76/1.60 | 0.013 | 0.0053, 0.0064 |

The full table (32 rows) is in the report.

Directions. Against the saved vectors of eighteen 26B-A4B measurements, the leading directions stand at a median of
0.71 on the left and 0.65 on the right to coder3101's instruct edit (13 shared), 0.69 and 0.65 to llmfan46's QAT and
instruct edits (12 and 16 shared), 0.62 and 0.65 to the maker's own English export of the same checkpoint (16
shared, both edits reaching layers 12 to 19) and 0.51 and 0.59 to mewse's; the kernel and projection edits stand
at 0.19 or less. The Japanese-prompt search sits nearer the English family on this checkpoint than on the 12B
(piece 1, 0.4), and nearer to coder3101's and llmfan46's searches than to the maker's own earlier one. Five of
the eleven shards (`3a554a7c`, `d5e7acd3`, `bb7350ae`, `8e6c73a5`, `4c7ea2c1`) equal the maker's English export's
first, second, ninth, tenth and eleventh: the embeddings, the layers below 7, the layers above 22 and the vision
tower, which neither search touched.

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home: the two version strings (5.6.2 to 5.13.0) are all that
differ; the 19,073-byte template differs from the pin's 18,683 in line endings alone and renders identically.

## For the recipe library

The directional-per-layer entry is the nearest and its 64 flags are the branch's many directions per matrix and its
direction per matrix; an arbitrary-rank entry would flag nothing and would record the expert pass as absent. The
direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat37/measurements/pair-2/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
