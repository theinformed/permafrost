# Reading of the calibration result: our norm-preserving projection of Mistral Small 3.2 24B (2026-10-14)

Created by Sean Egan, 2026-10-14.

This is the first measured norm-preserving row the recipe table has had. I applied the edit myself, so the 76 flags
describe the scorer. On reading, the copy is a single-direction removal with each changed row put back to its
original length, stored in bfloat16, and nothing else touched.

## How the row-norm restore changes the fingerprint

Set beside the single projection on the same base, the two copies agree on almost everything:

| Measure, median over 40 | Single projection, attention / down | Norm-preserving, attention / down |
| --- | --- | --- |
| First-value energy share | 0.9891 / 0.9881 | 0.9879 / 0.9877 |
| Energy outside the first direction, over the weight norm | 0.00153 / 0.00153 | 0.00161 / 0.00155 |
| Direction cosine | 0.999997 / 0.999999 | 0.999996 / 0.999999 |
| Relative change | 0.0147 / 0.0141 | 0.0147 / 0.0141 |
| Largest row-norm change | 0.0092 / 0.0073 | 0.00018 / 0.00009 |

- The rescale multiplies each row by a factor very close to one. That adds a small piece spread over many directions,
  about 0.0005 of the weight norm on attention outputs and 0.0003 on down projections, estimated from the medians.
  It is why the energy share sits a little lower and why the scorer raised 76 flags here against 68.
- The direction and the size of the edit are unchanged to the precision shown.
- The largest row-norm change falls from 0.0025 to 0.0149 on the plain projection to 0.00005 to 0.00027 here. What
  remains is bfloat16 rounding of each row. This single measure separates the two recipes, with a factor of nine
  between the largest norm-preserving value and the smallest plain-projection value.

## The calibrated line for this base

The single-projection line holds here too: energy share floor 0.98 (lowest measured 0.9851, so 1.49 percent of energy
outside the first direction against 2.0 percent allowed), direction cosine floor 0.999 (lowest measured 0.999989, about
90 times the measured gap), unchanged tensors within 0.001, and the proposed leftover rule of 0.0025 of the weight norm
(largest measured 0.00168).

What makes it the norm-preserving line is one more rule: the largest row-norm change stays at or below 0.001. That
sits 3.8 times above the largest value measured here and 2.5 times below the smallest value on the plain projection.
The scorer cannot apply it yet. Its only row-norm check is a yes or no at a tolerance of 0.00001, which fails all 80
of these known-clean matrices. Until the scorer reads the new limit, the norm-preserving entry stays inert; without it
the two lines would tie and the name would be chosen alphabetically.

## Limits of this reading

Each recipe has one run on one base. Round 4 recomputed the direction in its own forward pass, and neither run's
direction file came back with the report, so I have not measured how closely the two directions agree. The matching
relative changes suggest they are very close. Round 1's recipe card and timing record were not pulled, so only its
report is tracked.
