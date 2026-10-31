# Reading of the Stage 1 and Stage 2 result: llmfan46/gemma-4-26B-A4B-it-uncensored-heretic against google/gemma-4-26B-A4B-it (2026-10-31)

Measured on Nautilus, round 16 piece 2 (push card 5433, round card 5434, download job 4120061, compare job 4120063 on
the background queue, sweep 4120069; pulled home by card 5467). Modified revision `1a974f17` (2026-05-05, "Upload
chat_template.jinja"; the repository was created on 2026-04-07 at 00:57Z and the template was replaced on 04-14, 05-04
and 05-05), original pinned at `47b6801b` (2026-04-02, the release commit; shards `11276849` and `aab47033`, the same
weight file as every 26B-A4B pair so far). The maker's card names the method and its parameters: Heretic 1.2.0 with
Arbitrary-Rank Ablation, start layer 1, end layer 30, preserve weight 0.4621, steer weight 0.0006, overcorrect weight
0.7212, neighbour count 13, the attention output as the targeted component; it reports 11 refusals in 100 against 100
for the original, a KL divergence of 0.0468, PIQA 91.73 against 92.06 and MMLU 82.48 for the original.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 27 flags, on the
cluster and after re-scoring at home. All 27 flags are first energy shares. On reading, the footprint matches the
card and the flags measure the arbitrary-rank method, the maker's fifth copy and its first on a mixture.

- 27 of 1,013 tensors changed, all attention outputs, in layers 2 to 4 and 6 to 29. The attention outputs of layers 1
  and 5, inside the card's range, were rewritten and barely moved (relative change 0.000235 and 0.000127, under the
  0.001 threshold, row norms within 0.00005), and layer 0's reads exactly 0: the search left two in-range layers at
  weight near zero, as the maker's E4B copies left 17 and 13. The largest relative change outside the changed set is
  layer 1's 0.000235; outside the recipe's set it is 0.
- No expert touched: the 30 packed expert down tensors, the 30 packed gate-up tensors, the 30 routers, the shared
  down projections, the reading-side projections, the normalisations and the vision tower are unchanged, as in the
  two other arbitrary-rank and shared-projection copies of this base (round 12).
- The arbitrary-rank profile: first-value share 0.836 to 0.963 (median 0.927), first eight values 0.937 to 0.982, the
  first singular value 3.0 to 15.7 times the second, on relative changes of 0.010 to 0.038. The leftover beyond the
  first direction is 0.002 to 0.013 of the weight norm; in six layers (2, 3, 8, 9, 10 and 11) the first share is under 0.88, the
  most spread edits of the maker's method after coder3101's layer 10 on this base (0.659).
- Input side: along the leading direction the copy keeps −0.52 to 0.58 of the original's action on the right (weights
  0.42 to 1.52, median 1.29) and 0.49 to 0.98 on the left; the left fraction is above the right on all 27. Five layers
  read a weight under 1 (layer 3 at 0.42, 4 at 0.72, 18 at 0.99, 23 at 0.80, 25 at 0.78), a projection of part of the
  direction; 0.42 is the smallest weight read on the method (coder3101's layer 50 of the 31B read 0.51).
- The leading directions differ by layer (cross-layer cosine 0.11 to 0.42, median 0.27).
- Row norms moved by 0.0006 to 0.0079 relative (median 0.0022). The card makes no preservation claim.

| Layer | Relative change | E1 | E8 | Left, direction 1 | Right, direction 1 | Row norms | Cross-layer cosine | Within-layer cosine |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 0.032 | 0.836 | 0.979 | 0.49 | -0.24 | 0.0049 | 0.17 | 1.000 |
| 3 | 0.013 | 0.872 | 0.973 | 0.86 | 0.58 | 0.0023 | 0.21 | 1.000 |
| 4 | 0.017 | 0.945 | 0.982 | 0.77 | 0.28 | 0.0079 | 0.27 | 1.000 |
| 6 | 0.027 | 0.942 | 0.979 | 0.71 | -0.42 | 0.0023 | 0.32 | 1.000 |
| 7 | 0.026 | 0.940 | 0.980 | 0.51 | -0.37 | 0.0026 | 0.36 | 1.000 |
| 8 | 0.038 | 0.877 | 0.966 | 0.56 | -0.47 | 0.0034 | 0.38 | 1.000 |
| 9 | 0.034 | 0.865 | 0.953 | 0.82 | -0.37 | 0.0076 | 0.40 | 1.000 |
| 10 | 0.027 | 0.877 | 0.966 | 0.75 | -0.33 | 0.0022 | 0.42 | 1.000 |
| 11 | 0.016 | 0.879 | 0.937 | 0.97 | -0.24 | 0.0017 | 0.25 | 1.000 |
| 12 | 0.021 | 0.936 | 0.965 | 0.86 | -0.36 | 0.0017 | 0.31 | 1.000 |
| 13 | 0.021 | 0.905 | 0.948 | 0.89 | -0.30 | 0.0018 | 0.24 | 1.000 |
| 14 | 0.022 | 0.922 | 0.952 | 0.84 | -0.36 | 0.0021 | 0.32 | 1.000 |
| 15 | 0.022 | 0.927 | 0.958 | 0.92 | -0.26 | 0.0027 | 0.29 | 1.000 |
| 16 | 0.023 | 0.941 | 0.963 | 0.75 | -0.30 | 0.0072 | 0.39 | 1.000 |
| 17 | 0.022 | 0.912 | 0.947 | 0.98 | -0.49 | 0.0022 | 0.19 | 1.000 |
| 18 | 0.024 | 0.947 | 0.968 | 0.87 | 0.01 | 0.0041 | 0.26 | 1.000 |
| 19 | 0.026 | 0.903 | 0.956 | 0.88 | -0.05 | 0.0039 | 0.41 | 1.000 |
| 20 | 0.031 | 0.955 | 0.976 | 0.94 | -0.34 | 0.0051 | 0.19 | 1.000 |
| 21 | 0.022 | 0.929 | 0.965 | 0.80 | -0.19 | 0.0021 | 0.28 | 1.000 |
| 22 | 0.029 | 0.884 | 0.961 | 0.53 | -0.37 | 0.0022 | 0.28 | 1.000 |
| 23 | 0.010 | 0.933 | 0.954 | 0.98 | 0.20 | 0.0009 | 0.15 | 1.000 |
| 24 | 0.025 | 0.927 | 0.956 | 0.69 | -0.10 | 0.0030 | 0.28 | 1.000 |
| 25 | 0.016 | 0.958 | 0.973 | 0.80 | 0.22 | 0.0016 | 0.13 | 1.000 |
| 26 | 0.015 | 0.944 | 0.964 | 0.84 | -0.29 | 0.0006 | 0.16 | 1.000 |
| 27 | 0.017 | 0.954 | 0.971 | 0.92 | -0.29 | 0.0012 | 0.19 | 1.000 |
| 28 | 0.015 | 0.918 | 0.944 | 0.96 | -0.52 | 0.0008 | 0.11 | 1.000 |
| 29 | 0.010 | 0.963 | 0.969 | 0.93 | -0.02 | 0.0019 | 0.13 | 1.000 |

Against the four other measured copies of this base (TrevorJS in rounds 2 and 3, huihui-ai and coder3101 in round
12, prithivMLmods in piece 4), all on the same original weight file, no changed matrix has an equal measurement in any
field. Against the maker's four other copies the method reads the same: attention outputs only, input side, no norm
restoration, searched per-layer weights; the weights here (0.42 to 1.52) sit at the bottom of the maker's range (1.27
to 1.79 on E4B, 1.86 to 4.41 on E2B, 1.37 to 3.36 on 31B), as coder3101's did on this base (0.76 to 1.49).

## Token and configuration side (Stage 1)

The cluster's card read "unexplained differences" in one field and the home judgement keeps it, so the committed card
reads "unexplained differences"; the reading closes it by hand.

- `config.transformers_version` and `generation.transformers_version`: 5.5.0.dev0 on the original, 5.5.0 on the copy.
  Re-save effects.
- `template.default`: the copy's `chat_template.jinja` (17,344 bytes) matches none of Google's 13 revisions. It is
  Google's template of 2026-04-28 (`4c55b528`, carried in `462a98a1`; 16,934 bytes) with the maker's edits: a 14-line
  `format_type_argument` macro prepended, every `is sequence` test changed to `is iterable` (five places), and the
  four type comparisons (`| upper == 'STRING'`, `'ARRAY'`, `'OBJECT'`, and the response declaration's) rewritten to
  accept a type given as a list. Nothing in the conversation path changes, and the fixed conversation renders
  identically. The same macro and the same substitutions are in the maker's E2B template of round 8 (finding 19),
  which differs from this one in the quoting of two lines and in the empty thought block it adds to every model turn;
  this copy does not add the block. A real change by the maker to the tool-declaration path of the template, outside
  the card; the later-revision rule cannot close it because no Google revision equals it.

## For the recipe library

Consistent with the stated change on the weight side, and on the token side once the template is read as the
maker's patched Google template. The eighth measured arbitrary-rank copy and the second on a mixture, where it
reaches no expert; the candidate entry's weight band should start at 0.4. The saved direction vectors are not
committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/nautilus16/measurements/pair-2/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
