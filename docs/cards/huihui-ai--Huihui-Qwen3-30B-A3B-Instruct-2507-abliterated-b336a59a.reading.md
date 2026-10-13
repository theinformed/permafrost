# Reading of the Stage 2 result: huihui-ai/Huihui-Qwen3-30B-A3B-Instruct-2507-abliterated against Qwen/Qwen3-30B-A3B-Instruct-2507 (2026-10-13)

The automatic verdict says "recipe violations". On reading, the weights are consistent with a single-direction refusal
removal applied to every matrix that writes into the residual stream of a mixture-of-experts model.

- The base has 48 layers, each with 128 experts. The matrices that write into the residual stream are the 48
  attention output matrices and the 6,144 expert down projections (128 per layer). The kit's recipe table files expert
  down projections under "other", which produced the automatic verdict.
- What changed: exactly those 6,192 matrices out of 18,867 tensors. No other tensor changed.
- Each change is one direction: the first singular value holds at least 99.35 percent of the difference's energy, and
  the leading directions agree across all 6,192 matrices with cosine at least 0.99998.

Verdict: consistent with the stated change (single-direction projection, every layer) on the weights; the template and
token side is in the companion card. The kit change that teaches it expert down projections is filed. The original is
pinned at today's revision; the rerun under the upload-date pinning rule follows when that rule is in the kit.


## Update (2026-10-13, rescored with the architecture-aware classifier)

With the mixture-of-experts tensor names now carried in the kit, this report matches the single-projection recipe
with zero violations. The formal verdict for this copy is consistent with the stated abliteration.
