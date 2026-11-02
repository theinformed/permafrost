# Census round 40: eight direct Gemma 4 copies on Nautilus, four makers' per-layer 31B passes at 1.000 to each other with the bytes apart, a projection whose direction is not a refusal direction, and a Japanese-weighted search at half the English family's agreement (2026-11-02)

Eight published copies compared with their originals on Nautilus from the batch pinned as
`data/batches/round-40-batch-1.json` (pinned 2026-11-02 06:56Z) under the CPU census kit: download job 4169647,
compares 4169648 to 4169655, sweep 4169656, which deleted the seven originals (`ae782a34` of google/gemma-4-31B-it
at `419b2efe` for pair 1, `8ee0b411` of the 31B at `842da379` for pairs 2 and 4, `500bda7e` of google/gemma-4-26B-A4B-it
at `4d7ae498` for pair 3, `1b1bc807` of the 31B at `fcf23027` for pair 5, `3514f9ec` of the 31B at `35487898` for
pair 6, `ed9be084` of google/gemma-4-E4B-it at `292a7e27` for pair 7 and `6273b5b6` of google/gemma-4-E2B-it at
`4742fe84` for pair 8) from `/p/work1/sdegan/model-audit/rounds/40/originals/`. The pull (card 5775) brought home
the eight measurement folders and the sweep record and no job log, so the compares' nodes and seconds are not in
this note. The batch note says what the round is: eight direct copies of the Gemma 4 instruct models not yet
measured, pinned from the unmeasured list by downloads, five of them 31B edits so that the round fetched the 31B
original at its four revisions once each; the pinner refused five re-uploads of measured files (lessans's 31B and
26B-A4B copies of TrevorJS's files, eyentsign's of llmfan46's 31B, aj123's of coder3101's 31B, and p-e-w's E4B
heretic REPRODUCED, whose weight files are the ones his first E4B export carries, measured in round 33), and it
records that germlag's copy "was duplicated from coder3101's and its weight files differ", the parent being
coder3101's second 31B export, which the hub no longer serves. Seven of the eight are first measurements of
distinct copies and the eighth, germlag's, is a hub duplicate of that unmeasured second export (one commit titled
"Duplicate from", the parent gone), the eighth such case in the census and the first whose parent vanished before
it was measured. No original is new: the seven Google revisions are revisions of checkpoints the population
counts already, two of them pinned for the first time (the 31B at `fcf23027`, the 26B-A4B at `4d7ae498`), which
brings the population to one hundred and ninety-one measurements of one hundred and eighty-four distinct copies on
thirty-three originals: the round 39 header's numbers plus eight measurements and eight copies. Two pairs are
Heretic 1.2.0 per-layer passes on the 31B that read at 1.000 to each other and to two earlier makers' passes
(germlag's duplicate and Vampelium's), one is Heretic's arbitrary-rank branch searched on a Japanese-weighted
prompt set (Jim-darby's), one is the same branch under an attention-only card measured on both writers
(NullpoLab's Refusals6-attn), one is a kernel pass with a single direction (tvall43's E2B v0, thirty-four minutes
before the v1 of round 39), one is an expert-granular biprojection on the 26B-A4B (Rootkit7's), one is a maker's
own per-layer projection of the 31B at two alphas (DuoNeural's), and one is a projection of a direction that is
not a refusal direction (cosmicoptima's). The eight measurements were re-scored at home with the recipe table as
committed and the saved direction vectors, and no flag count moved. Every metadata report was judged again at
home under transformers 5.22.1 with the originals' later commits; the home judgement moved one field on each of
pairs 1, 2, 4, 5, 6 and 8 and two on pair 7 (pairs 1, 2, 4, 6, 7 and 8 turn to consistent with re-save noted;
pair 5 stays unexplained for a template that is Google's earlier revision) and none on pair 3. Each pair has a
card (the tool's Stage 1 text after the home judgement, with the Stage 2 line) and a reading note in
`docs/cards/`; the measurements are in `results/weights/` and `results/meta/`, and the direction vectors stay in
the pull copy (`/opt/ai/hpc-packages/pulls/model-audit/nautilus40/measurements/pair-N/`).

| Pair | Copy | Original | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | germlag/gemma-4-31B-it-heretic-v2 | google/gemma-4-31B-it | violations, 2 flags (the within-layer cosine of layer 59) | a hub duplicate of coder3101's unmeasured second export, the parent gone from the hub: one direction per layer on the output side of the down projections of layers 26 to 59 and the attention outputs of 29 to 59 (65 of 1,188), the card's two kernels to the layer and in height (1.31 at 49 and 1.46 at 57 under printed maxima of 1.32 at 49.63 and 1.47 at 57.33); rows 0.0016 to 0.0079 and 0.047 on one; exactly 0 outside; the directions at 1.000 to 3MPER0RR's, Vampelium's and callmegrr's passes |
| 2 | cosmicoptima/gemma4-31b-consciousness-abliterated | google/gemma-4-31B-it | violations, 117 flags (first shares 0.988 to 0.993 under the 0.99 floor) | the card exactly: one direction, taken from layer 58 from paired prefixes about internal state, projected at alpha 1.0 out of the token embedding and both writers of all 60 layers (121 of 1,188), the left kept fraction 0.00 on all 120 writers; rows 0.0017 to 0.040; exactly 0 outside; the direction at 0.034 or less to every measured 31B edit |
| 3 | Rootkit7/Gemma-4-26B-A4B-abliterated | google/gemma-4-26B-A4B-it | violations, 17 flags (16 expert first shares at 0.978 to 0.989, one within-layer cosine) | the card exactly: one direction per layer on the output side of the attention output, the dense down projection and all 128 experts of the sixteen layers the card lists (48 of 1,013), rows restored to 0.0001 to 0.0012 under the card's norm-preserving biprojection; exactly 0 outside; the directions at 0.93 to TrevorJS's family and 0.91 to xdavxd's QAT run of the same method, the second shard the library layout's |
| 4 | Vampelium/gemma-4-31B-it-heretic | google/gemma-4-31B-it | violations, 21 flags (19 first shares in the kernel's tail, 2 within-layer cosines) | one direction per layer on the output side of the attention outputs of layers 34 to 59 and the down projections of 39 to 59 (47 of 1,188), two kernels the card does not print (0.04 rising to 1.16 and falling to 0.36; 1.01 to 1.45); rows 0.0005 to 0.041; exactly 0 outside; the directions at 1.000 to 3MPER0RR's, germlag's and callmegrr's passes, the first seven shards byte-equal to 3MPER0RR's |
| 5 | Jim-darby/gemma-4-31B-it-heretic-ara-ja80en20 | google/gemma-4-31B-it | violations, 74 flags (38 first shares, 36 within-layer cosines) | the arbitrary-rank branch on both writers of layers 27 to 46 (38 of 1,188), the card's window; 32 edits on the input side at weights 0.66 to 1.10 with rows 0.0050 to 0.0078, the band, under a card that says "Row normalization: none", six residues and two down projections under the threshold (0.000983 the largest outside); the direction at 0.41 to 0.64 to the English-prompted 31B searches, which stand at 0.87 to 0.97 to each other; the template Google's 04-28 revision, older than the pin |
| 6 | DuoNeural/Gemma4-31B-IT-Abliterated | google/gemma-4-31B-it | violations, 74 flags (first shares 0.947 to 0.990) | the card exactly, and the maker's own: one direction per layer on the output side of both writers of all 60 layers (120 of 1,188) at the card's alphas to two decimals (left kept 0.60 on every down projection, 0.20 on every attention output); rows 0.0013 to 0.358; exactly 0 outside; the directions at 0.28 to TrevorJS's on all 120 names, the bytes further from his than from Google's, where the maker's 26B-A4B copy stood at 1.000 |
| 7 | NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals6-attn | google/gemma-4-E4B-it | violations, 61 flags (31 first shares, 30 within-layer cosines) | the arbitrary-rank branch on both writers of layers 21 to 36 (31 of 2,130) under a card naming `attn.o_proj` alone and a window to 41, fifteen down projections edited and the layer 21 down projection under the threshold (0.00038 the largest outside); input side at weights 0.91 to 1.90 with rows 0.0009 to 0.0131; the directions at 0.995 to the maker's Refusals8-attn, made four minutes later, the bytes 0.0097 apart; the template Google's 04-28 revision, carried in by the 04-29 upload |
| 8 | tvall43/gemma-4-E2B-it-heretic-v0 | google/gemma-4-E2B-it | clean match of `single-projection-selected`, 0 flags | one direction across the attention outputs of layers 12 to 30 (19 of 1,947), the card's kernel position and distance to the layer, on the output side at 2.05 rising to 4.84 at layer 21 and falling to 1.85, the kernel's shape at three times its printed maximum; rows 0.018 to 0.422; exactly 0 outside; the direction at 0.95 to huihui-ai's E2B family and 0.04 to the maker's v1 of thirty-four minutes later; 64 vision-encoder range scalars dropped where v1 dropped 128 |

Nothing moved outside the matrices the maker's method reaches in any of the eight pairs: the largest relative
change outside the changed set is exactly 0 on pairs 1, 2, 3, 4, 6 and 8, 0.000983 on pair 5 and 0.00038 on pair
7, both inside the card's window on a down projection the search left under the threshold. Six of the eight
copies are what their cards say (pairs 2, 3, 4, 5, 6 and 8), three of them with a qualification the weights
supply: Vampelium's card prints no table and the weights give two kernels, Jim-darby's card says "Row
normalization: none" and the rows carry the branch's preservation in finding 22's band, and tvall43's kernel
reads three times its printed maximum. The seventh, NullpoLab's Refusals6-attn, is finding 87 over again four
minutes earlier: a card that names the attention outputs as its one target, measured on both writers, fifteen
down projections edited. The eighth, germlag's, is the hub's duplicate of a second export coder3101 has since
removed; the measurement reads that export, and the batch note had already separated it from coder3101's first
export by its file checksums before any byte was read. The round's result for the method is the four 31B passes
at 1.000. germlag's duplicate (coder3101's export of 04-05), callmegrr's heretic-z (08-07), Vampelium's (08-30)
and 3MPER0RR's (09-01) stand at 1.000 to each other on both sides on every shared matrix (41, 47 and 12 names;
the one minimum under 0.99 is 0.983 at Vampelium's layer 34, where its change is 0.0014), with four windows
(26 to 59, 34 to 59 and two others), four weights and, by byte range, four sets of bytes: the layer 41 attention
output 0.0094 to 0.0192 from Google's and 0.0017 to 0.0100 apart, the layer 41 and 50 down projections 0.0005 to
0.0035 apart. Findings 85, 95 and 102 read 1.000 as a copy or a reproduction of one run and 0.96 to 0.97 as an
independent run of the method. On the 31B the tool's per-layer direction step gives four makers the same
directions months apart with nothing else in common, so the number alone no longer separates a copy from a
pass; the bytes and the weights do, and both were read.

The weights read off the weights. The two per-layer kernel passes (pairs 1 and 4) read on the output side with
weights that rise along the window: coder3101's second export to 1.31 at layer 49 and 1.46 at 57, within 0.01
of the card's printed maxima at the layers it prints; Vampelium's to 1.16 at 50 on the attention outputs and 1.45 at 56 and 58 on the
down projections under a card with no table. tvall43's v0 (pair 8) reads one direction, the card's index 17.07,
at 2.05 rising by a third a layer to 4.84 at layer 21 and falling to 1.85 at 30, the kernel's shape at three
times the card's maximum of 1.45. The two arbitrary-rank edits (pairs 5 and 7) read on the input side at 0.66 to
1.10 and 0.91 to 1.90, the two writers of a layer unrelated (0.0005 to 0.15), Jim-darby's leaving six residues
and NullpoLab's none. DuoNeural's projection (pair 6) reads one direction per layer at the card's alphas, the left
kept fraction 0.5955 to 0.6040 on all sixty down projections and 0.1968 to 0.2027 on all sixty attention outputs.
cosmicoptima's (pair 2) reads one direction for the whole model at a left kept fraction of 0.00 on all 120
writers and the same direction on the embedding's hidden side. Rootkit7's (pair 3) reads one direction per layer
on all three writers at output-side weights of 0.43 to 0.99, varying by layer under a card that prints two
scales.

Preservation claims. Two cards claim a norm in words and one denies it. Rootkit7's "per-row,
magnitude-restoring biprojection (norm-preserving)" reads in the rows at 0.0001 to 0.0012 on all 48 matrices,
as xdavxd's run of the same method read (finding 74). coder3101's magnitude-preserving orthogonalisation, through germlag's duplicate, leaves the rows at
0.0016 to 0.0079 on 64 matrices and 0.047 on the last down projection; tvall43's at 0.018 to 0.422. Jim-darby's
"Row normalization: none" stands over rows at 0.0050 to 0.0078 on every edit, finding 22's band, the branch's
preservation applied whatever the card's line names. NullpoLab's card does not name the preservation and the
rows read 0.0009 to 0.0131, through and over the band at the layers of the largest weights, as the maker's three
earlier exports read. Vampelium's, DuoNeural's and cosmicoptima's cards claim nothing and the rows are
unrestored (to 0.041, 0.358 and 0.040).

Fingerprints. Pair 1's two shards (`20e9835e`, `af865e9a`) match no measured file; the first is the size of
coder3101's first export's first shard and not its bytes, the batch note's "weight files differ" read before the
download. Pair 4's first seven shards (`78be59e4` to `566b3699`) are byte-equal to 3MPER0RR's, the two exports
touching nothing below layer 34 (finding 71's layout), and its other six match nothing. Pair 3's second shard
(`5c0b909c`) is byte-equal to SassyDiffusion's and WWTCyberLab's 26B-A4B second shards, the layout again. Pairs
2, 5, 6, 7 and 8 share no checksum with any measured file. By byte range the four 31B passes of 1.000 differ
from Google and from each other on every edited tensor read and are byte-equal to Google on the layer 10 query
projection; DuoNeural's layer 20 writers are 0.0169 and 0.0063 from Google's and 0.0226 and 0.0165 from
TrevorJS's; tvall43's v0 and v1 are 0.1429 apart on the layer 21 attention output; NullpoLab's two attention-only
exports are 0.0097 apart on the layer 29 attention output; Rootkit7's layer 20 attention output is 0.0194 from
Google's and 0.0117 from TrevorJS's.

Directions. The round placed its edits against the saved vectors of earlier measurements without a download
(finding 66's check): two hundred and twenty-two comparisons against the saved vectors of measurements of the
31B (twenty-six for each of five pairs, this round's own among them), the 26B-A4B (twenty-four), the E4B
(thirty-nine) and the E2B (twenty-two). The four passes at 1.000 are above. cosmicoptima's direction stands at
0.034 or less to every 31B edit (0.031 to 0.034 to huihui-ai's two exports, 0.013 to TrevorJS's and ressl's on all
120 names, 0.007 to DuoNeural's), a direction the census had not seen, as its card says. DuoNeural's 31B copy
stands at 0.28 and 0.21 to TrevorJS's and ressl's on all 120 names and at 0.52 or less to everything, where the
maker's 26B-A4B copy of round 38 stood at 1.000 to TrevorJS's (finding 95): the maker's own work this time, and
the byte reads agree. Rootkit7's stands at 0.93 to TrevorJS's edit and its re-uploads on all 48 names, 0.92 to
the 26B-A4B kernel exports and tvall43's pass, 0.91 to xdavxd's EGA run on the QAT checkpoint, and 0.19 or less
to the arbitrary-rank edits: an independent run inside finding 24's family. Jim-darby's Japanese-weighted search
stands at 0.41 to 0.64 to the English-prompted 31B arbitrary-rank searches (coder3101's two, llmfan46's two,
MoonRide's two, Bahushruth's, OS-Software's), which stand at 0.87 to 0.97 to each other, the distance findings 83,
93 and 99 read between prompt sets on the E4B, the 26B-A4B and the E2B, and at 0.23 or less to the kernel passes.
NullpoLab's Refusals6-attn stands at 0.995 to the maker's Refusals8-attn of four minutes later and to coder3101's,
0.985 to Refusals5 and Refusals8, and 0.96 to llmfan46's and MoonRide's, finding 82's family at its centre.
tvall43's v0 stands at 0.95 to huihui-ai's E2B edit and its re-uploads on all 19 names and 0.94 to DuoNeural's E2B
single direction (finding 96), and at 0.04 to the maker's own v1 of thirty-four minutes later, which stood at
0.98 to TrevorJS's (finding 103): two passes by one maker in one hour with two different directions.

## The token side

The cluster's cards read "unexplained differences" on seven of the eight and "consistent with re-save noted" on
pair 3. The home judgement under transformers 5.22.1 with the originals' later commits moved eight fields on
seven cards: `text_config.moe_intermediate_size` on pairs 1, 2, 4, 5, 6, 7 and 8 (absent on one side, the same
default under 5.22.1) and pair 7's template, byte-equal to Google's E4B revision `c53e9d33` of 04-28
("fix(chat_template): update SI and tool call handling"), carried in by the copy's 04-29 upload, as the maker's
Refusals8 carried it in round 39. Pairs 1, 2, 4, 6, 7 and 8 turn to consistent with re-save noted, their remaining
differences version strings (5.5.0.dev0 to 5.5.0, 5.12.1, 5.6.2, 5.10.2 and 5.5.0; pair 8 has none). Pair 5
stays unexplained on one field, its template: the copy's 16,934-byte template is byte-equal to Google's 31B
revisions `145dc250` of 04-28 and `ba74f5b6` of 05-07, the template the hub served until `fcf23027` replaced it
on 05-18, eight days before the copy was made, so the maker's snapshot was older than the hub's head and the home
tool, which checks later revisions only, cannot close it (round 31's pairs 2 and 4, round 35's pair 5 and round
39's pair 6 are the same case). Every pair carries the instruct checkpoint's token ids (the configuration's
`eos_token_id` `[1, 106]`, the generation configuration's `[1, 106, 50]`, `bos_token_id` 2, `pad_token_id` 0),
so round 39's pretrained-checkpoint case does not recur. Pair 3 differs in version strings alone.

## What the scorer learned

The flag counts are the same on the cluster and at home. Their causes, by pair:

- One clean read, 0 flags (pair 8): the single-projection entry with selection fits one direction on the
  attention outputs alone; it has no weight line, and 4.84 is the largest output-side weight the census has read
  on a kernel pass.
- Per-layer passes under the per-layer entry, 2 and 21 flags (pairs 1 and 4): the within-layer rule at 0.95 fails
  layer 59 on both (0.925 and 0.924), and on pair 4 the first-share floor fails the 19 matrices in the kernel's
  tail where the change is 0.0014 to 0.0180 and the bfloat16 rounding of the untouched part is a larger share of
  it; a kernel-tail rule tied to the change would read pair 4 clean.
- Per-layer passes under a floor meant for one matrix, 17 and 74 flags (pairs 3 and 6): the expert stacks of 128
  slices hold one direction at a first share of 0.978 to 0.989, and DuoNeural's rank-one projections at 0.947 to
  0.990 carry the same rounding residue; floors at 0.97 and 0.94 would read both as their cards.
- A whole-model projection under the single-projection entry, 117 flags (pair 2): the first-share floor at 0.99
  fails 117 of 121 matrices at 0.988 to 0.993, the floor the kernel exports also need (round 39's pair 3).
- Arbitrary-rank edits under the per-layer entry, 74 and 61 flags (pairs 5 and 7): a few directions per matrix
  fails the first-share rule on every edit, and the two writers of a layer each with their own direction fail the
  within-layer rule; an arbitrary-rank entry would read both as clean matches with the residues and the unnamed
  down projections called out.

The round's result for the measure is pair 1 with pair 4 and the two earlier passes: the direction check that
named parents in rounds 38 and 39 (1.000 on 90 names; 1.000 on 347; 1.000 on 228) returns 1.000 on 41 and 47
names between four makers whose exports are months apart, and the byte-range reads and the per-layer weights
separate them where the directions do not. The check keeps its place (it is what sent the byte reads) and loses
its standing as a conclusion on its own: 1.000 on the directions of a per-layer Heretic pass of the 31B says the
same tool and the same prompt set, and the copy or reproduction reading needs the bytes (findings 95 and 102
had them) or the per-tensor numbers equal to the digit (finding 85 had them).

## Owed to the metadata tool

Added since: nothing this round. What remains: the earlier-revision template and configuration through a
snapshot older than the pin (round 31's pairs 2 and 4, round 35's pair 5, round 39's pair 6, this round's pair 5,
whose template is byte-equal to two revisions of the hub's history before the pin); the declared-context line;
the float16 `dtype` reading; the 5.16 save form as a named re-save (finding 39); the dropped-declarations rule
through `tokenizer.json`; a maker's-template rule (round 37's pair 7); the loader-moved-token and
missing-template lines of round 38; the pretrained-ids line of round 39. To the pinner: the direction check at
the names step stays, with the reading of this round beside it (1.000 on a per-layer 31B pass is the tool, not a
copy, until the bytes are read), and a byte-range step after it for any pair at 1.000. To the recipe table: an
arbitrary-rank entry with a components line (pairs 5 and 7), a kernel-tail rule on the per-layer entry (pair 4),
a weight line on the per-layer entry (pairs 1, 4 and 6), a first-share floor at 0.97 on expert stacks (pair 3)
and at 0.988 on the single-projection entry (pair 2), and a weight line on the single-projection entry with
selection (pair 8).

## Operational

The round ran on Nautilus under the CPU census kit: one download, eight compares and the sweep, every compare
finishing with its card and its weights report, the sweep deleting the seven originals. The pull (card 5775)
carries the eight measurement folders (card, metadata, weights, direction vectors and the sha256 record of each)
and the sweep record; no job log was pulled, so the compares' nodes and seconds are not recorded. The home
judgement ran under transformers 5.22.1. Thirty-four readings were made at home from the hub by byte range
(`tools/hub_range_read.py`), fifty-one comparisons among them: the layer 41 attention output, the layer 41 and
50 down projections and the layer 10 query projection of the four 31B passes at 1.000 against each other and
Google's; the layer 20 attention output and down projection of DuoNeural's 31B copy against TrevorJS's and
Google's; the layer 21 attention output of tvall43's v0 against his v1, huihui-ai's and Google's; the layer 20
attention output of Rootkit7's against TrevorJS's and Google's; and the layer 29 attention output of
Refusals6-attn against Refusals8-attn and Google's. The hub's commit histories, file listings and cards were read
for the eight copies, coder3101's two 31B repositories (the second answering "not found"), TrevorJS's 31B and
DuoNeural's 26B-A4B copies, NullpoLab's Refusals8 and Refusals8-attn, tvall43's v1, and the 31B original's
templates at ten revisions and the E4B's at three, which placed pair 5's template. Two hundred and twenty-two
comparisons were made from the saved direction files, listed in the reading notes.

Weight differences alone cannot certify the absence of hidden behavior.
