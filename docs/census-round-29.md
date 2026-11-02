# Census round 29: eight pairs on Blueback, the first measured through the tower and prefix mappings (2026-11-02)

Eight published copies compared with their stated originals on Blueback from the batch pinned as
`data/batches/round-29-batch-1.json` (pinned 2026-10-31 19:12Z), the first batch on the kit that lists a vision or
audio tower the export left out: Pranavz's Hearthfire heretic (a text-only save of a Mistral Small 3.2 edit, the
vision tower and projector gone) and minpeter's Voxtral Mini 3B heretic (the audio tower gone), both held from
earlier rounds for that reason; beside them akpsahan's upload of the huihui 31B second version, claymorecrystal's
26B-A4B, three E4B copies of the instruct model (NullpoLab, alphakek, senjiangchen) and Felldude's copy declared
against the pretrained E4B. The pull of 11-02 00:00Z brought home the eight measurement folders and the sweep record
and no job log, so the download, compare and sweep job numbers and their seconds are not recorded in this note; the
sweep deleted the seven original checkpoints (`6eaac59a` of the Mistral Small 3.2 instruct original for pair 1,
`0b3e8030` of the Voxtral original for pair 2, `8ee0b411` of the 31B original for pair 3, `5f505b5a` of the
26B-A4B original for pair 4, `ed9be084` and `37a42740` of the E4B instruct original for pairs 5 and 6, and 7, and
`fc1eaf3f` of the pretrained E4B for pair 8) from `/p/work1/sdegan/model-audit/rounds/29/originals/`. The batch was
pinned before the duplicate rule (finding 38) and carries three measurements the rule would have refused (pairs 3,
4 and 7). The pinner's note held back four copies (TurkishCodeMan's E2B export of 18 layers against the original's
35, sitten1's 26B-A4B for room, and OS-Software's and TheUmbraWalker's E4B copies, named after the instruct model
but carded to the pretrained base, to be pinned against the instruct model); pair 8 is that case admitted. The
eight measurements were re-scored at home with the recipe table as committed and the saved direction vectors, and
no flag count moved. Every metadata report was judged again at home under transformers 5.22.1 with the originals'
commit histories, and the committed reports carry that judgement. Each pair has a card (the tool's Stage 1 text
after the home judgement, with the Stage 2 line) and a reading note in `docs/cards/`; the measurements are in
`results/weights/` and `results/meta/`, and the direction vectors stay in the pull copy
(`/opt/ai/hpc-packages/pulls/model-audit/blueback29/measurements/pair-N/`).

| Pair | Copy | Original | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | Pranavz/Hearthfire-24B-heretic | mistralai/Mistral-Small-3.2-24B-Instruct-2506 | violations, 347 flags (201 unexpected changes, 65 first shares, 80 direction cosines, one cross-kind) | a Heretic 1.2.0 edit on LatitudeGames/Hearthfire-24B, the fine-tune the README's title names and the `base_model` field does not: all 282 language tensors changed by 0.4 to 7.6 percent, the down-projection kernel readable through the training on all 40 layers (2.7 at the card's centre layer, 3.6 at layer 38) and the attention-output kernel's window on layers 19 to 34; the first pair measured through the prefix mapping (363 names under `language_model.`, 222 vision tensors the export left out) |
| 2 | minpeter/Voxtral-Mini-3B-Text-2507-hf-heretic | mistralai/Voxtral-Mini-3B-2507 | match, 0 flags | the card's Heretic 1.0.1 kernel pair read to the second decimal on the text tower of a speech model: the attention outputs of layers 9 to 26 at 0.99 to 1.26 (the card's 0.98 to 1.27 centred on 17.46) and the down projections of 7 to 29 at 1.02 to 1.10 (the card's 1.02 to 1.11); 232 language tensors equal to the release, the audio tower's 489 tensors mapped as left out; finding 7's third case closes |
| 3 | akpsahan/Huihui-gemma-4-31B-it-abliterated-v2 | google/gemma-4-31B-it | match, 0 flags | "Duplicate from huihui-ai/Huihui-gemma-4-31B-it-abliterated-v2": the maker's two shards under their checksums (`9a11eda6e0`, `bc366b3f1b`), every field equal to the round 12 report (110 matrices at weight 1.5), the first re-upload of the second version |
| 4 | claymorecrystal/gemma-4-26B-A4B-it-uncensored | google/gemma-4-26B-A4B-it | violations, 31 flags (the 30 packed expert tensors, one within-layer cosine) | "Duplicate from TrevorJS/gemma-4-26B-A4B-it-uncensored": TrevorJS's two shards under their checksums (`4b988df4e5`, `3d2388e809`), every field equal to the parent's second pass, the fourth repository on that file |
| 5 | NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals5 | google/gemma-4-E4B-it | violations, 51 flags (29 first shares 0.86 to 0.98, 22 within-layer cosines) | the card's Heretic arbitrary-rank edit (the L-BFGS branch) on the attention outputs of layers 19 to 36 and the down projections of 21 to 34, inside the card's 19 to 42, nearly one direction per matrix (fourth cumulative share 0.95 to 0.99), input side at 1.24 to 2.50, seven more down projections in the window rewritten under the threshold; rows moved 0.001 to 0.037 under no claim |
| 6 | alphakek/gemma-4-E4B-it-heretic-mythos-v1 | google/gemma-4-E4B-it | violations, 68 flags (34 first shares 0.006 to 0.96, 34 within-layer cosines) | a private Heretic fork's edit under a card that names no method: both writers of layers 11 to 27, a direction per matrix on 32 of 34 (input side, 1.04 to 2.04), two down projections (layers 16 and 20) left as residues of 0.14 and 0.17 percent with no direction, rows moved 0.0057 to 0.0078 on the 32, the band finding 22 reads on every Heretic copy that claims the step |
| 7 | senjiangchen/gemma-4-E4B-it-uncensored | google/gemma-4-E4B-it | violations, 6 flags (within-layer cosines on layers 5, 30 and 33) | "Duplicate from TrevorJS/gemma-4-E4B-it-uncensored": TrevorJS's file under its checksum (`37605ec579`), every field equal to the round 8 report, the second repository on that file |
| 8 | Felldude/gemma-4-E4B-uncensored | google/gemma-4-E4B | violations, 680 flags (510 unexpected changes, 85 first shares, 84 direction cosines, one cross-kind) | a copy declared against the pretrained base that stands on the instruct model: 592 of 664 language tensors changed by 0.1 to 160 percent against the base with the vision and audio towers equal, and the instruct model's template and end-of-sequence ids; read from the hub by byte range against google/gemma-4-E4B-it, the normalisation vectors equal byte for byte and nine matrices at 0.00003 to 0.0058, a light fine-tune of the instruct model, as the card's captioning line says |

Nothing moved outside the matrices the maker's method reaches in pairs 2, 3, 4, 6 and 7 (the largest relative
change outside the changed set is exactly 0) and in pair 5 beyond the seven in-window down projections the search
weighted under the threshold (0.00006 to 0.00025). Pair 1 changed every language tensor, the fine-tune's doing, and
pair 8 changed every language tensor but 72 against an original it does not stand on. The round's result is four
edits read, three hub duplicates and one copy measured against the wrong model. Three of the four edits read as
their cards say (pair 2 in both kernels to the second decimal, pair 5 in method and window, pair 1 in the method
named in its title and in the down-projection kernel through the training), and one (pair 6) reads a Heretic-shaped
edit under a card that says only "a private fork" and promises a write-up later. The three measurements the duplicate rule
would have refused cost three downloads and three compares for results the repository already held.

The weights read off the weights. Pair 2's kernels against the card: the attention output of layer 17 keeps -0.259
of the original's action along the shared direction, the card's 1.27 at position 17.46, and the kernel falls to
0.008 at layer 9 and 0.012 at 26, the card's 0.98 at distance 8.89; the down projections keep -0.102 at layers 21
and 22, the card's 1.11 at 21.50, and -0.024 at layer 7 and -0.063 at 29, the card's 1.02 at distance 15.14. One
direction on all 41 (within kinds at 1.0000, across kinds at 0.99999), output side, the left below the right on 41
of 41. Pair 1's down projections against the card through the training: the kept fraction along each layer's
leading output direction is -1.71 at layer 14 (a weight of 2.71 against the card's 2.66 at 14.59), -1.59 to -2.08
on layers 1 to 13, -1.52 to -1.80 on 15 to 25, then rising to -2.60 at layer 38 (3.60 against the card's 3.73 at
distance 25.63), with layer 0 at -0.61; the attention outputs keep -0.13 to -2.22 on layers 19 to 34, the card's
window (26.51 and 8.14), and 0.99 to 1.01 outside it, where only the training reached. Pair 5 reads no single
weight: the attention outputs keep -0.24 to -1.50 along their leading input directions and the down projections
-0.56 to -1.08, the left above the right on 29 of 29. Pair 6 keeps -0.04 to -1.04 on its attention outputs and
-0.77 to 0.01 on its down projections, input side, the left above the right on 32 of 32, and on layers 16 and 20
the down projections keep 0.98 and 1.00 of everything (residues). Pairs 3, 4 and 7 read their parents' numbers:
-0.497 to -0.501 on 110 matrices (weight 1.5), a median 0.03 to 0.18 kept on the output side of the 26B-A4B's 60
dense writers, and 0.03 to 0.77 and 0.01 to 0.54 on the E4B's two writers. Pair 8's numbers against the base are the
instruction tuning's and read nothing.

Preservation claims. Pair 6 claims nothing and reads 0.0057 to 0.0078 on its 32 edited matrices, the seven tenths of
a percent every Heretic copy that claims row-norm preservation leaves (finding 22), so the fork keeps the step and
the card omits it. Pair 5 claims nothing and moved its rows 0.001 to 0.037. Pair 2 claims nothing and moved its rows
0.025 to 0.056 on all 41, the largest band for a plain shared projection in the census, on a hidden size of 3,072.
Pair 1's rows moved 0.001 to 0.24 on the down projections under the training. Pairs 3, 4 and 7 inherit their
parents': up to 0.643 on huihui-ai's weight-1.5 edit, within 0.0012 and 0.0004 on TrevorJS's restorations.

Fingerprints. Fifteen measurements now stand on the 31B instruct original's weight file; pair 3 carries huihui-ai's
two shards and equals the round 12 report. Fourteen stand on the 26B-A4B instruct original's file; pair 4 carries
TrevorJS's two shards, the fourth repository on them. Twenty-three stand on the E4B instruct original's file; pair
7 carries TrevorJS's shard (`37605ec579`), and pairs 5 and 6 share no field with anything. Six stand on the Mistral
Small 3.2 instruct original; pair 1's ten shards match nothing. Pairs 2 and 8 are the first measurements on the
Voxtral original and on the pretrained E4B. Every one of the three duplicates was measured against a later Google
revision than its parent was (pair 3 against `842da379` where the parent read `439edf56`, pair 4 against `20da991a`
where the parent read `47b6801b`, pair 7 against `83df0a88` where the parent read `292a7e27`), and every field
equals the parent's report to the last digit, because the weight files of those revisions carry the same
checksums: Google's revisions of these repositories changed the template and the configuration and never a shard.

## The token side

The cluster's cards read "unexplained differences" on all eight, every one on configuration or template fields and
none on a weight. Re-judged at home under transformers 5.22.1, six fields move and two cards change their reading
to "consistent with re-save noted": pair 5, where `text_config.moe_intermediate_size` closes by the default rule
and the copy's 16,804-byte template is found equal to Google's own later revision `c53e9d33` of 04-28 ("fix
(chat_template): update SI and tool call handling") by the later-revision rule, the copy having been refreshed on
04-29; and pair 6, where the same field closes and the 5.6.0.dev0 version string is all that remains. The field
closes on pair 7 too, and `head_dim` closes on pairs 1 and 2 by the default rule. What stays as printed:

- Pairs 1 and 2: the conversions' token tables, 1,027 and 2,032 fields. Neither original ships a library tokenizer
  (`tekken.json` on both, finding 31), so the copies' `tokenizer.json`, tokenizer configuration and template have
  nothing on the original's side to compare on, and the tool marks the four files missing there. Pair 1's files
  are the fine-tune's: a 292-byte ChatML template, `<|im_end|>` (id 999) as the end-of-sequence token beside the
  original's id 2, the same 292 bytes LatitudeGames ships. Pair 2's are the maker's own text-only conversion's
  (minpeter/Voxtral-Mini-3B-Text-2507-hf): a 741-byte template and the Mistral special-token table. Both copies
  save a flat `MistralForCausalLM` configuration where the original nests a `text_config` under
  `Mistral3ForConditionalGeneration` and `VoxtralForConditionalGeneration`, so the same hidden size, layer count
  and rotary base appear as moved fields, and the model type change the exception table allows is the one
  "expected" entry on each. The tool cannot render the fixed conversation on the original's side.
- Pair 3: the earlier-revision template through a re-upload, huihui-ai's 12,045-byte file under a pin of 07-20
  whose Canonical file is 18,683 bytes, the case the parent's own round 12 reading closed by hand.
- Pair 4: the same through TrevorJS's 12,045-byte file of the 26B's 04-02 revision under the 06-03 pin (17,466
  bytes).
- Pair 7: the same through TrevorJS's 11,926-byte file of the E4B's 04-02 revision under the 04-10 pin (16,317
  bytes), the case lessans's copy of the maker's E2B file read in round 22.
- Pair 8: three `eos_token_id` fields (`[1, 106]` in the configuration and the tokenizer, `[1, 106, 50]` in the
  generation settings, against the base's single id 1) and a 17,336-byte template the base does not ship. All four
  are google/gemma-4-E4B-it's values and file at the revision current when the copy was made, correctly read as
  differences against the base and, read against the instruct model, no difference at all.

Every fixed conversation the tool could render in the round renders identically under both templates.

## What the scorer learned

The flag counts are the same on the cluster and at home. Their causes, by pair:

- A Heretic edit under a fine-tune, 347 flags (pair 1): 201 unexpected changes on the queries, keys, values, gates,
  up projections, the embedding and the head, which the training reached and no projection does; 65 first shares,
  of which 24 are attention outputs outside the kernel's window carrying only the training (0.06 to 0.26) and 16
  inside it carrying both (0.90 to 0.97); 80 direction cosines, since the training has no direction; and one
  cross-kind flag. As finding 18's pairs, the parent (LatitudeGames/Hearthfire-24B, unmeasured) must be measured
  as a separate term before the edit's strengths can be read on the attention outputs.
- A copy standing on another model, 680 flags (pair 8): every count is the instruction tuning's. The flags are the
  pinner's to prevent, not the scorer's to read.
- Arbitrary rank by a solver with a near-one spectrum, 51 flags (pair 5): 29 first shares of 0.86 to 0.98 (the
  fourth cumulative share 0.95 to 0.99) and 22 within-layer cosines of 0.003 to 0.15, each matrix its own
  direction. Beside Bahushruth's solver in round 26 (first shares 0.19 to 0.79), this branch's result is nearly a
  projection per matrix.
- Per-matrix directions and two residues, 68 flags (pair 6): 32 first shares of 0.51 to 0.96, two of 0.006 and
  0.030 on the residues, and 34 within-layer cosines of 0.01 to 0.14.
- The parents' flags (pairs 3, 4 and 7): 0, 31 (the 30 packed expert tensors with no singular values, and layer
  12's two writers at 0.949) and 6 (layers 5, 30 and 33 at 0.934 to 0.947).
- No flag on pair 2, the first measurement on a text tower cut from a speech model.

The round's finding for the measure is the mapping: pair 2 pairs 273 names after 489 audio-tower names are set
aside as a tower the export left out, and pair 1 pairs 363 names after a `language_model.` prefix is stripped from
the original's side and 222 vision names are set aside, where round 8's copy under the same prefix paired nothing
(finding 14) and round 26 held darkc0de's copy for the same reason. Both pairs measure, and pair 2 measures clean.

## Owed to the metadata tool

Added since: nothing this round. What remains: the conversion lookup when the original ships no library tokenizer
(pairs 1 and 2, finding 31's rule, with the Voxtral release as a third such original and the Hearthfire export as
a fourth source of token files); a flat-against-nested configuration rule for text-only saves of a wrapped model
(pairs 1 and 2, where the same values stand at two depths); the earlier-revision template through a re-upload
(pairs 3, 4 and 7, three more); and a reading of the instruct template on a base-declared copy as the parent marker
it is (pair 8, finding 26's case). To the pinner: a copy whose `base_model` field names a pretrained base while it
ships a chat template and the instruct model's end-of-sequence ids is pinned against the instruct model, the rule
the batch note applied to two held copies and not to pair 8; and the three duplicates, which the checksum rule
refuses.

## Operational

The pull of 11-02 00:00Z carries the eight measurement folders (card, metadata, weights, direction vectors and the
sha256 record of each) and the sweep record; no job log came home, so the jobs' numbers, nodes and seconds are not
in this note. Every compare finished with its card and its weights report, and the sweep ran after all eight and
deleted the seven originals. The home judgement ran under transformers 5.22.1. One reading was made at home from
the hub by byte range (`tools/hub_range_read.py`): fourteen tensors of pair 8's copy against google/gemma-4-E4B and
google/gemma-4-E4B-it, no download.

Weight differences alone cannot certify the absence of hidden behavior.
