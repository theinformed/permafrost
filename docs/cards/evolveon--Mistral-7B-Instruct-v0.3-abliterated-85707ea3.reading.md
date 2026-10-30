# Reading of the Stage 1 and Stage 2 result: evolveon/Mistral-7B-Instruct-v0.3-abliterated against mistralai/Mistral-7B-Instruct-v0.3 (2026-10-30)

Measured on Blueback, round 7 piece 8 (round card 5291, compare jobs 3392878 to 3392885, 4 to 6 minutes each, exit 0;
pulled home by card 5302). Modified revision `98c57aca` (2024-10-14), original pinned at `e0bc86c2` (2024-08-21). The
maker's card names the published abliteration article and its author's code as the method and says nothing more.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection`, 13 flags, on the cluster and after
re-scoring at home. All 13 flags are energy shares at the bfloat16 floor. On reading, the footprint is the article's
method applied to every layer, with the embedding edit that code makes.

- 65 of 291 tensors changed: the attention output and the feed-forward down projection in all 32 layers (64
  matrices) and the token embedding (0.0159 of its norm). Nothing else moved; the largest relative change outside the
  changed set is exactly 0.
- One direction, shared across layers and kinds: cosine 0.99999 or better with the median within each kind, 0.99999
  across kinds, 0.99999 within each layer.
- The weight is 1. Along the shared direction the copy keeps 0.000 to 0.004 of the original's action in all 64 layer
  matrices, a plain ablation. The embedding keeps 0.004 along its leading input direction, so its rows were projected
  orthogonal to the direction with the same weight; its first-value share is 0.9905 and 37 percent of its entries
  moved each way.
- Row norms moved by up to 0.021 on the layer matrices and 0.0019 on the embedding; no norm restoration.
- The 13 flags are the storage floor: first-value shares of 0.9890 to 0.9900 on matrices whose relative change is
  0.0146 to 0.0160, leftover 0.00153 to 0.00155 of the weight norm, with one minus the share at 0.92 to 0.93 of the
  floor law's prediction.

## Token and configuration side (Stage 1)

The tool's Stage 1 assessment is "consistent with re-save noted": the only difference is the library version string in the
generation settings (4.45.2 against 4.42.0.dev0). Every fixed conversation renders identically.

## For the recipe library

Consistent with the stated change on both sides. This is the cleanest weight-1 projection in the census so far and a
calibration point for the floor: at relative change 0.015, bfloat16 storage holds the first share at 0.989 to 0.990,
below the analytic 0.99 line, so the `single-projection` entry flags a textbook copy of its own method until the
scorer reads the leftover instead of the share. The saved direction vectors are not committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/blueback7/measurements/pair-8/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
