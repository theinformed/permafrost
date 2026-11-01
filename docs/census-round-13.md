# Census round 13: eight Gemma 4 and Mistral pairs (2026-10-31)

Eight published copies compared with their stated originals on Blueback, 2026-10-30, from the batch pinned as
`data/batches/round-13-batch-1.json`: push card 5404 (21:01Z), round card placed at 21:20Z, download job 3400579 on
the transfer queue (finished 22:34Z, checksums of all sixteen sides verified), compares 3400580 to 3400587 on the
background queue, sweep 3400588 behind them. The compares ran before the job-report fix of commit f7f4eeb and
posted no finish records; the desk cleared them as silent on 10-31. Compare 3400584 (pair 5) wrote its weight
comparison and stopped in the metadata step on the original's `generation_config.json`, which is not valid JSON at
the pin, so the sweep's condition was never met and the round's originals stay on Blueback until the purge window
takes them. Cards 5529 and 5530 pulled the logs and the measurements home. Pair 5's token side was built at home from
the small files of both sides with the same code path (`hpc/rounds/2/measure.py read_document` now reads such a
file; commit 6a08e37). The eight measurements were re-scored at home with the recipe table as committed and the
saved direction vectors, and no flag count moved. Every metadata report was judged again at home under transformers
5.6.2 with the originals' commit histories. Each pair has a card and a reading note in `docs/cards/`; the
measurements are in `results/weights/` and `results/meta/`, and the direction vectors stay in the pull copy
(`/opt/ai/hpc-packages/pulls/model-audit/blueback13/measurements/pair-N/`).

| Pair | Copy | Original | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | TrevorJS/gemma-4-E2B-it-uncensored | google/gemma-4-E2B-it | violations, 3 flags | consistent: norm-preserving biprojection on both writers of all 35 layers, one direction per layer, output side, rows within 0.0005; the maker's fifth size with the same fingerprint |
| 2 | huihui-ai/Huihui-gemma-4-E2B-it-abliterated | google/gemma-4-E2B-it | match, 0 flags | consistent: one shared direction at weight 1.00 on the 50 writers of layers 10 to 34, the card's "first 10 layers have not been abliterated"; equal in every field to prithivMLmods's E2B copy of round 18 |
| 3 | AEON-7/Gemma-4-12B-it-AEON-Abliterated-K4-BF16 | google/gemma-4-12B-it | violations, 90 flags (energy shares, within-layer directions) | consistent in every stated number: four directions per matrix (first four 0.996 to 0.997), one four-dimensional subspace across the 48 writers of the card's 24 layers, output side, rows within 0.0004 |
| 4 | huihui-ai/Huihui-gemma-4-12B-it-abliterated | google/gemma-4-12B-it | match, 0 flags | consistent: one shared direction at weight 1.00 on the 12 writers of layers 23 to 28, the card's "Only layers 23-28", output side |
| 5 | huihui-ai/Huihui-Mistral-Small-3.2-24B-Instruct-2506-abliterated | mistralai/Mistral-Small-3.2-24B-Instruct-2506 | match, 0 flags | consistent: one shared direction at weight 0.99 on all 80 writers, output side, inside the calibration envelope made on this base; the token side is a third party's conversion and the original's generation file is invalid JSON |
| 6 | grimjim/mistralai-Mistral-Nemo-Instruct-2407-extensive-BP-abliteration-12B | mistralai/Mistral-Nemo-Instruct-2407 | violations, 34 flags (floor) | consistent with the card's three sentences: both writers of layers 3 to 37, three block directions (layers 3 to 16, 17 to 21, 22 to 37), weight 1.0, output side; rows moved up to 0.032 under a method named for preserving them |
| 7 | DuoNeural/Mistral-NeMo-12B-Abliterated | mistralai/Mistral-Nemo-Instruct-2407 | violations, 80 flags (floor) | consistent in every stated number: one shared direction on all 80 writers at weight 0.29 to 0.30, the card's α 0.3, output side |
| 8 | llmfan46/gemma-4-12B-it-uncensored-heretic | google/gemma-4-12B-it | violations, 15 flags (energy shares) | consistent: arbitrary-rank edits on the attention outputs of layers 24 to 39, input side, searched weights 0.32 to 3.63; the eleventh arbitrary-rank copy |

Nothing moved outside the matrices the maker's method reaches in any pair: the largest relative change outside
the changed set is exactly 0 in pairs 1, 2, 3, 4, 5, 7 and 8 and 0.000096 in pair 6, a few bfloat16 values in three
matrices of layers 0 and 39. The round's result is eight copies that read as their cards say, two of them with no
flag, and the first round in which every pair closes. Pair 3 is the second subspace method in the census with its
rank stated in the card after round 18's null-space copy, and the first whose directions number four: the first
four singular values are near equal and the fourth is 19 to 195 times the fifth, and the 48 leading vectors span
one four-dimensional subspace (99.4 percent of their energy in four directions). Pair 7 is the first copy whose
shared weight reads below one half on every matrix, 0.29 to 0.30 against a card that says 0.3, on a base the card
says was already compliant. Pair 2 closes finding 9's E2B case: prithivMLmods/gemma-4-E2B-it-Uncensored-MAX equals
it in every field of all 2,011 tensors and every singular value.

The weights read off the weights: 1.00 on pair 2's 50 matrices and pair 4's 12 (−0.005 to 0.005 remaining), 0.99 on
pair 5's 80 (0.006 to 0.008), 1.0 on pair 6's 70 (−0.003 to 0.005), 0.29 to 0.30 on pair 7's 80, searched per-layer
weights of 0.32 to 3.63 on pair 8's input side (left above right on all 16). Pair 1 reads near 0 kept on most layers
with 0.24 to 0.69 on three, the biprojection's second term; pair 3 reads no single weight because four directions
are removed at once, and the first-four share reads the edit instead. The side read on all eight: output on pairs 1
to 7 (left below right on 34 of 35 per kind on pair 1, 47 of 48 on pair 3, all matrices on the rest), input on
pair 8.

Three preservation claims. Pairs 1 and 3 hold theirs within 0.0005 and 0.0004. Pair 6's rows moved by 0.004 to
0.032 under a method whose name carries norm preservation and whose published scripts hold it on TrevorJS's five
copies; this copy reads as a plain projection. Pairs 2, 4, 5 and 7 claim nothing and read the unrestored leftover
(0.006 to 0.079).

Fingerprints. Five measurements now stand on the one E2B weight file (shard `2db5482b` under three revisions of the
original: TrevorJS, huihui-ai, prithivMLmods, aifeifei798, llmfan46) and pair 2 equals prithivMLmods's in every
field, a re-upload; pair 1 shares no field with any of the four. Eight copies stand on the 12B file (igorls,
TrevorJS, coder3101, 3MPER0RR, richardyoung, lemuralabs and this round's AEON-7, huihui-ai and llmfan46) and no
changed matrix of pairs 3, 4 or 8 has an equal measurement in any field of the others; the leading output-side
vectors of igorls (0.60 to 0.61), huihui-ai (0.56 to 0.79), 3MPER0RR (0.37 to 0.47) and richardyoung (0.34 to 0.49)
lie partly inside pair 3's four-dimensional subspace and the input-side copies (llmfan46 about 0.1, coder3101 about
0.07) do not. Pairs 6 and 7 on the Nemo file share no field. Pair 5 shares no field with the calibration edit on
the same base or with llmfan46's copy of round 14.

## The token side

The cluster's cards read "consistent" on pair 2 and "unexplained differences" on the six that reached the metadata
step; pair 5's was built at home. Re-judged at home, one field closes by tool on pair 1
(`config.text_config.moe_intermediate_size`, the 5.6.2 default) and its card moves to "consistent with re-save
noted"; the rest close by hand:

- Nothing to close, pair 2: every small file equals Google's except the template, which is Google's release file
  with carriage-return line endings. Re-save only, pair 1: 5.5.0.dev0 to 5.5.0 in two version strings.
- The class defaults and a revision, pair 3: the six class-default fields of finding 11 under one 5.10.0.dev0 save,
  and `text_config.max_position_embeddings` 131,072 at the pin against 262,144 in the copy. The copy's own
  history carries that change (its commit of 06-07, "Restore native 256k context") three days after Google's commit
  `5926caa4` made the same one; the copy's pin is the revision before Google's change. Judged again under transformers
  5.22.1 after the home environment moved, the six class-default fields close on pairs 3 and 8; `max_position_embeddings`
  stays pair 3's one open field and pair 8 keeps its template (finding 39).
- The earlier-revision case, pair 4: the one unexplained field is the same `max_position_embeddings`, read the
  other way, because the copy's configuration is Google's `66bc78a7` file of 06-03 byte for byte and the pin rule
  chose `5926caa4` of 06-04 from the copy's squashed history of 06-07.
- Two re-saves, pairs 6 and 7: `torch_dtype` renamed `dtype` under 4.57.1 (pair 6), and under 5.10.1 the 1,000
  added tokens moved into `tokenizer.json`, the rotary settings into `rope_parameters`, the template into
  `chat_template.jinja` (pair 7, 1,006 fields).
- A patched template, pair 8: the class defaults under 5.10.2 and a template of 21,488 bytes that is Google's
  pinned file plus the maker's `format_type_argument` macro and two guards, the same macro as the maker's 26B-A4B
  copy carries and without the thought-block patch of finding 23.
- An original without a library tokenizer, pair 5: the original at the pin ships `config.json` and a
  `generation_config.json` only, with its tokenizer in `tekken.json`, and the copy ships unsloth's conversion
  files (tokenizer configuration, special-tokens map and template byte for byte at unsloth's revisions of
  2025-06-20 to 06-23) and the conversion's seven generation fields. The original's generation file was invalid
  JSON from the release commit of 2025-06-20 until Mistral's fix of 07-07; under transformers 5.6.2 a strict load
  of the pinned revision raises an error on it and the model loader falls back to settings built from the model
  configuration, which drops the temperature of 0.15.

Every fixed conversation renders identically. Six of the eight copies carry the template they were pinned against
or the same text with a formatting difference; pair 8 carries a patched Google template and pair 5 a conversion's.

## What the scorer learned

The flag counts are the same on the cluster and at home. Their causes, by pair:

- Four directions, 90 flags (pair 3): first shares 0.26 to 0.32 with the first four at 0.996 to 0.997, read by the
  energy-share rule as 48 failed projections, and 42 within-layer cosines between leading vectors drawn from one
  four-dimensional mixture. A first-k share with k read from the singular values (the fourth is 19 to 195 times
  the fifth here) names it as one number per matrix, the request rounds 16 and 18 made.
- The floor, 34 and 80 flags (pairs 6 and 7): first shares 0.987 to 0.995 on changes of 0.013 to 0.022, and 0.916
  to 0.950 on changes of 0.0042 to 0.0058, the fixed bfloat16 leftover on a weak edit; pair 7 is the clearest case
  of finding 3 so far, a weight of 0.3 producing shares the rule reads as failure on every matrix.
- Arbitrary rank, 15 flags (pair 8): first shares 0.914 to 0.983 on 15 of 16, with the first eight at 0.957 to
  0.997.
- A per-layer direction read twice, 3 flags (pair 1): one first share at 0.988 and two within-layer cosines at
  0.943 where the two writers of a layer carry directions measured at that layer.
- Nothing, on pairs 2, 4 and 5: the selected single-projection and per-layer entries matched the two huihui-ai
  Gemma copies, and the calibration entry made on Mistral Small 3.2 on 2026-10-14 matched its first published copy.

Two things the comparison could say by itself. A rank per matrix from the singular-value gaps, with a subspace test
across layers (the stacked leading vectors' singular values), which would have reported pair 3 as "rank 4, one
subspace, 48 matrices" and pair 6 as "three block directions". And the conversion lookup round 18 asked for, which
at home closed pair 5 by matching the copy's three files to unsloth's revisions by checksum.

## Owed to the metadata tool

A lenient JSON read with the fault named (done in commit 6a08e37; pair 5's report says which file and where); the
conversion lookup as a tool step (pair 5, 1,025 fields, closed at home by hand); the max-position revision pair
(pairs 3 and 4, one field each way, closed from the originals' and the copies' histories). To the batch pinner:
refuse or flag a pair whose original ships no library tokenizer until the conversion is named, and record the
original's later revisions beside the pin when the copy's configuration matches one of them.

Weight differences alone cannot certify the absence of hidden behavior.
