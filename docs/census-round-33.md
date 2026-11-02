# Census round 33: eight Gemma 4 pairs on Wheat (2026-11-02)

Eight published copies compared with their stated originals on Wheat from the batch pinned as
`data/batches/round-33-batch-1.json` (pinned 2026-11-01 01:16Z): download job 387105, compares 387106 to 387113,
sweep 387114, which deleted the six original checkpoints (`842da379` of the 31B instruct original for pair 1,
`fee6332c` of the E4B instruct original shared by pairs 2, 4 and 5, `d6436b3d` of the same original for pair 3,
`5926caa4` of the 12B instruct original for pair 6, `3e22461f` of the E2B instruct original for pair 7 and
`58540658` of the 12B QAT-unquantized original for pair 8) from `/p/work/sdegan/model-audit/rounds/33/originals/`.
The pull of 11-02 01:02Z brought home the eight measurement folders and the sweep record and no job log, so the
compares' nodes and seconds are not in this note. The round is the second on the image-free Wheat kit with the
standalone CPython 3.11 after round 31's third batch, and the first batch on that kit to run through at the first
attempt. The batch is the copies round 32 left for room, with one substitution: igorls's second 12B Heretic copy
took the place of ScottzillaSystems/supergemma4-e4b-abliterated, whose weight files equal Jiunsong's copy
measured in round 8 (finding 14), refused by the checksum rule of finding 38 before any download. The eight
measurements were re-scored at home with the recipe table as committed and the saved direction vectors, and no
flag count moved. Every metadata report was judged again at home under transformers 5.22.1 with the originals'
later commits, and the committed reports carry that judgement. Each pair has a card (the tool's Stage 1 text after
the home judgement, with the Stage 2 line) and a reading note in `docs/cards/`; the measurements are in
`results/weights/` and `results/meta/`, and the direction vectors stay in the pull copy
(`/opt/ai/hpc-packages/pulls/model-audit/wheat33/measurements/pair-N/`).

| Pair | Copy | Original | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | callmegrr/gemma-4-31B-it-heretic-z | google/gemma-4-31B-it | violations, 8 flags (first shares 0.914 to 0.989) | Heretic v1.4.0 with per-layer directions: the attention outputs of layers 37 to 46 and the down projections of 40 and 41, exactly the card's two windows, output side on 12 of 12, the kernels read back within 0.21 on every layer and within 0.05 on seven (0.19, 0.62, 1.10, 1.16, 0.61, 0.31 on layers 37, 39, 41, 42, 44, 46 against 0.26, 0.69, 1.12, 1.18, 0.75, 0.32); the narrowest 31B Heretic edit measured; the field names the pretrained base |
| 2 | p-e-w/gemma-4-E4B-it-heretic | google/gemma-4-E4B-it | violations, 37 flags (32 first shares, 4 direction cosines, one cross-kind) | the tool author's own export (the maker's REPRODUCED re-upload shares the files): Heretic v1.3.0, attention outputs 11 to 41 and down projections 5 to 41, the card's windows exactly, one shared direction, output side on 57 of 68, the heights following the kernels' shape and sitting 0.1 to 0.3 below them on the shoulders (down projections 1.34 at layer 26 against 1.40, 0.47 at 5 against 0.59); the field names the pretrained base |
| 3 | sh0ck0r/gemma-4-E4B-it-heretic | google/gemma-4-E4B-it | violations, 11 flags (8 first shares, 2 direction cosines, one cross-kind) | Heretic v1.3.0: attention outputs 19 to 41 and down projections 5 to 41, the card's windows exactly, one shared direction, output side on 51 of 60; the flat down kernel (1.33 to 1.38 across the window) reads 1.11 to 1.30, a tenth or two under; the field names the pretrained base |
| 4 | JokeHer/gemma-4-E4B-it-heretic | google/gemma-4-E4B-it | violations, 80 flags (40 first shares, 40 within-layer cosines) | Heretic v1.2.0's arbitrary-rank branch, start 19 and end 39: both writers of layers 19 to 38, input side on 39 of 40 at right-side weights 1.3 to 4.8 on the attention outputs and 3.4 to 30.1 on the down projections, each matrix its own direction, layer 37's down projection changed by 1.008 of its norm with its rows put back within 0.0063 and layer 20's left as a residue; KL 0.58 on the card; the field names the pretrained base |
| 5 | BinxNet/gemma-4-E4B-it-heretic | google/gemma-4-E4B-it | violations, 14 flags (8 first shares, 5 direction cosines, one cross-kind) | Heretic v1.4.0: attention outputs 7 to 41 and down projections 26 to 41, the card's windows exactly, one shared direction, output side on 44 of 51, the down kernel read within 0.22 (0.93, 1.01, 1.12, 1.22, 1.15 on layers 26, 30, 35, 38, 41 against 1.00, 1.15, 1.33, 1.44, 1.35) and the attention kernel's peak within 0.15 with its shoulders 0.2 to 0.6 short; the field names the pretrained base |
| 6 | BinxNet/gemma-4-12B-it-heretic | google/gemma-4-12B-it | violations, 19 flags (first shares 0.839 to 0.989) | Heretic v1.4.0: attention outputs 4 to 47 and down projections 27 to 37, the card's windows exactly, one shared direction, and the heights scatter (0.07 at layer 12, 0.03 at 20, 1.44 at 29, 0.13 at 32 on the attention outputs under a kernel of 0.56, 0.98, 1.42, 1.26), the left below the right on 24 of 55: the fourth Heretic copy of the 12B to read finding 46's scatter where the same maker's E4B export four days later reads its heights; the field names the pretrained base |
| 7 | yuna1126/gemma-4-E2B-Tema_Q-Abliterated | google/gemma-4-E2B-it | violations, 3 flags (first shares 0.948 to 0.988) | a tool new to the census (Tema_Q-Abliterated v1.0.0, SCAPE search) printing a raised-cosine kernel: the attention outputs of layers 14 to 18 and the down projections of 12 and 13, one direction per layer, output side on 7 of 7, the weights 0.20, 0.98, 1.53, 1.31, 0.53 and 0.93, 1.10 against the kernel's 0.19, 0.96, 1.53, 1.31, 0.53 and 0.93, 1.03, rows restored within 0.0004, and the kernel's two tails under the threshold at 0.00038 and 0.000028; metadata consistent with no field differing |
| 8 | igorls/gemma-4-12B-it-qat-q4_0-unquantized-heretic | google/gemma-4-12B-it-qat-q4_0-unquantized | match, 0 flags | the maker's second 12B Heretic copy, searched with thinking on, on the QAT checkpoint its field names: attention outputs 16 to 47 and down projections 20 to 44, the card's windows exactly, one direction per layer, first shares 0.9946 to 0.9977, output side on 47 of 57, the down kernel (1.43 to 1.48) read within 0.14 on layers 32 to 44 and falling away below, the attention heights scattered under a kernel of 1.29 to 1.48; 57 matrices to the first copy's 22, KL 0.32 to 0.028, the directions 0.15 to 0.96 from the first copy's |

Nothing moved outside the matrices the maker's method reaches in seven of the eight pairs (the largest relative
change outside the changed set is exactly 0) and in pair 7 beyond the kernel's own tails (0.00038 on layer 19's
attention output, where the raised cosine stands at 0.010). The round's result is eight edits read, every one as
its card says: six Heretic exports of the linear-kernel kind whose windows read to the layer on both writers, one
of the arbitrary-rank kind in its declared window, and one from a tool the census had not met whose printed kernel
reads back to the second decimal. No pair carries a parent or a change its card does not name. The declared base
is wrong on six of the eight, in the same way: the `base_model` field of Heretic's generated card names the
pretrained base, google/gemma-4-31B, google/gemma-4-E4B or google/gemma-4-12B, where the card's first sentence and
the weights name the instruct model (finding 67); the pinner paired all six by the sentence.

The weights read off the weights. Pair 1's kernels read back within 0.21 on all twelve matrices. Pairs 2, 3 and 5
read their windows exactly, their peaks within 0.07, 0.34 and 0.15, and their shoulders low by 0.1 to 0.6; pair 3's
flat down kernel reads flat, 0.1 to 0.2 under its height. Pair 6 reads its windows and no height on the attention
outputs: 0.07 at layer 12 and 0.03 at layer 47 where the kernel runs 0.56 and 0.47, 1.44 at layer 29 where it
runs 1.42, finding 46's scatter, on a copy whose relative changes follow the kernel. Pair 8 reads its windows, its
down kernel on the upper thirteen layers within 0.14, and the same scatter on the attention outputs; the two 12B
copies of this round, from different makers on different Google checkpoints, read alike. Pair 4 keeps -0.33 to
-3.81 along the leading input direction on the attention outputs and -2.44 to -29.09 on the down projections, with
layer 37's down projection kept at -29.09 on a change equal to the matrix (cosine 0.49 with the original by range
read). Pair 7 keeps 0.80, 0.02, -0.53, -0.31 and 0.47 on the attention outputs of 14 to 18, the raised cosine's one
minus 0.19, 0.96, 1.53, 1.31 and 0.53.

Preservation claims. No card of the round claims a row restoration. Pair 7 restores anyway, rows within 0.0004
on all seven matrices. Pairs 1, 2, 3, 5, 6 and 8 leave Heretic's band, 0.0010 to 0.0157. Pair 4's rows moved 0.0057
to 0.0078 on 39 matrices and 0.0008 on the residue, the band finding 22 reads under coder3101's preservation claim,
here with no claim.

Fingerprints. None of the eight copies equals a measured file. Three of the E4B exports (pairs 2, 3 and 5) share two of
their four shards with each other and with four earlier copies: the first (`aa3e9d1e`, the token embedding alone
in the library's four-shard layout) and the fourth (`8080cb1a`, the vision tower), because no Heretic edit touches
either; their second and third shards are each copy's own. Pair 1's second shard (`2bdb2df0`, layers 48 to 59 and
the vision tower) is the one Sabomako's and llmfan46's 31B exports carry for the same reason. A duplicate rule that
compares every shard tells the layout from a re-upload; one that matched any shard would have called seven
distinct E4B edits one file and three 31B edits another (finding 71). Pair 8 against the maker's first copy and against huihui-ai's edit of the same
QAT checkpoint: the saved leading vectors stand at 0.15 to 0.96 and 0.10 to 0.84, so the three searches on this
base found three directions.

## The token side

The cluster's cards read "unexplained differences" on seven of the eight, every one on configuration fields and
none on a weight, and "consistent" on pair 7. Re-judged at home under transformers 5.22.1, ten fields move and
seven cards change their reading to "consistent with re-save noted": `text_config.moe_intermediate_size` closes by
the default rule on pairs 1 to 5 (finding 11), and on pair 6 the three audio fields and the vision patch size close
the same way; pair 8 was "consistent with re-save noted" on both. Nothing stays open: the version strings and, on
pair 6, three repeated `dtype` fields are all that differ on any card. Every copy carries its pin's template (pair 4
a 17,695-byte file the tool reads as the same template) and every fixed conversation renders identically.

## What the scorer learned

The flag counts are the same on the cluster and at home. Their causes, by pair:

- Kernel shoulders, 8, 37, 11, 14 and 19 flags (pairs 1, 2, 3, 5 and 6): first shares of 0.84 to 0.99 where a
  linear kernel runs below 0.5 and the edit is 0.002 to 0.01 of the matrix. The rule's line is 0.99; the shoulders
  of a declared kernel sit at 0.91 to 0.99 on every copy of the round, and a line at 0.95 would clear most and a
  rule that reads the kernel would clear all.
- Per-matrix directions, 80 flags (pair 4): the per-layer entry expects the two writers of a layer to share a
  direction and flags every matrix when they do not; an arbitrary-rank entry (finding 22) would count the 39
  projections, the residue and layer 37's rewrite.
- A cosine kernel's edges, 3 flags (pair 7): first shares 0.948 to 0.988 on the three smallest edits.
- A clean match, 0 flags (pair 8): the first Heretic copy of the 12B to match the per-layer entry, and the match
  says nothing of the heights, which read on thirteen matrices and scatter on thirty-two.

The round's result for the measure is a second direction-file placement: pair 8's directions against the maker's
first copy and against huihui-ai's QAT edit, read from the saved vectors with no download (finding 66's check),
and pair 6's against pair 8's on the same architecture across two Google checkpoints.

## Owed to the metadata tool

Added since: nothing this round. What remains: the earlier-revision template through a snapshot older than the
pin (round 31's pairs 2 and 4); the declared-context line (round 31's pair 1); the float16 `dtype` reading
(round 31's pair 2). To the pinner: a `base_model` field that names a pretrained Gemma 4 base under a Heretic
card is the tool's inherited header and the first sentence names the parent (finding 67), the check finding 48
asked for on QAT names extended to the pretrained names; a repository whose weight files share a checksum with a
measured copy on some shards and differ on others is a distinct edit in the library's layout (finding 71); and
a card that prints a `kernel_shape` row is a tool other than Heretic whose kernel the reading can test.

## Operational

The pull of 11-02 01:02Z carries the eight measurement folders (card, metadata, weights, direction vectors and
the sha256 record of each) and the sweep record; no job log was pulled, so the compares' nodes and seconds are not
recorded. Every compare finished with its card and its weights report, and the sweep ran after all eight and
deleted the six originals. The home judgement ran under transformers 5.22.1. One reading was made at home from
the hub by byte range (`tools/hub_range_read.py`): layer 37's down projection of pair 4 against
google/gemma-4-E4B-it. Three readings were made from the saved direction files: pair 8 against
igorls/gemma-4-12B-it-heretic-v1, pair 8 against huihui-ai's QAT edit, and pair 6 against pair 8.

Weight differences alone cannot certify the absence of hidden behavior.
