# Reading of the Stage 1 and Stage 2 result: NullpoLab/gemma-4-E4B-it-Heretic-ARA-Refusals6-attn against google/gemma-4-E4B-it (2026-11-02)

Measured on Nautilus, round 40 piece 7 (download job 4169647, compare job 4169654, sweep 4169656; the pull carries
the measurements and the sweep record and no job log). Modified revision `c9807d51` (created 2026-04-05 12:49Z,
four minutes before the maker's Refusals8-attn at 12:53Z and the day after Refusals8; the weights uploaded at
12:54Z, "Upload folder" commits on 04-11 and 04-29, the last at 11:08Z), original pinned at `292a7e27`. The card
is in Japanese with an English copy beside it: Heretic 1.2.0's arbitrary-rank branch from the tool's pull
request 211 at commit `3b70fe5`, `target_components` `attn.o_proj`, `start_layer_index` 21, `end_layer_index`
41, `preserve_good_behavior_weight` 0.8666, `steer_bad_behavior_weight` 0.0014, `overcorrect_relative_weight`
0.7436, `neighbor_count` 14, 6 refusals in 100 against 99 in 100 and a KL divergence of 0.0211. It is the maker's
fourth E4B export in the census and the second under an attention-only card (Refusals8-attn, finding 87).

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 61 flags (31 first shares, 30
within-layer cosines), on the cluster and after re-scoring at home. On reading, the copy is an arbitrary-rank
edit of both writers of layers 21 to 36 under a card that names the attention outputs alone and a window to 41.

- 31 of 2,130 tensors changed: the attention outputs of layers 21 to 36 (16) and the down projections of 22 to
  36 (15). The down projection of layer 21 stayed under the threshold at 0.00038, the largest relative change
  outside the changed set; the other 2,098 tensors are exactly 0. The card's `end_layer_index` is 41 and the
  edits stop at 36; the card's `target_components` is `attn.o_proj` and fifteen down projections are edited, as
  on the maker's Refusals8-attn (finding 87, edits to 35 under a card to 39).
- Thirty-one edits, a few directions each: first shares 0.72 to 0.96 on the attention outputs and 0.32 to 0.95
  on the down projections, none left as a residue. The two writers of a layer are unrelated (0.0005 to 0.15).
- Input side on all 31: one minus the right kept fraction is 0.91 to 1.90 on the attention outputs (1.90 at layer
  29) and 1.00 to 1.60 on the down projections, the left side keeping 0.35 to 0.94. Rows moved 0.0015 to 0.0131
  on the attention outputs (0.0131 at layer 31, 0.0106 at 29, 0.0100 at 30) and 0.0009 to 0.0065 on the down
  projections, through and over finding 22's band at the layers of the largest weights, as the maker's other
  exports read (findings 56 and 87). Relative changes 0.0140 to 0.0484.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Down projection: change, E1, left kept, right kept | Weight | Rows |
| --- | --- | --- | --- | --- | --- |
| 21 | 0.0243, 0.911, 0.81, -0.35 | 1.35 | - | - | 0.0016, - |
| 22 | 0.0406, 0.801, 0.69, -0.29 | 1.29 | 0.0323, 0.445, 0.91, -0.20 | 1.20 | 0.0067, 0.0018 |
| 24 | 0.0387, 0.946, 0.35, -0.41 | 1.41 | 0.0207, 0.874, 0.77, -0.60 | 1.60 | 0.0055, 0.0009 |
| 27 | 0.0360, 0.802, 0.85, -0.39 | 1.39 | 0.0242, 0.548, 0.82, -0.27 | 1.27 | 0.0035, 0.0014 |
| 29 | 0.0391, 0.839, 0.93, -0.90 | 1.90 | 0.0222, 0.838, 0.71, -0.55 | 1.55 | 0.0106, 0.0019 |
| 31 | 0.0484, 0.934, 0.60, -0.24 | 1.24 | 0.0249, 0.563, 0.84, -0.10 | 1.10 | 0.0131, 0.0035 |
| 33 | 0.0320, 0.934, 0.91, -0.13 | 1.13 | 0.0140, 0.954, 0.86, -0.21 | 1.21 | 0.0069, 0.0015 |
| 35 | 0.0240, 0.715, 0.78, 0.09 | 0.91 | 0.0291, 0.449, 0.94, -0.00 | 1.00 | 0.0015, 0.0065 |
| 36 | 0.0361, 0.948, 0.75, -0.28 | 1.28 | 0.0318, 0.324, 0.81, -0.12 | 1.12 | 0.0070, 0.0014 |

The full table (16 rows) is in the report.

Directions. Against thirty-nine saved vectors of measurements of the E4B, the leading directions stand at 0.995
and 0.994 to the maker's Refusals8-attn on all 19 shared names (left minimum 0.755), 0.995 and 0.991 to
coder3101's edit (16), 0.985 to the maker's Refusals5 (26) and Refusals8 (27, left minimum 0.654), 0.984 to
SassyDiffusion's, 0.958 to llmfan46's two edits and their re-uploads, 0.956 to MoonRide's April edit on all 31,
0.92 to JokeHer's, 0.91 to alphakek's, 0.88 to coder3101's QAT edit and 0.86 to Himanshuoo8's: finding 82's E4B
family, the maker's two attention-only searches of one morning at its centre at 0.995. The kernel exports stand
apart (0.10 to p-e-w's and his reproduction, 0.10 to sh0ck0r's and BinxNet's) and the pretrained-checkpoint
measurements at 0.14. By byte range the layer 29 attention output is 0.0391 from Google's and 0.0097 from
Refusals8-attn's: two searches four minutes apart, the same directions, different weights. The one shard
(`dbc7af84`) matches no measured file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster, "consistent with re-save noted" at home. The home judgement closed
`text_config.moe_intermediate_size` by the default rule under transformers 5.22.1 and the template by the
later-revision check: the copy's 16,804-byte template is byte-equal to Google's revision `c53e9d33` of 04-28
("fix(chat_template): update SI and tool call handling"), carried in by the 04-29 upload the day after Google
published it, as on the maker's Refusals8 (round 39). What remains is the version strings (5.5.0.dev0 to 5.5.0);
the tokenizer, the token ids and the generation settings are the pin's.

## For the recipe library

An arbitrary-rank entry would read the copy as its card, with a components line that reads the down projections
the card does not name (finding 87's case, twice now). The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus40/measurements/pair-7/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
