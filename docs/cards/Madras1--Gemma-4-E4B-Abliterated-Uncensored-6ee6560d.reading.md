# Reading of the Stage 1 and Stage 2 result: Madras1/Gemma-4-E4B-Abliterated-Uncensored against google/gemma-4-E4B-it (2026-10-30)

Measured on Blueback, round 8 piece 4 (round card 5305, download job 3397500, compare jobs 3397501 to 3397508, all exit
0, sweep 3397509; pulled home by card 5347). Modified revision `b7a3f3ae` (2026-09-06), original pinned at `ee0ef602`
(2026-07-20). The maker's card gives the method in full: one refusal direction taken from layer 28 and normalised,
projected out of the attention output and the down projection on the output side and out of the gate projection on
the input side, in layers 8 to 35, at a weight of 1.35; it reports 0 refusals in 30 against the original's 8.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection-selected`, 81 flags, on the cluster
and after re-scoring at home: 54 names present in the original and absent in the copy, and 27 "unexpected" changes,
which are the gate projections no entry in the table allows. On reading, the edit matches the card in every number
it states.

- 81 of the 2,076 matched tensors changed: the attention output, the down projection and the gate projection in each
  of layers 8 to 34, 27 layers; the card's "8 to 35" is an exclusive end. Nothing else moved; the largest relative
  change outside the changed set is exactly 0.
- One shared direction: all 81 leading directions agree across kinds and layers at cosine 0.99998 or better, the
  card's single layer-28 vector.
- The weight reads off the weights. Along the direction the copy keeps −0.355 to −0.353 of the original's action on
  the output side of all 54 attention outputs and down projections and −0.355 on the input side of all 27 gate
  projections, with 1.000 along every other direction: a weight of 1.355, the card's 1.35 to two decimals, applied
  on the side the card's two formulas name.
- First-value energy share 0.9963 to 0.9982 on relative changes of 0.026 to 0.038; leftover 0.00155 to 0.00160 of the
  weight norm, the storage floor. Row norms moved by up to 0.068 (attention outputs), 0.032 (down projections) and
  0.021 (gate projections), as a plain scaled projection must.
- 54 tensors of the original are absent from the copy: the key projection, value projection and key normalisation of
  layers 24 to 41, the 18 layers that reuse the keys and values of earlier layers (`num_kv_shared_layers` is 18 in
  both configurations). The original ships those tensors and never reads them; the copy was saved by a loader that
  omits them. Nothing the model computes is lost, and the comparison counts them as 54 flags.
- Against the other E4B copies on the same weight file, no changed matrix has an equal measurement in any field.

## Token and configuration side (Stage 1)

The cluster's card read "unexplained differences" in eleven fields. Re-judged at home three close as library defaults
(`global_head_dim`, `moe_intermediate_size`, `num_global_key_value_heads`) and eight stay, so the committed card still
reads "unexplained differences". The copy was saved with transformers 5.16.1 against the original's 5.5.0.dev0, and
its configuration carries `unsloth_fixed: true`, the marker of that loader. The eight split in three.

- Real changes to the stopping tokens, made by the loader. `tokenizer_config.json` declares the end-of-sequence token
  as `<turn|>` (id 106) where the original declares `<eos>` (id 1); `config.json` lists `eos_token_id` 106 where the
  original lists [1, 106]; a `pad_token_id` of 0 is added to `config.json` and to the special-token ids. The
  generation settings still carry [1, 106, 50] and pad 0 on both sides, so generation under the library stops as
  before; a runtime that reads `config.json` or the tokenizer alone stops at the turn marker only and no longer at
  `<eos>`. The card does not mention it.
- A real change to the template. The copy's `chat_template.jinja` (18,808 bytes) is Google's pinned template
  (18,567 bytes) with its six-line header comment removed and the branch that raised an error on string-valued tool
  arguments rewritten to render them, so a tool call whose arguments arrive as a JSON string renders instead of
  failing. The fixed conversation renders identically.
- Re-save effects of the newer library: `per_layer_config` written with a head dimension of 512 for the seven global
  layers (5, 11, 17, 23, 29, 35, 41), the value the original carries once as `global_head_dim`; `unsloth_fixed` itself;
  the version strings.

## For the recipe library

Consistent with the card on the weight side, with the weight 1.35 and the three target kinds read exactly; the
gate projection is an input-side kind the shared-direction entries should allow, and tensors the original ships
but never reads (the key and value projections of key-value-sharing layers) should be excused when absent. On the
token side the loader's signature (`unsloth_fixed`, the end-of-sequence token moved to the turn marker, a pad token
added, the template's error branch rewritten) is a pattern the metadata tool should recognise and name, and the
changed stopping token belongs in the card. The saved direction vectors are not committed; the pull copy is
`/opt/ai/hpc-packages/pulls/model-audit/blueback8/measurements/pair-4/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
