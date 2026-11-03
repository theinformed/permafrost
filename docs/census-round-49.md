# Census round 49: eight second-generation edits on Wheat, two passes on Drummer's Magistral fine-tunes, one of them over a depth upscale whose inserted layers carry the printed kernel, a search confined to the first stack of a passthrough merge, a norm-preserving name over a plain projection, a fine-tune on the last five layers that leaves a measured edit in place, a second reasoning pass that contains the first, and the census's first Gemma 2 copy read clean (2026-11-03)

Eight published copies compared with the parents their cards name on Wheat from the batch pinned as
`data/batches/round-49-batch-1.json` (pinned 2026-11-02 10:50Z) under the image-free kit with the standalone
Python: download job 387515, compares 387516 to 387523, sweep 387524, which deleted the eight parents (`da4d9338` of
TheDrummer/Skyfall-31B-v4.2 at `e36a890b` for pair 1, `fd028102` of TheDrummer/Magidonia-24B-v4.3 at `5e5b5e15` for
pair 2, `43bbeaa4` of zerofata/MS3.2-PaintedFantasy-Visage-v3-34B at `0c18eaaa` for pair 3, `87901ba9` of
LatitudeGames/Harbinger-24B at `0ded8c1f` for pair 4, `5be5ede5` of ConicCat/Gemma4-Garnet-31B at `200c398e` for pair
5, `1767ba1c` of coder3101/gemma-4-26B-A4B-it-heretic at `e6d09d5c` for pair 6, `f5d286ba` of
coder3101/gemma-3-27b-it-heretic at `b9449797` for pair 7 and `da19653b` of sam-paech/Darkest-muse-v1 at `55f6ba02`
for pair 8) from `/p/work/sdegan/model-audit/rounds/49/originals/`. The pull (card 5840) brought home the eight
measurement folders and the sweep record and no job log, so the compares' nodes and seconds are not in this note.
The batch note says what the round is: the fifth from the second-generation pool, Heretic and abliteration edits of
community fine-tunes and of measured copies, each measured against the parent its card names: coder3101's edits of
two of TheDrummer's Mistral Small fine-tunes beside the maker's four Cydonia versions of round 44, vprilepskii's
norm-preserving biprojected edit of a Mistral Small fine-tune, llmfan46's edits of a 34B Mistral Small merge and of
ConicCat's first Garnet fine-tune, Tetratype's antislop pass on coder3101's measured 26B-A4B edit, DavidAU's second
reasoning pass on coder3101's Gemma 3 27B edit, and Naphula's edit of sam-paech's Gemma 2 fine-tune. It records that
no measured pair is repeated and no copy duplicates a measured weight file by checksum. The batch note calls
coder3101's 27B edit measured; the census has measured it only as a parent, in round 42 under Justbackup's hub
duplicate of DavidAU's first pass (finding 121), and not against Google. Against the parent its card names a copy
reads the edit alone, and the parent's own distance from the publisher's checkpoint is read by byte range where the
note needs it. The population rule of finding 117 applies: a community parent counts as neither an original nor a
copy, so the originals stay the publisher's thirty-four checkpoints and a parent enters the copy count only when it
is itself measured against its own parent. Six parents are unmeasured community repositories (two fine-tunes of
Magistral Small 2509, a depth extension of a Mistral Small 3.2 fine-tune, a fine-tune of Mistral Small 3.1
Instruct, a fine-tune of Google's Gemma 4 31B and a merge of Gemma 2 9B fine-tunes), pair 7's is an unmeasured first
edit, and pair 6's is coder3101's 26B-A4B edit, a copy the census already counts, measured in round 12 against Google
at this revision. All eight are first measurements of distinct copies. The population comes to two hundred and
thirty-eight measurements of two hundred and thirty-one distinct copies on thirty-four originals: the round 47
header's numbers plus eight measurements and eight copies, with thirty-five re-uploads among them. The eight
measurements were re-scored at home with the recipe table as committed and the saved direction vectors, and no flag
count moved. Every metadata report was judged again at home under transformers 5.22.1 with the parents' later
commits; the home judgement closed `config.rope_parameters` on pair 3 (the 5.x form of `rope_theta`) and
`config.text_config.moe_intermediate_size` on pair 5 (absent on one side and loaded as the same default), and moved
nothing on the other six; no judgement changed. Each pair has a card (the tool's Stage 1 text after the home
judgement, with the Stage 2 line) and a reading note in `docs/cards/`; the measurements are in `results/weights/` and
`results/meta/`, and the direction vectors stay in the pull copy
(`/opt/ai/hpc-packages/pulls/model-audit/wheat49/measurements/pair-N/`).

| Pair | Copy | Parent | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | coder3101/Skyfall-31B-v4.2-heretic | TheDrummer/Skyfall-31B-v4.2 | violations against `single-projection-selected`, 47 flags (46 first shares, 1 cross-kind) | one shared direction on the down projections of layers 8 to 53 and the attention outputs of 10 to 53, the kernels' reaches, on the output side; the printed flat 1.48 read within 0.011 on the fourteen attention outputs the upscale inserted near zero and 0.64 to 1.35 on the thirty others; exactly 0 outside; at 0.817 and 0.792 to grayarea's two shared-direction passes (finding 143) |
| 2 | coder3101/Magidonia-24B-v4.3-heretic | TheDrummer/Magidonia-24B-v4.3 | violations against `directional-per-layer-selected`, 18 flags (first shares 0.981 to 0.988) | one direction per layer on the down projections of 12 to 35 and the attention outputs of 27 to 34, the card's two kernels read within 0.0036 and 0.0050 on all 32 matrices, rows 0.010 to 0.070, exactly 0 outside; at 0.645 to Pranavz's Hearthfire pass (finding 144) |
| 3 | llmfan46/MS3.2-PaintedFantasy-Visage-v3-34B-ultra-uncensored-heretic | zerofata/MS3.2-PaintedFantasy-Visage-v3-34B | violations against `directional-per-layer-selected`, 11 flags (first shares 0.747 to 0.973) | the branch on 11 attention outputs of layers 10 to 27, the rest of the card's window from 3 to 28 traced (0.000268 outside), all inside the first of the merge's two stacks, input-side weights 1.28 to 2.39, no component amplified; at 0.64 to 0.84 to the maker's three Mistral Small searches (finding 145) |
| 4 | vprilepskii/Harbinger-24B-biprojected-norm-preserving-abliterated | LatitudeGames/Harbinger-24B | violations against `single-projection-selected`, 58 flags (first shares 0.907 to 0.988) | one direction on the down projections of layers 4 to 39 and the attention outputs of 15 to 36 at 1.000 to itself, output side at smooth weights to 1.443, rows 0.0031 to 0.0178 under a norm-preserving name, and by byte range a plain projection within 0.0026 to 0.0031 of the copy; exactly 0 outside; at 0.746 to venkycs's projection (finding 146) |
| 5 | llmfan46/Gemma-4-Garnet-31B-it-uncensored-heretic | ConicCat/Gemma4-Garnet-31B | violations against `directional-per-layer-selected`, 16 flags (first shares 0.924 to 0.971) | the branch on 16 attention outputs of layers 26 to 45, the card's window to the layer with four traced (0.0000034 outside), input-side weights 1.64 to 3.44, rows to 0.3246, no component amplified; at 0.883 to the maker's Garnet V2 search over a sibling training of Google's 31B (finding 147) |
| 6 | Tetratype/Gemma-4-26B-A4B-it-heretic-antislop | coder3101/gemma-4-26B-A4B-it-heretic | violations against `directional-per-layer-selected`, 46 flags (16 first shares, 15 layer cosines, 15 unexpected changes) | training on the attention outputs, dense and expert feed-forward tensors of layers 25 to 29 and the tied embedding, no direction, a float16 save (0.00000024 outside); coder3101's edit kept, the copy's difference from Google's at 1.0000 to it (finding 148) |
| 7 | DavidAU/Gemma-3-27b-it-Gemini-Heretic-Uncensored-Deeper-Reasoning-Series2 | coder3101/gemma-3-27b-it-heretic | violations against `single-projection`, 557 flags (308 unexpected changes, 124 first shares, 124 direction cosines, 1 cross-kind) | training on all seven linear maps of all 62 layers at 0.11 to 6.98 percent with two keys and values under the threshold (0.00085 outside), no direction; the maker's first pass contained in it at 0.82 to 0.96 with a second training at right angles (finding 149) |
| 8 | Naphula/Darkest-muse-v1-abliterated | sam-paech/Darkest-muse-v1 | match to `single-projection`, 0 flags | one direction projected out of both writers of all 42 layers at a flat 1.500 to 1.511, exactly 0 outside; the census's first Gemma 2 copy, with no measurement to stand against (finding 150) |

Nothing moved outside the matrices the maker's method reaches on any of the eight: the largest relative change
outside the changed set is exactly 0 on pairs 1, 2, 4 and 8, 0.000268 and 0.0000034 on pairs 3 and 5 (traced
attention outputs inside the windows), 0.00000024 on pair 6 (the float16 recast of the untouched tensors) and 0.00085
on pair 7 (two layer 1 projections the training left just under the threshold). All eight copies are what their cards
say, each read against the parent its card names: Heretic passes that read their cards' windows and kernels (pairs
1, 2, 3 and 5), a projection under a card that names grimjim's two posts (pair 4), a projection under a card that
names no method (pair 8), and two fine-tunes (pairs 6 and 7). The round's result for the method is pairs 6 and 7,
two trainings laid over Heretic edits. The antislop pass trains the last five layers and the tied embedding and moves
coder3101's edit by at most 0.00015 of itself along itself; the second reasoning pass trains every linear map, carries
the maker's first pass nearly whole and adds a second training at right angles to it, and moves the 27B edit back by
less than one percent of itself on the matrices read. Neither puts the edited direction back, the answer findings
138 and 142 gave on the two earlier trainings over edits where the question could be read.

The weights read off the weights. Three copies read kernels on the output side. coder3101's Magidonia pass reads both
printed kernels to the third decimal on all 32 matrices, as finding 135 read the same tool's record on Zephyr, and
the maker's Skyfall pass reads the kernels' reaches and the down kernel's shape, with the attention kernel's flat
1.48 read only on the fourteen inserted layers whose output projections the upscale left near zero (finding 143).
Naphula's projection reads a flat 1.5 on every writer. One reads a smooth shape the card does not print:
vprilepskii's projection at 1.364 to 1.443 on the down projections and 0.851 to 1.032 on the attention outputs. Two
read the arbitrary-rank branch on the input side: the PaintedFantasy search at 1.28 to 2.39 and the Garnet search at
1.64 to 3.44, no kept fraction of any saved component above 1.041 on either. Two carry no edit to read: the antislop
and reasoning fine-tunes, kept fractions near 1 on every layer matrix.

Preservation claims. One card names a row or norm preservation: vprilepskii's, by its name and its links to
grimjim's norm-preserving biprojection. The rows move by 0.0031 to 0.0178, through and over finding 22's band, as on
the edit of finding 130 under the same name, and by byte range the copy is a plain projection along its own
direction at its own weight to within 0.0026 to 0.0031 on three matrices, the rows moved as far as the plain
projection moves them; the columns, which the linked method normalises, hold within 0.00016 on 90 percent and move by
up to 0.0076 on the rest (finding 146). Naphula's card disclaims the norm-preserving form. The rows of the other
edits run 0.0022 to 0.0168 on the Skyfall pass, 0.0101 to 0.0705 on the Magidonia pass, 0.0016 to 0.0246 on the
PaintedFantasy search, 0.0017 to 0.3246 on the Garnet search and 0.0034 to 0.0317 on Naphula's projection, none under
a claim.

Fingerprints. Skyfall's 54 layers are Magistral Small's forty in order (layer 5 0.0153 from Magistral's, layers 30,
33, 48 and 53 0.019 to 0.024 from its 28, 29, 34 and 39) with seven pairs inserted after layers 27, 30, 33, 36, 39, 42
and 45, each copying the inputs of the layer before it (layer 28's queries 0.036 from Magistral's layer 27, layers 28
and 29 0.0035 apart) and carrying output projections of norm 0.23 to 0.41 and 1.07 to 1.15 against 9.9 to 20.6 and
36.8 to 47.3. Magidonia stands 0.0182 and 0.0269 from Magistral on the layer 5 queries and layer 30 attention output,
and coder3101's copy keeps its first three shards and its tenth by object id. PaintedFantasy is the passthrough its
card publishes (AntiRep's layers 0 to 28, then 10 to 39), trained apart afterward: its layer 29 stands 0.032 from
AntiRep's layer 10 and 0.035 from its own layer 10, its layer 5 0.0119 from AntiRep's, and AntiRep stands 0.0014 and
0.0031 from Mistral Small 3.2. vprilepskii's first shard is Harbinger's by object id. ConicCat's two Garnet versions
share their configuration, shard index, processor file and `tokenizer.json` by object id and stand 0.0434, 0.0425 and
0.0491 from each other on three matrices where each stands 0.029 to 0.033 from Google's, two adapters (rank 32 and
rank 64) trained side by side on Google's 31B. Tetratype's copy is coder3101's edit to the float16 rounding on every
layer from 0 to 24 and on the layer 20 attention output read by byte range. DavidAU's second pass shares its parent's
template, `tokenizer.json` and `tokenizer.model` by object id and adds a thinking template. Darkest-muse stands 0.0012
to 0.0032 from google/gemma-2-9b-it with no leading component, and Naphula's copy ships its parent's configuration,
index and token files by object id.

Directions. The round placed its edits against the saved vectors of earlier measurements without a download (finding
66's check): pairs 1 to 4 against the eleven Mistral Small 24B measurements with saved vectors and each other, by layer
number (Skyfall's and PaintedFantasy's depth changes noted below), pair 5 against the thirty-eight other 31B
measurements, pair 6 against the 26B-A4B measurements that share its names, pair 7 against Justbackup's measurement
of the maker's first pass and mlabonne's 27B projection, and pair 8 against none, since no measurement shares its
hidden size. coder3101's Skyfall pass stands at 0.817 to grayarea's text-only pass of Mistral Small 3.2 and 0.792 to
the same maker's Magistral pass, the two shared-direction passes, 0.586 to vprilepskii's edit, 0.544 to
SAIFIINDUSTRIES's Dolphin projection, 0.529 to the maker's Magidonia pass, 0.511 to venkycs's projection and 0.19 or
less to huihui-ai's projection and llmfan46's searches; matched by layer number past layer 27 it pairs Skyfall's
layers with shallower ones, and on layers 0 to 27 alone the first two numbers move by 0.003. The Magidonia pass stands
at 0.645 to Pranavz's Hearthfire pass, 0.529 to the Skyfall pass, 0.467 and 0.439 to grayarea's two passes and 0.38
or less to the rest. The PaintedFantasy search, whose window lies where the merge keeps AntiRep's numbering, stands at
0.836, 0.814 and 0.635 to the maker's first Magistral, Mistral Small 3.2 and second Magistral searches (0.903, 0.922
and 0.902 on the right) and 0.15 or less to every projection and kernel pass. vprilepskii's projection stands at
0.746 to venkycs's projection of Mistral Small 24B Instruct 2501, 0.660 and 0.621 to grayarea's two passes, 0.586 to
the Skyfall pass, 0.530 to SAIFIINDUSTRIES's and 0.383 to the Magidonia pass. llmfan46's Garnet search stands at 0.910
to the maker's 31B QAT search, 0.895 to coder3101's QAT edit, 0.883 to the maker's Garnet V2 search, 0.867 to
coder3101's 31B edit, 0.86 to the MeroMero edit and the Gembrain search, 0.839 to the Queen edit, 0.811 to the maker's
April edit, 0.709 to the Harmonia search and 0.18 or less to every kernel pass and projection. The antislop
training's leading vectors stand at 0.027 or less to every 26B-A4B measurement and 0.009 to coder3101's edit on the
five shared attention outputs. DavidAU's second pass stands at 0.491 on the left and 0.779 on the right to the first
pass on 418 shared names, and at 0.083 to mlabonne's projection.

## The token side

The cluster's cards read "consistent with re-save noted" on pairs 1, 2 and 7, "unexplained differences" on pairs 3,
4, 5 and 6 and "undecided" on pair 8, and the home judgement under transformers 5.22.1 with the parents' later commits
left all eight there, closing one field each on pairs 3 and 5. Pairs 1, 2 and 7 differ in version strings alone, with
the template and `tokenizer.json` the parent's by object id. Pair 3 is a transformers 5.3.0 save: the 354-byte
`tokenizer_config.json` drops the 1,000 `added_tokens_decoder` declarations (finding 44's form), the generation file
adds `pad_token_id` 11 and drops `do_sample`, `torch_dtype` is written as `dtype`, and the template is the parent's
with Windows line endings (2,722 bytes against 2,671), which the tool reads as equal. Pair 4 writes `torch_dtype` as
`dtype`, drops `_name_or_path` and moves the parent's 291-byte ChatML template into `chat_template.jinja`. Pair 5
carries the maker's 17,344-byte template of finding 134 over the parent's 12,045 bytes, put in by the same delete and
upload on 05-05 at 17:02Z, 24 seconds after it replaced the Garnet V2 copy's. Pair 6 is an Unsloth save in float16:
`eos_token_id` `[1, 106]` becomes 1, the generation list `[1, 106, 50]` becomes `[1, 1, 106, 50]`, `bos_token_id` and
`pad_token_id` are written at the top of the configuration, and `unsloth_version` and `model_name` are added. Pair 8
has no field that differs; neither side publishes a generation file, and the shared template refuses a system turn,
so the fixed conversation renders on neither side; rendered at home on a conversation without one, the two give the
same string. The token ids are the parents' on every pair (finding 100): Mistral's on pairs 1 to 3 (`bos_token_id` 1,
`eos_token_id` 2, `pad_token_id` 11 on the two Drummer pairs and added to pair 3's generation file, vocabulary
131,072), Harbinger's on pair 4 (`eos_token_id` 999, its `<|im_end|>`), the Gemma 4 instruct checkpoint's on pairs 5
and 6 (`eos_token_id` `[1, 106]`, generation `[1, 106, 50]`, `bos_token_id` 2, `pad_token_id` 0, vocabulary 262,144,
with pair 6's rewrite above), the Gemma 3 instruct checkpoint's on pair 7 (`[1, 106]`, vocabulary 262,208) and Gemma
2's on pair 8 (`bos_token_id` 2, `eos_token_id` 1, `pad_token_id` 0, vocabulary 256,000); no table is resized and
round 39's pretrained-checkpoint case does not recur.

## What the scorer learned

The flag counts are the same on the cluster and at home. Their causes, by pair:

- Training, 46 and 557 flags (pairs 6 and 7): unexpected changes on the readers and first shares and direction
  cosines on the writers; no entry reads training.
- A depth upscale under a shared-direction kernel pass, 47 flags (pair 1): first shares under the 0.99 floor on the
  down projections where the kernel's weight is small.
- Kernel and projection passes under the per-layer and single-projection entries, 18 and 58 flags (pairs 2 and 4):
  first shares of 0.907 to 0.988 under the floor.
- Arbitrary-rank searches under the per-layer entry, 11 and 16 flags (pairs 3 and 5): first shares of 0.75 to 0.97
  under the floor, the branch's own spread.
- None (pair 8): the single-projection entry reads Naphula's projection cleanly, as the per-layer entry read
  huihui-ai's two 12B projections in round 45.

The round's result for the measure is pair 1 against pair 2. The same maker, tool and kind of parent read two ways:
on a parent with Magistral's forty layers the printed kernels read to the third decimal, and on a parent that inserts
fourteen near-zero layers the printed heights read only there, so a kernel's heights are a reading of the parent's
writers as well as of the record.

## Owed to the metadata tool

What remains from round 47: the earlier-revision template and configuration through a snapshot older than the pin;
the declared-context line; the float16 `dtype` reading; the 5.16, 4.57.6, 5.8.0, 5.3.0 and 5.5.3 save forms as named
re-saves; the dropped-declarations rule through `tokenizer.json`; a maker's-template rule; the loader-moved-token and
missing-template lines of round 38; the pretrained-ids line of round 39; the special-flag line of round 41; the
Unsloth-parent line of round 42; the card-without-table line of round 43; the assistant-mask tag in the template
sandbox, the `quantization_config` line and the re-upload line of round 45; the `dtype` rename line, the
system-turn-free render, the added-generation-file line and the declared-against-stored `dtype` line of round 47. From
this round: the 5.3.0 save form a second time with the template's line endings rewritten (pair 3); the template moved
from `tokenizer_config.json` into `chat_template.jinja` as a named re-save (pair 4); the maker's template a seventh
time (pair 5); Unsloth's float16 save, which writes the tokenizer's end-of-sequence id alone into the configuration
and in front of the generation list (pair 6); and a missing generation file on both sides read as the parent's own,
so that a pair with no differing field is not left undecided (pair 8). To the recipe library: a shared-direction
kernel entry with a heights line (pair 1), a per-layer kernel entry with a heights line (pair 2), a column-norm line
for the method vprilepskii's card links (pair 4), an arbitrary-rank entry with a trace line (pairs 3 and 5), and a
training entry with an edit-kept line and a sibling-training line (pairs 6 and 7).

## Operational

The round ran on Wheat under the image-free kit with the standalone Python: one download, eight compares and the
sweep, every compare finishing with its card and its weights report, the sweep deleting the eight parents. Rounds 44,
46 and 48, pinned for Nautilus, are still on the cluster, so round 49 is read out before them. The pull (card 5840)
carries the eight measurement folders (card, metadata, weights, direction vectors and the sha256 record of each,
every checksum matching the file it names) and the sweep record; no job log was pulled, so the compares' nodes and
seconds are not recorded. The home judgement ran under transformers 5.22.1. One hundred and thirteen whole matrices
were read at home from the hub by byte range, five of them from the round 47 cache: the layer 27 to 30, 39 and 40
attention outputs and query projections of the Skyfall copy, Skyfall and Magistral Small 2509, with the layer 5, 28,
29, 30, 33, 48 and 53 query projections against Magistral's; the layer 5 query projection and layer 30 attention
output of the Magidonia copy, Magidonia and Magistral; the layer 5, 10, 29 and 58 query projections and layer 20
attention output of PaintedFantasy against the AntiRep model and Mistral Small 3.2; the layer 20 and 30 attention
outputs and layer 20 down projection of vprilepskii's copy and Harbinger; the layer 10, 30 and 40 attention outputs and
layer 5 query projection of the two Garnet versions and Google's 31B, and the layer 30, 37 and 44 attention outputs of
the two Garnet searches and their parents; the layer 20 and 25 to 29 attention outputs, layer 10 query projection and
token embedding of the antislop copy, coder3101's edit and Google's 26B-A4B; the layer 30 attention output, down and
query projections and layer 4 query projection of DavidAU's two passes, coder3101's 27B edit and Google's 27B; and the
layer 20 attention output and down projection and layer 5 query projection of Naphula's copy, Darkest-muse and
google/gemma-2-9b-it. The template of pair 8 was rendered at home through its own Jinja text on a conversation without
a system turn, and the templates of pairs 3 and 5 were compared byte for byte with the parents' and the maker's. The
hub's commit histories, file listings and cards were read for the eight copies and their eight parents, Magistral
Small 2509, Mistral Small 3.1 Instruct and 3.2, the AntiRep model, ConicCat's GarnetV2 and its adapter, the maker's
Garnet V2 search, DavidAU's first pass and Justbackup's duplicate, Google's Gemma 2 9B instruct checkpoint, and the
template history of pair 5. The byte-range cache is kept at `/var/tmp/permafrost-r49-rr` (9.0 GB). Two hundred and
thirty-three saved direction files were indexed across the pull copies of every round and one hundred and sixty-five
comparisons were made from them, listed in the reading notes.

Weight differences alone cannot certify the absence of hidden behavior.
