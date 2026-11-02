# Census round 31: four Gemma 4 pairs on Wheat, the third batch of the round (2026-11-02)

Four published copies compared with their stated originals on Wheat from the batch pinned as
`data/batches/round-31-batch-3.json` (pinned 2026-11-01 11:18Z): download job 387097, compares 387098 to 387101,
sweep 387102, which deleted the four original checkpoints (`5926caa4` of the 12B instruct original for pair 1,
`83df0a88` of the E4B instruct original for pair 2, `35487898` and `842da379` of the 31B instruct original for
pairs 3 and 4) from `/p/work/sdegan/model-audit/rounds/31/originals/`. The pull of 11-02 00:22Z brought home the
four measurement folders and the sweep record; the job logs at home (`wheat31-logs`, pulled 11-01 01:16Z) are the
two withdrawn chains' and not these jobs', so the compares' nodes and seconds are not in this note. Round 31 is the
first round built for Wheat without the container image, carrying a standalone CPython 3.11 because Wheat's transfer
nodes refuse user namespaces, and it ran three times. Batch 1 (eight pairs, pinned 10-31 21:53Z, chain 386958 to
386967) was withdrawn thirty minutes into its download when the pinner found four of its copies to be re-uploads of
measured files (geekcy2333's of WWTCyberLab's 26B-A4B edit, cyrilgiordano83's of TrevorJS's E2B edit, deewu0809's of
huihui-ai's E4B edit, Fuzzynetwork1989-alt's of prithivMLmods's E2B-MAX). Batch 2 (the remaining four, pinned 11-01
00:06Z, download 386971) stopped on its pair 3 at 00:39Z, because the kit then keyed input folders by pair number
and found the withdrawn chain's third copy in that folder. Batch 3 is the same four pairs on the kit that keys the
folders by the copy's identity. The four measurements were re-scored at home with the recipe table as committed and
the saved direction vectors, and no flag count moved. Every metadata report was judged again at home under
transformers 5.22.1 with the originals' later commits, and the committed reports carry that judgement. Each pair has
a card (the tool's Stage 1 text after the home judgement, with the Stage 2 line) and a reading note in `docs/cards/`;
the measurements are in `results/weights/` and `results/meta/`, and the direction vectors stay in the pull copy
(`/opt/ai/hpc-packages/pulls/model-audit/wheat31/measurements/pair-N/`).

| Pair | Copy | Original | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | AlekseyCalvin/Lyrical_Translator_ru2en_on_Gemma4_12b_heretic_SFT_Run2 | google/gemma-4-12B-it | violations, 425 flags (232 unexpected changes, 96 first shares, 96 direction cosines, one cross-kind) | a translation fine-tune of all seven projections of all 48 layers (the value projections of the eight global layers excepted) at 1.8 to 10 percent, over a Heretic edit the title names only by method: the down projections of layers 23, 27, 28, 29, 32 and 33 and the attention outputs of 29 and 34 keep igorls/gemma-4-12B-it-heretic-v1's fractions within 0.02 along directions equal to that copy's at 0.97 to 1.000; the configuration's context length halved to 131,072 |
| 2 | Ilya626/gemma-4-E4B-it-SDFT_Heretic_RP | google/gemma-4-E4B-it | violations, 611 flags (442 unexpected changes, 84 first shares, 84 direction cosines, one cross-kind) | a full fine-tune of the language stack at 0.16 to 0.56 percent with no kernel under it, and the 232 linear maps of the audio and vision towers replaced by Gaussian draws at the library's default scale (standard deviation 0.0200, kurtosis 3.00, no zeros), the normalisations and quantisation ranges around them Google's; saved in float16 with the E4B template of the 04-02 revision |
| 3 | Sabomako/gemma-4-31B-it-heretic | google/gemma-4-31B-it | violations, 5 flags (first shares 0.73 to 0.99) | the card's "custom ORBA" with no parameters printed: one direction per layer on both writers of layers 31 to 34 only, output side, weights 0.06 to 5.36, rows restored within 0.0004; the first 31B copy on Wheat |
| 4 | nguyenthilaitrieulong/gemma-4-31B-it-abliterated | google/gemma-4-31B-it | violations, 65 flags (47 first shares, 12 within-layer cosines, 6 unexpected changes) | "Duplicate from WWTCyberLab/gemma-4-31B-it-abliterated", an unmeasured parent, so the measurement of that edit: the card's five surfaces, four read to the number (an 18-module adapter on layers 57 to 59, a 1.5 pass on both writers of 55 to 59 at kept -0.500, 13 embedding rows at one eleventh, five `bad_words_ids`) and the "standard" ablation on layers 25 to 27 and 31 to 54 at weights 0.75 to 1.00 where the card says 33 to 52 |

Nothing moved outside the matrices the maker's method reaches in pairs 1, 3 and 4 (the largest relative change
outside the changed set is exactly 0) and in pair 2 beyond the float16 save's rounding (0.0000011 on the per-layer
input gates). The round's result is three edits read and one re-upload of an unmeasured edit, read as that edit. Two
of the three edits read as their cards say (pair 3 in its component pair, pair 1 in the method its title names and
in the adapter's reach), one (pair 4, the parent's card) in four of five surfaces with the fifth's window misstated,
and pair 2 reads a change its card does not mention: both towers' linear maps are fresh random matrices, and no
projection is in the language stack that the word Heretic would predict.

The weights read off the weights. Pair 3 keeps -0.36, -2.17, 0.58 and -4.36 along the leading output direction of
the attention outputs of layers 31 to 34 and -4.32, -0.32, 0.94 and 0.15 on the down projections, the two writers of
each layer within 0.02 in direction, the left below the right on 8 of 8. Pair 4 keeps 0.25 on layer 25 falling to
0.00 on 39 and rising to 0.24 on 54 on both writers, then -0.494 to -0.5001 on all ten writers of 55 to 59 (the
card's scale 1.5), with a second direction under those ten (first shares 0.69 to 0.79). Pair 1's leading directions
are the training's on the queries, keys, values, gates and up projections (kept 0.8 to 1.1 on both sides) and the
Heretic edit's on eight matrices in igorls's window, where the kept fractions equal igorls's own within 0.02 (down
projection of layer 28: -0.373 against -0.374). Pair 2 keeps 0.99 to 1.02 on every language matrix and -0.11 to
0.00 on the 232 tower matrices, which is what a matrix uncorrelated with the original reads.

Preservation claims. Pair 3 claims nothing and keeps its rows within 0.0004 on all eight matrices, the exact
restoration. Pair 4's parent claims nothing; its rows moved 0.002 to 0.09 under the projections, 0.004 to 0.51 under
the adapter and 0.909 on the embedding, the thirteen rows. Pair 1's rows moved 0.003 to 4.9, the training filling
key rows the original keeps near zero. Pair 2's rows moved 0.004 to 0.23 in the language stack and 0.42 to 3.9 in
the towers.

Fingerprints. Sixteen measurements now stand on the 31B instruct original's weight file. Pair 3's second shard
(`2bdb2df0`, layers 48 to 59 and the vision tower in the library's two-shard layout) equals the second shard of
callmegrr's (round 33) and llmfan46's exports, since none of the three touched a tensor in it; the first shards are
each copy's own and no measured field is shared. Pair 4's two shards are WWTCyberLab's under another name and equal
no measured file. Pair 1's five shards and pair 2's four are their own. Pair 4 against huihui-ai's second 31B
version, the other weight-1.5 edit on this base (finding 21): layer 56's attention output read from the hub by byte
range differs from huihui-ai's by 0.0306 of its norm, two directions at one weight.

## The token side

The cluster's cards read "unexplained differences" on all four, every one on configuration or template fields and
none on a weight. Re-judged at home under transformers 5.22.1, seven fields move and one card changes its reading
to "consistent with re-save noted": pair 3, where `text_config.moe_intermediate_size` closes by the default rule
and the version strings are all that remain. The field closes on pairs 2 and 4 too, and on pair 1 the three audio
fields and the vision patch size close by the default rule (finding 11). What stays as printed:

- Pair 1: `text_config.max_position_embeddings`, 262,144 in the original and 131,072 in the copy. The training's
  save halved the declared context length; the card says nothing of it. The template is the pin's and renders
  identically.
- Pair 2: four `dtype` fields reading float16 against bfloat16, the save's format and a true difference for a
  loader; and the template, Google's 11,926-byte E4B file of the 04-02 revision under the 04-10 pin (16,317
  bytes), the earlier-revision case lessans's and TrevorJS's copies read in rounds 22 and 29, closed by hand.
- Pair 4: `generation.bad_words_ids`, five token sequences the card's fifth surface describes, a disclosed change;
  and the template, Google's 12,045-byte 31B file of the 04-10 revision under the 07-20 pin (18,683 bytes), the
  case akpsahan's re-upload read in round 29.

Every fixed conversation renders identically under both templates.

## What the scorer learned

The flag counts are the same on the cluster and at home. Their causes, by pair:

- Training over an ablation, 425 flags (pair 1): 232 unexpected changes on the queries, keys, values, gates and up
  projections, 96 first shares of 0.13 to 0.86 on the two writers, 96 direction cosines and one cross-kind flag.
  As finding 18's pairs, the parent must be measured as a separate term; here the parent is identified (finding 66)
  and the pair can be re-pinned against it.
- Training with two towers replaced, 611 flags (pair 2): 442 unexpected changes (210 language projections the
  entries do not list as writers and 232 tower matrices), 84 first shares of 0.03 to 0.28 and 84 direction cosines
  on the two writers, one cross-kind flag. A rule for a module whose every matrix changed by more than its norm
  with no direction kept would name the towers.
- A restored projection at a high weight, 5 flags (pair 3): first shares of 0.959 to 0.993 on four matrices at
  weights 1.4 to 5.4, where the restoration leaves a second direction, and 0.734 on the smallest edit (layer 33's
  down projection, 0.0011 of its norm).
- Five methods in one file, 65 flags (pair 4): 47 first shares (the ten two-direction matrices of layers 55 to 59
  at 0.69 to 0.79, the adapter's modules, the embedding at 0.36 and the window's edges), 12 within-layer cosines on
  the adapter's layers and 6 unexpected changes (the queries, keys, gates and up projections of 57 to 59 count as
  six kinds beyond the entry's two writers).

The round's result for the measure is the direction file: pair 1's parent was placed by comparing its saved
leading vectors with an earlier measurement's, with no download and no range read (finding 66), a check the scorer
can run against every committed direction file on the same base.

## Owed to the metadata tool

Added since: nothing this round. What remains: the earlier-revision template through a snapshot older than the pin
(pairs 2 and 4, two more); a line for a declared context length that a copy halves (pair 1, finding 4's kind); and
a reading of a float16 save's `dtype` fields as the format of the file rather than a configuration edit (pair 2).
To the pinner: a one-commit repository titled "Duplicate from" names its parent before any download (finding 38),
and when the parent is unmeasured the pair is still worth its download, pinned under the parent's name; and a
copy whose title names a method ("heretic") and whose field names Google is a training-over-ablation pair whose
parent the direction files can find.

## Operational

The pull of 11-02 00:22Z carries the four measurement folders (card, metadata, weights, direction vectors and the
sha256 record of each) and the sweep record. The logs at home are the withdrawn chains' (batch 1's 386958, batch 2's
386971 with its stop at 00:39:52Z on 11-01, and the kit, verify, reporting and submit steps of both), so batch 3's
nodes and seconds are not recorded. Every compare finished with its card and its weights report, and the sweep ran
after all four and deleted the four originals. The home judgement ran under transformers 5.22.1. Four readings were
made at home from the hub by byte range (`tools/hub_range_read.py`): three tower matrices of pair 2 against
google/gemma-4-E4B-it, and layer 56's attention output of pair 4 against google/gemma-4-31B-it and huihui-ai's
second 31B version; one reading was made from the saved direction files, pair 1's eight matrices against the nine
other measured 12B copies' vectors.

Weight differences alone cannot certify the absence of hidden behavior.
