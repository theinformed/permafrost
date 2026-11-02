# Census round 37: eight pairs on Wheat, five of them on QAT-unquantized checkpoints and one a card that names one writer measured on both (2026-11-02)

Eight published copies compared with their originals on Wheat from the batch pinned as
`data/batches/round-37-batch-1.json` (pinned 2026-11-02 05:02Z) under the image-free kit with the standalone
Python: download job 387161, compares 387162 to 387169, sweep 387170, which deleted the eight originals
(`be573839` of google/gemma-4-12B-it-qat-q4_0-unquantized at `b6ed8627` for pair 1, `f601ea62` of the 26B-A4B QAT
checkpoint for pair 2, `8b30c5a4` of google/gemma-4-31B-it-qat-q4_0-unquantized at `1e4d8bee` for pair 3,
`773bb647`, `37a42740` and `ed9be084` of google/gemma-4-E4B-it at `3555bddc`, `83df0a88` and `292a7e27` for pairs
4, 6 and 8, `bec57494` of google/gemma-4-31B-it for pair 5 and `d5f88f28` of the 12B QAT checkpoint at `58540658`
for pair 7) from `/p/work/sdegan/model-audit/rounds/37/originals/`. The pull brought home the eight measurement
folders and the sweep record and no job log, so the compares' nodes and seconds are not in this note. All eight
are first measurements of distinct copies, none a re-upload, and the 31B QAT checkpoint enters the census as a new
original with pair 3, which brings the population to one hundred and fifty-nine measurements of one hundred and
fifty-two distinct copies on thirty-three originals: the round 35 header's numbers plus eight measurements, eight
copies and one original. Five of the eight stand on QAT checkpoints (two OS-Software exports made on Japanese
prompt sets, wnfldchen's merged 31B export, llmfan46's 12B export), two are MoonRide's first arbitrary-rank edits
of April, one is the per-layer pass TheUmbraWalker's second copy was built on, and one, NullpoLab's
Refusals8-attn, is a card that says `target_components = ["attn.o_proj"]` measured on both writers. The pinner
refused eadx's 12B QAT re-upload (huihui-ai's files, measured in round 32), six candidates measured in rounds 8,
12 and 30, and wnfldchen's unmerged 31B export, which carries its 120 adapter tensors under a `base_model` prefix.
The eight measurements were re-scored at home with the recipe table as committed and the saved direction vectors,
and no flag count moved. Every metadata report was judged again at home under transformers 5.22.1 with the
originals' later commits; the home judgement moved one field on each of pairs 4, 5 and 6 and two on pair 8 (all
four turn to consistent with re-save noted) and none on pairs 1, 2, 3 and 7. Each pair has a card (the tool's
Stage 1 text after the home judgement, with the Stage 2 line) and a reading note in `docs/cards/`; the
measurements are in `results/weights/` and `results/meta/`, and the direction vectors stay in the pull copy
(`/opt/ai/hpc-packages/pulls/model-audit/wheat37/measurements/pair-N/`).

| Pair | Copy | Original | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | OS-Software/gemma-4-12B-it-qat-q4_0-unquantized-heretic-ja-v2 | google/gemma-4-12B-it-qat-q4_0-unquantized | violations, 108 flags (54 first shares, 54 within-layer cosines) | Heretic 1.4.0's LoRA-adapter arbitrary-rank branch with row-norm preservation, searched on Japanese prompt sets as the card says: both writers of layers 13 to 39 (54 of 677), the card's start 13 and end 40, a few directions per matrix, input side on all 54 at weights 0.74 to 1.95, rows 0.0003 to 0.0057 at or under finding 22's band; exactly 0 outside; the leading directions stand at 0.40 and 0.30 to coder3101's 12B edit and at 0.14 or less to the kernel edits; the first shard is the library's layout shared with wnfldchen's and igorls's 12B QAT exports |
| 2 | OS-Software/gemma-4-26B-A4B-it-qat-q4_0-unquantized-heretic-ja | google/gemma-4-26B-A4B-it-qat-q4_0-unquantized | violations, 64 flags (32 first shares, 32 within-layer cosines) | the same branch on the 26B-A4B's attention outputs and shared down projections of layers 7 to 22 (32 of 1,013), the card's window, no expert touched, input side on all 32 at weights 1.24 to 2.09, rows 0.0012 to 0.0081 (in the band on five, under it on 26, over by 0.0001 on one); exactly 0 outside; the directions stand at 0.62 to 0.70 to the maker's English v2 export, coder3101's and llmfan46's 26B edits; five of the eleven shards equal the maker's English v2's |
| 3 | wnfldchen/gemma-4-31B-it-qat-q4_0-unquantized-heretic-merged | google/gemma-4-31B-it-qat-q4_0-unquantized (new original) | violations, 30 flags (first shares 0.63 to 0.98) | Heretic 1.4.0's arbitrary-rank edit at rank 256, merged from the maker's adapter repository as the card says: the attention outputs of layers 24 to 53 (30 of 1,188), the card's window and its one target, input side on 27 of 30 at weights 0.27 to 4.47, two matrices amplified rather than removed and the layer 50 matrix rewritten (relative change 0.416, rows 0.75); rows 0.014 to 0.75 on all 30 under the card's "row-norm preservation", every one above finding 22's band; exactly 0 outside; the left directions at 0.78 to 0.85 to the 31B arbitrary-rank family and the right at 0.37 to 0.40 |
| 4 | TheUmbraWalker/gemma-4-E4B-it-heretic | google/gemma-4-E4B-it | violations, 8 flags (within-layer cosines 0.91 to 0.95) | the per-layer Heretic 1.3.0 pass whose card the maker's second copy stacks under its own: both writers of layers 4 to 41 and 7 to 41 (73 of 2,076), the kernels' reach exactly, rank one, no readable weight; the leading directions equal the second copy's at 1.000 on 57 of 73 (the 16 others the second pass's attention window) and TrevorJS's E4B edit's at 0.98 and 0.99 on all 73; exactly 0 outside; the second shard byte-equal to the second copy's; the field names the pretrained base |
| 5 | MoonRide/gemma-4-31B-it-heretic-ara | google/gemma-4-31B-it | violations, 84 flags (44 first shares, 40 within-layer cosines) | Heretic 1.2.0's arbitrary-rank edit with row-norm preservation, four weeks before the maker's custom copy: all 24 attention outputs and 20 down projections of layers 30 to 53 above the line (44 of 1,188), 36 of them edits (input side, weights 1.35 to 4.39, rows 0.0059 to 0.0077, finding 22's band on every one) and 8 residues without a direction, four more down projections under the line at 0.0008 to 0.00098; the directions at 0.97 and 0.99 to llmfan46's 31B edit and 0.95 and 0.98 to coder3101's |
| 6 | MoonRide/gemma-4-E4B-it-heretic-ara | google/gemma-4-E4B-it | violations, 65 flags (33 first shares, 32 within-layer cosines) | the same edit on the E4B the day before: both writers of layers 21 to 37 above the line (33 of 2,076), 26 edits (input side, weights 0.08 to 2.30, rows in the band on 25) and 7 residues, one down projection under the line at 0.00091; the 54 shared-key-value tensors absent from the save; the directions at 0.99 on both sides to NullpoLab's Refusals5 and coder3101's E4B edit |
| 7 | llmfan46/gemma-4-12B-it-qat-q4_0-unquantized-uncensored-heretic | google/gemma-4-12B-it-qat-q4_0-unquantized | violations, 11 flags (first shares 0.85 to 0.97) | Heretic 1.2.0's arbitrary-rank edit on the attention outputs of layers 24 to 34 (11 of 677), the card's window and its one target, input side on all 11 at weights 1.23 to 2.64, rows 0.003 to 0.037 under no claim; exactly 0 outside; the directions at 0.97 and 0.94 to coder3101's 12B QAT edit and 0.95 to the maker's own instruct edit; the maker's macro template in `tokenizer_config.json` again |
| 8 | NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals8-attn | google/gemma-4-E4B-it | violations, 45 flags (25 first shares, 20 within-layer cosines) | the arbitrary-rank branch at commit `3b70fe5` on both writers under a card that says attention outputs only: 14 attention outputs of layers 17 to 31 and 11 down projections of 18 to 31 (25 of 2,130), the down projections edits by every measure (first shares 0.40 to 0.94, input side, weights 1.23 to 1.51), five more tensors under the line at 0.00013 or less; the window ends at 31 against the card's 42; the directions at 0.99 to coder3101's E4B edit and 0.98 and 0.99 to the maker's Refusals5; byte-range reads show the maker's Refusals6-attn copy edits down projections too |

Nothing moved outside the matrices the maker's method reaches in any of the eight pairs: the largest relative
change outside the changed set is exactly 0 on pairs 1, 2, 3, 4 and 7, and on pairs 5, 6 and 8 it is the search's
own footprint on matrices inside the window (0.00098 on four down projections, 0.00091 on one, 0.00013 on four down
projections and one attention output). Seven of the eight copies are what their cards say, two of them with a
qualification the card's parameters predict: wnfldchen's rows under a preservation weight of 0.1182 are not
preserved, and TheUmbraWalker's field names the pretrained base as finding 67 says the tool's card does. The eighth
is the round's result for the method. NullpoLab's card names one writer and the weights carry two, on this copy
and, by byte range, on the maker's other "attn" copy; the tool's pull-request branch applied the ablation to both
writers whatever `target_components` said, and the cards print the setting. The census reads the effect and not
the setting, which is what the writer count is for.

The weights read off the weights. The five arbitrary-rank edits by the maker's own solver (pairs 3, 5, 6, 7 and
8) read on the input side on 27 of 30, 36 of 36, 26 of 26, 11 of 11 and 25 of 25 matrices at weights of 1.2 to 2.6
with their tails to 4.4 and 4.5, and MoonRide's two searches edit 36 of 44 and 26 of 33 matrices in their windows
and leave the rest as residues without a direction, finding 58's shape with the search's selection visible. The
two LoRA-adapter exports (pairs 1 and 2) read on the input side at 0.74 to 2.09 with a few directions per matrix.
Pair 4's per-layer pass carries no readable weight, finding 46's scatter, where the same pass on the Mistral bases
reads its kernel.

Preservation claims. Four copies claim row-norm preservation and three hold it: MoonRide's two edits read 0.0059
to 0.0077 on all 36 and 0.0051 to 0.0078 on all 26, finding 22's band on 61 of 62 edited matrices; OS-Software's
two exports read at or under the band (0.0003 to 0.0057 on 54, 0.0012 to 0.0081 on 32). wnfldchen's 31B export
reads 0.014 to 0.75 on all 30, the first preservation claim in the census that holds on no matrix; its weight for
good behaviour is 0.1182 against the 12B export's 0.9174, and the rows went with the weight. Pairs 4, 7 and 8
claim nothing and read 0.003 to 0.015, 0.003 to 0.037 and 0.0008 to 0.014.

Fingerprints. Pair 1's first shard (`513abfa9`) is the 12B QAT library layout shared with wnfldchen's and igorls's
exports; pair 2 shares five of its eleven shards with the maker's English v2 export, the shards the window does
not touch; pair 4's second shard (`df30ce31`) is byte-equal to the maker's second copy's and its first and fourth
are the E4B layout and the shared vision tower (findings 71 and 75). Pairs 3, 5, 6, 7 and 8 share no checksum
with any measured file. The QAT originals: the 12B checkpoint's revisions `b6ed8627` and `58540658` carry one
weight file (`26f2cee4`), and pairs 1 and 7 are pinned at the two, as finding 75 read.

Directions. The round placed its edits against the saved vectors of earlier measurements without a download
(finding 66's check): one hundred and nine comparisons against the saved vectors of measurements of the 12B (thirty-three), the
26B-A4B (twenty-two), the 31B (twenty) and the E4B (thirty-four), this round's own among them. MoonRide's two April edits
are the earliest members of the arbitrary-rank families of finding 82: the 31B at 0.97 and 0.99 to llmfan46's and
0.95 and 0.98 to coder3101's, the E4B at 0.99 on both sides to NullpoLab's Refusals5 and coder3101's; NullpoLab's
Refusals8-attn stands at 0.99 to coder3101's and 0.98 and 0.99 to Refusals5, its down projections on the family's
down direction; llmfan46's 12B QAT edit stands at 0.97 and 0.94 to coder3101's 12B QAT edit and 0.95 to the
maker's own instruct edit, finding 72's rule a fifth time. wnfldchen's rank-256 search keeps the 31B family's
output direction (0.78 to 0.85 on the left) and loses its input direction (0.37 to 0.40 on the right).
OS-Software's two Japanese-prompt searches stand apart from the English families: 0.40 and 0.30 to coder3101's
12B edit, 0.62 to 0.70 to the maker's own English 26B export and the two English 26B edits, where the English
searches on one base stand at 0.92 to 0.97 (the 12B) and 0.94 (the 26B-A4B) to each other. TheUmbraWalker's first pass is the second copy's
direction at 1.000 on 57 of 73 and TrevorJS's at 0.98 and 0.99 on all 73: Heretic's per-layer pass and the
abliteration script's per-layer mean difference find the same direction on this base.

## The token side

The cluster's cards read "unexplained differences" on five of the eight and "consistent with re-save noted" on
three. The home judgement under transformers 5.22.1 with the originals' later commits moved five fields on four
cards: `text_config.moe_intermediate_size` on pairs 4, 5, 6 and 8 (absent on one side, the same default under
5.22.1) and pair 8's template, byte-equal to Google's revision `c53e9d33` of 04-28, which the later-revision check
matches; all four turn to consistent with re-save noted. What stays open is pair 7's `tokenizer_config.json`,
which carries the maker's 21,488-byte macro template in place of the pin's `chat_template.jinja` and a
`tokenizer.json` 154 bytes longer, the habit finding 19 read on the maker's instruct 12B copy. Pairs 1, 2 and 3
differ in version strings alone; pair 1's template differs from the pin's by its line endings and renders the
same.

## What the scorer learned

The flag counts are the same on the cluster and at home. Their causes, by pair:

- Arbitrary-rank edits under the per-layer entry, 108, 64, 30, 84, 65, 11 and 45 flags (pairs 1, 2, 3, 5, 6, 7
  and 8): a few directions per matrix fails the first-share rule on every edited matrix, and where both writers
  are edited each with its own direction the within-layer rule fails as well. An arbitrary-rank entry with the
  card's window and `target_components` would read pairs 3 and 7 as clean matches, pairs 1, 2, 5 and 6 as clean
  matches with the residues named, and pair 8 as eleven matrices outside the declared set, the right reading.
- A clean per-layer read, 8 flags (pair 4): four layers whose two writers agree at 0.91 to 0.95 where the rule
  asks 0.95.

The round's result for the measure is pair 8: the writer count the method reads from the weights disagreed with a
card, and byte-range reads on a sibling copy showed the weights right. The changed set is the check on the card,
not the other way round.

## Owed to the metadata tool

Added since: nothing this round. What remains: the earlier-revision template through a snapshot older than the
pin (round 31's pairs 2 and 4, round 35's pair 5); the declared-context line; the float16 `dtype` reading; the
5.16 save form as a named re-save (finding 39); the dropped-declarations rule through `tokenizer.json`; and from
this round, a maker's-template rule that names a `tokenizer_config.json` template seen on the maker's earlier
copies (pair 7, llmfan46's macro template a second time). To the pinner: a shape check at the names step, after
the round 39 pin stage read TurkishCodeMan/gemma-4-e2b-it-abliterated as a partial E2B export when all 164 of its
tensors differ in shape from the E2B's (finding 88); and the card's `target_components` read into the batch note so
that a one-writer card measured on both writers is flagged at the pin rather than at the reading (pair 8). To the
recipe table: an arbitrary-rank entry (window, target components, residues allowed, rows in the band under a
claim) and a LoRA-adapter variant of it, which seven of this round's eight pairs would match.

## Operational

The round ran on Wheat under the image-free kit with the standalone Python: one download, eight compares and the
sweep, every compare finishing with its card and its weights report, the sweep deleting the eight originals. The
pull carries the eight measurement folders (card, metadata, weights, direction vectors and the sha256 record of
each) and the sweep record; no job log was pulled, so the compares' nodes and seconds are not recorded. The home
judgement ran under transformers 5.22.1. Seven readings were made at home from the hub by byte range
(`tools/hub_range_read.py`): the down projections of layers 24, 28 and 33 and the attention output of 28 of
NullpoLab's Refusals6-attn and Refusals8-attn copies against google/gemma-4-E4B-it, and TurkishCodeMan's layer 0
query, layer 17 attention output, layer 9 down projection and two norms against google/gemma-2b-it,
google/gemma-1.1-2b-it and google/gemma-2b. The hub's commit histories and file listings were read for the eight
copies, NullpoLab's three sibling repositories, wnfldchen's adapter repository and TurkishCodeMan's. One hundred and nine
comparisons were made from the saved direction files, listed in the reading notes.

Weight differences alone cannot certify the absence of hidden behavior.
