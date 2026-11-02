# Census round 42: the first eight second-generation edits on Nautilus, each measured against the community parent its card names, a merge at 1.000 to the measured edit its card names as its body, two merge-maker searches at 0.96 to 0.99 to the 26B-A4B family, and two fine-tunes over unmeasured first edits (2026-11-02)

Eight published copies compared with the parents their cards name on Nautilus from the batch pinned as
`data/batches/round-42-batch-1.json` (pinned 2026-11-02 07:41Z) under the CPU census kit: download job 4171128,
compares 4171129 to 4171136, sweep 4171137, which deleted the eight parents (`809a6fce` of
bgg1996/Melinoe-Gemma4-31B-VL at `26acdef2` for pair 1, `7f9127fb` of zerofata/G4-MeroMero-31B at `35611a07` for
pair 2, `802111e7` of aifeifei798/Gemma-4-Queen-31B-it at `58bee46f` for pair 3, `110cf468` of
Vortex5/G4-Moonlight-Dusk-26B-A4B at `fa0ae315` for pair 4, `f5d286ba` of coder3101/gemma-3-27b-it-heretic at
`b9449797` for pair 5, `aadf407c` of Gryphe/Gemma-4-26B-A4B-StyleTune-V2 at `f34ba405` for pair 6, `85d6f845` of
DavidAU/gemma-3-4b-it-heretic-uncensored-abliterated-Extreme at `b2d64d29` for pair 7 and `8254c332` of
Vortex5/Chimera-X-26B-A4B at `44f28aef` for pair 8) from `/p/work1/sdegan/model-audit/rounds/42/originals/`. The
pull (card 5780) brought home the eight measurement folders and the sweep record and no job log, so the compares'
nodes and seconds are not in this note. The batch note says what the round is: the first from the second-generation
pool, Heretic edits applied to community fine-tunes and merges of Gemma 4 and Gemma 3 and to first edits, so each
pair measures the edit against the parent its card names and not against Google. It records that Justbackup's 27B
"was duplicated from DavidAU's and its weight files differ", which the hub's object ids and a byte-range read do
not bear out (below), and what was held or refused on the way: Naphula's Goetia 26B-A4B search, whose merge chain
names a base the lineage cannot place; Vortex5's Starry-Ocean 12B edit, which carries eleven tensor names its
parent lacks; the Mistral family, whose Ministral 3 Instruct and Devstral Small 2 originals are float8 on the hub;
and coder3101's Ministral 3 14B Reasoning edit, whose shard index names eight files the repository never
published. The round changes what a pair reads. Against Google a copy reads the edit and whatever the maker's
parent carried; against the parent its card names it reads the edit alone, and the parent's own distance from
Google is read separately by byte range where the note needs it. The direction check still works, because every
parent in the round descends from a Google checkpoint and the saved vectors of the Google-rooted families are the
edit's and not the parent's; where the parent is itself a first edit (pairs 5 and 7) the comparison is to that
edit's measurement, and neither of the two is measured, so those two pairs read the training over the edit with
no family to place a direction against. One population rule follows and the header applies it: a community parent
counts as neither an original nor a copy, so the originals stay the publisher's thirty-four checkpoints and a parent
enters the copy count only when it is itself measured against its own parent. Seven of the eight are first
measurements of distinct copies and the eighth, Justbackup's, is a hub duplicate of DavidAU's unmeasured 27B
fine-tune (one commit titled "Duplicate from", the twelve shards byte-equal to the parent's at its head and at two
earlier revisions by object id), the tenth hub duplicate in the census. The population comes to two hundred and six
measurements of one hundred and ninety-nine distinct copies on thirty-four originals: the round 41 header's numbers
plus eight measurements and eight copies, none of whose parents was in the population. Four pairs are the
arbitrary-rank branch over a fine-tune or a merge (llmfan46's two 31B edits of other makers' fine-tunes, Vortex5's
two edits of the maker's own merges), one is a kernel pass from the tool's 1.4.0 with a reproduction record over a
31B fine-tune (bgg1996's), one is a three-part merge whose card names a measured first edit as its body
(SubMaroon's), and two are Unsloth fine-tunes over unmeasured first edits (Justbackup's duplicate of DavidAU's 27B,
DavidAU's 4B). The eight measurements were re-scored at home with the recipe table as committed and the saved
direction vectors, and no flag count moved. Every metadata report was judged again at home under transformers
5.22.1 with the parents' later commits; the home judgement moved one field on one pair (pair 1's
`text_config.moe_intermediate_size`, absent on one side and the same default, which turns the pair to consistent
with re-save noted) and none on the other seven. Each pair has a card (the tool's Stage 1 text after the home
judgement, with the Stage 2 line) and a reading note in `docs/cards/`; the measurements are in `results/weights/`
and `results/meta/`, and the direction vectors stay in the pull copy
(`/opt/ai/hpc-packages/pulls/model-audit/nautilus42/measurements/pair-N/`).

| Pair | Copy | Parent | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | bgg1996/Melinoe-Gemma4-31B-VL-heretic | bgg1996/Melinoe-Gemma4-31B-VL | violations against `directional-per-layer-selected`, 2 flags (first shares 0.98996 and 0.98999) | Heretic 1.4.0's per-layer pass over a fine-tune of the 31B: one direction per layer on the output side of the attention outputs of layers 23 to 59 and the down projections of 38 to 48 (48 of 1,188), the card's kernels to the layer at both ends (51.65 less 28.98 and 43.01 less 5.21 give 23 and 38; 43.01 plus 5.21 gives 48; the attention window runs to the stack's last layer); the down kernel's peak to the second decimal (1.21 at 43 under 1.22 at 43.01) and the attention kernel's peak within 0.04 (1.41 at 51 to 53 under 1.45 at 51.65) with its lower end at 0.31 under a printed 0.93; rows 0.0016 to 0.0077 under a record naming a full row normalisation at rank 3; exactly 0 outside; the directions at 0.92 to the per-layer 31B passes of finding 105 and 0.13 to 0.15 to the round's two 31B searches |
| 2 | llmfan46/G4-MeroMero-31B-uncensored-heretic | zerofata/G4-MeroMero-31B | violations, 19 flags (first shares 0.892 to 0.967) | the arbitrary-rank branch on the attention outputs of layers 28 to 48 under a card to 49 (19 of 1,188), layer 42 untouched and layer 46 rewritten by 0.000003; 18 edits on the input side at weights 0.90 to 1.97 and layer 48's component multiplied by 1.34 rather than removed; rows 0.0009 to 0.0245, under and over the band; the directions at 0.94 to coder3101's 31B edit, 0.92 to MoonRide's, 0.89 to the maker's own April edit and 0.887 to the maker's Queen edit of this round; the maker's own 17,344-byte template in place of the parent's |
| 3 | llmfan46/Gemma-4-Queen-31B-it-uncensored-heretic | aifeifei798/Gemma-4-Queen-31B-it | violations, 30 flags (first shares 0.911 to 0.986) | the arbitrary-rank branch on the attention outputs of layers 26 to 55 under a card to 56 (30 of 1,188), every layer inside edited on the input side at weights 1.19 to 3.70 on 28, 0.26 at layer 48 and layer 50's component multiplied by 6.71 (relative change 0.1205, the rows moved 0.197); rows 0.0006 to 0.197; exactly 0 outside; the directions at 0.993 to the maker's own April 31B edit on all 18 shared names, 0.97 to MoonRide's and 0.96 to coder3101's; the same maker's template as pair 2 in place of the parent's release template |
| 4 | Vortex5/G4-Moonlight-Dusk-26B-A4B-heretic | Vortex5/G4-Moonlight-Dusk-26B-A4B | violations, 16 flags (first shares 0.002 to 0.976) | the arbitrary-rank branch under a card from 3 to 22 over the maker's four-model merge: 13 edits of the attention outputs of layers 9 to 21 on the input side at weights 1.31 to 2.96 with rows 0.0064 to 0.0077, the band; the attention outputs of layers 3 to 5 rewritten by 0.0010 to 0.0018 without a direction and those of 6 to 8 under the threshold (0.00099 the largest outside); layer 22 untouched; the directions at 0.985 to SassyDiffusion's 26B-A4B search, 0.955 to llmfan46's, 0.947 to coder3101's and 0.957 to the maker's Chimera-X edit of four days later |
| 5 | Justbackup/Gemma-3-27b-it-Uncensored-HERETIC-Gemini-Deep-Reasoning | coder3101/gemma-3-27b-it-heretic | violations against `single-projection`, 543 flags (124 first shares, 124 direction cosines, 294 unexpected changes, 1 cross-kind) | a hub duplicate of DavidAU's 27B fine-tune, measured against the unmeasured first edit both cards name: training on 418 of 1,247 tensors, the down, gate, up, query and attention output projections of all 62 layers, the values of 60 and the keys of 48, by 0.10 to 0.84 percent with layer 0's down projection at 4.07 percent, first shares 0.24 to 0.97, no direction; the 438 vision and embedding tensors untouched; 0.000995 the largest outside; the twelve shards byte-equal to DavidAU's at three revisions; by byte range the layer 30 attention output 0.0044 from coder3101's and 0.0223 from Google's |
| 6 | SubMaroon/Gemma-4-26B-A4B-StyleTune-QK-Heretic | Gryphe/Gemma-4-26B-A4B-StyleTune-V2 | violations against `single-projection-selected`, 100 flags (59 unexpected changes, 20 first shares, 20 direction cosines, 1 cross-kind) | the card's three edits read one by one (79 of 1,014): coder3101's arbitrary-rank body on the attention outputs of layers 10 to 29 on the input side at weights 0.76 to 1.49 with rows 0.0061 to 0.0080, at 1.000 to coder3101's directions on all 20 names and byte-equal to his at layer 20; the query and key interpolation on 59 matrices rewritten by 0.0010 to 0.0048 without a direction, the bytes 0.0003 to 0.0004 from Pantheon-Reasoning V2's and 0.0033 to 0.0034 from the base's; the `lm_head` equal to the parent's, which the card names as its source; 0.000994 the largest outside (layer 5's key) |
| 7 | DavidAU/gemma-3-4b-it-vl-Heretic-4-Horsemen-Uncensored | DavidAU/gemma-3-4b-it-heretic-uncensored-abliterated-Extreme | violations against `single-projection`, 307 flags (68 first shares, 68 direction cosines, 170 unexpected changes, 1 cross-kind) | an Unsloth fine-tune over the maker's own unmeasured first edit of the 4B: training on 238 of 883 tensors, all seven linear maps of all 34 layers, by 0.15 to 2.05 percent, first shares 0.23 to 0.98, no direction; the vision tower and the embeddings exactly 0; exactly 0 outside; by byte range the layer 20 attention output 0.0132 from the Extreme's and 0.0403 from Google's; no other measurement on the 4B to place a direction against |
| 8 | Vortex5/Chimera-X-26B-A4B-heretic | Vortex5/Chimera-X-26B-A4B | violations, 17 flags (first shares 0.704 to 0.965) | the arbitrary-rank branch on the attention outputs of layers 6 to 22 under a card to 23 (17 of 1,014) over the maker's multi-stage merge, which contains the Moonlight-Dusk merge of pair 4: every layer inside edited on the input side at weights 1.10 to 2.03 with rows 0.0058 to 0.0078, the band; exactly 0 outside; the directions at 0.991 to llmfan46's 26B-A4B search, 0.984 to coder3101's and to SubMaroon's body, 0.965 to SassyDiffusion's and 0.957 to the maker's Moonlight-Dusk edit |

Nothing moved outside the matrices the maker's method or training reaches in any of the eight pairs: the largest
relative change outside the changed set is exactly 0 on pairs 1, 3, 7 and 8, 0.000003 on pair 2 (one attention
output inside the window), and 0.00099 on pairs 4, 5 and 6 (three attention outputs inside the window on pair 4,
one key on pair 6, and the normalisation vectors a fine-tune leaves under the threshold on pair 5). All eight
copies are what their cards say, each read against the parent its card names and not against Google: the four
arbitrary-rank edits read their windows with the branch's selection inside them (pairs 2, 3, 4 and 8), the kernel
pass reads its kernels to the layer at both ends (pair 1), the merge reads its three edits one by one (pair 6),
and the two fine-tunes read training on every layer under cards that print the parent edit's table (pairs 5 and
7). The round's result for the method is pair 6. SubMaroon's card names coder3101's measured 26B-A4B edit as the
body, Gryphe's StyleTune-V2 as the source of its `lm_head` and Pantheon-Reasoning V2 as the donor of an
interpolation on the queries and keys, and says the body was verified by tensor comparison; measured against
StyleTune-V2, the attention outputs stand at 1.000 to coder3101's directions on all 20 shared names with the bytes
byte-equal at layer 20, the queries and keys sit nine tenths of the way to the donor's by byte range, and the
`lm_head` is the parent's. Findings 85, 95, 102 and 105 read 1.000 as one tool on one base and one prompt set, with
the bytes deciding between a copy and a run; this round's 1.000 is a copy the card declares, and the bytes agree.
The round's result for the branch is pairs 2, 3, 4 and 8. Four arbitrary-rank searches run over fine-tunes and
merges stand where the first-generation searches on the same checkpoints stand: Vortex5's two merges at 0.95 to
0.99 to the 26B-A4B family (SassyDiffusion's, llmfan46's, coder3101's) and 0.957 to each other, llmfan46's Queen
edit at 0.993 to the maker's own April 31B edit and its MeroMero edit at 0.94 to coder3101's, the two at 0.887 to
each other, so a parent that is a fine-tune or a merge of a Google checkpoint does not move the direction the
search finds, and the windows and the rows read as the branch's.

The weights read off the weights. The kernel pass reads on the output side. bgg1996's 1.4.0 pass (pair 1) rises
from 0.31 at layer 23 to 1.41 at layers 51 to 53 and falls to 1.19 at 59 on the attention outputs, with scatter
along the rise (0.18 at 28, 0.82 at 40, 0.98 at 47, 0.60 at 52), and from 1.03 at 38 to 1.21 at 43 and back to
1.10 at 48 on the down projections, the down kernel's shape and peak and the attention kernel's peak under a
record that names an orthogonalised direction and a full row normalisation at rank 3, the settings under which
ImanolSuarez's 1.3.0 pass read no kernel in its kept fractions (finding 114). The four arbitrary-rank edits read on
the input side: llmfan46's two at 0.90 to 1.97 (MeroMero) and 1.19 to 3.70 (Queen) with one layer in each
amplified rather than removed (layer 48's component multiplied by 1.34 on MeroMero, layer 50's by 6.71 on Queen,
the largest input-side reading in the census), Vortex5's two at 1.31 to 2.96 (Moonlight-Dusk) and 1.10 to 2.03
(Chimera-X), the writers of a layer unrelated where both are edited and the down projections untouched on all
four. SubMaroon's body (pair 6) reads coder3101's input-side weights of 0.76 to 1.49 on the attention outputs of
layers 10 to 29 and its queries and keys read a change without a direction. The two fine-tunes (pairs 5 and 7)
read training: first shares 0.24 to 0.97 and 0.23 to 0.98, both kept fractions near 1 on every matrix, every
linear map of every layer touched and the vision towers not.

Preservation claims. No card in the round claims a norm. bgg1996's record names `row_normalization` "full" at a
LoRA rank of 3 and the rows read 0.0016 to 0.0077 on all 48 matrices, the third reading of the setting after
Mitchins's and ImanolSuarez's (findings 92 and 114). The arbitrary-rank edits carry the branch's band on Vortex5's
two (0.0064 to 0.0077 and 0.0058 to 0.0078) and on coder3101's body under SubMaroon's merge (0.0061 to 0.0080),
and run through and over it on llmfan46's two (0.0009 to 0.0245 and 0.0006 to 0.197, the layer 50 row under the
6.71). The fine-tunes move the rows as training does, 0.00006 to 0.0467 and 0.0003 to 0.1015.

Fingerprints. Pair 1's first five shards (`39cd04b3`, `d4c37918`, `3488cce8`, `bb0e0090`, `16ee2995`) are
byte-equal to its parent's five, the layers below 23 the kernels do not reach, and its other eight match nothing
measured. Pair 5's twelve shards are DavidAU's at the parent's head and at `9e0a6b4d` and `75c7c4fd` by the hub's
object ids, and coder3101's first shard is byte-equal to Google's 27B. Pair 6's three shards, the third its
`lm_head` alone, match no measured file, and pairs 2, 3, 4, 7 and 8 share no checksum with any measured file. By
byte range bgg1996's layer 44 attention output is 0.0181 from its parent's, 0.0201 from Google's, 0.0130 from
Vampelium's and 0.0133 from germlag's (the parent 0.0087 from Google's; Vampelium's and germlag's 0.0068 apart),
its layer 44 down projection 0.0168 from the parent's and 0.0183 from Google's, and its layer 10 query projection
byte-equal to the parent's and 0.0094 from Google's, the fine-tune's own change; llmfan46's MeroMero edit at layer
40 is 0.0266 from the parent's, 0.0268 from Google's, 0.0217 from coder3101's and 0.0237 from the maker's own 31B
edit (the parent 0.0035 from Google's), at layer 48 0.0487 from the parent's and at layer 46 equal to the parent's
to four decimals with the bytes not equal; llmfan46's Queen edit at layer 50 is 0.1195 from the parent's, which
is 0.0032 from Google's, and 0.1195 from the maker's April edit, which leaves layer 50 byte-equal to Google's, and
at layer 45 0.0665 from the parent's and 0.0187 from the maker's April edit; Vortex5's Moonlight-Dusk edit at layer
16 is 0.0516 from the parent's, 0.0572 from Google's, 0.0367 from SassyDiffusion's and 0.0402 from llmfan46's (the
merge 0.0246 from Google's; SassyDiffusion's and llmfan46's 0.0082 apart), and its layer 4 attention output
0.0011 from the parent's, the trace; Vortex5's Chimera-X edit at layer 10 is 0.0367 from the parent's, 0.0413 from
Google's, 0.0276 from llmfan46's and 0.0273 from the maker's Moonlight-Dusk edit (the two merges 0.0135 apart, the
Chimera-X merge 0.0189 from Google's); SubMaroon's layer 20 attention output is byte-equal to coder3101's and
0.0377 from StyleTune-V2's, Google's and Pantheon V2's, its layer 20 queries and keys 0.0034 and 0.0033 from
StyleTune-V2's and 0.0004 and 0.0003 from Pantheon V2's (the donor 0.0036 and 0.0035 from the base), its layer 5
keys 0.0010 from the base's and 0.0003 from the donor's (0.0011 apart), its layer 20 down projection byte-equal to
StyleTune-V2's, coder3101's and Google's, and StyleTune-V2's layer 20 byte-equal to Google's on all four tensors
read; Justbackup's layer 30 attention output and down projection are byte-equal to DavidAU's, 0.0044 and 0.0065
from coder3101's and 0.0223 and 0.0209 from Google's (coder3101's 0.0218 and 0.0198 from Google's); DavidAU's 4B
fine-tune at layer 20 is 0.0132 and 0.0111 from the Extreme's on the attention output and the down projection,
0.0403 and 0.0286 from Google's (the Extreme's 0.0385 and 0.0273 from Google's). At the size of the query and key
changes on pair 6 a bfloat16 step is 0.4 percent of a value, so the alphas the card prints (0.85 on the sliding
layers, 0.65 on the global ones) cannot be read from the bytes, which place the merged tensors nine tenths of the
way to the donor's on both kinds of layer.

Directions. The round placed its edits against the saved vectors of earlier measurements without a download
(finding 66's check), the Google-rooted families standing in for the parents: one hundred and seventy-eight
comparisons against the saved vectors of measurements of the 31B (thirty for each of three pairs), the 26B-A4B
(twenty-nine for each of three pairs) and the 27B (one), and six among the round's own pairs; the 4B has no other
measurement, and pair 7's vectors wait in the pull copy. SubMaroon's attention outputs stand at 1.000 on both
sides to coder3101's 26B-A4B edit on all 20 shared names (minimum 1.000), at 0.992 to llmfan46's, 0.978 to
SassyDiffusion's, 0.95 to the two QAT searches, 0.984 to Chimera-X's edit and 0.947 to Moonlight-Dusk's of this
round, and at 0.21 or less to the kernel passes and projections of the 26B-A4B. Vortex5's Chimera-X edit stands at
0.991 to llmfan46's on all 17 names (minimum 0.910), 0.984 to coder3101's, 0.965 to SassyDiffusion's, 0.96 to the
two QAT searches and 0.957 to the maker's Moonlight-Dusk edit; Moonlight-Dusk's stands at 0.985 to
SassyDiffusion's on all 13 names, 0.955 to llmfan46's and 0.947 to coder3101's, both at 0.32 or less to every
kernel pass and projection on the base. llmfan46's Queen edit stands at 0.993 to the maker's own April 31B edit on
all 18 shared names, 0.968 to MoonRide's search, 0.964 to coder3101's, 0.953 to MoonRide's custom-prompt search,
0.93 and 0.92 to the maker's and coder3101's QAT searches, 0.84 to wnfldchen's merged search, 0.56 to Jim-darby's
Japanese-weighted search (finding 108's distance) and 0.20 or less to every 31B kernel pass and projection; the
maker's MeroMero edit stands at 0.939 to coder3101's on all 19 names, 0.916 to MoonRide's, 0.899 and 0.891 to the
two QAT searches, 0.890 to the maker's own April edit, 0.859 to MoonRide's custom-prompt search, 0.51 to
Jim-darby's and 0.15 or less to the passes and projections, and at 0.887 to the Queen edit (minimum 0.625 on 19
names, 0.953 on the right). bgg1996's kernel pass stands at 0.920 to Vampelium's on all 36 shared names, 0.919 to
callmegrr's, germlag's and 3MPER0RR's, 0.888 to ressl's, 0.874 to TrevorJS's, 0.84 to Sabomako's 31B on its 4
names, 0.81 to jcxu97's duplicate and nguyenthilaitrieulong's, 0.79 to wangzhang's head, 0.49 to null-space's, 0.40
to sh0ck0r's, 0.37 to DuoNeural's, 0.25 to 0.26 to huihui-ai's two and their re-uploads, and 0.13 to 0.15 to the
round's two 31B searches, 0.009 to cosmicoptima's. Justbackup's training stands at 0.071 to mlabonne's 27B
projection on 124 names, a fine-tune's change against an edit's direction, and DavidAU's 4B has nothing to stand
against.

## The token side

The cluster's cards read "unexplained differences" on six pairs and "consistent with re-save noted" on pairs 5 and
7. The home judgement under transformers 5.22.1 with the parents' later commits moved one field, pair 1's
`text_config.moe_intermediate_size` (absent on one side, the same default), which turns pair 1 to consistent with
re-save noted beside its version strings (5.5.0.dev0 to 5.13.1 in the configuration and the generation file);
pairs 5 and 7 stay as the cluster read them (4.57.3 to 4.57.6 on the 27B; 5.0.0.dev0 to 4.57.6 and three rope
fields absent on one side on the 4B). Pairs 2, 3, 4, 6 and 8 stay unexplained, each on what the parent carried.
Pairs 2 and 3 differ from their parents in the template alone: the two copies carry one 17,344-byte template, the
one the maker's own 31B repository has carried since its 05-05 upload, in place of zerofata's 16,934-byte template
(Google's 31B revision `145dc250` of 04-28, carried into the parent on 05-01) and aifeifei798's 12,045-byte
template (Google's release revision `419b2efe` of 04-02); the Queen copy took it by a delete and re-upload on 05-04
and 05-05, three weeks after its weights, and the MeroMero copy on the evening of its upload. A maker's template
over three repositories is the maker's-template case the round 37 note asked the tool for a line on, and the home
tool has none yet. Pair 6 differs on seven fields the parent's Unsloth save set: StyleTune-V2 carries
`eos_token_id` 106 alone, `pad_token_id` 0 and `unsloth_fixed` true with its template in `tokenizer_config.json`,
and the copy carries `eos_token_id` `[1, 106]`, no `pad_token_id`, no `unsloth_fixed`, a 18,683-byte
`chat_template.jinja` byte-equal to Google's 26B-A4B revision `35b4173c` of 07-15 in place of the parent's
16,448-byte one (Google's `1db3cff1` of 04-10), and a version string older than the parent's (5.5.0.dev0 against
5.10.2), the token files of coder3101's body rather than of the parent. Pairs 4 and 8 differ on one field each: the
parents, Unsloth saves without a `generation_config.json`, give the home tool nothing to compare, and the copies
carry one written from the configuration (`_from_model_config`, `eos_token_id` 106 on pair 4 from a parent whose
configuration names 106 alone, `[1, 106]` on pair 8), with the version strings 5.12.1 to 5.13.1 and 5.14.1. Every
Gemma 4 pair carries the instruct checkpoint's ids (`eos_token_id` `[1, 106]` or 106 through an Unsloth parent,
generation `[1, 106, 50]` or the parent's, `bos_token_id` 2), so round 39's pretrained-checkpoint case does not
recur, and the two Gemma 3 pairs carry `[1, 106]` on both sides. Pairs 1, 5 and 7 differ from their parents in
nothing but version strings and defaults, the fine-tunes and the kernel pass having re-saved the parent's token
files unchanged.

## What the scorer learned

The flag counts are the same on the cluster and at home. Their causes, by pair:

- A kernel pass under the per-layer entry, 2 flags (pair 1): two attention outputs at first shares of 0.98996 and
  0.98999 under the 0.99 floor, the restored rows' rounding on changes of 0.015; the other 46 pass. A floor at 0.98
  would read the copy as its card, with the kernel's lower end at 0.31 under a printed 0.93 still unread by any
  rule.
- Arbitrary-rank edits under the per-layer entry, 19, 30, 16 and 17 flags (pairs 2, 3, 4 and 8): a few directions
  per matrix fails the first-share rule on every edit, and pair 4's three traces fail it at 0.002 to 0.021; an
  arbitrary-rank entry would read all four as clean matches with pair 4's traces and pair 2's absent layer called
  out, and the amplified layers of pairs 2 and 3 need a weight line that allows a kept fraction above 1.
- A merge under the single-projection entry with selection, 100 flags (pair 6): the 59 queries and keys as
  unexpected changes, the 20 attention outputs at first shares of 0.659 to 0.959 and direction cosines under the
  rules; no entry reads a component as another measured copy's edit, which the saved vectors did at 1.000 in one
  comparison.
- Two fine-tunes under the single-projection entry, 543 and 307 flags (pairs 5 and 7): the gate, up, query, key and
  value projections as unexpected changes and the writers failing the first-share and cosine rules on every layer;
  a training entry (every linear map, first shares under 0.98, both kept fractions near 1) would read both as what
  their cards say.

The round's result for the measure is pair 6 against pairs 5 and 7. Against a community parent the direction
check keeps its meaning where the parent is a fine-tune or a merge of a Google checkpoint, because the saved
vectors are the edit's, and the merge's body read at 1.000 to the measured edit its card names; where the parent
is an unmeasured first edit, the copy reads its training and nothing else, and the first edit under it stays
unread until that parent is measured against Google, which the batch pinner should queue (coder3101's 27B,
DavidAU's 4B Extreme). The byte-range step the round 40 note asked for after any 1.000 is what read the merge's
queries and keys as nine tenths of the way to the donor's and the parent's layers as Google's.

## Owed to the metadata tool

Added since: nothing this round. What remains: the earlier-revision template and configuration through a
snapshot older than the pin (round 31's pairs 2 and 4, round 35's pair 5, round 39's pair 6, round 40's pair 5);
the declared-context line; the float16 `dtype` reading; the 5.16 save form as a named re-save (finding 39); the
dropped-declarations rule through `tokenizer.json`; a maker's-template rule (round 37's pair 7, now pairs 2 and 3
of this round); the loader-moved-token and missing-template lines of round 38; the pretrained-ids line of round
39; the special-flag line of round 41; and from this round an Unsloth-parent line, which would name the fields an
Unsloth save sets (`eos_token_id` as one id, `pad_token_id` 0, `unsloth_fixed`, the template in
`tokenizer_config.json`, no generation file) so that a copy restoring Google's form reads as a re-save and not as
unexplained (pairs 4, 6 and 8). To the pinner: a second-generation pair whose parent is an unmeasured first edit
should queue that parent against Google in the same batch (pairs 5 and 7), and the duplicate step should compare
the duplicate's object ids against every revision of the parent before recording that the files differ (pair 5).
To the recipe table: an arbitrary-rank entry with a components line and a weight line allowing a kept fraction
above 1 (pairs 2, 3, 4 and 8), a training entry (pairs 5 and 7), a merge entry that reads each component against
the saved vectors of measured copies (pair 6), and a first-share floor tied to the change on restored projections
(pair 1).

## Operational

The round ran on Nautilus under the CPU census kit: one download, eight compares and the sweep, every compare
finishing with its card and its weights report, the sweep deleting the eight parents. The pull (card 5780) carries
the eight measurement folders (card, metadata, weights, direction vectors and the sha256 record of each) and the
sweep record; no job log was pulled, so the compares' nodes and seconds are not recorded. The home judgement ran
under transformers 5.22.1. Eighty-three readings were made at home from the hub by byte range
(`tools/hub_range_read.py`), one hundred and forty comparisons among them: the layer 44 attention output and down
projection and the layer 10 query projection of bgg1996's pass against its parent's, Google's, Vampelium's and
germlag's; the layer 40, 46 and 48 attention outputs of llmfan46's MeroMero edit against zerofata's, Google's,
coder3101's and the maker's April edit; the layer 45 and 50 attention outputs of the Queen edit against
aifeifei798's, Google's and the maker's April edit; the layer 16 and 4 attention outputs of Vortex5's Moonlight-Dusk
edit against the merge's, Google's, SassyDiffusion's and llmfan46's; the layer 30 attention output and down
projection of Justbackup's duplicate against coder3101's, Google's and DavidAU's; the layer 20 attention output,
queries, keys and down projection and the layer 5 keys of SubMaroon's merge against StyleTune-V2's, coder3101's,
Google's and Pantheon-Reasoning V2's; the layer 20 attention output and down projection of DavidAU's 4B fine-tune
against the Extreme's and Google's; and the layer 10 attention output of Vortex5's Chimera-X edit against the
merge's, Google's, llmfan46's and the maker's Moonlight-Dusk edit and merge. The hub's commit histories, file
listings and cards were read for the eight copies and their eight parents, DavidAU's 27B repository at three
revisions, Google's 27B and 4B, and the template histories of Google's 31B and 26B-A4B, llmfan46's 31B,
coder3101's 26B-A4B and Gryphe's Pantheon-Reasoning V2; bgg1996's `reproduce/` folder was read at the pinned
revision. One hundred and eighty-four comparisons were made from the saved direction files, listed in the reading
notes.

Weight differences alone cannot certify the absence of hidden behavior.
