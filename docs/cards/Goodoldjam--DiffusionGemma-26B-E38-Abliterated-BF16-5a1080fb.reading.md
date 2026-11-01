# Reading of the Stage 1 and Stage 2 result: Goodoldjam/DiffusionGemma-26B-E38-Abliterated-BF16 against google/diffusiongemma-26B-A4B-it (2026-10-31)

Measured on Wheat, round 30 piece 6 (probe job 386940, download job 386942, compare job 386948, 1,509 seconds, sweep
386951), without the container image, under a standalone Python 3.11.18. Modified revision `3b57f5ed` (2026-08-18
at 04:33Z, the last of 33 commits; the weights went up on 08-15 at 21:06Z as "Upload frozen E38 BF16 checkpoint"
and the other 31 commits edit the README), original pinned at `f7f5b7f5` (2026-07-15). The card calls E38 "the
selected configuration from a controlled Heretic-based abliteration search" of more than 80 candidates, affecting
layers 7 to 16, `attn.o_proj` and `mlp.down_proj`, 20 language tensors, 0 vision tensors, in bfloat16, and says
this file is the reference for an NVFP4 derivative that keeps the 20 tensors in bfloat16. It reports 0 of 402
target refusals against 383 for the original. No kernel parameters are printed. The repository's `base_model`
field names the original.

## The original

DiffusionGemma 26B A4B is Google's block-diffusion variant of the Gemma 4 26B-A4B mixture: `architectures`
DiffusionGemmaForBlockDiffusion, `model_type` diffusion_gemma, text model `diffusion_gemma_text`, `canvas_length`
256, 30 layers, hidden size 2,816, 16 heads of 256 (512 on the global layers), shared feed-forward 2,112, 128
experts of 704, sliding window 1,024, bfloat16, saved by transformers 5.8.0.dev0 in 11 shards. The generation
settings are a denoising schedule (48 steps per canvas, times 0.4 to 0.8, an entropy bound of 0.1). Against the
26B-A4B instruct original the census has measured ten times, the language stack is the same 1,013 tensors under
`model.decoder.` instead of `model.language_model.`, with 34 tensors added: 4 `self_conditioning` projections on
the decoder and a `layer_scalar` on each of 30 encoder layers; the audio tower and its fields are absent; the
chat template is the 26B-A4B's 17,466-byte file (`36e3a42e`). The compare tool knew the Gemma 4 names under the
`model.language_model.` wrapper and read the `model.decoder.` names as kind "other", which is why the cluster
report ranks nothing and flags every changed tensor as unexpected; the naming table now lists `decoder.` and the
home report reads the roles.

## Weights (Stage 2)

The tool's assessment was "recipe violations" on the cluster, nearest recipe `single-projection`, 21 flags (20
unexpected changes of kind "other" and one missing projection), and "recipe violations" at home, nearest recipe
`single-projection-selected`, 40 flags: 20 first shares of 0.005 to 0.967 and 20 within-layer cosines of 0.015 to
0.449. On reading, the copy's changed set is the card's to the tensor, five of the 20 are at the floor of a
bfloat16 round trip, and the 15 that carry an edit are a multi-direction edit on the input side with unrelated
directions per matrix.

- 20 of 1,047 tensors changed: the attention outputs and the down projections of layers 7 to 16, the card's 20.
  The largest absolute difference, 0.2019 on the attention output of layer 9, is the card's `max_abs_delta` to
  its last digit. Nothing else moved: the largest relative change outside the changed set is
  exactly 0, 1,027 tensors equal the original, and shards 1, 2 and 7 to 11 carry the original's checksums. No
  expert, embedding or vision tensor changed.
- Five of the 20 are at the floor: the down projections of layers 9 to 12 and the attention output of layer 11
  moved by 0.0014 to 0.0017 with first shares of 0.005 to 0.009, kept fractions of 1.00 on both sides and the
  largest absolute difference 0.002 to 0.004, which is one bfloat16 step at those magnitudes. A tensor written
  back after a round trip through another precision, finding 3's floor.
- The 15 edited matrices are not rank one: first share 0.49 to 0.97, eighth share 0.95 to 0.98, with the second
  singular value 0.05 to 0.67 of the first. A sum of several directions per matrix, strongest on the attention
  outputs (0.87 to 0.97 first share).
- Input side on the nine attention outputs: the left kept fraction is 0.48 to 0.93 and the right −0.15 to −0.95,
  weights along the right direction of 1.15 to 1.95 (1.81 at layer 7, 1.95 at layer 9). The six edited down
  projections read 0.60 to 1.02 on the left and −0.90 to 1.02 on the right, the left above the right on all six,
  with a right-side weight of 1.90 at layer 8 and 1.25 at 14 and under 0.42 on the other four: no single side.
- The directions agree with the group reference at 0.02 to 0.45, and the home report flags all 20 on direction
  agreement: per-matrix directions, unrelated between the two writers of a layer.
- Rows moved by 0.0070 to 0.0078 on the 15 edited matrices, a narrow band, and by 0.0008 to 0.0013 on the five
  floor tensors.
- Relative changes of 0.014 to 0.047, the largest on the down projection of layer 8.
- The token side is the original's: configuration and generation settings equal field for field (version
  5.8.0.dev0 on both sides), the tokenizer configuration one byte shorter, the template 1,109 bytes longer and
  rendering the fixed conversation identically, a `model_index.json` and a scheduler folder added for the
  diffusion pipeline.

| Layer | Attention output: change, E1, E8, left kept, right kept | Down projection: change, E1, E8, left kept, right kept | Weight read | Within-layer cosine | Cross-layer cosine | Row norms |
| --- | --- | --- | --- | --- | --- | --- |
| 7 | 0.0363, 0.902, 0.980, 0.48, -0.81 | 0.0269, 0.903, 0.983, 0.98, 0.59 | 1.81/0.41 | - | 0.36/0.12 | 0.0075, 0.0071 |
| 8 | 0.0303, 0.945, 0.979, 0.52, -0.60 | 0.0471, 0.836, 0.983, 0.74, -0.90 | 1.60/1.90 | - | 0.43/0.15 | 0.0077, 0.0074 |
| 9 | 0.0360, 0.890, 0.971, 0.84, -0.95 | 0.0014, 0.009, 0.049, 1.00, 1.00 | 1.95/0.00 | - | 0.45/0.02 | 0.0075, 0.0013 |
| 10 | 0.0297, 0.904, 0.970, 0.75, -0.82 | 0.0016, 0.006, 0.033, 1.00, 1.00 | 1.82/0.00 | - | 0.43/0.07 | 0.0074, 0.0009 |
| 11 | 0.0017, 0.005, 0.021, 1.00, 1.00 | 0.0016, 0.007, 0.030, 1.00, 1.00 | -0.00/-0.00 | - | 0.02/0.06 | 0.0008, 0.0010 |
| 12 | 0.0151, 0.967, 0.973, 0.84, -0.15 | 0.0016, 0.006, 0.028, 1.00, 1.00 | 1.15/-0.00 | - | 0.43/0.03 | 0.0078, 0.0009 |
| 13 | 0.0265, 0.866, 0.962, 0.91, -0.82 | 0.0141, 0.896, 0.961, 1.02, 1.02 | 1.82/-0.02 | - | 0.35/0.16 | 0.0077, 0.0072 |
| 14 | 0.0251, 0.878, 0.968, 0.80, -0.66 | 0.0381, 0.486, 0.964, 0.60, -0.25 | 1.66/1.25 | - | 0.37/0.18 | 0.0077, 0.0068 |
| 15 | 0.0249, 0.870, 0.953, 0.93, -0.71 | 0.0169, 0.897, 0.971, 0.95, 0.94 | 1.71/0.06 | - | 0.31/0.14 | 0.0075, 0.0072 |
| 16 | 0.0249, 0.865, 0.969, 0.78, -0.64 | 0.0165, 0.956, 0.968, 0.86, 0.84 | 1.64/0.16 | - | 0.33/0.16 | 0.0071, 0.0070 |

The weight column reads one minus the right kept fraction on the attention output and one minus the left kept
fraction on the down projection.

## Token and configuration side (Stage 1)

"Consistent" on the cluster and at home: no changed field. The fixed conversation renders identically with the
`default` template.

## For the recipe library

The first measurement of a diffusion-variant copy, and the first "Heretic-based" card without a kernel whose
weights do not read as any Heretic edit measured so far: multi-direction per matrix, unrelated between the two
writers of a layer, input side on the attention outputs, five of twenty tensors round-trip floors. The 80-candidate
search the card describes could have composed several trials' projections, which is the shape measured; the
`arbitrary-rank` candidate line (input side, a tail of weak directions) is the nearest and would need a per-matrix
direction allowance to fit. The NVFP4 derivative the card recommends is a quantised copy of this file and needs no
measurement for its edit. The pull copy keeps the direction vectors at
`/opt/ai/hpc-packages/pulls/model-audit/wheat30/measurements/pair-6/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
