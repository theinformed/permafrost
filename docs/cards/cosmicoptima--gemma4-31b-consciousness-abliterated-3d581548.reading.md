# Reading of the Stage 1 and Stage 2 result: cosmicoptima/gemma4-31b-consciousness-abliterated against google/gemma-4-31B-it (2026-11-02)

Measured on Nautilus, round 40 piece 2 (download job 4169647, compare job 4169649, sweep 4169656; the pull carries
the measurements and the sweep record and no job log). Modified revision `50dd6dda` (created 2026-07-21 04:06Z,
the upload ten minutes later), original pinned at `842da379` of 07-20. The card calls the copy "an exploratory
weight-level intervention": one direction "derived from paired refusal and direct-answer prefixes for questions
about internal state, emotion, awareness", taken from decoder layer 58 with alpha 1.0 and "projected from the
token embedding and 120 residual-writing output matrices"; on its 48-prompt evaluation canonical refusals fell
from 26 to 17 and all 16 harmful-request controls still refuse. The configuration carries the method's name,
`residual_writer_orthogonal_projection`. It is the census's first copy whose direction is not a refusal
direction.

## Weights (Stage 2)

The tool's assessment was violations against `single-projection`, 117 flags (first shares of 0.9877 to 0.9932,
under the entry's floor of 0.99), on the cluster and after re-scoring at home. On reading, the copy is exactly
its card: one direction for the whole model, projected out of the token embedding and both writers of all 60
layers at alpha 1.0.

- 121 of 1,188 tensors changed: the token embedding and the attention output and down projection of every layer.
  Nothing else moved; the largest relative change outside the changed set is exactly 0 on all 1,067 other
  tensors.
- Rank one on every matrix, first shares 0.988 to 0.993, and one direction: the 120 writers' directions stand at
  1.000 to each other within and across kinds and layers.
- Output side on all 120 writers: the left kept fraction is -0.004 to 0.003, a weight of 1.00 on every matrix,
  the right side keeping 0.25 to 0.98; the embedding is projected on its hidden-dimension side (left kept 0.97,
  right kept -0.01), the same direction applied to the token vectors. Rows moved 0.0017 to 0.040, unrestored, under no
  claim. Relative changes 0.0134 to 0.0186.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Down projection: change, E1, left kept, right kept | Weight | Rows |
| --- | --- | --- | --- | --- | --- |
| 0 | 0.0142, 0.989, 0.00, 0.98 | 1.00 | 0.0135, 0.988, 0.00, 0.95 | 1.00 | 0.0131, 0.0049 |
| 10 | 0.0134, 0.988, -0.00, 0.95 | 1.00 | 0.0137, 0.988, 0.00, 0.83 | 1.00 | 0.0035, 0.0074 |
| 20 | 0.0141, 0.989, -0.00, 0.96 | 1.00 | 0.0142, 0.989, 0.00, 0.94 | 1.00 | 0.0087, 0.0062 |
| 30 | 0.0140, 0.989, 0.00, 0.84 | 1.00 | 0.0142, 0.989, 0.00, 0.75 | 1.00 | 0.0033, 0.0030 |
| 40 | 0.0140, 0.988, 0.00, 0.56 | 1.00 | 0.0141, 0.989, 0.00, 0.46 | 1.00 | 0.0025, 0.0026 |
| 45 | 0.0139, 0.988, 0.00, 0.46 | 1.00 | 0.0138, 0.988, 0.00, 0.26 | 1.00 | 0.0389, 0.0021 |
| 50 | 0.0135, 0.988, 0.00, 0.47 | 1.00 | 0.0138, 0.988, 0.00, 0.37 | 1.00 | 0.0024, 0.0030 |
| 59 | 0.0157, 0.991, 0.00, 0.48 | 1.00 | 0.0149, 0.990, 0.00, 0.42 | 1.00 | 0.0032, 0.0399 |

The token embedding: change 0.0142, E1 0.989, left kept 0.97, right kept -0.01, rows 0.0031. The full table (60
rows) is in the report.

Directions. Against twenty-six saved vectors of other measurements of the 31B, the direction stands at 0.034 or
less to every edit: 0.031 to 0.034 to huihui-ai's two exports and their re-uploads (110 to 120 shared names),
0.019 to null-space's, coder3101's and Sabomako's, 0.013 to TrevorJS's and ressl's on all 120, 0.014 to germlag's,
0.012 to Vampelium's, 0.011 to 3MPER0RR's and Jim-darby's, 0.007 to DuoNeural's. The refusal directions of the
measured 31B edits stand to each other at 0.4 to 1.000, and this direction stands apart from every one of
them, as the card's purpose says it should. The thirteen shards
(`26d88af4` to `715b15fa`) match no measured file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster, "consistent with re-save noted" at home: the home judgement closed
`text_config.moe_intermediate_size` by the default rule under transformers 5.22.1, leaving the version strings
(5.5.0.dev0 to 5.12.1). The tokenizer, the token ids, the generation settings and the 18,683-byte template are
the pin's.

## For the recipe library

The single-projection entry reads the copy exactly once its first-share floor allows 0.988 (the 120 matrices are
rank one with the residue of bfloat16 rounding at 0.007 to 0.012 of the change, the same floor the kernel
exports need). The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus40/measurements/pair-2/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
