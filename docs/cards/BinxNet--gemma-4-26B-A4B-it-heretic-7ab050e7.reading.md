# Reading of the Stage 1 and Stage 2 result: BinxNet/gemma-4-26B-A4B-it-heretic against google/gemma-4-26B-A4B-it (2026-11-01)

Measured on Nautilus, round 32 piece 2 (download job 4145233, compare job 4145235, 1,394 seconds, sweep 4145242).
Modified revision `0c503aff` (twelve commits on 2026-06-21 from 01:09Z to 03:47Z: the weights at 03:41Z, the
tokenizer, the processor, the README with an animation, and a `reproduce/` folder with the tool's configuration
and trial record), original pinned at `20da991a`, the revision current when the repository was created. The card
prints the Heretic 1.4.0 record: trial 183, row normalisation "full" with a rank-three correction, the attention
outputs at weight 1.44 centred on layer 21.35 (minimum 1.36, width 16.62), the down projections at 1.46 centred on
27.70 (minimum 0.57, width 17.08), a KL divergence of 0.0909 and 25 refusals in 100 against the original. The
`base_model` field names the original.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 21 flags, on the
cluster and after re-scoring at home: five first shares of 0.985 to 0.989 on the down projections of layers 11
to 15 and sixteen within-layer cosines of 0.88 to 0.95. On reading, the footprint is the card's two kernels to
the layer, one direction per matrix on the output side, and the kept fractions read the kernels at about half
their depth.

- 44 of 1,013 tensors changed: the attention outputs of layers 5 to 29 (25 matrices) and the shared dense down
  projections of layers 11 to 29 (19). The attention kernel centred on 21.35 with width 16.62 reaches 4.73 to
  37.97 of a 30-layer model, the down kernel centred on 27.70 with width 17.08 reaches 10.62 to 44.78: layers 5
  to 29 and 11 to 29 exactly. The experts, the routers, the other projections and the vision tower are unchanged;
  the largest relative change outside the changed set is exactly 0 and 969 tensors equal the original.
- One direction per matrix: first share 0.985 to 0.998, the two writers of a layer agreeing at 0.88 to 0.98
  (1.000 on layers 5 to 10, where only the attention output is edited), the directions drifting across layers at
  0.16 to 0.79 to the group reference.
- Output side on 42 of 44: the left kept fraction is below the right everywhere but on the attention outputs of
  layers 19 and 27 (left 0.64 and 0.50), the same two layers that read that way on sh0ck0r's copy of this round.
  The attention kernel is nearly flat (weight 1.36 to 1.44, so a kept fraction of -0.36 to -0.44 across the
  window); the left reads -0.25 to -0.38 from layer 17 to 29 apart from those two, and -0.01 to 0.16 on layers 5
  to 13, where the card's weight is as large as anywhere. The down kernel rises from 0.59 at layer 11 to 1.46 at
  27.70; the left reads 0.44 at 11 (kernel 0.41), 0.25 at 17 (0.10), 0.05 at 20 (-0.06), -0.12 at 23 (-0.22) and
  -0.10 to -0.13 at 27 and 28 (-0.44). About half the depth on the down projections, with the read closest at the
  shallow end. The weights along the leading direction are 0.36 to 1.38 on the attention outputs and 0.56 to 1.18
  on the down projections.
- Rows moved by 0.004 to 0.051 on the 44 matrices under the version's "full" row normalisation with a rank-three
  correction, every one of them by more than the 0.0004 a full restoration leaves (TrevorJS's copies). The
  rank-three correction may be why the kept fractions along the leading direction read short of the kernel: a
  low-rank term added after the projection changes the leading direction's share without changing the window.
- Relative changes of 0.026 to 0.046 on the attention outputs and 0.011 to 0.043 on the down projections.

| Layer | Attention output: change, E1, left kept, right kept, kernel 1-w | Down projection: change, E1, left kept, right kept, kernel 1-w | Within-layer cosine | Row norms |
| --- | --- | --- | --- | --- |
| 5 | 0.0384, 0.996, 0.01, 0.32, -0.36 | - | - | 0.0163, - |
| 8 | 0.0362, 0.998, -0.01, 0.26, -0.38 | - | - | 0.0142, - |
| 11 | 0.0373, 0.995, 0.16, 0.40, -0.39 | 0.0110, 0.985, 0.44, 0.90, 0.41 | 0.920 | 0.0223, 0.0163 |
| 14 | 0.0321, 0.998, -0.21, 0.39, -0.41 | 0.0138, 0.989, 0.35, 0.85, 0.25 | 0.955 | 0.0181, 0.0159 |
| 17 | 0.0289, 0.997, -0.31, 0.38, -0.42 | 0.0167, 0.992, 0.25, 0.84, 0.10 | 0.983 | 0.0188, 0.0119 |
| 20 | 0.0294, 0.997, -0.13, 0.44, -0.43 | 0.0208, 0.995, 0.05, 0.77, -0.06 | 0.954 | 0.0121, 0.0128 |
| 23 | 0.0270, 0.997, -0.25, 0.50, -0.43 | 0.0233, 0.996, -0.12, 0.77, -0.22 | 0.976 | 0.0093, 0.0089 |
| 26 | 0.0310, 0.997, -0.30, 0.28, -0.42 | 0.0310, 0.997, 0.33, 0.74, -0.37 | 0.957 | 0.0071, 0.0104 |
| 28 | 0.0274, 0.997, -0.37, 0.26, -0.41 | 0.0356, 0.998, -0.13, 0.69, -0.44 | 0.968 | 0.0070, 0.0201 |
| 29 | 0.0268, 0.996, -0.27, 0.27, -0.40 | 0.0431, 0.994, 0.07, 0.80, -0.39 | 0.957 | 0.0061, 0.0508 |

The kernel column is one minus the card's weight at that layer; the full table (44 rows) is in the report.

The fingerprint shares no measured field with the ten earlier reports on this original or with sh0ck0r's copy
of this round, which was made with the previous version of the same tool a month earlier on the same base; the
two share their first two shards (`a868d472`, `a3de0db5`), the library's sharding of what neither edit touches.
The two copies' windows differ (5 to 29 against 9 to 29 on the attention outputs, 11 to 29 against 13 to 29 on
the down projections). On the attention outputs of layers 17 to 29 the two copies' kept fractions agree within
0.1, and at layer 20 to four digits (-0.1303 on the left in both, 0.4398 against 0.4397 on the right): two
searches on the same base and the same prompts found the same direction and nearly the same kernel there. On the
down projections they differ by up to 0.25, where the two kernels' centres sit three layers apart.

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home: the two version strings (5.5.0.dev0 to 5.6.2) and
nothing else. The template is Google's pinned file and the fixed conversation renders identically.

## For the recipe library

The first Heretic 1.4 copy on a clean base in the census (the other, sh0ck0r's Artemis copy of round 20, sits on
a quantised parent). Its windows read to the layer and its direction count is right; its strengths read at about
half the card's depth on the down projections and from nothing to 0.9 of the depth on the attention outputs,
with rows moved 0.004 to 0.051 under a "full" row-normalisation claim. A Heretic 1.4 entry should expect the
rank-three correction to shorten the leading-direction read and should not read "full" as a restoration. The
pull copy keeps the direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus32/measurements/pair-2/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
