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
