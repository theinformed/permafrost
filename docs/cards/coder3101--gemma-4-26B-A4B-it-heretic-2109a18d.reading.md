# Reading of the Stage 1 and Stage 2 result: coder3101/gemma-4-26B-A4B-it-heretic against google/gemma-4-26B-A4B-it (2026-10-31)

Measured on Blueback, round 12 piece 6 (push card 5366, round card 5367, download job 3399779, compare jobs 3399780 to
3399785, all exit 0, sweep 3399786; pulled home by card 5448). Modified revision `e6d09d5c` (2026-04-14, the maker's
template commit; the repository was created on 2026-04-02 at 20:55Z and the weights were uploaded four minutes
later), original pinned at `47b6801b` (2026-04-02, the release commit). The maker's card names the method and its
parameters: Heretic 1.2.0 with Arbitrary-Rank Ablation and row-norm preservation, start layer 10, end layer 30,
preserve weight 0.5480, steer weight 0.0009, overcorrect weight 0.5868, neighbour count 14; it reports 11 refusals in
100 against 100 for the original and a KL divergence of 0.0499. The card lists no targeted component.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 20 flags, on the
cluster and after re-scoring at home. All 20 flags are energy shares. On reading, the footprint matches the card and
the flags measure the arbitrary-rank method on its first mixture-of-experts base.

- 20 of 1,013 tensors changed, all attention outputs, in layers 10 to 29 of 30: every layer of the card's range and
  the one component the method edits. Nothing else moved; the largest relative change outside the changed set is
  exactly 0. The 30 packed expert down tensors, the 30 packed gate-up tensors, the shared down projections, the
  routers, the reading-side projections and the vision tower are unchanged: on the mixture the method edits the
  attention output and nothing of the feed-forward side, as on the dense bases.
- The arbitrary-rank profile, spread wider than on the dense copies: first-value energy share 0.659 to 0.959 (median
  0.909), first eight values 0.918 to 0.972, on relative changes of 0.0095 to 0.0377. The leftover beyond the first
  direction is 0.0029 to 0.020 of the weight norm. Layer 10 is the most spread edit measured on the method: first
  share 0.659, first eight 0.918, the tail directions on the input side keeping a median 0.71.
- The leading direction sits on the input side. Along it the copy keeps −0.49 to 0.24 of the original's action on
  the right (weights 0.76 to 1.49, median 1.20) and 0.57 to 0.98 on the left; the left fraction is above the right on
  all 20. Four layers read a weight under 1 (layer 18 at 0.89, 23 at 0.81, 24 at 0.92, 25 at 0.76), a projection of
  part of the direction, where every dense copy of the method read 1.1 or more except layer 50 of the maker's 31B
  copy.
- The leading directions differ by layer (cosine 0.11 to 0.48 with their median, 0.28 in the middle).
- Row norms moved by 0.0061 to 0.0080 relative (median 0.0074). The card claims row-norm preservation; the rows moved
  by about seven tenths of a percent, as on the maker's E4B copy (0.0071 to 0.0078) and 31B copy (0.0059 to 0.0077).

| Layer | Relative change | E1 | E8 | Left, direction 1 | Right, direction 1 | Row norms |
| --- | --- | --- | --- | --- | --- | --- |
| 10 | 0.034 | 0.659 | 0.918 | 0.76 | −0.27 | 0.0077 |
| 11 | 0.011 | 0.921 | 0.940 | 0.94 | −0.20 | 0.0073 |
| 12 | 0.017 | 0.936 | 0.962 | 0.88 | −0.25 | 0.0075 |
| 13 | 0.021 | 0.886 | 0.934 | 0.90 | −0.19 | 0.0075 |
| 14 | 0.019 | 0.916 | 0.939 | 0.86 | −0.22 | 0.0072 |
| 15 | 0.019 | 0.923 | 0.952 | 0.92 | −0.26 | 0.0079 |
| 16 | 0.022 | 0.905 | 0.942 | 0.76 | −0.19 | 0.0069 |
| 17 | 0.021 | 0.889 | 0.931 | 0.98 | −0.43 | 0.0073 |
| 18 | 0.023 | 0.898 | 0.954 | 0.89 | 0.11 | 0.0075 |
| 19 | 0.029 | 0.809 | 0.936 | 0.94 | −0.18 | 0.0064 |
| 20 | 0.038 | 0.902 | 0.955 | 0.94 | −0.49 | 0.0073 |
| 21 | 0.022 | 0.894 | 0.957 | 0.83 | −0.19 | 0.0061 |
| 22 | 0.028 | 0.837 | 0.957 | 0.56 | −0.27 | 0.0074 |
| 23 | 0.009 | 0.905 | 0.925 | 0.98 | 0.19 | 0.0069 |
| 24 | 0.018 | 0.947 | 0.971 | 0.77 | 0.08 | 0.0076 |
| 25 | 0.015 | 0.959 | 0.972 | 0.79 | 0.24 | 0.0078 |
| 26 | 0.016 | 0.922 | 0.951 | 0.83 | −0.35 | 0.0072 |
| 27 | 0.016 | 0.932 | 0.951 | 0.93 | −0.20 | 0.0070 |
| 28 | 0.013 | 0.913 | 0.941 | 0.97 | −0.37 | 0.0080 |
| 29 | 0.012 | 0.927 | 0.946 | 0.95 | −0.18 | 0.0075 |

Against the maker's two other copies the method is the same with the smallest weights: 1.32 to 2.02 on E4B (round
8), 0.51 to 10.18 on 31B (piece 2), 0.76 to 1.49 here. Against the two other copies of this base (TrevorJS in rounds 2
and 3, huihui-ai in piece 5), which stand on the same original weight file (shards `11276849` and `aab47033`), no
changed matrix has an equal measurement in any field.

## Token and configuration side (Stage 1)

The cluster's card read "unexplained differences" in one field and the home judgement keeps it, so the committed card
reads "unexplained differences"; the reading closes it by hand.

- `template.default`: the copy's template (16,433 bytes, no blank line) is Google's template of 2026-04-10, 02:02Z
  (`1db3cff1`, carried in `7d4c97e5`; 16,448 bytes, the same file Google published for the 31B model that day) with
  its 15 blank lines removed and no other change; the fixed conversation renders identically. It is byte for byte the
  template in the maker's 31B copy (piece 2), committed three minutes earlier on 2026-04-14. The repository was
  created ten hours after the release commit, so the pin took the release template. The later-revision rule compares
  byte for byte after line endings and trailing whitespace, and blank lines defeat it.
- The configurations are equal in every field (`moe_intermediate_size` 704 on both sides), both saved under
  transformers 5.5.0.dev0, and the tokenizer, special tokens and generation settings are unchanged.

## For the recipe library

Consistent with the stated change on the weight side and on the token side once the template is read. The sixth
measured arbitrary-rank copy and the first on a mixture, where it reaches no expert; the candidate entry's first-share
line should start at 0.65 rather than the 0.90 round 3 wrote, and its weight band should start below 1. The saved
direction vectors are not committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/blueback12/measurements/pair-6/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
