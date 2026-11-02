# Reading of the Stage 1 and Stage 2 result: wnfldchen/gemma-4-12B-it-qat-q4_0-unquantized-heretic against google/gemma-4-12B-it-qat-q4_0-unquantized (2026-11-02)

Measured on Nautilus, round 34 piece 2 (download job 4163806, compare job 4163808, sweep 4163815; the pull of
11-01 21:23Z carries the measurements and the sweep record and no job log). Modified revision `ca3b6a31` (12
commits on 2026-07-17: model, tokenizer, processor and README between 02:47Z and 02:49Z, then a `reproduce/`
folder of six files and a README edit at 04:38Z), original pinned at `b8dea52d` (the QAT-unquantized checkpoint
of the 12B at a later Google revision than round 33's `58540658`; the two revisions carry the same weight file).
The card (34,120 bytes) is the page of a Heretic v1.4.0 fork, `wnfldchen/heretic` at branch `ara` commit
`7a4a5b68`: an arbitrary-rank ablation with row-norm preservation, start layer 19, end layer 42, preserve 0.9174,
steer 0.0004, overcorrect 0.9004, 13 neighbours, KL divergence 0.0606, keyword refusals 11 of 100 against 99 of
100. The `reproduce/` folder is the first in the census: `config.toml` (`use_ara_lora` true, rank 128, row
normalisation "full" with a rank-3 correction, 200 trials, the export from trial 195, 4-bit quantisation during
the search, a merged export), `requirements.txt`, `SHA256SUMS`, `reproduce.json` and the prompt set. The field
`base_model` names the QAT checkpoint.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 49 flags, on the
cluster and after re-scoring at home: the within-layer cosines of all 23 layers (0.012 to 0.102, counted on both
writers, 46) and three first shares (0.975 to 0.990). On reading, the copy is a rank-one edit of both writers of
layers 19 to 41, input side, with its own direction in every matrix, at weights near one on the down projections
and with four attention outputs that leave the band.

- 46 of 677 tensors changed: the attention outputs and down projections of layers 19 to 41 of 48, the card's
  start 19 and end 42 exactly. Nothing else moved; the largest relative change outside the changed set is exactly
  0, which places the copy on the QAT checkpoint (finding 48).
- Rank one on every matrix: first shares 0.975 to 0.999. The two writers of a layer do not share a direction
  (within-layer cosines 0.01 to 0.10) and the layers do not either (0.07 to 0.35 to the group reference): the
  LoRA-rank search found a direction per matrix.
- Input side on 44 of 46: the right kept fraction is below the left. Read as weights (one minus the right
  fraction) the down projections run 0.95 to 1.90 and most attention outputs 1.1 to 1.9. Four attention outputs
  stand apart: layer 35 keeps -3.14 on the right (weight 4.14, change 0.091, rows moved 0.145) and layer 41
  keeps -4.63 (weight 5.63, change 0.103, rows 0.289), the two largest changes of the copy; layers 36 and 39 keep
  +1.33 and +2.04 on the right with the left at 1.00, the leading input component amplified rather than removed
  (weights -0.33 and -1.04).
- Rows moved 0.0010 to 0.0106 on the other 44 under the card's "row-norm preservation": the preservation is the
  rank-3 correction the configuration names, and it holds to a hundredth where finding 57's holds to 0.0004.
- Against coder3101's arbitrary-rank edit of the same checkpoint (piece 7 of this round) the saved leading left
  vectors stand at 0.41 to 0.998 on the 18 attention outputs both edit (median 0.924; right median 0.926): two
  makers' searches, two tool versions, one direction. Against igorls's kernel search of the same checkpoint the
  median is 0.29 (45 shared), against huihui-ai's shared projection 0.05 (28 shared), against smashingtags's
  projection 0.27.

| Layer | Attention output: change, E1, left kept, right kept | Down projection: change, E1, left kept, right kept | Weights read (1 − right) | Within-layer cosine | Rows |
| --- | --- | --- | --- | --- | --- |
| 19 | 0.0369, 0.998, 0.83, -0.46 | 0.0227, 0.996, 0.94, 0.05 | 1.46, 0.95 | 0.024 | 0.0106, 0.0054 |
| 21 | 0.0328, 0.997, 0.85, -0.62 | 0.0237, 0.996, 0.91, -0.42 | 1.62, 1.42 | 0.012 | 0.0038, 0.0032 |
| 23 | 0.0165, 0.992, 0.93, -0.26 | 0.0176, 0.993, 0.88, -0.51 | 1.26, 1.51 | 0.075 | 0.0024, 0.0010 |
| 25 | 0.0346, 0.998, 0.90, -0.21 | 0.0197, 0.994, 0.93, -0.37 | 1.21, 1.37 | 0.035 | 0.0053, 0.0024 |
| 27 | 0.0236, 0.996, 0.80, -0.22 | 0.0212, 0.992, 0.81, -0.61 | 1.22, 1.61 | 0.067 | 0.0025, 0.0024 |
| 29 | 0.0261, 0.997, 0.97, -0.46 | 0.0188, 0.992, 0.77, -0.72 | 1.46, 1.72 | 0.033 | 0.0074, 0.0013 |
| 31 | 0.0188, 0.994, 0.84, 0.12 | 0.0216, 0.994, 0.91, -0.90 | 0.88, 1.90 | 0.027 | 0.0032, 0.0032 |
| 33 | 0.0246, 0.996, 0.91, -0.18 | 0.0218, 0.994, 0.76, -0.40 | 1.18, 1.40 | 0.019 | 0.0087, 0.0028 |
| 35 | 0.0914, 0.999, 0.90, -3.14 | 0.0188, 0.994, 0.73, -0.43 | 4.14, 1.43 | 0.013 | 0.1449, 0.0015 |
| 36 | 0.0240, 0.975, 1.00, 1.33 | 0.0159, 0.992, 0.75, -0.58 | -0.33, 1.58 | 0.023 | 0.0078, 0.0011 |
| 37 | 0.0291, 0.998, 0.97, -0.76 | 0.0125, 0.990, 0.95, -0.38 | 1.76, 1.38 | 0.048 | 0.0099, 0.0013 |
| 39 | 0.0331, 0.998, 1.01, 2.04 | 0.0171, 0.992, 0.90, -0.24 | -1.04, 1.24 | 0.018 | 0.0376, 0.0053 |
| 41 | 0.1029, 0.999, 0.91, -4.63 | 0.0206, 0.994, 0.71, -0.87 | 5.63, 1.87 | 0.036 | 0.2890, 0.0015 |

The copy's five shards are `513abfa9` (the token embedding and the first layers, equal to igorls's first shard
because neither edit reaches them, finding 71), `ebfb917e`, `eef00b05`, `5c194b3a` and `0d475126`; no measured
file is equal.

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home: the two version strings (5.10.0.dev0 to 5.14.1) are all
that differ. The template is the pin's 18,683-byte file and the fixed conversations render identically.

## For the recipe library

An arbitrary-rank entry (finding 22) with a per-matrix direction and an input-side weight band would match 42 of
the 46 and name the four outliers; the per-layer entry counts every matrix for not sharing a direction with its
neighbour. The copy is the first in the census to ship its search configuration and prompt set beside the weights.
The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus34/measurements/pair-2/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
