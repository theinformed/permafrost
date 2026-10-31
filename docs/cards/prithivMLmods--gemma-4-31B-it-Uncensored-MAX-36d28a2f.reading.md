# Reading of the Stage 1 and Stage 2 result: prithivMLmods/gemma-4-31B-it-Uncensored-MAX against google/gemma-4-31B-it (2026-10-31)

Measured on Nautilus, round 18 piece 3 (push card 5473, round card 5477, download job 4125751, compare job 4125754
on the background queue, sweep 4125760; pulled home by card 5493). Modified revision `6a6218c2` (2026-06-01, the
last of sixteen README commits; the repository was created on 2026-04-04 at 22:51Z and the weights were uploaded on
2026-04-10 at 04:22Z), original pinned at `419b2efe` (2026-04-02, the release commit). The maker's card says the copy
is huihui-ai/Huihui-gemma-4-31B-it-abliterated re-sharded for newer library releases with "no modifications to
weights or architecture", names Google in its `base_model` field, and reports a self-measured abliteration rate of
94.6 percent on 2,000 prompts. It is the maker's third copy in the census after the E4B and 26B-A4B re-uploads of
finding 9.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection`, 52 flags, on the cluster and
after re-scoring at home, all 52 energy shares at the storage floor. On reading, the copy is one shared direction
projected out of every residual writer at weight 1.0, the shape of the huihui-ai card's method, on the layer set a
first version of that maker's 31B copy would have if it edited every layer.

- 120 of 1,188 tensors changed: the attention output and the down projection of all 60 layers. Nothing else moved;
  the largest relative change outside the changed set is exactly 0 and 1,068 tensors equal the original.
- One shared direction on all 120: cross-layer cosine 1.0000 (minimum 0.99998), the two writers of each layer at
  1.0000, the two kinds at 0.99997.
- Weight 1.00: the copy keeps −0.001 to 0.008 of the original's action along the direction on the left and 0.30 to
  0.98 on the right, the left below the right on all 120, an output-side plain ablation. Relative change 0.0122 to
  0.0162 per matrix, first-value share 0.989 to 0.993, leftover 0.0013 to 0.0014 of the weight norm, every matrix
  inside the 0.0025 line: the floor of finding 3, read on a sixth base.
- Row norms moved by 0.0026 to 0.118 on 119 matrices and by 0.362 on the last layer's down projection, as a
  weight-1 projection with no restoration step does.

| Kind | Changed | Relative change | E1 | Left, direction 1 | Right, direction 1 | Row norms | Cross-layer cosine |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Attention output | 60 of 60 | 0.0122 to 0.0162 | 0.989 to 0.993 | 0.00 to 0.01 | 0.51 to 0.97 | 0.0032 to 0.118 | 1.0000 |
| Down projection | 60 of 60 | 0.0127 to 0.0162 | 0.989 to 0.993 | 0.00 to 0.01 | 0.30 to 0.98 | 0.0026 to 0.362 | 1.0000 |

The fingerprint test of finding 9 cannot be run: the census has measured huihui-ai's second 31B version (round 12,
110 matrices in layers 5 to 59 at weight 1.5) and not the first, which the card names. Against the second version
no per-tensor field is equal, which rules it out as the parent, and the layer set and weight differ from it in the
direction that version's card describes (it says the second version leaves the first five layers alone). The
timing fits the card: the first huihui-ai version's weights went up on 2026-04-10 at 03:05Z, this copy's 77 minutes
later, and the second version's repository did not exist until 2026-04-11. Against the five other 31B copies measured
on this original weight file (shards `eeef8791` and `01891222`: wangzhang, llmfan46, coder3101, TrevorJS and
huihui-ai's second version) and this round's null-space copy, no changed matrix has an equal measurement in any
field. If the card's parent holds, huihui-ai's shared projection has a fourth weight, 1.0, on this base's first
version, after 2.5 on E4B, 1.5 on the 31B second version and 3.0 on 26B-A4B (finding 21).

## Token and configuration side (Stage 1)

The cluster's card read "unexplained differences" and the home judgement under transformers 5.6.2 closes the one
open field by tool, so the committed card reads "consistent with re-save noted".

- `config.transformers_version` and `generation.transformers_version`: 5.5.0.dev0 on the original, 5.6.0.dev0 on
  the copy. Re-save effects.
- `config.text_config.moe_intermediate_size`: absent on one side and loading as the same default under 5.6.2, the
  field the tool closed on round 12's pairs 1 and 2 and round 16's pair 6.
- The template is Google's release template byte for byte (the pin is the release commit, so the earlier-revision
  case of the huihui-ai copies does not arise), and the configuration, tokenizer, special tokens and generation
  settings are otherwise equal. The fixed conversation renders identically. The huihui-ai first version's
  configuration and template, fetched at home, equal Google's release files as well.

## For the recipe library

Consistent with the card on both sides as far as the census can test it: a weight-1.0 shared projection on all 120
residual writers, the method of the parent the card names, with the parent itself unmeasured. The fingerprint test
needs huihui-ai/Huihui-gemma-4-31B-it-abliterated in a batch. The saved direction vectors are not committed; the
pull copy is `/opt/ai/hpc-packages/pulls/model-audit/nautilus18/measurements/pair-3/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
