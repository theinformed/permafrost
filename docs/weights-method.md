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

Along each of the eight leading directions the report also records how much of
the original's action the modified matrix keeps: on the left, the projection of
the modified row-combination u'W' onto the original u'W as a fraction of
|u'W|^2, and on the right the same for W v. A projection of weight a along a
direction leaves 1 - a there: 0 for a plain ablation, -0.5 at weight 1.5, -1
for a reflection, and 1 where the direction was not touched. The products go
a block of rows at a time, so no float32 copy of a whole matrix is needed.

A three-dimensional tensor, the packed expert layout, is measured one expert
at a time: each expert's relative change, first-value energy share and
remaining fraction along its leading direction, summarised as minimum, median
and maximum, with the agreement of the experts' leading left and right vectors
among themselves. The worst expert's energy share stands for the tensor, and
the experts' median directions are saved as its vectors, so the layer
agreement groups the packed output projection with the dense matrices of the
same width. Row norms are read per expert row.

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
before matching. An export that saves the same tensors under one wrapper more
or fewer, under one wrapper swapped for another, or without the `linear`
segment inside a tower (the table's `infixes`) is paired by name before the
comparison; each rule is accepted only when it pairs every modified name with
exactly one original, and the report names the wrapper and the side that wrote
it. Residual writers include full-attention `self_attn.o_proj`,
linear-attention `linear_attn.out_proj`, dense `mlp.down_proj`, and expert or
shared-expert down projections. Each has a separate kind in the report.

Three kinds of name found on one side only are listed apart from a real
omission: the key and value tensors of layers that read another layer's cache
(`unused_shared_kv`), a vision or audio tower the export left out entirely
(`dropped_towers`), and the scalar activation ranges, `input_max` and the like,
that Gemma 4's E-series originals carry beside their projections and a copy
saved through transformers drops (`dropped_statistics`). Everything else found on
one side is a structural violation.

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

## Pinning a pair

`hpc/pin_census.py` records each pair before a round: the copy at its current revision, the newest
original commit no later than the copy's creation, with both lineages. Its `names` step writes the
published tensor names of both sides and refuses a pair whose names no pairing rule of the comparison
reaches (the exact name, one wrapper added or dropped, two wrappers swapped, one segment inside a
tower), naming the counts on both sides, so the refusal comes before the rehearsal rather than from
an empty changed set. A copy whose hub id and revision a saved report under `results/weights/` already
carries is refused with the round that measured it, whatever a batch note says, unless
`--allow-duplicate` asks for the repeat. A copy whose name says `qat` and whose `base_model` field names
the instruct model of its size is pinned against that size's `-qat-q4_0-unquantized` checkpoint when the
hub has one, the field kept in the record beside a note, because such a card carries the QAT checkpoint's
own header; an original the caller names otherwise is followed as given. A repository the card's first
heading or first sentence names, other than the copy or its `base_model`, is recorded as `card_parent`
when it exists on the hub, with a warning naming it beside the field, and the pinned original does not
change for it. A `base_model` name the hub does not serve (a card naming google/gemma-3-12b where the hub
serves google/gemma-3-12b-it) is kept in the chain as a leaf marked `missing`, with a note at pin time;
it counts as a publisher root when its maker put out a leaf of the original's tree and is no party to
the comparison, and under any other maker the lineage screen holds the pair as unknown. A copy or
original whose hub id carries a restricted maker's model name (a 1B pass named for a GLM distillation)
is refused before any hub call, with the word named, under the same pattern list the home screen
applies to a batch before it leaves, so a pinned batch no longer fails that screen on a name. An
original whose config at the pinned revision declares quantised weights is refused at pin time, before
any fixture download, unless `--allow-quantised-original` asks for the pair; the record keeps the
original's dtype and whether it is quantised, or that the config could not be read. A rate limit from
the hub, wherever it arrives, stops the pass rather than reading as a missing repository or a refused
pair.

The `names` step also refuses a copy whose weight files are the ones a measured copy carries (by the
LFS checksums), naming that copy and its round; a copy whose paired tensors have other shapes than the
original's, as an export of some other model (one copy named for the E2B is the first-generation 2B);
a copy that carries only some of the original's layers in a tower it does carry, as a partial export,
with the missing range; a copy whose shard index names files the repository never published, with the
files it does publish; and an original whose weights are float8, whether its fixture is new or from an
earlier pass. Mistral's `consolidated*.safetensors`, the maker's own format published beside the HF
files, are left out of the fixture as the kit's download leaves them out of the checkpoint.

## How the population is counted

`hpc/population.py` counts the reports in `results/weights/` against the organisations in `data/publishers.txt`,
and it reads the judged lists in `data/population/`, one hub id per line. The reading notes in `docs/cards/` and
the findings decide which list a copy joins; a read-out adds each new copy to its list and reruns the script, which
exits with an error when a list names a hub id no report carries.

- A report is one file in `results/weights/`; the two calibration edits are reports that name no copy.
- A measurement is one comparison of a copy's folder with an original's folder, so a second report over the same two folders (the five round 2 second passes) adds no measurement.
- A distinct copy is keyed on its hub id alone, taken from the census block or, in the five Qwen reports written before that block existed, from the modified source; no two hub ids differ only in case.
- A repeated measurement is a further measurement of a copy already measured, against a second original or against the same original in a later round.
- An original is a checkpoint whose organisation is in `data/publishers.txt`.
- A community parent is any other repository a copy is measured against, and it counts as neither an original nor a copy unless it is measured against its own parent (finding 117), even when its files are a publisher's by object id.
- A copy on a community parent has at least one measurement against one, and the header separates the copies measured against no publisher's original.
- A re-upload is a copy whose weight files are another repository's by object id or checksum; the script counts those its census block marks (`duplicate_of`, or `same_weights_as` naming another repository), and `re-uploads.txt` lists every one the round notes judged.
- A copy is read unless `not-read.txt` lists it, as it lists the re-uploads read as another repository's report and the two copies whose comparison read nothing (one paired no tensor, one has a float8 original).
- A read copy is what its card says unless `differs.txt` lists it, and such a copy is training when `training.txt` lists it, its parent's files unchanged when `parent-files.txt` lists it, and an ablation otherwise, as its leading direction reads in the reading note.
- A copy's outside value is `summary.max_relative_difference_outside_changed_set` in its reading measurement, the report named after the copy, and the script counts the copies that read as their cards say with that value exactly 0.
- A small value is a nonzero outside value on matrices the method weighted near zero or did not name, judged per copy and listed in `small-outside.txt`, and the script counts the other nonzero values, which finding 1 names one by one.
- A copy measured against the pretrained base its field names while it stands on the instruct checkpoint its card names is listed in `instruct-on-pretrained.txt`, judged by byte range.

## Comparing the saved directions

Each comparison saves, for every changed matrix, the leading left and right singular directions of the difference
as float32 unit vectors in `weights.directions.safetensors` beside the report, the sign fixed by the largest left
entry, so the sign is a convention and every comparison below reads the absolute cosine. Five commands under `hpc/`
read those files across the census; none of them touches a checkpoint.

`hpc/direction_cosines.py --pulls DIR... --out results/directions` groups every measured copy by parent and compares
each pair of copies under a parent key by key, one copy's tensors loaded at a time, writing one json per parent
(every pair's per-side median, count, high and flipped fractions and the cosines themselves) and an index.
`hpc/direction_families.py` reads those files and writes `results/directions/families.md` and `.json`: the
distribution of the pooled cosines, per parent the families (connected components at a median absolute cosine of
0.9 or more over the shared right vectors) and the copies with no partner at 0.5, the same figures by name class,
the restriction to the keys where both reports read a first-singular energy share of 0.9 or more, and the pairs
whose signed and absolute medians differ. The parameter tables beside them, one per Gemma 4 parent, set each copy's
family beside the tool figures its reading note records.

`hpc/direction_layers.py --group results/directions/<parent>.json --pulls DIR --reference REPO --out FILE.md` takes
one copy that carries a direction per layer as the reference and reads, from the o_proj left vectors, how far the
reference's own direction turns between adjacent layers and between layers ten or more apart, and for every other
copy of the parent its window, its own spread, its own adjacent and far medians, and the reference layer its
middle-layer direction matches best. `hpc/direction_modes.py --directions results/directions --pulls DIR --families
results/directions/families.json --weights results/weights --out results/directions/modes.md` sorts every census
copy by those two figures of its own: one direction when the far median is 0.9 or more, per layer when the
adjacent median is 0.5 or more and the far median 0.2 or less, arbitrary rank when the adjacent median is under
0.2, mixed otherwise, and counts the modes by the word in the copy's name and by family. The rotation is read from
the attention-output vectors unless the copy's weight report says they carry no edit: when the median
first-singular share of its changed attention-output matrices is under 0.5 while that of its changed
down projections is 0.9 or more, the rotation is read from the down projections instead, and the table says
which matrix each mode was read from with both shares beside it.

`hpc/place_round.py --measurements PULL/measurements --directions results/directions --families
results/directions/families.json --pulls DIR --batches data/batches --weights results/weights --out FILE.md` is the
step a read-out runs after the digest: each new copy of the pulled round is set against the census copies of its
parent, keeping the nearest by median absolute cosine with its family number, and against the parent's per-layer
reference, chosen by the same rotation signature, giving the layer its direction matches best; a parent with no
census copies reads as new, and one with no per-layer copy gives no layer. The same noise rule applies here: a
pulled copy whose own report in its pair folder says its attention-output change carries no edit is read from its
down projections, the census copies likewise from the reports under `--weights`, and the row says which matrix it
was read from. A partner at a median of 0.9999 or more comes with a reading of the pin
records' weight-file checksums, the same files, different files or an overlap, so a re-upload and a second pass of
one tool are told apart before any byte is read.

`hpc/mode_sizes.py --modes results/directions/modes.json --weights results/weights --out FILE.md` sets each
copy's mode beside the size figures of its weight report (changed tensors and layers, the median and largest
relative difference over the changed tensors, the smallest first-singular energy share, the edited window as a
fraction of the parent's depth) and writes the medians with quartiles per mode with the count of copies reaching
the last layer, the copies whose share crosses their mode's line by name, the same figures per parent and the
per-copy rows. After the pull, `direction_cosines.py` and `direction_families.py` are run again so the census
includes the round.

Weight differences alone cannot certify the absence of hidden behavior.
