# Reading of the Stage 1 and Stage 2 result: huihui-ai/Huihui-gemma-4-31B-it-abliterated against google/gemma-4-31B-it (2026-11-01)

Measured on Blueback, round 22 piece 1. The pull carries the measurements and the sweep record and no job log, so
the job numbers and the compare seconds are not recorded here. Modified revision `2abf02b3` (five commits from
2026-04-09 15:13Z to 04-10: the weights by the large-folder tool at 03:05Z on 04-10, a README created and twice
updated), original pinned at `419b2efe` (04-02), the revision current when the repository was created. This is the
first version of the maker's 31B edit, the one the second version's card (round 12) compares itself with by
perplexity. The card says the refusal direction was removed with the maker's remove-refusals script and that both
thinking modes were abliterated; it names no layer window and no weight. The `base_model` field names the original.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection`, 52 flags, on the cluster and
after re-scoring at home: 52 first shares of 0.989 to 0.990, the bfloat16 floor of finding 3 on edits that move a
matrix by 1.2 to 1.6 percent. On reading, the copy is the maker's shared projection at weight 1.00 on every residual
writer of all 60 layers.

- 120 of 1,188 tensors changed: the attention output and the down projection of every layer. The queries, keys,
  values, gates, up projections, every normalisation vector and the embedding are unchanged; the largest relative
  change outside the changed set is exactly 0 and 1,068 tensors equal the original.
- One direction for the whole model: every changed matrix's leading direction agrees with the group's at 0.99998 or
  better, and the attention outputs' direction agrees with the down projections' at 0.99997.
- Weight 1.00 on the output side: the left kept fraction is 0.002 to 0.008 on the 60 attention outputs and -0.001
  to 0.007 on the 60 down projections, the right 0.51 to 0.97 and 0.30 to 0.98, the left below the right on 120 of
  120.
- First share 0.989 to 0.993, relative change 0.0122 to 0.0162, the floor case exactly: the leftover outside the
  first direction is 0.0013 to 0.0014 of each weight's norm.
- Rows moved by 0.003 to 0.118 on the attention outputs (layer 4) and 0.003 to 0.362 on the down projections
  (layer 59), unrestored.

| Layer | Attention output: change, E1, left kept, right kept | Down projection: change, E1, left kept, right kept | Row norms |
| --- | --- | --- | --- |
| 0 | 0.0122, 0.989, 0.004, 0.967 | 0.0134, 0.990, 0.006, 0.886 | 0.022, 0.013 |
| 4 | 0.0135, 0.990, 0.005, 0.860 | 0.0140, 0.991, 0.006, 0.968 | 0.118, 0.054 |
| 14 | 0.0136, 0.990, 0.006, 0.952 | 0.0160, 0.993, -0.001, 0.982 | 0.031, 0.070 |
| 20 | 0.0156, 0.992, 0.008, 0.967 | 0.0135, 0.990, 0.006, 0.653 | 0.028, 0.015 |
| 33 | 0.0162, 0.993, 0.005, 0.630 | 0.0162, 0.993, 0.004, 0.494 | 0.035, 0.033 |
| 43 | 0.0134, 0.990, 0.006, 0.576 | 0.0131, 0.989, 0.006, 0.302 | 0.019, 0.003 |
| 52 | 0.0127, 0.989, 0.006, 0.729 | 0.0127, 0.989, 0.006, 0.399 | 0.003, 0.030 |
| 59 | 0.0126, 0.989, 0.006, 0.825 | 0.0128, 0.989, 0.005, 0.667 | 0.012, 0.362 |

The full table (120 rows) is in the report.

Every measured field of all 1,188 tensors equals the round 18 report of prithivMLmods/gemma-4-31B-it-Uncensored-MAX
(`results/weights/prithivMLmods-gemma-4-31B-it-Uncensored-MAX.json`), whose card says it is this copy re-sharded
with no change to the weights and whose weights went up 77 minutes after these. The two repositories share no
checksum (this copy's two shards `741dc1f95d` and `57bf0f7f1f` against the re-upload's ten), which is what a
re-save gives; the fields are what the weights give. Finding 9's open case on the 31B closes: the maker's own file
reads weight 1.00 on all 60 layers, as its re-upload did, and against the second version (round 12, weight 1.5 on
layers 5 to 59) no field is equal. The fingerprint shares nothing else with the twelve earlier reports on this
original: TrevorJS's and ressl's copies change the same 120 matrices and no field agrees.

## Token and configuration side (Stage 1)

"Consistent" on the cluster and at home: every configuration, generation and token field equals the original's,
the version strings included (5.5.0.dev0 on both sides). The template is Google's pinned file and the fixed
conversation renders identically.

## For the recipe library

The `single-projection` entry fits this copy in every respect but the 0.99 first-share line, which the bfloat16
floor crosses on 52 of 120 matrices at this edit size; the leftover line of finding 3 (0.0025 of the weight norm)
would count none. This is the eighth weight the maker's script has read on a Gemma or Mistral base and the second
at exactly 1.00 on the 31B (finding 21). The pull copy keeps the direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/blueback22/measurements/pair-1/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
