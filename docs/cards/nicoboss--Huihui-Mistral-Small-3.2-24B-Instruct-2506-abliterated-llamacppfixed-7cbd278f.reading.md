# Reading of the Stage 1 and Stage 2 result: nicoboss/Huihui-Mistral-Small-3.2-24B-Instruct-2506-abliterated-llamacppfixed against mistralai/Mistral-Small-3.2-24B-Instruct-2506 (2026-10-31)

Measured on Nautilus, round 19 piece 8 (push card 5605, probe card 5616, round card 5626, download job 4142666, compare job 4142674 on the background queue, sweep 4142675; pulled home by card 5647). Modified revision `ebd022dd` (2025-07-07 at 15:16Z, "Upload 6 files",
fourteen minutes after the repository's first commit "Duplicate from
huihui-ai/Huihui-Mistral-Small-3.2-24B-Instruct-2506-abliterated"), original pinned at `1483f238` (2025-06-22).
The README is huihui-ai's, 7,224 bytes, byte for byte, and names the source's method (abliteration with the
remove-refusals tooling) and nothing of the fix; the name says the copy is the huihui-ai copy with its tokenizer
repaired for llama.cpp.

## Weights (Stage 2)

The tool's assessment was "recipe match", recipe `single-projection/mistral-small-3.2-24b`, 0 flags, on the
cluster and after re-scoring at home. The weight file is huihui-ai's: the ten shards carry the same LFS checksums
in both repositories (`b6c0aee6` to `101361dc`), the comparison read the same ten shard checksums, and every
measured field of all 585 tensors equals the round 13 report
(`results/weights/huihui-ai-Huihui-Mistral-Small-3.2-24B-Instruct-2506-abliterated.json`): 80 changed, every
attention output and down projection, one shared direction (cross-layer cosine 1.000), weight 1.0 on the output
side (left kept 0.006 to 0.008, right 0.28 to 0.96), rows moved 0.011 to 0.041, 505 tensors equal to the
original; the calibrated line for this base matches with no flag. The reading is in
`huihui-ai--Huihui-Mistral-Small-3.2-24B-Instruct-2506-abliterated-d9f80c54.reading.md`.

| Layer | Attention output: change, E1, E8, left kept, right kept | Down projection: change, E1, E8, left kept, right kept | Weight read | Within-layer cosine | Cross-layer cosine | Row norms |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0.0221, 0.995, 0.995, 0.01, 0.96 | 0.0164, 0.991, 0.992, 0.01, 0.84 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0410, 0.0223 |
| 1 | 0.0174, 0.992, 0.992, 0.01, 0.92 | 0.0149, 0.989, 0.990, 0.01, 0.63 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0279, 0.0222 |
| 2 | 0.0186, 0.993, 0.993, 0.01, 0.91 | 0.0146, 0.989, 0.990, 0.01, 0.56 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0221, 0.0220 |
| 3 | 0.0175, 0.992, 0.993, 0.01, 0.89 | 0.0143, 0.989, 0.989, 0.01, 0.44 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0248, 0.0219 |
| 4 | 0.0166, 0.991, 0.992, 0.01, 0.85 | 0.0150, 0.989, 0.990, 0.01, 0.49 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0250, 0.0250 |
| 5 | 0.0175, 0.992, 0.993, 0.01, 0.75 | 0.0155, 0.990, 0.991, 0.01, 0.47 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0284, 0.0241 |
| 6 | 0.0177, 0.992, 0.993, 0.01, 0.79 | 0.0156, 0.990, 0.991, 0.01, 0.52 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0274, 0.0231 |
| 7 | 0.0174, 0.992, 0.993, 0.01, 0.74 | 0.0162, 0.991, 0.991, 0.01, 0.46 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0247, 0.0255 |
| 8 | 0.0191, 0.993, 0.994, 0.01, 0.73 | 0.0164, 0.991, 0.992, 0.01, 0.45 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0284, 0.0243 |
| 9 | 0.0210, 0.994, 0.995, 0.01, 0.73 | 0.0174, 0.992, 0.993, 0.01, 0.50 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0268, 0.0261 |
| 10 | 0.0221, 0.995, 0.995, 0.01, 0.75 | 0.0179, 0.993, 0.993, 0.01, 0.54 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0293, 0.0230 |
| 11 | 0.0219, 0.995, 0.995, 0.01, 0.70 | 0.0203, 0.994, 0.994, 0.01, 0.66 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0267, 0.0305 |
| 12 | 0.0215, 0.995, 0.995, 0.01, 0.79 | 0.0186, 0.993, 0.993, 0.01, 0.67 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0378, 0.0271 |
| 13 | 0.0188, 0.993, 0.994, 0.01, 0.81 | 0.0187, 0.993, 0.994, 0.01, 0.75 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0245, 0.0296 |
| 14 | 0.0193, 0.994, 0.994, 0.01, 0.86 | 0.0171, 0.992, 0.992, 0.01, 0.71 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0344, 0.0259 |
| 15 | 0.0184, 0.993, 0.993, 0.01, 0.89 | 0.0163, 0.991, 0.992, 0.01, 0.76 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0261, 0.0235 |
| 16 | 0.0165, 0.991, 0.992, 0.01, 0.82 | 0.0161, 0.991, 0.991, 0.01, 0.77 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0230, 0.0246 |
| 17 | 0.0192, 0.993, 0.994, 0.01, 0.85 | 0.0156, 0.990, 0.991, 0.01, 0.75 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0264, 0.0235 |
| 18 | 0.0157, 0.990, 0.991, 0.01, 0.85 | 0.0153, 0.990, 0.991, 0.01, 0.50 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0239, 0.0216 |
| 19 | 0.0166, 0.991, 0.992, 0.01, 0.88 | 0.0153, 0.990, 0.991, 0.01, 0.62 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0248, 0.0238 |
| 20 | 0.0168, 0.992, 0.992, 0.01, 0.83 | 0.0147, 0.989, 0.990, 0.01, 0.50 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0234, 0.0221 |
| 21 | 0.0163, 0.991, 0.992, 0.01, 0.87 | 0.0145, 0.989, 0.990, 0.01, 0.48 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0223, 0.0220 |
| 22 | 0.0155, 0.990, 0.991, 0.01, 0.84 | 0.0148, 0.989, 0.990, 0.01, 0.59 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0232, 0.0236 |
| 23 | 0.0159, 0.990, 0.991, 0.01, 0.82 | 0.0144, 0.989, 0.989, 0.01, 0.45 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0220, 0.0226 |
| 24 | 0.0155, 0.990, 0.991, 0.01, 0.84 | 0.0143, 0.989, 0.989, 0.01, 0.54 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0227, 0.0201 |
| 25 | 0.0169, 0.992, 0.992, 0.01, 0.85 | 0.0141, 0.988, 0.989, 0.01, 0.37 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0234, 0.0202 |
| 26 | 0.0157, 0.990, 0.991, 0.01, 0.84 | 0.0141, 0.988, 0.989, 0.01, 0.44 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0235, 0.0185 |
| 27 | 0.0164, 0.991, 0.992, 0.01, 0.82 | 0.0139, 0.988, 0.989, 0.01, 0.28 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0222, 0.0175 |
| 28 | 0.0145, 0.989, 0.990, 0.01, 0.84 | 0.0137, 0.988, 0.988, 0.01, 0.30 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0216, 0.0169 |
| 29 | 0.0162, 0.991, 0.991, 0.01, 0.87 | 0.0138, 0.988, 0.989, 0.01, 0.34 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0234, 0.0176 |
| 30 | 0.0137, 0.988, 0.988, 0.01, 0.79 | 0.0137, 0.988, 0.988, 0.01, 0.37 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0190, 0.0190 |
| 31 | 0.0140, 0.988, 0.989, 0.01, 0.70 | 0.0138, 0.988, 0.989, 0.01, 0.41 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0178, 0.0183 |
| 32 | 0.0139, 0.988, 0.989, 0.01, 0.72 | 0.0137, 0.988, 0.988, 0.01, 0.50 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0192, 0.0196 |
| 33 | 0.0141, 0.988, 0.989, 0.01, 0.71 | 0.0137, 0.988, 0.988, 0.01, 0.51 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0162, 0.0186 |
| 34 | 0.0138, 0.988, 0.988, 0.01, 0.70 | 0.0136, 0.987, 0.988, 0.01, 0.40 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0186, 0.0110 |
| 35 | 0.0138, 0.988, 0.989, 0.01, 0.68 | 0.0140, 0.988, 0.989, 0.01, 0.79 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0113, 0.0199 |
| 36 | 0.0145, 0.989, 0.989, 0.01, 0.90 | 0.0141, 0.988, 0.989, 0.01, 0.82 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0167, 0.0193 |
| 37 | 0.0138, 0.988, 0.989, 0.01, 0.87 | 0.0137, 0.988, 0.988, 0.01, 0.43 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0169, 0.0151 |
| 38 | 0.0138, 0.988, 0.989, 0.01, 0.84 | 0.0139, 0.988, 0.989, 0.01, 0.73 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0177, 0.0196 |
| 39 | 0.0145, 0.989, 0.989, 0.01, 0.81 | 0.0140, 0.988, 0.989, 0.01, 0.39 | 0.99/0.99 | 1.000 | 1.00/1.00 | 0.0160, 0.0130 |

## Token and configuration side (Stage 1)

"Unexplained differences" on 2,025 fields on the cluster and at home, against the parent's 1,025, with the four
items the tool marks missing on the original's side (no `tokenizer.json`, tokenizer configuration or template in
Mistral's repository, which ships `tekken.json`). The thousand extra fields are the repair. The parent shipped
unsloth's tokenizer configuration and special-tokens map and no `tokenizer.json`, so its token ids could not be
resolved (ten "token ID unresolved" items in round 13). This copy adds a `tokenizer.json` of 17,078,037 bytes
(`b76085f9`; neither unsloth's 17,078,019-byte file nor the 17,078,174-byte file llmfan46's copy carries), a
`chat_template.json` of 2,772 bytes, and rewrites the tokenizer configuration (198,120 bytes against 213,240) and
the special-tokens map (21,449 against 21,440). With the file present the ids resolve (beginning 1, end 2, padding
11, unknown 0) and the `added_tokens.tokenizer` table and both vocabulary sizes (131,072) appear as fields the
parent's report lacked. In the added-token table 998 of the 1,000 entries equal the parent's; ids 32 and 33 read
`<SPECIAL_32>` and `<SPECIAL_33>` where the parent's files say `[ARGS]` and `[CALL_ID]`, and the same two strings
leave the additional-special-tokens lists. The configuration, generation settings and template are the parent's
byte for byte (1,349, 180 and 14,722 bytes), that is, unsloth's conversion with its seven generation fields
(finding 32). None of the 2,025 fields is a change the original can be compared on; the repair is of the kind the
name claims, a library tokenizer file added and two token names changed, with the weights untouched.

## For the recipe library

Nothing new on the weights: a byte-identical re-upload of huihui-ai's copy with its token files repaired, the
fourth re-upload of this round and the first whose change is the token side alone. The census's lookup of a copy's
tokenizer files against the conversions it has cached (finding 31) would name unsloth's files for the three
unchanged ones and would have nothing to name for the added `tokenizer.json`, which matches no file the census has
seen.
