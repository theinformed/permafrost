# Reading of the calibration result: our single projection of Mistral Small 3.2 24B (2026-10-14)

Created by Sean Egan, 2026-10-14.

I applied this edit myself, so every flag the scorer raised describes the scorer. The automatic verdict says
"recipe violations" with 68 flags. On reading, the copy is exactly what I made: one direction removed from 80
residual-writing matrices, nothing else touched, and the energy shortfall below 0.99 comes from saving the copy in
bfloat16.

## Why a clean rank-one edit scores below 0.99

The edit `W - r (rᵀ W)` changes each matrix by a single direction, so in exact arithmetic the first singular value
holds all of the difference. Saving the result in bfloat16 rounds every entry that moved. That rounding is spread
over thousands of directions, and the scorer counts it as energy outside the first one.

Three measurements say the leftover is rounding:

- The energy outside the first direction, taken as a norm and divided by the weight's own norm, sits between 0.00151
  and 0.00156 for all 80 matrices, in both kinds. Rounding to an 8-bit significand leaves about that much.
- About 27 percent of entries did not change at all. Those are the entries whose change was smaller than half a
  bfloat16 step, so they rounded back to the original value.
- Singular values two through eight are flat (0.0045 to 0.0094 against a first value of 0.60 on layer 10's down
  projection). A second real direction would stand out; rounding noise does not.

A synthetic check reproduces it. A random matrix stored in bfloat16, given a rank-one change of 1.46 percent of its
norm, cast back to bfloat16 and measured the same way, gives a first-value share of 0.9888, a leftover of 0.00154 of
the weight norm, and 26.6 percent of entries unchanged. The Mistral medians are 0.989, 0.00153 and 27 percent.

So the share follows a simple rule: one minus the share is roughly the square of the rounding leftover (about
0.0015) over the relative change. On this copy that leftover is close to constant, so the matrices that cleared 0.99
were simply the ones with the largest edits. The correlation between one minus the share and that prediction is
0.998 for attention outputs and 0.9997 for down projections. The same synthetic matrix with a gentler edit, 0.5
percent of its norm, scores 0.932. A fixed floor on this share is really a floor on how hard the edit pushed.

## The calibrated line for this base

- Energy share floor 0.98. The lowest measured value is 0.9859, so the line leaves room for 2.0 percent of energy
  outside the first direction against 1.41 percent measured.
- Direction cosine floor 0.999. The lowest measured value is 0.999994; the old floor of 0.95 never came close to
  firing, and 0.999 still leaves more than a hundred times the measured gap.
- Unchanged tensors stay within 0.001 relative change; the measured value outside the 80 is 0.
- Proposed rule for the scorer: energy outside the first direction no larger than 0.0025 of the weight norm. The
  largest measured value is 0.00156 here and 0.00168 on the norm-preserving copy. This rule depends only on the
  storage type, so it should carry to other bfloat16 bases; the scorer does not read it yet.

With the first three lines added for this base, the scorer matches both of my copies with zero flags.

## What it suggests for the census

Every census upload with a weight comparison so far carries the same leftover, 0.00151 to 0.00161 of the weight norm. The 68 and 75
energy-share flags on the Qwen3.5 27B and Qwen2.5 32B copies look like this same rounding effect. That is a
hypothesis to re-score on their own bases; the details are in [the calibration note](../calibration-mistral-small-3.2.md).
