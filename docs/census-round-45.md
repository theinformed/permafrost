# Census round 45: eight second-generation edits on Wheat, two makers' edits of one coding fine-tune by two methods, one maker's Google direction carried onto a fine-tune unchanged, a merge that read Mistral's float8 codes as weights, a re-upload with no tensor changed, and a Heretic pass on Nemo Instruct at 0.90 to the Nemo merges (2026-11-02)

Eight published copies compared with the parents their cards name on Wheat from the batch pinned as
`data/batches/round-45-batch-1.json` (pinned 2026-11-02 08:11Z) under the image-free kit with the standalone
Python: download job 387355, compares 387356 to 387363, sweep 387364, which deleted the seven parents (`8eb990dc` of
yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1 at `237e5d8e` for pairs 1 and 2, `b925d8d6` of
jenerallee78/Ministral-3-14B-abliterated at `0c255ddb` for pair 3, `977c0d38` of dphn/Dolphin3.0-R1-Mistral-24B at
`d96260c1` for pair 4, `88b6f9d8` of dphn/Dolphin-Mistral-24B-Venice-Edition at `853f8702` for pair 5, `de9e70d5` of
unsloth/Mistral-Nemo-Instruct-2407 at `e9976040` for pair 6, `f299bff5` of ConicCat/Gemma4-GarnetV2-31B at
`74f74a1b` for pair 7 and `8c36405d` of yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2 at `af644ab1`
for pair 8) from `/p/work/sdegan/model-audit/rounds/45/originals/`. The pull (card 5816) brought home the eight
measurement folders and the sweep record and no job log, so the compares' nodes and seconds are not in this note.
The batch note says what the round is: the third from the second-generation pool, abliteration and Heretic edits of
community fine-tunes and of measured copies, each measured against the parent its card names; three pairs share
yuxinlu1's two Gemma 4 12B fine-tunes as parents under two makers' edits, so the round reads two makers on one
checkpoint, and one pair is a second pass over a Ministral 3 14B first edit. It records that SAIFIINDUSTRIES's
copy "was duplicated from saukko's and its weight files differ", which the hub's object ids do not bear out
(below), and that SOMEHOTMEAL's Gemma 3 12B Janus pass was left out because its card declares a base the hub does
not serve (google/gemma-3-12b); the pinner now keeps such a name in the chain as a leaf marked `missing`, with a note
at pin time (`docs/weights-method.md`), so the next pin records the case where this one dropped it. Against the
parent its card names a copy reads the edit alone, and the parent's own distance from the publisher's checkpoint
is read by byte range where the note needs it. The population rule of finding 117 applies: a community parent
counts as neither an original nor a copy, so the originals stay the publisher's thirty-four checkpoints and a
parent enters the copy count only when it is itself measured against its own parent; none of the seven parents
is, jenerallee78's edit included, whose round 14 measurement through timfromhcs's duplicate read only the float8
quantisation (finding 37). Pair 6's parent is unsloth's re-upload of Nemo Instruct, whose five shards are
Mistral's by object id, so that pair is in effect measured against an original the census already counts. Six of
the eight are first measurements of distinct copies; SAIFIINDUSTRIES's is a hub duplicate of saukko's unmeasured
edit, measured as that edit, and AskVenice's carries its parent's ten shards by object id. The population comes to
two hundred and twenty-two measurements of two hundred and fifteen distinct copies on thirty-four originals: the
round 43 header's numbers plus eight measurements and eight copies, with thirty-five re-uploads among them. The
eight measurements were re-scored at home with the recipe table as committed and the saved direction vectors, and
no flag count moved. Every metadata report was judged again at home under transformers 5.22.1 with the parents'
later commits; the home judgement closed `config.rope_parameters` on pair 6 (the 5.x form of `rope_theta`) and
`config.text_config.moe_intermediate_size` on pair 7 (absent on the parent's side and loaded as the same default),
and moved nothing on the other six; no judgement changed. Each pair has a card (the tool's Stage 1 text after the
home judgement, with the Stage 2 line) and a reading note in `docs/cards/`; the measurements are in
`results/weights/` and `results/meta/`, and the direction vectors stay in the pull copy
(`/opt/ai/hpc-packages/pulls/model-audit/wheat45/measurements/pair-N/`).

| Pair | Copy | Parent | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | tpls/gemma-4-12B-coder-fable5-composer2.5-v1-abliterated | yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1 | violations against `single-projection-selected`, 355 flags (232 unexpected changes, 66 first shares, 56 direction cosines, 1 cross-kind) | one shared direction on the down projections of layers 9 to 47 and the attention outputs of 24 to 43 (59 matrices) with the kept fractions scattered on both sides, inside a bfloat16 recast of the float16 parent that moves 263 more matrices by 0.0011 to 0.0016 and six just under the threshold (0.00097 outside the changed set); at 0.957 to richardyoung's Heretic edit of the same parent and 0.49 to huihui-ai's (pair 2) (finding 127) |
| 2 | huihui-ai/Huihui-gemma-4-12B-coder-fable5-composer2.5-v1-abliterated | yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1 | clean match to `directional-per-layer-selected`, 0 flags | the projection of one direction out of both writers of layers 23 to 28 (12 of 677) at weight 1.00 on the output side, rows 0.016 to 0.079, exactly 0 outside; at 1.000 to the maker's projection of Google's 12B on all 12 names, the parent projected along that edit's direction reproducing the copy to within the bfloat16 rounding (finding 128) |
| 3 | SOMEHOTMEAL/Ministral-3-14B-Janus-Abliterated-V2-Base_And_GGUF | jenerallee78/Ministral-3-14B-abliterated | violations against `single-projection`, 345 flags (200 unexpected changes, 80 first shares, 64 direction cosines, 1 cross-kind) | every linear map of all 40 layers at 460 to 4,593 times its parent's norm: the card's DARE merge over a base read as Mistral's float8 codes without their scales, 30.1 percent of each matrix's entries the raw codes and the rest about 0.136 times them; exactly 0 outside; the parent's own edit read by byte range against Mistral's bfloat16 release, rank one at weight 1.00 on the writers with the queries byte-equal (findings 129 and 130) |
| 4 | SAIFIINDUSTRIES/Abliterated-Dolphin3.0-R1-Mistral-24B | dphn/Dolphin3.0-R1-Mistral-24B | violations against `single-projection`, 66 flags (first shares 0.987 to 0.990) | saukko's unmeasured edit under the hub's duplicate function, every file saukko's by object id: one direction projected out of the token embedding and both writers of all 40 layers (81 of 363) at weight 1.00, rows 0.0017 to 0.0151, exactly 0 outside; at 0.448 to venkycs's projection of Mistral Small 24B Instruct (finding 131) |
| 5 | AskVenice/venice-uncensored | dphn/Dolphin-Mistral-24B-Venice-Edition | `unchanged`, 1 flag (`missing_changed_projection`) | 0 of 363 tensors changed: the parent's ten shards by object id under Venice.ai's card, the first empty changed set in the census; the uncensoring is the parent's fine-tune of Mistral Small 24B Instruct, 0.0035 to 0.0056 on the matrices read with no leading component (finding 132) |
| 6 | 0xA50C1A1/Mistral-Nemo-Instruct-2407-Heretic-v2 | unsloth/Mistral-Nemo-Instruct-2407 | violations against `single-projection-selected`, 1 flag (cross-kind 0.894) | one shared direction on the output side of the attention outputs of layers 12 to 39 and the down projections of 5 to 39 (63 of 363), the card's kernel reaches to the layer, the down kernel 0.83 to 1.39 under a printed 1.41 to 1.47, the attention weights scattered 0.09 to 1.06; exactly 0 outside; at 0.898 to Sorihon's DARKNESS edit, 0.854 to the NemoMix edit, 0.57 to the Magnum edit and 0.39 to 0.43 to the three per-layer passes; a template with the assistant-mask tag the tool's renderer cannot read (finding 133) |
| 7 | llmfan46/Gemma-4-Garnet-V2-31B-it-ultra-uncensored-heretic | ConicCat/Gemma4-GarnetV2-31B | violations against `directional-per-layer-selected`, 20 flags (first shares 0.917 to 0.981) | the arbitrary-rank branch on the attention outputs of layers 25 to 45 under a card to 46, layer 29 rewritten at 0.000116, input-side weights 1.31 to 2.66 with no component amplified, rows 0.0003 to 0.0377; at 0.78 to 0.88 to the maker's four other 31B searches and 0.80 to coder3101's; the maker's 17,344-byte template put in by delete and re-upload ten days after the weights (finding 134) |
| 8 | huihui-ai/Huihui-gemma-4-12B-agentic-fable5-abliterated | yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2 | clean match to `directional-per-layer-selected`, 0 flags | the maker's projection on the same twelve matrices at weight 1.00, rows 0.024 to 0.071, exactly 0 outside; at 0.978 to pair 2 and to the maker's Google edit, the direction found again on this fine-tune (finding 128) |

Nothing moved outside the matrices the maker's method reaches on five of the eight: the largest relative change
outside the changed set is exactly 0 on pairs 2, 3, 4, 6 and 8, 0 on pair 5 because nothing changed, 0.000116 on
pair 7 (layer 29 inside the window) and 0.00097 on pair 1, where the bfloat16 recast of a float16 parent leaves six
matrices just under the threshold and 263 over it. Seven copies are what their cards say, each read against the
parent its card names: tpls's and huihui-ai's two edits read one direction on the writers (pairs 1, 2 and 8),
saukko's edit reads the classic projection its card's sources describe (pair 4), the Venice copy is the Dolphin
edition its card names (pair 5), and the two Heretic passes read their tables to the layer (pairs 6 and 7). The
eighth carries a change its card does not name: SOMEHOTMEAL's card prints a merge of jenerallee78's edit over
Mistral's instruct model, and the weights hold Mistral's float8 codes read as values, with no scale beside them
(pair 3). The round's result for the method is pairs 1 and 2: two makers' edits of
one checkpoint by two tools. tpls's edit is a Heretic-family direction (0.957 to richardyoung's Heretic edit of the
same fine-tune, 0.921 to BinxNet's Heretic pass of Google's 12B) with the scattered kept fractions finding 18 read
on richardyoung's; huihui-ai's is the maker's projection, at weight 1.00 on layers 23 to 28, with the direction the
maker found on Google's 12B carried onto the fine-tune unchanged (1.000 on every name, 0.99998 by byte range), and
the two edits stand at 0.49 to each other, where huihui-ai's Google edit stands at 0.43 to 0.46 to the Heretic
passes of Google's 12B. Neither is a
duplicate of the other: the two repositories share no weight file at any revision, one is five bfloat16 shards and
the other a single float16 file, and their matrices stand 0.018 to 0.033 apart. The maker's second 12B edit, of
yuxinlu1's agentic fine-tune, recomputes the direction (0.978 to the first, the parent projected along the Google
direction leaving a third of the change unexplained), so one maker on two fine-tunes by one fine-tuner carried the
base direction once and found it again once. The round's result for the base question of findings 123 and 126 is
pair 6: a Heretic pass on Nemo Instruct itself stands at 0.898 and 0.854 to Sorihon's passes on the two Lyra and
Gutenberg merges, 0.57 to the pass on anthracite-org's Magnum fine-tune of Nemo Instruct and 0.39 to 0.43 to the
three per-layer passes, so the base-side direction is nearest the shared-direction passes on the merges and not
the passes on Nemo Instruct's own fine-tunes; the agreement follows the method (one shared direction against one
per layer) at least as much as the parent.

The weights read off the weights. Three copies read one direction on the output side at weight 1.00: huihui-ai's
two (left kept fraction -0.003 to 0.005 on all 24 matrices) and saukko's (-0.004 to 0.003 on 80 writers, the
embedding along its hidden axis). Two read kernels: 0xA50C1A1's down projections, one minus the left kept fraction
at 1.29 at layer 5, 1.00 at 8, 0.83 at 10 and 11 and 1.39 at 19 to 24, holding at 1.29 to 1.38 to the end, under a
printed 1.41 to 1.47 that peaks at 24.17, with the attention outputs scattered 0.09 to 1.06; and tpls's, with no
weight to read (left -0.16 to 0.98, right -0.02 to 0.98). One reads the arbitrary-rank branch on the input side:
llmfan46's at 1.31 to 2.66 on twenty attention outputs, the left side 0.04 to 0.42, no kept fraction above 1. Two
carry no edit to read: the Venice copy, unchanged, and SOMEHOTMEAL's, whose differences are the float8 codes.

Preservation claims. One card in the round names a norm-preserving method, jenerallee78's (grimjim's
norm-preserving biprojection), and by byte range the three writers read move their rows by up to 0.0184, 0.0105 and
0.0108 against Mistral's bfloat16 release, the size of the unrestored projection finding 36 read on grimjim's own
Nemo copy. No other card claims a norm. The rows of the other edits run 0.0003 to 0.0377 on llmfan46's, 0.0009 to
0.0165 on tpls's, 0.0017 to 0.0151 on saukko's, 0.0038 to 0.0163 on 0xA50C1A1's, and 0.016 to 0.079 on huihui-ai's
two, over finding 22's band on all 24 matrices.

Fingerprints. SAIFIINDUSTRIES's ten shards (`b5a6a7f5` to `605483d5`), README, configuration, generation file,
index, token files and `trainer_state.json` are saukko's at every revision by object id; AskVenice's ten shards
(`65828eac` to `2ca2d9db`) are dphn's Venice Edition's from its upload of 2025-06-12 to the pinned revision, with
the small files re-saved; jenerallee78's first shard (`a381935a`) is mistralai/Ministral-3-14B-Instruct-2512-BF16's
first shard, the layers below the edit, and its configuration and `tokenizer.json` are that repository's at
`bbc49ba0`; unsloth's five Nemo shards are Mistral's; huihui-ai's two copies and tpls's carry the parents'
template, processor file and `tokenizer.json`, and llmfan46's configuration (`6d6fac89`) is the maker's April 31B
repository's. By byte range: huihui-ai's coder edit at layer 25 stands 0.0058 and 0.0067 from the maker's Google
edit, the distance between the parent and Google's (0.0055 and 0.0063), and the parent projected along the Google
edit's leading direction reproduces it to within 0.0016 of the matrix; the agentic edit stands 0.0081 and 0.0097
from the coder edit, the two fine-tunes 0.0049 and 0.0057 apart and 0.0055 to 0.0087 from Google's; tpls's copy
stands 0.0049, 0.0253 and 0.0176 from the parent on the layer 25 attention output, the layer 25 down projection and
the layer 30 attention output, 0.0183, 0.0133 and 0.0108 from richardyoung's copy and 0.0217, 0.0329 and 0.0176 from
huihui-ai's, and its layer 5 query projection is the parent's float16 matrix rounded to bfloat16 on every entry,
where the three float16 copies (huihui-ai's two, richardyoung's) are byte-equal to the parent there. On Ministral:
30.07 to 30.09 percent of the entries of four of SOMEHOTMEAL's matrices are the float8 codes stored by
mistralai/Ministral-3-14B-Instruct-2512, the rest about 0.136 times them; jenerallee78's query projections of
layers 0 and 20 are byte-equal to the bfloat16 release and its layer 20 and 30 attention outputs and layer 20 down
projection stand 0.0149 to 0.0185 from it, each a rank-one difference; Mistral's float8 checkpoint dequantised stands
0.027 from its bfloat16 release on every matrix read. On Mistral Small: saukko's layer 20 attention output and down
projection stand 0.0191 and 0.0160 from Dolphin R1's with the query projection byte-equal, Dolphin R1 stands 0.376 to
0.509 from Mistral's Base 2501 (a full fine-tune with first shares of 0.0018 to 0.0048), and the Venice Edition
stands 0.0035 to 0.0056 from Mistral Small 24B Instruct 2501 (first shares 0.082 to 0.29), the instruct model 0.034
to 0.038 from the base. On Nemo: 0xA50C1A1's layer 24 attention output and down projection stand 0.0182 and 0.0204
from the parent's, 0.0221 and 0.0225 from grimjim's and 0.0186 and 0.0208 from DuoNeural's, and its layer 1
attention output and layer 3 down projection are byte-equal to the parent's, which is Mistral's on all four
matrices read. On the 31B: llmfan46's layer 42 attention output stands 0.0367 from the parent's, 0.0507 from
Google's, 0.0473 from the maker's April edit and 0.0470 from coder3101's, its layer 29 0.00012 from the parent's,
and its layer 10 query projection and layer 35 down projection are the parent's bytes; the parent stands 0.022 to
0.035 from Google's on the four matrices read, with first shares of 0.12 to 0.32.

Directions. The round placed its edits against the saved vectors of earlier measurements without a download
(finding 66's check): the three 12B pairs against the forty measurements of the 12B and its QAT checkpoint, pair 6
against the eight Nemo measurements and the controls, pair 7 against the thirty-four 31B measurements, pairs 3 and 4
against every Mistral-family measurement. huihui-ai's coder edit stands at 1.000 on the left and on the right
(minimum 1.000) to the maker's projection of Google's 12B on all 12 names and to its two hub duplicates, at 0.978
and 0.982 to the agentic edit, 0.70 and 0.81 to the maker's QAT projection, 0.66 to AEON-7's, 0.62 to smashingtags's
and Paul691's, 0.53 to TrevorJS's, 0.50 to richardyoung's, 0.49 and 0.40 to tpls's and 0.21 or less to the kernel
passes. tpls's edit, restricted to its 59 edited matrices, stands at 0.957 and 0.936 to richardyoung's Heretic edit
of the parent on all 39 shared names (minimum 0.940), 0.921 to BinxNet's, 0.87 to 3MPER0RR's, prithivMLmods's and
MoonRide's, 0.863 to lemuralabs's, 0.70 to enkato64bit's, 0.54 to jwest33's, 0.46 to 0.49 to huihui-ai's three,
0.24 to TrevorJS's, 0.20 to OpenYourMind's and 0.09 to coder3101's. 0xA50C1A1's Nemo pass stands at 0.898 and 0.898
to the DARKNESS edit (63 names, minimum 0.891), 0.854 and 0.856 to the NemoMix edit, 0.574 and 0.594 to the
Magnum edit, 0.468 and 0.470 to grimjim's pass, 0.429 to the Celeste edit, 0.395 to the EtherealAurora edit, 0.389
to the Dans edit and 0.107 to DuoNeural's projection. llmfan46's Garnet edit stands on the left at 0.875 to the
maker's QAT search, 0.850 to coder3101's QAT edit, 0.807 to the MeroMero edit, 0.804 to coder3101's 31B edit, 0.802
to the Queen edit, 0.789 and 0.775 to MoonRide's two, 0.781 to the maker's April edit, 0.700 to Bahushruth's, 0.678
to wnfldchen's, 0.623 to densenet's, 0.549 to Jim-darby's and 0.406 to OS-Software's QAT search, and at 0.15 or less
to every kernel pass and projection. saukko's Dolphin edit stands at 0.448 to venkycs's projection of Mistral Small
24B Instruct 2501 and 0.20 to huihui-ai's Mistral Small 3.2 projection. SOMEHOTMEAL's vectors stand at 0.955 to
round 14's measurement of timfromhcs's duplicate, both differences dominated by the same float8 codes, and at 0.14
or less to every other Mistral edit.

## The token side

The cluster's cards read "unexplained differences" on pairs 1, 3, 6 and 7, "consistent with re-save noted" on pair
4 and "consistent" on pairs 2, 5 and 8, and the home judgement under transformers 5.22.1 with the parents' later
commits left all eight there, closing one field each on pairs 6 and 7. Pair 1 differs in the four `dtype` fields,
`float16` to `bfloat16`, the recast its commit title names. Pair 3's token files are the float8 instruct
checkpoint's head where the parent's are the bfloat16 release's December files: the parent's 1,000 added-token
declarations are absent from the copy's 22,174-byte `tokenizer_config.json`, ids 34 and 35 read `[THINK]` and
`[/THINK]` on the parent's side and `<SPECIAL_34>` and `<SPECIAL_35>` on the copy's, the template moves from 7,754
to 11,913 bytes and renders the fixed conversation identically, the copy publishes no generation file and writes
the generation ids into its text sub-configuration beside the `quantization_config`. Pair 4 differs in version
strings and `_name_or_path`. Pair 6 is a transformers 5.3.0 save of a 4.49.0.dev0 parent, and its template carries a
commit of 04-08 that wraps each assistant turn in `{% generation %}` and `{% endgeneration %}` for the SFT trainer's
assistant mask: the tool's sandboxed renderer fails on the tag ("Encountered unknown tag 'generation'"), so the
card lists the render as missing evidence, and rendered at home through transformers the template gives the
parent's text with one newline added after the final `</s>`, the round's one template that renders differently,
as Magnum's did in finding 126. Pair 7 carries the maker's 17,344-byte template in place of
Google's 16,448-byte revision of 04-10 on the parent, put in by delete and re-upload on 05-04 and 05-05, each time
three minutes after the same file went onto the maker's April 31B repository; the two render identically. The token
ids are the parents' on every pair (finding 100): the Gemma 4 instruct checkpoint's on the three 12B pairs and the
31B pair (`eos_token_id` `[1, 106]`, generation `[1, 106, 50]`, `bos_token_id` 2, `pad_token_id` 0), Mistral's on
pairs 3, 5 and 6 (`bos_token_id` 1, `eos_token_id` 2, `pad_token_id` 11 on pair 3's side and 10 on pair 6's), and
Dolphin R1's on pair 4 (`eos_token_id` `[2, 131072]`, the vocabulary 131,074 with the two tokens Dolphin added on
both sides); no table is resized and round 39's pretrained-checkpoint case does not recur.

## What the scorer learned

The flag counts are the same on the cluster and at home. Their causes, by pair:

- A recast inside the changed set, 355 flags (pair 1): 232 unexpected changes on matrices the bfloat16 recast moved
  by 0.0011 to 0.0016, then first shares and direction cosines at the edit's ends; a recast line that compares each
  matrix with the parent rounded to the copy's storage type would close the 232.
- Codes read as weights, 345 flags (pair 3): every linear map changed by hundreds of times its norm; no entry should
  read it, and the names step that refuses a float8 original would catch it if it also refused a copy whose stored
  values exceed its parent's by two orders of magnitude or whose configuration declares a quantisation its files
  do not carry.
- A classic projection under the single-projection entry, 66 flags (pair 4): first shares of 0.987 to 0.990 on a
  bfloat16 save, finding 51's storage floor; read beside the storage type the entry matches.
- An unchanged pair, 1 flag (pair 5): the nearest entry asks for a changed writer; a re-upload line would read it.
- A shared-direction kernel pass under the selected single-projection entry, 1 flag (pair 6): the cross-kind cosine
  at 0.894 under a 0.95 floor that round 43's three shared-direction Nemo passes also sit under (0.89 to 0.94).
- An arbitrary-rank search under the per-layer entry, 20 flags (pair 7): first shares of 0.917 to 0.981 under the
  floor, the branch's own spread; an arbitrary-rank entry would read it with layer 29 named.
- Two clean matches (pairs 2 and 8): huihui-ai's projections read cleanly, as the maker's first-generation 12B edit
  did.

The round's result for the measure is pair 2 against pair 1. The direction check reads 1.000 between a maker's
edit of a fine-tune and the same maker's edit of the base checkpoint, and the bytes confirm it as the base
direction carried over, so a 1.000 across parents is now a reading of reuse as well as of a shared parent (findings
95 and 105); and on one checkpoint two tools stand at 0.49, the distance the same two families stand at on Google's
12B, so the check separates tools on a fine-tune as it does on the base.

## Owed to the metadata tool

Added since: the pinner's `missing` leaf for a declared base the hub does not serve, which this round's batch note
asked for. What remains: the earlier-revision template and configuration through a snapshot older than the pin; the
declared-context line; the float16 `dtype` reading, now with a bfloat16 save of a float16 parent (pair 1); the 5.16,
4.57.6 and 5.8.0 save forms as named re-saves, joined by 5.3.0 (pair 6); the dropped-declarations rule through
`tokenizer.json`; a maker's-template rule (pair 7, the fourth of the maker's repositories in the census to carry the 17,344-byte
file); the
loader-moved-token and missing-template lines of round 38; the pretrained-ids line of round 39; the special-flag line
of round 41; the Unsloth-parent line of round 42; the card-without-table line of round 43; and from this round the
assistant-mask tag in the template sandbox (pair 6), a line that reads a `quantization_config` the files do not carry
(pair 3), and a re-upload line for a copy whose shards are its parent's by object id under a first commit that is not
the duplicate function (pair 5). To the recipe table: a recast line (pair 1), a storage-type reading of the first-share
floor (pair 4), an arbitrary-rank entry with a weight line allowing a kept fraction under -1 on the input side (pair
7), a single-direction entry on both writers with a kernel line and a scatter line (pair 6), and a reused-direction
line that names a direction carried from the base (pair 2).

## Operational

The round ran on Wheat under the image-free kit with the standalone Python: one download, eight compares and the
sweep, every compare finishing with its card and its weights report, the sweep deleting the seven parents. Round 44,
pinned for Nautilus, is still on the cluster, so round 45 is read out before it. The pull (card 5816) carries the
eight measurement folders (card, metadata, weights, direction vectors and the sha256 record of each, every checksum
matching the file it names) and the sweep record; no job log was pulled, so the compares' nodes and seconds are not
recorded. The home judgement ran under transformers 5.22.1. One hundred and nineteen readings were made at home
from the hub by byte range, one hundred and sixty-one comparisons among them: the layer 25 attention output and down
projection, the layer 30 attention output and the layer 5 query projection of the three 12B copies against their
parents, Google's 12B, huihui-ai's Google edit and richardyoung's edit; the layer 0 and 20 query projections, layer 20
and 30 attention outputs and layer 20 down projection of SOMEHOTMEAL's and jenerallee78's copies against Mistral's
float8 checkpoint (codes and scales), its bfloat16 release at `bbc49ba0` and the Base 2512 checkpoint; the layer 20
attention output, query projection and down projection of saukko's edit, Dolphin R1, the Venice Edition and
venkycs's edit against Mistral Small 24B Base and Instruct 2501; the layer 24 attention output and down projection,
layer 1 attention output and layer 3 down projection of 0xA50C1A1's edit against unsloth's, Mistral's, grimjim's and
DuoNeural's; and the layer 42 and 29 attention outputs, layer 10 query projection and layer 35 down projection of
llmfan46's Garnet edit against ConicCat's, Google's, the maker's April edit and coder3101's. The template of pair 6
was rendered at home through transformers at both of its revisions. The hub's commit histories, file listings at
every revision and cards were read for the eight copies, their seven parents, saukko's repository,
mistralai/Ministral-3-14B-Instruct-2512 and its bfloat16 release, Mistral's Base 2512, Mistral Small 24B Base and
Instruct 2501, Mistral's Nemo Instruct, Google's 12B and 31B and the maker's April 31B repository. Two hundred and
seventeen saved direction files were indexed across the pull copies of every round and one hundred and ninety-six
comparisons were made from them, listed in the reading notes.

Weight differences alone cannot certify the absence of hidden behavior.
