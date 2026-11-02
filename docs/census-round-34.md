# Census round 34: eight Gemma 4 pairs on Nautilus, seven of them on QAT checkpoints (2026-11-02)

Eight published copies compared with their stated originals on Nautilus from the batch pinned as
`data/batches/round-34-batch-1.json` (pinned 2026-11-01 11:48Z): download job 4163806, compares 4163807 to
4163814, sweep 4163815, which deleted the six original checkpoints (`20e0b4c7` of the 26B-A4B QAT-unquantized
original at `641f1844` shared by pairs 1 and 3, `dc54e169` of the 12B QAT-unquantized original at `b8dea52d` for
pair 2, `a0104340` of the E4B QAT-unquantized original for pair 4, `f601ea62` of the 26B-A4B QAT-unquantized
original at `f1e06dc5` for pair 5, `d5f88f28` of the 12B QAT-unquantized original at `58540658` shared by pairs 6
and 7, and `b8ed5f05` of the DiffusionGemma original for pair 8) from
`/p/work1/sdegan/model-audit/rounds/34/originals/`. The pull of 11-01 21:23Z brought home the eight measurement
folders and the sweep record and no job log, so the compares' nodes and seconds are not in this note. The batch
is the census's first on the QAT-unquantized checkpoints as a set: six copies on two of the three sizes measured
before (the 26B-A4B and the 12B) and one on the E4B's, which enters the census as its thirtieth original, beside a third
copy of the DiffusionGemma base. Two of the eight were pinned with a question: eadx's repository is a hub
duplicate of a huihui-ai copy that was never measured, and smashingtags's is named after the instruct model and
pinned against the QAT checkpoint its card and field name. The eight measurements were re-scored at home with the
recipe table as committed and the saved direction vectors, and no flag count moved. Every metadata report was
judged again at home under transformers 5.22.1 with the originals' later commits, and no field moved on any of
the eight; the committed reports carry that judgement. Each pair has a card (the tool's Stage 1 text after the
home judgement, with the Stage 2 line) and a reading note in `docs/cards/`; the measurements are in
`results/weights/` and `results/meta/`, and the direction vectors stay in the pull copy
(`/opt/ai/hpc-packages/pulls/model-audit/nautilus34/measurements/pair-N/`).

| Pair | Copy | Original | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | llmfan46/gemma-4-26B-A4B-it-qat-q4_0-unquantized-uncensored-heretic | google/gemma-4-26B-A4B-it-qat-q4_0-unquantized | violations, 12 flags (first shares 0.379 to 0.939) | Heretic v1.2.0's arbitrary-rank branch on one component: the attention outputs of layers 11 to 22, the card's start 11 and end 23, input side on 12 of 12 at weights 1.10 to 1.70, several directions per matrix, no expert touched; the directions stand at 0.85 to 0.98 to the maker's instruct edit of this base; the template is a 23,077-byte file matching no Google revision |
| 2 | wnfldchen/gemma-4-12B-it-qat-q4_0-unquantized-heretic | google/gemma-4-12B-it-qat-q4_0-unquantized | violations, 49 flags (46 within-layer cosines, 3 first shares) | a Heretic v1.4.0 fork's LoRA-rank search with a `reproduce/` folder: both writers of layers 19 to 41, the card's window, rank one with a direction per matrix, input side on 44 of 46 at weights 0.95 to 1.90, four attention outputs outside the band (4.14 and 5.63 at layers 35 and 41, the leading input component amplified at 36 and 39), rows to 0.0106 under a preservation setting; the directions stand at 0.92 to coder3101's edit of the same checkpoint |
| 3 | eadx/Huihui-gemma-4-26B-A4B-it-qat-q4_0-unquantized-abliterated | google/gemma-4-26B-A4B-it-qat-q4_0-unquantized | match, 0 flags | the hub's duplicate of huihui-ai's QAT edit, whose parent repository is gone: a shared projection at a weight of 3.50 on both writers of all 30 layers, output side on 60 of 60, two directions (layers 0 to 11 and 14 to 29), the same two the maker's instruct edit of this base uses at 3.0; the largest shared weight in the census; metadata consistent with nothing differing |
| 4 | prithivMLmods/gemma-4-E4B-it-qat-heretic_decensored | google/gemma-4-E4B-it-qat-q4_0-unquantized | violations, 3 flags (2 direction cosines, one cross-kind) | Heretic's linear kernels on the first copy of the E4B QAT checkpoint: down projections 12 to 41 and attention outputs 18 to 41, both windows exactly, one shared direction, output side on 51 of 54, the down kernel's slope read 0.05 to 0.35 under its height, the attention heights scattered (0.29 at layer 37 under 1.31); the fourth shard equals the instruct exports' and the vision tower is the instruct model's file by byte range |
| 5 | xdavxd/gemma-4-26B-A4B-it-qat-heretic-ega | google/gemma-4-26B-A4B-it-qat-q4_0-unquantized | violations, 30 flags (29 worst-expert first shares, one within-layer cosine) | TrevorJS's norm-preserving biprojection with an expert-granular pass: attention outputs, shared down projections and all 128 experts of all 30 layers, 90 tensors and 3,840 expert slices as the card says, one direction per layer across the three kinds, output side on 90 of 90, kept medians 0.01 to 0.18 on 28 layers, rows within 0.0004 on the dense matrices and 0.0009 per expert tensor; the directions stand at 0.97 to TrevorJS's instruct edit; the 5.16 save form on the configuration |
| 6 | smashingtags/gemma-4-12b-it-abliterated | google/gemma-4-12B-it-qat-q4_0-unquantized | match, 0 flags | a plain projection at exactly 1.00 of one direction per layer out of both writers of layers 14 to 47 (34 of 48, the card's "top 70%"), output side on 68 of 68, on the QAT checkpoint under an instruct-model name (layer 0 byte-equal to the QAT file by range read); the directions stand at 0.95 to igorls's kernel search of the same checkpoint |
| 7 | coder3101/gemma-4-12B-it-qat-q4_0-unquantized-heretic | google/gemma-4-12B-it-qat-q4_0-unquantized | violations, 24 flags (first shares 0.53 to 0.97) | Heretic v1.2.0's arbitrary-rank branch: the attention outputs of layers 24 to 47, the card's window, the down projections in it exactly 0, input side on 24 of 24 at weights 0.76 to 2.54, rows 0.0070 to 0.0079 on all 24 under the maker's preservation claim; the directions stand at 0.88 to the maker's instruct edit and 0.92 to wnfldchen's |
| 8 | Umranz/diffusiongemma-26B-A4B-it-abliteration | google/diffusiongemma-26B-A4B-it | violations, 76 flags (38 first shares, 38 within-layer cosines) | Heretic's arbitrary-rank branch capped at layer 20 by the maker: both writers of layers 1 to 19, 15 of the 38 residues (0.0012 to 0.0045, kept 1.00 both sides), 23 edits at weights 0.87 to 1.42, each matrix its own direction, no expert touched, rows 0.0043 to 0.0079 on 37 of 38 under no claim; the directions stand at 0.86 to 0.99 to Goodoldjam's on twelve matrices; `return_dict_in_generate` added to the generation file |

Nothing moved outside the matrices the maker's method reaches in any of the eight pairs: the largest relative
change outside the changed set is exactly 0 on all eight. Seven of the eight stand on a QAT-unquantized
checkpoint, which the exact 0 establishes against an original that differs from the instruct model by 0.14 to
0.16 of a matrix (finding 48), and every one of the eight names its true original in its `base_model` field,
where round 33's Heretic exports named the pretrained base in six of eight (finding 67). Two pairs were read for
their parent by byte range (`tools/hub_range_read.py`): smashingtags's layer 0 attention output is byte-equal to
the QAT checkpoint's, and the E4B QAT checkpoint's vision tower is byte-equal to the instruct model's. The round's
result is eight edits read, every one as its card says, from five methods: three arbitrary-rank Heretic exports
(pairs 1, 7 and 8), a LoRA-rank fork of the same branch (pair 2), one linear-kernel Heretic export (pair 4), one
shared projection (pair 3), one plain per-layer projection (pair 6) and one norm-preserving biprojection with an
expert pass (pair 5). No pair carries a parent or a change its card does not name.

The weights read off the weights. Pair 3 keeps -2.50 along the leading output direction on all 60 matrices, a
weight of 3.50; pair 6 keeps 0.00 on all 68, a weight of 1.00. Pair 5 keeps 0.02 to 0.46 on the dense matrices
and a median 0.01 to 0.18 per expert tensor on 28 of 30 layers, finding 24's second term. Pair 4's down kernel
reads its slope (0.81 at layer 12 rising to 1.11 at 31 and 32, against 0.90 to 1.18) and sits under it by 0.05 to
0.35; its attention heights read 1.09 to 1.19 on layers 24 to 27 and 0.29 to 0.67 on 18, 32, 37 and 39, the
scatter of finding 46 on an E4B checkpoint for the first time. Pairs 1, 2 and 7 read input-side weights, 1.10 to
1.70, 0.95 to 1.90 (with 4.14 and 5.63 on two attention outputs and two amplified) and 0.76 to 2.54. Pair 8 reads
weights 0.87 to 1.42 on its 23 edits and residues on 15.

Preservation claims. Pair 5 claims row-norm preservation and the rows stay within 0.0004 on the dense matrices
and 0.0009 per packed expert tensor, the second claim in the census to hold after Bahushruth's (finding 57).
Pair 7 claims it and reads 0.0070 to 0.0079, the band of finding 22. Pair 2's configuration sets a rank-3
row-normalisation correction and the rows read 0.0010 to 0.0106 on 44 matrices, 0.145 and 0.289 on the two
outliers. Pair 8 claims nothing and reads the 0.007 band on 37 of 38 (finding 68's pattern). Pairs 1, 4 and 6
claim nothing and read Heretic's band or wider; pair 3's rows move 0.12 to 0.97 under a weight of 3.5.

Fingerprints. None of the eight copies equals a measured file. Pair 1's second shard (`c2c6ab9a`) equals mewse's
second shard and pair 2's first (`513abfa9`) equals igorls's first: the untouched end of the library's layout
(finding 71). Pair 4's fourth shard (`8080cb1a`) is the vision tower the seven instruct-model E4B exports carry,
and it is the QAT checkpoint's too, so the E4B QAT release shares its vision tower with the instruct model byte
for byte. Pair 8's shards 8 to 11 equal the original's and Goodoldjam's. Pair 3 is a hub duplicate (one commit,
two authors) of a parent the hub no longer serves, so it is the only measurement of that edit, the second such
case after finding 64. Google's QAT revisions share one weight file per size: the 26B-A4B at `641f1844` and
`f1e06dc5` and the 12B at `b8dea52d` and `58540658` carry the same shards, so pairs 1, 3 and 5 stand on one file
and pairs 2, 6 and 7 on another.

Directions. The round placed its edits against the saved vectors of fourteen earlier copies without a download
(finding 66's check). Four makers' QAT edits stand on their own instruct edits' directions: llmfan46 at a median
0.935, coder3101 at 0.88, huihui-ai (through eadx) at 0.99 and TrevorJS's method (through xdavxd) at 0.97. On the
12B QAT checkpoint, five edits by five makers sort into pairs by method: wnfldchen's and coder3101's arbitrary-rank
searches at 0.92, smashingtags's plain projection and igorls's kernel search at 0.95, and huihui-ai's shared
projection at 0.05 to 0.38 from all four (finding 72). On the diffusion base, Umranz's and Goodoldjam's searches
agree at 0.86 to 0.99 on twelve of the twenty matrices both reach and at 0.13 or less on the other eight.

## The token side

The cluster's cards read "unexplained differences" on three of the eight, "consistent with re-save noted" on three
and "consistent" on two, and the home judgement under transformers 5.22.1 moved no field on any of them. The
three that stay open: pair 1's template (a 23,077-byte file that matches no Google revision, rendering
identically) and tokenizer file (154 bytes longer, no field differing), pair 5's 5.16 save form (finding 39, the
same three fields that stand on mewse's and OS-Software's cards), and pair 8's `return_dict_in_generate` added to
the generation file. Every other copy carries its pin's template, and every fixed conversation renders identically
on all eight.

## What the scorer learned

The flag counts are the same on the cluster and at home. Their causes, by pair:

- Arbitrary-rank edits under the per-layer entry, 12, 24 and 76 flags (pairs 1, 7 and 8): first shares of
  0.02 to 0.97 where the method carries several directions per matrix, and on pair 8 the within-layer cosine
  as well. An arbitrary-rank entry (finding 22) would count the projections and the residues.
- A per-matrix direction, 49 flags (pair 2): the LoRA-rank search finds a direction per matrix and the per-layer
  entry expects the two writers to share one.
- The worst expert, 30 flags (pair 5): the rule reads the minimum first share over 128 experts (0.946 to 0.990)
  where every median is 0.990 or above; a rule on the median would clear 29 of the 30.
- Kernel shoulders, 3 flags (pair 4): two direction cosines of 0.94 at the top of the window and the cross-kind
  line.
- Clean matches, 0 flags (pairs 3 and 6): the two plain projections of the round, at weights 3.50 and 1.00 that
  the match does not report.

The round's result for the measure is the direction placement at scale: fourteen comparisons from the saved
vectors, which sorted five edits of one checkpoint by method and placed four makers' QAT edits on their instruct
edits' directions.

## Owed to the metadata tool

Added since: nothing this round. What remains: the earlier-revision template through a snapshot older than the
pin (round 31's pairs 2 and 4); the declared-context line (round 31's pair 1); the float16 `dtype` reading (round
31's pair 2); the 5.16 save form as a named re-save rather than an open difference (finding 39, now on three
copies of one checkpoint). To the pinner: a repository named after the instruct model whose `base_model` field
names the QAT checkpoint is paired by the field and checked by range read below the window (pair 6); a hub
duplicate whose parent returns 404 is the parent's only measurement and is read as such (pair 3); and a `reproduce/`
folder is read for its configuration before the weights (pair 2).

## Operational

The pull of 11-01 21:23Z carries the eight measurement folders (card, metadata, weights, direction vectors and the
sha256 record of each) and the sweep record; no job log was pulled, so the compares' nodes and seconds are not
recorded. Every compare finished with its card and its weights report, and the sweep ran after all eight and
deleted the six originals. The home judgement ran under transformers 5.22.1. Four readings were made at home from
the hub by byte range (`tools/hub_range_read.py`): smashingtags's layer 0 attention output and layer 20 down
projection against the QAT and instruct 12B originals, and the E4B QAT checkpoint's vision tensor
`model.vision_tower.encoder.layers.0.mlp.down_proj.linear.weight` and layer 20 attention output against
google/gemma-4-E4B-it. Fourteen readings were made from the saved direction files, listed in the reading notes.

Weight differences alone cannot certify the absence of hidden behavior.
