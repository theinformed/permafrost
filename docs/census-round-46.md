# Census round 46: eight edits on Nautilus, the re-pin of chulcher's E4B copy reading the card's two kernels alone on the pretrained base, two makers' passes of one Mag-Mell merge in one direction 1.24 times apart in size, and one maker's passes of two Nemo parents at equal sizes and 0.84 apart in direction

Eight published copies compared with their pinned parents on Nautilus from the batch pinned as
`data/batches/round-46-batch-1.json`: download job 4184047, compare jobs 4184048 to 4184055 and sweep job 4184056,
which deleted the round's seven originals (the two Mag-Mell pairs share one parent) and kept none. The pull (card
5854) brought home the eight measurement folders and the sweep record and no job log, so the compares' nodes and
seconds are not in this note. The batch note says what the round is: the re-pin of chulcher's E4B copy against
google/gemma-4-E4B, the pretrained checkpoint round 39 found it standing on (finding 100), allowed as a duplicate of
its round 39 measurement, and then the third Nautilus round from the second-generation pool, abliteration and
Heretic edits of community fine-tunes and of earlier edits, each measured against the parent its card names. Two
pairs share inflatebot's Mag-Mell parent, and EldritchLabs's Scale1.2 copy names Naphula's edit in its card where
its field names inflatebot, so it is pinned against inflatebot and read beside Naphula's. The batch note records
what was held on the way: SOMEHOTMEAL's Gemma 3 12B Janus pass, whose token embedding carries 262,145 rows against
its parent's 262,208, a resized vocabulary no pairing rule covers yet. No measured pair is repeated except the
declared re-pin, and no copy duplicates a measured weight file by checksum. One parent is a publisher checkpoint,
google/gemma-4-E4B (pair 1). The other seven pairs stand on six community parents, which count as neither originals
nor copies (finding 117): yuxinlu1's coding and agentic fine-tunes of Gemma 4 12B, measured under other makers'
edits before (findings 18, 127 and 128), and four new to the census, tpls's SFT of the coding fine-tune,
inflatebot's Mag-Mell R1, p-e-w's Heretic noslop pass of Mistral Nemo Instruct and SicariusSicariiStuff's Impish
Bloodmoon 12B. The batch note calls p-e-w's pass a measured edit; round 28's batch pinned it, but no report of it is
in `results/weights/`, so the parent's own edit is not separated here. The hub ids of pair 1 collide with round 39's:
`results/weights/chulcher-gemma-4-e4b-abliterated.json`, `results/meta/chulcher-gemma-4-e4b-abliterated.json`, the
Stage 1 card and its reading note now carry the round 46 measurement, and the round 39 versions stay in git history
at commit 9670afa. The population comes to two hundred and sixty-nine measurements of two hundred and sixty-three
distinct copies on thirty-four originals and fifty-six community parents, counted by `hpc/population.py` from the
reports and the lists in `data/population/`; the replaced report means the round adds seven measurements to the
count, not eight. The eight measurements were re-scored at home with the recipe table as committed and the saved
direction vectors, and no assessment or nearest recipe moved. Every metadata report was judged again at home under
transformers 5.22.1 with the originals' later commits; the home judgement closed one field on pair 1
(`config.text_config.moe_intermediate_size`) and moved nothing on the other seven; no judgement changed. Each pair
has a card (the tool's Stage 1 text after the home judgement, with the Stage 2 line) and a reading note in
`docs/cards/`; the measurements are in `results/weights/` and `results/meta/`, and the direction vectors stay in
the pull copy (`/opt/ai/hpc-packages/pulls/model-audit/nautilus46/measurements/pair-N/`).

| Pair | Copy | Parent | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | chulcher/gemma-4-e4b-abliterated | google/gemma-4-E4B | violations against `directional-per-layer-selected`, 2 flags (first shares 0.9857 and 0.9895) | the card's two kernels on the pretrained checkpoint: the attention outputs of layers 17 to 33 and the down projections of 33 to 38, the windows the card prints, one direction per layer; 23 tensors where round 39 against the instruct model read 595; exactly 0 outside (finding 171) |
| 2 | llmfan46/gemma-4-12B-coder-fable5-composer2.5-v1-uncensored-heretic | yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1 | violations against `single-projection-selected`, 22 flags (20 direction cosines 0.776 to 0.950, 1 first share 0.9826, 1 cross-kind cosine 0.5058) | one shared direction (0.963 between layers) on the attention outputs of layers 3 to 47 and the down projections of 8 to 47, at 0.957 to tpls's and 0.899 to richardyoung's passes of the same parent; exactly 0 outside (finding 174) |
| 3 | llmfan46/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-uncensored-heretic | yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2 | violations against `directional-per-layer-selected`, 7 flags (6 within-layer cosines 0.792 to 0.932, 1 first share 0.9878) | one shared direction (0.974) on the attention outputs of layers 9 to 47 and the down projections of 20 to 47, at 0.963 to the maker's pass of the coding fine-tune; exactly 0 outside (finding 174) |
| 4 | tpls/gemma-4-12B-coder-fable5-composer2.5-v1-sft-v5-abliterated | tpls/gemma-4-12B-coder-fable5-composer2.5-v1-sft-v5 | violations against `single-projection-selected`, 6 flags (first shares 0.971 to 0.989) | one direction on seven late matrices, the down projections of layers 39 to 42 and the attention outputs of 45 to 47, at 0.05 to the maker's own and every other edit of the coding fine-tune; exactly 0 outside (finding 175) |
| 5 | EldritchLabs/MN-12B-Mag-Mell-R1-Uncensored-Scale1.2 | inflatebot/MN-12B-Mag-Mell-R1 | match to `single-projection`, 0 flags | one direction on both writers of all 40 layers, Naphula's at 0.9997 with difference norms 1.24 times smaller; exactly 0 outside (finding 172) |
| 6 | Naphula/MN-12B-Mag-Mell-R1-Uncensored | inflatebot/MN-12B-Mag-Mell-R1 | match to `single-projection`, 0 flags | one direction (0.9999988 between layers) on both writers of all 40 layers, the maker's Gemma 2 form; exactly 0 outside (finding 172) |
| 7 | EldritchLabs/Mistral-Nemo-Instruct-2407-heretic-noslop-MPOA | p-e-w/Mistral-Nemo-Instruct-2407-heretic-noslop | match to `single-projection`, 0 flags | one direction on both writers of all 40 layers over an unmeasured Heretic pass, at the sizes of the maker's Mag-Mell pass matrix by matrix and 0.84 from its direction; exactly 0 outside (finding 173) |
| 8 | SicariusSicariiStuff/Impish_Bloodmoon_12B_Abliterated | SicariusSicariiStuff/Impish_Bloodmoon_12B | violations against `directional-per-layer-selected`, 15 flags (first shares 0.754 to 0.989) | a per-layer pass in two kernels' shapes, the attention outputs of layers 15 to 32 peaking at 24 and the down projections of 29 to 39 rising to the last layer, by the maker of the parent; exactly 0 outside |

Nothing moved outside the matrices the methods reach on any pair: the largest relative change outside the changed
set is exactly 0 on all eight, with no traces under the threshold. All eight copies edit the writers alone: no
query, key, value, gate or up projection moved on any pair, no norm and no embedding, and on pair 1 neither tower
nor any per-layer gate or projection. The cards of the seven new copies were not read in this pass; the reading
notes judge each copy by the form its weights take, and pair 1's by the card round 39 read.

Pair 1 is the direct measurement finding 100 asked for. Against google/gemma-4-E4B at `7aa32e68` it changes 23 of
2,130 tensors, the attention outputs inside the card's 24.83 less and plus 8.80 and the down projections inside
35.18 less and plus 3.09, highest at layers 25 and 35 beside the kernels' peaks, and the three values round 39 read
by byte range inside the windows (0.0209, 0.0284 and 0.0283) come back to the fourth digit. The leading directions
stand at 0.015 to 0.217 at the median to six edits of the instruct E4B.

The two Mag-Mell passes carry one direction, 0.9997 on the output side on all 80 matrices, on the same profile
across layers, and Naphula's difference norms are 1.24 times EldritchLabs's at the median (1.15 to 1.30). The
copy whose name says Scale1.2 is the smaller. EldritchLabs's two passes, made two hours and thirty-seven minutes
apart on 2026-03-05, move their matrices by the same fraction (the ratio 1.0009 at the median, 0.92 to 1.07) on two
parents whose matrices have the same norms, and their directions stand at 0.840 on every layer: one setting, a
direction found again on each parent.

llmfan46's two passes on yuxinlu1's two fine-tunes stand at 0.963 to each other and edit one shared direction from
early layers to the last; on the coding fine-tune the pass stands at 0.957 to tpls's abliteration and 0.899 to
richardyoung's Heretic pass and at 0.463 to huihui-ai's projection, the split finding 127 read. tpls's second edit,
of its own SFT of the coding fine-tune, stands at 0.05 to all three on the seven names it moved.

Pair 8's maker edits its own fine-tune in two kernels' shapes with a direction that turns across layers (0.558
between layers), at 0.20 to 0.28 to the other Nemo measurements this round and before.

Preservation claims. No changed matrix on any pair keeps its row norms (the preserved count is 0 on all 451 changed
matrices of the round), pair 7's MPOA among them; the cards' claims are not read here.

Fingerprints. The two llmfan46 copies were created nine days apart (2026-06-21 at 21:30 and 06-30 at 18:04), the
second seventeen hours after its parent's pinned commit, and both are transformers 5.12.1 saves over 5.10.2 parents
with the same rewritten template. tpls's copy is a 5.12.1 save over a 5.13.0.dev0 parent committed seven hours and forty-two minutes
earlier.
The two EldritchLabs copies were created at 06:30 and 09:07 on 2026-03-05. Naphula's measured revision is of
2026-05-25, five months after its repository was created and eleven weeks after the EldritchLabs copy whose card
names it.

Directions. This round placed every copy's saved vectors against earlier measurements (finding 66's check): pair
1 against six edits of the instruct E4B and Felldude's training on the pretrained one; pairs 2 to 4 against the
three earlier edits of yuxinlu1's coding fine-tune and huihui-ai's of the agentic one; pairs 5 to 8 against one
another and against 0xA50C1A1's and grimjim's passes of Nemo Instruct. The numbers are in the reading notes.

## The token side

The cluster's cards read "unexplained differences" on pairs 1, 2, 3 and 7, "undecided" on 4, 5 and 6 and
"consistent" on 8, and the home judgement left all eight there. Pair 1 differs in 4 fields: the two version strings
(5.5.0.dev0 to 5.5.0), `text_config.moe_intermediate_size` (closed at home by the default rule) and the template,
which the pretrained checkpoint does not ship and the copy carries; the end-of-sequence ids that stayed open
against the instruct model in round 39 do not differ against the base. Pairs 2 and 3 differ in the version strings
(5.10.2 to 5.12.1) and a template rewritten beyond line endings, which renders the fixed conversation the same.
Pair 4 differs in the version strings alone, and its template fails to render on both sides (an unknown
`generation` tag). Pairs 5 and 6 differ in nothing compared, with no generation file on either side. Pair 7 drops
the parent's chat template. Pair 8 drops `_name_or_path` (expected).

## What the scorer learned

The assessment and the nearest recipe are the same on the cluster and at home on all eight; the home re-score
measured the within-layer agreement from the saved direction files and kept the group references of the cluster's
comparison. The flags' causes, by pair:

- Kernel passes, 2 and 15 flags (pairs 1 and 8): first shares under the 0.99 floor at the kernels' tails, where the
  changes are smallest, 0.0126 and 0.0148 on pair 1 and 0.0017 to 0.0134 on pair 8.
- Shared-direction passes, 22 and 7 flags (pairs 2 and 3): direction cosines where the direction turns on early
  layers (pair 2) or the two writers part on three late layers (pair 3), and one first share each.
- A small selected pass, 6 flags (pair 4): first shares of 0.971 to 0.989 on changes of 0.006 to 0.013.
- One-direction passes on every layer, 0 flags (pairs 5 to 7).

## What stays open

To the reading: the seven new copies' cards, so that each pass can be read against its printed parameters and
EldritchLabs's Scale1.2 card against the Naphula revision it names; Naphula's revision history, to find whether an
earlier revision carried a different size; the side of each edit; and the leftover outside the first direction on
pairs 4 and 8. To the pinner: p-e-w's noslop pass against mistralai/Mistral-Nemo-Instruct-2407, owed from round
28's pairing, which would separate what EldritchLabs's second pass touched from what p-e-w's first did and place
its direction. To the metadata tool: a template the original does not ship read beside the re-save rule (pair 1);
a template that fails to render on both sides (pair 4). To the recipe library: the shared-direction entry with a
turn tolerance that round 44 asked for (pairs 2 and 3); a first-share floor read against the size of the change
(pairs 1, 4 and 8); and a scale line between two copies on one parent along a shared direction (pairs 5 and 6). To
the pinner's names step: the vocabulary-resize rule the held Janus pass needs.

## Operational

The round ran on Nautilus: the sweep deleted the seven originals and kept none, with none absent. Round 46 is read
out after round 44 and after rounds 47, 49, 51 and 52, which ran on Wheat. The pull (card 5854) carries the eight measurement folders (card,
metadata, weights, direction vectors and the measurement record of each) and the sweep record; no job log was
pulled, so the nodes and seconds are not recorded, and the job ids come from the round's waiter. The home judgement
ran under transformers 5.22.1. No matrix was read from the hub by byte range this round and no card was read from
the hub; the saved direction files were compared with the earlier pull copies' on the names the reading notes give.
The numbers in this note and the reading notes come from the measurement reports, the home judgement, the home
re-score and those comparisons.

Weight differences alone cannot certify the absence of hidden behavior.
