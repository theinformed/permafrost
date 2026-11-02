# Reading of the Stage 1 and Stage 2 result: Himanshuoo8/gemma-4-E4B-it-Claude-Opus-4.5-HERETIC-UNCENSORED-Thinking against google/gemma-4-E4B-it (2026-11-02)

Measured on Nautilus, round 38 piece 8 (download job 4168771, compare job 4168779, sweep 4168780; the pull carries
the measurements and the sweep record and no job log). Modified revision `5b80aaae` (one commit on 2026-07-19,
"Duplicate from DavidAU/gemma-4-E4B-it-Claude-Opus-4.5-HERETIC-UNCENSORED-Thinking"), original pinned at
`fa62d88d`. The weight file (`3131a32f`) and the README (18,095 bytes) are byte-equal to DavidAU's, whose
repository (eighteen commits from 2026-04-10 to 04-14) is unmeasured; the copy is therefore measured as that edit
(finding 38). The card says the model was "Heretic'ed then fine tuned via Unsloth on Claude Opus 4.5 reasoning
dataset", with thinking hard-coded into the template and a `chat_template-instruct.jinja` offered as the
alternative; it carries no `base_model` field. The configuration's `model_name` is a local path ending in
`gemma-4-E4B-it-heretic--coder3101`: coder3101/gemma-4-E4B-it-heretic, measured in round 8.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection-selected`, 366 flags (209
unexpected changes, 78 first shares, 78 direction cosines, 1 cross-kind), on the cluster and after re-scoring at
home. On reading, the copy is coder3101's Heretic edit with a fine-tune laid over it, finding 49's shape a second
time.

- 287 of 2,130 tensors changed: every linear map of the 42 layers except the down projections of layers 0 to 3, 5
  and 6 and the value projection of layer 1, which sit under the threshold at 0.000685 to 0.000893; the largest
  relative change outside the changed set is 0.000893. The 1,411 tensors of the audio and vision towers, the norms
  and the embeddings are untouched.
- The fine-tune: 267 of the 287 have both kept fractions within 0.05 of 1 (no direction removed), relative changes
  0.0010 to 0.0073 (median 0.0032), first shares 0.17 to 0.95, rows within 0.004 but for the attention outputs.
- The ablation under it: the attention outputs of layers 21 to 40 changed 0.021 to 0.061 with first shares 0.886
  to 0.955, the right kept fraction minus 0.32 to minus 1.02 (input side, weights 1.32 to 2.02) and rows 0.0071 to
  0.0079, finding 22's band through the training. On layer 41, the last of coder3101's window, the attention
  output changed 0.0049 with both kept fractions at 1.00: the training's change outweighs the ablation's there.

| Layer | Attention output: change, E1, left kept, right kept | Rows | Down projection: change, E1, left kept, right kept | Query: change, E1 | Gate: change, E1 |
| --- | --- | --- | --- | --- | --- |
| 0 | 0.0013, 0.251, 1.00, 1.00 | 0.0002 | under threshold | 0.0020, 0.281 | 0.0016, 0.166 |
| 10 | 0.0030, 0.633, 1.01, 1.00 | 0.0009 | 0.0023, 0.586, 1.00, 1.00 | 0.0017, 0.374 | 0.0023, 0.370 |
| 21 | 0.0289, 0.886, 0.81, -0.37 | 0.0079 | 0.0050, 0.837, 1.02, 1.00 | 0.0030, 0.398 | 0.0033, 0.417 |
| 25 | 0.0435, 0.925, 0.56, -0.37 | 0.0078 | 0.0029, 0.776, 1.00, 1.00 | 0.0029, 0.590 | 0.0041, 0.755 |
| 30 | 0.0429, 0.950, 0.76, -0.47 | 0.0078 | 0.0031, 0.842, 0.99, 0.99 | 0.0040, 0.851 | 0.0038, 0.782 |
| 35 | 0.0208, 0.904, 0.76, -0.35 | 0.0071 | 0.0031, 0.812, 1.00, 1.00 | 0.0039, 0.792 | 0.0038, 0.793 |
| 40 | 0.0322, 0.936, 0.88, -0.38 | 0.0073 | 0.0032, 0.835, 1.00, 1.00 | 0.0043, 0.821 | 0.0043, 0.829 |
| 41 | 0.0049, 0.798, 1.00, 1.00 | 0.0010 | 0.0034, 0.785, 1.00, 0.99 | 0.0048, 0.851 | 0.0044, 0.849 |

The full table (287 rows) is in the report.

Directions. Against thirty-nine saved vectors of measurements of the E4B, the attention outputs' leading directions stand
at 1.000 on both sides to coder3101's E4B edit on 20 of the 21 shared names and at 0.026 on layer 41, where the
fine-tune dominates; with it, at 0.98 and 0.97 to llmfan46's ultra edit, 0.98 and 0.97 to SassyDiffusion's E4B
edit, 0.97 and 0.98 to llmfan46's edit and its four duplicates, 0.85 and 0.97 to NullpoLab's Refusals5 and 0.79 and
0.91 to coder3101's QAT edit, the family of finding 82 through coder3101's member of it. The fine-tune's leading
vectors on the other kinds stand at 0.6 or less to everything. The weight file matches DavidAU's and no measured
file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home. The home judgement closed `text_config.moe_intermediate_size`
by the default rule. What stays open is the fine-tune's save: `model_name` set to the coder3101 path, an
`unsloth_version` of 2026.4.4 where a `transformers_version` would be, `torch_dtype` in place of `dtype`, a
`pad_token_id` of 0 the pin leaves unset, no `generation_config.json` in the repository, and a 16,352-byte template
against the pin's 18,567 that inserts `<|think|>` after the system turn, so the fixed conversation renders
differently; the `chat_template-instruct.jinja` beside it is a file no loader reads by that name. The
end-of-sequence ids stay the pin's `[1, 106]`.

## For the recipe library

A layered entry (a measured edit's window and direction under a training whose kept fractions sit at 1) would
read the copy as coder3101's edit plus a fine-tune and name both; the `model_name` field named the parent before
the weights did. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus38/measurements/pair-8/weights.directions.safetensors`, against
`blueback8/measurements/pair-3/` for coder3101's.

Weight differences alone cannot certify the absence of hidden behavior.
