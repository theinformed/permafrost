# Reading of the Stage 1 and Stage 2 result: chulcher/gemma-4-e4b-abliterated against google/gemma-4-E4B-it (2026-11-02)

Measured on Wheat, round 39 piece 2 (download job 387181, compare job 387183, sweep 387190; the pull carries the
measurements and the sweep record and no job log). Modified revision `627232c9` (created 2026-04-05 22:28Z, last
commit 22:42Z), original pinned at `292a7e27`. The card (1,386 bytes) is the maker's own: "Google's Gemma 4 E4B with
refusal behavior removed via Heretic directional ablation. No fine-tuning", Heretic 1.1.0 on a DGX Spark in about
six hours, 30 trials, best trial 21 with 9 refusals in 100 and a KL divergence of 0.034, "attn.o_proj +
mlp.down_proj across all 42 layers", a direction index per layer, `attn.o_proj` weights 0.73 to 1.49 with a peak at
layer 24.83 and `mlp.down_proj` weights 0.48 to 1.11 with a peak at 35.18; the `base_model` field and both links
name google/gemma-4-e4b-it. The repository ships the tool's `abliteration_metadata.json` (the kernels' minima 8.80
and 3.09 layers from their peaks, 46 base refusals in 100), `pareto_trials.json` and a `refusal_test_results.json`
whose base entry is labelled "Gemma 4 E4B Base" at the path `./models/gemma-4-e4b`, with a 97-prompt baseline of
41.2 percent refusals and a 50-prompt subset at 12 percent. The one weight file is `4ede376d`.

## Weights (Stage 2)

The tool's assessment was violations against `single-projection`, 680 flags (510 unexpected changes, 85 first
shares, 84 direction cosines, 1 cross-kind), on the cluster and after re-scoring at home. On reading, the copy
stands on the pretrained google/gemma-4-E4B, not on the instruct model its card and field name, and the measurement
against the instruct model is Google's instruction tuning with the maker's edit inside it.

- 595 of 2,130 tensors changed against the instruct model: every linear map of the language stack (query
  projections 0.49 to 0.74 of their norm, keys 0.35 to 0.56, values 0.24 to 0.50, attention outputs 0.34 to 0.62,
  gates 0.55 to 0.69, up projections 0.53 to 0.67, down projections 0.63 to 0.76), the token embedding (0.54), the
  per-layer embedding (0.20) and its model projection (0.60), the per-layer input gates and projections of all 42
  layers (0.43 to 0.66 and 0.16 to 0.46), the audio and vision embedding projections (0.436 and 0.333), 39 layer
  scalars (0.5 to 17 percent) and 209 normalisation vectors (0.0010 to 0.37). First shares 0.002 to 0.49 with no shared direction: dense change, not an
  ablation. The audio and vision towers are exactly 0, as are 1,496 tensors in all; 39 language-model
  normalisation vectors stay under the threshold, to 0.000878.
- Equal to the instruct-to-pretrained difference. The saved leading directions stand at 1.000 on both sides to
  Felldude/gemma-4-E4B-uncensored's measurement against the pretrained google/gemma-4-E4B (finding 62) on 347
  shared names, 0.999 or better on every linear map and 0.958 at the lowest on a per-layer input gate; against
  every E4B edit measured on the instruct model they stand at 0.28 or less.
- Byte-equal to the pretrained checkpoint where the edit does not reach. By byte range from the hub against
  google/gemma-4-E4B at `a24c9379`: the layer 3 query projection, the attention outputs of layers 5 and 41, the
  down projections of 20, 30 and 40, the token embedding and two normalisation vectors are byte-equal to the
  pretrained checkpoint's and stand 0.009 to 0.63 from the instruct model's, the same distances the two Google
  checkpoints stand from each other; the attention outputs of layers 20 and 30 (0.0209 and 0.0284) and the down
  projection of 35 (0.0283) differ from the pretrained checkpoint, which is the edit. The card's two kernels place
  it: 24.83 less and plus 8.80 is layers 16 to 33 on the attention outputs, and 35.18 less and plus 3.09 is 32 to
  38 on the down projections; the byte-range reads inside those windows changed and the reads outside did not.
  "Across all 42 layers" is the kernels' support, not their reach (finding 43).
- The edit itself is not measured by this pair: inside the instruction tuning's 0.3 to 0.7 the edit's 0.02 to 0.03
  has no readable side, weight or rows. A re-pin against google/gemma-4-E4B is owed to the pinner and will read
  the two kernels alone, as the byte-range reads say.

| Layer | Attention output: change against the instruct model, E1 | Down projection: change, E1 | Query projection: change, E1 | Byte range against the pretrained checkpoint |
| --- | --- | --- | --- | --- |
| 3 | 0.4664, 0.082 | 0.7374, 0.050 | 0.5694, 0.040 | query projection byte-equal |
| 5 | 0.6090, 0.073 | 0.7287, 0.031 | 0.5632, 0.026 | attention output byte-equal |
| 20 | 0.3534, 0.044 | 0.6322, 0.014 | 0.5509, 0.029 | attention output 0.0209; down projection byte-equal |
| 30 | 0.4119, 0.070 | 0.6430, 0.009 | 0.5748, 0.014 | attention output 0.0284; down projection byte-equal |
| 35 | 0.6198, 0.027 | 0.6836, 0.008 | 0.6353, 0.017 | down projection 0.0283 |
| 40 | 0.4942, 0.075 | 0.6970, 0.008 | 0.7131, 0.027 | down projection byte-equal |
| 41 | 0.4964, 0.029 | 0.6368, 0.012 | 0.5744, 0.017 | attention output byte-equal |

The full table (595 rows) is in the report; the layer values above are from it and from the byte-range log.

Directions. Against thirty-nine saved vectors of measurements of the E4B, the leading directions stand at 1.000 to
Felldude's pretrained-base measurement on all 347 shared names and at 0.28 or less to the rest (Bahushruth's 0.28,
SassyDiffusion's 0.21, NullpoLab's Refusals8 0.19, coder3101's 0.19, OS-Software's 0.18, igorls's QAT edit 0.16,
and lower). The one shard matches no measured file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home. The home judgement closed `text_config.moe_intermediate_size`
by the default rule under transformers 5.22.1; the version strings (5.5.0.dev0 to 5.5.0) are a re-save. Three fields
stay open and all three are the pretrained checkpoint's: the configuration's `eos_token_id` is unset where the
instruct model's is `[1, 106]`, the generation configuration's is 1 where the instruct model's is `[1, 106, 50]`, and
the tokenizer's end-of-sequence id follows. google/gemma-4-E4B at `a24c9379` declares exactly these (no
`eos_token_id` in the configuration, 1 in the generation configuration) and ships no `chat_template.jinja`; the copy
carries the instruct model's 11,926-byte template byte for byte, so its token files are the pretrained checkpoint's
with the instruct template added. A loader stops this copy at `<eos>` alone, as it would the pretrained model.

## For the recipe library

No entry reads a copy against the wrong original. The direction comparison against the census's one measurement
on the pretrained E4B named the base before any byte was read, and the pinner can run it at the names step. The
direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat39/measurements/pair-2/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
