# Reading of the Stage 1 and Stage 2 result: huihui-ai/Qwen2.5-32B-Instruct-abliterated against Qwen/Qwen2.5-32B-Instruct (2026-10-13)

This is the first census copy where the metadata audit finds a real divergence from the original, so this note covers
both the token side and the weight side.

## Token side (Stage 1): the padding token was changed

The automatic verdict is "unexplained differences". On reading, the change is genuine. The original pads with
`<|endoftext|>` (id 151643). This copy sets the tokenizer's padding token to `<|im_end|>` (id 151645), and adds a
padding-token entry to special_tokens_map.json where the original had none. The other token diffs in this copy are
the harmless re-save kind (the same strings and ids moved into a separate file).

Two things make this worth recording for the population study:

- A downstream user inherits a different padding token than the base model declares, with nothing in the card to
  say so. This is the undisclosed-drift class the field has flagged in abliterated copies.
- The copy also disagrees with itself: the tokenizer now pads with id 151645, while the generation settings still
  pad with id 151643. Code that reads one or the other will pad differently. For plain single-prompt generation this
  is harmless; for batched generation or any further training it is a quiet footgun.

The change is a common side effect of abliteration tooling that rewrites the chat tokens, and carries no sign of
hidden behavior on its own. It is logged as a divergence the census should count, and the best guess is a tooling default with no intent behind it.

## Weight side (Stage 2): a single-direction removal, plus one embedding touch

The weight verdict reads "recipe violations"; on reading it is a clean single-direction refusal removal on a
standard dense architecture.

- What changed: 129 matrices. Every attention output (64 self_attn.o_proj) and every feed-forward down projection
  (64 mlp.down_proj), plus the token embedding matrix once.
- Each change is one direction: the leading directions agree with cosine at least 0.99994, and the first singular
  value holds at least 98.77 percent of each difference's energy. The 75 energy-share flags are the down
  projections and attention outputs sitting just under the strict 0.99 gate, as expected for a down-projection edit.
- The single flagged embedding change lines up with the padding-token edit above; a changed token mapping moves the
  embedding matrix. It is one tensor and consistent with the token-side finding.

## Verdict

Weight side: consistent with a stated abliteration (single-direction projection over attention outputs and
feed-forward down projections). Token side: one real divergence, the padding token, logged as undisclosed drift with
an internal inconsistency a downstream user would not expect. The original is pinned at today's revision; the rerun
under the upload-date pinning rule follows when that rule is in the kit.


## Update (2026-10-13, rescored with the architecture-aware classifier)

The attention and feed-forward names are now recognized. Seventy-six flags remain. Seventy-five are down projections
and attention outputs with first-value energy between 0.988 and 0.990, just under the 0.99 gate. One is the
embedding matrix, which the token-side finding above already explains. The verdict stays undecided until the
down-projection energy floor is set in the recipe library.


## Update (2026-10-14, calibration on our own edit)

A single projection I applied myself to Mistral Small 3.2 24B drew 68 flags of this same kind, so the 0.99 floor
looks like the cause of these 75. bfloat16 rounding leaves 0.00151 to 0.00158 of each matrix's norm outside the first
direction on this copy, the same as on mine, and the shortfall follows the size of the edit in both kinds. Scored in
a scratch copy with the floor at 0.98, all 75 clear.

The embedding flag reads differently on a closer look. The change moved 71 percent of the embedding's entries, where
a padding-token remap would move one row, and its direction agrees with all 128 attention and down-projection
directions at cosine 0.99993 or better. The best guess is that the refusal direction was projected out of the token
embedding too. The padding-token change on the token side stands on its own.

Both points stay hypotheses until a line calibrated for this base, or the leftover rule, is in the scorer. Details:
`docs/calibration-mistral-small-3.2.md`.
