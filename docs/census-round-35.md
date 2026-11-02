# Census round 35: eight pairs on Wheat, three of them copies measured again against the parents their cards name (2026-11-02)

Eight published copies compared with their originals on Wheat from the batch pinned as
`data/batches/round-35-batch-1.json` (pinned 2026-11-02 03:44Z) under the image-free kit with the standalone
Python: download job 387143, compares 387144 to 387151, sweep 387152, which deleted the seven originals
(`52250dca` of google/gemma-4-E4B-it at `fee6332c` for pair 1, `db9bfb44` of TheDrummer/Artemis-31B-v1.1 for pair
2, `65eb5edf` of LatitudeGames/Hearthfire-24B for pair 3, `ae782a34` of google/gemma-4-31B-it at `419b2efe` for
pair 4, `6b9df1e0` of google/gemma-4-E2B-it for pair 5, `c81b1ac4` of google/gemma-4-12B-it for pair 6 and
`a0104340` of the E4B QAT-unquantized checkpoint shared by pairs 7 and 8) from
`/p/work/sdegan/model-audit/rounds/35/originals/`. The pull brought home the eight measurement folders and the
sweep record and no job log, so the compares' nodes and seconds are not in this note. The round is special in
three ways. Pairs 1 to 3 measure a copy the census had measured once, with the same weight files, against the
parent its card or its bytes named: Felldude's E4B against the instruct model (round 29 measured it against the
pretrained base its field names, finding 62), sh0ck0r's Artemis heretic against TheDrummer/Artemis-31B-v1.1 (round
20 against Google, finding 45) and Pranavz's heretic against LatitudeGames/Hearthfire-24B (round 29 against Mistral
Small 3.2, finding 61); each new report is stored beside the old one under a suffix naming the parent
(`.vs-E4B-it`, `.vs-Artemis-31B-v1.1`, `.vs-Hearthfire-24B`), and the new report is the reading of record for each
copy, the old one kept as the record of what the field's pin measures. Pair 4 is the first copy whose vision tower
drops the `.linear.` segment inside every encoder linear, paired through the in-tower mapping (the `name_mapping`
block of its weights file records the infix carried by the original and 189 names renamed). Pairs 5 to 8 are
first measurements, two of them on the E4B QAT checkpoint. DuoNeural's DiffusionGemma copy was held at the pin:
its export names 1,674 tensors without the model prefix against the original's 1,047, and nothing pairs. The
eight measurements were re-scored at home with the recipe table as committed and the saved direction vectors, and
no flag count moved. Every metadata report was judged again at home under transformers 5.22.1 with the originals'
later commits; the home judgement moved one field on pair 2, one on pair 3, one on pair 4 (which turned its
reading to consistent with re-save noted) and four on pair 6, and none on the other four. Each pair has a card
(the tool's Stage 1 text after the home judgement, with the Stage 2 line) and a reading note in `docs/cards/`; the
measurements are in `results/weights/` and `results/meta/`, and the direction vectors stay in the pull copy
(`/opt/ai/hpc-packages/pulls/model-audit/wheat35/measurements/pair-N/`).

| Pair | Copy | Original | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | Felldude/gemma-4-E4B-uncensored (second measurement) | google/gemma-4-E4B-it | violations, 304 flags (187 unexpected changes, 58 first shares, 58 direction cosines, one cross-kind) | a light training pass on two bands of layers: 245 of 2,076 tensors changed by 0.1 to 0.7 percent on layers 0 to 14 and 27 to 41 (the queries, keys, values, gates, ups, both writers, the per-layer gates and projections), layers 15 to 26 at 0.0001 or less, the towers and embeddings equal, no direction (first shares 0.001 to 0.016, kept fractions within 0.03 of 1); round 29's range reads predicted the numbers within 0.0001; the token side consistent |
| 2 | sh0ck0r/Artemis-31B-v1.1-heretic (second measurement) | TheDrummer/Artemis-31B-v1.1 | violations, 45 flags (first shares 0.922 to 0.990) | the clean Heretic 1.4.0 edit the card prints: both writers in both kernel windows exactly (attention outputs 25 to 59, down projections 17 to 54), one direction, output side on 69 of 73, the down kernel within 0.04 of the card on layers 43 to 54 and under by up to 0.62 at the peak, the attention kernel within 0.10 on 18 of 35 layers, rows 0.001 to 0.007 under the "full" normalisation claim; exactly 0 outside; the 5.16 save form on the configuration |
| 3 | Pranavz/Hearthfire-24B-heretic (second measurement) | LatitudeGames/Hearthfire-24B | violations, 2 flags (within-layer cosines 0.946 and 0.955) | the Heretic 1.2.0 edit the card prints: the down projections of all 40 layers and the attention outputs of 19 to 34, both windows exactly, first shares 0.9985 to 0.9995, the kept fractions equal to round 29's to the second decimal and the leading vectors equal at 1.000 on all 56, the down kernel within 0.07 on 16 layers and under by up to 0.51, the attention heights scattered (1.13 to 3.22 under 3.06 to 3.75); exactly 0 outside; the copy's tokenizer configuration drops Hearthfire's 1,000 control-token declarations |
| 4 | Kooten/gemma-4-31b-abliterated-v1.1 | google/gemma-4-31B-it | violations, 211 flags (189 unexpected changes, 22 first shares) | two things: a Heretic linear-kernel edit of the language stack (down projections 20 to 59, attention outputs 24 to 50, one direction, output side on all 67) whose kernel reads off the weights as straight lines the card does not print (attention 1.47 at layer 37 falling to 0.70 at distance 13, down 1.15 at 54 falling to 0.69 at distance 34), and a vision tower whose 189 encoder linears are fresh draws at a standard deviation of 0.0199 (cosine 0.000 to Google's, relative differences 1.206 and 1.643 as the scale ratios predict) while its norms and embeddings equal Google's; the first pair through the infix mapping |
| 5 | Dzluck/gemma-4-E2B-it-abliterated-v2 | google/gemma-4-E2B-it | match, 0 flags | a re-upload of huihui-ai/Huihui-gemma-4-E2B-it-abliterated-v2 (the same weight file `c1a72f14`, README and token files, no duplicate relation on the hub) and the only measurement of that edit: the maker's shared projection at a weight of 2.50 (left kept -1.500 on all 60) out of both writers of layers 5 to 34, along the first version's direction at 1.000 on the 50 matrices both edit; the template and tokenizer configuration are Google's files at the 04-02 release revision, two months before the re-upload's pin |
| 6 | enkato64bit/SuperGemma-4-12b-abliterated | google/gemma-4-12B-it | violations, 361 flags (232 unexpected changes, 88 first shares, 40 direction cosines, one cross-kind) | a hub duplicate of Jiunsong/SuperGemma-4-12b-abliterated byte for byte (the same single file `e67b7e6c`) and the only measurement of that edit: a projection of one direction at exactly 0.50 out of both writers of layers 14 to 37 under a merged adapter that moves every linear of all 48 layers by 0.1 to 0.7 percent with a steep spectrum, every sixth pair of layers most; the generation file bans 48 token sequences (the JSON fence in twelve spellings, "confidential instructions", "I can give a concise answer", test-code fragments) and sets a 12-gram repeat block; a 28,982-byte template no Google revision carries |
| 7 | coder3101/gemma-4-E4B-it-qat-q4_0-unquantized-heretic | google/gemma-4-E4B-it-qat-q4_0-unquantized | violations, 16 flags (first shares 0.455 to 0.969) | Heretic v1.2.0's arbitrary-rank branch on the attention outputs of layers 20 to 35, the card's start 20 and end 36, input side on 16 of 16 at weights 1.19 to 1.91, several directions per matrix, the down projections exactly 0, rows 0.0065 to 0.0078 under the preservation claim; the right vectors stand at 0.91 to the maker's instruct E4B edit and 0.92 to 0.95 to JokeHer's, NullpoLab's and alphakek's |
| 8 | igorls/gemma-4-E4B-it-qat-q4_0-unquantized-heretic | google/gemma-4-E4B-it-qat-q4_0-unquantized | violations, 64 flags (32 first shares, 32 within-layer cosines) | Heretic's LoRA-rank branch searched with thinking on, as the card says: both writers of layers 21 to 36 at relative changes of 0.10 to 0.21 on the attention outputs, a direction per matrix (within-layer cosines 0.001 to 0.106), input side on 29 of 32 at weights 1.33 to 3.46, rows 0.016 to 0.28 under no claim; no direction shared with any of twenty E4B edits (medians 0.65 or less); its first shard equals prithivMLmods's QAT export's and its fourth is the shared vision tower |

Nothing moved outside the matrices the maker's method reaches in six of the eight pairs: the largest relative
change outside the changed set is exactly 0 on pairs 2, 3, 4, 5, 7 and 8, 0.00099 on pair 1 (the threshold: 17
more language tensors sit just under it, the training's tail) and 0.00096 on pair 6 (eight down projections under
the adapter's tail). The three re-measurements settle their findings. Against the parents their READMEs name,
sh0ck0r's and Pranavz's Heretic edits read as their cards describe them and nothing else: 73 and 56 matrices in
place of 603 and 282, 45 and 2 flags in place of 686 and 347, and the kernels the first pass read through a 9
percent round trip and a 1 percent fine-tune are the kernels read against the parent, to the second decimal on
the kept fractions and at a median cosine of 0.998 and 1.000 on the leading directions. Felldude's copy against
the instruct model is a small fine-tune of two bands of layers, as the round 29 range reads predicted to the
fourth decimal, with the middle twelve layers and both towers untouched. Of the five first measurements, four are
what their cards say (pairs 5, 6, 7 and 8, two of them read as the only measurements of unmeasured parents) and
one carries a change its card does not name: Kooten's vision tower is 189 random matrices under a card that says
"Uncensored using Heretic" and nothing of the tower, finding 63's case a second time, this time with the dropped
`.linear.` segment as the visible trace of how it happened.

The weights read off the weights. Pair 5 keeps -1.500 along the leading output direction on all 60 matrices, a
weight of 2.50; pair 6 keeps 0.50 on all 48 of its ablated writers, a weight of 0.50, the first below one in the
census. Pair 4's kernel reads as two straight lines with their peaks and slopes, a Heretic record recovered from
the weights where the card prints none (finding 59's check in reverse). Pair 2's down kernel reads within 0.04 on
its far side (layers 43 to 54) and under by 0.08 to 0.62 on its near side; pair 3's reads within 0.07 on 16 of 40
layers and the attention heights scatter, as both did when read through the training. Pairs 7 and 8 read
input-side weights of 1.19 to 1.91 and 1.33 to 3.46 with several directions per matrix.

Preservation claims. Pair 7 claims row-norm preservation and reads 0.0065 to 0.0078, the band of finding 22, the
sixth time on this maker's exports. Pair 2's "full" normalisation with a rank-three correction reads 0.0010 to
0.0073. Pairs 3, 4, 5 and 8 claim nothing and read 0.011 to 0.24, 0.004 to 0.53, 0.015 to 0.15 and 0.016 to 0.28;
pair 6's adapter moves rows by 0.0005 or less on the kinds its projection leaves alone.

Fingerprints. Two of the eight copies are other repositories' files: Dzluck's single file `c1a72f14` is
huihui-ai's E2B v2 file and enkato64bit's `e67b7e6c` is Jiunsong's 12B file, both parents unmeasured and both
measured here for the first time through the re-upload (findings 64 and 73 again). Pair 8's first shard
(`62cfc14d`) equals prithivMLmods's QAT E4B export's first and its fourth (`8080cb1a`) is the vision tower shared
across the E4B instruct and QAT releases (finding 75). Pairs 1, 2 and 3 carry the files their first measurements
carried. Pairs 4 and 7 share no checksum with any measured file.

Directions. The round placed its edits against the saved vectors of forty-four earlier measurements without a
download (finding 66's check). The three re-measurements against their own first passes: Pranavz's directions
equal at 1.000 on all 56 matrices, sh0ck0r's at 0.85 or better on 64 of 73 (median 0.998, the nine others where
the first pass had read the parent's noise), Felldude's unrelated (median 0.009), as they must be when the first
pass measured the instruct training. Dzluck's copy carries huihui-ai's E2B direction at 1.000 on all 50 shared
matrices: the maker's second version is the first version's direction at two and a half times the weight from
five layers earlier. coder3101's QAT edit stands on the maker's instruct edit at 0.91 and on JokeHer's, NullpoLab's
and alphakek's at 0.92 to 0.95, the E4B arbitrary-rank family of finding 72; igorls's LoRA-rank edit stands at
0.65 or less to all twenty. Kooten's direction stands at 0.55 and 0.58 to huihui-ai's two 31B versions and 0.82 to
Sabomako's on eight matrices; enkato64bit's at 0.57 to MoonRide's, BinxNet's and 3MPER0RR's.

## The token side

The cluster's cards read "unexplained differences" on five of the eight, "consistent with re-save noted" on two
and "consistent" on one. The home judgement under transformers 5.22.1 with the originals' later commits moved
seven fields on four cards: `text_config.moe_intermediate_size` on pairs 2 and 4 (absent on one side, the same
default under 5.22.1; pair 4's card turns to consistent with re-save noted), `rope_parameters` on pair 3 (the
`rope_theta` field in its new form, loading as the same value), and four configuration fields pair 6 leaves out
that load as the same values (`audio_config.audio_samples_per_token`, `audio_config.hidden_size`,
`audio_config.output_proj_dims`, `vision_config.model_patch_size`). What stays open: pair 2's `per_layer_config`
(the 5.16 save form, finding 39); pair 3's 1,000 dropped control-token declarations, its dropped additional special
token and a `tokenizer.json` 155 bytes longer than Hearthfire's, which keeps finding 44's rule from reading the
drop against a shared file; pair 5's template and tokenizer configuration, which are Google's files at the E2B's
04-02 release revision (byte-equal by sha256) and so the earlier-revision case round 31 left owed, now with a
cause: the pin follows the re-uploader's creation date where the edit was made two months earlier; and pair 6's
generation file (48 banned sequences and a 12-gram repeat block) and 28,982-byte template. Pair 1 is consistent
where round 29 read the instruct model's files against the base; pairs 7 and 8 differ in version strings alone.

## What the scorer learned

The flag counts are the same on the cluster and at home. Their causes, by pair:

- Training under the per-layer entry, 304 and 361 flags (pairs 1 and 6): every trained linear is an unexpected
  change and every first share under 0.99 a flag. Pair 6 is two methods at once, a projection at 0.50 on 48
  matrices and an adapter on 320; a composed entry (finding 49) would read both and flag neither.
- Random matrices through the mapping, 189 of pair 4's 211 flags: the infix mapping paired the tower and the
  entry counted it as unexpected change. A rule that reads a kept fraction of 0, a first share near one over
  the matrix size and a relative difference equal to the square root of one plus a squared scale ratio would
  name the fresh draw (finding 63).
- Arbitrary-rank edits under the per-layer entry, 16 and 64 flags (pairs 7 and 8): several directions per
  matrix, and on pair 8 a direction per matrix as well.
- Kernel shoulders, 45 and 22 flags (pairs 2 and 4): first shares of 0.92 to 0.99 at the low-weight ends of the
  windows.
- Clean reads, 0 and 2 flags (pairs 5 and 3): a shared projection and a per-layer Heretic edit, the latter's two
  flags at 0.95 where the within-layer rule asks 0.96.

The round's result for the measure is the three re-measurements: the kernels and directions it read through a
round trip and through a fine-tune were the right ones, so a pairing by the wrong field costs flags and a
cleaner report but not the reading, and the second measurement of a pair on a different system with a different
original reproduces the first pass's numbers where both measured the same thing.

## Owed to the metadata tool

Added since: nothing this round. What remains: the earlier-revision template through a snapshot older than the
pin, now with pair 5 as a case where the snapshot is the parent's creation date rather than the re-upload's
(round 31's pairs 2 and 4 stay); the declared-context line (round 31's pair 1); the float16 `dtype` reading
(round 31's pair 2); the 5.16 save form as a named re-save (finding 39, pair 2 again); a dropped-declarations rule
that reads the decoder of each side's `tokenizer.json` when the files differ by a few bytes (pair 3). To the
pinner: a hub duplicate's weight files are compared against the hub's listing of its named source whether or not
the source is measured (pair 6, where the batch note's "different weight files" was against the measured E4B
export); a README whose first heading names another repository is a re-upload candidate whatever the commit title
says (pair 5); and a `card_parent` recorded from a README's first sentence is how pairs 2 and 3 were pinned
(`docs/weights-method.md`).

## Operational

The round ran on Wheat under the image-free kit with the standalone Python: one download, eight compares and the
sweep, every compare finishing with its card and its weights report, the sweep deleting the seven originals. The
pull carries the eight measurement folders (card, metadata, weights, direction vectors and the sha256 record of
each) and the sweep record; no job log was pulled, so the compares' nodes and seconds are not recorded. The home
judgement ran under transformers 5.22.1. Three readings were made at home from the hub by byte range
(`tools/hub_range_read.py`): Kooten's vision-tower query of layer 0, down projection of layer 13 and up projection
of layer 26 against google/gemma-4-31B-it at `419b2efe` and `842da379`. The hub's file listings were read for
huihui-ai/Huihui-gemma-4-E2B-it-abliterated-v2 and Jiunsong/SuperGemma-4-12b-abliterated, and five small files of
each were compared by sha256 with the re-uploads'; Dzluck's template and tokenizer configuration were compared the
same way with google/gemma-4-E2B-it at `4742fe84`. Forty-four readings were made from the saved direction files,
listed in the reading notes.

Weight differences alone cannot certify the absence of hidden behavior.
