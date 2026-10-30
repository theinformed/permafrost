# Census round 8: eight Gemma 4 and Ministral 3 pairs (2026-10-30)

Eight published copies compared with their stated originals on Blueback, 2026-10-30, from the batch pinned as
`data/batches/round-8-batch-1.json`: round card 5305, download job 3397500, compares 3397501 to 3397508 (exit 0),
sweep 3397509, which deleted the six original checkpoints (two were shared between pairs: `292a7e27` of the E4B
original by pairs 1 and 3, `5926caa4` of the 12B original by pairs 6 and 7). Card 5347 pulled the measurements home.
They were re-scored with the recipe table as committed today and the saved direction vectors; the kit carried the
same table, so no flag count moved. Every metadata report was judged again at home under transformers 5.6.2 with the
originals' commit histories, as rounds 3 and 7 found necessary for Gemma 4 copies (the kit's pinned 4.56.2 has no
Gemma 4 class and the compute nodes have no hub access). Each pair has a card (the tool's Stage 1 text after the
home judgement, with the Stage 2 line) and a reading note in `docs/cards/`; the measurements are in `results/weights/`
and `results/meta/`, and the direction vectors stay in the pull copy
(`/opt/ai/hpc-packages/pulls/model-audit/blueback8/measurements/pair-N/`).

| Pair | Copy | Original | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | TrevorJS/gemma-4-E4B-it-uncensored | google/gemma-4-E4B-it | violations, 6 flags (three layers' direction cosines) | consistent with the card: one direction per layer on every attention output and down projection, row norms within 0.0004, scale 1.0 with the biprojection's second term |
| 2 | Jiunsong/supergemma4-e4b-abliterated | google/gemma-4-E4B-it | violations, 2,850 flags (names) | not measured: the copy is the text model under a `language_model.model.` prefix without the audio and vision towers, so no tensor was paired; its template adds a fixed system text to every conversation |
| 3 | coder3101/gemma-4-E4B-it-heretic | google/gemma-4-E4B-it | violations, 21 flags (energy shares) | consistent: arbitrary-rank edits on the 21 attention outputs of layers 21 to 41, input side, weights 1.32 to 2.02; the claimed row-norm preservation reads 0.007 |
| 4 | Madras1/Gemma-4-E4B-Abliterated-Uncensored | google/gemma-4-E4B-it | violations, 81 flags (54 absent tensors, 27 gate projections) | consistent: one direction at weight 1.355 (card 1.35) on attention output, down and gate projections of layers 8 to 34; the copy omits 54 unused key-value tensors and its loader moved the end-of-sequence token |
| 5 | llmfan46/gemma-4-E2B-it-ultra-uncensored-heretic | google/gemma-4-E2B-it | violations, 7 flags (energy shares) | consistent: arbitrary-rank edits on the 7 attention outputs of layers 17 to 23, input side, weights 1.86 to 4.41 |
| 6 | TrevorJS/gemma-4-12B-it-uncensored | google/gemma-4-12B-it | violations, 1 flag (floor) | consistent: one direction per layer on the attention output and down projection of layers 15 to 47, row norms within 0.0004 |
| 7 | richardyoung/gemma-4-12B-coder-fable5-composer2.5-v1-heretic | google/gemma-4-12B-it | violations, 628 flags | consistent with the card, which names a coding fine-tune as the parent: dense training on all 557 changed tensors, with one shared direction on the attention outputs of layers 15 to 47 and the down projections of layers 24 to 42 on top; the `base_model` field names the grandparent |
| 8 | ccharnkij/Ministral-3-8B-Reasoning-2512-Uncensored | mistralai/Ministral-3-8B-Reasoning-2512 | violations, 307 flags | consistent with the card's "LoRA": a low-rank change on all 238 projections of 34 layers, nothing projected out (remaining fractions 0.94 to 1.05), embedding, head, norms and vision tower unchanged |

In the seven measured pairs nothing moved outside the matrices the maker's description reaches: the largest relative
change outside the changed set is exactly 0 in six and 0.00099 in pair 7, where it is the normalisation vectors of
the fine-tune that stayed under the 0.001 threshold. Five of the seven are ablations and read as their cards say,
with the weight and the side of the edit read off the weights: 1.355 against the card's 1.35 on pair 4, scale 1.0
under a biprojection on pairs 1 and 6, searched per-layer weights of 1.32 to 2.02 and 1.86 to 4.41 on the input side
of the attention outputs on the two arbitrary-rank copies. The two others are training. Pair 8 is the first copy in
the census whose refusal removal is a merged adapter with no projection at all: 238 matrices changed by 0.6 to 1.8
percent, the first eight directions of each carrying 67 to 99 percent of the change, and 0.94 to 1.05 of the
original's action kept along every leading direction. Pair 7 is a coding fine-tune with an ablation on top, measured
against the grandparent its `base_model` field names while its card names the parent; the measures separate the two
(first-value share 0.93 to 0.99 against 0.02 to 0.80, cross-layer agreement 0.90 to 0.998 against 0.10 to 0.14), and
they cannot read the ablation's weight through the training, so the pair against the parent
(yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1 at `237e5d8e`) is owed to the next batch beside the 3MPER0RR pair
against its instruct parent.

Pair 2 was not measured. The copy carries 719 tensors under `language_model.model.` and the original 2,130 under
`model.`; every one of the 719 names is a language-model name of the original once the prefix is removed, and the
audio tower (752 tensors), the vision tower (659) and their two embedding projections are absent from the copy. The
comparison strips three wrappers and this is a fourth, so it paired nothing and its 2,850 flags count names. The card
describes training beside the ablation; the weight-level reading waits for a prefix rule and a second comparison.

No duplicate fingerprint turned up. The seven E4B copies now measured (round 2's llmfan46 copy, round 7's huihui-ai,
prithivMLmods and llmfan46 ultra copies, this round's pairs 1, 3 and 4; pair 2 has no measurement) all stand on one
original weight file (shard `cfbd3d2f`), and the three 12B copies (igorls, pairs 6 and 7) on another (`5a84cb31`);
across every pair of them no changed matrix has an equal measurement in any field, and the only equality in the
census remains the huihui-ai and prithivMLmods pair of round 7 (2,130 of 2,130 tensors equal).

## The token side

The cluster's cards read "unexplained differences" on seven of the eight pairs and "consistent with re-save noted" on
pair 8 (the kit's 4.56.2 has the Mistral 3 classes). Re-judged at home, pair 1 closes by tool (its one field is the
null `moe_intermediate_size`, a library default; its template is the pinned release template byte for byte) and its
committed card reads "consistent with re-save noted". The same field closes on pairs 3, 4 and 5 and two more on
pair 4 (`global_head_dim`, `num_global_key_value_heads`), and nothing else moves by tool. The remaining fields, pair
by pair, with what each is:

- Templates that match no commit of the original repository, four pairs. Pair 3 carries Google's 2026-04-10 template
  with 14 blank lines removed and nothing else; the copy's repository was created on 04-03, so the pin took the 04-02
  release template, and its weights of 04-14 carry the fix Google published four days before them. The later-revision
  rule compares byte for byte after line endings and trailing whitespace, and blank lines defeat it: a re-save
  effect in all but the rule's letter. Pair 5 carries Google's 2026-04-28 template plus a 14-line macro that accepts a
  list of types in a tool schema; it equals no commit of Google's E2B or E4B repository (neither has a pull-request
  branch) and renders the fixed conversation identically: a real change on the tool-schema path whose origin the
  hub does not show. Pair 4 carries Google's pinned 2026-07-20 template minus its header comment, with the branch
  that raised an error on string-valued tool arguments rewritten to render them: a real change by the loader. Pair 2
  carries Google's pinned 2026-04-10 template with a six-line block that writes a fixed system text ("You are a
  precise coding assistant" and three formatting rules) into every conversation and the system turn forced on, so
  the fixed conversation renders differently (545 bytes against 176), while its `tokenizer_config.json` still holds
  Google's unmodified template: a real change by the maker, and two templates in one repository.
- The four audio and vision values (`audio_samples_per_token`, `hidden_size`, `output_proj_dims` 640 and
  `model_patch_size` 48), absent from pairs 6 and 7 as they were from the igorls copy in round 7. Loaded at home under
  transformers 5.10.1 and 5.12.1, the versions that saved those copies, the original's configuration and the copies'
  both give 640, 640, 640 and 48; the values are the defaults of the library's unified Gemma 4 audio and vision
  configuration classes, which it omits when writing a configuration and restores when reading one, and a save of
  Google's own configuration under either version drops the same four fields. Re-save effects, on three copies by
  three makers under three library versions. Round 7 read the igorls copy the other way (its configuration "loads
  1024 for the hidden size, 1536 for the output projection"); those are the defaults of the library's other Gemma 4
  class, and under the class the copy's `model_type` selects it loads 640, 640, 640 and 48. Finding 11 is corrected
  accordingly.
- Data types repeated into sub-configurations where the original wrote null (pairs 6 and 7, audio and vision) or
  `float16` throughout (pair 7, inherited from its parent's configuration, which the copy's equals in every field
  but the version string). Re-save effects; the tool's repetition rule covers an absent original and should cover a
  null one.
- Pair 4's loader (transformers 5.16.1 with `unsloth_fixed: true` written into the configuration) moved the
  end-of-sequence token from `<eos>` (id 1) to `<turn|>` (id 106) in `tokenizer_config.json` and `config.json`
  (where the list [1, 106] became 106), added a pad token of 0 to the configuration and the special-token ids, and
  wrote `per_layer_config` with a head dimension of 512 for the seven global layers (the original's one
  `global_head_dim`). The generation settings keep [1, 106, 50], so generation under the library stops as before;
  a runtime reading the configuration or tokenizer alone stops at the turn marker only. Real changes, by the tool,
  outside the card.
- Pair 2's end-of-sequence list [1, 106] became [1, 106, 50] in the configuration, the generation settings' list
  copied up; and its `vision_config` is gone, in agreement with the dropped tower. Real changes consistent with the
  copy's files.
- Pair 8 is clean: ten re-save effects (version strings, four library defaults, three repeated data types, a pad
  token repeated from the generation settings), its template equal to the pinned January revision; Mistral replaced
  that template in July, after the copy.

## What the scorer learned

The flag counts are the same on the cluster and at home. Their causes, by pair:

- Name sets, 2,904 flags. Pair 2's 2,850 are a wrapper prefix the comparison does not strip (`language_model.model.`)
  and two towers the copy left out; pair 4's 54 are the key projection, value projection and key normalisation of
  the 18 layers that share key-value with earlier layers, which the original ships and never reads and the copy's
  loader omits. A prefix rule and a rule for tensors the configuration marks as unused would remove both.
- Dense training, 935 flags. Pair 7's 628 and pair 8's 307 are unexpected changes, energy shares and direction
  cosines on matrices no projection entry describes. A dense-change line (first share under 0.5 on readers and
  writers, remaining fractions near 1, every projection changed) would name both before any projection entry is
  tried, with a merged-adapter sub-case for pair 8 (slow singular-value fall, first eight shares 0.67 to 0.99, no
  shared direction) and a "training plus ablation" case for pair 7 (a shared direction at 0.90 to 0.998 across
  layers on a subset of the writers, with the dense change under it).
- Arbitrary rank, 28 flags (pairs 3 and 5), the energy-share profile that stays at 0.90 to 0.98 through the eighth
  value. Four copies of the method are now measured, all on the input side of the attention output, at weights of
  1.27 to 4.41; the candidate entry written in round 3 should widen its remaining-fraction band from "−1 to 0 on one
  side" to "below 0 on one side, weight reported", and one of the four (pair 3) claims row-norm preservation that
  reads 0.007.
- The gate projection, 27 flags (pair 4): an input-side kind the shared-direction entries should allow, as the
  per-layer entries allow query, key and value.
- Within-layer direction, 6 flags (pair 1): three layers at 0.934 to 0.947 under the per-layer entry's 0.95 line, on
  a method whose biprojection separates the two edits of a layer by a few degrees. Pair 6, the same method on the
  12B base, clears the line in all 33 layers (0.970 to 0.999).
- The floor, 1 flag (pair 6): a share of 0.9899 on a relative change of 0.017, leftover 0.0017.

The remaining fraction read the declared weight on pair 4 to two decimals (−0.355 on all 81 matrices against a card
of 1.35), as it read mlabonne's 1.5 in round 3 and huihui-ai's 2.5 in round 7, and it read the side of each edit: the
output side on the 54 writers and the input side on the 27 gate projections, as the card's two formulas say. It is
also what separates pair 8 from every ablation in the census (0.94 to 1.05 along every leading direction, nothing
removed). The row norms sort the restorations: 0.0001 to 0.0004 on the two TrevorJS copies (the tightest measured),
0.0018 to 0.0040 on the igorls copy of round 7, 0.007 on the coder3101 copy that claims preservation, 0.003 to 0.068
on the plain and scaled projections.

Two gaps in the comparison itself. A copy exported under another wrapper (pair 2) pairs no tensor and produces a
report with no measurement and 2,850 flags; the strip list should learn `language_model.model.` and report a
prefix-mapped comparison as such. A copy measured against its grandparent (pair 7) carries the parent's training in
every matrix; the dense-change line would say so, and the pin rule should read the card's first line as well as the
`base_model` field, since this is the second copy (after the re-upload in round 7) whose card names a nearer parent
than the field does.

## Owed to the metadata tool

A whitespace-normalised template comparison that drops blank lines (pair 3); a "two templates in one repository"
finding (pair 2); the class-default rule for the saving library's own configuration classes (pairs 6 and 7, and the
igorls correction); the repetition rule for a null original (pairs 6 and 7); the loader signature of `unsloth_fixed`
with its moved end-of-sequence token and added pad token (pair 4); a rule that reads a copy's configuration against
its card-named parent's before the original's (pair 7). And to the batch: the two parent pairs, pair 7 against
yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1 and the 3MPER0RR copy against Mistral-7B-Instruct-v0.3, and pair 2
again with the prefix rule.

Weight differences alone cannot certify the absence of hidden behavior.
