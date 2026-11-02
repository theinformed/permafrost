# Census round 38: eight direct Gemma 4 copies on Nautilus, one carrying another maker's edit under its own card and one a hub duplicate of an unmeasured fine-tune (2026-11-02)

Eight published copies compared with their originals on Nautilus from the batch pinned as
`data/batches/round-38-batch-1.json` (pinned 2026-11-02 05:11Z) under the CPU census kit: download job 4168771,
compares 4168772 to 4168779, sweep 4168780, which deleted the seven originals (`726eaa98` of
google/gemma-4-26B-A4B-it at `47b6801b` for pair 1, `37a42740` of google/gemma-4-E4B-it at `83df0a88` for pair 2,
`87a447ff` of google/gemma-4-12B-it at `5926caa4` for pairs 3 and 4, `e933fd51` of the 26B-A4B at `7d4c97e5` for
pair 5, `d80e1b2c` and `5e6bb5ba` of google/gemma-4-E2B-it at `6b7e72c6` and `3e22461f` for pairs 6 and 7, and
`5719e553` of the E4B at `fa62d88d` for pair 8) from `/p/work1/sdegan/model-audit/rounds/38/originals/`. The pull
brought home the eight measurement folders and the sweep record and no job log, so the compares' nodes and seconds
are not in this note. The batch note says what the round is: eight direct copies of the Gemma 4 instruct models
pinned by size class, the pinner having refused gsting's 26B-A4B copy as huihui-ai's weight files measured in round
12 and recorded that DuoNeural's 26B-A4B card names its own GGUF export where its `base_model` field names Google.
Seven of the eight are first measurements of distinct copies and the eighth, Himanshuoo8's, is a hub duplicate of
DavidAU's unmeasured E4B copy (one commit titled "Duplicate from", the weight file byte-equal); no original is new,
the four Google revisions all standing in the population already, which brings the population to one hundred and
seventy-five measurements of one hundred and sixty-eight distinct copies on thirty-three originals: the round 36
header's numbers plus eight measurements and eight copies. Three pairs are Heretic 1.2.0 arbitrary-rank edits
(SassyDiffusion's of the 26B-A4B and the E4B, RumiaChannel's Refusals2 of the 12B), one is a maker's own
arbitrary-rank solver (Bahushruth's E2B), one is a maker's own null-space projection on every linear map
(jwest33's 12B), one is a single-direction projection with a kernel the card does not print (DuoNeural's E2B), one
is TrevorJS's 26B-A4B edit under DuoNeural's card, and one is coder3101's E4B edit under an Unsloth fine-tune
reached through the duplicate. The eight measurements were re-scored at home with the recipe table as committed
and the saved direction vectors, and no flag count moved. Every metadata report was judged again at home under
transformers 5.22.1 with the originals' later commits; the home judgement moved one field on each of pairs 1, 2, 6,
7 and 8 and five on pair 3 (pairs 2, 3 and 7 turn to consistent with re-save noted; pairs 1, 6 and 8 stay
unexplained for reasons the field closures do not touch) and none on pairs 4 and 5. Each pair has a card (the
tool's Stage 1 text after the home judgement, with the Stage 2 line) and a reading note in `docs/cards/`; the
measurements are in `results/weights/` and `results/meta/`, and the direction vectors stay in the pull copy
(`/opt/ai/hpc-packages/pulls/model-audit/nautilus38/measurements/pair-N/`).

| Pair | Copy | Original | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | SassyDiffusion/gemma-4-26B-A4B-it-heretic-ara | google/gemma-4-26B-A4B-it | violations, 61 flags (35 first shares, 26 within-layer cosines) | an arbitrary-rank edit whose card is 208 bytes of front matter and the tag `heretic-ara`: the attention outputs of layers 6 to 28 (20) and the dense down projections of 6 to 27 (15), 35 of 1,013, no expert touched, twelve more under the threshold to 0.000673; input side on all 35 at weights 0.42 to 1.89, rows 0.0007 to 0.027 under no claim; the directions at 0.98 to llmfan46's and coder3101's 26B-A4B edits; saved through Unsloth, which moved the end-of-sequence token to `<turn\|>` and set a pad token the original leaves unset, with Google's later template |
| 2 | SassyDiffusion/gemma-4-E4B-it-heretic | google/gemma-4-E4B-it | violations, 21 flags (first shares 0.47 to 0.97) | Heretic 1.2.0's arbitrary-rank edit with row-norm preservation on the attention outputs of layers 21 to 41 (21 of 2,076), the card's start 21 and end 42 and its one target, no down projection; input side on all 21 at weights 0.84 to 2.72, rows 0.0068 to 0.0078, finding 22's band on every one; exactly 0 outside; the directions at 0.98 and 0.97 to coder3101's E4B edit and 0.99 to alphakek's; the 54 shared-key-value tensors absent from the save |
| 3 | RumiaChannel/gemma-4-12B-it-uncensored-ara-Refusals2 | google/gemma-4-12B-it | violations, 80 flags (40 first shares, 40 within-layer cosines) | Heretic 1.2.0's arbitrary-rank edit with row-norm preservation on both writers of layers 23 to 42 (40 of 677), the card's start 23 and end 43; 37 edits on the input side at weights 0.45 to 1.52 with rows 0.0052 to 0.0079, the band on every one, and three down projections left as residues (0.0013 to 0.0017, no direction); exactly 0 outside; the directions at 0.98 and 0.99 to the maker's Refusals9 and 0.55 to 0.64 to the English 12B family and the Japanese export; the template Google's later revision |
| 4 | jwest33/gemma-4-12B-it-null-space-abliterated | google/gemma-4-12B-it | violations, 271 flags (175 first shares, 96 unexpected changes) | the maker's own null-space projection, its configuration and direction files in the repository: every linear map of all 48 layers and the token embedding (329 of 677), one direction equal to the shipped `mean_direction` at 0.96 to 1.00 on every matrix, writers on the output side and readers on the input side, a Gaussian weight over the layers (0.10 on layers 0 to 7, 1.07 at layer 27, 0.15 at 47) that reads back from the shipped configuration within 0.047; rows to 0.082 under a Frobenius-norm claim; exactly 0 outside; the direction at 0.58 or less to every other 12B edit |
| 5 | DuoNeural/gemma-4-26B-A4B-it-abliterated | google/gemma-4-26B-A4B-it | violations, 31 flags (30 worst-expert first shares, 1 within-layer cosine) | TrevorJS's 26B-A4B edit under a card that names the maker's own "expert-granular" method: the attention outputs, dense down projections and packed expert down projections of all 30 layers (90 of 1,013), one direction per layer shared by the three kinds and by the 128 experts of a layer, output side with the biprojection's second term, rows within 0.0012; exactly 0 outside; the directions equal to TrevorJS's at 1.000 on all 90, the tensors within 0.0004 to 0.0006 of TrevorJS's by byte range where both stand 0.018 to 0.023 from Google's, uploaded eight days after TrevorJS's |
| 6 | DuoNeural/Gemma-4-E2B-Heretic | google/gemma-4-E2B-it | clean match of `single-projection-selected`, 0 flags | one direction projected from the down projections of layers 6 to 34 and the attention outputs of 15 to 34 (49 of 1,951), output side at weights that rise from 0.75 at layer 6 to 1.43 at 21 and fall to 0.83 at 34 on the down projections and run 1.03 to 1.32 on the attention outputs, a kernel the card does not print; rows 0.006 to 0.040, unrestored; exactly 0 outside; the direction at 0.925 to huihui-ai's E2B edit on every matrix and 0.08 or less to every other; no chat template in the repository; the card says 42 layers of a 35-layer model |
| 7 | Bahushruth/gemma-4-E2B-it-abliterated | google/gemma-4-E2B-it | violations, 36 flags (18 first shares, 18 within-layer cosines) | the maker's own arbitrary-rank solver on both writers of layers 16 to 24 (18 of 1,951) under a card that names all 35; a few directions per matrix (first shares 0.27 to 0.56), input side at weights 1.56 to 2.08, rows within 0.0004 under the card's reparameterisation, the third preservation claim in the census that holds; exactly 0 outside; the directions at 0.69 or less to every E2B edit; the 60 shared-key-value tensors absent from the save |
| 8 | Himanshuoo8/gemma-4-E4B-it-Claude-Opus-4.5-HERETIC-UNCENSORED-Thinking | google/gemma-4-E4B-it | violations, 366 flags (209 unexpected changes, 78 first shares, 78 direction cosines, 1 cross-kind) | a hub duplicate of DavidAU's unmeasured E4B copy: coder3101's Heretic edit of the attention outputs of layers 21 to 41, named in the configuration's `model_name` and standing at 1.000 on 20 of the 21, under an Unsloth fine-tune of 0.1 to 0.7 percent on every linear map of the 42 layers (287 of 2,130, seven more under the threshold to 0.000893), a template that inserts a thinking tag after the system turn, and no generation configuration |

Nothing moved outside the matrices the maker's method reaches in six of the eight pairs: the largest relative
change outside the changed set is exactly 0 on pairs 2, 3, 4, 5, 6 and 7, and on pairs 1 and 8 it is the search's
own footprint and the fine-tune's tail inside the window (0.000673 on twelve matrices of layers 5 to 7 and
0.000893 on seven matrices of layers 0 to 6). Six of the eight copies are what their cards say, two of them with a
qualification the card itself supplies: DuoNeural's E2B card names 42 layers on a 35-layer model and prints no
kernel, and Bahushruth's names all 35 layers where the solver touched nine. The seventh is a hub duplicate and is
measured as its parent, DavidAU's fine-tune over coder3101's edit, which that parent's card describes. The eighth
is the round's result for the method. DuoNeural's 26B-A4B copy describes a method of the maker's own, a
per-expert refusal direction across all 128 experts, and the weights carry TrevorJS's edit: one direction per
layer shared by the experts, as finding 13 read TrevorJS's own, the saved directions equal to TrevorJS's at 1.000
on all 90 matrices, and the tensors themselves within 0.0004 to 0.0006 of TrevorJS's by byte range where both
copies stand 0.018 to 0.023 from Google's. xdavxd's independent run of the same method on the QAT checkpoint
stands at 0.97 to TrevorJS's (finding 74); 1.000 is not a second run.

The weights read off the weights. The three Heretic arbitrary-rank edits (pairs 1, 2 and 3) read on the input
side on 35 of 35, 21 of 21 and 37 of 40 matrices at weights of 0.42 to 2.72, with three of RumiaChannel's down
projections left as residues without a direction, finding 58's shape. Bahushruth's solver (pair 7) reads on the
input side at 1.56 to 2.08 with a few directions per matrix, finding 57's over-reflection again. jwest33's
projection (pair 4) reads on the output side of the writers and the input side of the readers, one direction on
every matrix, with the Gaussian weight schedule the shipped configuration names (`adaptive_position_center` 0.6,
`adaptive_position_sigma` 0.2, `direction_multiplier` 1.1) read back from 329 matrices within 0.047. DuoNeural's E2B
(pair 6) reads one direction on the output side at a kernel-shaped weight on both writers, where the per-layer
Heretic passes of finding 46 read no weight at all. DuoNeural's 26B-A4B (pair 5) reads TrevorJS's biprojection:
along the leading output direction the attention outputs keep 0.02 to 0.28, the dense down projections 0.00 to
0.51 and the experts a median 0.01 to 0.52, with the right side keeping 0.45 to 0.88. Himanshuoo8's duplicate
(pair 8) reads coder3101's input-side edit at weights 1.32 to 2.02 on the attention outputs of 21 to 40 and the
fine-tune everywhere else, 267 of its 287 changed matrices with both kept fractions within 0.05 of 1.

Preservation claims. Four copies claim row-norm preservation and all four hold it: SassyDiffusion's E4B edit reads
0.0068 to 0.0078 on all 21 and RumiaChannel's 0.0052 to 0.0079 on all 37 edits, finding 22's band on every
matrix; Bahushruth's reparameterisation reads 0.0001 to 0.0004 on all 18, the third claim in the census that holds
to the row (findings 57 and 74); DuoNeural's 26B-A4B card claims nothing and reads TrevorJS's 0.0001 to 0.0012.
jwest33's card claims the Frobenius norm of each matrix and the rows read 0.0003 to 0.082, which is what a
whole-matrix restoration leaves on the rows. Pairs 1 and 6 claim nothing and read 0.0007 to 0.027 and 0.006 to
0.040, and the ablation under pair 8's fine-tune reads 0.0071 to 0.0079 on the attention outputs of 21 to 40,
coder3101's band through the training.

Fingerprints. Pair 8's one weight file (`3131a32f`) is byte-equal to DavidAU's, the duplicate read from the commit
title and the checksum before the measurement. Pair 6's first two shards (`9ebcea19`, `b07560fd`) are the E2B
library layout shared with huihui-ai's, amkkk's, anlord's, aifeifei798's and prithivMLmods's exports (finding 71).
Pair 1's second shard (`5c0b909c`) equals WWTCyberLab's second, the 26B-A4B layout for the tensors neither edit
touches. Pair 5's two shards (`4415dd6b`, `e6dbf9c4`) differ from TrevorJS's (`4b988df4`, `3d2388e8`) and from
every measured file, which is what tensors 0.0004 apart give; the edit is TrevorJS's by its directions and its
values, not by its checksums. Pairs 2, 3, 4 and 7 share no checksum with any measured file.

Directions. The round placed its edits against the saved vectors of earlier measurements without a download
(finding 66's check): two hundred and forty-four comparisons against the saved vectors of measurements of the 12B
(seventy-four), the 26B-A4B (forty-eight), the E2B (forty-four) and the E4B (seventy-eight), this round's own among
them. SassyDiffusion's two edits join the arbitrary-rank families of finding 82: the 26B-A4B at 0.98 and 0.97 to
llmfan46's instruct edit and 0.98 on both sides to coder3101's, the E4B at 0.98 and 0.97 to coder3101's and 0.99
to alphakek's. RumiaChannel's Refusals2 stands at 0.98 and 0.99 to the maker's Refusals9 of the same base on 38
shared names, and at 0.55 to 0.64 on the left to the English 12B family (coder3101's, llmfan46's, the QAT edits)
and 0.64 to OS-Software's first Japanese export: one maker's two searches agree with each other and stand apart
from the rest at the distance finding 93 measured between searches, not between languages. DuoNeural's 26B-A4B
stands at 1.000 to TrevorJS's on all 90 names (left minimum 1.000, right minimum 0.978) and with it to the four
re-uploads of TrevorJS's file; xdavxd's run of the method on the QAT checkpoint stands at 0.97 and 0.95 to both,
and the 26B-A4B kernel edits (sh0ck0r's, BinxNet's, tvall43's, SevenOfNine's) at 0.965 to 0.981. DuoNeural's E2B
stands at 0.925 on both sides to huihui-ai's E2B direction on every one of 45 shared names, the same number on
every matrix because both edits use one direction for the model, and at 0.08 or less to every other E2B edit.
Bahushruth's solver stands at 0.69 to amkkk's, 0.68 to llmfan46's ultra edit and 0.61 to MoonRide's custom edit,
its own direction. jwest33's projection stands at 0.58 to the three kernel exports of the 12B and 0.55 to
huihui-ai's two 12B edits, and under 0.52 to the rest. Himanshuoo8's duplicate stands at 1.000 to coder3101's
E4B edit on 20 of 21 shared names and at 0.026 on the twenty-first, layer 41, where the fine-tune's change
(0.0049) outweighs the ablation's.

## The token side

The cluster's cards read "unexplained differences" on six of the eight, "consistent" on pair 4 and "consistent with
re-save noted" on pair 5. The home judgement under transformers 5.22.1 with the originals' later commits moved
ten fields on six cards: `text_config.moe_intermediate_size` on pairs 2, 6, 7 and 8 (absent on one side, the same
default under 5.22.1); pair 1's template, byte-equal to Google's revision `4c55b528` of 04-28; and on pair 3 four
audio and vision fields the 5.10.2 save leaves out (`audio_samples_per_token`, `hidden_size`, `output_proj_dims`,
`model_patch_size`, the same values under 5.22.1) and the template, byte-equal to Google's revision `711c1368` of
07-15. Pairs 2, 3 and 7 turn to consistent with re-save noted. Pair 1 stays unexplained for what Unsloth's save
did (finding 15's shape): the tokenizer's end-of-sequence token moved from `<eos>` (1) to `<turn|>` (106), the
configuration's `eos_token_id` from the pair `[1, 106]` to 106 alone, and `pad_token_id` from unset to 0, with the
generation configuration still naming `[1, 106, 50]`. Pair 6 stays unexplained because the repository ships no
chat template at all, in a model whose template is a file beside the weights. Pair 8 stays unexplained for the
fine-tune's save: `model_name` set to a local path ending in `gemma-4-E4B-it-heretic--coder3101`, an
`unsloth_version` of 2026.4.4 in place of a `transformers_version`, `torch_dtype` in place of `dtype`, a pad token
of 0, no `generation_config.json`, and a 16,352-byte template that inserts `<|think|>` after the system turn (so
the fixed conversation renders differently) beside a `chat_template-instruct.jinja` the loader never reads. Pair 4
differs in nothing, saved by the same library version as its original; pair 5 differs in version strings alone.

## What the scorer learned

The flag counts are the same on the cluster and at home. Their causes, by pair:

- Arbitrary-rank edits under the per-layer entry, 61, 21, 80 and 36 flags (pairs 1, 2, 3 and 7): a few
  directions per matrix fails the first-share rule on every edited matrix, and where both writers are edited each
  with its own direction the within-layer rule fails as well. An arbitrary-rank entry would read pairs 2, 3 and 7
  as clean matches (pair 3 with its three residues named) and pair 1 as a clean match under no card.
- A whole-model projection, 271 flags (pair 4): the per-layer entry names two writers, so the 96 gate and up
  projections are unexpected changes and the 175 first shares are the readers and writers of the early and late
  layers, where the Gaussian weight is 0.10 to 0.5 and the first share 0.80 to 0.90. An entry for a one-direction
  projection on every linear map with a per-layer weight would read the copy as a clean match with its schedule.
- The expert rule, 31 flags (pair 5): the scorer takes the worst expert (0.881 in layer 0, 0.951 to 0.990
  elsewhere) where the median expert is 0.99 in every layer, the flags finding 13 read on TrevorJS's own copy, and
  one within-layer cosine at 0.949 on layer 29. The 1.000 to TrevorJS's directions is not a rule the scorer has.
- A clean read, 0 flags (pair 6): the single-projection entry with selection fits one direction on 49 matrices.
- A fine-tune over an ablation, 366 flags (pair 8): every tensor the training touched outside the two writers is an
  unexpected change (209), and the ablation's window reads as 78 first shares and 78 direction cosines on the
  writers because the training's small change on the other writer of each layer has its own direction.

The round's result for the measure is pair 5: a card that describes its own method, a flag count and a fingerprint
that both match that method's family, and the saved directions equal to one earlier copy's at 1.000 where an
independent run of the same method gives 0.97. The direction comparison, not the recipe table, is the test that
separated the two, and it should run at the pin on every copy whose base has a measured family.

## Owed to the metadata tool

Added since: nothing this round. What remains: the earlier-revision template through a snapshot older than the
pin (round 31's pairs 2 and 4, round 35's pair 5); the declared-context line; the float16 `dtype` reading; the
5.16 save form as a named re-save (finding 39); the dropped-declarations rule through `tokenizer.json`; a
maker's-template rule (round 37's pair 7); and from this round, a loader-moved-token rule that reads Unsloth's
`unsloth_fixed` flag with the end-of-sequence and pad changes it makes (pair 1, finding 15's shape on a Gemma 4
copy) and a missing-template line that says so in one phrase when a repository ships no `chat_template.jinja`
(pair 6). To the pinner: a direction check at the names step against the saved vectors of the base's measured
family, so that a copy standing at 1.000 to a measured edit is flagged before it is downloaded (pair 5), and the
`model_name` field of a fine-tune's configuration read into the batch note when it names a measured copy (pair
8). To the recipe table: an arbitrary-rank entry, which four of this round's eight pairs would match, and a
whole-model one-direction entry with a per-layer weight (pair 4).

## Operational

The round ran on Nautilus under the CPU census kit: one download, eight compares and the sweep, every compare
finishing with its card and its weights report, the sweep deleting the seven originals. The pull (card 5766)
carries the eight measurement folders (card, metadata, weights, direction vectors and the sha256 record of each)
and the sweep record; no job log was pulled, so the compares' nodes and seconds are not recorded. The home
judgement ran under transformers 5.22.1. Three readings were made at home from the hub by byte range
(`tools/hub_range_read.py`): the layer 12 attention output and down projection and the layer 29 attention output
of DuoNeural's 26B-A4B copy against TrevorJS's and Google's. The hub's commit histories, file listings and cards
were read for the eight copies, DavidAU's parent repository, DuoNeural's GGUF export and the four originals, and
jwest33's three shipped files (`abliteration_config.json`, `refusal_directions.pt`, `null_space_projectors.pt`)
were read for the configuration and the mean direction. Two hundred and forty-four comparisons were made from
the saved direction files, listed in the reading notes.

Weight differences alone cannot certify the absence of hidden behavior.
