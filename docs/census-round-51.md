# Census round 51: eight edits on Wheat, two makers' Heretic passes on one Magistral Small fine-tune, a shared-direction pass of the earlier Skyfall, two Ministral 3 passes read against the pretrained bases their fields name and separated from the instruct checkpoints by byte range, a Mistral Small pass whose template tells the model to facilitate harmful requests, a pipeline's pass of the 26B-A4B, a training under an uncensored name and a rank-four edit over a fine-tune that stands on the instruct 26B-A4B

Eight published copies compared with their pinned originals on Wheat from the batch pinned as
`data/batches/round-51-batch-1.json` (pinned 2026-11-02 22:52Z) under the image-free kit with the standalone Python:
download job 387623, compares 387624 to 387631, sweep 387632, which deleted the eight originals (`fd028102` of
TheDrummer/Magidonia-24B-v4.3 at `5e5b5e15` for pair 1, `3dddfacc` of mistralai/Ministral-3-14B-Base-2512 at
`5b0ceedb` for pair 2, `c7dba84a` of TheDrummer/Skyfall-31B-v4.1 at `b41944d3` for pair 3, `6eaac59a` of
mistralai/Mistral-Small-3.2-24B-Instruct-2506 at `95a6d26c` for pair 4, `6f752cf5` of google/gemma-4-26B-A4B-it at
`4c55b528` for pair 5, `175cfc07` of unsloth/gemma-4-E4B-it at `4e22d7e5` for pair 6, `3f33f195` of
mistralai/Ministral-3-3B-Base-2512 at `6f9c4b12` for pair 7 and `bfa990fc` of google/gemma-4-26b-a4b at `24548b62`
for pair 8) from `/p/work/sdegan/model-audit/rounds/51/originals/`. The pull (card 5846) brought home the eight
measurement folders and the sweep record and no job log, so the compares' nodes and seconds are not in this note.
The batch note says what the round is: edits of community fine-tunes, of Mistral pretrained bases and of two Google
checkpoints, each measured against the parent its card or field names: grayarea's Heretic passes of TheDrummer's
Magidonia v4.3 and Skyfall v4.1, nchapman's passes of the two Ministral 3 instruct checkpoints, darkc0de's pass of
Mistral Small 3.2, keithtyser's pass of the 26B-A4B instruct checkpoint, AlSamCur123's "uncensored-continued" E4B and
OS-Software's CyberStag copy. nchapman's two copies name the instruct checkpoints in their cards and the pretrained
bases in their fields, so they are pinned against the bases and the read-out says what that shows; OS-Software's
copy names the pretrained 26B-A4B in its field. The note lists what was left out on the way (grayarea's Magistral
pass, measured in round 18; darkc0de's Mistral Small 4 119B, whose original is float8; two yamatazen merges whose
chains hold a base the lineage cannot place; DavidAU's 1B pass, whose name carries a restricted maker's model name;
and Jiunsong's 26B, whose declared parent the hub does not serve), and it records that no measured pair is repeated
and no copy duplicates a measured weight file by checksum. Two parents are unmeasured community fine-tunes
(TheDrummer's Magidonia and Skyfall v4.1) and one is unsloth's re-upload of the E4B instruct checkpoint, whose file is
Google's by object id; under the rule of finding 117 they count as neither originals nor copies. The other five
originals are publisher checkpoints, and three of them enter the census for the first time: the pretrained Ministral
3 14B and 3B and the pretrained Gemma 4 26B-A4B, each pinned from a field, and each the original of a copy that
stands on the instruct sibling (findings 153 and 158). All eight are first measurements of distinct copies. The
population comes to two hundred and forty-six measurements of two hundred and thirty-nine distinct copies on
thirty-seven originals: the round 49 header's numbers plus eight measurements, eight copies and three originals,
with thirty-five re-uploads among them. The eight measurements were re-scored at home with the recipe table as
committed and the saved direction vectors, and no flag count moved. Every metadata report was judged again at home
under transformers 5.22.1 with the originals' later commits; the home judgement closed
`config.text_config.rope_parameters` on pair 4 (the 5.x form of `rope_theta`) and twenty-two fields on pair 8 (the
text configuration a text-only save writes at the top level, read as defaults), and moved nothing on the other six;
no judgement changed. Each pair has a card (the tool's Stage 1 text after the home judgement, with the Stage 2 line)
and a reading note in `docs/cards/`; the measurements are in `results/weights/` and `results/meta/`, and the
direction vectors stay in the pull copy (`/opt/ai/hpc-packages/pulls/model-audit/wheat51/measurements/pair-N/`).

| Pair | Copy | Original | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | grayarea/Magidonia-24B-v4.3-heretic-v1.2 | TheDrummer/Magidonia-24B-v4.3 | violations against `directional-per-layer-selected`, 35 flags (first shares 0.961 to 0.990) | one shared direction on the down projections of layers 6 to 39 and the attention outputs of 11 to 39, the kernels' reaches; the down kernel read within 0.034, the attention kernel under its height, by 0.35 and 0.21 at layers 27 and 29; exactly 0 outside; at 0.574 to coder3101's pass of the same parent and 0.88 to the maker's Skyfall pass (finding 151) |
| 2 | nchapman/Ministral-3-14B-Instruct-2512-heretic-BF16 | mistralai/Ministral-3-14B-Base-2512 | violations against `single-projection`, 366 flags (204 unexpected changes, 81 first shares, 80 direction cosines, 1 cross-kind) | Mistral's instruction tuning on every linear map with the edit inside it; by byte range the instruct checkpoint the card names outside the kernels' reaches and a per-layer rank-one edit inside them, the printed kernels within 0.0044 on nine matrices (finding 153) |
| 3 | grayarea/Skyfall-31B-v4.1-Heretic-v1.2 | TheDrummer/Skyfall-31B-v4.1 | violations against `directional-per-layer-selected`, 95 flags (first shares 0.974 to 0.990, every changed matrix) | one shared direction on the down projections of layers 5 to 53 and the attention outputs of 8 to 53 in two kernel shapes no table prints, the fourteen inserted layers in line with their neighbours; exactly 0 outside; at 0.929 to coder3101's pass of Skyfall v4.2 on all 90 names (finding 152) |
| 4 | darkc0de/Mistral-Small-3.2-24B-Instruct-2506-heretic | mistralai/Mistral-Small-3.2-24B-Instruct-2506 | violations against `directional-per-layer-selected`, 12 flags (first shares 0.986 to 0.990) | one direction per layer on the attention outputs of layers 4 to 39 and the down projections of 8 to 38, the down kernel within 0.028, the attention kernel short by 0.26 and 0.17 at layers 27 and 29; exactly 0 outside; at 0.69 to 0.85 to the per-layer passes (finding 154); a template whose default system message tells the model to facilitate illegal and harmful requests (finding 155) |
| 5 | keithtyser/gemma-4-26B-A4B-it-local-abliterated-sota-internal-t34 | google/gemma-4-26B-A4B-it | violations against `directional-per-layer-selected`, 24 flags (16 first shares, 8 layer cosines) | one direction per layer on the dense writers of layers 12 to 29 in two kernel shapes no table prints, no expert; 0.00074 outside; at 0.85 to 0.90 to the Heretic and TrevorJS families (finding 156) |
| 6 | AlSamCur123/gemma-4-E4B-it-uncensored-continued | unsloth/gemma-4-E4B-it | violations against `single-projection`, 343 flags (174 unexpected changes, 84 first shares, 84 direction cosines, 1 cross-kind) | training on every linear map the text decoder uses at 0.5 to 7.7 percent, the unused shared-cache keys and values untouched, no direction; exactly 0 outside; at 0.042 or less to every measurement of the E4B (finding 157) |
| 7 | nchapman/Ministral-3-3B-Instruct-2512-heretic-BF16 | mistralai/Ministral-3-3B-Base-2512 | violations against `single-projection`, 201 flags (139 unexpected changes, 53 first shares, 8 direction cosines, 1 cross-kind) | Mistral's instruction tuning with the edit inside it; by byte range the instruct checkpoint outside the kernels' reaches and one shared direction inside them, 1.0000 on nine matrices, the printed kernels within 0.0045 (finding 153) |
| 8 | OS-Software/CyberStag-Security-26B-A4B-V1-Uncensored-Heretic | google/gemma-4-26b-a4b | violations against `single-projection`, 626 flags (444 unexpected changes, 91 first shares, 90 direction cosines, 1 cross-kind) | Google's instruction tuning with deer-sec's adapter and the edit inside it; by byte range deer-sec's fine-tune within 0.0014 of the instruct checkpoint, and the copy that fine-tune with a rank-four input-side edit inside the card's window from 12 to 20, layer 20 unchanged, at 0.69 to 0.80 to the maker's QAT edit (finding 158) |

Nothing moved outside the matrices the method reaches on the five pairs whose originals are the parents the edits
stand on: the largest relative change outside the changed set is exactly 0 on pairs 1, 3, 4 and 6 and 0.00074 on
pair 5 (the layer 11 down projection, the tail of a kernel). On the three pairs pinned against pretrained bases it is
0.00099, 0.00074 and 0.00084 (pairs 2, 7 and 8), on normalisation vectors the instruction tuning left just under the
threshold. All eight copies are what their cards say, read against the parents their cards name: four Heretic passes
whose printed kernels read (pairs 1, 2, 4 and 7), two Heretic passes under cards with no table (pairs 3 and 5), a
training under Unsloth's upload card (pair 6) and the maker's transport edit over the fine-tune its card names (pair
8). The round's result for the pinning is pairs 2, 7 and 8: three copies pinned from fields that name pretrained
bases stand on the instruct checkpoints, two of them under cards that say so and one through a parent whose own
field says otherwise, and in each the bytes separate the edit from the publisher's instruction tuning without a
download.

The weights read off the weights. Four copies read printed kernels on the output side. nchapman's 14B pass reads both
per-layer kernels within 0.0044 against the instruct checkpoint, and the 3B pass both shared-direction kernels within
0.0045, each a little under. grayarea's Magidonia pass reads its down kernel within 0.034 and darkc0de's within 0.028,
and both read their attention kernels under the printed height by up to a tenth, with the two largest shortfalls on
both at layers 27 and 29 (0.35 and 0.21, 0.26 and 0.17). keithtyser's pass reads two kernel shapes the card does not
print, 0.65 to 1.36 on the attention outputs and 0.04 to 0.80 on the dense down projections, and grayarea's Skyfall
pass two more, 0.60 to 1.00 and 0.69 to 0.86, with its fourteen inserted layers read within a tenth of their
neighbours. OS-Software's edit reads on the input side at 1.06 to 1.89 and rank four. AlSamCur123's copy carries no
edit to read.

Preservation claims. Three cards name a row normalisation: grayarea's two ("full row renormalization" under MPOA) and
keithtyser's ("full row normalization"). The rows move by 0.0019 to 0.0159 on the Magidonia pass, 0.0023 to 0.0086 on
the Skyfall pass and 0.0034 to 0.0258 on keithtyser's, in and over finding 22's band. OS-Software's card says
"none" and the rows move by 0.018 to 0.031. The rows of the passes under no claim run 0.0019 to 0.0380 on darkc0de's.

Fingerprints. Magidonia's and Skyfall v4.1's first shards are the copies' by object id, and Skyfall v4.1's last.
Skyfall v4.1 has v4.2's 54-layer layout, the two versions 0.020 to 0.030 apart on the forty Magistral layers and 1.26
apart on the inserted writers of layers 28 and 29; v4.1 stands 0.0139 from Magistral Small 2509 on the layer 5 query
projection. unsloth's Mistral Small 3.2 shards are Mistral's by object id, and unsloth's E4B file is Google's. The
Ministral 3 instruct checkpoints stand 0.070 to 0.091 from their pretrained bases on the attention outputs read, and
nchapman's copies are the instruct checkpoints byte for byte outside the kernels' reaches. deer-sec's fine-tune stands
0.00013 to 0.00135 from google/gemma-4-26B-A4B-it and byte-equal on its down projections, where the instruct and
pretrained 26B-A4B checkpoints stand 0.77 to 1.29 apart.

Directions. The round placed its edits against the saved vectors of earlier measurements without a download
(finding 66's check): pairs 1, 3 and 4 against the Mistral Small 24B measurements and each other, by layer number
(Skyfall's two versions share a layout), pair 5 against the 26B-A4B measurements, pair 6 against the forty-two E4B
measurements, pair 2 against the two other Ministral 3 14B measurements and by byte range against jenerallee78's
projection, pair 7 against none, since no measurement stands on Ministral 3 3B, and pair 8 from byte-range directions,
since its saved vectors read the instruction tuning. grayarea's Magidonia pass stands at 0.882 to the maker's Skyfall
pass, 0.829 to coder3101's Skyfall pass, 0.774 and 0.691 to the maker's text-only and Magistral passes and 0.574 to
coder3101's pass of the same parent. The Skyfall pass stands at 0.929 to coder3101's v4.2 pass and 0.870 and 0.759 to
the maker's text-only and Magistral passes. darkc0de's pass stands at 0.847 and 0.764 to Pranavz's two measurements,
0.685 to coder3101's Magidonia pass, 0.41 to 0.46 to the five shared-direction passes and 0.161 and 0.076 to
huihui-ai's projection and llmfan46's search of the same checkpoint. keithtyser's pass stands at 0.85 to 0.90 to
tvall43's, sh0ck0r's, BinxNet's, SevenOfNine's, TrevorJS's, xdavxd's and Rootkit7's edits and 0.21 or less to every
arbitrary-rank search. AlSamCur123's training stands at 0.042 or less to every measurement of the E4B. nchapman's 14B edit
stands at 0.51 to 0.76 to jenerallee78's projection of the same checkpoint by byte range, and OS-Software's edit at
0.69 to 0.80 to the maker's QAT edit.

## The token side

The cluster's cards read "consistent with re-save noted" on pair 1 and "unexplained differences" on the other seven,
and the home judgement under transformers 5.22.1 with the originals' later commits left all eight there, closing one
field on pair 4 and twenty-two on pair 8. Pair 1 differs in version strings alone, with the template,
`tokenizer_config.json` and special-token map the parent's by object id. Pair 3 adds a `grayarea` block to
`config.json` naming the run's configuration and dataset ("heretic: gemma-3-27b-v1", "heretic: gemma-3-v2"); its
template and token files are the parent's by object id. Pairs 2 and 7 carry the instruct checkpoints' templates and
token files by object id over pretrained bases that publish no template, so `template.default` reads as an
unexplained addition. Pair 4's original publishes `tekken.json` and no transformers token files or template, so the
copy's 1,000 declared special tokens, ids and template read as additions; its template was uploaded as Unsloth's and
replaced four minutes later by one whose default system message is a persona told to obey all commands and
facilitate illegal and harmful requests, which the fixed conversation, opening with a system turn, does not render
(finding 155). Pair 5's template is Google's own of 04-10, older than the pinned 04-28 revision. Pair 6 is an Unsloth
save with a 2,375-byte template found in no revision of the parent or Google's checkpoint, rendering the fixed
conversation the same. Pair 8 is a text-only `Gemma4ForCausalLM` save with the instruct checkpoint's `tokenizer.json`
by object id and its stop list `[1, 106, 50]` where the pretrained checkpoint's generation file ends on 1. The token
ids are the parents' on every pair read against its parent (finding 100): Mistral's on pairs 1, 3 and 4
(`bos_token_id` 1, `eos_token_id` 2, `pad_token_id` 11, vocabulary 131,072), the instruct checkpoint's on pairs 5
and 6 (`eos_token_id` `[1, 106]`, generation `[1, 106, 50]`, `bos_token_id` 2, `pad_token_id` 0, vocabulary
262,144); and on the three pairs pinned against pretrained bases the copies carry the instruct checkpoints' ids,
equal to the bases' on the two Ministral 3 pairs and differing in the stop list on pair 8. No table is resized.

## What the scorer learned

The flag counts are the same on the cluster and at home. Their causes, by pair:

- The publisher's instruction tuning under a pin from a field, 366, 201 and 626 flags (pairs 2, 7 and 8): unexpected
  changes on every reader and first shares and direction cosines on the writers.
- Training, 343 flags (pair 6): the same pattern, from an adapter on every map the forward pass uses.
- Shared-direction passes under the per-layer entry, 35 and 95 flags (pairs 1 and 3): first shares under the 0.99
  floor where the kernel's weight is small.
- Per-layer passes, 12 and 24 flags (pairs 4 and 5): first shares under the floor, and on pair 5 layer cosines where
  the down weight falls to 0.04.

The round's result for the measure is pair 4 against pair 1 and coder3101's pass of round 49: two Heretic 1.2 runs
on Mistral Small derivatives read their down kernels to the second decimal and fall short of their attention
kernels at the same two layers, where a Heretic 1.1 run on one of the same parents read its attention kernel to the
third decimal, so a heights line has to carry the tool's version.

## Owed to the metadata tool

What remains from round 49: the earlier-revision template and configuration through a snapshot older than the pin;
the declared-context line; the float16 `dtype` reading; the 5.16, 4.57.6, 5.8.0, 5.3.0 and 5.5.3 save forms as named
re-saves; the dropped-declarations rule through `tokenizer.json`; a maker's-template rule; the loader-moved-token and
missing-template lines of round 38; the pretrained-ids line of round 39; the special-flag line of round 41; the
Unsloth-parent line of round 42; the card-without-table line of round 43; the assistant-mask tag in the template
sandbox, the `quantization_config` line and the re-upload line of round 45; the `dtype` rename line, the
system-turn-free render, the added-generation-file line and the declared-against-stored `dtype` line of round 47; the
5.3.0 save with rewritten line endings, the template moved into `chat_template.jinja`, the maker's template a seventh
time, Unsloth's float16 save and a missing generation file on both sides of round 49. From this round: the
system-turn-free render a second time and now with content, a default system message replaced (pair 4); the
earlier-revision template on a copy uploaded after the pin (pair 5); a comparison against the instruct checkpoint's
files when the original publishes none in transformers form, as Mistral's tekken-only and pretrained repositories do
(pairs 2, 4 and 7); a maker's block in `config.json` read as the run's record (pair 3); and the text-only save of a
multimodal checkpoint read as one form (pair 8). To the recipe library: a shared-direction kernel entry and a
per-layer kernel entry with a heights line that carries the tool's version (pairs 1, 3 and 4); a per-layer entry
with no expert and a dense-down kernel (pair 5); a training entry with a used-maps line (pair 6); the transport
entry of finding 42 (pair 8). To the pinner: a pair whose card names a parent its field does not is pinned against
the card's parent when the hub serves it in safetensors form (pairs 2, 7 and 8), and a parent's tokenizer and
generation files are checked against the publisher's instruct and pretrained checkpoints before an original is
chosen (pair 8).

## Operational

The round ran on Wheat under the image-free kit with the standalone Python: one download, eight compares and the
sweep, every compare finishing with its card and its weights report, the sweep deleting the eight originals. Rounds
44, 46, 48 and 50, pinned for Nautilus, are still on the cluster, so round 51 is read out before them. The pull (card
5846) carries the eight measurement folders (card, metadata, weights, direction vectors and the sha256 record of
each, every checksum matching the file it names) and the sweep record; no job log was pulled, so the compares' nodes
and seconds are not recorded. The home judgement ran under transformers 5.22.1. One hundred and forty-seven whole
matrices were read at home from the hub by byte range, twelve of them from the round 49 cache, with the first four
megabytes of fourteen more: the layer 20, 27, 30 and 33 writers and the layer 5 query projection of grayarea's and
coder3101's Magidonia passes and Magidonia; the layer 5 and 28 query projections and the layer 27 to 30 attention
outputs of Skyfall v4.1 and v4.2, the layer 27 to 30 attention outputs of the two Skyfall passes and the
layer 5 query projection of grayarea's, and Magistral's layer 5 and 28 query projections; the writers of layers 5, 10, 11, 20, 22, 28, 30, 33, 35
and 39 and the layer 20 query and gate projections of nchapman's 14B copy and the instruct checkpoint at `847d2b6b`,
two of them against the pretrained base and three against jenerallee78's projection; the writers of layers 2, 3, 4,
10, 15, 16, 20 and 25 and the layer 15 query and gate projections of the 3B copy and the instruct checkpoint at
`ecc3ba8b`, two against the pretrained base; and the layer 10, 11, 12, 15, 20 and 21 attention outputs, the layer 11,
12, 15, 20, 21 and 25 down projections and the layer 5 query projection of OS-Software's copy and deer-sec's
fine-tune, with google/gemma-4-26B-A4B-it on seven of them and google/gemma-4-26b-a4b on five. The heads were the token
embeddings, output heads, projectors and final normalisations of the two Ministral 3 copies and their instruct
checkpoints. The templates of pair 4 and Unsloth's were rendered at home on the fixed conversation and on a
conversation without a system turn, and the templates of pairs 4, 5 and 6 were traced through every commit of the
copy, the parent and Google's or Unsloth's repository. The hub's commit histories, file listings and cards were read
for the eight copies, the eight originals, the instruct checkpoints of Ministral 3 at the copies' upload, unsloth's
Mistral Small 3.2, google/gemma-4-E4B-it and google/gemma-4-26B-A4B-it, deer-sec's fine-tune, TheDrummer's Skyfall
v4.2 and jenerallee78's edit. The byte-range cache is kept at `/var/tmp/permafrost-r51-rr` (8.2 GB). Two hundred and
forty-one saved direction files were indexed across the pull copies of every round, and the comparisons made from
them are listed in the reading notes.

Weight differences alone cannot certify the absence of hidden behavior.
