# Reading of the Stage 1 and Stage 2 result: ImanolSuarez/gemma-4-E4B-it-heretic-seguridadDeLaInformacion against google/gemma-4-E4B-it (2026-11-02)

Measured on Wheat, round 41 piece 4 (download job 387195, compare job 387199, sweep 387203; the pull carries the
measurements and the sweep record and no job log). Modified revision `50f4cdf9` (created 2026-05-23 19:29Z, the
model, the tokenizer, the card and a `reproduce/` folder uploaded within two minutes), original pinned at
`d6436b3d` of 05-18, the revision the maker's own record names as `model_commit`. The card is Heretic 1.3.0's
table under the pretrained base's name in its `base_model` field (`google/gemma-4-E4B`, finding 67's inherited
header): `direction_index` 29.08, `attn.o_proj` with a maximum weight of 1.30 at position 30.63 and a minimum of
0.47 at a distance of 13.10, `mlp.down_proj` with 1.34 at 33.43 and 0.72 at 17.07, a KL divergence of 0.0094 and
6 refusals in 100 against 99 in 100. The `reproduce/` folder says what the name does not: the direction prompts
are mlabonne's English `harmless_alpaca` and `harmful_behaviors` at `train[:400]`, the evaluation prompts their
`test[:100]`, the system prompt "You are a helpful assistant.", `row_normalization` "full" at a LoRA rank of 3,
`orthogonalize_direction` true, `winsorization_quantile` 1.0, trial 92 of 200 with seed 3523619699, on one RTX
5080 under Windows 11 and transformers 5.9.0. "seguridadDeLaInformacion" names no prompt set in the record; the
run is the tool's default English search.

## Weights (Stage 2)

The tool's assessment was violations against `single-projection-selected`, 10 flags (6 first shares at 0.978 to
0.989 on the attention outputs of layers 18 to 22, 3 direction cosines, 1 cross-kind), on the cluster and after
re-scoring at home. On reading, the copy is one direction projected from both writers across a window whose lower
ends are the card's kernels to the layer and whose upper end stops six layers short of them.

- 37 of 2,076 tensors changed: the down projections of layers 17 to 35 and the attention outputs of 18 to 35.
  The card's kernels open at 33.43 less 17.07 (16.4, layer 17) and 30.63 less 13.10 (17.5, layer 18), the
  windows' lower ends to the layer, and reach past the stack's last layer, 41; both writers of layers 36 to 41
  are exactly 0, twelve matrices the kernels cover and the weights do not show. Nothing else moved; the largest
  relative change outside the changed set is exactly 0 on all 2,039 other tensors.
- Rank one on every matrix (first shares 0.978 to 0.997) and one direction for the whole window: the layers at
  0.94 to 1.00 to each other within a kind and the two writers of a layer at 0.91 to 1.00, the card's single
  direction index of 29.08.
- Output side on all 37, and the kept fractions do not trace the card's kernels: one minus the left kept
  fraction is 0.65 at layer 17 rising to 0.98 at 26 and 1.02 at 31 and falling to 0.81 at 35 on the down
  projections, under a printed maximum of 1.34, and 0.16 to 0.91 with no order along the window on the
  attention outputs, under a printed maximum of 1.30; the relative change rises along the window from 0.010 to
  0.029 on both writers, which is the kernel's shape. The record's two settings the census has not read before,
  the full row normalisation at rank 3 and the orthogonalised direction, stand between the projection and the
  kept fractions. Rows moved 0.0039 to 0.0112, rising with the layer. Relative changes 0.0099 to 0.0290.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Down projection: change, E1, left kept, right kept | Weight | Rows |
| --- | --- | --- | --- | --- | --- |
| 17 | - | - | 0.0146, 0.989, 0.35, 0.57 | 0.65 | -, 0.0040 |
| 18 | 0.0099, 0.978, 0.80, 0.85 | 0.20 | 0.0155, 0.990, 0.36, 0.58 | 0.64 | 0.0044, 0.0046 |
| 20 | 0.0121, 0.985, 0.66, 0.86 | 0.34 | 0.0167, 0.992, 0.21, 0.52 | 0.80 | 0.0057, 0.0058 |
| 23 | 0.0161, 0.991, 0.39, 0.62 | 0.61 | 0.0194, 0.994, 0.27, 0.33 | 0.74 | 0.0055, 0.0064 |
| 26 | 0.0191, 0.993, 0.09, 0.70 | 0.91 | 0.0223, 0.995, 0.02, 0.28 | 0.98 | 0.0072, 0.0056 |
| 29 | 0.0275, 0.997, 0.36, 0.56 | 0.64 | 0.0290, 0.997, 0.22, 0.17 | 0.78 | 0.0091, 0.0052 |
| 31 | 0.0270, 0.996, 0.84, 0.54 | 0.16 | 0.0243, 0.996, -0.02, 0.09 | 1.02 | 0.0112, 0.0060 |
| 33 | 0.0263, 0.996, 0.77, 0.55 | 0.23 | 0.0248, 0.996, 0.16, 0.13 | 0.84 | 0.0090, 0.0085 |
| 35 | 0.0210, 0.993, 0.61, 0.64 | 0.39 | 0.0234, 0.995, 0.19, 0.16 | 0.81 | 0.0068, 0.0086 |

The full table (19 rows) is in the report.

Directions. Against thirty-nine saved vectors of other measurements of the E4B, the direction stands at 0.755 on
the left and 0.750 on the right to p-e-w's E4B export and his reproduction of it on all 37 shared names (minimum
0.724), at 0.71 to sh0ck0r's (36), 0.69 to BinxNet's (28) and 0.72 to Dingdust's attention outputs, at 0.40 to
treadon's, 0.37 to Madras1's, 0.35 to TrevorJS's, its re-upload and TheUmbraWalker's first pass, 0.23 to
jokernifty's, and at 0.11 or less to the rest: 0.09 to 0.11 to NullpoLab's five arbitrary-rank exports, 0.093 to
Felldude's and chulcher's pretrained-base copies, 0.084 to coder3101's, 0.077 to MoonRide's, 0.066 to
llmfan46's, 0.010 to DuoNeural's and huihui-ai's. The number sits between the 0.96 to 0.98 at which independent
runs of the tool's earlier versions stand to each other on this base (findings 85 and 102) and the 0.4 to 0.6 a
change of prompt set reads (findings 83, 93 and 99), on a run whose record names the same English prompt sets
as theirs. By byte range the layer 26 attention output is 0.0191 from Google's, 0.0165 from p-e-w's and 0.0177
from sh0ck0r's (those two 0.0066 apart), and the layer 26 down projection 0.0223 from Google's, 0.0243 from
p-e-w's and 0.0256 from sh0ck0r's: as far from the family's tensors as from the original's. Of the four shards,
the fourth (`8080cb1a`) is byte-equal to the E4B layout shard nine measured exports carry (p-e-w's two, sh0ck0r's,
BinxNet's, DuoNeural's, OS-Software's, TheUmbraWalker's, and igorls's and prithivMLmods's on the QAT
checkpoint), finding 71's layout, and the first three (`aa3e9d1e`, `9ff4341d`, `cdfd7caa`) match no measured
file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster on one field, "consistent with re-save noted" at home: the home
judgement closed `text_config.moe_intermediate_size` by the default rule under transformers 5.22.1, leaving the
version strings (5.5.0.dev0 to 5.9.0, the record's library). The 17,695-byte template renders the fixed
conversation identically to the pin's 17,336 bytes and differs from it in line endings and trailing whitespace
alone, the Windows save the record names. The tokenizer, the token ids (`eos_token_id` `[1, 106]`, generation
`[1, 106, 50]`) and the generation settings are the pin's.

## For the recipe library

The single-projection entry with selection reads the direction and misses the window's upper end; a
kernel-tail rule would name the six layers the card's kernels cover and the weights do not, and a weight line
would print kept fractions that do not read a kernel under a full row normalisation. The direction vectors stay
in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat41/measurements/pair-4/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
