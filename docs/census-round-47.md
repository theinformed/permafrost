# Census round 47: eight second-generation edits on Wheat beyond the instruct lines, a Zephyr pass read to its published kernels, a circuit breaker stripped back to Mistral's instruct model before its edit, a text-only re-save that is Mistral's checkpoint, two fine-tunes that leave the edits under them in place, a pruned 21B-A4B, and one maker's two 31B searches, one over a merge that carries the other (2026-11-02)

Eight published copies compared with the parents their cards name on Wheat from the batch pinned as
`data/batches/round-47-batch-1.json` (pinned 2026-11-02 09:57Z) under the image-free kit with the standalone
Python: download job 387398, compares 387399 to 387406, sweep 387407, which deleted the eight parents (`35721988` of
HuggingFaceH4/zephyr-7b-beta at `892b3d7a` for pair 1, `f2804e89` of GraySwanAI/Mistral-7B-Instruct-RR at
`5b9121da` for pair 2, `73cf896b` of anthracite-core/Mistral-Small-3.2-24B-Instruct-2506-Text-Only at `c5ac8f3b` for
pair 3, `0788671a` of jwest33/gemma-3-4b-it-null-space-abliterated at `3d50eeaa` for pair 4, `bd3ba5d4` of
0xSero/Gemma-4-21B at `e5921d70` for pair 5, `4a4e0c91` of Nimbz/Gemma-4-Gembrain-31B at `6c8b9228` for pair 6,
`d53f7513` of virtuous7373/Gemma-4-Harmonia-31B at `874d478b` for pair 7 and `8229bd07` of
coder3101/gemma-4-31B-it-heretic at `9a1c7f5d` for pair 8) from `/p/work/sdegan/model-audit/rounds/47/originals/`.
The pull (card 5829) brought home the eight measurement folders and the sweep record and no job log, so the
compares' nodes and seconds are not in this note. The batch note says what the round is: the fourth from the
second-generation pool, abliteration and Heretic edits of community fine-tunes and of measured copies, each
measured against the parent its card names, and the first to reach outside the Gemma and Mistral instruct lines:
Zephyr, a circuit-breaker Mistral 7B, a text-only re-save of Mistral Small 3.2, a pruned Gemma 4 21B-A4B and a
fine-tune applied on top of a measured Heretic edit, beside llmfan46's edits of two Gemma 4 31B merges and
jwest33's fine-tune over the maker's null-space edit of Gemma 3 4B. It records that no measured pair is repeated
and no copy duplicates a measured weight file by checksum, and that DavidAU's Gemma 3 27B reasoning pass was refused
on the way because its weight files are the ones Justbackup's copy carries, the duplicate pinned in round 42
(finding 121), so the pinner's checksum rule kept a second measurement of one file out of the batch. Against the
parent its card names a copy reads the edit alone, and the parent's own distance from the publisher's checkpoint
is read by byte range where the note needs it. The population rule of finding 117 applies: a community parent
counts as neither an original nor a copy, so the originals stay the publisher's thirty-four checkpoints and a
parent enters the copy count only when it is itself measured against its own parent. The rule covers two parents
the pinner marks as roots of their chains, Zephyr (its card names Mistral 7B v0.1 as its base) and GraySwanAI's
model (whose configuration names Mistral 7B Instruct v0.2 and whose card names no base); neither is a publisher's
checkpoint, and neither enters the original count. Six parents are unmeasured community repositories, pair 4's an
unmeasured first edit, and pair 8's is coder3101's 31B edit, a copy the census already counts, measured in round
12 against Google at this revision with these two shards. All eight are first measurements of distinct copies. The
population comes to two hundred and thirty measurements of two hundred and twenty-three distinct copies on
thirty-four originals: the round 45 header's numbers plus eight measurements and eight copies, with thirty-five
re-uploads among them. The eight measurements were re-scored at home with the recipe table as committed and the
saved direction vectors, and no flag count moved. Every metadata report was judged again at home under
transformers 5.22.1 with the parents' later commits; the home judgement closed `config.head_dim` and
`config.rope_parameters` on pair 2 (absent on one side and loaded as the same value) and moved nothing on the other
seven; no judgement changed. Each pair has a card (the tool's Stage 1 text after the home judgement, with the Stage
2 line) and a reading note in `docs/cards/`; the measurements are in `results/weights/` and `results/meta/`, and
the direction vectors stay in the pull copy (`/opt/ai/hpc-packages/pulls/model-audit/wheat47/measurements/pair-N/`).

| Pair | Copy | Parent | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | richardyoung/zephyr-7b-beta-abliterated | HuggingFaceH4/zephyr-7b-beta | violations against `directional-per-layer-selected`, 5 flags (first shares 0.956 to 0.989) | the down projections of layers 10 to 27 and the attention outputs of 20 to 28, one direction per layer on the output side, Heretic 1.1's two published kernels read within 0.0011 and 0.0029, exactly 0 outside; no measurement stands on Zephyr, and the direction stands at 0.48 to 0.63 to the Mistral 7B v0.3 edits (finding 135) |
| 2 | wangzhang/Mistral-7B-Instruct-RR-Abliterated | GraySwanAI/Mistral-7B-Instruct-RR | violations against `single-projection-selected`, 215 flags (138 unexpected changes, 41 first shares, 35 direction cosines, 1 cross-kind) | 200 of 291 changed, 118 of them only the circuit breaker's rank-16 adapter removed, the copy Mistral 7B Instruct v0.2's bytes there; the edit on the other 82: one direction on the attention outputs of 5 to 31, the down projections of 23 to 31 and the input side of the keys and values of 16 to 31 at weights to 5.62, and the queries of 18 to 31 on a direction of their own; exactly 0 outside (finding 136) |
| 3 | grayarea/Mistral-Small-3.2-24B-Instruct-2506-Text-Only-Heretic-v1.2 | anthracite-core/Mistral-Small-3.2-24B-Instruct-2506-Text-Only | violations against `directional-per-layer-selected`, 26 flags (first shares 0.979 to 0.990) | one shared direction on the down projections of layers 8 to 39 and the attention outputs of 11 to 39, weights 0.68 to 1.27 in a kernel's shape, rows 0.0023 to 0.0078 under a card naming full row renormalization, exactly 0 outside; the parent Mistral's checkpoint by byte range; at 0.856 to the maker's Magistral pass (finding 137) |
| 4 | jwest33/gemma-3-4b-null-space-abliterated-RP-writer | jwest33/gemma-3-4b-it-null-space-abliterated | violations against `single-projection`, 302 flags (165 unexpected changes, 68 first shares, 68 direction cosines, 1 cross-kind) | training on all seven linear maps of all 34 layers at 0.10 to 0.71 percent with five key projections under the threshold (0.00099 outside), the vision tower and the embedding exactly 0, no direction, the training at the level of chance to the maker's published direction; the parent's edit rank one by byte range (finding 138) |
| 5 | coder3101/gemma-4-21b-a4b-it-REAP-heretic | 0xSero/Gemma-4-21B | violations against `directional-per-layer-selected`, 19 flags (first shares 0.391 to 0.919) | the arbitrary-rank branch on the attention outputs of layers 11 to 29, the card's window, input-side weights 0.59 to 1.34, rows 0.0061 to 0.0077 in the band, exactly 0 outside and on every expert; the parent's attention outputs Google's bytes; at 0.898 to the maker's 26B-A4B edit (finding 139) |
| 6 | llmfan46/Gemma-4-Gembrain-31B-it-uncensored-heretic | Nimbz/Gemma-4-Gembrain-31B | violations against `directional-per-layer-selected`, 31 flags (first shares 0.905 to 0.972) | the branch on 31 attention outputs of layers 21 to 58 under a card from 5 to 60, thirteen more traced (0.000176 outside), input-side weights 0.24 to 3.17, no component amplified; a bfloat16 save of a float32 parent; at 0.886 to 0.908 to the maker's April, Queen and MeroMero edits and coder3101's (finding 140) |
| 7 | llmfan46/Gemma-4-Harmonia-31B-uncensored-heretic | virtuous7373/Gemma-4-Harmonia-31B | violations against `directional-per-layer-selected`, 22 flags (first shares 0.891 to 0.975) | the branch on 22 attention outputs of layers 26 to 54, the rest of the card's window from 14 to 54 traced (0.000234 outside), input-side weights 0.22 to 2.20, no component amplified; over a merge of the maker's own edits whose leading component stands at 0.876 and 0.930 to pair 6's edit; at 0.60 to 0.80 to the maker's searches (findings 140 and 141) |
| 8 | nbeerbower/Gemma4-Gutenberg-31B-Heretic | coder3101/gemma-4-31B-it-heretic | violations against `single-projection-selected`, 459 flags (262 unexpected changes, 98 first shares, 98 direction cosines, 1 cross-kind) | training on 360 linear maps of the text decoder at 0.10 to 0.77 percent with 50 more under the threshold (0.000999 outside), the vision tower exactly 0, no direction; the maker's standard adapter merged onto the measured edit, the change equal to the standard Gutenberg's at 0.994 and 0.997 and the edit kept to 0.00002 of itself (finding 142) |

Nothing moved outside the matrices the maker's method reaches on six of the eight: the largest relative change
outside the changed set is exactly 0 on pairs 1, 2, 3 and 5, 0.000176 on pair 6 and 0.000234 on pair 7 (traced
attention outputs inside the windows), and 0.00099 and 0.000999 on the two fine-tunes, pairs 4 and 8, whose training
leaves five and fifty linear maps just under the threshold. All eight copies are what their cards say, each read
against the parent its card names: Heretic passes that read their cards and records (pairs 1, 3, 5, 6 and 7),
abliterix's two steps as its card prints them (pair 2), and two adapters merged as their cards describe (pairs 4 and
8). The round's result for the method is pairs 1 and 2, the first two copies outside the Gemma and Mistral instruct
lines. On Zephyr, a preference-tuned fine-tune of Mistral 7B v0.1 that no other measurement stands on, Heretic 1.1's
per-layer pass reads its two kernels from the published `abliteration_info.json` to the third decimal on all 27
matrices, the windows to the layer and nothing else moved, so a new line reads as the instruct lines do when the
record is published. On GraySwanAI's circuit-breaker model the measurement against the parent reads 200 matrices and
215 flags, and the bytes say why: 118 of them are the parent's rank-16 adapter removed to the last bit, the copy
Mistral 7B Instruct v0.2's bytes there, and the edit on the other 82 is a single-direction projection like any
other, rank one at 0.997 to 0.9997 on the layers the adapter never touched. The circuit breaker left no residue of
its own in the edit; it is gone because the card's first step subtracts it. A representation-rerouting defence
published as an adapter on a public checkpoint is, to this measurement, a difference from that checkpoint, and the
census can read it, and its removal, only when it pairs the copy with the checkpoint underneath.

The weights read off the weights. Two copies read kernels on the output side: the Zephyr pass at 1.158 to 1.490
on the down projections and 0.335 to 1.297 on the attention outputs, within 0.0011 and 0.0029 of the published
kernels, and grayarea's text-only pass at 0.69 to 1.27 on the down projections and 0.68 to 1.25 on the attention
outputs, a kernel's shape under a card that prints no table. One reads a linear kernel at large weights: the
abliterix edit at 5.62 at layer 22 falling by 0.245 to 0.25 a layer on the attention outputs, 1.84 to 1.95 on the
down projections, 1.88 to 2.76 on the input side of the keys and values and 2.49 to 2.99 on the output side of
the queries, inside the card's strength range of 1.5 to 6.0. Three read the arbitrary-rank branch on the input
side: coder3101's REAP pass at 0.59 to 1.34, llmfan46's Gembrain search at 0.24 to 3.17 and the Harmonia search at
0.22 to 2.20, no kept fraction above 1 on either side of any of the three. Two carry no edit to read: the RP-writer
and the Gutenberg fine-tunes, both kept fractions near 1 on every matrix.

Preservation claims. Two cards in the round name a row preservation. coder3101's REAP card names Heretic's row-norm
preservation and the rows move by 0.0061 to 0.0077, finding 22's band on all 19 matrices, as on the maker's other
arbitrary-rank edits. grayarea's card names MPOA and full row renormalization and the rows move by 0.0023 to 0.0078,
in and under the band, as the maker's Magistral pass read 0.0026 to 0.0107 under the same words (finding 31).
jwest33's parent card names Frobenius-norm preservation, which the rows do not measure (finding 94). No other card
claims a norm. The rows of the other edits run 0.0072 to 0.0325 on the Zephyr pass, 0.005 to 0.178 on the abliterix
edit (0.048 to 0.178 on the attention outputs), 0.0007 to 0.0355 on the Gembrain search and 0.0008 to 0.0215 on the
Harmonia search.

Fingerprints. The Zephyr copy's layer 5 query projection is Zephyr's bytes and Zephyr stands 0.034 to 0.044 from
Mistral 7B v0.1 on the three matrices read with no leading component. GraySwanAI's model is Mistral 7B Instruct v0.2
at `63a8b081` on layers 21 to 31 byte for byte and on layers 0 to 20 that model plus an adapter whose sixteen
components carry 0.985 to 0.990 of the change on the three matrices read; the copy's gate and up projections of
every layer, its down projections of 0 to 22, queries of 0 to 17, keys and values of 0 to 15 and attention outputs
of 0 to 4 equal the instruct model's on the first 2,000,000 bytes, and the layer 10 gate and query projections are
byte-equal whole. The copy's `tokenizer.json` (`780dd6a1`) is the file the Zephyr copy carries. anthracite-core's
text-only parent is mistralai/Mistral-Small-3.2-24B-Instruct-2506 at `95a6d26c` on the layer 20 attention output,
the layer 5 query projection and the token embedding byte for byte, and grayarea's copy keeps the parent's tokenizer
and special-token map by object id. jwest33's RP-writer ships the parent's `abliteration_config.json`,
`refusal_directions.pt` and `null_space_projectors.pt` by object id, and its token embedding is the parent's
bytes; the parent stands 0.0152 to 0.0220 from google/gemma-3-4b-it on the layer 20 attention output, down and
query projections and the embedding, each difference rank one (first shares 0.990 to 0.995), and 0.0022 on the
layer 5 gate projection. 0xSero's 21B and 19B REAP checkpoints carry Google's 26B-A4B attention outputs byte for
byte on the five layers read. The Gembrain parent is 27 float32 shards under a configuration that declares
bfloat16; it stands 0.0088 and 0.0098 from Google's on the layer 40 and 48 attention outputs and 0.00016 on layer
10, with no leading component. The Harmonia parent stands 0.0818, 0.0698 and 0.0609 from Google's on the same three,
the first two with a leading component at 0.876 and 0.930 to the Gembrain edit's. nbeerbower's two Gutenberg copies
share their configuration (`20dfb9ad`) and index by object id, and on the layer 30 query projection, where
coder3101's matrix is Google's bytes, they are byte-equal to each other.

Directions. The round placed its edits against the saved vectors of earlier measurements without a download (finding
66's check): pairs 1 and 2 against the seven Mistral 7B measurements and each other, the only ones whose hidden size
(4,096) and layer count match, pair 3 against the ten Mistral Small 24B measurements with saved vectors, pair 4
against the one other Gemma 3 4B measurement, pair 5 against the thirty-three 26B-A4B measurements, whose attention
outputs have the pruned checkpoint's shape, and pairs 6 to 8 against the thirty-seven other 31B measurements. The
Zephyr pass stands on the left at 0.631 to evolveon's projection of Mistral 7B Instruct v0.3, 0.627 to the maker's
own v0.3 edit, 0.559 to DogOnKeyboard's, 0.546 to paoloronco's, 0.485 and 0.484 to 3MPER0RR's two measurements,
0.357 to the abliterix edit and 0.047 to the maker's OBLITERATUS copy of v0.2. The abliterix edit, on the 32
attention outputs, stands at 0.733 to 3MPER0RR's measurement against the instruct v0.3 model, 0.674 to paoloronco's,
0.648 to DogOnKeyboard's, 0.555 to richardyoung's v0.3 edit, 0.549 to evolveon's, 0.397 to the Zephyr pass and 0.012
to the OBLITERATUS copy, the one other edit of Mistral 7B Instruct v0.2. grayarea's text-only pass stands at 0.856
and 0.857 to the maker's Magistral Small 2509 pass (59 names, minimum 0.854), 0.628 to saukko's Dolphin R1
projection, 0.533 to venkycs's Mistral Small 24B projection, 0.398 and 0.370 to Pranavz's Hearthfire pass, 0.235 to
huihui-ai's Mistral Small 3.2 projection and nicoboss's duplicate, and 0.06 or less to llmfan46's three searches on
Mistral Small 3.2 and Magistral; the two calibration edits of Mistral Small 3.2 have no saved vectors at home and
were not compared. The RP-writer's vectors stand at 0.079 to DavidAU's 4B fine-tune, two trainings with nothing to
share. coder3101's REAP pass stands at 0.898 to the maker's own 26B-A4B edit (19 names, minimum 0.646), to
SassyDiffusion's search and to SubMaroon's body, 0.890 to llmfan46's MeroMero 26B-A4B edit, 0.862 to the maker's
April 26B-A4B edit, 0.858 to Vortex5's Chimera-X edit, 0.841 and 0.825 to the two QAT edits, and 0.20 or less to
every kernel pass and projection. llmfan46's Gembrain search stands at 0.908 to the maker's Queen edit, 0.896 to
coder3101's 31B edit, 0.888 to the MeroMero edit, 0.886 to the maker's April edit and coder3101's QAT edit, 0.883 to
the maker's QAT search, 0.819 to the Garnet search, 0.731 to the Harmonia search and 0.601 to Jim-darby's
Japanese-weighted search; the Harmonia search at 0.797 to the maker's QAT search, 0.731 to the Gembrain search,
0.713 to the Garnet search, 0.670 to the MeroMero edit, 0.634 to the Queen edit and 0.602 to the April edit and
coder3101's 31B edit; both at 0.21 or less to every kernel pass and projection. The Gutenberg training's leading
vectors stand at 0.028 or less to every 31B edit on the attention outputs and 0.010 to coder3101's.

## The token side

The cluster's cards read "unexplained differences" on pairs 1, 2, 3, 4, 6 and 7 and "consistent with re-save noted"
on pairs 5 and 8, and the home judgement under transformers 5.22.1 with the parents' later commits left all eight
there, closing two fields on pair 2. Three pairs write `torch_dtype` as `dtype` with the same value (pairs 1, 2 and
3), which the tool reads as two changed fields. Pair 1 writes the special-token map as objects where Zephyr writes
strings, the same tokens and ids, and adds `do_sample` to the generation file. Pair 2 is a transformers 5.5.3 save
of a 4.40.0 parent: the three `added_tokens_decoder` entries and the empty `additional_special_tokens` list are
dropped, `rope_theta` becomes `rope_parameters`, and the template moves into `chat_template.jinja` with the parent's
text; Mistral's v0.2 template refuses a system turn, so the fixed conversation renders on neither side and the card
lists the render as missing evidence, and rendered at home on a conversation without one the two give the same
string. Pair 4's template (1,581 bytes against the parent's 1,579) differs beyond line endings and renders
identically, and the copy drops the parent's `cache_implementation: hybrid`. Pairs 6 and 7 add a generation file
where the parent publishes none, and both carry the maker's 17,344-byte template of finding 134 with Windows line
endings (17,708 bytes, `60103108`): on pair 6 over Google's 04-28 revision, a template change the fixed conversation
renders identically, and on pair 7 over a parent that already carries the 17,344-byte file through its merge, which
the tool reads as equal after line endings. The same 17,708-byte file went onto the maker's April 31B repository on
05-18 and was replaced there fourteen minutes later. Pair 8's template and tokenizer are coder3101's by object id.
The token ids are the parents' on every pair (finding 100): Zephyr's on pair 1 (`bos_token_id` 1, `eos_token_id` 2,
`pad_token_id` 2), Mistral's on pairs 2 and 3 (`bos_token_id` 1, `eos_token_id` 2, no pad; vocabularies 32,000 and
131,072), the Gemma 3 instruct checkpoint's on pair 4 (`eos_token_id` `[1, 106]`, `bos_token_id` 2, `pad_token_id`
0, vocabulary 262,208), and the Gemma 4 instruct checkpoint's on pairs 5 to 8 (`eos_token_id` `[1, 106]`, generation
`[1, 106, 50]` on pairs 5 and 8 and `[1, 106]` in the generation files pairs 6 and 7 add, `bos_token_id` 2,
`pad_token_id` 0, vocabulary 262,144); no table is resized and round 39's pretrained-checkpoint case does not recur.

## What the scorer learned

The flag counts are the same on the cluster and at home. Their causes, by pair:

- A strip under an edit, 215 flags (pair 2): 138 unexpected changes, 41 first shares and 35 direction cosines on
  the matrices where the parent's adapter was removed; measured against the instruct model underneath, the pair
  would read 82 matrices of one projection.
- Training, 302 and 459 flags (pairs 4 and 8): unexpected changes on the readers and first shares and direction
  cosines on the writers of two merged adapters; no entry reads training.
- Kernel passes under the per-layer entry, 5 and 26 flags (pairs 1 and 3): first shares under the 0.99 floor on
  the matrices where the kernel's weight is small (pair 1) or across a shared direction under a row
  renormalisation (pair 3).
- Arbitrary-rank searches under the per-layer entry, 19, 31 and 22 flags (pairs 5, 6 and 7): first shares of 0.39
  to 0.98 under the floor, the branch's own spread.

The round's result for the measure is pair 2 against pair 8. On a parent that is a defence trained into a public
checkpoint, the pair the card names reads the removal of that training as most of the change, and only a second
pairing with the checkpoint underneath reads the edit; on a parent that is a measured edit, the pair reads the
training alone and the saved vectors and the bytes read the edit as kept. Both are second-generation pairs, and the
census needs the grandparent pairing on the first kind and not on the second.

## Owed to the metadata tool

What remains from round 45: the earlier-revision template and configuration through a snapshot older than the pin;
the declared-context line; the float16 `dtype` reading; the 5.16, 4.57.6, 5.8.0 and 5.3.0 save forms as named
re-saves; the dropped-declarations rule through `tokenizer.json`; a maker's-template rule (pairs 6 and 7, the fifth
and sixth of the maker's repositories in the census to carry the file, now with Windows line endings); the
loader-moved-token and missing-template lines of round 38; the pretrained-ids line of round 39; the special-flag line
of round 41; the Unsloth-parent line of round 42; the card-without-table line of round 43; the assistant-mask tag in
the template sandbox, the `quantization_config` line and the re-upload line of round 45. From this round: a rename
line for `torch_dtype` written as `dtype` (pairs 1 to 3); a render that falls back to a conversation without a
system turn when a template refuses one (pair 2); the 5.5.3 save form, which drops the `added_tokens_decoder` block
(pair 2); a generation file added where the parent publishes none (pairs 6 and 7); and a line that reads a
configuration's declared `dtype` against the stored type of the shards (pair 6's parent). To the recipe table: a
kernel line that reads a published Heretic record (pair 1), a strip line that pairs a copy with the checkpoint under
an adapter its card or configuration names (pair 2), a shared-direction entry on both writers with a kernel line
and a row-normalisation line (pair 3), a training entry with an edit-kept line for a parent that is itself a
measured edit (pairs 4 and 8), and an arbitrary-rank entry with a trace line (pairs 5 to 7).

## Operational

The round ran on Wheat under the image-free kit with the standalone Python: one download, eight compares and the
sweep, every compare finishing with its card and its weights report, the sweep deleting the eight parents. Rounds 44
and 46, pinned for Nautilus, are still on the cluster, so round 47 is read out before them. The pull (card 5829)
carries the eight measurement folders (card, metadata, weights, direction vectors and the sha256 record of each,
every checksum matching the file it names) and the sweep record; no job log was pulled, so the compares' nodes and
seconds are not recorded. The home judgement ran under transformers 5.22.1. One hundred and thirty-four whole
matrices and the first 2,000,000 bytes of 448 more were read at home from the hub by byte range: the layer 24
attention output, layer 19 down projection and layer 5 query projection of the Zephyr copy, Zephyr and Mistral 7B
v0.1; the layer 10 and 25 query, gate and attention output projections of the abliterix copy, GraySwanAI's model and
Mistral 7B Instruct v0.2, and the head of every linear map of the copy and the instruct model; the layer 20
attention output, layer 5 query projection and token embedding of grayarea's copy, its parent and Mistral Small 3.2;
the layer 20 attention output, down and query projections, layer 5 gate projection and token embedding of the
RP-writer, its parent and Gemma 3 4B; the attention outputs of layers 12, 14 to 24 and 27 of coder3101's two REAP
edits and Google's 26B-A4B, and of layers 12, 15, 20, 24 and 27 of the two REAP checkpoints; the layer 10, 40 and 48
attention outputs of the two llmfan46 copies, their parents and Google's 31B; and the layer 10, 16, 30 and 45
attention outputs and layer 30 query projection of the Gutenberg copy, coder3101's edit, the standard Gutenberg and
Google's 31B. The 4B parent's published `refusal_directions.pt` was read at home as tensors only. The template of
pair 2 was rendered at home through its own Jinja text on a conversation without a system turn, and the templates of
pairs 6 and 7 were compared byte for byte with the maker's 17,344-byte file. The hub's commit histories, file
listings and cards were read for the eight copies and their eight parents, Mistral 7B v0.1 and Instruct v0.2,
Mistral Small 3.2, Google's Gemma 3 4B, 26B-A4B and 31B instruct checkpoints, 0xSero's 19B checkpoint and
coder3101's 19B edit, nbeerbower's standard Gutenberg, and the template histories of the two copies, their parents,
the maker's April 31B repository and Google's 31B. Two hundred and thirty saved direction files were indexed across
the pull copies of every round and one hundred and seventy comparisons were made from them, listed in the reading
notes.

Weight differences alone cannot certify the absence of hidden behavior.
