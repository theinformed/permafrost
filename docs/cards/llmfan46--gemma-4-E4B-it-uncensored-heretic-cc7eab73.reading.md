# Reading of the Stage 1 and Stage 2 result: llmfan46/gemma-4-E4B-it-uncensored-heretic against google/gemma-4-E4B-it (2026-10-29)

Measured on Nautilus, round 2 piece 3 (job 3763595, 7 minutes, exit 0). Modified revision `446ec370` (2026-05-04),
original pinned at `292a7e27` (2026-04-02). The maker's card names the method and its parameters: Heretic 1.2.0 with
Arbitrary-Rank Ablation, layers 8 to 36, targeted component attn.o_proj only, with the weights its search chose.

## Weights (Stage 2)

The automatic verdict is "recipe violations", nearest recipe single-projection-selected, 23 flags. On reading, the
footprint matches the card and the flags measure a method the table does not describe yet.

- 11 of 2,130 tensors changed, all attention outputs, in layers 21 to 35 of 42. That sits inside the card's layer
  range 8 to 36 and its single target component. Seventeen other attention outputs differ by at most 0.00008 of their
  norm, below the 0.001 threshold: layers the search weighted near zero. Nothing outside the attention outputs moved,
  including the per-layer embeddings and the vision and audio towers.
- The changes are not rank-one. First-value energy share is 0.92 to 0.96, and the first eight values together reach
  only 0.94 to 0.97; the remainder is spread across many directions. Relative change is 0.02 to 0.05, large enough
  that bfloat16 rounding accounts for at most 0.005 of the missing share. The method's name says as much:
  arbitrary rank. The table's "arbitrary-rank" entry is still "not yet measured".
- The leading directions differ by layer (cosine 0.15 to 0.46 with the median), as Heretic's per-layer directions
  would.
- Row norms moved by up to 0.017 relative; nothing in the card claims they were preserved.

## Token and configuration side (Stage 1)

The automatic verdict is "unexplained differences": two fields. On reading, both are explained.

- `template.default`: the copy carries Google's later template, matching `google/gemma-4-E4B-it` at commits
  `c53e9d33` (2026-04-28) and `3555bddc` (2026-05-07) exactly; the pinned modified revision is itself the maker's
  commit "Upload chat_template.jinja" of 2026-05-04. The fixed conversation renders identically.
- `config.text_config.moe_intermediate_size`: absent in every Google revision, present and null in the copy, saved
  with transformers 5.5.0 against the original's 5.5.0.dev0. A re-save addition.

## For the recipe library

Consistent with the stated change on both sides. For the recipe library this is the first measured arbitrary-rank
edit: an energy profile that does not climb toward 1 by the eighth value is its signature, distinct from the
bfloat16 floor, which only lowers the first share on small edits and climbs to 1 within one or two values. The
"arbitrary-rank" entry can be calibrated from this when a run of our own is made.

Weight differences alone cannot certify the absence of hidden behavior.
