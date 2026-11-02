# Census round 41: the last seven direct Gemma 4 copies on Wheat, a hub duplicate that holds the export its parent replaced at 1.000 with the bytes byte-equal to the parent's history, a 12B projection to 6.5 at 0.99 to TrevorJS's directions with every row restored, and a function-calling original's first copy (2026-11-02)

Seven published copies compared with their originals on Wheat from the batch pinned as
`data/batches/round-41-batch-1.json` (pinned 2026-11-02 07:14Z) under the image-free census kit with the
standalone Python: download job 387195, compares 387196 to 387202, sweep 387203, which deleted the six originals
(`87a447ff` of google/gemma-4-12B-it at `5926caa4` for pairs 1 and 6, `c6c096c1` of google/functiongemma-270m-it
at `ead2a1f9` for pair 2, `ed9be084` of google/gemma-4-E4B-it at `292a7e27` for pair 3, `c6f78367` of the E4B at
`d6436b3d` for pair 4, `6273b5b6` of google/gemma-4-E2B-it at `4742fe84` for pair 5 and `bec57494` of
google/gemma-4-31B-it at `439edf56` for pair 7) from `/p/work/sdegan/model-audit/rounds/41/originals/`. The pull
(card 5776) brought home the seven measurement folders and the sweep record and no job log, so the compares'
nodes and seconds are not in this note. The batch note says what the round is: the last of the direct Gemma 4
copies on the unmeasured list, seven from seven makers, and the end of that pool; the pinner refused
thirty-two re-uploads of measured files (huihui-ai's files ten times, TrevorJS's four, coder3101's five,
llmfan46's four, null-space's two, and one each of Himanshuoo8's, tvall43's, Sabomako's, lemuralabs's,
Kooten's, igorls's and Paul691's), passed three gated repositories (Faulknerv1981's E4B, tyr3xy's E2B,
theailearner's HiveCoderPlus), and left aside CyborgPaloma's E4B heretic, whose declared base
google/gemma-4-E4B-base does not exist on the hub (the repository is itself named for it). It records that
jcxu97's 31B "was duplicated from wangzhang's and its weight files differ"; the hub's history explains the
difference, the duplicate holding the export of 04-10 that wangzhang replaced with trial 40 on 04-29 and the
census measured at its head. Six of the seven are first measurements of distinct copies and the seventh,
jcxu97's, is a hub duplicate of that unmeasured earlier export (one commit titled "Duplicate from", the parent
repository present and its head another file), the ninth hub duplicate in the census and the first whose parent
export survives only in its repository's history. One original is new, google/functiongemma-270m-it, a
270-million-parameter Gemma 3 text model tuned for function calling, the smallest checkpoint measured; the
other five Google revisions were pinned in earlier rounds. The population comes to one hundred and ninety-eight
measurements of one hundred and ninety-one distinct copies on thirty-four originals: the round 40 header's
numbers plus seven measurements, seven copies and one original. Two pairs are the arbitrary-rank branch
(RumiaChannel's third 12B search and NullpoLab's first E4B export), three are kernel passes (Roman0's per-layer
Heretic 1.1.0 pass on functiongemma, MoonRide's single-direction 1.2.0 pass on the E2B, ImanolSuarez's 1.3.0
pass on the E4B with a reproduction record), one is the maker's custom projection with exact row restoration
(Sabomako's 12B, finding 65's method on a second base) and one is Abliterix on five components a layer
(jcxu97's duplicate). The seven measurements were re-scored at home with the recipe table as committed and the
saved direction vectors, and no flag count moved. Every metadata report was judged again at home under
transformers 5.22.1 with the originals' later commits; the home judgement moved fourteen fields on six pairs
(five on pair 1, two on pair 3, one each on pairs 4, 5 and 7, four on pair 6; pairs 1, 3, 4, 5, 6 and 7 turn
to consistent with re-save noted) and none on pair 2, which stays unexplained on seven token fields. Each pair
has a card (the tool's Stage 1 text after the home judgement, with the Stage 2 line) and a reading note in
`docs/cards/`; the measurements are in `results/weights/` and `results/meta/`, and the direction vectors stay
in the pull copy (`/opt/ai/hpc-packages/pulls/model-audit/wheat41/measurements/pair-N/`).

| Pair | Copy | Original | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | RumiaChannel/gemma-4-12B-it-uncensored-ara-Refusals4 | google/gemma-4-12B-it | violations, 52 flags (26 first shares, 26 within-layer cosines) | the arbitrary-rank branch on both writers of layers 24 to 36 (26 of 677), the card's window to the layer; 21 edits on the input side at weights 0.47 to 1.71 with rows 0.0049 to 0.0079, the band, and five down projections left as residues; exactly 0 outside; the directions at 0.96 and 0.94 to the maker's Refusals2 and Refusals9 of the same morning and 0.55 to the English-prompted 12B edits |
| 2 | Roman0/functiongemma-270m-it-heretic | google/functiongemma-270m-it | clean match of `directional-per-layer-selected`, 0 flags | the card exactly, on a new original: one direction per layer on the output side of the down projections of layers 8 to 17 and the attention outputs of 9 to 17 (19 of 236), both windows ending at the stack's last layer, the kernels to the layer and to the second decimal (1.40 to 1.45 under 1.40 and 1.46; 0.85 to 1.29 under 0.85 and 1.33); rows 0.019 to 0.489; exactly 0 outside; two tokens marked special that the original does not mark, `<start_function_response>` among them |
| 3 | NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals3 | google/gemma-4-E4B-it | violations, 52 flags (26 first shares, 26 within-layer cosines) | the arbitrary-rank branch on both writers of layers 19 to 31 (26 of 2,130), every matrix edited on the input side at weights 0.73 to 1.43, the window ending six layers short of the card's 37; rows 0.0011 to 0.0184, through and over the band; exactly 0 outside; the directions at 0.98 to the maker's Refusals8 and 0.93 to 0.96 to its three other exports, the maker's first |
| 4 | ImanolSuarez/gemma-4-E4B-it-heretic-seguridadDeLaInformacion | google/gemma-4-E4B-it | violations against `single-projection-selected`, 10 flags (6 first shares at 0.978 to 0.989, 3 direction cosines, 1 cross-kind) | one direction on the output side of the down projections of layers 17 to 35 and the attention outputs of 18 to 35 (37 of 2,076), the kernels' lower ends to the layer and both writers of 36 to 41 untouched where the kernels reach the stack's end; the kept fractions under the printed maxima and without the kernel's order under a full row normalisation at rank 3, the relative change rising 0.010 to 0.029; rows 0.0039 to 0.0112; exactly 0 outside; the direction at 0.75 to p-e-w's and 0.69 to 0.71 to sh0ck0r's and BinxNet's on a run whose record names the tool's English prompt sets under a Spanish name |
| 5 | MoonRide/gemma-4-E2B-it-heretic | google/gemma-4-E2B-it | clean match of `single-projection-selected`, 0 flags | the card exactly: one direction on the output side of the down projections of layers 11 to 34 and the attention outputs of 15 to 34 (44 of 2,011), the kernels to the layer and to the second decimal (1.17 to 1.38 under 1.38; 1.14 to 1.21 under 1.21 and 1.14); rows 0.0055 to 0.034; exactly 0 outside; the direction at 0.98 to tvall43's v0, 0.97 to huihui-ai's family and 0.96 to DuoNeural's, and 0.06 to the maker's own arbitrary-rank export of six hours later |
| 6 | Sabomako/gemma-4-12B-it-heretic | google/gemma-4-12B-it | violations, 29 flags (first shares 0.741 to 0.989) | one direction per layer on the output side of 31 matrices in three bands (both writers of layers 18 to 23 and 34 to 39, the down projections of 24 to 30; 31 of 677), at 6.29, 6.52 and 6.16 on the down projections of 21 to 23 and 0.06 to 1.08 elsewhere, every row restored within 0.0003, under a 674-byte card naming "Heretic v1.3.0 with custom ORBA"; exactly 0 outside; the directions at 0.986 to TrevorJS's 12B edit on all 31 names with the bytes 0.10 apart at layer 21 |
| 7 | jcxu97/gemma-4-31B-it-abliterated | google/gemma-4-31B-it | clean match of `directional-per-layer-selected`, 0 flags | a hub duplicate of wangzhang's first export, the one his repository's head replaced: one direction per layer shared by the attention outputs of layers 29 to 59, the down projections of 29 to 58, the keys of 27 to 53, the queries of 31 to 47 and the values of 42 to 58 (120 of 1,188), the writers on the output side to 5.33 and the readers on the input side to 5.54, every row restored within 0.0011, the card's five components; exactly 0 outside; the directions at 1.000 to the measured trial 40 on all 73 shared names with the kept fractions different on every one, the bytes byte-equal to the parent's 04-11 revision and 0.003 to 0.074 from its head |

Nothing moved outside the matrices the maker's method reaches in any of the seven pairs: the largest relative
change outside the changed set is exactly 0 on all seven. Six of the seven copies are what their cards say
(pairs 1, 2, 3, 4, 5 and 6), two of them with a qualification the weights supply: NullpoLab's Refusals3 ends six
layers before its card's `end_layer_index`, as three of the maker's four other exports did (finding 86's
selection), and ImanolSuarez's edits stop at layer 35 where the card's kernels reach 41, twelve matrices the
kernels cover and the weights do not touch, under a row normalisation that leaves the kept fractions without the
kernel's shape. The seventh, jcxu97's, is a hub duplicate measured as the export it holds, which its card
describes exactly; the batch note had separated its files from the parent's head by checksum before any byte was
read, and the hub's file listings placed them in the parent's history by object id. The round's result for the
method is pair 7 against pair 6. jcxu97's duplicate stands at 1.000 to the census's measurement of wangzhang's
head on all 73 shared matrices, and the two are two trials of one search: the kept fractions differ on every
shared matrix (the layer 29 attention output at a weight of 1.38 here and 3.48 there), the duplicate edits 30
down projections the head leaves alone, and by byte range the duplicate is byte-equal to the parent's `90a225e3`
of 04-11 on four tensors and 0.0032 to 0.0740 from the head's on the three edited ones. Sabomako's 12B stands at
0.986 to TrevorJS's 12B edit on all 31 shared matrices, in the 0.98 to 0.99 at which the one-direction family's
independent runs stand (findings 85 and 103), with the weights the maker's own (6.3 to 6.5 on three down
projections where TrevorJS's are 0.85 to 0.98) and the bytes further from his than from Google's on two of three
tensors read. Findings 85, 95, 102 and 105 read 1.000 as one tool on one base and one prompt set, with the bytes
deciding between a copy and a run; this round's 1.000 is a copy of a revision the parent's head no longer shows,
and the bytes found it in the history.

The weights read off the weights. The three kernel passes read on the output side. Roman0's per-layer pass of
functiongemma (pair 2) rises from 1.41 at layer 8 to 1.45 at 12 and 13 and falls to 1.40 at 17 on the down
projections and from 0.93 at 9 to 1.29 at 13 and 0.85 at 17 on the attention outputs, the card's two kernels
within 0.04 at the layers the positions name; the eighteen-layer stack ends where the kernels do. MoonRide's
single direction on the E2B (pair 5) rises from 1.17 at layer 11 to 1.38 at 26 and falls to 1.27 at 34 on the
down projections and from 1.14 to 1.21 at 25 and back to 1.15 on the attention outputs, the card's maxima to the
second decimal at the layers it prints, the far end of the down kernel beyond the stack. ImanolSuarez's (pair 4)
reads one direction at kept fractions that do not trace a kernel (0.65 to 1.02 on the down projections, 0.16 to
0.91 on the attention outputs with no order) under a record that names a full row normalisation at rank 3 and an
orthogonalised direction, while the relative change rises along the window from 0.010 to 0.029 as a kernel
would. The two arbitrary-rank edits (pairs 1 and 3) read on the input side at 0.47 to 1.71 and 0.73 to 1.43, the
two writers of a layer unrelated, Refusals4 leaving five residues and Refusals3 none. Sabomako's projection
(pair 6) reads one direction per layer at 6.2 to 6.5 on three down projections and 0.06 to 1.08 on the other 28
matrices, the maker's 31B signature (four layers to 5.4, finding 65) on a wider window. jcxu97's duplicate (pair
7) reads one direction per layer on all five of the card's components, the writers on the output side (1.38 to
1.95 and 1.86 to 5.33) and the readers on the input side (3.6 to 4.3 on the keys, 3.9 to 5.54 on the queries,
1.41 to 1.72 on the values).

Preservation claims. Two cards claim a norm and both read in the rows: jcxu97's "norm-preserving row magnitude
restoration" at 0.00007 to 0.00108 on all 120 matrices, and Sabomako's "custom ORBA", which names no norm in
words and restores every row within 0.0003, as the maker's 31B did. Roman0's and MoonRide's cards claim nothing
and the rows are unrestored (to 0.489 and 0.034). ImanolSuarez's record names `row_normalization` "full" and
the rows read 0.0039 to 0.0112, rising with the layer, a second reading of the setting after Mitchins's (finding
92). RumiaChannel's Refusals4 carries the branch's band, 0.0049 to 0.0079 on every edit,
and NullpoLab's Refusals3 reads 0.0011 to 0.0184, through and over it, as the maker's four other exports read.

Fingerprints. Pair 7's two shards (`613f3f35`, `566addbf`) are wangzhang's at `2a9b26cd` and `90a225e3` by the
hub's object ids and are not the head's. Pair 4's fourth shard (`8080cb1a`) is byte-equal to the E4B layout
shard nine measured exports carry (finding 71), and its first three match nothing. Pairs 1, 2, 3, 5 and 6 share
no checksum with any measured file. By byte range jcxu97's layer 41 attention output, query projection and
down projection and layer 10 query projection are byte-equal to wangzhang's `90a225e3`, and 0.0295, 0.0032 and
0.0740 from the head's trial 40, whose layer 41 down projection is byte-equal to Google's; Sabomako's layer 21
down projection is 0.1208 from Google's and 0.1025 from TrevorJS's, its layer 21 attention output 0.0064 from
Google's and 0.0119 from TrevorJS's; Refusals4's layer 30 attention output is 0.0075 and 0.0094 from Refusals2's
and Refusals9's, which stand 0.0046 apart; Refusals3's layer 29 attention output is 0.0175 from Refusals8's;
MoonRide's layer 21 attention output is 0.0105 from huihui-ai's and 0.0921 from tvall43's v0; ImanolSuarez's
layer 26 attention output is 0.0165 from p-e-w's and 0.0191 from Google's; Roman0's layer 12 down projection is
0.0700 from Google's with one value in ten thousand at exactly zero where Google's has none, the projection's
smallest results under the bfloat16 floor, and its layer 3 down projection, outside the windows, byte-equal.

Directions. The round placed its edits against the saved vectors of earlier measurements without a download
(finding 66's check): one hundred and eighty-one comparisons against the saved vectors of measurements of the
12B (twenty-eight for each of two pairs, this round's other 12B among them), the E4B (thirty-nine for each of
two pairs), the E2B (twenty-three) and the 31B (twenty-four); functiongemma has no other measurement, and pair
2's nineteen vectors wait in the pull copy for the next copy of that checkpoint. jcxu97's duplicate stands at
1.000 on both sides to wangzhang's measured head on all 73 shared names (29 attention outputs, 13 keys, 17
queries, 14 values), at 0.84 to 0.89 to the per-layer 31B passes of finding 105 and to Sabomako's 31B, and at
0.52 or less to the rest, 0.013 to cosmicoptima's. Sabomako's 12B stands at 0.986 and 0.989 to TrevorJS's 12B
edit and its four re-uploads on all 31 names (minimum 0.952), at 0.61 to Carlosian's and 0.60 to Paul691's
duplicate, and at 0.27 or less to the kernel passes and the arbitrary-rank searches. ImanolSuarez's stands at
0.755 to p-e-w's two exports on all 37 names, 0.71 to sh0ck0r's and 0.69 to BinxNet's, between the 0.96 to 0.98
of independent runs of the tool's earlier versions and the 0.4 to 0.6 of a changed prompt set, on the prompt
sets p-e-w's run used; its record names the tool's version, an orthogonalised direction and a full row
normalisation as what differs. MoonRide's E2B pass stands at 0.982 to tvall43's v0 (16 names), 0.970 to
huihui-ai's family (44) and 0.960 to DuoNeural's (44), the E2B's single direction from a fourth maker (findings
96 and 110), and at 0.063 and 0.047 to the maker's own two arbitrary-rank searches of the same evening and the
next day. Refusals4 stands at 0.957 and 0.937 on the left to the maker's Refusals2 and Refusals9 (26 names,
0.98 and 0.96 on the attention outputs, the residues on either side near zero) and at 0.55 and 0.54 to
llmfan46's and coder3101's 12B edits, finding 99's distance. Refusals3 stands at 0.982 to the maker's Refusals8,
0.955 to Refusals6-attn, 0.949 to Refusals8-attn and 0.929 to Refusals5, at 0.87 to coder3101's and 0.86 to
llmfan46's, finding 82's family, and at 0.093 to ImanolSuarez's of this round.

## The token side

The cluster's cards read "unexplained differences" on all seven. The home judgement under transformers 5.22.1
with the originals' later commits moved fourteen fields on six cards: the templates of pairs 1 and 3, pair 1's
18,683 bytes byte-equal to Google's 12B revision `711c1368` of 07-15 ("fix: chat template"), carried in by the
copy's 07-21 update of the template and the tokenizer configuration six weeks after the weights, and pair 3's
16,804 bytes byte-equal to the E4B's `c53e9d33` of 04-28, carried in by the 04-29 upload as the maker's Refusals8
and Refusals6-attn carried it; `text_config.moe_intermediate_size` on pairs 3, 4, 5 and 7 (absent on one side,
the same default under 5.22.1); and four audio and vision configuration fields on each of the two 12B pairs
(`audio_samples_per_token`, `hidden_size`, `output_proj_dims`, `model_patch_size`, absent on one side and the
same value under 5.22.1). Pairs 1, 3, 4, 5, 6 and 7 turn to consistent with re-save noted, their remaining
differences version strings (5.10.0.dev0 to 5.10.2 and 5.12.1 on the 12B; 5.5.0.dev0 to 5.5.0, 5.9.0, 5.5.0 and
5.5.3). Pair 4's 17,695-byte template and the pin's 17,336 differ in line endings and trailing whitespace alone,
the Windows save its record names. Pair 2 stays unexplained on seven token fields the home tool does not judge:
in `tokenizer_config.json`'s `added_tokens_decoder` and in `tokenizer.json` the copy marks tokens 50
(`<start_function_response>`) and 255999 (`<start_of_image>`) as special where the original marks neither, the
flag that decides whether a decoder skipping special tokens drops them from the text, and the copy ships no
`added_tokens.json` where the original's holds `<end_of_image>` and `<image_soft_token>`; the ids are equal on
both sides (`bos_token_id` 2, `eos_token_id` `[1, 50]`, `pad_token_id` 0, generation `[1, 50, 106]`) and the
version strings are the same 4.57.3. Every Gemma 4 pair carries the instruct checkpoint's token ids
(`eos_token_id` `[1, 106]`, generation `[1, 106, 50]`, `bos_token_id` 2, `pad_token_id` 0), so round 39's
pretrained-checkpoint case does not recur, and pair 4's `base_model` field names the pretrained base over
instruct-model weights, finding 67's inherited header.

## What the scorer learned

The flag counts are the same on the cluster and at home. Their causes, by pair:

- Three clean reads, 0 flags (pairs 2, 5 and 7): the per-layer entry with selection fits one direction per layer
  on an eighteen-layer stack and on five kinds of matrix at once, and the single-projection entry with selection
  fits one direction on 44 matrices; none has a weight line, and 5.54 on a query projection is the largest
  input-side weight the census has read on a restored projection.
- A single direction under the single-projection entry, 10 flags (pair 4): six attention outputs at first shares
  of 0.978 to 0.989 under the 0.99 floor where the change is 0.010 to 0.014, three direction cosines and one
  cross-kind cosine at 0.91 to 0.94; a floor at 0.97 would read the copy as its card, and no rule reads the six
  layers the kernels cover and the weights do not.
- A restored projection under the per-layer entry, 29 flags (pair 6): first shares of 0.741 to 0.989 on the 29
  matrices whose change is under 0.02, where the bfloat16 rounding of the restored rows is a larger share of a
  small change; the two matrices at 0.992 pass. A floor tied to the change would read the copy as its card.
- Arbitrary-rank edits under the per-layer entry, 52 and 52 flags (pairs 1 and 3): a few directions per matrix
  fails the first-share rule on every edit, and the two writers of a layer each with their own direction fail
  the within-layer rule; an arbitrary-rank entry would read both as clean matches with pair 1's residues and
  pair 3's short window called out.

The round's result for the measure is pair 7. The direction check that named parents in rounds 38 and 39 and
read four makers at 1.000 in round 40 returns 1.000 on 73 names between a duplicate and a measured repository,
and the number names the repository and not the file: the parent's head is a later trial of the same search,
with one direction and other weights, and the duplicate holds the earlier one. The byte-range step the round 40
note asked for after any 1.000 is what placed the bytes in the parent's history, and the duplicate rule needs
the parent's commit history beside its file listing (finding 71's lesson from the other side).

## Owed to the metadata tool

Added since: nothing this round. What remains: the earlier-revision template and configuration through a
snapshot older than the pin (round 31's pairs 2 and 4, round 35's pair 5, round 39's pair 6, round 40's pair 5);
the declared-context line; the float16 `dtype` reading; the 5.16 save form as a named re-save (finding 39); the
dropped-declarations rule through `tokenizer.json`; a maker's-template rule (round 37's pair 7); the
loader-moved-token and missing-template lines of round 38; the pretrained-ids line of round 39; and from this
round a special-flag line, which would name a token whose `special` flag the copy changed and what the flag
does (pair 2). To the pinner: the duplicate step should read the parent's commit history and match the
duplicate's object ids against every revision, naming the revision it holds (pair 7). To the recipe table: an
arbitrary-rank entry with a components line (pairs 1 and 3), a kernel-tail rule on the single-projection entry
that names the layers a card's kernels cover and the weights do not (pair 4), a first-share floor tied to the
change on restored projections (pair 6) and a weight line on both entries with selection (pairs 2, 5, 6 and 7).

## Operational

The round ran on Wheat under the image-free census kit with the standalone Python: one download, seven compares
and the sweep, every compare finishing with its card and its weights report, the sweep deleting the six
originals. The pull (card 5776) carries the seven measurement folders (card, metadata, weights, direction
vectors and the sha256 record of each) and the sweep record; no job log was pulled, so the compares' nodes and
seconds are not recorded. The home judgement ran under transformers 5.22.1. Sixty-six readings were made at home
from the hub by byte range (`tools/hub_range_read.py`), eighty-seven comparisons among them: the layer 41
attention output, query projection and down projection and the layer 10 query projection of jcxu97's duplicate
against wangzhang's `90a225e3`, his head and Google's; the layer 21 down projection and attention output, the
layer 30 down projection and the layer 10 query projection of Sabomako's 12B against TrevorJS's and Google's; the
layer 30 attention output and layer 31 down projection of Refusals4 against Refusals2's, Refusals9's and
Google's; the layer 29 attention output and down projection of Refusals3 against Refusals8's, Refusals6-attn's
and Google's; the layer 21 attention output and layer 20 down projection of MoonRide's E2B pass against
huihui-ai's, tvall43's v0 and Google's; the layer 26 attention output and down projection of ImanolSuarez's
against p-e-w's, sh0ck0r's and Google's; and the layer 12 down projection, layer 13 attention output and layer 3
down projection of Roman0's against Google's. The hub's commit histories, file listings and cards were read for
the seven copies, wangzhang's 31B repository at three revisions, RumiaChannel's Refusals2 and Refusals9,
NullpoLab's four other exports, MoonRide's two E2B searches, Sabomako's 31B, CyborgPaloma's E4B repository and
ImanolSuarez's `reproduce/` folder, and the six originals' histories. One hundred and eighty-one comparisons were
made from the saved direction files, listed in the reading notes.

Weight differences alone cannot certify the absence of hidden behavior.
