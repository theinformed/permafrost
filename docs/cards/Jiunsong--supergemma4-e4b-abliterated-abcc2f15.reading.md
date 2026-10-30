# Reading of the Stage 1 and Stage 2 result: Jiunsong/supergemma4-e4b-abliterated against google/gemma-4-E4B-it (2026-10-30)

Measured on Blueback, round 8 piece 2 (round card 5305, download job 3397500, compare jobs 3397501 to 3397508, all exit
0, sweep 3397509; pulled home by card 5347). Modified revision `5b76a44b` (2026-04-17), original pinned at `83df0a88`
(2026-04-10, 16:35Z). The maker's card calls the copy "abliterated and tuned", with quality recovery, formatting
discipline, better code output and serving hardening on top of the ablation; it gives evaluation scores and no
method, layer set, direction or training data.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection`, 2,850 flags, on the cluster and at
home. The flags count names and no weight was measured.

- 0 tensors matched. The original has 2,130 names under `model.` (719 in the language model, 752 in the audio tower,
  659 in the vision tower); the copy has 719 names under `language_model.model.` and no tower. After the prefix is
  removed every one of the copy's 719 names is a language-model name of the original, so the copy is the text model
  re-exported under another wrapper with the audio and vision towers and their two embedding projections left out.
  The comparison strips `model.`, `model.language_model.` and `transformer.` and nothing else, so it paired nothing.
- The 2,850 flags are 2,130 original-only names, 719 modified-only names and one missing changed projection.
- The copy is four shards (15.0 GB) against the original's one file, so there is no shard-level fingerprint to compare
  with the other E4B copies either.

The weight-level question is open. The card describes training beside the ablation, so a dense change is expected
when the pair is measured; a comparison with a `language_model.model.` prefix rule, against the same pinned revision,
is owed to the next round.

## Token and configuration side (Stage 1)

The tool's Stage 1 assessment is "unexplained differences" in six fields, before and after the home re-judgment (none
of the six is a library-default field, so the re-judgment changes nothing). The reading closes them by hand, and
four are real changes the card does not describe.

- `template.default`: the copy's `chat_template.jinja` (16,704 bytes) is Google's template at the pinned revision
  (16,317 bytes) with a six-line block added that defines a fixed system text ("You are a precise coding assistant",
  followed by three formatting rules) and with the condition that opens the system turn replaced by `if true`. Every
  conversation rendered with this template begins with that text, and a system message the user supplies follows it
  after a blank line. The fixed conversation renders differently (545 bytes against the original's 176). A real
  change, made by the maker, and the behaviour the card calls formatting discipline.
- `template_source.tokenizer_config`: the copy's `tokenizer_config.json` carries a template of its own, and it is
  Google's unmodified 16,317-byte template (`781d1094`). The repository holds two templates; the library reads
  `chat_template.jinja` first, older code reads the one in the tokenizer configuration, and the two render different
  conversations.
- `config.eos_token_id` and `special_token_ids.eos_token_id`: [1, 106] in the original, [1, 106, 50] in the copy, the
  list the generation settings already carry on both sides. The three ids agree across the copy's files; stopping
  behaviour under the library is unchanged.
- `config.vision_config`: present in the original, absent in the copy. The configuration describes the text model
  the copy ships, in agreement with the dropped towers; the audio configuration is still listed.
- `transformers_version` is 5.5.0.dev0 on both sides, so the saving library is unrecorded.

## For the recipe library

Undetermined at the weight level and a real change at the prompt level. The comparison needs a name-prefix rule for
the `language_model.model.` wrapper before this copy, and others exported the same way, can be measured; the
metadata tool needs to report two templates in one repository as a finding of its own. No direction file was saved
for this pair.

Weight differences alone cannot certify the absence of hidden behavior.
