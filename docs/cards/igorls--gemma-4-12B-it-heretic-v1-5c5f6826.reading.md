# Reading of the Stage 1 and Stage 2 result: igorls/gemma-4-12B-it-heretic-v1 against google/gemma-4-12B-it (2026-10-30)

Measured on Blueback, round 7 piece 3 (round card 5291, compare jobs 3392878 to 3392885, 4 to 6 minutes each, exit 0;
pulled home by card 5302). Modified revision `192d14f6` (2026-06-04), original pinned at `66bc78a7` (2026-06-03,
21:50Z, the first README commit after Google squashed the repository's history at 21:14Z). The maker's card names
Heretic's directional ablation, "norm-preserving, biprojected", and reports 0 refusals in 100 at a KL divergence of
0.0284.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection-selected`, 9 flags, on the cluster and
after re-scoring at home. All 9 flags are energy shares at the bfloat16 floor. On reading, the footprint matches the
card.

- 22 of 677 tensors changed: the feed-forward down projection in layers 22 to 34 (13 matrices) and the attention
  output in layers 29 to 37 (9 matrices) of 48. Nothing else moved; the largest relative change outside the changed
  set is exactly 0. The 677 names are the same on both sides: the text model, the audio and vision embedding
  projections and the vision patch embedder. The 11 tensors outside the text model are unchanged.
- One direction, shared across layers: cosine 0.9925 to 0.9991 with the median (0.998 in the middle), 0.986 across
  the two kinds. That is the tool's `direction_index` setting, one residual direction (or an interpolation of two
  neighbouring ones) applied to every chosen layer.
- The weight varies by layer and by component, as the tool's weight kernel does. Along the shared direction the copy
  keeps -0.38 to -0.08 of the original's action on the down projections (a weight of 1.08 to 1.38) and 0.30 to 0.51
  on the attention outputs (a weight of 0.49 to 0.70).
- Row norms moved by 0.0018 to 0.0040 relative. That is above the 0.0011 line the two norm-preserving copies of round
  2 held and well under plain projections of this size (0.003 to 0.025 in piece 5), which fits the source's
  approximate norm restoration.
- The 9 flags are the storage floor: first-value shares of 0.981 to 0.988 on relative changes of 0.010 to 0.013,
  leftover 0.00142 to 0.00148 of the weight norm, inside the calibrated 0.0025 line.

## Token and configuration side (Stage 1)

The tool's Stage 1 assessment is "unexplained differences" in six configuration fields, before and after the home re-judgment.
The copy was saved with transformers 5.10.1 against the original's 5.10.0.dev0. Loading both configurations at home
under 5.10.1 settles which fields are the library's and which are the copy's.

- `config.audio_config.dtype`, `config.vision_config.dtype` and `config.text_config.dtype`: the copy writes
  "bfloat16" in each sub-configuration where the original leaves it null; the top-level `dtype` is bfloat16 on both
  sides. A repetition, as the tool already says for the text one.
- `config.audio_config.audio_samples_per_token`, `hidden_size` and `output_proj_dims` (640 in the original) and
  `config.vision_config.model_patch_size` (48): absent in the copy. Under 5.10.1 the original's configuration loads
  640, 640, 640 and 48; the copy's loads 1024 for the hidden size, 1536 for the output projection and nothing for the
  other two. A 5.10.1 re-save of the original's configuration writes all four values back, so the library did not
  drop them; the copy's `config.json` lacks them. The weights disagree with the copy's own configuration under that
  library: the copy ships `model.embed_audio.embedding_projection.weight` unchanged at shape [3840, 640], the
  original's geometry. The card's text-only use is unaffected; audio input through this configuration is an open
  question this audit does not run.

## For the recipe library

Consistent with the stated change on the weight side. The single-direction heretic edit now has two measured copies
(this one and piece 5): a shared direction with per-layer weights that follow a kernel, which the shared-direction
entries match on direction and energy and the remaining-fraction measurement describes. A norm-restoration line
between 0.0011 and 0.004 would separate the approximate restoration from the exact one. On the token side the
metadata tool needs a rule for a field whose absence loads differently from its presence, judged under the library
version that saved the copy. The saved direction vectors are not committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/blueback7/measurements/pair-3/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
