# Reading of the Stage 2 result: huihui-ai/Huihui-Qwen3.8-27B-abliterated against Qwen/Qwen3.8-27B (2026-10-13)

The automatic verdict says "recipe violations". On reading, the weights are consistent with a single-direction
refusal removal applied to a hybrid architecture, on a chosen subset of the layers.

- The base has 64 layers: 48 use linear attention (their output matrix is linear_attn.out_proj) and 16 use full
  attention (self_attn.o_proj). Tensor names carry a language_model prefix. The recipe table in the kit knows only
  self_attn.o_proj and mlp.down_proj, so it filed the 26 changed linear-attention output matrices under "other" and
  called the untouched expected matrices violations.
- What changed: 70 matrices, every one a matrix that writes into the residual stream (9 of 16 attention outputs,
  26 of 48 linear-attention outputs, 35 of 64 feed-forward down projections). Nothing else changed: the largest
  relative difference outside those 70 is 0.0.
- Each change is one direction: the first singular value holds at least 99.23 percent of the difference's energy
  where measured, and the leading directions agree across all 70 matrices with cosine at least 0.99999.
- The 38 expected matrices left untouched are a choice of layers, the pattern a tool makes when it selects layers by
  their measured effect.

Verdict: consistent with the stated change (single-direction projection, layer-selected) on the weights; the
template and token side is in the companion card. Pass lines for this hybrid architecture are not yet in the kit, so
the formal line stays "undecided until the recipe entry exists"; the kit change is filed. The original is pinned at today's
revision; the rerun under the upload-date pinning rule follows when that rule is in the kit.
