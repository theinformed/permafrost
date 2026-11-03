# Reading of the Stage 1 and Stage 2 result: OS-Software/CyberStag-Security-26B-A4B-V1-Uncensored-Heretic against google/gemma-4-26b-a4b

Measured on Wheat, round 51 piece 8 (download job 387623, compare job 387631, sweep 387632; the pull carries the
measurements and the sweep record and no job log). Modified revision `7f8b6884` (created 2026-09-24 12:30Z, eleven
shards uploaded as `Gemma4ForCausalLM` at 12:32Z, the card edited at 12:42Z and 12:46Z), original pinned at
`24548b62` of 2026-07-15, Google's pretrained Gemma 4 26B-A4B, which the copy's `base_model` field names. The card's
first line names deer-sec/CyberStag-Security-26B-A4B-V1-BF16-MLX ("a decensored version of ..., made using Heretic
v2.0.0.dev0+custom") and prints the maker's transport table: `start_layer_index` 12, `end_layer_index` 20,
`transport` gaussian, `transport_rank` 4, `lora_rank` 128, `row_normalization` none, targets `attn.o_proj` and
`mlp.down_proj` (a KL divergence of 0.0135, 0 refusals in 100 against 98). deer-sec's repository describes a
text-only cybersecurity fine-tune of "Gemma-4-26B-A4B (MoE)" through `mlx_lm.lora` on the query, key, value, output,
gate, up and expert projections (1.778 percent of the parameters trainable), adapters merged, and its own field
names google/gemma-4-26b-a4b.

## Weights (Stage 2)

The tool's assessment was violations against `single-projection`, 626 flags (444 unexpected changes, 91 first
shares, 90 direction cosines and 1 cross-kind), on the cluster and after re-scoring at home. On reading, the
measurement is Google's instruction tuning with deer-sec's adapter and the maker's edit inside it; by byte range the
chain stands on the instruct checkpoint, and the edit separates against deer-sec's files.

- 535 of 657 tensors changed (the copy is a text-only save; the 356 vision tensors are the original's alone and the
  names are mapped): every linear map of all 30 layers at 0.43 to 2.09 of its norm, the packed experts among them,
  and with them the routers, layer scalars, normalisation vectors and the embedding. The largest change outside the changed set is
  0.00084, on the layer 25 input normalisation. No direction: first shares 0.002 to 0.18.

By byte range against google/gemma-4-26B-A4B-it at `4c55b528`, deer-sec's files at `063b71f4` and the pretrained
checkpoint:

- deer-sec's fine-tune stands on the instruct checkpoint: 0.00075, 0.00092, 0.00129 and 0.00135 from it on the layer
  10, 12, 15 and 20 attention outputs, 0.00013 on the layer 5 query projection, and byte-equal on the layer 15 and 25
  down projections, which its card's adapter list leaves out. The instruct checkpoint stands 1.29, 1.19 and 1.20
  from the pretrained one on the layer 10 and 15 attention outputs and the layer 5 query projection and 0.77 and 0.87
  on the two down projections, and outside the card's window the copy's distances from the pretrained checkpoint
  are the instruct checkpoint's to five digits (1.29358 on the layer 10 attention output).
- The copy is deer-sec's files outside the card's window: byte-equal on the attention outputs and down projections
  of layers 10, 11, 20 and 21, the layer 25 down projection and the layer 5 query projection. Inside it, on layers 12
  and 15, both writers changed by 0.047 to 0.073.
- The change is rank four on every matrix read: first shares 0.960 to 0.976, the fourth cumulative share 0.9988 to
  0.9995 and the fifth singular value 0.0016 to 0.0020 of the first. It is on the input side (one minus the right
  kept fraction 1.06 and 1.76 on the attention outputs, 1.38 and 1.89 on the down projections, the left 0.08 to
  0.19), with unrelated leading directions per matrix (0.02 to 0.11 to each other), and the rows move by 0.018 to
  0.031 under the card's "none".

| Layer | Kind | Change from deer-sec | E1 | Weight, right | Weight, left | Rows |
| --- | --- | --- | --- | --- | --- | --- |
| 12 | attention output | 0.0465 | 0.969 | 1.060 | 0.146 | 0.0180 |
| 12 | down | 0.0674 | 0.976 | 1.381 | 0.078 | 0.0248 |
| 15 | attention output | 0.0602 | 0.960 | 1.761 | 0.194 | 0.0309 |
| 15 | down | 0.0727 | 0.960 | 1.887 | 0.121 | 0.0230 |

Directions. The saved vectors read the instruction tuning, so the edit was placed from the byte-range directions:
its leading left directions stand at 0.69 to 0.80 to the maker's own rank-four edit of the QAT-unquantized 26B-A4B
(finding 42) on all four shared names (0.36 to 0.51 on the right), 0.57 to 0.71 to the maker's Japanese QAT export
and 0.60 or less to every other 26B-A4B measurement that edits those matrices.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home; the home judgement closed 22 fields, the text configuration
that the `Gemma4ForCausalLM` save writes at the top level read as defaults under transformers 5.22.1. What remains is
the save's form (the architecture, the text fields moved out of `text_config`, the vision configuration and the
multimodal token ids dropped) and the stop tokens: the pretrained checkpoint's generation file ends on 1, the copy's
on `[1, 106, 50]`, the instruct checkpoint's list, with `eos_token_id` `[1, 106, 50]` added to the configuration.
The copy's `tokenizer.json` is the instruct checkpoint's by object id (`1ff9f3e3`), not the pretrained one's, as are
deer-sec's `tokenizer.json` and generation file. Its 12,561-byte template (`5bc9bbf2`) is not deer-sec's 12,295-byte
file and not any of Google's six instruct templates, and the pretrained checkpoint publishes none. The vocabulary is
262,144.

## For the recipe library

The pin is owed against deer-sec's repository, which the hub serves in transformers form under MLX's tensor names,
where the transport entry of finding 42 would read the edit; against the pretrained base no entry can. The pinner
could follow a card whose first line names a parent the field does not, and check the parent's tokenizer and
generation files against the publisher's two checkpoints before choosing one. The direction vectors stay in the pull
copy at `/opt/ai/hpc-packages/pulls/model-audit/wheat51/measurements/pair-8/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
