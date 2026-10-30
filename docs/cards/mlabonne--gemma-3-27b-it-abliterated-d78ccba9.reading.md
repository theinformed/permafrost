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

## Second pass (2026-10-30)

Measured again on Nautilus, round 3 piece 2 (card 5055, download job 4080809, compare job 4080811, exit 0), on the
same pins (modified `eaa815df`, original `dfb98f29`) and the same shard checksums, with the comparison as of commit
d0f48bb. The second-pass report is `results/weights/mlabonne-gemma-3-27b-it-abliterated.pass-2.json`; its leading
vectors are in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus3/measurements/pair-2/weights.directions.safetensors`.

It reads as before: recipe match, `single-projection`, 0 flags, 124 changed tensors, 0 outside them. Every measure
both passes report is equal to the last digit, the within-layer agreement included (median 0.999997, minimum
0.99999).

The new measure confirms the card's number. Along the leading output direction of every one of the 124 matrices
the copy keeps −0.497 of the original's action (band −0.507 to −0.491, both kinds), so the weight is 1.50 within
0.01 on every matrix; the card says 1.5. Along the second to eighth directions it keeps 0.998 to 1.004, so nothing
else was touched. On all 124 matrices the left fraction is below the right one (right 0.0 to 0.99), the order of a
rank-one edit on the output side. This is the first declared weight the measure has been checked against, and it
reads it to two decimals.

On the token side the cluster's card reads "consistent with re-save noted" as before: the twenty added
configuration fields load as the library defaults under transformers 4.56.2, which knows this architecture, and
the result is the same at home. The re-judged report is `results/meta/mlabonne-gemma-3-27b-it-abliterated.pass-2.json`.
