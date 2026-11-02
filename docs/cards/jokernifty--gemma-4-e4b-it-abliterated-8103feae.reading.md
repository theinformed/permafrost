# Reading of the Stage 1 and Stage 2 result: jokernifty/gemma-4-e4b-it-abliterated against google/gemma-4-E4B-it (2026-11-01)

Measured on Blueback, round 25 piece 1. The pull carries the measurements and the sweep record and no job log.
Modified revision `7f7586e8` (three commits on 2026-05-31: the folder upload at 15:53Z, three minutes after the
repository was created, and a README update), original pinned at `d6436b3d` (05-18), the revision current when
the repository was created. The card describes a single orthogonal projection: 32 harmful and 32 harmless
instructions, the refusal direction taken at layer 25 (about 60 percent of depth), `W_new = W - (r r^T) W` applied
to `self_attn.o_proj`, `mlp.down_proj` and the token embedding on text decoder layers 20 to 34 of 42, every other
tensor left alone, with a paragraph on why the projection is limited to the middle band on this family. The
`base_model` field names the original.

## Weights (Stage 2)

The tool's assessment was "recipe match", recipe `single-projection-selected`, 0 flags, on the cluster and after
re-scoring at home. On reading, the copy is the card's projection on the card's 31 matrices at weight 1.0000, saved
in float16, which leaves the measure without the bfloat16 floor for the first time in the census.

- 31 of 2,076 tensors changed: the attention output and the down projection of layers 20 to 34 (30) and
  `embed_tokens` (relative change 0.0188). The 54 shared-KV tensors of layers 24 to 41 are dropped by the export,
  as finding 14's rule maps them. The 336 tensors the tool lists as unchanged with a nonzero difference moved by at
  most 1.07 × 10⁻⁶ of their norm: the per-layer input gates and the vision tower's patch embedder, whose smallest
  bfloat16 values round when stored as float16. 1,709 tensors equal the original bit for bit.
- One direction for the whole model, the embedding included: every changed matrix's leading direction agrees with
  the group's at 0.9999999 or better, the attention outputs with the down projections at the same figure, and the
  embedding's direction along its hidden axis is the same vector.
- Weight 1.0000 on the output side of the 30 projections: the left kept fraction is within 0.00005 of 0 on all 30,
  the right 0.68 to 0.86 on the attention outputs and 0.27 to 0.80 on the down projections. On the embedding the
  right kept fraction is 0.00002 and the left 0.943: the direction is removed along the hidden axis of every token
  row, which is the card's third target.
- No floor: the first share is 0.99988 to 0.99993 on all 31 (fourth cumulative share the same), where every
  bfloat16 copy in the census reads 0.989 to 0.997 at this edit size (finding 3). Saved in float16, the rounding
  outside the first direction is 0.00009 of the norm instead of 0.0013 to 0.0016.
- Rows moved by 0.006 to 0.015 on the attention outputs and 0.004 to 0.010 on the down projections, unrestored;
  the embedding's by 0.0039.
- Relative change 0.019 to 0.022 on the attention outputs and 0.019 to 0.0225 on the down projections.

| Layer | Attention output: change, E1, left kept, right kept | Down projection: change, E1, left kept, right kept | Within-layer cosine | Row norms |
| --- | --- | --- | --- | --- |
| 20 | 0.0204, 0.9999, -0.00000, 0.810 | 0.0196, 0.9999, -0.00000, 0.478 | 1.0000 | 0.0066, 0.0043 |
| 22 | 0.0207, 0.9999, -0.00000, 0.701 | 0.0200, 0.9999, -0.00000, 0.795 | 1.0000 | 0.0075, 0.0101 |
| 24 | 0.0220, 0.9999, 0.00000, 0.675 | 0.0225, 0.9999, -0.00000, 0.404 | 1.0000 | 0.0074, 0.0080 |
| 27 | 0.0197, 0.9999, -0.00000, 0.780 | 0.0194, 0.9999, 0.00000, 0.465 | 1.0000 | 0.0056, 0.0045 |
| 29 | 0.0203, 0.9999, 0.00000, 0.857 | 0.0199, 0.9999, 0.00000, 0.405 | 1.0000 | 0.0152, 0.0045 |
| 31 | 0.0202, 0.9999, 0.00000, 0.766 | 0.0194, 0.9999, -0.00000, 0.269 | 1.0000 | 0.0057, 0.0042 |
| 34 | 0.0190, 0.9999, 0.00000, 0.721 | 0.0196, 0.9999, -0.00000, 0.332 | 1.0000 | 0.0058, 0.0036 |
| embedding | 0.0188, 0.9999, 0.943, 0.00002 | - | - | 0.0039 |

The full table (31 rows) is in the report.

The fingerprint shares no measured field with the eleven earlier reports on this original. The copy is one
15,882,475,420-byte shard (`3726d55442`).

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, four fields. Under transformers 5.22.1
`text_config.moe_intermediate_size` (null in a 5.9.0 save) closes by the default rule. What stays open is the data
type: `dtype`, `text_config.dtype`, `audio_config.dtype` and `vision_config.dtype` read `bfloat16` in the original
and `float16` in the copy, and every tensor in the weight file is float16. The card does not say the save changed
the storage type; the configuration and the weights agree with each other, so the four fields are a true
difference the tool reads correctly, not a re-save artefact. The template is Google's pinned file and the fixed
conversation renders identically.

## For the recipe library

The `single-projection-selected` entry fits with no flag, and the copy calibrates the measure's floor: the same
edit size that reads 0.989 to 0.993 on every bfloat16 copy reads 0.9999 here, which is the storage-floor reading of
finding 3 confirmed from the other side. A token-embedding projection on the hidden axis reads as the writers'
direction with the sides swapped (right kept 0.00002, left 0.943), a different shape from finding 6's one-layer
patch and finding 30's thirteen scaled rows. The pull copy keeps the direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/blueback25/measurements/pair-1/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
