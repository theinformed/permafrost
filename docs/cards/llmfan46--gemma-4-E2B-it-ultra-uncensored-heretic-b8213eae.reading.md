# Reading of the Stage 1 and Stage 2 result: llmfan46/gemma-4-E2B-it-ultra-uncensored-heretic against google/gemma-4-E2B-it (2026-10-30)

Measured on Blueback, round 8 piece 5 (round card 5305, download job 3397500, compare jobs 3397501 to 3397508, all exit
0, sweep 3397509; pulled home by card 5347). Modified revision `13d8eefa` (2026-05-05; the repository was created on
2026-04-26), original pinned at `b4a60110` (2026-04-10, 16:35Z). The maker's card names the method and its parameters:
Heretic 1.2.0 with Arbitrary-Rank Ablation, start layer 17, end layer 24, targeted component attn.o_proj only, with
the preserve, steer and overcorrect weights its search chose and a neighbour count of 4; it reports 4 refusals in
100 against the original's 98 and a KL divergence of 0.0779. The first E2B copy in the census.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 7 flags, on the
cluster and after re-scoring at home. All 7 flags are energy shares. On reading, the footprint matches the card and
the flags measure the arbitrary-rank method.

- 7 of 2,011 tensors changed, all attention outputs, in layers 17 to 23 of 35: every layer of the card's range and
  its one component. Nothing else moved; the largest relative change outside the changed set is exactly 0, the
  per-layer embeddings and the audio and vision towers included.
- The arbitrary-rank profile: first-value energy share 0.950 to 0.976 and first eight values 0.970 to 0.989, on
  relative changes of 0.036 to 0.092; the leftover is 0.0066 to 0.0143 of the weight norm, five to nine times the
  storage floor.
- The leading direction sits on the input side, as on the maker's E4B copies. Along it the copy keeps −0.86 to −3.41
  of the original's action on the right (weights 1.86 to 4.41) and 0.29 to 0.91 on the left; the left fraction is
  above the right on all 7. The tail directions keep 0.77 to 1.10 (median 0.97). Layer 18 carries the largest edit
  measured on this method: weight 4.41, relative change 0.092, row norms moved by 0.066.
- The leading directions differ by layer (cosine 0.26 to 0.31 with their median).
- Row norms moved by 0.006 to 0.066 relative; the card claims no norm preservation.

| Layer | Relative change | E1 | E8 | Left, direction 1 | Right, direction 1 | Row norms |
| --- | --- | --- | --- | --- | --- | --- |
| 17 | 0.052 | 0.970 | 0.986 | 0.51 | −1.32 | 0.011 |
| 18 | 0.092 | 0.976 | 0.989 | 0.29 | −3.41 | 0.066 |
| 19 | 0.045 | 0.954 | 0.970 | 0.77 | −2.22 | 0.012 |
| 20 | 0.051 | 0.950 | 0.977 | 0.69 | −1.36 | 0.013 |
| 21 | 0.036 | 0.968 | 0.978 | 0.91 | −0.86 | 0.006 |
| 22 | 0.049 | 0.959 | 0.973 | 0.62 | −1.47 | 0.009 |
| 23 | 0.063 | 0.959 | 0.976 | 0.55 | −1.61 | 0.037 |

Against the maker's E4B copies (round 2: 11 layers at weights 1.27 to 1.79; round 7: 17 layers) this one edits fewer
layers harder. The E2B base has no other copy in the census to compare fingerprints with.

## Token and configuration side (Stage 1)

The cluster's card read "unexplained differences" in two fields. Re-judged at home the configuration field closes and
the template stays, so the committed card still reads "unexplained differences".

- `config.text_config.moe_intermediate_size`: absent in the original, null in the copy, the library default under
  5.6.2. Saved with transformers 5.5.0 against the original's 5.5.0.dev0.
- `template.default`: the copy's template (17,229 bytes) is Google's template of 2026-04-28 (`6b7e72c6` in the E2B
  repository, 16,804 bytes) plus a 14-line macro, `format_type_argument`, and seven call sites that accept a list of
  types in a tool schema where Google's template accepts one string. It equals no commit of Google's E2B or E4B
  repository (neither has a pull-request branch), and Google's next template (2026-05-18) does not contain the
  macro. The fixed conversation renders identically. A real change on the tool-schema path, origin unknown; the
  maker's E4B copy of round 7 carried Google's 2026-04-28 template byte for byte.

## For the recipe library

Consistent with the stated change on the weight side; the template is a patched Google template the tool cannot
match to any revision. The fourth measured arbitrary-rank copy and the first with a weight past 4; the candidate
entry's remaining-fraction band (−1 to 0 on one side) is too narrow and should read "below 0 on one side" with the
weight reported. The saved direction vectors are not committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/blueback8/measurements/pair-5/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
