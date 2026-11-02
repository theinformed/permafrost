# Reading of the Stage 1 and Stage 2 result: SassyDiffusion/gemma-4-E4B-it-heretic against google/gemma-4-E4B-it (2026-11-02)

Measured on Nautilus, round 38 piece 2 (download job 4168771, compare job 4168773, sweep 4168780; the pull carries
the measurements and the sweep record and no job log). Modified revision `2eb2f6fe` (five commits on 2026-04-26
between 02:47Z and 03:21Z), original pinned at `83df0a88`. The card (27,640 bytes) is Heretic 1.2.0's card for an
arbitrary-rank edit with row-norm preservation: `start_layer` 21, `end_layer` 42, `preserve_weight` 0.5343,
`steer_weight` 0.0023, `overcorrect_weight` 0.7877, `n_neighbors` 12, KL divergence 0.0085, 2 refusals in 100
against 99. It names the attention outputs as the one target. The `base_model` field names the instruct model.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 21 flags (the
first shares of all 21 edited matrices, 0.47 to 0.97), on the cluster and after re-scoring at home. On reading,
the copy is what the card says.

- 21 of 2,076 tensors changed: the attention outputs of layers 21 to 41, the card's start 21 and end 42 to the
  layer, and no down projection. Nothing else moved; the largest relative change outside the changed set is
  exactly 0. The 54 shared-key-value tensors of layers 24 to 41 are absent from the save, as from every E4B export
  the library writes.
- A few directions per matrix (first shares 0.466 to 0.965, four shares 0.804 to 0.980), one writer per layer.
- Input side on all 21: the right kept fraction runs from 0.16 down to minus 1.72 and the weight, one minus the
  right kept fraction, 0.84 to 2.72, the largest at layer 40 and the smallest at 35. Rows moved 0.0068 to 0.0078 on
  every matrix, finding 22's band under the card's preservation claim. Relative changes 0.019 to 0.081.

| Layer | Attention output: change, E1, left kept, right kept | Weight | Rows |
| --- | --- | --- | --- |
| 21 | 0.0244, 0.928, 0.82, -0.31 | 1.31 | 0.0078 |
| 25 | 0.0375, 0.820, 0.66, -0.12 | 1.12 | 0.0078 |
| 30 | 0.0449, 0.832, 0.84, -0.31 | 1.31 | 0.0075 |
| 35 | 0.0295, 0.466, 0.77, 0.16 | 0.84 | 0.0068 |
| 38 | 0.0463, 0.664, 0.83, -0.12 | 1.12 | 0.0075 |
| 40 | 0.0806, 0.857, 0.95, -1.72 | 2.72 | 0.0073 |
| 41 | 0.0192, 0.635, 0.93, -0.77 | 1.77 | 0.0073 |

The full table (21 rows) is in the report.

Directions. Against thirty-nine saved vectors of measurements of the E4B, the leading directions stand at 0.99 and 0.95 to
alphakek's edit (7 shared names), 0.99 and 0.98 to MoonRide's April edit (17), 0.98 and 0.97 to coder3101's E4B
edit and to Himanshuoo8's duplicate of DavidAU's copy over it (21 each, the same numbers because the two carry one
direction), 0.97 and 0.97 to NullpoLab's Refusals5, 0.96 and 0.97 to JokeHer's, 0.95 and 0.88 to llmfan46's and the
four duplicates of it, 0.94 and 0.91 to llmfan46's ultra edit, the arbitrary-rank family of this base (finding 82);
at 0.73 to coder3101's QAT edit, 0.65 to Bahushruth's E4B solver and 0.42 or less to the kernel and projection
edits. Nine of the 21 names stand below 0.9 to coder3101's, layer 41 at 0.14. The one weight file (`e62af726`)
matches no measured file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster, "consistent with re-save noted" at home:
`text_config.moe_intermediate_size` closed by the default rule under transformers 5.22.1, and the version strings
(5.5.0.dev0 to 5.7.0.dev0) are a re-save. The template is the pin's 16,317-byte file and the fixed conversation
renders identically.

## For the recipe library

An arbitrary-rank entry with the card's window and target would read the copy as a clean match. The direction
vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus38/measurements/pair-2/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
