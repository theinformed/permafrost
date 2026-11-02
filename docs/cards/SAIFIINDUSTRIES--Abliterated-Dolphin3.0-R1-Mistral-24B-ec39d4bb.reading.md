# Reading of the Stage 1 and Stage 2 result: SAIFIINDUSTRIES/Abliterated-Dolphin3.0-R1-Mistral-24B against dphn/Dolphin3.0-R1-Mistral-24B (2026-11-02)

Measured on Wheat, round 45 piece 4 (download job 387355, compare job 387359, sweep 387364; the pull carries the
measurements and the sweep record and no job log). Modified revision `91301f62` (created 2026-10-03 03:13Z, one
commit titled "Duplicate from saukko/Abliterated-Dolphin3.0-R1-Mistral-24B"), parent pinned at `d96260c1` of
2025-04-25, dphn's Dolphin 3.0 R1 fine-tune of Mistral Small 24B Base 2501 (created 2025-02-06, the weights
uploaded that day and unchanged since). saukko's repository (created 2025-05-26, the weights uploaded at 22:36Z
and unchanged through its head `238a8e39` of 05-28) is present on the hub, and the duplicate's ten shards
(`b5a6a7f5` to `605483d5`) are saukko's ten at every one of its revisions by the hub's object ids, as are its
README, configuration, generation file, index, token files and the parent's `trainer_state.json`. The batch note's
"its weight files differ" describes the comparison with the parent; against the named source the files are the
same. The pair is measured as saukko's edit, which the census has not measured otherwise. The card is saukko's:
mlabonne's abliteration article and FailSpy's abliterator as the method, "no DPOs to heal the damage", no layer,
weight or count.

## Weights (Stage 2)

The tool's assessment was violations against `single-projection`, 66 flags (first shares 0.987 to 0.990 under the
0.99 floor), on the cluster and after re-scoring at home. On reading, the copy is the classic projection of one
direction out of the token embedding and both residual writers of every layer, at a weight of 1.00.

- 81 of 363 tensors changed: the token embedding, the attention outputs of all 40 layers and the down projections of
  all 40 layers. The `lm_head`, the readers and the normalisation vectors read exactly 0, and the largest relative
  change outside the changed set is exactly 0.
- One direction on all 81: median agreement 0.999998 (minimum 0.99999), cross-kind 0.99998, first shares 0.987 to
  0.993.
- Output side on all 80 writers at weight 1.00 (left kept fraction -0.004 to 0.003); the embedding carries the same
  direction along its hidden axis (right kept 0.002).
- Relative changes 0.0135 to 0.0191 on the attention outputs and 0.0137 to 0.0167 on the down projections, 0.0136 on
  the embedding.
- Rows moved 0.0017 to 0.0151, through and over finding 22's band, with no restoration step.

| Layer | Attention output: change, E1, left kept, right kept | Down projection: change, E1, left kept, right kept |
| --- | --- | --- |
| 0 | 0.0141, 0.988, -0.004, 0.92 | 0.0138, 0.988, 0.002, 0.52 |
| 10 | 0.0148, 0.989, 0.002, 0.72 | 0.0146, 0.989, 0.002, 0.32 |
| 20 | 0.0191, 0.993, 0.002, 0.61 | 0.0160, 0.991, 0.002, 0.37 |
| 30 | 0.0139, 0.988, 0.003, 0.74 | 0.0138, 0.988, 0.002, 0.28 |
| 39 | 0.0146, 0.989, 0.002, 0.79 | 0.0141, 0.988, 0.002, 0.31 |

Directions. The census has no other measurement on Dolphin's fine-tune. To venkycs's projection of Mistral Small 24B
Instruct 2501, the same architecture and one checkpoint over, the direction stands at 0.448 on all 78 shared names
(maximum 0.448, one direction against one direction), to nicoboss's duplicate of huihui-ai's Mistral Small 3.2
projection at 0.201, to Pranavz's Hearthfire kernels at 0.21 and to every Nemo and Ministral edit at 0.023 or less.
By byte range at layer 20 the attention output is 0.0191 from the parent's with the leading component of the
difference carrying 0.993 of it, and the query projection is byte-equal to the parent's; the parent's attention
output stands 0.376 from Mistral's Base 2501 and its query projection 0.397, a full fine-tune whose difference has
no leading component (first share 0.0033 and 0.0048), and the leading direction of that fine-tune stands at 0.005
to the copy's. The copy's projection direction stands at 0.448 to venkycs's by byte range as well, the value the
saved vectors give.

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home: `_name_or_path`, the configuration's version string
(4.48.1 to 4.52.3) and the generation file's. The token ids are the parent's on both sides (`bos_token_id` 1,
`eos_token_id` `[2, 131072]` in the configuration and the generation file), the vocabulary is 131,074 on both sides
with the two tokens Dolphin added, and the 2,513-byte template renders the fixed conversation identically.

## For the recipe library

The single-projection entry reads the copy once its first-share floor is read beside the storage type (finding 51's
case, every first share 0.987 to 0.993 on a bfloat16 save); an embedding line would name the hidden-axis reading.
The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat45/measurements/pair-4/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
