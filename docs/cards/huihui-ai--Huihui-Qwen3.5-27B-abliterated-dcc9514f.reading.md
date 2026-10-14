# Reading of the Stage 2 result: huihui-ai/Huihui-Qwen3.5-27B-abliterated against Qwen/Qwen3.5-27B (2026-10-13)

The automatic verdict says "recipe violations". On reading, the weights are consistent with a single-direction
refusal removal applied to a hybrid architecture. This copy carries a wider footprint than the 27B sibling: the
direction is projected out of the feed-forward down projections as well as the attention outputs.

- The base is the same hybrid family: linear-attention layers (output matrix linear_attn.out_proj) and full-attention
  layers (self_attn.o_proj), with a language_model prefix, plus a small multi-token-prediction head (mtp.layers).
  The recipe table in the kit knows only self_attn.o_proj and mlp.down_proj, so it filed the 48 changed
  linear-attention output matrices as "unexpected_change". This reflects the tool's naming table; the weights themselves show nothing anomalous.
- What changed: 130 matrices, every one a matrix that writes into the residual stream — 48 linear-attention outputs,
  16 full-attention outputs (self_attn.o_proj), 64 feed-forward down projections (mlp.down_proj), and 2 in the
  prediction head (one down projection, one attention output). Nothing outside that set moved: the largest relative
  difference elsewhere is 0.
- Each change is one direction: the leading directions agree across the changed matrices with cosine at least
  0.999984, and the first singular value holds at least 98.73 percent of each difference's energy. The 47
  "first_energy_share" flags are the down projections (and six attention outputs) sitting a little below the strict
  0.99 single-projection gate — expected, since down-projection abliteration is slightly less rank-pure than the
  attention-output edit, and still overwhelmingly rank-1.

What is new here, for the census: the same vendor uses a different projection footprint across its models. The 27B
sibling (Qwen3.8-27B) edited the attention outputs only; this one also edits every feed-forward down projection.
Same single-direction method, broader reach.

Verdict: consistent with the stated change (single-direction projection over attention outputs and feed-forward
down projections) on the weights; the template and token side is in the companion card. Pass lines for this hybrid
architecture are not yet in the kit, so the formal line stays "undecided until the recipe entry exists"; the kit
change is filed (brief 7). The original is pinned at today's revision; the rerun under the upload-date pinning rule
follows when that rule is in the kit.


## Update (2026-10-13, rescored with the architecture-aware classifier)

The hybrid attention names are now recognized, so the spurious naming flags are gone. Seventy flags remain. Sixty
eight are feed-forward down projections and attention outputs whose first-value energy share sits between 0.987 and
0.990, a touch under the recipe's 0.99 purity gate. Two are the multi-token-prediction head, whose names the kit
does not yet carry. The down-projection energy floor is a recipe-library question that the calibration pass will
settle; the verdict stays undecided until that floor is set.


## Update (2026-10-14, calibration on our own edit)

A single projection I applied myself to Mistral Small 3.2 24B drew 68 flags of this same kind, so the 0.99 floor
looks like the cause of these. bfloat16 rounding leaves 0.00152 to 0.00156 of each matrix's norm outside the first
direction on this copy, the same as on mine, and the shortfall follows the size of the edit in every kind. The earlier
line about down projections being less rank-pure does not hold. Scored in a scratch copy with the floor at 0.98, all
68 clear and the two prediction-head flags remain. This stays a hypothesis until a line calibrated for this base, or
the leftover rule, is in the scorer. Details: `docs/calibration-mistral-small-3.2.md`.
