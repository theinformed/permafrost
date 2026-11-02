# Reading of the Stage 1 and Stage 2 result: ressl/gemma-4-31B-it-uncensored against google/gemma-4-31B-it (2026-11-01)

Measured on Nautilus, round 20 piece 1 (download job 4143641, compare job 4143642, whose drop did not reach the desk,
sweep 4143650). Modified revision `b7e5c931` (eleven commits from 2026-07-08 15:56Z to 07-28, the weights uploaded
at 16:09Z on the first day and the README rewritten six times after), original pinned at `35487898` (06-03), the
revision current when the repository was created. The card names Google as the base, calls the copy "uncensored
(abliterated)", reports 0 of 686 effective refusals across four datasets and a KL divergence of 0.1234 against the
base, and prints no method, no layer and no weight.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer`, 56 flags, on the cluster and
after re-scoring at home. 120 of 1,188 tensors changed: the attention output and the down projection of every one of
the 60 layers, and nothing else (the largest change outside is exactly 0). Each change is rank one (first share 0.975
to 0.996, second cumulative share within 0.0008 of the first); the left kept fraction is below the right on 118 of
120 (output side); the two writers of a layer share a direction (cosine 0.93 to 0.999) that drifts across layers
(0.001 to 0.50 to the group direction); and the rows are back within 0.0004 of the original's norms on all 120.
The weights along the leading direction are 0.29 to 1.00 on the attention outputs (one minus a left kept fraction
of 0.00 to 0.71) and 0.43 to 1.00 on the down projections, deepest in layers 21 to 27 and 45 to 59. This is the
reach of TrevorJS/gemma-4-31B-it-uncensored (round 12) to the tensor: the same 120 matrices, output side, rows
restored to the same tolerance, one direction per layer. It is not that file: no field agrees, the kept fractions
differ by up to 0.37 and the largest absolute differences by up to 0.005, and the card does not name TrevorJS.
Two makers now ship the same method on this base.

The 56 flags are 54 first shares between 0.975 and the 0.99 floor, on matrices whose change is 1.4 to 2.5 percent of
the norm, and two within-layer cosines of 0.925 on layer 12. A per-layer entry with a 0.97 floor on 60-layer bases
would count the cosines alone.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster, two fields, and "consistent with re-save noted" at home. The two version
strings (5.5.0.dev0 to 5.13.0) close as a re-save. `text_config.moe_intermediate_size` is written as null by the
5.13.0 save where Google's file omits it and loads to the same default under transformers 5.22.1 (the rule from
round 19). The template is Google's own 18,683-byte revision of 07-15 (`ae53464b`, commit "fix: chat template")
of the 31B repository, later than the pin's 17,466-byte file; the later-revision rule read the original's commit
history and closed it, the first time that rule has closed a field at a round's own judgement. The tokenizer
configuration grew from 2,095 to 3,702 bytes with the same revision. The fixed conversation renders identically.

## For the recipe library

A second maker's edit with TrevorJS's reach and restoration under a card that states no method. The read-back is
clean enough that the kernel of the tool, if the maker named it, could be checked layer by layer; the per-layer
weights above are the numbers to check against. The pull copy keeps the direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus20/measurements/pair-1/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
