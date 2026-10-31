# Reading of the Stage 1 and Stage 2 result: prithivMLmods/gemma-4-26B-A4B-it-Uncensored-MAX against google/gemma-4-26B-A4B-it (2026-10-31)

Measured on Nautilus, round 16 piece 4 (push card 5433, round card 5434, download job 4120061, compare job 4120065 on
the background queue, sweep 4120069; pulled home by card 5467). Modified revision `febed22d` (2026-06-01, a README
commit; the repository was created on 2026-04-04 and the weights were uploaded on 2026-04-11 at 11:17Z, nine hours
after huihui-ai uploaded the copy named below, at 02:51Z), original pinned at `47b6801b` (2026-04-02, the release
commit; shards `11276849` and `aab47033`). The maker's card says the copy is "an optimized release built on top of
huihui-ai/Huihui-gemma-4-26B-A4B-it-abliterated", re-sharded, with "no modifications to weights"; its `base_model`
field names Google, and its model-index entry is named "gemma-4-31B-it-Uncensored-MAX", the other size.

## Weights (Stage 2)

The tool's assessment was "recipe match", `single-projection-selected`, 0 flags, on the cluster and after re-scoring
at home. On reading, the copy is huihui-ai's edit, re-uploaded, as its card says and its field does not.

- 50 of 1,013 tensors changed: the attention output and the shared down projection of layers 5 to 29. Nothing else
  moved; the largest relative change outside the changed set is exactly 0, and no expert tensor, router or
  reading-side projection changed.
- One shared direction (cross-layer cosine 0.999997 or more on all 50), rank one (first share 0.999, the first
  singular value 162 to 557 times the second), output side (left below right on all 50), weight 3.0: along the
  leading direction the copy keeps −1.998 to −2.004 of the original's action on the left. Row norms moved by 0.08 to
  0.61.
- Every per-tensor field of all 1,013 tensors equals huihui-ai's round 12 report
  (`results/weights/huihui-ai-Huihui-gemma-4-26B-A4B-it-abliterated.json`) to the last digit, and the saved direction
  file equals round 12's pair 5 file byte for byte (sha256 `2b8bd691`); the two originals are one weight file. The
  same result as finding 9 on E4B, from the same maker, and the same method the fingerprint test is for.

| Layer | Relative change | E1 | E8 | Left, direction 1 | Right, direction 1 | Row norms | Cross-layer cosine | Within-layer cosine |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | 0.074 | 1.000 | 1.000 | -2.00 | 0.19 | 0.2824 | 1.00 | 1.000 |
| 6 | 0.083 | 1.000 | 1.000 | -2.00 | -0.01 | 0.3324 | 1.00 | 1.000 |
| 7 | 0.082 | 1.000 | 1.000 | -2.00 | -0.14 | 0.4272 | 1.00 | 1.000 |
| 8 | 0.084 | 1.000 | 1.000 | -2.00 | -0.29 | 0.3031 | 1.00 | 1.000 |
| 9 | 0.093 | 1.000 | 1.000 | -2.00 | -0.20 | 0.2503 | 1.00 | 1.000 |
| 10 | 0.094 | 1.000 | 1.000 | -2.00 | -0.26 | 0.0985 | 1.00 | 1.000 |
| 11 | 0.076 | 1.000 | 1.000 | -2.00 | -0.04 | 0.0920 | 1.00 | 1.000 |
| 12 | 0.081 | 1.000 | 1.000 | -2.00 | -0.43 | 0.0826 | 1.00 | 1.000 |
| 13 | 0.077 | 1.000 | 1.000 | -2.00 | -0.18 | 0.1101 | 1.00 | 1.000 |
| 14 | 0.070 | 1.000 | 1.000 | -2.00 | -0.10 | 0.1388 | 1.00 | 1.000 |
| 15 | 0.064 | 0.999 | 0.999 | -2.00 | 0.12 | 0.1250 | 1.00 | 1.000 |
| 16 | 0.067 | 0.999 | 0.999 | -2.00 | 0.44 | 0.1816 | 1.00 | 1.000 |
| 17 | 0.054 | 0.999 | 0.999 | -2.00 | 0.17 | 0.2498 | 1.00 | 1.000 |
| 18 | 0.063 | 0.999 | 0.999 | -2.00 | 0.09 | 0.1596 | 1.00 | 1.000 |
| 19 | 0.073 | 1.000 | 1.000 | -2.00 | 0.76 | 0.3515 | 1.00 | 1.000 |
| 20 | 0.059 | 0.999 | 0.999 | -2.00 | -0.01 | 0.1151 | 1.00 | 1.000 |
| 21 | 0.057 | 0.999 | 0.999 | -2.00 | 0.22 | 0.1434 | 1.00 | 1.000 |
| 22 | 0.057 | 0.999 | 0.999 | -2.00 | -0.08 | 0.1740 | 1.00 | 1.000 |
| 23 | 0.057 | 0.999 | 0.999 | -2.00 | 0.82 | 0.2835 | 1.00 | 1.000 |
| 24 | 0.059 | 0.999 | 0.999 | -2.00 | 0.24 | 0.1638 | 1.00 | 1.000 |
| 25 | 0.050 | 0.999 | 0.999 | -2.00 | -0.05 | 0.2277 | 1.00 | 1.000 |
| 26 | 0.056 | 0.999 | 0.999 | -2.00 | -0.01 | 0.1482 | 1.00 | 1.000 |
| 27 | 0.058 | 0.999 | 0.999 | -2.00 | 0.05 | 0.1247 | 1.00 | 1.000 |
| 28 | 0.047 | 0.999 | 0.999 | -2.00 | 0.02 | 0.1929 | 1.00 | 1.000 |
| 29 | 0.050 | 0.999 | 0.999 | -2.00 | 0.26 | 0.2704 | 1.00 | 1.000 |

The shared down projections:

| Layer | Relative change | E1 | E8 | Left, direction 1 | Right, direction 1 | Row norms | Cross-layer cosine | Within-layer cosine |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | 0.060 | 0.999 | 0.999 | -2.00 | 0.38 | 0.1542 | 1.00 | 1.000 |
| 6 | 0.061 | 0.999 | 0.999 | -2.00 | 0.18 | 0.2852 | 1.00 | 1.000 |
| 7 | 0.060 | 0.999 | 0.999 | -2.00 | 0.33 | 0.0981 | 1.00 | 1.000 |
| 8 | 0.062 | 0.999 | 0.999 | -2.00 | 0.35 | 0.2826 | 1.00 | 1.000 |
| 9 | 0.060 | 0.999 | 0.999 | -2.00 | 0.34 | 0.2597 | 1.00 | 1.000 |
| 10 | 0.056 | 0.999 | 0.999 | -2.00 | 0.59 | 0.2463 | 1.00 | 1.000 |
| 11 | 0.052 | 0.999 | 0.999 | -2.00 | 0.49 | 0.3704 | 1.00 | 1.000 |
| 12 | 0.055 | 0.999 | 0.999 | -2.00 | 0.59 | 0.3094 | 1.00 | 1.000 |
| 13 | 0.054 | 0.999 | 0.999 | -2.00 | 0.47 | 0.3197 | 1.00 | 1.000 |
| 14 | 0.051 | 0.999 | 0.999 | -2.00 | 0.54 | 0.4184 | 1.00 | 1.000 |
| 15 | 0.050 | 0.999 | 0.999 | -2.00 | 0.59 | 0.3848 | 1.00 | 1.000 |
| 16 | 0.047 | 0.999 | 0.999 | -2.00 | 0.62 | 0.2841 | 1.00 | 1.000 |
| 17 | 0.044 | 0.999 | 0.999 | -2.00 | 0.65 | 0.3308 | 1.00 | 1.000 |
| 18 | 0.044 | 0.999 | 0.999 | -2.00 | 0.65 | 0.3332 | 1.00 | 1.000 |
| 19 | 0.043 | 0.999 | 0.999 | -2.00 | 0.61 | 0.3905 | 1.00 | 1.000 |
| 20 | 0.043 | 0.999 | 0.999 | -2.00 | 0.49 | 0.3453 | 1.00 | 1.000 |
| 21 | 0.042 | 0.999 | 0.999 | -2.00 | 0.51 | 0.3064 | 1.00 | 1.000 |
| 22 | 0.041 | 0.999 | 0.999 | -2.00 | 0.47 | 0.3782 | 1.00 | 1.000 |
| 23 | 0.041 | 0.999 | 0.999 | -2.00 | 0.67 | 0.3753 | 1.00 | 1.000 |
| 24 | 0.041 | 0.999 | 0.999 | -2.00 | 0.63 | 0.4113 | 1.00 | 1.000 |
| 25 | 0.039 | 0.999 | 0.999 | -2.00 | 0.69 | 0.5613 | 1.00 | 1.000 |
| 26 | 0.038 | 0.999 | 0.999 | -2.00 | 0.78 | 0.4522 | 1.00 | 1.000 |
| 27 | 0.039 | 0.999 | 0.999 | -2.00 | 0.73 | 0.4414 | 1.00 | 1.000 |
| 28 | 0.040 | 0.999 | 0.999 | -2.00 | 0.83 | 0.4784 | 1.00 | 1.000 |
| 29 | 0.043 | 0.999 | 0.999 | -2.00 | 0.75 | 0.6092 | 1.00 | 1.000 |

## Token and configuration side (Stage 1)

The cluster's card read "consistent with re-save noted" and the home judgement keeps it, so the committed card
reads "consistent with re-save noted".

- `config.transformers_version` and `generation.transformers_version`: 5.5.0.dev0 on the original, 5.6.0.dev0 on the
  copy. Re-save effects.
- The template is Google's release template byte for byte (the pin is the release commit, so the earlier-revision
  case of the huihui-ai copy does not arise here), the configuration, tokenizer, special tokens and generation
  settings are otherwise equal, and the fixed conversation renders identically.

## For the recipe library

Consistent with the card on both sides, and the card is right where the `base_model` field is not: the copy is
huihui-ai's shared-projection edit at weight 3.0 and must be counted as that edit, as finding 9 counts the maker's
E4B re-upload. The saved direction vectors are not committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/nautilus16/measurements/pair-4/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
