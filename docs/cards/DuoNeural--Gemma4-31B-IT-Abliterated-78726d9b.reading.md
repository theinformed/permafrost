# Reading of the Stage 1 and Stage 2 result: DuoNeural/Gemma4-31B-IT-Abliterated against google/gemma-4-31B-it (2026-11-02)

Measured on Nautilus, round 40 piece 6 (download job 4169647, compare job 4169653, sweep 4169656; the pull carries
the measurements and the sweep record and no job log). Modified revision `0e5a5b43` (created 2026-06-06 22:11Z,
the weights at 22:15Z, the card at 22:27Z), original pinned at `35487898` of 06-03. The card is the maker's own
method, not a tool's table: per-layer directions from 15 harmful and 15 harmless prompts taken at the first
generated token ("harmful prompts universally produce token 'I'"), "orthogonal rank-1 projection" of both
writers with "Alpha: {down_proj: 0.4, o_proj: 0.8}" over "All 60 decoder layers (120 weights total)", and a KL
divergence of 1.606 the card marks as significant and disclosed. It is the maker's third copy in the census: the
26B-A4B copy of round 38 carried TrevorJS's edit byte for byte under the maker's card (finding 95), the E2B copy
a single direction of the maker's own (finding 96).

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer`, 74 flags (first shares of 0.947 to 0.990
under the entry's floor), on the cluster and after re-scoring at home. On reading, the copy is exactly its card,
and the maker's own work: one direction per layer projected from the output side of both writers of all 60
layers at the card's two alphas.

- 120 of 1,188 tensors changed: the attention output and down projection of every layer. Nothing else moved; the
  largest relative change outside the changed set is exactly 0 on all 1,068 other tensors.
- Rank one on every matrix (first shares 0.947 to 0.999) and one direction per layer: the two writers of a layer
  at 0.999 to 1.000 to each other, the layers at 0.07 (median) to one another.
- Output side on all 120: the left kept fraction is 0.5955 to 0.6040 on every down projection, a weight of 0.40,
  and 0.1968 to 0.2027 on every attention output, a weight of 0.80, the card's two alphas to two decimals on all
  sixty layers; the right side keeps 0.65 to 0.98. Rows moved 0.0013 to 0.358 (0.358 on the last attention
  output, 0.238 on the first), unrestored, under no claim. Relative changes 0.0048 to 0.0455.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Down projection: change, E1, left kept, right kept | Weight | Rows |
| --- | --- | --- | --- | --- | --- |
| 0 | 0.0365, 0.998, 0.20, 0.88 | 0.80 | 0.0112, 0.989, 0.60, 0.98 | 0.40 | 0.2376, 0.0879 |
| 10 | 0.0166, 0.996, 0.20, 0.98 | 0.80 | 0.0058, 0.980, 0.60, 0.97 | 0.40 | 0.0561, 0.0173 |
| 20 | 0.0169, 0.994, 0.20, 0.94 | 0.80 | 0.0063, 0.972, 0.60, 0.89 | 0.40 | 0.0317, 0.0114 |
| 30 | 0.0373, 0.998, 0.20, 0.81 | 0.80 | 0.0156, 0.993, 0.60, 0.90 | 0.40 | 0.2047, 0.1028 |
| 40 | 0.0142, 0.990, 0.20, 0.81 | 0.80 | 0.0071, 0.966, 0.60, 0.92 | 0.40 | 0.0274, 0.0159 |
| 50 | 0.0117, 0.984, 0.20, 0.95 | 0.80 | 0.0059, 0.949, 0.60, 0.77 | 0.40 | 0.0177, 0.0085 |
| 59 | 0.0131, 0.989, 0.20, 0.75 | 0.80 | 0.0048, 0.964, 0.60, 0.93 | 0.40 | 0.3582, 0.2042 |

The full table (60 rows) is in the report.

Directions. Against twenty-six saved vectors of other measurements of the 31B, the directions stand at 0.282 on
the left and 0.208 on the right to TrevorJS's edit on all 120 shared names and the same to ressl's, at 0.52 to
callmegrr's (12 shared), 0.47 to Sabomako's (8), 0.40 to germlag's, 0.39 to nguyenthilaitrieulong's, 0.35 to
Vampelium's, 0.31 to 3MPER0RR's, and at 0.19 or less to the rest (0.13 to Jim-darby's, 0.08 to huihui-ai's and
coder3101's, 0.007 to cosmicoptima's). The maker's 26B-A4B copy stood at 1.000 to TrevorJS's on every name
(finding 95); this one stands at 0.28, and by byte range the layer 20 attention output is 0.0169 from Google's
and 0.0226 from TrevorJS's (TrevorJS's is 0.0152 from Google's), the layer 20 down projection 0.0063 from
Google's and 0.0165 from TrevorJS's: an edit of the maker's own, further from TrevorJS's than either is from the
original. The thirteen shards (`a723b352` to `68299177`) match no measured file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster, "consistent with re-save noted" at home: the home judgement closed
`text_config.moe_intermediate_size` by the default rule under transformers 5.22.1, leaving the version strings
(5.5.0.dev0 to 5.10.2, as the card says). The tokenizer, the token ids, the generation settings and the
17,466-byte template are the pin's.

## For the recipe library

The per-layer entry reads the copy on 46 of 120 matrices under a 0.99 floor; a weight line (0.40 and 0.80 on
the output side) and a floor at 0.94 would read all 120. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus40/measurements/pair-6/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
