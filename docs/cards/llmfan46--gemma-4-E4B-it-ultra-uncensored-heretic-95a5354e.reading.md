# Reading of the Stage 1 and Stage 2 result: llmfan46/gemma-4-E4B-it-ultra-uncensored-heretic against google/gemma-4-E4B-it (2026-10-30)

Measured on Blueback, round 7 piece 1 (round card 5291, compare jobs 3392878 to 3392885, 4 to 6 minutes each, exit 0;
pulled home by card 5302). Modified revision `5964fe4c` (2026-05-04), original pinned at `292a7e27` (2026-04-02). The
maker's card names the method and its parameters: Heretic 1.2.0 with Arbitrary-Rank Ablation, start layer 7, end
layer 36, targeted component attn.o_proj only, with the preserve, steer and overcorrect weights its search chose; it
reports 3 refusals in 100 and a KL divergence of 0.0076.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 17 flags, as scored on
the cluster, and the same after re-scoring at home with the table as committed today (the kit carried the current
table). All 17 flags are energy shares. On reading, the footprint matches the card and the flags measure the method the
table still lists as "not yet measured".

- 17 of 2,130 tensors changed, all attention outputs, in layers 18, 19 and 21 to 35 of 42. That sits inside the card's
  layer range 7 to 36 and its single target component. The 13 other attention outputs in that range differ by at most
  0.000006 of their norm. Nothing outside the attention outputs moved, including the per-layer embeddings and the
  vision and audio towers.
- The changes are not rank-one. First-value energy share is 0.936 to 0.975 and the first eight values together reach
  only 0.963 to 0.985. Relative change is 0.026 to 0.057, so bfloat16 rounding accounts for at most 0.004 of the
  missing share. The method's source fits a rank-50 adapter per matrix by default.
- The leading directions differ by layer (cosine 0.11 to 0.41 with the median, 0.24 in the middle). Along each
  matrix's leading direction the copy keeps 0.26 to 0.91 of the original's action on the output side and reverses it
  on the input side (-1.51 to -0.28); a projection would leave the same fraction on both sides.
- Row norms moved by up to 0.045 relative; the card claims no norm preservation.
- Against the same maker's round 2 copy of this base (11 attention outputs in layers 21 to 35, relative change 0.02 to
  0.05), the "ultra" copy edits 17 layers at 0.03 to 0.06.

## Token and configuration side (Stage 1)

The cluster's first scoring read "unexplained differences" in two fields. Re-judged at home with the later-revision
rule it reads "consistent with re-save noted", and that is the card committed here.

- `template.default`: the copy carries Google's later template, equal byte for byte to `google/gemma-4-E4B-it` at
  commit `c53e9d33` (2026-04-28, "update SI and tool call handling"); the pinned modified revision is itself the
  maker's commit "Upload chat_template.jinja" of 2026-05-04. The fixed conversation renders identically.
- `config.text_config.moe_intermediate_size`: absent in the original, present and null in the copy, which the
  library in the pins (5.6.2) loads as its default. Saved with transformers 5.5.0 against the original's 5.5.0.dev0.

## For the recipe library

Consistent with the stated change on both sides. This is the second measured arbitrary-rank edit, from the same tool
and maker as the first: an energy profile that stays between 0.94 and 0.99 through the eighth value, directions that
differ by layer, and unequal remaining fractions on the two sides of each matrix. The "arbitrary-rank" entry can be
calibrated from these two copies once a run of our own is made. The saved direction vectors are not committed
(`*.safetensors` is ignored); the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/blueback7/measurements/pair-1/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
