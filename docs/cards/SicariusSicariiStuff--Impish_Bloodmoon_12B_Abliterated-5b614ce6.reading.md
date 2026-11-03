# Reading of the Stage 1 and Stage 2 result: SicariusSicariiStuff/Impish_Bloodmoon_12B_Abliterated against SicariusSicariiStuff/Impish_Bloodmoon_12B

Measured on Nautilus, round 46 piece 8 (download job 4184047, compare jobs 4184048 to 4184055 for the round's eight
pieces, sweep job 4184056; the pull, card 5854, carries the measurements and the sweep record and no job log, so the
node and the seconds are not recorded). Modified revision `06527e1a`, created on 2026-02-05 at 10:44 and last
revised on 02-10 at 04:48. Parent pinned at `e9d665ad` (2025-12-30), the maker's own Impish Bloodmoon 12B, a
fine-tune whose field names mistralai/Mistral-Nemo-Instruct-2407; it is new to the census. One maker's fine-tune and
the same maker's edit of it. The copy's own card was not read in this pass. The parent counts as neither an
original nor a copy (finding 117).

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 15 flags (first shares of 0.754 to
0.989 under the 0.99 floor, on the attention outputs of layers 15 to 18 and 30 to 32 and the down projections of 29
to 36), with the same assessment and nearest recipe on the cluster and after re-scoring at home.
`single-projection-selected` reads 42, `directional-per-layer` 66 and `single-projection` 93. On reading, the copy is
a per-layer pass in two kernels' shapes, one rising and falling on the attention outputs, one rising to the last
layer on the down projections.

- 29 of 363 tensors changed: the attention outputs of layers 15 to 32 and the down projections of 29 to 39; layers
  29 to 32 carry both. The queries, keys, values, gates and up projections of all 40 layers, the attention outputs
  of 0 to 14 and 33 to 39, the down projections of 0 to 28, the embedding and the 81 norms are exactly 0. The
  largest change outside the changed set is 0.
- Relative changes: attention outputs 0.0017 to 0.0515, median 0.0218, rising from 0.0017 at layer 15 to 0.0515 at
  layer 24 and falling to 0.0034 at 32; down projections 0.0029 at layer 29 rising to 0.0194 at 39, median 0.0114.
- One direction per layer, turning across the stack: between layers 0.5581 at the median and 0.0374 at the least;
  the two writers of the four shared layers at 0.9958 or better. To the group's direction the attention outputs
  stand at 0.8333 at the median (0.3502 at the least) and the down projections at 0.9165 (0.5583).
- First shares 0.7539 to 0.9990; the lowest is the layer 15 attention output, the smallest change of the 29. No
  changed matrix keeps its row norms (0 of 29).
- Every tensor pairs by name: none on one side only, no unused shared projection, no dropped tower or statistic.

| Kind | Changed | Layers | Exactly 0 | Relative change, least | Median | Most |
| --- | --- | --- | --- | --- | --- | --- |
| attention output | 18 of 40 | 15 to 32 | 22 | 0.0017 | 0.0218 | 0.0515 |
| down projection | 11 of 40 | 29 to 39 | 29 | 0.0029 | 0.0114 | 0.0194 |
| query, key, value | 0 of 120 | none | 120 | - | - | - |
| gate, up | 0 of 80 | none | 80 | - | - | - |

| Direction group | Matrices | Median cosine to the group | Least |
| --- | --- | --- | --- |
| attention outputs, width 5,120 | 18 | 0.8333 | 0.3502 |
| down projections, width 5,120 | 11 | 0.9165 | 0.5583 |
| between layers | 29 | 0.5581 | 0.0374 |

Against other Nemo measurements. On the output side the copy stands at 0.281 at the median to grimjim's
abliteration of Nemo Instruct (27 shared names), 0.195 to 0xA50C1A1's Heretic pass of it (finding 133, 29 names),
and 0.256 and 0.260 to EldritchLabs's and Naphula's passes of this round (pairs 7 and 6). The maker's training sits
between this edit and Nemo Instruct, and on Nemo the direction follows the fine-tune as much as the base (finding
123).

The shape is that of a Heretic per-layer pass: an attention kernel peaking at layer 24 with its tails under 0.004,
a down kernel still rising at the last layer, and a direction that changes from layer to layer. The copy's name says abliterated; the card's
method is not read here.

## Token and configuration side (Stage 1)

"Consistent" on the cluster and at home, 1 difference: `config._name_or_path`, naming the parent, is dropped
(expected). The fixed conversation renders the same with the `default` template.

## For the recipe library

`directional-per-layer-selected` reads the pass with first-share flags on its tails, where the changes are 0.0017 to
0.0134 of the norm. The kernel heights and reaches would read against a card table once the card is read. The
direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus46/measurements/pair-8/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
