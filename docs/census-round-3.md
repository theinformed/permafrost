# Census round 3: the second pass of round 2's five pairs (2026-10-30)

Round 2's five pairs were measured a second time on Nautilus on 2026-10-29 and 30 (card 5055; download job 4080809,
then comparisons 4080810, 4080811, 4080812, 4080814 and 4080815 for pairs 1 to 5, all exit 0) with the comparison as
of commit d0f48bb. The round reused round 2's pins without a new batch file. The census row and the metadata report of
each measurement carry the same modified and original revisions as round 2's pinned batch of pairs, the run records
name round 2's input paths, and the shard checksums in every second-pass report equal the first pass's. The pass added
the measures round 2 asked for. Every changed matrix now records how much of the original's action the copy keeps
along each of its eight leading directions (a projection of weight a leaves 1 − a, so 0 is a plain ablation, −0.5 a
weight of 1.5, −1 a reflection, and 1 an untouched direction). The packed three-dimensional expert tensors are
measured one expert at a time, with the worst expert's energy share standing for the tensor and the experts' median
directions saved as its vectors, and the per-layer direction rule reads those saved vectors. The five second-pass
measurements were pulled to `/opt/ai/hpc-packages/pulls/model-audit/nautilus3/measurements/pair-1` to `pair-5` and
re-scored at home with the recipe table as committed today; the reports are
`results/weights/<maker>-<name>.pass-2.json` and `results/meta/<maker>-<name>.pass-2.json` beside the first pass's
files, and each pair's reading note in `docs/cards/` carries a dated second-pass section. The direction files were
never committed (`*.safetensors` is ignored), so they stay in the pull copies.

| Pair | Copy | First pass, as scored | Second pass, as scored | What the new measures add |
| --- | --- | --- | --- | --- |
| 1 | wangzhang/gemma-4-31B-it-abliterated | violations, 10 flags, nearest `directional-per-layer-selected` | the same 10 flags, every measure equal | weight 2.75 to 3.78 on the attention outputs in a smooth arc over layers 18 to 57; 0.8 to 5.6 on query and key, 0.8 to 1.4 on value; the row norms, restored, show none of it |
| 2 | mlabonne/gemma-3-27b-it-abliterated | match, 0 flags, `single-projection` | match, 0 flags, every measure equal | weight 1.50 within 0.01 on all 124 matrices, the card's 1.5 read from the weights |
| 3 | llmfan46/gemma-4-E4B-it-uncensored-heretic | violations, 11 flags, nearest `directional-per-layer-selected` | the same 11 flags, every measure equal | one direction on the input side of each attention output at weight 1.27 to 1.79, plus a tail of weak directions holding 4 to 8 percent of the energy |
| 4 | TrevorJS/gemma-4-26B-A4B-it-uncensored | violations, 64 flags, nearest `directional-per-layer` | 31 flags, dense measures equal; the 30 packed expert tensors now measured | all 128 experts per layer share one output direction (cosine 0.996 to 0.999); layers 10 and 12 clear 0.95 (0.991, 0.995); scale 1.0 read as 0.05 to 0.14 remaining |
| 5 | byroneverson/Mistral-Small-Instruct-2409-abliterated | violations, 48 flags, nearest `directional-per-layer-selected` | the same 48 flags, every measure equal | weight 0.05 to 11.1 by layer, the notebook's 2.0 times a direction length that was never 1; embedding and layer 24 patched at the same 3.09 |

Both passes agree on every measure they share. Relative changes, difference norms, energy shares, row norms and
within-layer direction cosines are equal to the last digit on all 6,085 matched tensors of the five pairs, as two
runs of the same deterministic sketch on the same bytes should be. Two numbers moved for reasons that are rule
changes between the kits: pair 1's two key projections in layers 35 and 41 form a group of two, and the comparison
now reports the angle between the pair (0.022) where the October kit reported each vector's angle from their mean
(0.715; 2 × 0.715² − 1 = 0.022); pair 4's layer cosines changed where the experts' median direction joined the layer
group. No assessment and no nearest entry changed on pairs 1, 2, 3 and 5; pair 4 dropped from 64 flags to 31 because
its 30 packed tensors are now measured.

## The new measures, pair by pair

The remaining fraction is clean on one side of a rank-one edit and mixed on the other. For an edit on the output
side (the residual writers' usual case) the fraction along the leading left vector is 1 − a exactly and the fraction
along the right vector is at least that; for an edit on the input side the roles swap. The order of the two fractions
therefore tells the side: the left is below the right on all 124 matrices of pair 2, all 60 dense matrices of pair 4,
49 of 50 of pair 5 (the exception is the embedding, whose residual coordinates are its columns) and the 40 attention
outputs of pair 1, and the left is above the right on pair 1's 54 query, key and value edits and on all 11 of
pair 3.

Pair 2 is the check. The card says weight 1.5; along the leading output direction every one of the 124 matrices
keeps −0.497 (band −0.507 to −0.491), and along the second to eighth directions 0.998 to 1.004. The measure reads
a declared weight to two decimals on its first use.

Pair 3 (arbitrary rank) is what the pass was for. On each of the 11 attention outputs the leading direction sits on
the input side, in the coordinates of the concatenated head outputs: the input-side fraction is −0.27 to −0.79
(weights 1.27 to 1.79, median 1.46) and the output-side fraction 0.29 to 0.92. Along the second to eighth directions
the copy keeps 0.90 to 1.03 (median 0.986), weights under about 0.1 each; the first value holds 0.920 to 0.960 of
the energy and the first eight 0.935 to 0.975, so 2.5 to 6.5 percent lies beyond the eighth direction at relative
changes of 0.02 to 0.05, where rounding alone would leave 0.999 by the second value. The method is one
over-projected direction per layer, its weight searched (between a plain ablation and a reflection on every matrix),
with a many-direction tail of small weights. The table of all 11 layers is in the pair's reading note.

Pair 4 (packed experts) resolves. The 30 packed tensors hold 128 experts each, all changed, each expert's relative
change 0.015 to 0.051 with per-layer medians of 0.018 to 0.022, the dense band. Within a layer the experts' leading
output directions agree at median cosine 0.996 to 0.999 (minimum 0.940), the card's one modification on all 128,
and their input directions are unrelated (0.07 to 0.08), as each expert has its own input space. The median expert's
first-value energy share is 0.989 to 0.994 in every layer; the worst expert's is 0.881, 0.951, 0.969 and 0.973 in
layers 0, 2, 1 and 17 and 0.979 to 0.990 elsewhere, and since the scorer takes the worst expert those are the 30
flags that remain. With the experts' median direction as a third member in each layer group, layers 10 and 12 read
0.991 and 0.995 (minima 0.962 and 0.970) against 0.941 and 0.947 as a pair, and 29 of the 30 layers clear the 0.95
line; layer 29 sits at 0.949 and is the one direction flag left. The remaining fraction along the leading output
direction is 0.02 to 0.28 on the attention outputs, −0.001 to 0.51 on the dense down projections and 0.009 to 0.52
on the experts' medians, which is the card's scale 1.0 with the biprojection's input-side term adding to it where
that term is comparable (layer 29's experts 0.52, layer 26's down projection 0.51). Row norms per expert row move
by at most 0.00118.

Pair 1 reads a weight the row norms hid. Along each attention output's leading direction the copy keeps −1.75
(layer 18) to −2.78 (layers 37 and 38) to −1.77 (layer 57): weights 2.75 to 3.78 in a smooth arc. The reading side
peaks higher: query at weight 5.6 in layer 41, key at 5.6 in layer 36, value at 1.4 in layer 48, each in its own
arc. The first pass read the row-norm change at 0.0008 on these matrices, which the norm-preserving step
guarantees whatever the weight; the remaining fraction is the only reading of the strength the weights give, and the
card gives no number for it.

Pair 5 reads the notebook's amount per matrix, and it is 2.0 on none of them. Along the leading output direction
the 49 writers keep 0.95 (layer 9's down projection, relative change 0.0012) to −10.1 (layer 50's, 0.21): weights
0.05 to 11.1, rising with the edit; the ratio of relative change to weight is 0.0155 to 0.042 on all 49, each
matrix's own share along its direction, so the weight is what varies. A weight of 2.0 on a unit direction reads −1
everywhere; the direction's length was not 1, and the applied weight is 2 × |d|² with |d|² from 0.02 to 5.6 by layer,
which is also why the early-layer entries fell below threshold in the first pass. The embedding keeps −2.0854 along
its leading input direction and layer 24's down projection −2.0853 along its output direction: the same vector at
the same weight, 3.09, on both, the notebook's layer 25.

## The token side

The cluster's cards read pair 1 and pair 3 "unexplained differences" on two fields each
(`config.text_config.moe_intermediate_size` and `template.default`), pairs 2 and 4 "consistent with re-save noted"
and pair 5 "consistent". The first pass closed all five at home. The two that regressed did so on the cluster for
two reasons that are properties of where the card is written, and neither is a change in the copies:

- The compare job writes the card on a compute node without network access (`hpc/rounds/2/measure.py` runs the
  document comparison alone and never calls the hub), so the rule that explains a template equal to one the original
  repository published later cannot read that repository's commits there.
- The rule that explains an added configuration field by the library's default asks the installed transformers for
  the model type's configuration class. The kit pins transformers 4.56.2 (`compute-requirements.txt`), whose models
  directory has `gemma3` and `gemma3n` and no `gemma4`, so for the two Gemma 4 copies the rule has nothing to ask and
  the null `moe_intermediate_size` stays unexplained. Pair 2 is Gemma 3, which 4.56.2 knows, so its twenty added
  fields close on the cluster; pair 4 is Gemma 4 but has no such field difference.

Re-judged at home under transformers 5.6.2 with the original repositories' histories, the same two reports read
"consistent with re-save noted" on the same commits as the first pass (`145dc250` for pair 1, `c53e9d33` for pair 3),
and the other three are unchanged. The re-judged reports are the `results/meta/*.pass-2.json` files, each keeping the
cluster's reading in its `reclassification` block. A cluster card for a Gemma 4 copy will keep reading this way until
the kit's pins move past 4.56.2 or the card is re-judged at home as a matter of course.

## What it means for the entries

Arbitrary rank. The entry can be written from pair 3's numbers as a candidate, with a run of our own to calibrate it
before it enters the table: attention outputs in a selected set of layers, one matrix per layer (so no within-layer
direction term); first-value energy share at least 0.90 (measured 0.920 to 0.960); energy in the first eight values
between 0.93 and 0.98 at relative change above 0.02, the signature that separates it from a rank-one edit under the
rounding floor; a remaining fraction along the leading direction between −1 and 0 on one side (measured −0.79 to
−0.27), the tail directions keeping at least 0.89; everything outside the changed set within 0.001 (measured
0.00008); no row-norm limit (0.0016 to 0.0165). The library's runner records that the pinned public release 1.3.0
has no arbitrary-rank search, and the card names release 1.2.0, so the calibration run needs that release.

Packed experts in the per-layer entries. The scorer measures them now; what the line needs is a decision on the
worst expert. Pair 4's median expert sits at 0.989 to 0.994 in every layer and its worst at 0.881 to 0.990, so a
0.99 line on the worst expert flags all 30 and a 0.985 line on the median flags none. The candidate: median-expert
share at least 0.985 with the worst expert reported, the experts' output directions agreeing within a layer at 0.94
or better (measured minimum 0.940), the experts' median direction joining the layer's dense directions under the
0.95 layer line (29 of 30 pass; layer 29 at 0.949), a remaining fraction along the leading output direction near 0
with the biprojection's second term allowed to about 0.5, and row norms within 0.0015 per expert row (the 0.001
norm-preserving line catches five of pair 4's 30 tensors at 0.00101 to 0.00118). The next comparison should keep
every expert's share rather than the three-number spread, so the worst expert can be read.

The projection weight. The remaining fraction along the leading direction is now a measured field, and a
projection entry can carry a weight band: 1.0 for a plain ablation (pair 4 reads 0.02 to 0.28 on its dense matrices
with the second term), 1.5 for pair 2 (read to 0.01), and the per-layer bands above for pairs 1 and 5. A per-layer
entry should expect the weight to vary smoothly with the layer when the method searches it, as pair 1's arcs do.

## Findings to carry

- The remaining fraction reads a declared projection weight to two decimals: pair 2's 124 matrices all read 1.50
  within 0.01 against the card's 1.5, with directions 2 to 8 untouched within 0.004.
- Norm-preserving edits hide their weight from the row-norm rule and the remaining fraction recovers it: pair 1's
  attention outputs carry weights of 2.75 to 3.78 (past a reflection on every one of the 40 layers) and its query
  and key projections up to 5.6, with row norms within 0.0008; the card names a searched strength and no value.
- A per-layer direction whose length is not 1 turns a fixed amount into a weight that varies two hundredfold:
  pair 5's notebook says 2.0, the weights read 0.05 to 11.1 by layer, and the embedding and layer 24 read the same
  3.09 to four decimals.
- The side of an edit is readable from the order of the two fractions: 273 of 274 output-side matrices in pairs 1,
  2, 4 and 5 put the left fraction below the right, pair 1's 54 reading-side edits and pair 3's 11 put it above.
  Pair 3's leading direction sits on the input side of the attention output, which no entry in the table describes.
- A mixture-of-experts abliteration can be read expert by expert: pair 4's 128 experts per layer share one output
  direction at cosine 0.996 to 0.999, and the experts' direction resolves the two layers (10 and 12) the dense pair
  left at 0.941 and 0.947.
- A card written on a cluster without network access and with a library older than the architecture reads
  "unexplained differences" on fields that close at home; the pinned 4.56.2 has no Gemma 4 class, so every Gemma 4
  copy's card needs the home judgement until the pins move.

Weight differences alone cannot certify the absence of hidden behavior.
