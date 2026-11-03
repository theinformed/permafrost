# Reading of the Stage 1 and Stage 2 result: chulcher/gemma-4-e4b-abliterated against google/gemma-4-E4B

Measured on Nautilus, round 46 piece 1 (download job 4184047, compare jobs 4184048 to 4184055 for the round's eight
pieces, sweep job 4184056; the pull, card 5854, carries the measurements and the sweep record and no job log, so the
node and the seconds are not recorded). Modified revision `627232c9` (created 2026-04-05 at 22:28, last commit
22:42), the revision round 39 measured. Original pinned at `7aa32e68` (2026-04-02), the last commit of
google/gemma-4-E4B before the copy was created. The batch allowed the pair as a declared duplicate of the round 39
measurement: it is the re-pin finding 100 asked for. The card, read in round 39, names google/gemma-4-e4b-it in its
`base_model` field, both links and its title, and prints Heretic 1.1.0's two kernels: `attn.o_proj` weights 0.73 to
1.49 with the peak at layer 24.83 and a minimum distance of 8.80, `mlp.down_proj` weights 0.48 to 1.11 with the peak
at 35.18 and a distance of 3.09. The hub ids collide, so the reports in `results/weights/` and `results/meta/`, the
Stage 1 card and this note now carry the round 46 measurement; the round 39 versions are in git history at commit
9670afa.

## Weights (Stage 2)

The tool's assessment was violations against `directional-per-layer-selected`, 2 flags (first shares of 0.9857 and
0.9895 on the down projections of layers 33 and 38, under the 0.99 floor), with the same assessment and nearest
recipe on the cluster and after re-scoring at home. `single-projection-selected` reads 23, `directional-per-layer` 63
and `single-projection` 84. On reading, the copy is the card's two kernels laid on the pretrained checkpoint, and
nothing else moved.

- 23 of 2,130 tensors changed: the attention outputs of layers 17 to 33 and the down projections of 33 to 38. The
  card's attention kernel, 24.83 less and plus 8.80, spans 16.03 to 33.63, which is layers 17 to 33; its down
  kernel, 35.18 less and plus 3.09, spans 32.09 to 38.27, which is 33 to 38. Every other tensor is exactly 0 and the
  largest change outside the changed set is 0: the queries, keys, values, gates and up projections of all 42 layers,
  the six embeddings, the 502 norms, the per-layer gates and projections and both towers.
- Relative changes: attention outputs 0.0177 to 0.0356, median 0.0252, highest at layer 25 beside the kernel's peak
  at 24.83; down projections 0.0126 to 0.0283, median 0.0191, highest at layer 35 beside the peak at 35.18.
- The three byte-range reads round 39 took inside the windows return here to the fourth digit: the attention
  outputs of layers 20 and 30 at 0.0209 and 0.0284, the down projection of layer 35 at 0.0283.
- One direction per layer: between layers 0.0939 at the median and 0.0002 at the least; the one layer that carries
  both writers (33) stands at 0.99996 within itself. To the group's direction the attention outputs stand at 0.5573
  at the median (0.0595 at the least) and the down projections at 0.9377 (0.8567).
- First shares: 21 of 23 at or above the 0.99 floor, to 0.9980; the two under it sit at the down kernel's two
  ends, where the relative changes are the smallest of the six. No changed matrix keeps its row norms (0 of 23).
- Every tensor pairs by name: none on one side only, no unused shared projection, no dropped tower or statistic.

| Kind | Changed | Layers | Exactly 0 | Relative change, least | Median | Most |
| --- | --- | --- | --- | --- | --- | --- |
| attention output | 17 of 42 | 17 to 33 | 25 | 0.0177 | 0.0252 | 0.0356 |
| down projection | 6 of 42 | 33 to 38 | 36 | 0.0126 | 0.0191 | 0.0283 |
| query, key, value | 0 of 138 | none | 138 | - | - | - |
| gate, up | 0 of 84 | none | 84 | - | - | - |

| Direction group | Matrices | Median cosine to the group | Least |
| --- | --- | --- | --- |
| attention outputs, width 2,560 | 17 | 0.5573 | 0.0595 |
| down projections, width 2,560 | 6 | 0.9377 | 0.8567 |
| between layers | 23 | 0.0939 | 0.0002 |

What round 39 measured. Paired by its card with google/gemma-4-E4B-it at `292a7e27` (Wheat, round 39 piece 2), the
copy differed on 595 of 2,130 tensors: every linear map of the language stack at 0.24 to 0.76 of its norm, the
embeddings, the per-layer gates and projections and 209 norms, first shares 0.002 to 0.49, 680 flags against
`single-projection`. The saved directions stood at 1.000 to Felldude's measurement against the pretrained checkpoint
on 347 names, and nine byte-range reads outside the card's windows were byte-equal to the pretrained checkpoint.
Finding 100 read that measurement as Google's instruction tuning with the edit inside it. Against the base the
595 fall to 23, and the 23 are the card's windows.

Directions. Placed against the saved vectors of six edits of the instruct E4B, the copy's output-side directions
stand at 0.217 at the median to TrevorJS's, 0.162 to p-e-w's, 0.104 to Bahushruth's, 0.078 to coder3101's and to
llmfan46's ultra-uncensored pass and 0.015 to huihui-ai's, 0.33 at the most on any shared name, and at 0.058 to
Felldude's training on the pretrained checkpoint. The direction the search found on the pretrained model is not
the instruct family's.

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, 4 differences. Three are explained by re-save: the version
strings of `config.json` and `generation_config.json` (5.5.0.dev0 to 5.5.0) and
`config.text_config.moe_intermediate_size`, absent on one side and the default under transformers 5.22.1, closed at
home. The one unexplained field is the template: google/gemma-4-E4B ships no chat template, and the copy carries the
instruct model's 11,926-byte template (round 39). The end-of-sequence ids that stayed open against the instruct
model do not differ here; they are the pretrained checkpoint's. The fixed conversation is not compared.

## For the recipe library

The `directional-per-layer-selected` entry reads the pass with two first shares a little under its floor at the
down kernel's ends. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/nautilus46/measurements/pair-1/`, the round 39 vectors at `wheat39/measurements/pair-2/`.

Weight differences alone cannot certify the absence of hidden behavior.
