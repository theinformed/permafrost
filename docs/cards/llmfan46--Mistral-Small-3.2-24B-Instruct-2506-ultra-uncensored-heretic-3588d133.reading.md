# Reading of the Stage 1 and Stage 2 result: llmfan46/Mistral-Small-3.2-24B-Instruct-2506-ultra-uncensored-heretic against mistralai/Mistral-Small-3.2-24B-Instruct-2506 (2026-10-31)

Measured on Blueback, round 14 piece 6 (push card 5421, download job 3401154, compare job 3401160; pulled home by
card 5533). Modified revision `481769bd` (the repository was created on 2026-03-19; sixteen later commits edit the
README), original pinned at `95a6d26c` (2025-12-22). The card says Heretic v1.2.0 with arbitrary-rank ablation,
`o_proj` only, start layer 7, end layer 35.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 8 flags, on the
cluster and after re-scoring at home, all energy shares (0.941 to 0.979).

- 8 of 585 tensors changed above the threshold: the attention outputs of layers 12, 15, 16, 18, 19, 25, 30 and 31.
  Twenty more attention outputs inside the card's range of 7 to 34 were rewritten under the threshold, at
  relative change 0.000097 to 0.000225 (the largest change outside the changed set is that 0.000225); the search
  weighted them near zero and the rewrite left bfloat16 traces, the residue pattern of finding 22. No down
  projection moved.
- Input side: the left kept fraction is −0.04 to 0.43 and the right −4.28 to −1.62, the left above the right on 8
  of 8. One minus the right kept fraction is 2.62 to 5.28, the largest searched weights on a Mistral base so far
  (layer 15 at 5.28, relative change 0.100).
- First-value share 0.941 to 0.979 and first-eight 0.986 to 0.994, the arbitrary-rank residue beyond one
  direction; cross-layer cosine 0.27 to 0.44. Row norms moved by 0.011 to 0.052.

| Layer | Attention output: change, E1, E8, left kept, right kept | Weight read | Cross-layer cosine | Row norms |
| --- | --- | --- | --- | --- |
| 12 | 0.0733, 0.969, 0.994, 0.00, -3.99 | 4.99 | 0.38 | 0.0253 |
| 15 | 0.1000, 0.957, 0.991, -0.04, -4.28 | 5.28 | 0.44 | 0.0522 |
| 16 | 0.0756, 0.971, 0.992, 0.31, -2.84 | 3.84 | 0.42 | 0.0340 |
| 18 | 0.0670, 0.978, 0.990, 0.33, -2.00 | 3.00 | 0.39 | 0.0288 |
| 19 | 0.0477, 0.968, 0.989, 0.43, -1.62 | 2.62 | 0.35 | 0.0107 |
| 25 | 0.0643, 0.946, 0.989, 0.24, -2.04 | 3.04 | 0.27 | 0.0300 |
| 30 | 0.0620, 0.941, 0.987, 0.32, -1.71 | 2.71 | 0.30 | 0.0223 |
| 31 | 0.0605, 0.950, 0.986, 0.10, -1.94 | 2.94 | 0.29 | 0.0169 |

The weight read is one minus the right kept fraction, the input side. Against huihui-ai's copy of the same base
(round 13 pair 5, one shared direction at weight 0.99 on 80 matrices, output side), no changed matrix has an equal
measurement in any field; the two copies stand on one weight file under two revisions of the original (`1483f238`
and `95a6d26c`, shards `91831c2c` and following).

## Token and configuration side (Stage 1)

"Unexplained differences", 1,025 fields, and the judgement is the same as for huihui-ai's copy: a third party's
conversion of an original that ships no library tokenizer (finding 31). The original at the pin has `tekken.json`;
the copy ships a `tokenizer.json` of 17,078,174 bytes (`c46ef3c5`), a 423-byte tokenizer configuration re-saved
under transformers 5.3.0, a special-tokens map (`eea95589`) that is unsloth's file byte for byte, a template of
15,182 bytes that is unsloth's revision `3ed8d341` (2025-08-26) after the removal of 299 carriage returns, a
configuration with `unsloth_fixed: true`, and generation settings with the conversion's seven fields. The rotary
settings' `rope_parameters` form closed at home as a library re-save. The fixed conversation renders identically
with the conversion's template.

## For the recipe library

Consistent with the card: attention outputs only inside layers 7 to 34, eight above the threshold and twenty left
as residues, input side, arbitrary rank, searched weights 2.62 to 5.28, the twelfth arbitrary-rank copy (finding
22) and the second on a Mistral base. The saved direction vectors are not committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/blueback14/measurements/pair-6/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
