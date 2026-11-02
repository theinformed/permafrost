# Reading of the Stage 1 and Stage 2 result: OS-Software/gemma-4-12B-it-qat-q4_0-unquantized-heretic-ja-v2 against google/gemma-4-12B-it-qat-q4_0-unquantized (2026-11-02)

Measured on Wheat, round 37 piece 1 (download job 387161, compare job 387162, sweep 387170; the pull carries the
measurements and the sweep record and no job log). Modified revision `90825e3e` (six commits on 2026-08-03 between
08:09Z and 08:12Z: the weights, the tokenizer, the processor and the README twice), original pinned at `b6ed8627`
(06-04), a revision of the QAT-unquantized 12B checkpoint that carries the same single weight file (`26f2cee4`) as
the `58540658` revision of round 33 and piece 7 of this round and the `b8dea52d` revision of round 34 (finding 75).
The card (32,674 bytes, Google's QAT card under the tool's table) says Heretic v1.4.0 "with the Arbitrary-Rank
Ablation (ARA) method using a LoRA adapter and row-norm preservation": `start_layer_index` 13, `end_layer_index`
40, `preserve_good_behavior_weight` 1.0000, `steer_bad_behavior_weight` 0.9032, `overcorrect_relative_weight`
0.9915, `neighbor_count` 1, keywords 0 of 100 against 100 of 100, KL divergence 0.0637, and that the refusal
measurement used the maker's Japanese prompt sets (`harmless_alpaca_ja`, `harmful_behaviors_ja`). The `base_model`
field names google/gemma-4-12B-it and the first sentence names the QAT checkpoint, the inherited header of finding
48; the pinner followed the name and recorded the QAT checkpoint as `card_parent`. The maker's fourth copy in the
census and the first on the 12B; a `-ja` first version (06-25) and an English `-v3` (09-07) of the same checkpoint
are unmeasured.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 108 flags (54
first shares of 0.36 to 0.96 and 54 within-layer cosines of 0.003 to 0.073), on the cluster and after re-scoring at
home. On reading, the copy is the card's window on both writers, input side, with many directions per matrix and
the rows within the preservation claim.

- 54 of 677 tensors changed: the attention outputs and the down projections of layers 13 to 39, the card's start 13
  and end 40 with the end exclusive. Nothing else moved; the largest relative change outside the changed set is
  exactly 0 and 623 tensors equal the original, which places the copy on the QAT checkpoint (finding 48).
- Many directions per matrix: first shares 0.36 to 0.96, the fourth cumulative share 0.74 to 0.99 and the eighth
  0.85 to 0.995. The LoRA-adapter branch with its row correction spreads the change over a subspace where the
  maker's earlier exports cut at rank four (findings 42 and 57 on the maker's E4B and 26B-A4B copies).
- Input side on 54 of 54: the left kept fraction is 0.64 to 0.99 and the right -0.95 to 0.26, the left above the
  right on every matrix. Read as weights, one minus the right kept fraction, 0.74 to 1.95 (median 1.63), the
  attention outputs 0.87 to 1.94 and the down projections 0.74 to 1.95.
- No shared direction: within a layer 0.003 to 0.073, across layers 0.04 to 0.35 to the group reference.
- Rows moved 0.0003 to 0.0057 under the card's preservation claim, at or under the bottom of finding 22's band
  (0.0057 to 0.0080) on all 54, where wnfldchen's LoRA-adapter export of the same checkpoint read 0.0010 to 0.0106
  (finding 72).
- Relative changes 0.0067 to 0.052, the largest on the attention output of layer 32.

| Layer | Attention output: change, E1, E4, left kept, right kept | Down projection: change, E1, E4, left kept, right kept | Weight read | Within-layer cosine | Rows |
| --- | --- | --- | --- | --- | --- |
| 13 | 0.0141, 0.955, 0.98, 0.69, 0.13 | 0.0067, 0.910, 0.97, 0.93, 0.26 | 0.87/0.74 | 0.009 | 0.0011, 0.0003 |
| 16 | 0.0313, 0.673, 0.86, 0.71, -0.48 | 0.0154, 0.687, 0.87, 0.89, -0.66 | 1.48/1.66 | 0.011 | 0.0032, 0.0007 |
| 20 | 0.0344, 0.541, 0.79, 0.66, -0.30 | 0.0186, 0.678, 0.85, 0.83, -0.59 | 1.30/1.59 | 0.025 | 0.0045, 0.0011 |
| 24 | 0.0305, 0.679, 0.87, 0.77, -0.63 | 0.0278, 0.392, 0.74, 0.89, -0.70 | 1.63/1.70 | 0.051 | 0.0028, 0.0012 |
| 28 | 0.0433, 0.400, 0.74, 0.70, -0.63 | 0.0287, 0.491, 0.79, 0.85, -0.79 | 1.63/1.79 | 0.055 | 0.0050, 0.0015 |
| 32 | 0.0522, 0.422, 0.76, 0.78, -0.49 | 0.0294, 0.582, 0.84, 0.84, -0.62 | 1.49/1.62 | 0.040 | 0.0057, 0.0011 |
| 36 | 0.0357, 0.591, 0.88, 0.99, -0.94 | 0.0260, 0.456, 0.78, 0.90, -0.68 | 1.94/1.68 | 0.003 | 0.0016, 0.0015 |
| 39 | 0.0340, 0.692, 0.92, 0.81, -0.88 | 0.0259, 0.434, 0.76, 0.71, -0.63 | 1.88/1.63 | 0.009 | 0.0012, 0.0011 |

The full table (54 rows) is in the report.

Directions. Against the saved vectors of thirty 12B measurements, this copy's leading directions stand apart from
all of them. The nearest are the English arbitrary-rank searches: coder3101's instruct 12B edit at a median of
0.41 on the left and 0.30 on the right (54 shared), llmfan46's 12B QAT edit of piece 7 at 0.40 and 0.36 (11
shared), llmfan46's instruct edit at 0.39 and 0.28, coder3101's QAT edit at 0.37 and 0.29 and wnfldchen's at 0.36
and 0.34; the kernel and projection edits of the same checkpoint stand at 0.13 or less (igorls's at 0.13, smashingtags's
at 0.14 on the left, huihui-ai's at 0.05). Where the English searches of one method agree among themselves at 0.92
to 0.97 (finding 72, and piece 7 below), the search over Japanese prompts found a direction that shares 0.4 of its
length with theirs. The first shard (`513abfa9`) equals wnfldchen's and igorls's 12B QAT exports' first shards, the
library's layout of the embeddings and the layers no edit touches (finding 71); the other four shards equal no
measured file.

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home: the two version strings (5.10.0.dev0 to 5.13.0) are
all that differ. The template is 19,073 bytes against the pin's 18,683 and differs in line endings alone; the fixed
conversation renders identically.

## For the recipe library

The directional-per-layer entry is the nearest and all 108 flags are the LoRA-adapter branch's many directions per
matrix and its direction per matrix; an arbitrary-rank entry (finding 22) that reads the input-side weights, the
subspace share and the row band would flag nothing. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat37/measurements/pair-1/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
