# Reading of the Stage 1 and Stage 2 result: mlabonne/gemma-3-27b-it-abliterated against google/gemma-3-27b-it (2026-10-29)

Measured on Nautilus, round 2 piece 2 (job 3763594, 23 minutes, exit 0). Modified revision `eaa815df` (2025-03-16),
original pinned at `dfb98f29` (2025-03-01). The maker's card names the method: a refusal direction computed per layer
from hidden states, applied with a refusal weight of 1.5.

## Weights (Stage 2)

The automatic verdict is "recipe match", nearest recipe single-projection, 0 flags. This is the first census upload
to pass the analytic line as published.

- 124 of 1,247 tensors changed: every attention output and every feed-forward down projection in all 62 layers.
  Nothing else moved; the largest relative change outside the 124 is exactly 0 and the vision tower is bit-identical.
- Each change is one direction, and it is the same direction everywhere: the leading directions agree with their
  kind median at cosine 0.99999 or better (minimum 0.999990), across kinds too. First-value energy share is at least
  0.9936. Relative change is 0.019 to 0.025, a tight band.
- The card says the direction was computed per layer. The weights say those per-layer directions were nearly
  identical in this model, or were replaced by one; the data cannot tell the two apart, and neither contradicts the
  card.
- Row norms were not preserved: the largest relative change in a row norm is 0.069. A refusal weight above 1 scales
  the projection past removal, which is what that looks like. The card says 1.5.

## Token and configuration side (Stage 1)

The automatic verdict was "unexplained differences": twenty configuration fields; the re-save rule for added fields
now classes all twenty as explained and the verdict reads "consistent with re-save noted". On reading, all twenty are fields
the original's config.json did not carry and the copy's does, with the values the library writes by default for this
architecture (attention_bias false, hidden_activation gelu_pytorch_tanh, vocab_size 262208, max_position_embeddings
131072, rope_theta 1000000, sliding_window_pattern 6, and so on). No field present in both files differs. The
tokenizer, special tokens and chat template are unchanged, and the fixed conversation renders identically. This is
the shape of a save through a newer library two weeks after the original's release. The tool judges an added field
against the installed library's defaults and records the version; under transformers 4.56.2, the round's pins, all
twenty load as the default (seventeen do under 5.6.2, which moved the rotary fields).

## For the recipe library

Consistent with the stated change on both sides, with one formal match on the weights. It is also a useful point for
the recipe library: a projection with weight 1.5 keeps the rank-one shape and the shared direction, and shows up in
the row norms rather than the singular values.

Weight differences alone cannot certify the absence of hidden behavior.
