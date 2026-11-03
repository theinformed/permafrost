# Reading of the Stage 1 and Stage 2 result: EldritchLabs/Mistral-Nemo-Instruct-2407-heretic-noslop-MPOA against p-e-w/Mistral-Nemo-Instruct-2407-heretic-noslop

Measured on Nautilus, round 46 piece 7 (download job 4184047, compare jobs 4184048 to 4184055 for the round's eight
pieces, sweep job 4184056; the pull, card 5854, carries the measurements and the sweep record and no job log, so the
node and the seconds are not recorded). Modified revision `f43ce1c4`, created on 2026-03-05 at 06:30 and last
revised on 03-06 at 04:07; the maker's Mag-Mell copy (pair 5) followed two hours and thirty-seven minutes after the
creation. Parent pinned at `8e9a40f6` (2026-01-11), p-e-w's Heretic "noslop" pass of Mistral Nemo Instruct 2407,
whose `base_model` field names mistralai/Mistral-Nemo-Base-2407. The batch note calls the parent a measured edit;
round 28's batch pinned it against Mistral's instruct checkpoint, but no report of it is in `results/weights/`, so
the parent is not a measured copy and its own edit is not separated here. The copy is an edit of an edit. Its own
card was not read in this pass. The parent counts as neither an original nor a copy (finding 117).

## Weights (Stage 2)

The tool's assessment was a match to `single-projection`, 0 flags, with the same assessment and nearest recipe on
the cluster and after re-scoring at home; all four entries match. On reading, the second pass is one direction on
both writers of every layer, at the sizes of the maker's Mag-Mell pass.

- 80 of 363 tensors changed: the attention outputs and down projections of all 40 layers. The queries, keys,
  values, gates and up projections, the embedding, the 81 norms and the one other tensor are exactly 0. The largest
  change outside the changed set is 0.
- Relative changes: attention outputs 0.0156 to 0.0216, median 0.0179; down projections 0.0156 to 0.0187, median
  0.0167.
- One direction: 0.9997 to the group at the median on both writers (0.9987 and 0.9986 at the least); between layers
  0.99939 at the median (0.99728 at the least); the two writers of a layer at 0.999997.
- First shares 0.9901 to 0.9945, every one above the 0.99 floor. No changed matrix keeps its row norms (0 of 80),
  under a name that says MPOA.
- Every tensor pairs by name: none on one side only, no unused shared projection, no dropped tower or statistic.

| Kind | Changed | Layers | Exactly 0 | Relative change, least | Median | Most |
| --- | --- | --- | --- | --- | --- | --- |
| attention output | 40 of 40 | 0 to 39 | 0 | 0.0156 | 0.0179 | 0.0216 |
| down projection | 40 of 40 | 0 to 39 | 0 | 0.0156 | 0.0167 | 0.0187 |
| query, key, value | 0 of 120 | none | 120 | - | - | - |
| gate, up | 0 of 80 | none | 80 | - | - | - |

| Direction group | Matrices | Median cosine to the group | Least |
| --- | --- | --- | --- |
| attention outputs, width 5,120 | 40 | 0.9997 | 0.9987 |
| down projections, width 5,120 | 40 | 0.9997 | 0.9986 |
| between layers | 80 | 0.99939 | 0.99728 |

Against the maker's Mag-Mell pass (pair 5). The relative changes agree matrix by matrix, the ratio 1.0009 at the
median and 0.92 to 1.07, on two parents whose matrices have the same norms at the median (64.06 here, 63.80 on
Mag-Mell). The directions stand at 0.840 on the output side on all 80 shared names, 0.839 to 0.840 on every layer,
and 0.842 on the input side: one setting of size, a direction found again on each parent. To Naphula's Mag-Mell
pass (pair 6) the directions stand at 0.839.

Against other passes on Nemo Instruct. On the output side the copy stands at 0.640 at the median to grimjim's
extensive abliteration of Nemo Instruct on 70 shared names (0.34 to 0.93) and at 0.458 to 0xA50C1A1's Heretic pass
(finding 133) on 63. Whether its direction agrees with p-e-w's noslop direction under it waits on a measurement of
the parent against Mistral's checkpoint, which would also show what the second pass touched that the first left.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, 1 difference: the copy ships no chat template where the
parent carries Nemo's (`{%- if messages[0]["role"] == "system" %}` ...). With the template absent on one side, the
fixed conversation is not compared. No version string differs.

## For the recipe library

A template dropped by an edit of an edit is a token-side change the metadata tool reads as unexplained, correctly.
The parent's own measurement against mistralai/Mistral-Nemo-Instruct-2407 is owed to the pinner, from round 28's
pairing. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus46/measurements/pair-7/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
