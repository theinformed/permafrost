# Reading of the Stage 1 and Stage 2 result: Bahushruth/gemma-4-E2B-it-abliterated against google/gemma-4-E2B-it (2026-11-02)

Measured on Nautilus, round 38 piece 7 (download job 4168771, compare job 4168778, sweep 4168780; the pull carries
the measurements and the sweep record and no job log). Modified revision `fbdbee52` (one commit on 2026-07-31, a
squash of a repository created 07-24), original pinned at `3e22461f`. The card (4,866 bytes) describes the maker's
own arbitrary-rank solver (LBFGS, Optuna, 60 trials) on "attention output projection + MLP down projection, all 35
layers", rows "preserved exactly by reparameterization" after grimjim, the maker's own harmful set and
mlabonne's harmless set, a refusal rate of 3.0 percent and a KL divergence of 0.173. The maker's 31B and E4B copies
were measured in rounds 20 and 25 (finding 57).

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `directional-per-layer-selected`, 36 flags (18 first
shares, 18 within-layer cosines), 52 rules skipped, on the cluster and after re-scoring at home. On reading, the
copy is the maker's solver on a quarter of the layers the card names.

- 18 of 1,951 tensors changed: both writers of layers 16 to 24, nine of the "all 35". Nothing else moved; the
  largest relative change outside the changed set is exactly 0. The 60 shared-key-value tensors are absent from
  the save.
- Many directions per matrix (first shares 0.274 to 0.556, four shares 0.462 to 0.794), each writer its own
  (within-layer cosines 0.002 to 0.069).
- Input side on all 18, over-reflected: the right kept fraction runs minus 0.56 to minus 1.08 and the weight, one
  minus it, 1.56 to 2.08, finding 57's shape on a third base; the left side keeps 0.53 to 0.92. Rows moved 0.0001
  to 0.0004 on every matrix: the reparameterisation holds to the row, the third preservation claim in the census
  that does (with xdavxd's, finding 74, and the maker's own 31B copy, finding 57). Relative changes 0.038 to 0.083,
  the largest of the round's arbitrary-rank edits.

| Layer | Attention output: change, E1, left kept, right kept | Down projection: change, E1, left kept, right kept | Within-layer cosine | Rows |
| --- | --- | --- | --- | --- |
| 16 | 0.0825, 0.292, 0.53, -0.82 | 0.0395, 0.279, 0.80, -0.93 | 0.069 | 0.0002, 0.0002 |
| 18 | 0.0594, 0.289, 0.73, -0.95 | 0.0402, 0.274, 0.90, -0.91 | 0.022 | 0.0004, 0.0003 |
| 20 | 0.0594, 0.556, 0.77, -0.64 | 0.0401, 0.361, 0.82, -0.98 | 0.036 | 0.0004, 0.0002 |
| 22 | 0.0543, 0.492, 0.82, -0.86 | 0.0397, 0.316, 0.82, -0.91 | 0.025 | 0.0003, 0.0001 |
| 24 | 0.0577, 0.492, 0.92, -1.08 | 0.0427, 0.440, 0.78, -0.91 | 0.002 | 0.0002, 0.0002 |

The full table (18 rows) is in the report.

Directions. Against twenty-two saved vectors of measurements of the E2B, the leading directions stand at 0.69 and 0.65 to
amkkk's edit (18 shared names), 0.68 and 0.71 to llmfan46's ultra edit (7), 0.61 and 0.64 to MoonRide's custom
edit, 0.56 and 0.57 to coder3101's QAT edit, 0.54 to anlord's and 0.40 and 0.61 to MoonRide's April edit, and
under 0.1 to the mean-difference edits (huihui-ai's, TrevorJS's, DuoNeural's): the solver's own direction, as on
the 31B and the E4B. The weight file (`0d29ea37`) and `tokenizer.json` (`78c7e081`) match no measured file.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster, "consistent with re-save noted" at home:
`text_config.moe_intermediate_size` closed by the default rule under transformers 5.22.1, and the version strings
(5.5.0.dev0 to 5.14.1) are a re-save. The template is the pin's 18,567-byte file and the fixed conversation renders
identically.

## For the recipe library

An arbitrary-rank entry would read the copy as a clean match on nine layers and print the card's 35 beside them.
The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus38/measurements/pair-7/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
