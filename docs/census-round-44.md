# Census round 44: eight edits on Nautilus, one maker's four Heretic passes of one Cydonia fine-tune moving from one direction per layer to one shared direction, a second maker's searches of three Mistral Small fine-tunes with one 64-layer stack moved to 5.52 of a matrix's norm, and a search of Pantheon-Reasoning on the attention outputs alone

Eight published copies compared with their pinned parents on Nautilus from the batch pinned as
`data/batches/round-44-batch-1.json`: sweep job 4180457, which deleted the round's five originals (the four Cydonia
passes share one parent) and kept none. The pull (card 5853) brought home the eight measurement folders and the sweep
record and no job log, so the download and compare job ids and the compares' nodes and seconds are not in this note.
The batch note says what the round is: the second round from the second-generation pool, Heretic edits applied to
community fine-tunes of Mistral Small and of Gemma 4, each measured against the parent its card names rather than
against the base maker, four of the eight one maker's successive edits of the same Cydonia checkpoint, so that the
round reads how a maker's search moves between versions on one parent. It records what was held on the way:
coder3101's vision re-export of its first Cydonia pass, which carries a vision tower of 222 names its text-only parent
lacks and so cannot be paired under the present rules; the pinner's names step refused it and PaintedFantasy took its
place. No measured pair is repeated and no copy duplicates a measured weight file by checksum. None of the eight
parents is a publisher checkpoint. All eight are community parents, which count as neither originals nor copies
(finding 117): four are new to the census (TheDrummer's Cydonia v4.3, ReadyArt's Forgotten-Abomination 36B v4.1 and
Omega-Darker Gaslight 24B, Gryphe's Pantheon-Reasoning 1.1) and one, zerofata's PaintedFantasy v4.1, is the parent of
round 52's pair 8. All eight are first measurements of distinct copies. The population comes to two hundred and
sixty-two measurements of two hundred and fifty-six distinct copies on thirty-four originals and fifty-two community
parents, counted by `hpc/population.py` from the reports and the lists in `data/population/`. The eight measurements
were re-scored at home with the recipe table as committed and the saved direction vectors, and no assessment or
nearest recipe moved. Every metadata report was judged again at home under transformers 5.22.1 with the originals'
later commits; the home judgement closed one field on pairs 5, 6 and 8 (`config.rope_parameters`, the 5.x form of
`rope_theta`) and moved nothing on the other five; no judgement changed. Each pair has a card (the tool's Stage 1 text
after the home judgement, with the Stage 2 line) and a reading note in `docs/cards/`; the measurements are in
`results/weights/` and `results/meta/`, and the direction vectors stay in the pull copy
(`/opt/ai/hpc-packages/pulls/model-audit/nautilus44/measurements/pair-N/`).

| Pair | Copy | Parent | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | coder3101/Cydonia-24B-v4.3-heretic | TheDrummer/Cydonia-24B-v4.3 | violations against `directional-per-layer-selected`, 15 flags (first shares 0.891 to 0.990) | one direction per layer on the attention outputs of layers 24 to 29 and the down projections of 9 to 39, the two writers of a layer at 1.000, the layers at 0.457; exactly 0 outside (finding 167) |
| 2 | coder3101/Cydonia-24B-v4.3-heretic-v2 | TheDrummer/Cydonia-24B-v4.3 | violations against `single-projection-selected`, 41 flags (first shares 0.756 to 0.990) | one shared direction (0.99999 between layers) on the attention outputs of layers 7 to 39 and the down projections of 16 to 39, made four minutes after pair 1; one trace of 0.0005995 below the down reach (finding 167) |
| 3 | coder3101/Cydonia-24B-v4.3-heretic-v3 | TheDrummer/Cydonia-24B-v4.3 | violations against `directional-per-layer-selected`, 55 flags (first shares 0.961 to 0.990) | a nearly shared direction (0.9972 between layers) on both writers of layers 3 to 39, the widest reach of the four; exactly 0 outside (finding 167) |
| 4 | coder3101/Cydonia-24B-v4.3-heretic-v4 | TheDrummer/Cydonia-24B-v4.3 | violations against `single-projection-selected`, 59 flags (58 first shares 0.852 to 0.990, 1 cross-kind cosine 0.9068) | a nearly shared direction (0.9910 between layers) on the attention outputs of layers 10 to 38 and the down projections of 4 to 39, made six minutes after pair 3; exactly 0 outside (finding 167) |
| 5 | llmfan46/Forgotten-Abomination-36B-v4.1-ultra-uncensored-heretic | ReadyArt/Forgotten-Abomination-36B-v4.1 | violations against `directional-per-layer-selected`, 36 flags (first shares 0.939 to 0.989) | a search of 40 attention outputs between layers 17 and 63 of a 64-layer stack, one direction per matrix, 21 of them moved by more than half their norm, to 5.5239 at layer 23; seven traces to 0.00006002 (findings 168 and 169) |
| 6 | llmfan46/Omega-Darker-Gaslight_The-Final-Forgotten-Fever-Dream-24B-ultra-uncensored-heretic-v2 | ReadyArt/Omega-Darker-Gaslight_The-Final-Forgotten-Fever-Dream-24B | violations against `directional-per-layer-selected`, 12 flags (first shares 0.601 to 0.921) | a search of 12 attention outputs between layers 14 and 31, one direction per matrix; six traces to 0.00005784 (finding 168) |
| 7 | Vortex5/Pantheon-Reasoning-26B-A4B-1.1-heretic | Gryphe/Pantheon-Reasoning-26B-A4B-1.1 | violations against `directional-per-layer-selected`, 23 flags (first shares 0.839 to 0.963) | a search of the attention outputs of layers 7 to 29 alone, one direction per matrix, no expert and no dense writer; exactly 0 outside (finding 170) |
| 8 | llmfan46/MS3.2-PaintedFantasy-v4.1-24B-ultra-uncensored-heretic-v2 | zerofata/MS3.2-PaintedFantasy-v4.1-24B | violations against `directional-per-layer-selected`, 18 flags (first shares 0.717 to 0.949) | a second search of 18 attention outputs between layers 12 and 39, one direction per matrix, reaching the layer the first version left at 0; fourteen traces to 0.0000903 (finding 168) |

Nothing moved outside the matrices the methods reach on four pairs: the largest relative change outside the changed
set is exactly 0 on pairs 1, 3, 4 and 7. On pair 2 it is 0.0005995, on one down projection of layers 0 to 15, below the
reach of the pass's down edit. On pairs 5, 6 and 8 it is 0.00006002, 0.00005784 and 0.0000903, on attention outputs
the searches left under the threshold, seven, six and fourteen of them. All eight copies edit the writers alone: no
query, key, value, gate or up projection moved on any pair, no norm and no embedding, and on pair 7 no expert. The
cards of the eight copies were not read in this pass, so no copy is set against its card's table here, and the
reading notes judge each copy by the form its weights take.

The four Cydonia passes come in two pairs: pairs 1 and 2 created four minutes apart on 2025-12-20 and saved under
transformers 4.57.3, pairs 3 and 4 six minutes apart on 2026-02-15 and saved under 4.57.6. The first pass applies one
direction per layer (0.457 between layers, the two writers of a layer at 1.000) to 37 matrices; the second applies one
shared direction (0.99999) to 57; the third and fourth apply a direction that turns a little between layers (0.9972
and 0.9910) to 74 and 65. The flags rise with the changed set, 15, 41, 55 and 59, and all but one are first shares
under the 0.99 floor. The maker's two Magidonia passes made the same move from per-layer to shared six minutes apart
(findings 144 and 160).

llmfan46's three searches edit the attention outputs alone, one direction per matrix (0.017, 0.048 and 0.022 between
layers), with traces under the threshold inside the reach. On the two 24B parents the relative changes run 0.0223 to
0.0559; on the 64-layer Forgotten-Abomination stack they run 0.0494 to 5.5239, with 21 of 40 above 0.5. The second
PaintedFantasy search keeps the first's count of 18 matrices and its start at layer 12 and edits layer 39, which the
first left exactly 0. Vortex5's search of Pantheon-Reasoning has the form of the maker's two earlier searches (finding
119), not of the per-layer pass of the Phoenix-X merge that contains this parent (finding 165).

Preservation claims. No changed matrix on any pair keeps its row norms (the preserved count is 0 on all 326 changed
matrices of the round), and the cards' claims are not read here.

Fingerprints. The four Cydonia copies match the parent in every compared token and configuration field apart from
the version strings. llmfan46 revised
its three copies on 2026-03-27 within two hours and thirty-three minutes (19:57, 21:46 and 22:30), and all three are
transformers 5.3.0 saves that drop the 1,000 `added_tokens_decoder` declarations; the two over parents that publish no
generation file add one. Pair 5's parent configuration still carries `_name_or_path` naming
ReadyArt/Forgotten-Safeword-36B-4.1, its own parent, and the copy drops it.

Directions. The round placed no edit against the saved vectors of earlier measurements (finding 66's check): every
direction number in this note is a copy's own, from its weights report. The comparisons owed are the four Cydonia
passes against one another layer by layer, against the maker's Magidonia and Mistral Small 3.2 passes and against the
other Mistral Small 24B measurements; llmfan46's three searches against one another, against the PaintedFantasy v1
search and against the four searches finding 166 set beside it; and the Pantheon-Reasoning search against the 26B-A4B
families of findings 119 and 165.

## The token side

The cluster's cards read "consistent with re-save noted" on pairs 1 to 4 and "unexplained differences" on pairs 5 to
8, and the home judgement left all eight there. Pairs 1 to 4 differ in the version strings of the configuration and
generation file alone, 4.57.1 to 4.57.3 on the December passes and to 4.57.6 on the February ones. Pairs 5 and 6 differ
in 1,012 and 1,011 fields: the 1,000 dropped `added_tokens_decoder` declarations and the decoder block that held them,
the `pad_token_id` entry among the special-token ids, an added generation file, `rope_theta` moved into
`rope_parameters`, the `torch_dtype` to `dtype` move, the template moved out of `tokenizer_config.json`, the separate
declaration of `additional_special_tokens`, `config.pad_token_id` and the version string, with pair 5's expected
`_name_or_path` beside them. Pair 8 differs in 1,006, the dropped declarations, the decoder block, `rope_theta`, the
special-token declaration and two version strings; its template does not differ from the parent's, where the first
version's carried Windows line endings on all 51 lines (finding 166). Pair 7 differs in 9: two version strings from
5.5.0.dev0 and 5.6.0.dev0 to 5.13.0, the `dtype` move inside `text_config` and `vision_config` (re-saves) and at the
top level (unexplained), and the template moved out of `tokenizer_config.json` (unexplained). The fixed conversation
renders the same on all eight. The home judgement's one change is `config.rope_parameters` on pairs 5, 6 and 8, read
as the field both saved configurations load to the same value; `config.rope_theta` on the same pairs stays
unexplained.

## What the scorer learned

The assessment and the nearest recipe are the same on the cluster and at home on all eight; the home re-score
measured the within-layer agreement from the saved direction files and kept the group references of the cluster's
comparison. The flags' causes, by pair:

- Directional passes, 15, 41, 55 and 59 flags (pairs 1 to 4): first shares under the 0.99 floor on most changed
  matrices, the least 0.891, 0.756, 0.961 and 0.852, and on pair 4 one cross-kind cosine of 0.9068.
- Searches of the attention outputs, 36, 12, 23 and 18 flags (pairs 5 to 8): first shares under the floor on 36 of
  40, on all 12, on all 23 and on all 18.

The nearest recipe splits the Cydonia passes by direction mode only loosely: the per-layer pass and the third pass
read nearest `directional-per-layer-selected`, the second and fourth `single-projection-selected`, and on pair 2 the
two entries tie at 41. A shared-direction kernel entry that allows a measured turn between layers would read pairs 2
to 4 as one form.

## What stays open

To the reading: the eight copies' cards and their Heretic tables, so that each pass's reach and kernel or window can
be read against the weights; the saved-vector comparisons listed under Directions; on pair 5, the parent's tensor
norms and a byte-range read of the layer 23 attention output on both sides, which decide whether 5.5239 is an
amplified component or a change on a near-empty writer (finding 169); the side of each search's edit; and the
leftover outside the first direction on the flagged first shares of pairs 1 to 4, the line round 52 read on the
maker's other passes. To the metadata tool, beside what round 52 lists: the 5.3.0 save that drops the declarations, on
three more copies (pairs 5, 6 and 8); `rope_theta` and `rope_parameters` read as one field rather than one
closed and one open (pairs 5, 6 and 8); an added generation file over a parent that publishes none (pairs 5 and 6);
the top-level `dtype` move read as the re-save the same tool already reads inside the sub-configurations (pairs 5 to
7); the 5.13.0 save that moves the template out of the token configuration (pair 7); and a dropped `_name_or_path`
naming the parent's own parent read as expected (pair 5). To the recipe library: a shared-direction kernel entry with
a turn tolerance (pairs 2 to 4); a search entry whose relative-change line is read against the parent's own norms
(pair 5); and the input-side search entry with a window line and a traces line, once the windows are read (pairs 5,
6 and 8). To the pinner: a vision re-export over a text-only parent, held this round, needs a pairing rule that names
the tower and pairs the rest.

## Operational

The round ran on Nautilus: the sweep deleted the five originals and kept none, with none absent. Round 44 is read out after
round 52, which ran on Wheat. The pull (card 5853) carries the
eight measurement folders (card, metadata, weights, direction vectors and the measurement record of each) and the
sweep record; no job log was pulled, so the download and compare job ids, nodes and seconds are not recorded. The home
judgement ran under transformers 5.22.1. No matrix was read from the hub by byte range this round, no card was read
from the hub, and no saved direction file was compared with another; the numbers in this note and the reading notes
come from the measurement reports, the home judgement and the home re-score.

Weight differences alone cannot certify the absence of hidden behavior.
