# Comparing checkpoint weights

The comparison reads matching tensor names from safetensors shards, one pair at
a time. It records each shard's SHA-256 checksum and pins remote checkpoints to
their resolved revision. Added names, missing names, and different shapes are
reported separately. Comparisons run on CPU with one thread by default.

Each difference is computed in float32. Floating-point formats, including
bfloat16, are converted before subtraction. Native quantized tensors are
dequantized; packed integer formats need their own decoder and are rejected.
Casting packed integers would compare storage codes instead of weights.

The relative Frobenius difference is the norm of the difference divided by the
original norm. Norms are accumulated in float64. A zero original with a nonzero
difference has an undefined relative difference and is marked changed. The
report also gives the signed mean, signed extrema, largest absolute difference,
and fractions of positive and negative entries. These distinguish a small
distributed change from a concentrated change or a consistent signed shift.

For a changed matrix, randomized SVD estimates its top eight singular values
using twelve sketch columns, four power iterations, and a recorded random seed.
The squared singular values divided by the squared Frobenius difference give
the energy shares for the first one through eight directions. Low-rank
estimates can underestimate energy; they are estimates, not exact ranks.
The leading left and right vectors go into a separate safetensors file.

Across layers, unit left vectors are grouped by tensor kind and output width.
Their signs are aligned to the most central vector before taking a coordinate
median and normalizing it. Absolute cosines with that median measure agreement.
An all-zero coordinate median is reported as undefined. The report also checks
agreement between attention output and feed-forward
down projections of equal output width. Right vectors are saved for later work;
their input widths and meanings differ between these projections.

The analytic `single-projection` envelope requires every attention `o_proj`
and feed-forward `down_proj` tensor to change above 0.001, at least 0.99 of each
difference's energy in its first singular value, and direction cosine at least
0.95. Every other tensor must remain within 0.001. The report lists all envelope
violations and the nearest measured or analytic recipe. Other recipes remain
“not yet measured.” The analytic envelope is not a measured recipe library.

Row norms are checked independently with relative tolerance 0.00001 and absolute
tolerance 0.0000001. A rank-one change can alter row norms. Conversely, unchanged
row norms say little about rank. The summary gives the changed names and kinds,
largest difference among unchanged tensors, largest difference outside the
recipe's projection set, smallest first-value energy share, and median and
minimum direction agreement.

The two CPU controls use a 135-million-parameter instruction checkpoint.
The rounding copy converts every tensor through bfloat16 and back to float32.
The projection copy uses the normalized difference between mean residuals for
32 harmful-style and 32 harmless instructions, measured at the final token of
the assistant prefix, at the input to the middle block. This follows the
[difference-of-means construction](https://github.com/andyrdt/refusal_direction/blob/main/pipeline/submodules/generate_directions.py)
of [Arditi et al.](https://arxiv.org/abs/2406.11717).
The prompt lists are tame source inputs in `data/prompts/`. They test the
weight comparison; this run does not validate refusal behavior. The forward
pass streams blocks only as far as that residual, with no answer generation.
Each output projection becomes `W - r (rᵀ W)` and is saved in float32.

Use `audit compare-weights --modified DIR --original DIR --out REPORT`.
The venv's `audit` entry point exposes the same commands. `make-null --model REPO`
also accepts separate steps: `prepare`, `rounding`, `activations --batch-index N`
for N from 0 to 7, `project`, and `compare`. Saved batches are tied to the exact
weights and prompts. The default runs all steps. A remote file above 1 GB is
rejected before downloading. Generated checkpoints and reports stay under
`data/`; this control uses about 1.3 GB. Copies can be deleted after their
reports and checksums are retained; the prompt lists remain versioned.

Weight differences alone cannot certify the absence of hidden behavior.
