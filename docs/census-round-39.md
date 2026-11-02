# Census round 39: eight direct Gemma 4 copies on Wheat, one standing on the pretrained base under a card naming the instruct model, one a hub duplicate of an unmeasured projection over a third party's fine-tune, and the tool author's own reproduction at 1.000 (2026-11-02)

Eight published copies compared with their originals on Wheat from the batch pinned as
`data/batches/round-39-batch-1.json` (pinned 2026-11-02 06:41Z) under the image-free kit with the standalone
Python: download job 387181, compares 387182 to 387189, sweep 387190, which deleted the five originals (`726eaa98`
of google/gemma-4-26B-A4B-it at `47b6801b` for pair 1, `ed9be084` of google/gemma-4-E4B-it at `292a7e27` for pairs 2
and 8, `52250dca` of the E4B at `fee6332c` for pair 3, `6273b5b6` of google/gemma-4-E2B-it at `4742fe84` for pairs 4,
5 and 7, and `c81b1ac4` of google/gemma-4-12B-it at `707f0a3b` for pair 6) from
`/p/work/sdegan/model-audit/rounds/39/originals/`. The pull (card 5770) brought home the eight measurement folders
and the sweep record and no job log, so the compares' nodes and seconds are not in this note. The batch note says
what the round is: eight direct copies of the Gemma 4 instruct models not yet measured, pinned from the unmeasured
list by downloads and mixed by size class, the pinner having refused six re-uploads of measured files
(ScottzillaSystems's, benbird316's, liham86's, Ishowbackup's and AgentAnon's copies of TrevorJS's and Jiunsong's
files, Huy112200's of Himanshuoo8's), yeyuxx's 26B multimodal export whose names pair with nothing in the original,
and TurkishCodeMan's E2B copy, a partial export of eighteen of thirty-five layers; OS-Software's CyberStag copy is
held until deer-sec's MLX export has a name recipe, and Jiunsong's 26B multimodal copy and AgentAnon's 26B copy are
gone from the hub. The note also records that tvall43's E2B copy drops the original's 128 vision-encoder range
scalars, listed apart as `dropped_statistics`. Seven of the eight are first measurements of distinct copies and the
eighth, Paul691's, is a hub duplicate of OpenYourMind's unmeasured 12B copy (one commit titled "Duplicate from",
every file byte-equal); no original is new, the five Google revisions all standing in the population already, which
brings the population to one hundred and eighty-three measurements of one hundred and seventy-six distinct copies
on thirty-three originals: the round 38 header's numbers plus eight measurements and eight copies. Two pairs are
Heretic 1.2.0 kernel passes by one maker on one evening (tvall43's E2B and 26B-A4B), one is the Heretic author's
own second reproduction of his E4B export (p-e-w's REPRODUCED-2), three are arbitrary-rank edits from the tool's
pull-request branch (MoonRide's two E2B exports, NullpoLab's Refusals8), one is a Heretic 1.1.0 kernel pass made on
the pretrained google/gemma-4-E4B under a card naming the instruct model (chulcher's), and one is a
single-direction projection over the coder fine-tune of finding 25, reached through the duplicate (OpenYourMind's
through Paul691's). The eight measurements were re-scored at home with the recipe table as committed and the
saved direction vectors, and no flag count moved. Every metadata report was judged again at home under
transformers 5.22.1 with the originals' later commits; the home judgement moved one field on each of pairs 2, 3,
4, 5 and 7 and two on pair 8 (pairs 3, 4, 5, 7 and 8 turn to consistent with re-save noted; pair 2 stays
unexplained for the pretrained checkpoint's token ids, pair 6 for Google's earlier revision) and none on pairs 1
and 6. Each pair has a card (the tool's Stage 1 text after the home judgement, with the Stage 2 line) and a
reading note in `docs/cards/`; the measurements are in `results/weights/` and `results/meta/`, and the direction
vectors stay in the pull copy (`/opt/ai/hpc-packages/pulls/model-audit/wheat39/measurements/pair-N/`).

| Pair | Copy | Original | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | tvall43/gemma-4-26B-A4B-it-heretic | google/gemma-4-26B-A4B-it | clean match of `directional-per-layer-selected`, 0 flags | one direction per layer projected from the attention outputs of layers 16 to 29 (14 of 1,013), the stack's last fourteen, no down projection and no expert; output side at a flat weight of 4.09 to 4.18 where the card prints four kernels peaking at 24.12; rows 0.05 to 0.41 under no claim; exactly 0 outside; the directions at 0.98 to the 26B-A4B kernel exports and 0.97 to TrevorJS's |
| 2 | chulcher/gemma-4-e4b-abliterated | google/gemma-4-E4B-it | violations, 680 flags (510 unexpected changes, 85 first shares, 84 direction cosines, 1 cross-kind) | the pretrained google/gemma-4-E4B with a Heretic 1.1.0 kernel pass inside it, under a card and a field naming the instruct model: every linear map of the language stack, the embeddings, the per-layer gates and projections and 209 norms moved 0.001 to 0.76 with no direction (595 of 2,130), the towers exactly 0; the saved directions at 1.000 to Felldude's measurement against the pretrained checkpoint on all 347 shared names; by byte range, byte-equal to the pretrained checkpoint on nine tensors outside the card's two kernel windows and 0.02 to 0.03 from it on three inside; the token ids the pretrained checkpoint's |
| 3 | p-e-w/gemma-4-E4B-it-heretic-REPRODUCED-2 | google/gemma-4-E4B-it | violations, 37 flags (32 first shares, 4 direction cosines, 1 cross-kind) | the tool author's second reproduction of his own E4B export, twenty-two minutes after it: the attention outputs of layers 11 to 41 and the down projections of 5 to 41 (68 of 2,076), the card's two kernels to the layer and in shape (down projections 0.47 to 1.34 to 0.86 on the output side under a card maximum of 1.47); rows 0.0027 to 0.0086 under "full" normalisation; exactly 0 outside; every per-tensor number equal to the first export's to four to six digits and to the last digit on none, the directions at 1.000 on all 68, the tensors 0.0001 apart by byte range where the first export and REPRODUCED are byte-equal |
| 4 | tvall43/gemma-4-E2B-it-heretic-v1 | google/gemma-4-E2B-it | clean match of `directional-per-layer-selected`, 0 flags | one direction per layer on both writers inside the card's two windows to the layer (the attention outputs of 21 to 34 and the down projections of 24 to 32, 23 of 1,883), output side at weights of 3.33 rising to 4.53 on the attention outputs and 3.67 to 3.88 on the down projections, a third of which the card's kernels print; rows 0.03 to 0.17 and 1.63 on one matrix; exactly 0 outside; the directions at 0.98 to TrevorJS's E2B edit and 0.99 to anlord's; the vision encoder's 128 range scalars dropped by the save and listed apart |
| 5 | MoonRide/gemma-4-E2B-it-heretic-ara | google/gemma-4-E2B-it | violations, 32 flags (16 first shares, 16 within-layer cosines) | the arbitrary-rank branch on both writers of layers 15 to 22 (16 of 2,011), the card's window exactly; twelve edits on the input side at weights 0.58 to 1.23 with rows 0.0065 to 0.0078, the band, and four down projections left as residues at 0.0018; exactly 0 outside; the directions at 0.80 and 0.97 to llmfan46's ultra edit and 0.51 to the maker's own export of the next day |
| 6 | Paul691/gemma-4-12B-it-abliterated-uncensored | google/gemma-4-12B-it | violations, 649 flags (457 unexpected changes, 96 direction cosines, 95 first shares, 1 cross-kind) | a hub duplicate of OpenYourMind's unmeasured 12B copy: one direction per matrix projected from the output side at a weight of 0.40 on both writers of all 48 layers (left kept 0.590 to 0.606 on all 96), over the coder fine-tune finding 25 placed under lemuralabs's copy, the 228 readers equal to lemuralabs's report to the last digit and byte-equal by byte range, the directions at 1.000 on all 228; 553 of 677 changed, 67 more under the threshold; a card whose first revision claimed a "healing" pass and dropped the claim four minutes later; the context length and template Google's revision of the day the parent was made |
| 7 | MoonRide/gemma-4-E2B-it-heretic-ara-custom | google/gemma-4-E2B-it | violations, 76 flags (38 first shares, 38 within-layer cosines) | the arbitrary-rank branch searched with a custom system prompt on both writers of layers 16 to 34 (38 of 2,011), the card's window exactly; 35 edits on the input side at weights 0.18 to 1.30 with rows 0.0060 to 0.0078, the band, and three residues; exactly 0 outside; the directions at 0.87 to coder3101's QAT edit, 0.85 to llmfan46's and 0.51 to the maker's export of the day before |
| 8 | NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals8 | google/gemma-4-E4B-it | violations, 56 flags (28 first shares, 28 within-layer cosines) | the arbitrary-rank branch on both writers of layers 21 to 34 (28 of 2,130), the card's window exactly, every matrix edited; input side at weights 0.83 to 1.27 with rows 0.0011 to 0.0096, at and under the band; exactly 0 outside; the directions at 0.99 to the maker's Refusals8-attn, 0.94 to coder3101's and Refusals5 and 0.90 or better to the rest of finding 82's E4B family; the template Google's 04-28 revision, carried in by the 04-29 upload |

Nothing moved outside the matrices the maker's method reaches in six of the eight pairs: the largest relative
change outside the changed set is exactly 0 on pairs 1, 3, 4, 5, 7 and 8. On pairs 2 and 6 the changed set is the
whole language stack and the question is whose: on pair 6 the readers are the coder fine-tune, equal to
lemuralabs's report on all 228 and byte-equal to lemuralabs's copy by byte range, with 67 more tensors under the
threshold to 0.000989; on pair 2 the changed set is Google's instruction tuning, the saved directions at 1.000 to
Felldude's measurement of the pretrained checkpoint, with 39 norms under the threshold to 0.000878. Six of the
eight copies are what their cards say (pairs 1, 3, 4, 5, 7 and 8), two of them with a qualification the weights
supply: tvall43's two cards print kernels whose shape and height the weights do not show (a flat 4.1 on the 26B-A4B,
3.3 to 4.5 on the E2B), and the three arbitrary-rank cards do not name the row-norm preservation the branch applies
and the rows show. The seventh and eighth are the round's results for the method. chulcher's E4B copy names
google/gemma-4-e4b-it in its field, its links and its title and stands on the pretrained google/gemma-4-E4B: the
census's one measurement on that checkpoint, Felldude's, placed it at 1.000 on 347 names before any byte was
read, nine byte-range reads outside the card's kernel windows are byte-equal to the pretrained checkpoint, three
inside them are 0.02 to 0.03 from it, and the copy's token ids and shipped evaluation ("Gemma 4 E4B Base") say the
same. Findings 26 and 62 read the field naming the pretrained base over weights on the instruct model; this is the
reverse, and the measurement reads the instruction tuning with the edit lost inside it. OpenYourMind's 12B copy,
through Paul691's duplicate, names Google as its one parent and carries yuxinlu1's coder fine-tune under its
projection, the fine-tune finding 25 named under lemuralabs's copy from the normalisation vectors: here the
readers are equal to lemuralabs's to the last digit on all 228, byte-equal on the three read, and the saved
directions at 1.000 on every one, while the writers carry a projection of the maker's own at 0.40 that is not
lemuralabs's (the layer 20 attention outputs 0.0424 apart, more than either stands from Google's). Two makers, two
projections, one fine-tune under both, and neither card names it.

The weights read off the weights. tvall43's two kernel passes (pairs 1 and 4) read one direction per layer on the
output side at weights the cards do not print: 4.09 to 4.18 across fourteen attention outputs on the 26B-A4B, and
3.33 to 4.53 on the E2B's attention outputs with 3.67 to 3.88 on its down projections, the E2B's windows to the
layer from the card's peaks and minimum distances (32.17 less 11.43 is 20.7, 28.03 less and plus 4.34 is 23.7 to
32.4) and the 26B-A4B's window the stack's end. p-e-w's reproduction (pair 3) reads the author's two kernels in
shape on the output side (the down projections 0.47 at layer 5, 1.34 at 26, 0.86 at 41, under a printed maximum
of 1.47 at 27.73; the attention outputs 0.17, 0.73, 0.41 under 0.81 at 26.47), finding 46's scatter on the right
side (0.03 to 0.85). The three arbitrary-rank edits (pairs 5, 7 and 8) read on the input side at weights 0.58 to
1.23, 0.18 to 1.30 and 0.83 to 1.27, with the two writers of a layer unrelated (0.001 to 0.125), MoonRide's two
leaving four and three matrices as residues (finding 58) and NullpoLab's leaving none. OpenYourMind's projection
(pair 6) reads one direction per matrix at a left kept fraction of 0.590 to 0.606 on all 96 writers, a weight of
0.40 on the output side with the right side keeping 0.72 to 0.99, the directions differing between the two writers
of a layer (median 0.25) and across layers (median 0.35). chulcher's edit (pair 2) has no readable side or weight
inside the instruction tuning; the byte-range reads give its windows.

Preservation claims. None of the eight cards claims a norm in words. The three arbitrary-rank cards carry the
branch's row-norm preservation unnamed and the rows read it: MoonRide's 0.0065 to 0.0078 on twelve edits and 0.0060
to 0.0078 on 35, finding 22's band on every edit, with the residues at 0.0007 to 0.0009; NullpoLab's 0.0011 to
0.0096, at and under the band as the maker's two earlier exports read. p-e-w's reproduce record says "full"
normalisation with a rank-3 correction and the rows read 0.0027 to 0.0086. tvall43's two passes leave the rows at
0.05 to 0.41 and 0.03 to 1.63, OpenYourMind's projection at 0.0015 to 0.175, unrestored.

Fingerprints. Pair 6's one weight file (`6503b6fa`) is byte-equal to OpenYourMind's, the duplicate read from the
commit title and the checksum before the measurement. Pair 3's first and fourth shards (`aa3e9d1e`, `8080cb1a`)
equal the first export's and the E4B library layout shared with sh0ck0r's, BinxNet's and TheUmbraWalker's exports,
the fourth with igorls's and prithivMLmods's QAT exports as well (finding 71); its second and third (`ad521587`,
`62d196fb`) differ from the first export's (`78c1ee08`, `2dda6bb6`), the shards that hold the 68 edited tensors,
0.0001 apart by byte range. Pairs 1, 2, 4, 5, 7 and 8 share no checksum with any measured file; pair 2's single
shard carries the pretrained checkpoint's tensors under the instruct template and is equal to neither Google
file.

Directions. The round placed its edits against the saved vectors of earlier measurements without a download
(finding 66's check): two hundred and forty-three comparisons against the saved vectors of measurements of the
26B-A4B (twenty-four), the E4B (seventy-eight), the E2B (sixty-five) and the 12B (thirty-seven), this round's own
among them. Two of them named a parent. chulcher's copy stands at 1.000 on both sides to Felldude's measurement
against the pretrained google/gemma-4-E4B on all 347 shared names (0.999 or better on every linear map, 0.958 at
the lowest on one per-layer input gate) and at 0.28 or less to every edit of the instruct model: the leading
direction of every tensor's change is the instruct-to-pretrained difference. OpenYourMind's copy stands at 1.000
to lemuralabs's on all 228 readers and at 0.00 to 0.85 on the 96 writers (median 0.11), so the shared part is the
fine-tune and the projection is the maker's own; against the other 12B edits its writers stand at 0.70 or less.
p-e-w's reproduction stands at 1.000 to the first export on all 68 names (minimum 1.000 on both sides), at 0.96 to
sh0ck0r's export and 0.94 to BinxNet's, and 0.82 to prithivMLmods's QAT kernel export: two runs of one method by
two makers at 0.96, the author's own reproduction at 1.000, the number the census had read only on re-uploads and
copies of a run (findings 85 and 95). tvall43's 26B-A4B stands at 0.98 to SevenOfNine's, BinxNet's and sh0ck0r's
kernel exports on all 14 names and 0.97 to TrevorJS's; the E2B at 0.99 to anlord's, 0.98 to TrevorJS's and 0.94 to
aifeifei798's, the one-direction family of finding 53, and at 0.15 or less to the arbitrary-rank edits. MoonRide's
two exports stand at 0.80 and 0.85 on the left to llmfan46's ultra edit and 0.68 and 0.87 to coder3101's QAT edit,
and at 0.51 on the left and 0.89 on the right to each other, a day apart with a custom system prompt between
them, a looser family than the E4B's. NullpoLab's Refusals8 stands at 0.99 to the maker's Refusals8-attn on all 20
shared names, 0.94 to coder3101's and to Refusals5, and 0.82 to 0.93 to the rest of finding 82's E4B family.

## The token side

The cluster's cards read "unexplained differences" on seven of the eight and "consistent" on pair 1. The home
judgement under transformers 5.22.1 with the originals' later commits moved seven fields on six cards:
`text_config.moe_intermediate_size` on pairs 2, 3, 4, 5, 7 and 8 (absent on one side, the same default under
5.22.1) and pair 8's template, byte-equal to Google's revision `c53e9d33` of 04-28 ("fix(chat_template): update SI
and tool call handling"), carried in by the copy's 04-29 upload. Pairs 3, 4, 5, 7 and 8 turn to consistent with
re-save noted, their remaining differences version strings (5.5.0.dev0 to 5.11.0, 5.5.0 and 5.5.1). Pair 2 stays
unexplained on three fields that are the pretrained checkpoint's values: the configuration's `eos_token_id` unset
where the instruct model's is `[1, 106]`, the generation configuration's 1 where the instruct model's is
`[1, 106, 50]`, and the tokenizer's end-of-sequence id with them; google/gemma-4-E4B at `a24c9379` declares exactly
these and ships no template, and the copy carries the instruct model's 11,926-byte template byte for byte beside
them. Pair 6 stays unexplained on two fields that are Google's own values of the day the parent was made:
`text_config.max_position_embeddings` 131,072 and a 17,466-byte template, both byte-equal to the original's
revisions `657684fe` and `66bc78a7` of 06-03 (the context raised to 262,144 by `5926caa4` on 06-04, the template
replaced at `711c1368` on 07-15), where the pin is `707f0a3b` of 07-20. Pair 1 differs in nothing.

## What the scorer learned

The flag counts are the same on the cluster and at home. Their causes, by pair:

- Two clean reads, 0 flags (pairs 1 and 4): the per-layer entry with selection fits one direction per layer on
  the attention outputs alone and on both writers; it has no weight line, and 4.1 and 3.3 to 4.5 are the largest
  output-side weights the census has read on a kernel pass.
- The single-projection entry on a kernel pass, 37 flags (pair 3): the first-share floor at 0.99 fails 32 matrices
  at 0.969 to 0.989, as it did on the first export; a kernel entry with the floor at 0.96 would read it clean.
- Arbitrary-rank edits under the per-layer entry, 32, 76 and 56 flags (pairs 5, 7 and 8): a few directions per
  matrix fails the first-share rule on every edited matrix and residue, and the two writers of a layer each with
  their own direction fail the within-layer rule; an arbitrary-rank entry would read all three as clean matches
  with the residues named.
- The wrong original, 680 flags (pair 2): every tensor of the instruction tuning is an unexpected change or a
  failed first share. The scorer cannot say whose change it reads; the direction comparison against the one
  measurement on the pretrained checkpoint did, and the pinner should run it at the names step.
- A projection over a fine-tune, 649 flags (pair 6): the 457 unexpected changes are the fine-tune's readers and
  norms, the 95 first shares and 96 direction cosines the writers whose first shares are 0.75 to 0.99 under one
  direction per matrix. The direction comparison against lemuralabs's vectors named the fine-tune on the readers
  (1.000 on 228) and separated the projection on the writers (median 0.11).

The round's result for the measure is pairs 2 and 6 together: in both the changed set is the whole language stack
and the recipe table has nothing to say, and in both the saved direction vectors of one earlier measurement named
what the change was (Google's instruction tuning; yuxinlu1's fine-tune) with 1.000 on every tensor the two copies
share and a flat number on the tensors they do not. Pair 3 calibrates the scale: a second run of the same method
by another maker is 0.96, the author's own reproduction is 1.000 with the bytes 0.0001 apart.

## Owed to the metadata tool

Added since: nothing this round. What remains: the earlier-revision template and configuration through a snapshot
older than the pin (round 31's pairs 2 and 4, round 35's pair 5, this round's pair 6 on both `max_position_embeddings`
and the template, where Google's 06-03 revision carries both values); the declared-context line; the float16
`dtype` reading; the 5.16 save form as a named re-save (finding 39); the dropped-declarations rule through
`tokenizer.json`; a maker's-template rule (round 37's pair 7); the loader-moved-token and missing-template lines
of round 38; and from this round, a pretrained-ids line that reads an unset configuration `eos_token_id` with a
generation value of 1 on a Gemma 4 copy as the pretrained checkpoint's token files (pair 2). To the pinner: the
direction check at the names step against every measured family of the base, the pretrained checkpoint's
measurements included, so that chulcher's copy is paired with google/gemma-4-E4B before the download (a re-pin
against it is owed now) and OpenYourMind's parent is named from lemuralabs's vectors; and a re-pin of chulcher's
copy against the pretrained checkpoint. To the recipe table: an arbitrary-rank entry (three of this round's pairs),
a kernel entry with a first-share floor at 0.96 (pair 3) and a weight line on the per-layer entry (pairs 1 and 4).

## Operational

The round ran on Wheat under the image-free kit with the standalone Python: one download, eight compares and the
sweep, every compare finishing with its card and its weights report, the sweep deleting the five originals. The
pull (card 5770) carries the eight measurement folders (card, metadata, weights, direction vectors and the sha256
record of each) and the sweep record; no job log was pulled, so the compares' nodes and seconds are not recorded.
The home judgement ran under transformers 5.22.1. Twenty-six readings were made at home from the hub by byte
range (`tools/hub_range_read.py`): twelve of chulcher's copy against google/gemma-4-E4B-it and the pretrained
google/gemma-4-E4B (the layer 3 query projection, the attention outputs of layers 5, 20, 30 and 41, the down
projections of 20, 30, 35 and 40, the token embedding and two normalisation vectors), three of p-e-w's three
exports against each other and Google's (the layer 26 attention output and down projection, the layer 11
attention output), and seven of Paul691's copy against OpenYourMind's, lemuralabs's and Google's (the layer 20
query, gate, attention output and down projections, the layer 13 query norm, the layer 5 attention output and the
token embedding). The hub's commit histories, file listings and cards were read for the eight copies,
OpenYourMind's parent repository at its first and current card, p-e-w's first export with its `reproduce/` folder
and his REPRODUCED repository, chulcher's three shipped records, the 12B original's templates and configurations
at seven revisions, and the pretrained E4B's token files. Two hundred and forty-three comparisons were made from
the saved direction files, listed in the reading notes.

Weight differences alone cannot certify the absence of hidden behavior.
