# Reading of the Stage 1 and Stage 2 result: llmfan46/gemma-4-E4B-it-uncensored-heretic against google/gemma-4-E4B-it (2026-10-29)

Measured on Nautilus, round 2 piece 3 (job 3763595, 7 minutes, exit 0). Modified revision `446ec370` (2026-05-04),
original pinned at `292a7e27` (2026-04-02). The maker's card names the method and its parameters: Heretic 1.2.0 with
Arbitrary-Rank Ablation, layers 8 to 36, targeted component attn.o_proj only, with the weights its search chose.

## Weights (Stage 2)

The automatic verdict was "recipe violations", nearest recipe single-projection-selected, 23 flags, as scored on the
cluster; re-scored with the per-layer entries it is nearest `directional-per-layer-selected` with 11 flags, the
energy shares below. The copy changes one matrix per layer, so the per-layer entry asserts nothing about its
directions and the nearer label does not mean a match. On reading, the footprint matches the card and the flags
measure a method the table does not describe yet.

- 11 of 2,130 tensors changed, all attention outputs, in layers 21 to 35 of 42. That sits inside the card's layer
  range 8 to 36 and its single target component. Seventeen other attention outputs differ by at most 0.00008 of their
  norm, below the 0.001 threshold: layers the search weighted near zero. Nothing outside the attention outputs moved,
  including the per-layer embeddings and the vision and audio towers.
- The changes are not rank-one. First-value energy share is 0.92 to 0.96, and the first eight values together reach
  only 0.94 to 0.97; the remainder is spread across many directions. Relative change is 0.02 to 0.05, large enough
  that bfloat16 rounding accounts for at most 0.005 of the missing share. The method's name says as much:
  arbitrary rank. The table's "arbitrary-rank" entry is still "not yet measured".
- The leading directions differ by layer (cosine 0.15 to 0.46 with the median), as Heretic's per-layer directions
  would.
- Row norms moved by up to 0.017 relative; nothing in the card claims they were preserved.

## Token and configuration side (Stage 1)

The automatic verdict is "consistent with re-save noted" now that the tool reads the library defaults and the
original repository's later commits; it finds the same two commits named below, `c53e9d33` and `3555bddc`. On first scoring it was
"unexplained differences" in two fields, and the reading stands.

- `template.default`: the copy carries Google's later template, matching `google/gemma-4-E4B-it` at commits
  `c53e9d33` (2026-04-28) and `3555bddc` (2026-05-07) exactly; the pinned modified revision is itself the maker's
  commit "Upload chat_template.jinja" of 2026-05-04. The fixed conversation renders identically.
- `config.text_config.moe_intermediate_size`: absent in every Google revision, present and null in the copy, saved
  with transformers 5.5.0 against the original's 5.5.0.dev0. A re-save addition, and the tool now classes it as
  explained by re-save.

## For the recipe library

Consistent with the stated change on both sides. For the recipe library this is the first measured arbitrary-rank
edit: an energy profile that does not climb toward 1 by the eighth value is its signature, distinct from the
bfloat16 floor, which only lowers the first share on small edits and climbs to 1 within one or two values. The
"arbitrary-rank" entry can be calibrated from this when a run of our own is made.

Weight differences alone cannot certify the absence of hidden behavior.

## Second pass (2026-10-30)

Measured again on Nautilus, round 3 piece 3 (card 5055, download job 4080809, compare job 4080812, exit 0), on the
same pins (modified `446ec370`, original `292a7e27`) and the same shard checksums, with the comparison as of commit
d0f48bb. The second-pass report is `results/weights/llmfan46-gemma-4-E4B-it-uncensored-heretic.pass-2.json`; its
leading vectors are in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus3/measurements/pair-3/weights.directions.safetensors`.

It reads as before: recipe violations, nearest `directional-per-layer-selected`, the same 11 energy-share flags, 11
changed tensors, 0.00008 outside them. Every measure both passes report is equal to the last digit.

The new measure is what this pass was for. Along the eight leading directions of each of the 11 attention outputs
the copy keeps the following fractions of the original's action (left is along the output-side vector, right along
the input-side vector; E1 and E8 are the energy in the first value and in the first eight):

| Layer | Relative change | E1 | E8 | Left, direction 1 | Right, direction 1 | Right, directions 2 to 8 |
| --- | --- | --- | --- | --- | --- | --- |
| 21 | 0.030 | 0.931 | 0.960 | 0.77 | −0.36 | 0.93 to 1.01 |
| 22 | 0.036 | 0.957 | 0.971 | 0.62 | −0.40 | 0.95 to 1.00 |
| 23 | 0.039 | 0.920 | 0.935 | 0.81 | −0.79 | 0.96 to 0.99 |
| 24 | 0.044 | 0.960 | 0.972 | 0.29 | −0.47 | 0.94 to 1.00 |
| 25 | 0.035 | 0.960 | 0.975 | 0.59 | −0.27 | 0.95 to 1.01 |
| 26 | 0.026 | 0.942 | 0.952 | 0.76 | −0.34 | 0.97 to 1.02 |
| 27 | 0.046 | 0.941 | 0.963 | 0.80 | −0.57 | 0.90 to 1.03 |
| 29 | 0.025 | 0.957 | 0.967 | 0.92 | −0.53 | 0.98 to 1.00 |
| 30 | 0.052 | 0.947 | 0.961 | 0.62 | −0.58 | 0.92 to 0.99 |
| 32 | 0.036 | 0.948 | 0.961 | 0.74 | −0.73 | 0.91 to 1.01 |
| 35 | 0.022 | 0.952 | 0.964 | 0.77 | −0.41 | 0.96 to 1.00 |

The leading direction sits on the input side of the attention output, in the coordinates of the concatenated
head outputs. On all 11 matrices the left fraction is above the right one, the order a rank-one edit on the input
side produces; the output-side edits of the other four pairs give the reverse order on 273 of their 274 matrices
(the one exception is an embedding, whose residual coordinates are on the right). Along that direction the copy
keeps −0.27 to −0.79, a weight of 1.27 to 1.79 (median 1.46), past a plain ablation (which reads 0) and short of a
reflection (−1), a scaled projection whose weight differs by layer as a searched per-layer weight would. The rest
of the edit is a weak tail. Along the second to eighth directions the copy keeps 0.90 to 1.03 (median 0.986),
weights under about 0.1 each, and 2.5 to 6.5 percent of the energy lies beyond the eighth direction. The profile is one over-projected direction plus many small ones, which is
what the method's name says. The library's runner records that the pinned public release 1.3.0 has no
arbitrary-rank search; the card names release 1.2.0, so a run of our own needs that release.

For an arbitrary-rank entry these numbers give a first line, from one copy: attention outputs in a selected set of
layers, one matrix per layer (so no within-layer direction term); first-value energy share at least 0.90 (measured
0.920 to 0.960); energy in the first eight values 0.93 to 0.975 at relative change 0.02 to 0.05, where the rounding
floor alone would leave 0.999, which is the signature that separates it from a rank-one edit; a remaining fraction
along the leading direction between −1 and 0 on one side (measured −0.79 to −0.27) with the tail directions keeping
at least 0.89; everything outside the changed set within 0.001 (measured 0.00008); no row-norm limit (0.0016 to
0.0165). A calibration run of our own is needed before the line goes into the table.

On the token side the cluster's card reads "unexplained differences" on `config.text_config.moe_intermediate_size`
and `template.default`, the two fields the first pass closed. The compare job runs without network access, so the
template rule cannot read the original repository's later commits, and its pinned transformers 4.56.2 has no
Gemma 4 configuration class, so the library-default rule has nothing to ask. Re-judged at home under transformers
5.6.2 with the original repository's history, the same report reads "consistent with re-save noted" on the same
commits, `c53e9d33` and `3555bddc`; that report is
`results/meta/llmfan46-gemma-4-E4B-it-uncensored-heretic.pass-2.json`, with the cluster's reading kept in its
`reclassification` block.
