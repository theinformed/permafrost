# Reading of the Stage 1 and Stage 2 result: prithivMLmods/gemma-4-E2B-it-Uncensored-MAX against google/gemma-4-E2B-it (2026-10-31)

Measured on Nautilus, round 18 piece 6 (push card 5473, round card 5477, download job 4125751, compare job 4125757
on the background queue, sweep 4125760; pulled home by card 5493). Modified revision `ae5ff124` (2026-06-01, the
last of twelve README commits; the repository was created on 2026-04-13 at 13:38Z and the weights uploaded at
15:59Z), original pinned at `b4a60110` (2026-04-10, the response-schema commit). The maker's card says the copy is
huihui-ai/Huihui-gemma-4-E2B-it-abliterated re-sharded for newer library releases with "no modifications to weights
or architecture", and names Google in its `base_model` field; it is the maker's fourth copy in the census and the
third whose card names a huihui-ai parent.

## Weights (Stage 2)

The tool's assessment was "recipe match", nearest recipe `single-projection-selected`, 0 flags, on the cluster and
after re-scoring at home. On reading, the copy is one shared direction projected out of the residual writers of
layers 10 to 34 at weight 1.0, the layer set the huihui-ai card describes ("the first 10 layers have not been
abliterated").

- 50 of 2,011 tensors changed: the attention output and the down projection of each of layers 10 to 34 of 35.
  Nothing else moved; the largest relative change outside the changed set is exactly 0 and 1,961 tensors, the
  per-layer embeddings, the shared key-value projections, the audio and vision towers among them, equal the original.
- One shared direction on all 50: cross-layer cosine 1.0000 (minimum 0.999996), the two writers of each layer at
  1.0000.
- Weight 1.00: the copy keeps −0.000 to −0.005 of the original's action along the direction on the left and 0.19 to
  0.85 on the right, the left below the right on all 50. Relative change 0.023 to 0.028, first-value share 0.995 to
  0.997, leftover 0.0014 to 0.0016 of the weight norm, every matrix inside the 0.0025 line; the entry's thresholds
  clear because the edit moved each matrix by more than the 1.55 percent finding 3 names.
- Row norms moved by 0.0059 to 0.0259, as a weight-1 projection without restoration does.

| Kind | Changed | Relative change | E1 | Left, direction 1 | Right, direction 1 | Row norms | Cross-layer cosine |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Attention output | 25 of 35 (layers 10 to 34) | 0.023 to 0.028 | 0.995 to 0.997 | −0.00 | 0.46 to 0.85 | 0.0059 to 0.0259 | 1.0000 |
| Down projection | 25 of 35 (layers 10 to 34) | 0.025 to 0.028 | 0.996 to 0.997 | −0.00 | 0.19 to 0.71 | 0.0063 to 0.0212 | 1.0000 |

The fingerprint test of finding 9 cannot be run: huihui-ai's E2B copy is unmeasured. What can be said is that the
layer set is the one that copy's card states, that the method is the one its other copies carry (one shared
direction, every residual writer from a chosen layer on), that its weights went up on 2026-04-08 at 16:08Z and this
copy's five days later, and that against the two other E2B copies measured on this original weight file (shard
`2db5482b`: llmfan46 in round 8, aifeifei798 in round 16) no changed matrix has an equal measurement in any field.
If the card's parent holds, huihui-ai's projection reads 1.0 on E2B as on this round's 31B re-upload, against 2.5 on
E4B, 1.5 on the 31B second version and 3.0 on 26B-A4B (finding 21).

## Token and configuration side (Stage 1)

The cluster's card read "unexplained differences" on four fields. The home judgement closes one by tool and the
template by the commit history, so the reading is consistent while the committed card keeps the tool's text.

- `config.transformers_version` and `generation.transformers_version`: 5.5.0.dev0 on the original, 5.6.0.dev0 on
  the copy. Re-save effects.
- `config.text_config.moe_intermediate_size`: absent on one side and loading as the same default under 5.6.2,
  closed by tool as on pair 3.
- The template (11,926 bytes, `55572b8d`) differs from the pinned one (16,317 bytes) and equals Google's E2B release
  template of 2026-04-02 (`4742fe84`) byte for byte: the earlier-revision case of the huihui-ai copies (rounds 7
  and 12), arrived at through the parent, whose own template is the same release file with carriage-return line
  endings (12,188 bytes). The pin is the 2026-04-10 revision because the repository was created three days after
  it; the files it carries are those of a repository created on 2026-04-08. The fixed conversation renders
  identically under both templates.
- The tokenizer, special tokens and generation settings are otherwise equal.

## For the recipe library

Consistent with the card on both sides as far as the census can test it: a weight-1.0 shared projection on 50
residual writers, matched by the `single-projection-selected` entry with the first ten layers as the unchanged
subset, and the parent unmeasured. The fingerprint test needs huihui-ai/Huihui-gemma-4-E2B-it-abliterated in a
batch. The saved direction vectors are not committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/nautilus18/measurements/pair-6/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
