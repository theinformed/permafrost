# Census round 43: eight second-generation edits on Wheat, six of them one maker's Heretic passes on six Mistral Nemo 12B fine-tunes whose directions stand at 0.33 to 0.90 to each other, a 31B arbitrary-rank edit that moves its rows to 0.777 under a preservation claim, and a 26B-A4B search at 0.98 to the family (2026-11-02)

Eight published copies compared with the parents their cards name on Wheat from the batch pinned as
`data/batches/round-43-batch-1.json` (pinned 2026-11-02 07:50Z) under the image-free kit with the standalone
Python: download job 387204, compares 387205 to 387212, sweep 387213, which deleted the eight parents (`1f0ade62`
of zerofata/G4-MeroMero-26B-A4B at `475ecf2d` for pair 1, `71bcc86c` of Gryphe/Gemma-4-31B-StyleTune at
`5a46842f` for pair 2, `dfd4ec92` of DavidAU/MN-GRAND-Gutenberg-Lyra4-Lyra-12B-DARKNESS at `acfc836e` for pair 3,
`d4acaa67` of anthracite-org/magnum-v4-12b at `3200513f` for pair 4, `eb863cd2` of
PocketDoc/Dans-PersonalityEngine-V1.3.0-12b at `62004ca4` for pair 5, `069b476c` of
MarinaraSpaghetti/NemoMix-Unleashed-12B at `74fe434e` for pair 6, `4b1ab041` of nothingiisreal/MN-12B-Celeste-V1.9
at `26ff4e3b` for pair 7 and `38fd65d4` of yamatazen/EtherealAurora-12B-v2 at `f218cef0` for pair 8) from
`/p/work/sdegan/model-audit/rounds/43/originals/`. The pull (card 5778) brought home the eight measurement folders
and the sweep record and no job log, so the compares' nodes and seconds are not in this note. The batch note says
what the round is: the second from the second-generation pool, Heretic and arbitrary-rank edits applied to
community fine-tunes, each measured against the parent its card names; six are Sorihon's Heretic edits of Mistral
Nemo 12B fine-tunes, a family new to the census whose originals are bf16 on the hub, and the other two edit
zerofata's and Gryphe's Gemma 4 fine-tunes. It records what was held or lost on the way: Sao10K's MN-12B-Lyra-v4,
the parent of a seventh Sorihon edit, is gated by its maker, and DavidAU's 12B GPT-5.1 Thinking edit and
Sorihon's KansenSakura Erosion edit are gone from the hub. The round takes the second-generation reading of round
42 to a second base. Against the parent its card names a copy reads the edit alone, and the parent's own distance
from the publisher's checkpoint is read by byte range where the note needs it; for the two Gemma 4 pairs the
saved vectors of the Google-rooted families stand in for the parents as they did in round 42, and for the six
Nemo pairs the census has two measured edits of Nemo Instruct (DuoNeural's projection and grimjim's block-wise
pass, round 13) and, for the first time, six edits by one maker on six fine-tunes of one base, which lets the note
ask whether the direction a pass finds is the base's or the fine-tune's. The population rule of finding 117
applies: a community parent counts as neither an original nor a copy, so the originals stay the publisher's
thirty-four checkpoints and the eight are eight first measurements of eight distinct copies. The population comes
to two hundred and fourteen measurements of two hundred and seven distinct copies on thirty-four originals: the
round 42 header's numbers plus eight measurements and eight copies. Two pairs are the arbitrary-rank branch over
a Gemma 4 fine-tune (llmfan46's third second-generation search, on zerofata's 26B-A4B; densenet's on Gryphe's 31B,
an Unsloth save under a card claiming row-norm preservation), and six are Heretic passes on both writers of Nemo
fine-tunes and merges under cards that print no table (three a refusal count and a KL line, three an image). The
eight measurements were re-scored at home with the recipe table as committed and the saved direction vectors, and
no flag count moved. Every metadata report was judged again at home under transformers 5.22.1 with the parents'
later commits; the home judgement closed 25 fields on pair 2 (the 24 `added_tokens_decoder` entries and
`added_tokens.decoder`, which repeat the added-token record of the `tokenizer.json` both sides share) and
`config.rope_parameters` on pairs 4 and 7 (the 5.x form of `rope_theta`), and moved nothing on the other five;
no judgement changed. Each pair has a card (the tool's Stage 1 text after the home judgement, with the Stage 2
line) and a reading note in `docs/cards/`; the measurements are in `results/weights/` and `results/meta/`, and the
direction vectors stay in the pull copy (`/opt/ai/hpc-packages/pulls/model-audit/wheat43/measurements/pair-N/`).

| Pair | Copy | Parent | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | llmfan46/G4-MeroMero-26B-A4B-it-uncensored-heretic | zerofata/G4-MeroMero-26B-A4B | violations against `directional-per-layer-selected`, 11 flags (first shares 0.858 to 0.942) | the arbitrary-rank branch on the attention outputs of layers 15 to 25 under a card to 26 (11 of 1,013) over zerofata's fine-tune, every edit on the input side at weights 0.99 to 1.55; rows 0.0005 to 0.0055, under the band; exactly 0 outside; the directions at 0.979 to Vortex5's Chimera-X edit, 0.957 to the Moonlight-Dusk edit, 0.953 to SassyDiffusion's and 0.94 to the maker's own April search; a 17,708-byte template of the maker's own that renders as the parent's; the repository deleted and re-uploaded within an hour of its creation (finding 125) |
| 2 | densenet/Gemma-4-31B-StyleTune-heretic-ara | Gryphe/Gemma-4-31B-StyleTune | violations, 66 flags (36 direction cosines, 30 first shares 0.859 to 0.989) | the arbitrary-rank branch on both writers of layers 30 to 47 under a card to 48 (36 of 1,189) over Gryphe's fine-tune, whose layers are Google's bytes and whose trained `lm_head` the edit leaves alone; input-side weights 0.84 to 4.36 on the attention outputs and 2.10 to 3.35 on the down projections; relative changes to 0.279; rows 0.019 to 0.777 under a card "with row-norm preservation"; exactly 0 outside; the left directions at 0.951 to wnfldchen's merged search and 0.910 to llmfan46's April edit, the right at 0.74 and 0.45; an Unsloth save (finding 124) |
| 3 | Sorihon/MN-GRAND-Gutenberg-Lyra4-Lyra-12B-DARKNESS-heretic | DavidAU/MN-GRAND-Gutenberg-Lyra4-Lyra-12B-DARKNESS | violations against `single-projection-selected`, 54 flags (53 first shares 0.972 to 0.989, 1 cross-kind) | one shared direction on the output side of the attention outputs of layers 3 to 39 and the down projections of 4 to 39 (73 of 363) over DavidAU's merge; the down kernel 0.43 to 0.82 readable to the layer, the attention weights scattered 0.07 to 1.20; rows 0.0030 to 0.0135; exactly 0 outside; at 0.904 to the maker's NemoMix edit on all 67 names, 0.55 to grimjim's pass and 0.09 to DuoNeural's projection; a card of an image and a field (finding 123) |
| 4 | Sorihon/Magnum-v4-12B-Heretic | anthracite-org/magnum-v4-12b | violations, 34 flags (first shares 0.867 to 0.989) | one shared direction on the output side of the down projections of layers 7 to 39 and the attention outputs of 10 to 39 (63 of 363) over anthracite-org's fine-tune of Nemo Instruct; the down kernel rising from 0.19 to 1.03 at layer 29 and falling to 0.67, the attention weights scattered 0.33 to 1.28; rows 0.0013 to 0.0137; exactly 0 outside; at 0.71 to the maker's Celeste edit and 0.66 to grimjim's; a 5.8.0 save that drops the thousand declarations and replaces the template with one that renders differently (findings 123 and 126) |
| 5 | Sorihon/Dans-PersonalityEngine-V1.3.0-12B-Heretic | PocketDoc/Dans-PersonalityEngine-V1.3.0-12b | violations, 18 flags (first shares 0.950 to 0.989) | one direction per layer on the output side of the attention outputs of layers 11 to 39 and the down projections of 21 to 38 (47 of 363) over PocketDoc's fine-tune of Nemo Base; the attention component removed whole at 0.98 to 1.16 on every layer, the down kernel 0.39 to 1.08 at layer 30; the last layer's attention output apart at a right kept fraction of 0.39; rows 0.0015 to 0.0222; exactly 0 outside; the first shard the parent's; at 0.73 to the maker's Celeste edit (finding 123) |
| 6 | Sorihon/NemoMix-Unleashed-12B-Heretic | MarinaraSpaghetti/NemoMix-Unleashed-12B | violations against `single-projection-selected`, 40 flags (39 first shares 0.954 to 0.989, 1 cross-kind) | one shared direction on the output side of the down projections of layers 6 to 39 and the attention outputs of 7 to 39 (67 of 363) over MarinaraSpaghetti's five-source merge; the down kernel 0.35 to 0.83, the attention weights scattered 0.09 to 1.03; rows 0.0027 to 0.0152; exactly 0 outside; at 0.904 to the maker's DARKNESS edit; a template added where the parent published none (findings 123 and 126) |
| 7 | Sorihon/MN-12B-Celeste-V1.9-Heretic | nothingiisreal/MN-12B-Celeste-V1.9 | violations, 9 flags (first shares 0.983 to 0.989) | one direction per layer on the output side of the attention outputs of layers 18 to 39 and the down projections of 22 to 34 (35 of 363) over nothingiisreal's fine-tune of Nemo Instruct, the narrowest window of the six; attention weights 0.59 to 1.31, the down kernel 0.81 to 1.15 at layer 28; rows 0.0022 to 0.0111; exactly 0 outside; at 0.73 to the maker's Dans edit, 0.71 to the Magnum edit and 0.68 to grimjim's; a 5.8.0 save that drops the thousand declarations (findings 123 and 126) |
| 8 | Sorihon/EtherealAurora-12B-v2-Heretic | yamatazen/EtherealAurora-12B-v2 | violations, 40 flags (32 first shares 0.923 to 0.989, 8 direction cosines) | one direction per layer on the output side of the attention outputs of layers 4 to 39 and the down projections of 8 to 39 (68 of 363) over yamatazen's merge, which carries natong19's abliteration of Nemo Instruct; the loosest agreement between layers of the six (0.861 adjacent, 0.001 at the minimum); attention weights scattered 0.12 to 1.27, the down kernel 0.19 to 0.81; rows 0.0013 to 0.0218; exactly 0 outside; at 0.70 to the maker's Celeste edit and 0.09 to DuoNeural's projection (finding 123) |

Nothing moved outside the matrices the maker's method reaches in any of the eight pairs: the largest relative
change outside the changed set is exactly 0 on all eight, the first round since round 40 with no residue and no
trace in it. All eight copies are what their cards say, each read against the parent its card names: the two
arbitrary-rank edits read their windows with the branch's selection inside them and one layer short of the card's
`end_layer_index` (pairs 1 and 2), and the six Nemo passes read both writers on the output side under cards that
hold nothing to read them against (pairs 3 to 8). The round's result for the method is the six as a set. One
maker, one tool and six fine-tunes and merges of one base give six windows (3, 7, 11, 6, 18 and 4 to 39), two
methods (one direction shared across every layer and both writers on DARKNESS, Magnum and NemoMix at median
agreements of 0.996 to 0.998; one direction per layer on Dans, Celeste and EtherealAurora at adjacent agreements of
0.86 to 0.95 and 0.06 to 0.16 between the first layer and the last), a down kernel readable to the layer on all
six with its peak between layers 22 and 30, and attention weights scattered on four, near 1 on Dans and 0.59 to
1.31 on Celeste, finding 46's scatter on a Mistral base for the first time; on five of the six the last layer's
attention output reads apart from its kernel at a right kept fraction of 0.39 to 0.71. The directions stand at
0.33 to 0.90 to each other and the agreements follow the parents' lineage (the two merges carrying Lyra and
Gutenberg at 0.904, the two fine-tunes of Nemo Instruct at 0.71, the three per-layer passes at 0.61 to 0.73 among
themselves), so on this base the direction is the fine-tune's as much as the base's, where the Gemma 4 families
stand at 0.93 to 0.99 across makers and parents (findings 119, 120 and 125). The round's result for the branch is
pair 2 against pair 1. densenet's 31B edit, "with row-norm preservation" on its card, moves its rows 0.019 to
0.777 on both writers of eighteen layers at input-side weights to 4.36, the second copy to print the claim and the
second on which it holds on no row (finding 84), with its left directions at 0.95 to wnfldchen's and its right at
0.74; llmfan46's 26B-A4B edit, with no claim, keeps its rows under the band on ten of eleven layers and stands at
0.98 to the Chimera-X edit and 0.94 to the maker's own April search, the family of finding 119 gaining a sixth
member.

The weights read off the weights. The six Nemo passes read on the output side. The down projections carry a
kernel on every copy: 0.57 at layer 4 dipping to 0.43 at 9 to 11 and rising to 0.82 at 22 to 25 on DARKNESS, 0.19
at 7 rising without a dip to 1.03 at 29 on Magnum, 0.39 at 21 to 1.08 at 30 on Dans, 0.41 at 6 dipping to 0.35 at
10 and rising to 0.83 at 24 on NemoMix, 0.85 at 22 to 1.15 at 28 on Celeste, 0.19 at 8 to 0.81 at 28 to 30 on
EtherealAurora, each falling toward the stack's end (0.63, 0.67, 0.39, 0.48, 0.81 and 0.53 at the last layer of
each window). The attention outputs carry the scatter: on DARKNESS 0.07 to 1.20 with the component reversed at
layers 26, 27 and 31 (1.12, 1.20, 1.08) beside 0.18 at 14; on Magnum 0.33 to 1.28; on NemoMix 0.09 to 1.03; on
EtherealAurora 0.12 to 1.27; on Celeste 0.59 to 1.31; on Dans 0.98 to 1.16 on every layer from 11 to 38, the
component removed whole with a small overshoot, the one attention side of the six that reads a setting. The two
arbitrary-rank edits read on the input side: llmfan46's at 0.99 to 1.55 on eleven attention outputs with the down
projections untouched, densenet's at 0.84 to 4.36 on the attention outputs and 2.10 to 3.35 on the down
projections of the same eighteen layers, the writers of a layer unrelated on both.

Preservation claims. One card in the round claims a norm, densenet's "with row-norm preservation", and the rows
read 0.019 to 0.777 on all 36 matrices, over the band on every one. The other arbitrary-rank edit, llmfan46's,
carries no claim and reads 0.0005 to 0.0055, under the band on ten layers and at its lower edge on layer 20. The
six Nemo passes carry no claim and read 0.0013 to 0.0222, through and over the band, with the last layer's
attention output at 0.0222 on Dans and 0.0218 on EtherealAurora.

Fingerprints. Pair 5's first shard (`dff85594`) is byte-equal to its parent's by object id, the layers below the
window; pair 3's and pair 4's `tokenizer.json` re-saves share one object id; the other shards of the eight match
no measured file. By byte range the layer 1 attention output and query projection of every Nemo copy read are
byte-equal to the parent's, and the parents stand from Nemo Instruct's at that layer by the fine-tunes' own
changes (DARKNESS 0.0067 and 0.0042, Magnum 0.0166 and 0.0107, Dans 0.1159 and 0.0377, NemoMix 0.0240 and 0.0172, Celeste 0.0432 and 0.0183, EtherealAurora 0.0473 and 0.0269) and 0.025 to 0.110 from Nemo Base's. At layer
24 DARKNESS's attention output is 0.0203 from the parent's, 0.0299 from Instruct's, 0.0415 from Base's, 0.0302
from DuoNeural's and 0.0329 from grimjim's (the parent 0.0220 from Instruct's and 0.0360 from Base's; Instruct
0.0362 from Base; DuoNeural's 0.0043 and grimjim's 0.0161 from Instruct's), its down projection 0.0121 from the
parent's and 0.0211 from Instruct's; Magnum's attention output is 0.0198 from the parent's, 0.0246 from
Instruct's and 0.0435 from Base's (the parent 0.0146 from Instruct's), its down projection 0.0132 from the
parent's and 0.0209 from Instruct's; Dans's attention output is 0.0173 from the parent's, 0.0653 from Instruct's and 0.0563 from Base's (the parent 0.0631 from Instruct's and 0.0536 from Base's, farther from both than they are from each other), its down projection 0.0097 from the parent's; NemoMix's attention output is 0.0167 from the parent's, 0.0266 from Instruct's and 0.0274 from Base's (the parent 0.0208 and 0.0215), its down projection 0.0121 from the parent's; Celeste's attention output is 0.0195 from the parent's, 0.0435 from Instruct's and 0.0566 from Base's (the parent 0.0389 and 0.0530), its down projection 0.0141 from the parent's; EtherealAurora's attention output is 0.0223 from the parent's, 0.0391 from natong19's abliterated Instruct, 0.0400 from Instruct's and 0.0477 from Base's (the parent 0.0324 from natong19's and 0.0330 from Instruct's; natong19's 0.0156 from Instruct's), its down projection 0.0101 from the parent's; and the six copies' layer 24 attention outputs stand 0.0275 (DARKNESS to NemoMix) to 0.0755 (Dans to Celeste) apart. llmfan46's layer 20 attention output is 0.0333 from the parent's, 0.0339
from Google's, 0.0255 from the maker's April edit, 0.0303 from SassyDiffusion's, 0.0269 from coder3101's and 0.0336
from Chimera-X's (the parent 0.0064 from Google's; the four edits 0.0307 to 0.0429 from Google's and 0.0141 to
0.0322 apart), and its layer 10 query projection is byte-equal to the parent's and 0.0059 from Google's. densenet's layer 44 attention output is 0.2750 from the parent's and from Google's, 0.2653
from llmfan46's April edit, 0.2657 from the Queen edit and 0.2619 from coder3101's, its layer 46 attention output
0.2406 from the parent's and from Google's and 0.2143 from llmfan46's, and the parent's layers 44 and 46 are
byte-equal to Google's (llmfan46's April edit 0.0404 and 0.0639 from Google's at those layers, the Queen edit and
coder3101's 0.0354 at 44), its layer 44 down projection 0.0576 from the parent's and from Google's, its layer 10 query projection byte-equal to both, and its `lm_head` byte-equal to the parent's, the one tensor Gryphe trained.

Directions. The round placed its edits against the saved vectors of earlier measurements without a download
(finding 66's check): the two Gemma 4 pairs against the Google-rooted families (twenty-nine measurements of the
26B-A4B for pair 1, thirty-one of the 31B for pair 2, with the round 42 edits among them), the six Nemo pairs
against each other (fifteen comparisons) and against DuoNeural's projection and grimjim's pass on Nemo Instruct
and two controls on Mistral Small. llmfan46's 26B-A4B edit stands at 0.979 on the left and 0.965 on the right to
Vortex5's Chimera-X edit on all 11 names, 0.957 to the Moonlight-Dusk edit, 0.953 and 0.923 to SassyDiffusion's,
0.942 and 0.955 to the maker's own April search, 0.932 and 0.943 to SubMaroon's body and coder3101's edit, 0.926
and 0.919 to the two QAT searches, 0.81 to mewse's, 0.67 and 0.59 to OS-Software's two Japanese-weighted searches,
0.24 or less to tvall43's and Rootkit7's, 0.203 to TrevorJS's kernel family and 0.055 to huihui-ai's projection.
densenet's 31B edit stands on the left at 0.951 to wnfldchen's merged search (18 names, minimum 0.179), 0.910 to
llmfan46's April edit, 0.875 to the Queen edit, 0.812 to llmfan46's QAT search, 0.793 to MoonRide's custom-prompt
search, 0.761 to coder3101's, 0.758 to Bahushruth's, 0.669 to the MeroMero 31B edit, 0.539 to MoonRide's
arbitrary-rank search, 0.442 to Jim-darby's, 0.28 or less to every kernel pass and projection, 0.210 to bgg1996's
pass and 0.011 to cosmicoptima's, and on the right at 0.35 to 0.74 to the same searches, the side that carries the
weights. The six Nemo passes stand to each other at 0.904 and 0.905 (DARKNESS to NemoMix, 67 names, minimum
0.897), 0.729 and 0.732 (Dans to Celeste, 35), 0.707 and 0.692 (Magnum to Celeste), 0.696 and 0.609 (Celeste to
EtherealAurora), 0.664 and 0.613 (Dans to EtherealAurora), 0.605 and 0.617 (Magnum to Dans), 0.514 and 0.531
(DARKNESS to Magnum), 0.500 and 0.517 (Magnum to NemoMix), 0.455 and 0.423 (Magnum to EtherealAurora), 0.370
(DARKNESS to Dans), 0.365 (DARKNESS to Celeste), 0.360 (NemoMix to Dans), 0.353 (NemoMix to Celeste), 0.335
(DARKNESS to EtherealAurora) and 0.327 (NemoMix to EtherealAurora); to grimjim's block-wise pass at 0.549, 0.656,
0.524, 0.391, 0.675 and 0.430 (pairs 3 to 8, left) and to DuoNeural's difference-of-means projection at 0.094,
0.116, 0.114, 0.089, 0.118 and 0.089; to venkycs's and Pranavz's edits on Mistral Small at 0.027 or less.

## The token side

The cluster's cards read "unexplained differences" on all eight pairs and the home judgement under transformers
5.22.1 with the parents' later commits left all eight there, closing 25 fields on pair 2 and one each on pairs 4
and 7. Pair 1 differs from its parent in the template alone: a 17,708-byte template in place of the parent's
16,448-byte one (Google's 26B-A4B revision `1db3cff1` of 04-10), the two differing in the tool-call macros and
rendering the fixed conversation identically, the maker's fourth template in the census and the maker's-template
case a third time; the version strings read 5.5.4 to 5.9.0 and 5.5.0.dev0 to 5.9.0. Pair 2 differs on seven fields
after the home judgement closed the 24 `added_tokens_decoder` entries and `added_tokens.decoder` that repeat the
record of the `tokenizer.json` both sides share: the Unsloth save's `torch_dtype` for `dtype`, `use_cache` false,
`model_name` and `unsloth_version` 2026.7.2, the configuration's version string dropped (5.9.0 to none; the
generation file 5.9.0 to 5.5.0) and the template copied into `tokenizer_config.json` (24,234 bytes against 2,719)
beside a `chat_template.jinja` byte-equal to the parent's. The six Nemo pairs read the version each copy was saved
under. Pairs 4 and 7 are transformers 5.8.0 saves of 4.45.0.dev0 and 4.44.0.dev0 parents: each drops the 1,000
added-token declarations and the `special_tokens_map.json` (finding 44's case, `tokenizer_config.json` at 442 and
338 bytes), writes `rope_parameters` (closed at home as the 5.x form of `rope_theta`) and turns `use_cache` from
false to true; pair 4's `pad_token` changes from `<pad>` (id 10) to `</s>` (id 2) and its template is replaced by
a 1,053-byte Mistral template whose spacing differs from the parent's and renders the fixed conversation
differently (`[INST] What is two plus two?[/INST] Four.` against `[INST]What is two plus two?[/INST]Four.`), the
round's one rendering difference. Pairs 3, 5, 6 and 8 are 4.57.6 saves of 4.43.3, 4.51.3, 4.44.0 and 4.49.0
parents: `torch_dtype` to `dtype`, `use_cache` false to true on pairs 5, 6 and 8, a `generation_config.json` written
from the configuration (`_from_model_config`, `bos_token_id` 1, `eos_token_id` 2) where the parents of pairs 3, 6
and 8 published none, a `pad_token` `</s>` added where the parents of pairs 3 and 6 declared none, and the template
moved to `chat_template.jinja`: the parent's own 763-byte template on pair 5, the 1,053-byte Mistral template on
pairs 3 and 6 (pair 6's parent published no template at all, so the tool has nothing to render on that side) and a
291-byte ChatML template on pairs 7 and 8. The token ids are the parents' on every pair: the instruct
checkpoint's on the two Gemma 4 pairs (`eos_token_id` `[1, 106]`, generation `[1, 106, 50]`, `bos_token_id` 2 on
pair 1; 106 and `pad_token_id` 0 through the Unsloth parent on pair 2) and Mistral's on the six Nemo pairs
(`bos_token_id` 1, `eos_token_id` 2, `pad_token_id` 10 on pair 5), with the vocabulary 131,072 on every Nemo side
and no table resized; round 39's pretrained-checkpoint case does not recur.

## What the scorer learned

The flag counts are the same on the cluster and at home. Their causes, by pair:

- Arbitrary-rank edits under the per-layer entry, 11 and 66 flags (pairs 1 and 2): a few directions per matrix
  fails the first-share rule on every edit, and pair 2's 36 matrices fail the layer-cosine rule as well because
  the two writers of a layer are unrelated; an arbitrary-rank entry would read both as clean matches with the
  absent layer called out, and pair 2 needs a weight line that allows a kept fraction of 4.36 and a rows line that
  reads a preservation claim against the rows.
- Shared-direction passes under the single-projection entry, 54 and 40 flags (pairs 3 and 6): first shares of
  0.95 to 0.99 under the floor on 53 and 39 matrices and one cross-kind cosine each; a single-direction entry on
  both writers with a kernel line would read both as kernel passes.
- A shared-direction pass under the per-layer entry, 34 flags (pair 4): first shares under the floor on 34 of 63
  matrices, the entry chosen by the selection and not by the direction; the same single-direction entry would
  read it.
- Per-layer passes under the per-layer entry, 18, 9 and 40 flags (pairs 5, 7 and 8): first shares under the floor
  on 18, 9 and 32 matrices and, on pair 8, 8 layer cosines where adjacent layers agree at 0.5 or less; a floor at
  0.98 would clear pairs 5 and 7 and leave pair 8's eight.

The round's result for the measure is the six Nemo pairs against the Gemma 4 families. Where finding 66's check
has read 0.93 or more as one tool on one base, the six read one tool on one base at 0.33 to 0.90 by the parent
under it, so an agreement under 0.9 between two edits of one Mistral base no longer separates tools or prompt
sets, and the check's strong readings (findings 95, 102, 105 and 118) stay strong because they stand at 0.99 to
1.000 with the bytes behind them. The byte-range step after a high agreement, asked for in round 40, read nothing
this round above 0.98, and the step after a low one read the parents' own distances from Nemo Instruct, which are
of the size of the edits.

## Owed to the metadata tool

Added since: nothing this round. What remains: the earlier-revision template and configuration through a
snapshot older than the pin (round 31's pairs 2 and 4, round 35's pair 5, round 39's pair 6, round 40's pair 5);
the declared-context line; the float16 `dtype` reading; the 5.16 save form as a named re-save (finding 39), now
joined by the 4.57.6 and 5.8.0 forms this round reads on six pairs (the `dtype` rename, `use_cache`, the written
generation file, `rope_parameters`, the dropped declarations); the dropped-declarations rule through
`tokenizer.json` (pairs 4 and 7); a maker's-template rule (round 37's pair 7, round 42's pairs 2 and 3, this
round's pair 1); the loader-moved-token and missing-template lines of round 38 (pair 6's parent); the pretrained-ids
line of round 39; the special-flag line of round 41; the Unsloth-parent line of round 42, which this round's pair
2 turns around (an Unsloth copy over a plain parent, the fields the save sets listed in the reading note); and from
this round a card-without-table line, which would say that a Nemo copy's card holds no window or setting to read
the weights against. To the recipe table: an arbitrary-rank entry with a components line, a weight line allowing a
kept fraction above 1 and a rows line that reads a preservation claim (pairs 1 and 2), a single-direction entry
on both writers with a kernel line and a scatter line (pairs 3, 4 and 6), a per-layer entry on both writers (pairs
5, 7 and 8), and a last-layer line for the attention output that reads apart from its kernel on five of six.

## Operational

The round ran on Wheat under the image-free kit with the standalone Python: one download, eight compares and the
sweep, every compare finishing with its card and its weights report, the sweep deleting the eight parents. The
pull (card 5778) carries the eight measurement folders (card, metadata, weights, direction vectors and the sha256
record of each) and the sweep record; no job log was pulled, so the compares' nodes and seconds are not recorded.
The home judgement ran under transformers 5.22.1. One hundred and sixty-six readings were made at home from the hub by byte range (`tools/hub_range_read.py`), three hundred and thirty-one comparisons among them: the layer 24 attention output and down projection of each Nemo copy against its parent's, Nemo Instruct's, Nemo Base's, DuoNeural's and grimjim's, and the layer 1 attention output and query projection of each against its parent's and the two Mistral checkpoints; the layer 24 attention output of the EtherealAurora edit against natong19's abliterated Instruct; the six copies' layer 24 attention outputs against each other; the layer 20 attention output and layer 10 query projection of llmfan46's edit against zerofata's, Google's, the maker's April edit, SassyDiffusion's, coder3101's and Chimera-X's; and the layer 44 and 46 attention outputs, layer 44 down projection, layer 10 query projection and `lm_head` of densenet's edit against Gryphe's, Google's, llmfan46's two 31B edits and coder3101's (Google's 31B has no `lm_head` tensor, its embeddings tied). The hub's commit histories, file listings and cards were
read for the eight copies and their eight parents, Mistral's Nemo Instruct and Nemo Base, natong19's abliterated
Nemo Instruct, Google's 26B-A4B and 31B, and the template histories of llmfan46's three repositories; Sao10K's
MN-12B-Lyra-v4 answered gated and DavidAU's and Sorihon's two withdrawn repositories answered not found. Two
hundred and nine saved direction files were indexed across the pull copies of every round and sixty-three
comparisons were made from them, listed in the reading notes.

Weight differences alone cannot certify the absence of hidden behavior.
