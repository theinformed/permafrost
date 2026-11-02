# Census round 36: eight pairs on Nautilus, every one on a QAT-unquantized checkpoint (2026-11-02)

Eight published copies compared with their originals on Nautilus from the batch pinned as
`data/batches/round-36-batch-1.json` (pinned 2026-11-02 04:15Z) under the CPU census kit: download job 4167620,
compares 4167621 to 4167628, sweep 4167629, which deleted the six originals (`f947cd25` of
google/gemma-4-31B-it-qat-q4_0-unquantized at `4f926903` for pairs 1 and 2, `20e0b4c7` of the 26B-A4B QAT checkpoint
at `641f1844` for pair 3, `8b30c5a4` of the 31B QAT checkpoint at `1e4d8bee` for pair 4, `be573839` of the 12B QAT
checkpoint at `b6ed8627` for pairs 5 and 6, `f601ea62` of the 26B-A4B QAT checkpoint at `f1e06dc5` for pair 7 and
`d5f88f28` of the 12B QAT checkpoint at `58540658` for pair 8) from `/p/work1/sdegan/model-audit/rounds/36/originals/`.
The pull brought home the eight measurement folders and the sweep record and no job log, so the compares' nodes and
seconds are not in this note. The batch note says what the round is: the QAT-unquantized copies left after rounds 32
to 35, each pinned against the QAT checkpoint its name cites rather than the instruct model its card header names
(finding 67), and no pair repeats a measured pair. All eight are first measurements of distinct copies, none a
re-upload, and no original is new (the 31B QAT checkpoint entered the census with round 37, which was read out
before this round), which brings the population to one hundred and sixty-seven measurements of one hundred and sixty
distinct copies on thirty-three originals: the round 37 header's numbers plus eight measurements and eight copies.
Three pairs are Heretic 1.2.0 arbitrary-rank edits (llmfan46's and coder3101's of the 31B checkpoint, coder3101's
of the 26B-A4B), two are OS-Software's Heretic v2 rank-four transport edits (the 31B and the 12B, the maker's third
and fourth bases), one is a Heretic v1 kernel pass (JJaguar's, the 12B), one is a kernel searched on the instruct
26B-A4B and transferred to its QAT checkpoint with the experts edited (Mitchins's), and one is OS-Software's first
Japanese-prompt export (the 12B). The eight measurements were re-scored at home with the recipe table as committed
and the saved direction vectors, and no flag count moved. Every metadata report was judged again at home under
transformers 5.22.1 with the originals' later commits, and the home judgement moved no field on any of the eight:
the three `per_layer_config` cards and the regenerated generation configuration stay as the cluster read them.
Each pair has a card (the tool's Stage 1 text, with the Stage 2 line) and a reading note in `docs/cards/`; the
measurements are in `results/weights/` and `results/meta/`, and the direction vectors stay in the pull copy
(`/opt/ai/hpc-packages/pulls/model-audit/nautilus36/measurements/pair-N/`).

| Pair | Copy | Original | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | llmfan46/gemma-4-31B-it-qat-q4_0-unquantized-uncensored-heretic | google/gemma-4-31B-it-qat-q4_0-unquantized at `4f926903` | violations, 16 flags (first shares 0.877 to 0.979) | Heretic 1.2.0's arbitrary-rank edit on a selection of the card's window: the attention outputs of layers 16, 18, 21, 22 and 24 to 35 (16 of 1,188) inside the card's 9 to 35 and on its one target, ten more layers of the window rewritten under the threshold (0.00003 to 0.000195), input side on all 16 at weights 1.58 to 3.64, rows 0.0023 to 0.052 under no claim; the directions at 0.99 to coder3101's edit of the same checkpoint and 0.93 to the maker's own instruct edit; the maker's 23,077-byte template again |
| 2 | coder3101/gemma-4-31B-it-qat-q4_0-unquantized-heretic | google/gemma-4-31B-it-qat-q4_0-unquantized at `4f926903` | violations, 21 flags (first shares) | the same tool's edit with row-norm preservation on the card's window 15 to 38: 17 attention outputs edited (16, 22 and 24 to 38) at weights 1.52 to 3.79 with layer 16 at 0.57, rows 0.0068 to 0.0079 on all 17, four residues above the threshold and three under it (largest 0.000898); the directions at 0.99 to llmfan46's and 0.96 to the maker's own instruct edit |
| 3 | coder3101/gemma-4-26B-A4B-it-qat-q4_0-unquantized-heretic | google/gemma-4-26B-A4B-it-qat-q4_0-unquantized at `641f1844` | violations, 9 flags (first shares 0.444 to 0.955) | the same edit on the attention outputs of layers 12 to 20 (9 of 1,013), the card's window exactly, no expert touched, input side at weights 1.06 to 1.81, rows 0.0067 to 0.0077 on all 9; exactly 0 outside; the directions at 0.99 to llmfan46's QAT edit and 0.94 to the maker's own instruct edit |
| 4 | OS-Software/gemma-4-31B-it-qat-q4_0-unquantized-uncensored-heretic | google/gemma-4-31B-it-qat-q4_0-unquantized at `1e4d8bee` | violations, 44 flags (22 first shares, 22 within-layer cosines) | Heretic v2's rank-four transport edit on both writers of layers 30 to 40 (22 of 1,188), the card's window, fourth cumulative shares 0.993 to 0.998, input side at weights 0.86 to 2.05 and 0.99 to 2.39, writers unrelated within a layer, rows 0.0012 to 0.037 under "none"; exactly 0 outside; the leading input direction at 0.65 to 0.77 to the arbitrary-rank family; the field names the instruct model |
| 5 | OS-Software/gemma-4-12B-it-qat-q4_0-unquantized-uncensored-heretic-v3 | google/gemma-4-12B-it-qat-q4_0-unquantized at `b6ed8627` | violations, 35 flags (17 first shares, 18 within-layer cosines) | the same rank-four edit on both writers of layers 23 to 31 (18 of 677), fourth cumulative shares 0.989 to 0.999, input side at weights 0.76 to 1.67 and 0.58 to 2.43, rows 0.0010 to 0.031 under "none"; exactly 0 outside; the leading input direction at 0.59 to 0.68 to the arbitrary-rank family; the field names the instruct model |
| 6 | JJaguar/gemma-4-12B-it-qat-q4_0-unquantized-heretic-nx | google/gemma-4-12B-it-qat-q4_0-unquantized at `b6ed8627` | violations, 2 flags (one first share 0.980, one cross-kind cosine 0.85) | Heretic v1's kernel pass: the down projections of layers 21 to 46 and the attention outputs of 25 to 47 (49 of 677), the two kernels' reach to the layer, one direction (group cosines 0.96 to 1.00), kept fractions that read no kernel; exactly 0 outside; the direction at 0.90 to five kernel exports of the instruct 12B and 0.25 to the thinking-on search of the same checkpoint; the field names the instruct model |
| 7 | Mitchins/gemma-4-26B-A4B-it-qat-q4_0-unquantized-uncensored-heretic | google/gemma-4-26B-A4B-it-qat-q4_0-unquantized at `f1e06dc5` | violations, 8 flags (seven worst experts, one within-layer cosine) | a kernel searched on the instruct model and transferred to the QAT checkpoint, as the card and its `reproduce/` record say: the attention outputs of layers 3 to 29 with the dense down projections of 15 to 23 and all 128 experts of 11 to 26 (52 of 1,013), the record's three kernels to the layer, one direction through all three kinds, rows 0.007 to 0.022 on the dense writers and 0.03 to 0.18 on the experts under "full" row normalisation; exactly 0 outside; a generation configuration rewritten by the loader (sampling and the `<|tool_response>` stop token gone) |
| 8 | OS-Software/gemma-4-12B-it-qat-q4_0-unquantized-heretic-ja | google/gemma-4-12B-it-qat-q4_0-unquantized at `58540658` | violations, 138 flags (66 first shares, 72 within-layer cosines) | the LoRA-adapter arbitrary-rank branch searched on Japanese prompts, on both writers of layers 10 to 46 (73 of 677), the card's window, one attention output under the threshold (0.000086), input side at weights 0.74 to 1.77 and 0.79 to 3.73, rows 0.0007 to 0.21 under no claim; the output direction at 0.52 to 0.64 to the English family, closer than the maker's second Japanese search |

Nothing moved outside the matrices the maker's method reaches in any of the eight pairs: the largest relative
change outside the changed set is exactly 0 on pairs 3, 4, 5, 6 and 7, and on pairs 1, 2 and 8 it is the search's
own footprint on matrices inside the window (0.000195 on ten attention outputs of llmfan46's window, 0.000898 on
three of coder3101's, 0.000086 on one of OS-Software's). All eight copies are what their cards say at the weight
level, two of them with a qualification the card's own numbers predict: llmfan46's and coder3101's searches
edited a selection of their windows and left the other layers as residues, finding 22's shape; Mitchins's "full"
row normalisation holds on the dense writers and not on the experts. The eighth is also the round's token-side
result: Mitchins's `generation_config.json` was written by the library from the model configuration, which
dropped the checkpoint's sampling settings and its third stop token, and the card does not say so.

The weights read off the weights. The three arbitrary-rank edits by the maker's own solver (pairs 1, 2 and 3)
read on the input side on 16 of 16, 17 of 17 and 9 of 9 matrices at weights of 1.5 to 2.3 in the middle with
tails to 3.6 and 3.8 on the 31B, where the two 31B searches left ten and seven layers of their windows as
residues. The two rank-four transport edits (pairs 4 and 5) read four directions per matrix exactly (fourth
cumulative shares 0.989 to 0.998) on both writers, input side, writers unrelated within a layer, finding 42's
shape on two more bases. The LoRA-adapter Japanese search (pair 8) reads a few directions per matrix on both
writers at the largest weights of the maker's exports (3.73 and 3.08 on two attention outputs). The two kernel
passes (pairs 6 and 7) read one direction through every edited matrix and no kernel in their kept fractions,
finding 46's scatter, on the 12B QAT checkpoint and on the mixture's dense writers and experts alike.

Preservation claims. Two copies claim row-norm preservation and hold it: coder3101's two edits read 0.0068 to
0.0079 on all 17 and 0.0067 to 0.0077 on all 9, finding 22's band on every matrix. Mitchins's record says "full"
row normalisation at adapter rank 3, and the rows read 0.007 to 0.016 on the attention outputs, 0.009 to 0.022 on
the dense down projections and 0.028 to 0.18 on the experts. OS-Software's three cards print "none" or nothing
and read 0.001 to 0.037, 0.001 to 0.031 and 0.0007 to 0.21; llmfan46's and JJaguar's claim nothing and read
0.0023 to 0.052 and 0.0026 to 0.011.

Fingerprints. The two 31B QAT edits (pairs 1 and 2) share their second shard (`fd00e7a5`), the half of a
two-shard save that neither window reaches; the 12B exports of OS-Software and JJaguar (pairs 5 and 6) share
their first two shards (`513abfa9`, `ebfb917e`), and the first is the layout finding 71 read on wnfldchen's,
igorls's and the maker's `-ja-v2` exports. Pairs 3, 4, 7 and 8 share no checksum with any measured file; pair 7's
eleven shards equal the checksums in the maker's own `SHA256SUMS`. Google's 31B QAT revisions `4f926903` and
`1e4d8bee` carry one pair of shards (`8ad3c678`, `a373e714`), as the 12B's and 26B-A4B's revisions do (finding 75).

Fields. Four of the eight `base_model` fields name the instruct model (OS-Software's three cards, JJaguar's) while
the README's first sentence names the QAT checkpoint; the pinner paired them by the rule in `docs/weights-method.md`
and the weights confirm it, exactly 0 outside the windows against the QAT files. Three name the QAT checkpoint
(llmfan46's, coder3101's two) and Mitchins's names both.

Directions. The round placed its edits against the saved vectors of earlier measurements without a download
(finding 66's check): two hundred and eighteen comparisons against the saved vectors of measurements of the 31B
and its QAT checkpoint (twenty-three for each of three pairs), the 26B-A4B and its checkpoint (twenty-two for each
of two) and the 12B and its checkpoint (thirty-five for each of three), this round's own among them. coder3101's and
llmfan46's searches of the 31B QAT checkpoint, five days apart with different parameters, stand at 0.99 to each
other on the 14 matrices both edit, the closest agreement between two makers' searches the census has read, and
at 0.93 to 0.96 to the two makers' instruct 31B edits; coder3101's 26B-A4B QAT edit stands at 0.99 to llmfan46's
QAT edit and 0.94 to the maker's own instruct edit: finding 72's rule on three more pairs (finding 89). OS-Software's
two rank-four edits stand at 0.56 or less on the left to every edit and at 0.59 to 0.77 on the right to the
arbitrary-rank families (finding 90). JJaguar's kernel pass stands at 0.90 to the five kernel exports of the
instruct 12B and at 0.25 to igorls's thinking-on search of the same checkpoint (finding 91). Mitchins's transferred
kernel stands apart, at most 0.57 to sh0ck0r's and 0.47 to TrevorJS's (finding 92). OS-Software's first Japanese
search stands at 0.52 to 0.64 on the left to the English arbitrary-rank family and 0.59 to its own second search,
where the second stood at 0.30 to 0.40 to the family (finding 93).

## The token side

The cluster's cards read "unexplained differences" on four of the eight and "consistent with re-save noted" on
four. The home judgement under transformers 5.22.1 with the originals' later commits moved no field: the
`per_layer_config` map of a 5.15 or 5.16 save on pairs 4, 5 and 7 (finding 39's form, closed by hand each time),
pair 7's generation configuration (`_from_model_config` true; `do_sample`, `top_k` 64 and `top_p` 0.95 gone;
`eos_token_id` [1, 106] where the checkpoint has [1, 106, 50], the `<|tool_response>` token) and pair 1's template
(llmfan46's 23,077-byte file, equal to the maker's 26B QAT export's and rendering identically, finding 19) stay
open. Pairs 2, 3, 6 and 8 differ in version strings alone.

## What the scorer learned

The flag counts are the same on the cluster and at home. Their causes, by pair:

- Arbitrary-rank edits under the per-layer entry, 16, 21, 9 and 138 flags (pairs 1, 2, 3 and 8): a few directions
  per matrix fails the first-share rule on every edited matrix and on coder3101's four residues, and where both
  writers are edited each with its own direction the within-layer rule fails as well. An arbitrary-rank entry with
  the card's window with residues allowed and rows in the band under a claim would read pairs 1, 2 and 3 as clean
  matches, and its LoRA-adapter variant would read pair 8 as a clean match with one residue.
- Rank-four transport edits under the per-layer entry, 44 and 35 flags (pairs 4 and 5): the rank-stated subspace
  entry finding 42 asked for would count none.
- Kernel passes, 2 and 8 flags (pairs 6 and 7): one first share at 0.980 and a cross-kind cosine at 0.85 on
  JJaguar's; the worst expert of seven packed tensors at 0.976 to 0.989 and one layer at 0.867 on Mitchins's,
  finding 13's reading of the worst expert where the median expert is above the line.

The round's result for the measure is the pair of 31B searches: two makers' solvers on one checkpoint, with
different windows and settings, found one direction to 0.99, which is what a direction library indexed by method
needs to place a new copy before its weights are read.

## Owed to the metadata tool

Added since: nothing this round. What remains: the earlier-revision template through a snapshot older than the
pin (round 31's pairs 2 and 4, round 35's pair 5); the declared-context line; the float16 `dtype` reading; the
5.15 and 5.16 save form as a named re-save (finding 39, three more cards this round); the dropped-declarations rule
through `tokenizer.json`; the maker's-template rule (finding 19, llmfan46's 23,077-byte template a second time);
and from this round, a rule that names a generation configuration the library regenerated from the model
configuration (`_from_model_config` true) and lists what it dropped against the original's file, so that pair 7's
eight fields read as one event. To the pinner: the card's `base_model` against its first sentence read into the
batch note where they differ (four of the round's eight), beside the shape check and the `target_components` line
round 37 asked for. To the recipe table: the arbitrary-rank entry and its LoRA-adapter variant (seven of this
round's eight pairs and seven of round 37's would match one of them), the rank-stated subspace entry, and a kernel
entry that reads the card's kernels to the layer and takes the median expert.

## Operational

The round ran on Nautilus under the CPU census kit: one download and eight compares, then the sweep, every compare
finishing with its card and its weights report, the sweep deleting the six originals. The pull carries the eight
measurement folders (card, metadata, weights, direction vectors and the sha256 record of each) and the sweep
record; no job log was pulled, so the compares' nodes and seconds are not recorded. The home judgement ran under
transformers 5.22.1. No byte-range read was needed. The hub's commit histories and file listings were read for the
eight copies and the three QAT originals, the eight READMEs at the pinned revisions, Mitchins's `reproduce/` folder
(its record with the configuration and checksum list) and the 26B-A4B QAT checkpoint's `tokenizer.json` for the identity
of token 50. Two hundred and eighteen comparisons were made from the saved direction files, listed in the reading
notes.

Weight differences alone cannot certify the absence of hidden behavior.
