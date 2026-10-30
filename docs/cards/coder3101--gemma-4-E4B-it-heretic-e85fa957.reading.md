# Reading of the Stage 1 and Stage 2 result: coder3101/gemma-4-E4B-it-heretic against google/gemma-4-E4B-it (2026-10-30)

Measured on Blueback, round 8 piece 3 (round card 5305, download job 3397500, compare jobs 3397501 to 3397508, all exit
0, sweep 3397509; pulled home by card 5347). Modified revision `24a5d4b1` (2026-04-14; the repository was created on
2026-04-03), original pinned at `292a7e27` (2026-04-02). The maker's card names the method and its parameters: Heretic
1.2.0 with Arbitrary-Rank Ablation and row-norm preservation, start layer 21, end layer 42, with the preserve, steer
and overcorrect weights its search chose and a neighbour count of 14; it reports 3 refusals in 100 and a KL
divergence of 0.0058. The card lists no targeted component.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 21 flags, on the
cluster and after re-scoring at home. All 21 flags are energy shares. On reading, the footprint matches the card and
the flags measure the arbitrary-rank method, which the table still lists as "not yet measured".

- 21 of 2,130 tensors changed, all attention outputs, in layers 21 to 41 of 42: every layer of the card's range, and
  the one component the method edits. Nothing else moved; the largest relative change outside the changed set is
  exactly 0.
- Layer 41 is a rounding residue. Its relative change is 0.0018, its first-value energy share 0.002 and its first
  eight 0.013, the copy keeps 1.000 and 1.001 of the original's action along the leading directions, and its row
  norms moved by 0.0008. The search gave that layer a weight near zero, and what survives is bfloat16 rounding of a
  matrix that was rewritten.
- The other 20 are the arbitrary-rank profile: first-value share 0.905 to 0.965, first eight values 0.950 to 0.981,
  on relative changes of 0.020 to 0.061 where rounding alone would leave 0.999 by the second value.
- The leading direction sits on the input side. Along it the copy keeps −0.32 to −1.02 of the original's action on
  the right (weights 1.32 to 2.02, median 1.46) and 0.33 to 0.97 on the left; the left fraction is above the right
  on 20 of the 21 matrices (layer 41 is the exception), the order round 3 read on the same maker tool's other copies.
  The tail directions keep 0.70 to 1.08 (median 0.96).
- The leading directions differ by layer (cosine 0.11 to 0.37 with their median, 0.21 in the middle).
- Row norms moved by 0.0071 to 0.0078 relative on the 20 matrices. The card claims row-norm preservation; the rows
  moved by about three quarters of a percent, more than the approximate restoration of the igorls copy in round 7
  (0.0018 to 0.0040) and inside the 0.0016 to 0.0165 of the llmfan46 arbitrary-rank copies, whose cards claim none.
- Against llmfan46's two E4B copies of the same method (11 attention outputs in layers 21 to 35; 17 in layers 18 to
  35) and the other E4B copies on the same weight file, no changed matrix has an equal measurement in any field.

## Token and configuration side (Stage 1)

The cluster's card read "unexplained differences" in two fields. Re-judged at home the configuration field closes and
the template stays, so the committed card still reads "unexplained differences"; the reading closes the template by
hand.

- `config.text_config.moe_intermediate_size`: absent in the original, null in the copy, the library default under
  5.6.2. `transformers_version` is 5.5.0.dev0 on both sides.
- `template.default`: the copy's template (16,303 bytes) is Google's template of 2026-04-10, 02:02Z (`ab4d2025`,
  16,317 bytes) with 14 blank lines removed and no other change; the fixed conversation renders identically. The
  copy's repository was created on 2026-04-03, so the pin rule chose the release template of 2026-04-02, and its
  weights revision of 2026-04-14 carries the template Google had published four days earlier. The later-revision
  rule compares byte for byte after line endings and trailing whitespace, and blank lines defeat it; a comparison
  that drops blank lines would close this field.

## For the recipe library

Consistent with the stated change on the weight side and on the token side once the template is read. The third
measured arbitrary-rank copy on this base, with the second maker and the first claim of row-norm preservation, which
the row norms put at 0.007. The saved direction vectors are not committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/blueback8/measurements/pair-3/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
