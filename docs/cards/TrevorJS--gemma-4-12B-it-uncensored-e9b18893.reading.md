# Reading of the Stage 1 and Stage 2 result: TrevorJS/gemma-4-12B-it-uncensored against google/gemma-4-12B-it (2026-10-30)

Measured on Blueback, round 8 piece 6 (round card 5305, download job 3397500, compare jobs 3397501 to 3397508, all exit
0, sweep 3397509; pulled home by card 5347). Modified revision `159eb7a8` (2026-06-13), original pinned at `5926caa4`
(2026-06-04). The maker's card names the method and its settings: norm-preserving biprojected abliteration with one
direction per layer, applied to the attention output and the down projection in the top 70 percent of the layers
(it names layers 15 to 47) at scale 1.0; it reports 6 refusals in 100, a KL divergence of 0.0556, and a library
requirement of transformers 5.10.1 or later, tested on 5.12.0.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 1 flag, on the
cluster and after re-scoring at home. The flag is one energy share at the storage floor. On reading, the footprint
matches the card.

- 66 of 677 tensors changed: the attention output and the down projection in each of layers 15 to 47 of 48, which is
  33 layers, the card's 70 percent rounded down. Nothing else moved; the largest relative change outside the changed
  set is exactly 0, and the 11 tensors outside the text model are unchanged.
- One direction per layer: within a layer the two edits agree at cosine 0.970 to 0.999 (median 0.995), every layer
  above the 0.95 line; between layers the median directions agree at 0.147.
- Row norms moved by 0.0001 to 0.0004 relative (largest 0.00036), the same restoration as the maker's E4B copy in
  piece 1.
- Relative change 0.0155 to 0.0206, first-value energy share 0.990 to 0.996, leftover 0.0012 to 0.0017 of the weight
  norm. The one flag is layer 42's attention output at a share of 0.9899 on a relative change of 0.0172, leftover
  0.0017, inside the calibrated floor.
- Along each matrix's leading output direction the copy keeps −0.01 to 0.68 of the original's action on the attention
  outputs (median 0.18) and 0.00 to 0.41 on the down projections (median 0.03), the left fraction below the right on
  65 of 66: scale 1.0 with the biprojection's second term.
- Against the two other copies of this base (igorls in round 7, piece 7 of this round), which stand on the same
  original weight file (shard `5a84cb31`), no changed matrix has an equal measurement in any field.

## Token and configuration side (Stage 1)

The tool's Stage 1 assessment is "unexplained differences" in six configuration fields before and after the home
re-judgment; the reading closes all six as effects of the saving library. The copy was saved with transformers
5.12.0 against the original's 5.10.0.dev0.

- `config.audio_config.audio_samples_per_token`, `hidden_size` and `output_proj_dims` (640 in the original) and
  `config.vision_config.model_patch_size` (48): absent in the copy. These are the same four fields the igorls copy of
  the same base lacked in round 7. Loaded at home under 5.10.1 and under 5.12.1 (the version that saved this copy),
  the original's configuration and the copy's both give 640, 640, 640 and 48: the four values are the defaults of the
  library's unified Gemma 4 audio and vision configuration classes, which the library omits when it writes a
  configuration and restores when it reads one. A save of Google's own configuration under either version drops the
  same four fields. The copy's configuration describes the weights it ships (the audio embedding projection is
  unchanged at shape [3840, 640]).
- `config.audio_config.dtype` and `config.vision_config.dtype`: null in the original, "bfloat16" in the copy, the
  top-level data type repeated into the sub-configurations, as the tool already says for the text one.

## For the recipe library

Consistent with the stated change on both sides. The second norm-preserving per-layer copy of this maker, and with
pieces 1 and 4 of round 2 the fourth with row norms held within 0.0011, a line a norm-preserving entry can carry.
On the token side the four audio and vision values are a library default under 5.10 and later, which settles the
same fields on the igorls copy (round 7) the other way from that reading. The saved direction vectors are not
committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/blueback8/measurements/pair-6/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
