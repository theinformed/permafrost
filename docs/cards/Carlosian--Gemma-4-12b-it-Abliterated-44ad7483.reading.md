# Reading of the Stage 1 and Stage 2 result: Carlosian/Gemma-4-12b-it-Abliterated against google/gemma-4-12B-it (2026-11-01)

Measured on Blueback, round 22 piece 6. The pull carries the measurements and the sweep record and no job log.
Modified revision `d8f9cc80` (eight commits from 2026-06-28 to 07-20: the weights at 05:18Z on 06-28 under the
title "cleancone2 bf16 weights", then six README commits that add a card, an audit of residual refusals on 200
prompts, benchmark results and the citations), original pinned at `5926caa4` (06-04), the revision current when
the repository was created. The card describes a biprojected clean-cone abliteration in the lineage of the Nous
Research `llm-abliteration` toolkit: a refusal direction biprojected against a `target_retain` control set,
removal as a clean cone with K = 4, a residual-stream band of layers 14 to 34 with the primary direction near
layer 24, cone rank 2, a flat rotation of alpha 1.0. The `base_model` field names the original in lower case.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 48 flags, on the
cluster and after re-scoring at home: 42 first shares of 0.59 to 0.91 and six within-layer cosines of 0.84 to 0.95.
On reading, the copy is the card's band with two directions per matrix, the "cone rank 2" of the card, and rows
restored to the original's magnitudes.

- 42 of 677 tensors changed: the attention output and the down projection of layers 14 to 34, the card's band.
  Nothing else moved; the largest relative change outside the changed set is exactly 0 and 635 tensors equal the
  original.
- Two directions per matrix: the first share is 0.63 to 0.87 on the attention outputs and 0.59 to 0.91 on the
  down projections, and the fourth cumulative share 0.986 to 0.995 everywhere. The first two directions carry the
  change; what is left after them is the bfloat16 floor. Within a layer the two writers' leading directions agree
  at 0.84 to 0.996, across layers at a median of 0.54.
- Mixed sides along the leading direction: the left kept fraction is 0.07 to 0.95 on the attention outputs and
  0.008 to 0.71 on the down projections, the right 0.46 to 0.83 and 0.23 to 0.84, the left below the right on 12
  of 21 and 17 of 21. A rank-two edit has no single side to read along one direction.
- Rows moved by 0.0001 to 0.0005 on all 42: restored, as the toolkit's norm-preserving variants do.
- Relative change 0.022 to 0.034 on the attention outputs and 0.021 to 0.030 on the down projections.

| Layer | Attention output: change, E1, E4, left kept, right kept | Down projection: change, E1, E4, left kept, right kept | Within-layer cosine | Row norms |
| --- | --- | --- | --- | --- |
| 14 | 0.0270, 0.872, 0.986, 0.789, 0.828 | 0.0210, 0.910, 0.991, 0.485, 0.839 | 0.996 | 0.0002, 0.0003 |
| 16 | 0.0260, 0.712, 0.995, 0.855, 0.719 | 0.0249, 0.671, 0.995, 0.061, 0.630 | 0.95 | 0.0003, 0.0002 |
| 20 | 0.0255, 0.786, 0.995, 0.950, 0.463 | 0.0246, 0.748, 0.995, 0.700, 0.392 | 0.99 | 0.0003, 0.0003 |
| 24 | 0.0227, 0.715, 0.992, 0.344, 0.615 | 0.0263, 0.710, 0.994, 0.322, 0.459 | 0.97 | 0.0003, 0.0001 |
| 28 | 0.0243, 0.655, 0.992, 0.407, 0.562 | 0.0262, 0.640, 0.993, 0.280, 0.374 | 0.84 | 0.0003, 0.0005 |
| 31 | 0.0247, 0.650, 0.992, 0.135, 0.597 | 0.0247, 0.658, 0.992, 0.429, 0.502 | 0.93 | 0.0002, 0.0001 |
| 34 | 0.0239, 0.647, 0.992, 0.668, 0.503 | 0.0241, 0.593, 0.992, 0.101, 0.228 | 0.95 | 0.0002, 0.0001 |

The full table (42 rows) is in the report.

The fingerprint shares no measured field with the seventeen earlier reports on this original.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster; "consistent with re-save noted" at home. Under transformers 5.22.1 the
12B family's six fields (finding 39) close by tool, the four omitted defaults by the default rule and the two
sub-configuration data types by the data-type rule, and what remains is the version strings (5.10.0.dev0 to
5.12.1). The template is Google's pinned file and the fixed conversation renders identically.

## For the recipe library

A rank-two edit on both writers of a stated band, rows restored: the shape finding 27 read on AEON-7's 12B copy
(four directions) at a lower rank, and the second copy on this base from the Nous toolkit's lineage. No entry
reads a fixed rank above one; a `cone-rank-k` entry that reads the fourth cumulative share against 0.99 and sets
no side would count no flag here. The pull copy keeps the direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/blueback22/measurements/pair-6/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
