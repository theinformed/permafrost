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

For every changed two-dimensional tensor, randomized SVD estimates its top eight singular values
using twelve sketch columns, four power iterations, and a recorded random seed.
The squared singular values divided by the squared Frobenius difference give
the energy shares for the first one through eight directions. Low-rank
estimates can underestimate energy; they are estimates, not exact ranks.
The leading left and right vectors go into a separate safetensors file.
This measurement includes embeddings, query matrices, and unrecognized roles.
The first singular value's energy share is recorded for each changed matrix.

Across layers, unit left vectors are grouped by tensor kind and output width.
Their signs are aligned to the most central vector before taking a coordinate
median and normalizing it. Absolute cosines with that median measure agreement.
An all-zero coordinate median is reported as undefined. The report also checks
agreement among all residual-writing projections of equal output width.
Right vectors are saved for later work;
their input widths and meanings differ between these projections. A group of
two vectors reports the angle between them, since both sit at the same angle
from their mean.

Within each layer, the edits are compared again in the residual stream's own
coordinates: the left vector of a residual writer (attention output, down
projection, expert output) and the right vector of a residual reader (query,
key, value, gate and up projections). The same aligned median gives each edit a
layer direction cosine, and the summary records, for every layer, how many
edits it holds and which kinds, plus the agreement between the layers' median
directions, which is reported and not required. A layer with one edit agrees
with itself; the per-layer entries therefore say nothing about direction where
a maker changed one matrix per layer. `rescore_weights` measures this after the
fact from the saved vectors file when it sits beside the report or is named
with `directions=`; without the vectors the report says so and the per-layer
entries cannot match.

Tensor roles are regular-expression patterns in `audit/recipes.json`. The
optional `model.`, `model.language_model.`, or `transformer.` wrapper is stripped
before matching. Residual writers include full-attention `self_attn.o_proj`,
linear-attention `linear_attn.out_proj`, dense `mlp.down_proj`, and expert or
shared-expert down projections. Each has a separate kind in the report.

The analytic `single-projection` envelope requires every residual-writing
matrix present in the checkpoint to change above 0.001, at least 0.99 of each
difference's energy in its first singular value, and direction cosine at least
0.95. Every other tensor must remain within 0.001. The report lists all envelope
violations and the nearest measured or analytic recipe.

`single-projection-selected` uses the same energy and direction limits but
allows any subset of residual writers to remain within 0.001. At least one
residual writer must change; a whole projection kind may be skipped. The report
lists skipped tensors with their layer and kind. When both envelopes match,
`single-projection` takes precedence as the more specific all-layers case.

`directional-per-layer` and `directional-per-layer-selected` are the same two
envelopes for a method that computes its direction once per layer: the same
energy and unchanged limits, a layer direction cosine of at least 0.95 in
place of the shared-direction cosine, no cross-kind check, and the attention
query, key and value projections as optional kinds beside the embedding, since
the tools that work per layer also project the reading side of attention. At
equal violation counts a shared-direction envelope ranks before a per-layer
one, as it asserts more about the edit. Other recipes remain
“not yet measured.” The analytic envelope is not a measured recipe library.

The [reference recipe runners](recipe-library.md) produce a separate measured
`envelopes.json`, accepted by `compare-weights --recipes`. Each measured recipe
requires matching base shard checksums. A measured row-norm preservation rule is
checked for every matrix with row-norm measurements. Skipped and unchanged
reference runs supply no measured matching candidate.

`audit.weights.rescore_weights(path)` updates a saved report from its per-tensor
measurements without downloading or reading checkpoint weights. It reclassifies
roles and recalculates recipe matches and summary counts. Saved singular values,
energy shares, and direction cosines remain unchanged. The direction summary
keeps its original group references and cross-kind coverage; re-scoring cannot
extend that coverage without the saved vectors. The report records this in
`rescoring.direction_measurements`. A fresh comparison measures agreement among
all residual writers.

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
