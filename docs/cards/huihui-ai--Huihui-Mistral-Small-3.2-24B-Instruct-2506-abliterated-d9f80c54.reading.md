# Reading of the Stage 1 and Stage 2 result: huihui-ai/Huihui-Mistral-Small-3.2-24B-Instruct-2506-abliterated against mistralai/Mistral-Small-3.2-24B-Instruct-2506 (2026-10-31)

Measured on Blueback, round 13 piece 5 (push card 5404, download job 3400579, compare job 3400584; pulled home by
card 5530). Modified revision `7526a405` (the weights were uploaded on 2025-07-02 at 17:31Z), original pinned at
`1483f238` (2025-06-27). The card says the copy was made with the maker's remove-refusals script and nothing more
about layers or scale. The compare job wrote the weight comparison and the saved direction vectors and then
stopped in the metadata step: the original's `generation_config.json` at the pin is not valid JSON (a trailing
comma after `"temperature": 0.15`), and the kit's JSON parsing at that commit rejected it. The small files of both sides were
fetched at home and the token side was judged with the same code path and a lenient reader; the metadata report
carries a `home_measurement` note saying so.

## Weights (Stage 2)

The tool's assessment was "recipe match", recipe `single-projection/mistral-small-3.2-24b`, 0 flags, on the
cluster and after re-scoring at home. That recipe entry is the calibration edit made on this base on 2026-10-14
(`audit/calibration/mistral-small-3.2-24b.json`); this is the first published copy to fall inside it, and none of
its fields equals the calibration run's.

- 80 of 585 tensors changed: the attention output and the down projection of all 40 layers. Nothing else moved;
  the largest relative change outside the changed set is exactly 0 and 505 tensors equal the original.
- One shared direction: cross-layer cosine 1.000 on all 80 matrices. First-value share 0.987 to 0.995, relative
  change 0.014 to 0.022.
- The left kept fraction is 0.006 to 0.008 on all 80, a weight of 0.99; the right is 0.28 to 0.96 and the left is
  below the right on 80 of 80, an output-side edit.
- Row norms moved by 0.011 to 0.041, the unrestored leftover of a plain projection.

| Layer | Attention output: change, E1, E8, left kept, right kept | Down projection: change, E1, E8, left kept, right kept | Weight read | Cross-layer cosine | Row norms |
| --- | --- | --- | --- | --- | --- |
| 0 | 0.0221, 0.995, 0.995, 0.01, 0.96 | 0.0164, 0.991, 0.992, 0.01, 0.84 | 0.99/0.99 | 1.00/1.00 | 0.0410, 0.0223 |
| 1 | 0.0174, 0.992, 0.992, 0.01, 0.92 | 0.0149, 0.989, 0.990, 0.01, 0.63 | 0.99/0.99 | 1.00/1.00 | 0.0279, 0.0222 |
| 2 | 0.0186, 0.993, 0.993, 0.01, 0.91 | 0.0146, 0.989, 0.990, 0.01, 0.56 | 0.99/0.99 | 1.00/1.00 | 0.0221, 0.0220 |
| 3 | 0.0175, 0.992, 0.993, 0.01, 0.89 | 0.0143, 0.989, 0.989, 0.01, 0.44 | 0.99/0.99 | 1.00/1.00 | 0.0248, 0.0219 |
| 4 | 0.0166, 0.991, 0.992, 0.01, 0.85 | 0.0150, 0.989, 0.990, 0.01, 0.49 | 0.99/0.99 | 1.00/1.00 | 0.0250, 0.0250 |
| 5 | 0.0175, 0.992, 0.993, 0.01, 0.75 | 0.0155, 0.990, 0.991, 0.01, 0.47 | 0.99/0.99 | 1.00/1.00 | 0.0284, 0.0241 |
| 6 | 0.0177, 0.992, 0.993, 0.01, 0.79 | 0.0156, 0.990, 0.991, 0.01, 0.52 | 0.99/0.99 | 1.00/1.00 | 0.0274, 0.0231 |
| 7 | 0.0174, 0.992, 0.993, 0.01, 0.74 | 0.0162, 0.991, 0.991, 0.01, 0.46 | 0.99/0.99 | 1.00/1.00 | 0.0247, 0.0255 |
| 8 | 0.0191, 0.993, 0.994, 0.01, 0.73 | 0.0164, 0.991, 0.992, 0.01, 0.45 | 0.99/0.99 | 1.00/1.00 | 0.0284, 0.0243 |
| 9 | 0.0210, 0.994, 0.995, 0.01, 0.73 | 0.0174, 0.992, 0.993, 0.01, 0.50 | 0.99/0.99 | 1.00/1.00 | 0.0268, 0.0261 |
| 10 | 0.0221, 0.995, 0.995, 0.01, 0.75 | 0.0179, 0.993, 0.993, 0.01, 0.54 | 0.99/0.99 | 1.00/1.00 | 0.0293, 0.0230 |
| 11 | 0.0219, 0.995, 0.995, 0.01, 0.70 | 0.0203, 0.994, 0.994, 0.01, 0.66 | 0.99/0.99 | 1.00/1.00 | 0.0267, 0.0305 |
| 12 | 0.0215, 0.995, 0.995, 0.01, 0.79 | 0.0186, 0.993, 0.993, 0.01, 0.67 | 0.99/0.99 | 1.00/1.00 | 0.0378, 0.0271 |
| 13 | 0.0188, 0.993, 0.994, 0.01, 0.81 | 0.0187, 0.993, 0.994, 0.01, 0.75 | 0.99/0.99 | 1.00/1.00 | 0.0245, 0.0296 |
| 14 | 0.0193, 0.994, 0.994, 0.01, 0.86 | 0.0171, 0.992, 0.992, 0.01, 0.71 | 0.99/0.99 | 1.00/1.00 | 0.0344, 0.0259 |
| 15 | 0.0184, 0.993, 0.993, 0.01, 0.89 | 0.0163, 0.991, 0.992, 0.01, 0.76 | 0.99/0.99 | 1.00/1.00 | 0.0261, 0.0235 |
| 16 | 0.0165, 0.991, 0.992, 0.01, 0.82 | 0.0161, 0.991, 0.991, 0.01, 0.77 | 0.99/0.99 | 1.00/1.00 | 0.0230, 0.0246 |
| 17 | 0.0192, 0.993, 0.994, 0.01, 0.85 | 0.0156, 0.990, 0.991, 0.01, 0.75 | 0.99/0.99 | 1.00/1.00 | 0.0264, 0.0235 |
| 18 | 0.0157, 0.990, 0.991, 0.01, 0.85 | 0.0153, 0.990, 0.991, 0.01, 0.50 | 0.99/0.99 | 1.00/1.00 | 0.0239, 0.0216 |
| 19 | 0.0166, 0.991, 0.992, 0.01, 0.88 | 0.0153, 0.990, 0.991, 0.01, 0.62 | 0.99/0.99 | 1.00/1.00 | 0.0248, 0.0238 |
| 20 | 0.0168, 0.992, 0.992, 0.01, 0.83 | 0.0147, 0.989, 0.990, 0.01, 0.50 | 0.99/0.99 | 1.00/1.00 | 0.0234, 0.0221 |
| 21 | 0.0163, 0.991, 0.992, 0.01, 0.87 | 0.0145, 0.989, 0.990, 0.01, 0.48 | 0.99/0.99 | 1.00/1.00 | 0.0223, 0.0220 |
| 22 | 0.0155, 0.990, 0.991, 0.01, 0.84 | 0.0148, 0.989, 0.990, 0.01, 0.59 | 0.99/0.99 | 1.00/1.00 | 0.0232, 0.0236 |
| 23 | 0.0159, 0.990, 0.991, 0.01, 0.82 | 0.0144, 0.989, 0.989, 0.01, 0.45 | 0.99/0.99 | 1.00/1.00 | 0.0220, 0.0226 |
| 24 | 0.0155, 0.990, 0.991, 0.01, 0.84 | 0.0143, 0.989, 0.989, 0.01, 0.54 | 0.99/0.99 | 1.00/1.00 | 0.0227, 0.0201 |
| 25 | 0.0169, 0.992, 0.992, 0.01, 0.85 | 0.0141, 0.988, 0.989, 0.01, 0.37 | 0.99/0.99 | 1.00/1.00 | 0.0234, 0.0202 |
| 26 | 0.0157, 0.990, 0.991, 0.01, 0.84 | 0.0141, 0.988, 0.989, 0.01, 0.44 | 0.99/0.99 | 1.00/1.00 | 0.0235, 0.0185 |
| 27 | 0.0164, 0.991, 0.992, 0.01, 0.82 | 0.0139, 0.988, 0.989, 0.01, 0.28 | 0.99/0.99 | 1.00/1.00 | 0.0222, 0.0175 |
| 28 | 0.0145, 0.989, 0.990, 0.01, 0.84 | 0.0137, 0.988, 0.988, 0.01, 0.30 | 0.99/0.99 | 1.00/1.00 | 0.0216, 0.0169 |
| 29 | 0.0162, 0.991, 0.991, 0.01, 0.87 | 0.0138, 0.988, 0.989, 0.01, 0.34 | 0.99/0.99 | 1.00/1.00 | 0.0234, 0.0176 |
| 30 | 0.0137, 0.988, 0.988, 0.01, 0.79 | 0.0137, 0.988, 0.988, 0.01, 0.37 | 0.99/0.99 | 1.00/1.00 | 0.0190, 0.0190 |
| 31 | 0.0140, 0.988, 0.989, 0.01, 0.70 | 0.0138, 0.988, 0.989, 0.01, 0.41 | 0.99/0.99 | 1.00/1.00 | 0.0178, 0.0183 |
| 32 | 0.0139, 0.988, 0.989, 0.01, 0.72 | 0.0137, 0.988, 0.988, 0.01, 0.50 | 0.99/0.99 | 1.00/1.00 | 0.0192, 0.0196 |
| 33 | 0.0141, 0.988, 0.989, 0.01, 0.71 | 0.0137, 0.988, 0.988, 0.01, 0.51 | 0.99/0.99 | 1.00/1.00 | 0.0162, 0.0186 |
| 34 | 0.0138, 0.988, 0.988, 0.01, 0.70 | 0.0136, 0.987, 0.988, 0.01, 0.40 | 0.99/0.99 | 1.00/1.00 | 0.0186, 0.0110 |
| 35 | 0.0138, 0.988, 0.989, 0.01, 0.68 | 0.0140, 0.988, 0.989, 0.01, 0.79 | 0.99/0.99 | 1.00/1.00 | 0.0113, 0.0199 |
| 36 | 0.0145, 0.989, 0.989, 0.01, 0.90 | 0.0141, 0.988, 0.989, 0.01, 0.82 | 0.99/0.99 | 1.00/1.00 | 0.0167, 0.0193 |
| 37 | 0.0138, 0.988, 0.989, 0.01, 0.87 | 0.0137, 0.988, 0.988, 0.01, 0.43 | 0.99/0.99 | 1.00/1.00 | 0.0169, 0.0151 |
| 38 | 0.0138, 0.988, 0.989, 0.01, 0.84 | 0.0139, 0.988, 0.989, 0.01, 0.73 | 0.99/0.99 | 1.00/1.00 | 0.0177, 0.0196 |
| 39 | 0.0145, 0.989, 0.989, 0.01, 0.81 | 0.0140, 0.988, 0.989, 0.01, 0.39 | 0.99/0.99 | 1.00/1.00 | 0.0160, 0.0130 |

Against llmfan46's copy of the same base (round 14 pair 6, measured on the same weight file under revision
`95a6d26c`), no changed matrix has an equal measurement in any field.

## Token and configuration side (Stage 1)

"Unexplained differences", 1,025 fields, and the judgement is a conversion, not an edit. The original at the pin
ships `config.json` and `generation_config.json` only, with its tokenizer in `tekken.json`; the copy ships a
tokenizer configuration of 213,240 bytes (`03c113fd`), a special-tokens map (`eea95589`) and a template of
14,722 bytes (`cafc16d3`) that are byte for byte the files of unsloth's conversion of this model at its revisions
`42cd5fdb`, `ff984dcd` and `776efdbd` of 2025-06-20 to 06-23, and no `tokenizer.json`. The 1,010 token fields are
the conversion's added-token table with no original to compare against, and the token identities stay unresolved
because the copy has no `tokenizer.json`. The copy's generation settings (180 bytes) carry the conversion's seven
fields (beginning, end and padding tokens, sampling on, a maximum length of 131,072, temperature 0.15, version
4.52.4) and not the original's two. The original's own file was invalid JSON from the release commit of 2025-06-20
until Mistral's fix of 2025-07-07 (`46a27874`, "fix invalid json file"); under transformers 5.6.2 a strict load of
the pinned original raises an error on that file and the model loader falls back to settings built from the model
configuration, dropping the temperature. The fixed conversation renders identically with the conversion's
template.

## For the recipe library

Consistent with the card as far as it goes: one shared direction at weight 0.99 on both writers of every layer,
output side, rows unrestored, and inside the calibration envelope for a single projection on this base. The saved
direction vectors are not committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/blueback13/measurements/pair-5/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
