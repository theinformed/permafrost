# Reading of the Stage 1 and Stage 2 result: TrevorJS/gemma-4-26B-A4B-it-uncensored against google/gemma-4-26B-A4B-it (2026-10-29)

Measured on Nautilus, round 2 piece 4 (job 3763596, 21 minutes, exit 0). Modified revision `fc582b97` (2026-04-03),
original pinned at `47b6801b` (2026-03-11). The maker's card describes the method in detail: norm-preserving
biprojected abliteration on o_proj and the shared mlp.down_proj in all layers, the same modification on all 128
expert down projections per layer, per-layer refusal directions, scale 1.0.

## Weights (Stage 2)

The automatic verdict was "recipe violations", nearest recipe single-projection, 121 flags as scored on the cluster.
Re-scored with the per-layer entries it is nearest `directional-per-layer` with 64 flags: 60 on the 30 packed expert
tensors (no singular values, so no energy share and no direction) and four layer-direction flags. Within each layer
the attention output and the down projection agree at cosine 0.94 to 0.99 (median 0.977), against 0.10 between
layers; 28 layers clear the 0.95 line, layers 10 and 12 sit at 0.941 and 0.947 (the four flags, two matrices
each), and the next lowest are layers 9 and 27 at 0.953 and 0.956. The card's method projects both sides of each matrix, and the
input-side term bends the leading direction of the difference by about that much. On reading, the weights match the
card's description line by line, and the remaining flags come from the packed experts the tool has not measured.

- 90 of 1,013 tensors changed: in each of the 30 layers the attention output, the shared feed-forward down
  projection and the packed expert down projection (shape 128 by 2816 by 704). Nothing else moved: the packed expert
  gate-up tensors, the query, key and value projections and the vision tower are bit-identical, and the largest
  relative change outside the 90 is exactly 0. That is the card's footprint exactly.
- The 60 two-dimensional changes are each one direction (first-value energy share at least 0.9906, relative change
  0.018 to 0.030) and the direction differs by layer (cosine 0.03 to 0.63 with the median, the two kinds moving
  together layer by layer). The card says per-layer directions. The table's projection entries ask for one shared
  direction, hence 60 direction flags.
- Row norms were restored: the largest relative change in a row norm is 0.0004 on the attention outputs and 0.0011
  on the down projections, against 0.005 to 0.015 for a plain projection of this size. That is the card's
  norm-preserving step.
- The 30 packed expert tensors are three-dimensional, so the comparison recorded their relative change (0.019 to
  0.023, the same band as the dense edits) but computed no singular values. The scorer then flagged each for a
  missing energy share. A per-expert measure on packed tensors is a scorer follow-up; until it exists these 30 are
  unmeasured, not failed.
- The round's own naming table knew the packed expert names; the shared table in `audit/recipes.json` did not until
  today, and now classes `layers.N.experts.down_proj` as an expert down projection and `layers.N.experts.gate_up_proj`
  as the expert gate-up pair.

## Token and configuration side (Stage 1)

The automatic verdict is "consistent with re-save noted": only the two saved transformers version strings differ
(5.5.0.dev0 to 5.5.0). Tokenizer, special tokens, generation settings and chat template are unchanged, and the fixed
conversation renders identically.

## For the recipe library

Consistent with the stated change on both sides, and the most completely described upload in the census so far. It
is also the first mixture-of-experts copy measured; the packed expert layout is now in the shared table, and the
per-expert singular values are the next thing the scorer needs.

Weight differences alone cannot certify the absence of hidden behavior.

## Second pass (2026-10-30)

Measured again on Nautilus, round 3 piece 4 (card 5055, download job 4080809, compare job 4080814, exit 0), on the
same pins (modified `fc582b97`, original `47b6801b`) and the same shard checksums, with the comparison as of commit
d0f48bb. The second-pass report is `results/weights/TrevorJS-gemma-4-26B-A4B-it-uncensored.pass-2.json`; its leading
vectors, the packed experts' median directions among them, are in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus3/measurements/pair-4/weights.directions.safetensors`.

Scored with today's table it reads recipe violations, nearest `directional-per-layer`, 31 flags where the first pass
had 64: 30 energy-share flags on the 30 packed expert tensors and one layer-direction flag (layer 29). The 90 changed
tensors, the 0 outside them and every measure on the 60 dense matrices are equal to the last digit between the
passes. The 30 packed expert tensors, which the first pass recorded without singular values, are now measured one
expert at a time.

- All 128 experts changed in every layer. Each expert's relative change is 0.015 to 0.051 (per-layer medians
  0.018 to 0.022, the band of the dense edits), and its leading output direction agrees with the other 127 at
  median cosine 0.996 to 0.999 (minimum 0.940, in layer 21). That is the card's "same modification on all 128
  expert down projections per layer", read from the weights. The experts' input directions are unrelated to each
  other (median cosine 0.07 to 0.08), as each expert has its own input space.
- First-value energy share per expert: the median expert in every layer sits at 0.989 to 0.994, within 0.001 of
  the 0.99 line; the worst expert sits at 0.881 (layer 0), 0.951 (layer 2), 0.969 (layer 1), 0.973 (layer 17) and
  0.979 to 0.990 in the other 26 layers. The scorer takes the worst expert, hence the 30 flags. The second term
  of the biprojection (the input-side projection) is the likely source of the worst experts' shortfall, as it is of
  the direction bends below; the per-expert record keeps only the minimum, median and maximum, so the next
  comparison should keep each expert's share.
- Layers 10 and 12 resolve. The first pass compared two vectors per layer (attention output and dense down
  projection) and reported their pairwise angle: 0.941 and 0.947. With the experts' median direction as a third
  member the layer medians are 0.991 and 0.995 and the minima 0.962 and 0.970, above the 0.95 line. Across the 30
  layers the three-member groups agree at median 0.980 to 0.998 and minimum 0.949 to 0.994. The one flag left is
  layer 29, where the experts' median direction sits at 0.949 from the layer's median (the first pass had the dense
  pair at 0.973 there).
- Remaining fraction along the leading output direction, where a plain ablation reads 0: attention outputs 0.02 to
  0.28 (median 0.14), dense down projections −0.001 to 0.51 (median 0.08), the per-layer median over the 128
  experts 0.009 to 0.52 (median 0.05). The card's scale 1.0 is what the small values read. The large ones sit
  where the input-side term is comparable to the output-side one (layer 29's experts 0.52, layer 26's down
  projection 0.51, layer 9's 0.34), the same places the leading directions bend. On all 60 dense matrices the left
  fraction is below the right one (right 0.45 to 0.88), the order of an edit on the output side. Along the second to
  eighth directions the dense matrices keep 0.99 to 1.05.
- Row norms, now read per expert row: the largest relative change on a packed expert tensor is 0.00118 (layer 3),
  with layers 10, 15, 22 and 24 between 0.00101 and 0.00115 and the rest under 0.001; the dense matrices are as
  before. The norm-preserving step holds on the experts too, and a 0.001 line would catch five of the 30 by a hair.

For a per-layer entry that covers packed experts these numbers give a first line: expert down projections scored
per expert, with the median expert's energy share at least 0.985 (measured 0.989 to 0.994) and the worst expert
reported; the experts' output directions agreeing within a layer at cosine 0.94 or better (measured minimum
0.940); the experts' median direction joining the layer's dense directions under the 0.95 layer line (29 of 30
layers pass, layer 29 at 0.949); a remaining fraction along the leading output direction near 0 with the
biprojection's second term allowed up to about 0.5; row norms within 0.0015 per expert row. The biprojection
itself, which puts a second direction on the input side, is the thing a calibration run of our own should
reproduce before the line is fixed.

On the token side the cluster's card reads "consistent with re-save noted" as before: the two saved transformers
version strings differ and nothing else. The same at home; the report is
`results/meta/TrevorJS-gemma-4-26B-A4B-it-uncensored.pass-2.json`.
