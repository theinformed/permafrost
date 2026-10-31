# Reading of the Stage 1 and Stage 2 result: llmfan46/gemma-4-31B-it-uncensored-heretic against google/gemma-4-31B-it (2026-10-31)

Measured on Blueback, round 12 piece 1 (push card 5366, round card 5367, download job 3399779, compare jobs 3399780 to
3399785, all exit 0, sweep 3399786; pulled home by card 5448). Modified revision `d5bfc0d9` (2026-09-19, the maker's
latest template commit; the repository was created on 2026-04-03), original pinned at `419b2efe` (2026-04-02, the
release commit). The maker's card names the method and its parameters: Heretic 1.2.0 with Arbitrary-Rank Ablation,
start layer 30, end layer 48, preserve weight 0.5437, steer weight 0.0005, overcorrect weight 0.9949, neighbour count
15, targeted component `attn.o_proj`; it reports 10 refusals in 100 against 99 for the original, a KL divergence of
0.0541, and an MMLU accuracy of 85.90 percent against 86.50.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 18 flags, on the
cluster and after re-scoring at home. All 18 flags are energy shares. On reading, the footprint matches the card and
the flags measure the arbitrary-rank method, which the table still lists as "not yet measured".

- 18 of 1,188 tensors changed, all attention outputs, in layers 30 to 47 of 60: every layer of the card's range and
  its one component. Nothing else moved; the largest relative change outside the changed set is exactly 0, the
  feed-forward matrices, the query, key and value projections and the vision tower included. The 31B base has no
  audio tower and no per-layer embeddings.
- The arbitrary-rank profile: first-value energy share 0.910 to 0.977, first eight values 0.956 to 0.992, on relative
  changes of 0.0185 to 0.0746. The leftover beyond the first direction is 0.0040 to 0.0117 of the weight norm, three to
  eight times the storage floor.
- The leading direction sits on the input side, as on the maker's three smaller copies. Along it the copy keeps −2.36
  to −0.37 of the original's action on the right (weights 1.37 to 3.36, median 1.95) and 0.60 to 0.99 on the left; the
  left fraction is above the right on all 18. The tail directions keep 0.65 to 1.16 (medians per matrix 0.93 to 1.00).
- The leading directions differ by layer (cosine 0.07 to 0.42 with their median, 0.29 in the middle).
- Row norms moved by 0.0016 to 0.037 relative; the card claims no norm preservation. Layer 45 carries the largest edit
  of the copy: weight 3.36, relative change 0.075, row norms moved by 0.032.

| Layer | Relative change | E1 | E8 | Left, direction 1 | Right, direction 1 | Row norms |
| --- | --- | --- | --- | --- | --- | --- |
| 30 | 0.033 | 0.962 | 0.973 | 0.88 | −1.40 | 0.013 |
| 31 | 0.026 | 0.939 | 0.969 | 0.92 | −0.85 | 0.004 |
| 32 | 0.038 | 0.958 | 0.980 | 0.92 | −1.06 | 0.018 |
| 33 | 0.026 | 0.948 | 0.963 | 0.81 | −0.62 | 0.009 |
| 34 | 0.024 | 0.965 | 0.978 | 0.86 | −0.79 | 0.004 |
| 35 | 0.020 | 0.942 | 0.956 | 0.90 | −0.41 | 0.005 |
| 36 | 0.021 | 0.961 | 0.971 | 0.60 | −1.00 | 0.002 |
| 37 | 0.039 | 0.957 | 0.981 | 0.95 | −1.56 | 0.037 |
| 38 | 0.025 | 0.965 | 0.979 | 0.89 | −0.54 | 0.004 |
| 39 | 0.028 | 0.965 | 0.976 | 0.74 | −0.65 | 0.010 |
| 40 | 0.030 | 0.944 | 0.965 | 0.78 | −1.13 | 0.013 |
| 41 | 0.019 | 0.944 | 0.959 | 0.94 | −0.89 | 0.004 |
| 42 | 0.021 | 0.961 | 0.981 | 0.68 | −0.96 | 0.002 |
| 43 | 0.025 | 0.974 | 0.989 | 0.63 | −0.94 | 0.013 |
| 44 | 0.040 | 0.970 | 0.984 | 0.94 | −0.37 | 0.013 |
| 45 | 0.075 | 0.977 | 0.992 | 0.95 | −2.36 | 0.032 |
| 46 | 0.064 | 0.976 | 0.991 | 0.92 | −1.89 | 0.036 |
| 47 | 0.039 | 0.910 | 0.966 | 0.99 | −1.81 | 0.037 |

Against the maker's three smaller copies the method is the same and the settings differ by size: the E4B copy of
round 2 edits 11 attention outputs in layers 21 to 35 at weights 1.27 to 1.79, the E4B ultra copy of round 7 17 in
layers 18 to 35, the E2B copy of round 8 7 in layers 17 to 23 at 1.86 to 4.41, and this one 18 in layers 30 to 47 at
1.37 to 3.36; on all four the leading direction is on the input side and the row norms are not restored. On the two
E4B copies 17 and 13 attention outputs inside the declared range stayed within 0.00008 of their norm; here every
layer of the range changed. Against the four other copies of this base (wangzhang in round 2, pieces 2, 3 and 4 of
this round), which stand on the same original weight file (shards `eeef8791` and `01891222`), no changed matrix has
an equal measurement in any field.

## Token and configuration side (Stage 1)

The cluster's card read "unexplained differences" in three fields. Re-judged at home the configuration field closes
by tool and the template stays, so the committed card still reads "unexplained differences"; the reading settles the
template by hand as a change the maker made.

- `config.text_config.moe_intermediate_size`: absent in the original, null in the copy. The two `config.json` files
  differ in that line and in the version string (5.5.0.dev0 against 5.5.0) and in nothing else; the text configuration
  carries `enable_moe_block` false and `num_experts` null in both, so the field is the library's default for a block
  the dense model does not have, written by the newer library on save. A re-save effect, and the tool classes it so
  under 5.6.2.
- `generation.transformers_version` and `config.transformers_version`: the saved version strings, re-save.
- `template.default` and `rendered_template.default`: the copy's `chat_template.jinja` (18,841 bytes) is Google's
  template of 2026-07-15 (`68abe480`, carried unchanged through `842da379`; 18,683 bytes, with Google's own header
  "Published: 2026-07-09") with one line changed. Where Google's template opens each model turn of the history with
  `<|turn>model` and a newline, the maker's writes an empty thought block (`<|channel>thought`, newline,
  `<channel|>`) after it whenever thinking is off and the message carries no reasoning field. The fixed conversation
  renders at 232 bytes against 204: the earlier answer "Four." becomes "<|channel>thought\n<channel|>Four.". The
  maker's commit of 2026-09-19 uploaded, beside the new template, a file named
  `chat_template.jinja.official-2026-07-09.bak` that equals Google's 2026-07-15 template byte for byte, and deleted it
  nine seconds later. Google's card says the 26B and 31B models emit the empty block themselves when thinking is off,
  and that thoughts from earlier turns are not to be added to the history. A real change by the maker to the prompt
  of every multi-turn conversation with thinking off, outside the card. The later-revision rule cannot close it
  because the template equals no commit of Google's repository. The maker replaced the template seven times between
  2026-04-14 and 2026-09-19 (2026-05-04, 05-05, four times on 05-18, 06-11, 09-19); the 2026-06-11 version, 23,077
  bytes, equals no Google commit either.

## For the recipe library

Consistent with the stated change on the weight side; on the token side the weights and configuration are the
original's and the template is the maker's. The fourth arbitrary-rank copy of this maker and the first on the 31B
base; the candidate entry's weight band should reach 3.4 here and 10.2 on piece 2. The saved direction vectors are
not committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/blueback12/measurements/pair-1/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
