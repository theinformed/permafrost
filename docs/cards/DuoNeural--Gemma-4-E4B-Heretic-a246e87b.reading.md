# Reading of the Stage 1 and Stage 2 result: DuoNeural/Gemma-4-E4B-Heretic against google/gemma-4-E4B-it (2026-11-01)

Measured on Blueback, round 25 piece 3. The pull carries the measurements and the sweep record and no job log.
Modified revision `3e166f79` (three commits on 2026-05-01: a model card and the weights by the large-folder tool
at 22:31Z, two minutes after the repository was created), original pinned at `c53e9d33` (04-28), the revision
current when the repository was created. The card calls the copy an experimental drop made with "Heretic
(arcee-ai)", described as a LoRA-based Pareto sweep over refusal rate and KL divergence: best trial 204, 43
refusals in 100 remaining, KL divergence 0.0750, targets `o_proj` and `down_proj` on 42 layers each, with a
pointer to the maker's other E4B copy for complete removal. The `base_model` field names the original.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection-selected`, 18 flags, on the
cluster and after re-scoring at home: 18 first shares of 0.976 to 0.990 on the attention outputs of layers 10 to
23 and 38 to 41, where the edit is 0.9 to 1.4 percent of the norm. On reading, the copy is one direction shared
across the model, output side, on the down projections of layers 6 to 41 at a flat weight of about 1.4 and on the
attention outputs of layers 10 to 41 at a weight that rises from 0.4 to 0.9 at layer 30 and falls again.

- 68 of 2,076 tensors changed: the down projections of layers 6 to 41 (36) and the attention outputs of 10 to 41
  (32); the card's "42 layers each" is the set the tool searched, not the set it changed. Nothing else moved; the
  largest relative change outside the changed set is exactly 0 and 2,008 tensors equal the original. The 54
  shared-KV tensors are dropped by the export.
- One direction for the whole model: every changed matrix agrees with the group at 0.9999 or better, the two
  kinds at 0.9997, the two writers of a layer at 0.9998 to 1.000.
- Output side on 68 of 68. On the down projections the left kept fraction is -0.363 at layer 6, falling smoothly
  to -0.412 at 29 and back to -0.387 at 41 (weight 1.36 to 1.41), the right -0.04 to 0.84. On the attention outputs
  the left runs 0.61 at layer 10, 0.36 at 20, 0.11 at 30, 0.19 at 34 and 0.37 at 41 (weight 0.39 to 0.89), the
  right 0.69 to 0.95.
- Rank one everywhere: first share 0.976 to 0.993 on the attention outputs and 0.997 to 0.998 on the down
  projections, the floor accounting for the rest.
- Rows moved by 0.003 to 0.007 on the attention outputs and 0.004 to 0.015 on the down projections, unrestored.
- Relative change 0.009 to 0.017 on the attention outputs and 0.026 to 0.036 on the down projections.

| Layer | Attention output: change, E1, left kept, right kept | Down projection: change, E1, left kept, right kept | Within-layer cosine | Row norms |
| --- | --- | --- | --- | --- |
| 6 | - | 0.0268, 0.997, -0.363, 0.468 | - | -, 0.0060 |
| 10 | 0.0088, 0.976, 0.611, 0.948 | 0.0291, 0.997, -0.373, 0.843 | 1.000 | 0.0038, 0.0145 |
| 16 | 0.0121, 0.986, 0.459, 0.815 | 0.0362, 0.998, -0.384, 0.292 | 1.000 | 0.0044, 0.0096 |
| 20 | 0.0138, 0.990, 0.356, 0.869 | 0.0287, 0.997, -0.393, 0.279 | 1.000 | 0.0051, 0.0065 |
| 25 | 0.0154, 0.991, 0.233, 0.787 | 0.0283, 0.997, -0.404, 0.072 | 1.000 | 0.0049, 0.0066 |
| 30 | 0.0175, 0.993, 0.106, 0.778 | 0.0279, 0.997, -0.411, -0.030 | 1.000 | 0.0049, 0.0056 |
| 35 | 0.0158, 0.991, 0.214, 0.697 | 0.0273, 0.997, -0.400, 0.001 | 1.000 | 0.0057, 0.0058 |
| 41 | 0.0127, 0.987, 0.365, 0.739 | 0.0271, 0.997, -0.387, 0.109 | 1.000 | 0.0036, 0.0043 |

The full table (68 rows) is in the report.

The fingerprint shares no measured field with the eleven earlier reports on this original. Its first and last
shards (`aa3e9d1e04`, `8080cb1ab7`) equal OS-Software's and TheUmbraWalker's E4B copies', the library's four-shard
layout of the embeddings and the tail that none of the three edits touches, and its first shard equals
prithivMLmods's E4B re-upload's for the same reason.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, one field. Under transformers 5.22.1
`text_config.moe_intermediate_size` (null in a 5.7.0 save) closes by the default rule. What stays open is a
template the copy does not ship: there is no `chat_template.jinja` and no template in the tokenizer
configuration, so the tool records "chat template missing" and the field reads Google's file against null. A
loader falls back to no template, which is a real difference and not a re-save.

## For the recipe library

One shared direction at a smooth weight on both writers of a stated window is the single-projection shape with a
schedule, and the `single-projection-selected` entry fits it but for 18 first shares at the floor. The card's
"LoRA-based" description reads as the merged rank-one adapter it would be: nothing in the weights distinguishes a
merged rank-one LoRA on the output side from a direct projection, and the down projections' weight of 1.36 to
1.41 with the attention outputs' kernel-shaped 0.39 to 0.89 is the shape Heretic's two kernels give. The copy
ships no template. The pull copy keeps the direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/blueback25/measurements/pair-3/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
