# Reading of the Stage 1 and Stage 2 result: tvall43/gemma-4-26B-A4B-it-heretic against google/gemma-4-26B-A4B-it (2026-11-02)

Measured on Wheat, round 39 piece 1 (download job 387181, compare job 387182, sweep 387190; the pull carries the
measurements and the sweep record and no job log). Modified revision `5ee9a57f` (created 2026-04-02 21:41Z, last
commit 23:08Z the same evening, two hours after the maker's E2B copy of pair 4), original pinned at `47b6801b`. The
card is Heretic 1.2.0's table with a line from the maker over it ("lets pretend that the last try didnt happen.
mpoa+soma, only attn.o. ara seems superior"): a direction index per layer, `attn.o_proj` as the one target with four
kernels whose maxima are 0.98, 1.07, 0.95 and 1.34 at position 24.12 and whose minima are 0.97, 0.75, 0.74 and 0.11
at a distance of 8.63, a KL divergence of 0.1575, and 12 refusals in 100 against 100 in 100. The copy drops the
`.linear.` segment from 27 names the original carries, mapped before the comparison.

## Weights (Stage 2)

The tool's assessment was a clean match of `directional-per-layer-selected`, 0 flags, on the cluster and after
re-scoring at home. On reading, the copy is one direction per layer projected from the attention outputs of the
last fourteen layers at a flat weight of about 4.1 on the output side, nothing else touched.

- 14 of 1,013 tensors changed: the attention outputs of layers 16 to 29, the stack's last fourteen. No dense down
  projection and no expert moved; the largest relative change outside the changed set is exactly 0 on all 999
  other tensors.
- Rank one on every matrix: first shares 0.9995 to 1.000. One direction per layer, as the card's direction index
  says: the directions of the fourteen layers stand at 0.43 to 0.87 to their mean.
- Output side on all 14: the left kept fraction is minus 3.09 to minus 3.18, a weight of 4.09 to 4.18 on every
  layer, within 0.09 of each other across the window; the right side keeps minus 1.24 to 0.32. The card's four
  kernels peak at layer 24.12 and fall to their minima 8.63 layers away, and the measured weights have no peak.
  Rows moved 0.052 to 0.413, unrestored, under no claim (the maker's "ara seems superior" compares a run the
  repository does not carry). Relative changes 0.074 to 0.094.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Rows |
| --- | --- | --- | --- | --- |
| 16 | 0.0918, 1.000, -3.09, -0.07 | 4.09 | 0.204 |
| 17 | 0.0821, 1.000, -3.08, -0.67 | 4.08 | 0.292 |
| 18 | 0.0813, 1.000, -3.10, -0.62 | 4.10 | 0.117 |
| 19 | 0.0941, 1.000, -3.13, 0.32 | 4.13 | 0.229 |
| 20 | 0.0848, 1.000, -3.14, -0.41 | 4.14 | 0.128 |
| 21 | 0.0899, 1.000, -3.16, -0.92 | 4.16 | 0.149 |
| 22 | 0.0836, 1.000, -3.14, -0.48 | 4.14 | 0.105 |
| 23 | 0.0767, 1.000, -3.14, -0.44 | 4.14 | 0.076 |
| 24 | 0.0904, 1.000, -3.13, -1.24 | 4.13 | 0.052 |
| 25 | 0.0740, 1.000, -3.14, -0.96 | 4.14 | 0.064 |
| 26 | 0.0909, 1.000, -3.18, -1.06 | 4.18 | 0.057 |
| 27 | 0.0911, 1.000, -3.17, 0.18 | 4.17 | 0.062 |
| 28 | 0.0802, 1.000, -3.16, -1.10 | 4.16 | 0.071 |
| 29 | 0.0788, 1.000, -3.14, -0.99 | 4.14 | 0.413 |

Directions. Against twenty-four saved vectors of measurements of the 26B-A4B, the directions stand at 0.98 on both
sides to SevenOfNine's, BinxNet's and sh0ck0r's kernel exports on all 14 shared names (left minimum 0.917), at 0.97
and 0.96 to TrevorJS's edit, to DuoNeural's copy of it and to its four re-uploads, at 0.94 to xdavxd's run on the
QAT checkpoint, at 0.58 to Mitchins's QAT kernel pass, at 0.45 to WWTCyberLab's and at 0.33 to llmfan46's QAT
edit (7 shared): the 26B-A4B's one-direction family of findings 24 and 74, joined by a copy that used a different
weight and a shorter window. The two shards (`c6eef31d`, `0ac3ecbd`) match no measured file.

## Token and configuration side (Stage 1)

"Consistent" on the cluster and at home, the one card of the round that read so on the cluster: the configuration,
the generation configuration, the tokenizer and the template are the pin's.

## For the recipe library

The per-layer entry with selection reads the copy exactly; a weight line would print the flat 4.1 beside the
card's four kernels that the weights do not show. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat39/measurements/pair-1/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
