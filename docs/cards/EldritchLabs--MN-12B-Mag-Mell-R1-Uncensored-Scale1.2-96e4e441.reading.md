# Reading of the Stage 1 and Stage 2 result: EldritchLabs/MN-12B-Mag-Mell-R1-Uncensored-Scale1.2 against inflatebot/MN-12B-Mag-Mell-R1

Measured on Nautilus, round 46 piece 5 (download job 4184047, compare jobs 4184048 to 4184055 for the round's eight
pieces, sweep job 4184056; the pull, card 5854, carries the measurements and the sweep record and no job log, so the
node and the seconds are not recorded). Modified revision `d6f3e11a`, created on 2026-03-05 at 09:07 and last
revised at 12:19, two hours and thirty-seven minutes after the maker's Nemo Instruct copy (pair 7). Parent pinned
at `b5f9f348` (2025-04-03). inflatebot's Mag-Mell R1 is a merge whose field lists IntervitensInc's ChatML re-save of
Mistral Nemo Base 2407 and six Nemo fine-tunes (nbeerbower's bophades, wissenschaft and Gutenberg v4, elinas's
Chronos-Gold, Fizzarolli's Sunrose and anthracite-org's magnum v2.5 KTO), 40 layers at a width of 5,120. The batch
note records that the copy's card names Naphula's edit of the same merge (pair 6) while its `base_model` field names
inflatebot's, so the pair is pinned against inflatebot and read beside Naphula's. The copy's own card was not read
in this pass. The parent counts as neither an original nor a copy (finding 117).

## Weights (Stage 2)

The tool's assessment was a match to `single-projection`, 0 flags, with the same assessment and nearest recipe on
the cluster and after re-scoring at home; all four entries match. On reading, the copy is one direction on both
writers of every layer, Naphula's direction at a smaller size.

- 80 of 363 tensors changed: the attention outputs and down projections of all 40 layers. The queries, keys,
  values, gates and up projections, the embedding, the 81 norms and the one other tensor are exactly 0. The largest
  change outside the changed set is 0.
- Relative changes: attention outputs 0.0154 to 0.0215, median 0.0182, highest at layer 0; down projections 0.0155
  to 0.0182, median 0.0167.
- One direction: 0.9998 to the group at the median on both writers (0.9990 at the least); between layers 0.99957 at
  the median (0.99770 at the least); the two writers of a layer at 0.999997.
- First shares 0.9901 to 0.9945, every one above the 0.99 floor. No changed matrix keeps its row norms (0 of 80).
- Every tensor pairs by name: none on one side only, no unused shared projection, no dropped tower or statistic.

| Kind | Changed | Layers | Exactly 0 | Relative change, least | Median | Most |
| --- | --- | --- | --- | --- | --- | --- |
| attention output | 40 of 40 | 0 to 39 | 0 | 0.0154 | 0.0182 | 0.0215 |
| down projection | 40 of 40 | 0 to 39 | 0 | 0.0155 | 0.0167 | 0.0182 |
| query, key, value | 0 of 120 | none | 120 | - | - | - |
| gate, up | 0 of 80 | none | 80 | - | - | - |

| Direction group | Matrices | Median cosine to the group | Least |
| --- | --- | --- | --- |
| attention outputs, width 5,120 | 40 | 0.9998 | 0.9990 |
| down projections, width 5,120 | 40 | 0.9998 | 0.9990 |
| between layers | 80 | 0.99957 | 0.99770 |

Against Naphula's edit of the same parent (pair 6). The saved vectors stand at 0.9997 at the median on the output
side on all 80 shared names (0.9990 at the least) and at 0.9982 on the input side (0.9834). Naphula's changes are
the larger: its difference norms are 1.24 times this copy's at the median, 1.15 to 1.30 matrix by matrix (1.23 on
the attention outputs, 1.24 on the down projections), and its relative changes run 0.0191 to 0.0268 against 0.0154
to 0.0215. The profile across layers is the same on both, highest on the layer 0 attention output and on the
attention outputs of layers 15, 18, 23 and 28. The 1.2 in this copy's name is the size of the measured ratio, with
this copy the smaller of the two. Naphula's measured revision (`4987a8f5`, 2026-05-25) is later than this copy, so
which revision the card names is not read here.

Against the maker's other pass (pair 7, on p-e-w's Nemo Instruct edit), the relative changes agree layer by layer
(the ratio 1.0009 at the median, 0.92 to 1.07) and the directions stand at 0.840 on the output side on all 80
(0.839 to 0.840) and 0.842 on the input side. To 0xA50C1A1's Heretic pass of Nemo Instruct (finding 133) they stand
at 0.403 on 63 shared names.

## Token and configuration side (Stage 1)

"Undecided" on the cluster and at home: no compared field differs, and the generation file is missing on both
sides, the missing evidence the tool names. The fixed conversation renders the same with the `default` template.

## For the recipe library

`single-projection` reads this pass and Naphula's as one form. A scale read between two copies on one parent, the
ratio of their difference norms along a shared direction, is the line the library lacks for a copy that names
another copy as its source. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus46/measurements/pair-5/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
