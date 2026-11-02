# Reading of the Stage 1 and Stage 2 result: tvall43/gemma-4-E2B-it-heretic-v0 against google/gemma-4-E2B-it (2026-11-02)

Measured on Nautilus, round 40 piece 8 (download job 4169647, compare job 4169655, sweep 4169656; the pull carries
the measurements and the sweep record and no job log). Modified revision `39472f85` (created 2026-04-02 18:52Z,
the card revised at 18:57Z, thirty-four minutes before the maker's v1 at 19:26Z), original pinned at `4742fe84`,
the release revision of eight hours earlier. The card is Heretic 1.2.0's table with the maker's note over it
("p-e-w beat me to it with ara, with a better result. my normal recipie of mpoa+soma, attn.o only. didnt go as
well as qwen3.5 liked to"): a direction index of 17.07, `attn.o_proj` as the one target with four kernels whose
maxima are 1.28, 1.45, 1.41 and 1.34 at position 20.70 and whose minima are 0.47, 1.31, 0.91 and 0.18 at a
distance of 9.37, a KL divergence of 0.2453 and 9 refusals in 100 against 98 in 100. The copy drops the
`.linear.` segment from 16 names the original carries, mapped before the comparison, and drops the vision
encoder's input and output range scalars on the attention outputs of its sixteen layers (64 `original_only`
names, listed apart as `dropped_statistics`), where the maker's v1 of the same evening dropped 128 (round 39).

## Weights (Stage 2)

The tool's assessment was a clean match of `single-projection-selected`, 0 flags, on the cluster and after
re-scoring at home. On reading, the copy is one direction for the whole window, projected from the attention
outputs of layers 12 to 30 on the output side at a weight that rises to 4.84 and falls again, the kernel's
shape.

- 19 of 1,947 tensors changed: the attention outputs of layers 12 to 30, the card's kernel position 20.70 less
  and plus its distance 9.37 (11.3 to 30.1) to the layer. No down projection moved; the largest relative change
  outside the changed set is exactly 0 on all 1,928 other tensors.
- Rank one on every matrix (first shares 0.9989 to 0.9998) and one direction: the nineteen directions stand at
  1.000 to each other, the card's single direction index of 17.07.
- Output side on all 19: one minus the left kept fraction is 2.05 at layer 12, rising by about 0.33 a layer to
  4.84 at layer 21 and falling to 1.85 at layer 30, a kernel centred where the card's is and three times its
  printed maximum; the right side keeps -0.85 to 0.63 (finding 46's scatter). Rows moved 0.018 to 0.422 (0.422 at
  layer 23), unrestored, under a card naming magnitude preservation. Relative changes 0.048 to 0.120.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Rows |
| --- | --- | --- | --- |
| 12 | 0.0521, 0.999, -1.05, 0.42 | 2.05 | 0.0176 |
| 14 | 0.0716, 0.999, -1.71, -0.54 | 2.71 | 0.0345 |
| 16 | 0.0931, 1.000, -2.38, -0.36 | 3.38 | 0.0728 |
| 18 | 0.0986, 1.000, -3.04, -0.31 | 4.04 | 0.1438 |
| 20 | 0.1173, 1.000, -3.71, -0.85 | 4.71 | 0.2887 |
| 21 | 0.1199, 1.000, -3.84, -0.39 | 4.84 | 0.2871 |
| 23 | 0.0971, 1.000, -3.17, -0.39 | 4.17 | 0.4222 |
| 25 | 0.0870, 1.000, -2.51, -0.23 | 3.51 | 0.1177 |
| 27 | 0.0682, 0.999, -1.85, -0.00 | 2.85 | 0.0358 |
| 30 | 0.0480, 0.999, -0.85, 0.63 | 1.85 | 0.0214 |

The full table (19 rows) is in the report.

Directions. Against twenty-two saved vectors of measurements of the E2B, the direction stands at 0.949 and 0.948
to huihui-ai's E2B edit on all 19 shared names (minimum 0.938) and the same to its two re-uploads and Dzluck's
copy, at 0.941 to DuoNeural's E2B single direction (16, finding 96), and at 0.13 or less to everything else: 0.084
to TrevorJS's, 0.10 to MoonRide's arbitrary-rank searches, 0.053 to anlord's, and 0.038 to the maker's own v1 on
the 10 names they share. The two exports of one evening carry different directions: v0 one direction across the
window at the huihui-ai family's 0.95, v1 one per layer at 0.98 to TrevorJS's and 0.99 to anlord's (round 39). By
byte range the layer 21 attention output is 0.1199 from Google's on v0, 0.0839 on v1 and 0.1429 between the two,
and 0.0977 from huihui-ai's. The one shard (`6c57b4c9`) matches no measured file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster on one field, "consistent with re-save noted" at home: the home
judgement closed `text_config.moe_intermediate_size` by the default rule under transformers 5.22.1 and nothing
else differs, no version string among them; the tokenizer, the token ids, the generation settings and the
11,926-byte template are the release revision's.

## For the recipe library

The single-projection entry with selection reads the copy exactly; a weight line would print the kernel the
card's four maxima do not (1.85 to 4.84). The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus40/measurements/pair-8/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
