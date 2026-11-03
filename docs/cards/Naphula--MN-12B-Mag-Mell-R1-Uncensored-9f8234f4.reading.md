# Reading of the Stage 1 and Stage 2 result: Naphula/MN-12B-Mag-Mell-R1-Uncensored against inflatebot/MN-12B-Mag-Mell-R1

Measured on Nautilus, round 46 piece 6 (download job 4184047, compare jobs 4184048 to 4184055 for the round's eight
pieces, sweep job 4184056; the pull, card 5854, carries the measurements and the sweep record and no job log, so the
node and the seconds are not recorded). Modified revision `4987a8f5`, last revised on 2026-05-25 at 08:11; the
repository was created on 2025-12-02 at 03:57. Parent pinned at `b5f9f348` (2025-04-03), the last commit before
the repository was created and the revision pair 5 is measured against. inflatebot's Mag-Mell R1 is a merge of six
Mistral Nemo fine-tunes over IntervitensInc's ChatML re-save of Nemo Base 2407 (pair 5's note names them). Naphula's
two Gemma 2 copies read as one direction projected out of both writers at a flat 1.5 (findings 150 and 161). The
copy's own card was not read in this pass. The parent counts as neither an original nor a copy (finding 117).

## Weights (Stage 2)

The tool's assessment was a match to `single-projection`, 0 flags, with the same assessment and nearest recipe on
the cluster and after re-scoring at home; all four entries match. On reading, the copy is one direction on both
writers of every layer, the same direction to the sixth decimal on all 80, the maker's form on a third family.

- 80 of 363 tensors changed: the attention outputs and down projections of all 40 layers. The queries, keys,
  values, gates and up projections, the embedding, the 81 norms and the one other tensor are exactly 0. The largest
  change outside the changed set is 0.
- Relative changes: attention outputs 0.0191 to 0.0268, median 0.0222, highest at layer 0; down projections 0.0193
  to 0.0224, median 0.0208.
- One direction: 1.0000 to the group at the median and at the least on both writers; between layers 0.9999988 at
  the median (0.999995 at the least); the two writers of a layer at 0.999998.
- First shares 0.9934 to 0.9965, every one above the 0.99 floor. No changed matrix keeps its row norms (0 of 80).
- Every tensor pairs by name: none on one side only, no unused shared projection, no dropped tower or statistic.

| Kind | Changed | Layers | Exactly 0 | Relative change, least | Median | Most |
| --- | --- | --- | --- | --- | --- | --- |
| attention output | 40 of 40 | 0 to 39 | 0 | 0.0191 | 0.0222 | 0.0268 |
| down projection | 40 of 40 | 0 to 39 | 0 | 0.0193 | 0.0208 | 0.0224 |
| query, key, value | 0 of 120 | none | 120 | - | - | - |
| gate, up | 0 of 80 | none | 80 | - | - | - |

| Direction group | Matrices | Median cosine to the group | Least |
| --- | --- | --- | --- |
| attention outputs, width 5,120 | 40 | 1.0000 | 1.0000 |
| down projections, width 5,120 | 40 | 1.0000 | 1.0000 |
| between layers | 80 | 0.9999988 | 0.999995 |

Against EldritchLabs's edit of the same parent (pair 5), whose card names this one. The saved vectors stand at
0.9997 at the median on the output side on all 80 shared names (0.9990 at the least) and at 0.9982 on the input
side (0.9834). This copy's difference norms are 1.24 times pair 5's at the median (1.15 to 1.30 matrix by matrix),
on the same profile across layers. Against EldritchLabs's pass of p-e-w's Nemo Instruct edit (pair 7) it stands at
0.839 on the output side, and at 0.406 to 0xA50C1A1's Heretic pass of Nemo Instruct (finding 133) on 63 shared
names. The measured revision is five months after the repository was created and eleven weeks after pair 5, so
whether an earlier revision carried a different size is not read here.

The maker's Gemma 2 projections moved both writers of 42 and of 26 layers with one direction at 0.9996 between the
two parents (finding 161). This pass keeps that form on Mistral Nemo: every layer, one direction, the relative
changes within 0.019 to 0.027 and no layer left out.

## Token and configuration side (Stage 1)

"Undecided" on the cluster and at home: no compared field differs, and the generation file is missing on both
sides, the missing evidence the tool names. The fixed conversation renders the same with the `default` template.

## For the recipe library

`single-projection` reads the pass cleanly, as it read the maker's Gemma 2 projections. The flat weight read on
those (1.5) is not read on this pass in this note; the comparison with pair 5 gives only the ratio of the two
copies' sizes. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus46/measurements/pair-6/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
