# Reading of the Stage 1 and Stage 2 result: llmfan46/G4-MeroMero-26B-A4B-it-uncensored-heretic against zerofata/G4-MeroMero-26B-A4B (2026-11-02)

Measured on Wheat, round 43 piece 1 (download job 387204, compare job 387205, sweep 387213; the pull carries the
measurements and the sweep record and no job log). Modified revision `3a6233b2`: the repository was created
2026-05-22 18:24Z, the weights uploaded at 18:26Z and the card revised at 18:28Z and 18:56Z, then every file was
deleted at 19:12Z and 19:13Z and nine files uploaded at 19:16Z, the upload measured here. Parent pinned at
`475ecf2d` of 05-02, zerofata's fine-tune of google/gemma-4-26B-A4B-it (created 04-15). The card is Heretic
1.2.0's arbitrary-rank table under pull request 211 on `attn.o_proj`: `start_layer_index` 15, `end_layer_index`
26, `preserve_good_behavior_weight` 0.3274, `steer_bad_behavior_weight` 0.0005, `overcorrect_relative_weight`
0.6647, `neighbor_count` 15, a KL divergence of 0.0152 and 12 refusals in 100 against 99. The copy is measured
against the fine-tune its card names and not against Google, so the pair reads the edit alone; the parent's own
distance from Google is read by byte range below.

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 11 flags (first shares 0.858 to
0.942 under the 0.99 floor), on the cluster and after re-scoring at home. On reading, the copy is the
arbitrary-rank branch on the attention outputs of layers 15 to 25, every edit on the input side, the rows under
the band.

- 11 of 1,013 tensors changed: the attention outputs of layers 15 to 25. The card's window runs to 26, where the
  attention output is untouched; nothing moved on the other 1,002 tensors, the experts and the vision tower
  included. The largest relative change outside the changed set is exactly 0.
- A few directions per matrix (first shares 0.86 to 0.94) and no direction shared across layers (median agreement
  0.36, minimum 0.19); the down projections are untouched.
- Input side on all 11: one minus the right kept fraction is 1.25, 1.22, 1.55, 0.99, 1.05, 1.38, 1.26, 1.43,
  1.00, 1.09 and 1.16 at layers 15 to 25. Relative changes 0.0100 (layer 23) to 0.0333 (layer 20).
- Rows moved 0.0005 to 0.0055, under finding 22's band of 0.005 to 0.008 on ten layers and at its lower edge on
  layer 20.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Rows |
| --- | --- | --- | --- |
| 15 | 0.0226, 0.912, 0.92, -0.25 | 1.25 | 0.0028 |
| 17 | 0.0194, 0.920, 0.98, -0.55 | 1.55 | 0.0014 |
| 18 | 0.0230, 0.933, 0.86, 0.01 | 0.99 | 0.0038 |
| 20 | 0.0333, 0.888, 0.94, -0.38 | 1.38 | 0.0055 |
| 21 | 0.0242, 0.858, 0.74, -0.26 | 1.26 | 0.0022 |
| 22 | 0.0225, 0.942, 0.67, -0.43 | 1.43 | 0.0012 |
| 23 | 0.0100, 0.915, 0.97, -0.00 | 1.00 | 0.0005 |
| 25 | 0.0228, 0.942, 0.83, -0.16 | 1.16 | 0.0019 |

The full table (11 rows) is in the report.

Directions. Against the saved vectors of other measurements of the 26B-A4B, the Google-rooted family standing in
for the parent, the directions stand at 0.979 on the left and 0.965 on the right to Vortex5's Chimera-X edit on
all 11 shared names, 0.957 to Vortex5's Moonlight-Dusk edit, 0.953 and 0.923 to SassyDiffusion's search (10
names), 0.942 and 0.955 to the maker's own 26B-A4B search of April, 0.932 and 0.943 to SubMaroon's body and to
coder3101's edit, 0.926 to the maker's QAT search, 0.919 to coder3101's QAT search, 0.81 to mewse's, 0.67 and 0.59
to OS-Software's two Japanese-weighted searches, 0.24 or less to tvall43's and Rootkit7's, 0.203 to TrevorJS's
family of kernel passes, 0.055 to huihui-ai's projection and under 0.01 to the controls on other bases. By byte
range the layer 20 attention output is 0.0333 from the parent's, 0.0339 from Google's, 0.0255 from the maker's own
April edit, 0.0303 from SassyDiffusion's, 0.0269 from coder3101's and 0.0336 from Chimera-X's (the parent 0.0064
from Google's; the maker's April edit 0.0307, SassyDiffusion's 0.0429, coder3101's 0.0377 and Chimera-X's 0.0384
from Google's; the maker's April edit 0.0159 from coder3101's and 0.0210 from SassyDiffusion's), and the layer 10 query projection is byte-equal to the parent's and 0.0059 from Google's, the fine-tune's own change. The nine
shards match no measured file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home on `template.default`: the copy carries a 17,708-byte
template in place of the parent's 16,448-byte one (Google's 26B-A4B revision `1db3cff1` of 04-10). The two differ
in the tool-call macros (a `format_type_argument` macro and a `filter_keys` switch the parent's lacks) and render
the fixed conversation identically. It is the maker's fourth template in the census: the 17,344-byte one on the
maker's 31B and 26B-A4B repositories of April and May and on the MeroMero 31B edit of round 42, an 18,841-byte one
now on the maker's 31B head, and Google's 18,683-byte revision `35b4173c` of 07-15 on the 26B-A4B head. The
version strings read 5.5.4 to 5.9.0 in the configuration and 5.5.0.dev0 to 5.9.0 in the generation file. The
token ids (`eos_token_id` `[1, 106]`, generation `[1, 106, 50]`, `bos_token_id` 2, `pad_token_id` 0) and the
generation settings are the parent's.

## For the recipe library

An arbitrary-rank entry with a components line would read the copy as its card with layer 26's absence called
out. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat43/measurements/pair-1/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
