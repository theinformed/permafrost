# Census round 52: eight edits on Wheat, a Heretic 1.1 pass of Mistral Small 3.2 read to the third decimal where a 1.2 pass fell short, one maker's second Magidonia pass placed inside the first, one maker's two Gemma 2 projections carrying one direction, a merge card whose second step is absent from the weights, a distillation whose adapter reached only the per-layer input maps, an Unsloth training that keeps its parent's edit, a per-layer pass of a six-model merge and a fifth search of one maker on Mistral Small

Eight published copies compared with their pinned parents on Wheat from the batch pinned as
`data/batches/round-52-batch-1.json` under the image-free kit with the standalone Python: download job 387662,
compares 387663 to 387670, sweep 387671, which deleted the eight originals (`6eaac59a` of
mistralai/Mistral-Small-3.2-24B-Instruct-2506 at `95a6d26c` for pair 1, `fd028102` of TheDrummer/Magidonia-24B-v4.3 at
`5e5b5e15` for pair 2, `49c9fb82` of Vortex5/Phoenix-X-26B-A4B at `2ef31dd8` for pair 3, `f38ecdec` of
prithivMLmods/gemma-4-E4B-it-Uncensored-MAX at `a236367a` for pair 4, `21ed8e63` of sam-paech/Delirium-v1 at `98dc2dad`
for pair 5, `5c413153` of Vortex5/Gemma-4-26B-A4B-Animus-V14.1-FFT-heretic at `e413cb2e` for pair 6, `9dfa54ea` of
amkkk/Gemma4_E2B_Abliterated_Baked_HF_Ready at `9cea12fb` for pair 7 and `0f5f22c8` of
zerofata/MS3.2-PaintedFantasy-v4.1-24B at `f147119f` for pair 8) from `/p/work/sdegan/model-audit/rounds/52/originals/`.
The pull (card 5849) brought home the eight measurement folders and the sweep record and no job log, so the compares'
nodes and seconds are not in this note. The batch note says what the round is: the first list drawn from the pruned
candidate scan, edits of community fine-tunes, merges and measured copies, each measured against the parent its card
names, with coder3101's Mistral Small 3.2 pass against Mistral's checkpoint. It lists what was left out on the way
(heretic-org's Xortron pass, whose declared chain loops back on itself; Lambent's Mira v1.13 merge, Mantis2024's writer
copy and ShyliaSafetensors's Ariel Alloy pass, whose chains hold a base the lineage cannot place; nightmedia's DECKARD
re-save, whose tensor names cannot be paired; huihui-ai's 48B, whose named parent is a 26B; and saukko's Dolphin 3.0 R1
pass, whose weight files match a copy measured in round 45), and it records that no measured pair is repeated and no
copy duplicates a measured weight file by checksum. One original is a publisher checkpoint (pair 1). The other seven
are community parents, which count as neither originals nor copies (finding 117); two of them are measured copies,
prithivMLmods's re-upload of huihui-ai's E4B edit (round 7) and amkkk's baked E2B edit (round 32), and their own
results are the reading's reference. All eight are first measurements of distinct copies. The population comes to two
hundred and fifty-four measurements of two hundred and forty-eight distinct copies on thirty-four originals and
forty-eight community parents, counted by `hpc/population.py` from the reports and the lists in `data/population/`.
The eight measurements were re-scored at home with the recipe table as committed and the saved direction vectors, and
no flag count moved. Every metadata report was judged again at home under transformers 5.22.1 with the originals'
later commits; the home judgement closed twenty-five fields on pair 4 (special-token declarations that repeat the
shared token file) and one on pair 8 (`rope_parameters`, the 5.x form of `rope_theta`), and moved nothing on the other
six; no judgement changed. Each pair has a card (the tool's Stage 1 text after the home judgement, with the Stage 2
line) and a reading note in `docs/cards/`; the measurements are in `results/weights/` and `results/meta/`, and the
direction vectors stay in the pull copy (`/opt/ai/hpc-packages/pulls/model-audit/wheat52/measurements/pair-N/`).

| Pair | Copy | Parent | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | coder3101/Mistral-Small-3.2-24B-Instruct-2506-heretic | mistralai/Mistral-Small-3.2-24B-Instruct-2506 | violations against `directional-per-layer-selected`, 12 flags (first shares 0.856 to 0.989) | one direction per layer on the down projections of layers 2 to 39 and the attention outputs of 18 to 29, both Heretic 1.1 kernels within 0.006, layers 27 and 29 to the third decimal; exactly 0 outside; at 0.926 to darkc0de's 1.2 pass of the same checkpoint (finding 159) |
| 2 | coder3101/Magidonia-24B-v4.3-heretic-v2 | TheDrummer/Magidonia-24B-v4.3 | violations against `single-projection-selected`, 12 flags (first shares 0.923 to 0.985 on the down projections) | one direction on the attention outputs of layers 8 to 39 and the down projections of 28 to 39, the kernels within 0.008; exactly 0 outside; at 0.990 and 0.969 to the maker's first pass's directions of layers 23 and 24, where index 23.37 points, and 0.851 to grayarea's pass of the same parent (finding 160) |
| 3 | alexokita/Phoenix-X-26B-A4B-Heretic | Vortex5/Phoenix-X-26B-A4B | violations against `directional-per-layer-selected`, 7 flags (6 layer cosines, 1 first share) | one direction per layer on the dense down projections of layers 8 to 29 and the attention outputs of 15 to 29, no expert; exactly 0 outside; at 0.86 to 0.87 to the per-layer passes of Google's checkpoint (finding 165) |
| 4 | Hyphonical/gemma-4-E4B-it-Uncensored-MAX-opus-4.7 | prithivMLmods/gemma-4-E4B-it-Uncensored-MAX | violations against `single-projection`, 379 flags (210 unexpected changes, 84 first shares, 84 direction cosines, 1 cross-kind) | training on every linear map of the text decoder at 0.9 to 7.7 percent, huihui-ai's edit under it whole, the unused shared-cache values moved by rank-one changes; exactly 0 outside (finding 164) |
| 5 | Naphula/Delirium-v1-abliterated | sam-paech/Delirium-v1 | match against `single-projection-selected`, 0 flags | one direction out of both writers of layers 15 to 40 at a flat 1.50; exactly 0 outside; at 0.9996 to the maker's Darkest-muse projection on all 52 shared names (finding 161) |
| 6 | SubMaroon-exp/Kanimus-26B-A4B-FFT-heretic | Vortex5/Gemma-4-26B-A4B-Animus-V14.1-FFT-heretic | violations against `single-projection-selected`, 29 flags (28 unexpected changes, 1 missing projection) | the card's task arithmetic on the queries and keys of all 30 layers to the last bit by byte range, and none of the LoRA merge the card also describes; 0.00081 outside on queries and keys under the threshold (finding 162) |
| 7 | amkkk/Gemma4_E2B_Abliterated_Opus_Distilled | amkkk/Gemma4_E2B_Abliterated_Baked_HF_Ready | violations against `single-projection-selected`, 71 flags (70 unexpected changes, 1 missing projection) | training on the 70 per-layer input maps alone, the only text-decoder modules the adapter's target list names, the towers and the baked edit unchanged; exactly 0 outside (finding 163) |
| 8 | llmfan46/MS3.2-PaintedFantasy-v4.1-24B-ultra-uncensored-heretic-v1 | zerofata/MS3.2-PaintedFantasy-v4.1-24B | violations against `directional-per-layer-selected`, 18 flags (first shares 0.591 to 0.933) | an input-side search of 18 attention outputs inside the card's window 4 to 38 with seventeen traced, weights 1.22 to 2.16, nothing amplified; 0.000043 outside on traced layers; at 0.86 to 0.91 on the input side to the maker's four other Mistral Small searches (finding 166) |

Nothing moved outside the matrices the methods reach on six pairs: the largest relative change outside the changed set
is exactly 0 on pairs 1 to 5 and 7. On pair 8 it is 0.000043, on the attention outputs of the search's window that the
search left under the threshold, and on pair 6 it is 0.00081, on the queries and keys of layers 0 to 13 that the
card's arithmetic moved by less than the threshold. Seven copies are what their cards say: five ablations whose kernels,
scales or windows read off the weights (pairs 1, 2, 3, 5 and 8) and two trainings (pairs 4 and 7). Pair 6 carries the
first of the two edits its card describes and none of the second, and joins the copies whose cards and weights differ.
The round's result for the measure is pair 1 against round 51's pair 4: the same checkpoint under Heretic 1.1 and 1.2,
the directions at 0.926, and the attention kernel read to the third decimal under 1.1 at the two layers where 1.2 fell
short.

The weights read off the weights. coder3101's two passes read printed kernels on the output side: the Mistral Small
3.2 pass within 0.0017 on all 38 down projections and 0.006 on all 12 attention outputs, the Magidonia pass within
0.0053 and 0.0079, a little under the printed heights on most matrices. alexokita's Phoenix-X pass reads 0.44 to 1.10
and 0.39 to 1.30 on the two dense writers, rising across the window without one smooth kernel. Naphula's projection
reads 1.500 to 1.504 on every matrix. llmfan46's search reads on the input side at 1.22 to 2.16. The two trainings and
the task arithmetic carry no edit to read.

Preservation claims. None of the eight cards names a row normalisation. The rows move by 0.0029 to 0.0656 on
coder3101's Mistral Small 3.2 pass, 0.0060 to 0.0423 on the Magidonia pass, 0.0037 to 0.0255 on the Phoenix-X pass,
0.0032 to 0.0320 on the Delirium projection and 0.0016 to 0.0283 on the PaintedFantasy search, through and over
finding 22's band.

Fingerprints. coder3101's Mistral Small 3.2 copy publishes Mistral's consolidated layout beside the transformers file,
and by byte range the consolidated layer 24 attention output is the transformers file's bytes and its layer 5 attention
output Mistral's; both consolidated files hold 585 tensors. prithivMLmods's pinned revision carries huihui-ai's edit
(the layer 20 and 30 attention outputs at -1.501 and -1.499 of Google's component along it). sam-paech's Delirium v1
stands 0.00010 to 0.00084 from google/gemma-2-9b-it on three matrices, and 0.0012 to 0.0032 from Darkest-muse.
unsloth's 26B-A4B re-upload is Google's bytes on the two matrices read for both. The token files of pairs 2 and 6 are
their parents' by checksum, and pair 5's are, with the template inside them.

Directions. The round placed six edits against the saved vectors of earlier measurements without a download (finding
66's check): pair 1 against the Mistral Small 24B measurements, pair 2 against the same and against the maker's first
pass layer by layer, pair 3 against the 26B-A4B measurements, pair 5 against the maker's Darkest-muse projection, the
only measurement on its hidden size, and pair 8 against the maker's four Mistral Small searches; pair 4's training was
compared with every measurement of the E4B. coder3101's Mistral Small 3.2 pass stands at 0.926 to darkc0de's pass of the same
checkpoint, 0.80 to Pranavz's Hearthfire pass, 0.672 to the maker's first Magidonia pass, 0.40 to 0.51 to the
shared-direction passes and 0.104 to huihui-ai's projection. The maker's second Magidonia pass stands at 0.990 and 0.969
to the first pass's layer 23 and 24 directions, 0.851 to grayarea's MPOA pass of the same parent, 0.774 and 0.753 to the
two Skyfall passes and 0.686 to the first pass on the names they share. alexokita's pass stands at 0.86 to 0.87 to the
per-layer Heretic passes of Google's 26B-A4B, 0.844 to TrevorJS's family and 0.27 or less to every arbitrary-rank
search. Naphula's Delirium projection stands at 0.9996 to the maker's Darkest-muse projection on all 52 shared names,
and by byte range the two edits' leading directions on the layer 20 attention output stand at 0.99956. llmfan46's
search stands at 0.86 to 0.91 on the input side to the maker's other four Mistral Small searches. Hyphonical's training
stands at 0.14 or less at the median to every measurement of the E4B, and at 0.57 to 0.81 to DavidAU's Unsloth training on the
unused shared-cache values both move. Kanimus's queries and keys and amkkk's per-layer maps carry no direction.

## The token side

The cluster's cards read "consistent" on pair 6, "consistent with re-save noted" on pairs 2 and 7, "undecided" on
pairs 1 and 5 and "unexplained differences" on pairs 3, 4 and 8, and the home judgement left all eight there. Pair 1
publishes no transformers token files or template, as Mistral's repository does not, so nothing could be rendered;
the configuration and generation file differ in the version string. Pair 2 differs in version strings alone. Pair 5's
shared template refuses a system turn, the case of finding 150, and the token files are the parent's by checksum. Pair
6's token configuration carries the card's patch of `extra_special_tokens` from a list to a mapping, which the tool
reads as the same declarations. Pair 7's token configuration and template differ from the parent's files in bytes and
in no compared field, rendering the fixed conversation the same. Pair 3 adds a generation file with the instruct
checkpoint's ids where the merge publishes none, and the 5.15.0 `per_layer_config` declaration of the full-attention
layers. Pair 4 is an Unsloth save: an `unsloth_version` field, a `model_name` naming the parent, `pad_token_id` 0, the
template written into the token configuration and the generation file dropped with the parent's stop list `[1, 106,
50]`. Pair 8 is a transformers 5.3.0 save that drops the 1,000 `added_tokens_decoder` declarations and writes the
parent's template with Windows line endings on all 51 lines, the maker's form of finding 145. The token ids are the
parents' on every pair (finding 100), and no table is resized.

## What the scorer learned

The flag counts are the same on the cluster and at home. Their causes, by pair:

- Training, 379 and 71 flags (pairs 4 and 7): unexpected changes on the readers, and on pair 4 first shares and
  direction cosines on the writers.
- Task arithmetic on the queries and keys, 29 flags (pair 6): unexpected changes on maps no recipe edits.
- Kernel passes, 12, 12 and 7 flags (pairs 1, 2 and 3): first shares under the 0.99 floor where the kernel's weight is
  small, at the bfloat16 leftover of the Mistral Small calibration, and on pair 3 layer cosines at the three layers
  whose writers disagree.
- An input-side search under the per-layer entry, 18 flags (pair 8): first shares of an edit that is not rank one.

The round's result for the measure is the leftover line: on pairs 1 and 2 every flagged first share has a leftover
outside its first direction of 0.00105 to 0.00160 of the weight's norm, under the calibrated 0.0025 of the Mistral
Small calibration, so the floor charges storage on small edits. A kernel entry also needs the tool's version beside its
heights (finding 159).

## Owed to the metadata tool

What remains from round 51: the earlier-revision template and configuration through a snapshot older than the pin; the
declared-context line; the float16 `dtype` reading; the 5.16, 4.57.6, 5.8.0, 5.3.0 and 5.5.3 save forms as named
re-saves; the dropped-declarations rule through `tokenizer.json`; a maker's-template rule; the loader-moved-token and
missing-template lines of round 38; the pretrained-ids line of round 39; the special-flag line of round 41; the
Unsloth-parent line of round 42; the card-without-table line of round 43; the assistant-mask tag in the template
sandbox, the `quantization_config` line and the re-upload line of round 45; the `dtype` rename line, the
system-turn-free render, the added-generation-file line and the declared-against-stored `dtype` line of round 47; the
5.3.0 save with rewritten line endings, the template moved into `chat_template.jinja`, the maker's template a seventh
time, Unsloth's float16 save and a missing generation file on both sides of round 49; the system-turn-free render with
content, the earlier-revision template on a copy uploaded after the pin, a comparison against the instruct checkpoint's
files when the original publishes none in transformers form, a maker's block in `config.json` and the text-only save of
a multimodal checkpoint of round 51. From this round: the 5.3.0 save with rewritten line endings a second time (pair 8);
`rope_theta` and `rope_parameters` read as one field (pair 8); the added generation file again, now with the instruct
ids over a merge (pair 3); the 5.15.0 `per_layer_config` as a save form (pair 3); an Unsloth save that drops its
parent's generation file (pair 4); and a token configuration that differs in bytes and in no compared field, which the
card should name as a re-save (pairs 6 and 7). To the recipe library: a per-layer and a shared-direction kernel entry
with a heights line that carries the tool's version (pairs 1 and 2); a per-layer entry with no expert and two free
kernel shapes (pair 3); a training entry with a used-maps line that reads the shared-cache projections (pairs 4 and 7);
a task-arithmetic entry checkable against two named checkpoints (pair 6); the input-side search entry with its window's
end excluded (pair 8). To the pinner: a card's adapter target list checked against the checkpoint's module names
(pair 7), a second weight file in another layout read as well (pair 1), and a card's named arithmetic checked by byte
range before a download (pair 6).

## Operational

The round ran on Wheat under the image-free kit with the standalone Python: one download, eight compares and the
sweep, every compare finishing with its card and its weights report, the sweep deleting the eight originals. Rounds
44, 46, 48 and 50, pinned for Nautilus, are still on the cluster, so round 52 is read out before them. The pull (card
5849) carries the eight measurement folders (card, metadata, weights, direction vectors and the sha256 record of each,
every checksum matching the file it names) and the sweep record; no job log was pulled, so the compares' nodes and
seconds are not recorded. The home judgement ran under transformers 5.22.1. Fifty-five whole matrices were read at
home from the hub by byte range, seven of them from the round 49 cache: the layer 24 and 5 attention outputs of
coder3101's Mistral Small 3.2 copy in both its layouts and of Mistral's consolidated file; the layer 10, 31 and 40
value projections and the layer 20 and 30 attention outputs of Hyphonical's copy, prithivMLmods's pinned revision and
google/gemma-4-E4B-it at `83df0a88`; the layer 5 query projection and the layer 20 attention output and down
projection of sam-paech's Delirium v1, Darkest-muse and google/gemma-2-9b-it at `11c9b309`, and the layer 10 and 20
attention outputs of Naphula's Delirium copy beside the layer 20 attention output of the Darkest-muse copy; and the
layer 20 query and key projections, the layer 5 query projection and the layer 23 key projection of Kanimus, its
parent, TeichAI's distillation at `a0e9522e` and unsloth's re-upload at `60941ad6`, with the layer 20 attention output
of Kanimus, its parent and unsloth's re-upload and two matrices of google/gemma-4-26B-A4B-it. Five factors of the
LoRA adapter SubMaroon/Dark-Goetia-26B-A4B-LoRA-v4 at `eb793246` were read by byte range, with its configuration and
shard header. The template of pair 8 and its parent's were fetched and compared byte for byte. The cards of the eight
copies and of four parents were read from the files on the hub. The home judgement read the originals' later commits through the hub API; no other commit history or file listing was read this round.
The byte-range cache is kept at `/var/tmp/permafrost-r52-rr` (1.0 GB). Two hundred and forty-nine saved direction
files were indexed across the pull copies of every round, and the comparisons made from them are listed in the reading
notes.

Weight differences alone cannot certify the absence of hidden behavior.
