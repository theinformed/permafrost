# Reading of the Stage 1 and Stage 2 result: coder3101/gemma-4-31B-it-heretic against google/gemma-4-31B-it (2026-10-31)

Measured on Blueback, round 12 piece 2 (push card 5366, round card 5367, download job 3399779, compare jobs 3399780 to
3399785, all exit 0, sweep 3399786; pulled home by card 5448). Modified revision `9a1c7f5d` (2026-04-14, the maker's
template and tokenizer-configuration commits; the repository was created on 2026-04-02 at 20:57Z and the weights were
uploaded on 2026-04-03), original pinned at `419b2efe` (2026-04-02, the release commit). The maker's card names the
method and its parameters: Heretic 1.2.0 with Arbitrary-Rank Ablation and row-norm preservation, start layer 1, end
layer 59, preserve weight 0.8438, steer weight 0.0002, overcorrect weight 1.0760, neighbour count 15; it reports 15
refusals in 100 against 99 for the original and a KL divergence of 0.0434. The card lists no targeted component.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 58 flags, on the
cluster and after re-scoring at home. All 58 flags are energy shares. On reading, the footprint matches the card, 35
of the flags measure the arbitrary-rank method and 23 measure rounding residues of matrices the search rewrote at a
weight near zero.

- 58 of 1,188 tensors changed, all attention outputs, in layers 1 to 58 of 60: every layer of the card's range and
  the one component the method edits. Nothing else moved; the largest relative change outside the changed set is
  exactly 0.
- 23 of the 58 are rounding residues, in layers 1 to 17, 19, 20, 22, 23, 25 and 35: relative change 0.0013 to 0.0018,
  first-value energy share 0.002 to 0.028, the copy keeping 0.994 to 1.000 and 0.988 to 1.007 of the original's action
  along the leading directions, row norms moved by 0.0007 to 0.0008 (layer 4 by 0.0069). The search gave those layers
  weights near zero and what survives is bfloat16 rounding of a matrix that was rewritten, as layer 41 of the maker's
  E4B copy was in round 8. Every layer below 18 is in this set.
- The other 35, in layers 18, 21, 24, 26 to 34 and 36 to 58, carry the arbitrary-rank profile: first-value share 0.915
  to 0.971, first eight values 0.931 to 0.988, on relative changes of 0.0087 to 0.169 where rounding alone would leave
  0.999 by the second value. The leftover beyond the first direction is 0.0024 to 0.031 of the weight norm.
- The leading direction sits on the input side. Along it the copy keeps −9.18 to 0.49 of the original's action on the
  right (weights 0.51 to 10.18, median 1.98) and 0.40 to 0.98 on the left; the left fraction is above the right on all
  35. Layer 48 is the largest edit measured on this method so far: weight 10.18, relative change 0.169. Layer 50 reads
  0.51, a projection of half the direction. The tail directions keep 0.56 to 1.07 (medians per matrix 0.87 to 1.00).
- The leading directions differ by layer (cosine 0.009 to 0.41 with their median, 0.10 in the middle).
- Row norms moved by 0.0059 to 0.0077 relative on the 35 (median 0.0071). The card claims row-norm preservation; the
  rows moved by about seven tenths of a percent, the same 0.007 the maker's E4B copy read in round 8 (0.0071 to
  0.0078) and the 26B copy reads in piece 6 (0.0061 to 0.0080). The restoration step leaves that residue on every copy
  by this maker, against 0.0016 to 0.037 on the llmfan46 copy of the same base, whose card claims none.

| Layer | Relative change | E1 | E8 | Left, direction 1 | Right, direction 1 | Row norms |
| --- | --- | --- | --- | --- | --- | --- |
| 18 | 0.035 | 0.923 | 0.979 | 0.54 | −1.08 | 0.0071 |
| 21 | 0.028 | 0.964 | 0.980 | 0.40 | −0.91 | 0.0071 |
| 24 | 0.025 | 0.951 | 0.960 | 0.76 | −0.61 | 0.0073 |
| 26 | 0.018 | 0.949 | 0.955 | 0.82 | −0.41 | 0.0071 |
| 27 | 0.024 | 0.941 | 0.951 | 0.73 | −0.80 | 0.0073 |
| 28 | 0.027 | 0.944 | 0.958 | 0.82 | −0.73 | 0.0073 |
| 29 | 0.015 | 0.948 | 0.957 | 0.93 | −0.64 | 0.0059 |
| 30 | 0.031 | 0.961 | 0.972 | 0.85 | −1.43 | 0.0074 |
| 31 | 0.027 | 0.950 | 0.965 | 0.90 | −1.20 | 0.0071 |
| 32 | 0.035 | 0.967 | 0.978 | 0.82 | −1.55 | 0.0071 |
| 33 | 0.031 | 0.948 | 0.961 | 0.74 | −0.88 | 0.0071 |
| 34 | 0.028 | 0.945 | 0.961 | 0.75 | −1.23 | 0.0068 |
| 36 | 0.027 | 0.951 | 0.959 | 0.47 | −1.60 | 0.0074 |
| 37 | 0.046 | 0.948 | 0.970 | 0.90 | −2.04 | 0.0071 |
| 38 | 0.028 | 0.947 | 0.967 | 0.81 | −0.62 | 0.0068 |
| 39 | 0.044 | 0.963 | 0.973 | 0.63 | −1.65 | 0.0068 |
| 40 | 0.014 | 0.936 | 0.944 | 0.82 | −0.24 | 0.0074 |
| 41 | 0.009 | 0.922 | 0.935 | 0.96 | −0.12 | 0.0070 |
| 42 | 0.033 | 0.952 | 0.965 | 0.47 | −1.69 | 0.0076 |
| 43 | 0.031 | 0.968 | 0.980 | 0.49 | −1.28 | 0.0072 |
| 44 | 0.035 | 0.962 | 0.976 | 0.97 | −0.66 | 0.0066 |
| 45 | 0.034 | 0.967 | 0.981 | 0.98 | −0.95 | 0.0066 |
| 46 | 0.068 | 0.953 | 0.983 | 0.88 | −1.34 | 0.0071 |
| 47 | 0.017 | 0.915 | 0.931 | 0.88 | −0.82 | 0.0070 |
| 48 | 0.169 | 0.967 | 0.988 | 0.85 | −9.18 | 0.0066 |
| 49 | 0.042 | 0.971 | 0.984 | 0.70 | −1.24 | 0.0066 |
| 50 | 0.020 | 0.957 | 0.972 | 0.84 | 0.49 | 0.0071 |
| 51 | 0.044 | 0.965 | 0.980 | 0.93 | −1.72 | 0.0071 |
| 52 | 0.050 | 0.962 | 0.984 | 0.61 | −0.98 | 0.0073 |
| 53 | 0.012 | 0.939 | 0.957 | 0.93 | −0.68 | 0.0065 |
| 54 | 0.049 | 0.954 | 0.980 | 0.49 | −1.76 | 0.0072 |
| 55 | 0.038 | 0.946 | 0.978 | 0.94 | −1.41 | 0.0077 |
| 56 | 0.052 | 0.956 | 0.976 | 0.94 | −2.96 | 0.0075 |
| 57 | 0.026 | 0.953 | 0.967 | 0.58 | −0.88 | 0.0075 |
| 58 | 0.028 | 0.951 | 0.970 | 0.79 | −0.86 | 0.0073 |

Against the maker's two other copies the method is the same and the layer kernel differs: the E4B copy of round 8
edits 21 attention outputs in layers 21 to 41 at weights 1.32 to 2.02 with one residue layer, the 26B copy of piece 6
edits 20 in layers 10 to 29 at 0.76 to 1.49 with none, and this one rewrites 58 and leaves 23 as residues. Against the
four other copies of this base (wangzhang in round 2, pieces 1, 3 and 4 of this round), which stand on the same
original weight file (shards `eeef8791` and `01891222`), no changed matrix has an equal measurement in any field.

## Token and configuration side (Stage 1)

The cluster's card read "unexplained differences" in two fields. Re-judged at home the configuration field closes
and the template stays, so the committed card still reads "unexplained differences"; the reading closes the template
by hand.

- `config.text_config.moe_intermediate_size`: absent in the original, null in the copy, the library default under
  5.6.2; `enable_moe_block` is false and `num_experts` null on both sides. Both files name 5.5.0.dev0 as the saving
  version, so two builds of the same development version differ in whether they write the field. A re-save effect.
- `template.default`: the copy's template (16,433 bytes, no blank line) is Google's template of 2026-04-10, 02:02Z
  (`e51e7dcd`, carried in the pinned `439edf56` of piece 4; 16,448 bytes) with its 15 blank lines removed and no
  other change; the fixed conversation renders identically. It is the same file, byte for byte, as the template in
  the maker's 26B copy (piece 6), committed three minutes later on 2026-04-14. The copy's repository was created ten
  hours after Google's release commit, so the pin took the release template, and the maker's template commit of
  04-14 carries the fix Google had published four days earlier. The later-revision rule compares byte for byte after
  line endings and trailing whitespace, and blank lines defeat it, as they did on the maker's E4B copy in round 8 (14
  blank lines there).

## For the recipe library

Consistent with the stated change on the weight side and on the token side once the template is read. The fifth
measured arbitrary-rank copy of this maker's tool, the second with a row-norm preservation claim that reads 0.007,
and the first whose declared range covers nearly the whole model; the candidate entry needs a line for rewritten
layers at weight near zero (relative change under 0.002, first share under 0.05, remaining fractions at 1), which the
energy-share rule flags today. The saved direction vectors are not committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/blueback12/measurements/pair-2/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
