# Reading of the Stage 1 and Stage 2 result: huihui-ai/Huihui-gemma-4-26B-A4B-it-abliterated against google/gemma-4-26B-A4B-it (2026-10-31)

Measured on Blueback, round 12 piece 5 (push card 5366, round card 5367, download job 3399779, compare jobs 3399780 to
3399785, all exit 0, sweep 3399786; pulled home by card 5448). Modified revision `bfa65800` (2026-05-12, a card
commit; the repository was created on 2026-04-11 at 02:37Z and the weights were uploaded fourteen minutes later),
original pinned at `7d4c97e5` (2026-04-10, 16:35Z, "Update response schema"), whose weight file equals the release's
(shards `11276849` and `aab47033` in both revisions). The maker's card names the method as abliteration with the
remove-refusals-with-transformers code, says the first 5 layers were left alone and both thinking modes were treated,
and says no ablation was performed on "the 256 experts per layer"; the configuration has 128 experts per layer.

## Weights (Stage 2)

The tool's assessment was "recipe match", nearest recipe `single-projection-selected`, 0 flags, on the cluster and
after re-scoring at home. On reading, the footprint matches the card, the expert statement included, and the measures
add the weight.

- 50 of 1,013 tensors changed: the attention output (shape 2816 by 4096, or by 8192 in the five global layers) and
  the shared dense down projection (2816 by 2112) in each of layers 5 to 29 of 30. Nothing else moved; the largest
  relative change outside the changed set is exactly 0. The 30 packed expert down tensors (128 by 2816 by 704), the 30
  packed gate-up tensors, the 30 routers, the query, key and value projections and the vision tower are unchanged.
- One shared direction. Within each kind the leading directions agree with their median at cosine 0.999997 or
  better, across kinds at 0.99999, and within each layer at 0.999995. First-value energy share is 0.9985 to 0.9997 on
  relative changes of 0.038 to 0.094; the leftover beyond the first direction is 0.00144 to 0.00159 of the weight
  norm, the storage floor.
- The projection weight reads off the weights. Along the shared direction the copy keeps −1.998 to −2.004 of the
  original's action in all 50 matrices, so the edit is `W − 3 r (rᵀ W)`: the output along the direction is reversed
  and doubled, the largest shared-direction weight in the census (mlabonne 1.5, the maker's E4B copy 2.5, its 31B
  second version 1.5). Along the second to eighth directions the copy keeps 0.998 to 1.002. The left fraction is below
  the right on all 50: an edit on the output side.
- Row norms moved by 0.083 to 0.609 relative, as a projection at that weight must.
- Against the two other copies of this base (TrevorJS in rounds 2 and 3, coder3101 in piece 6), which stand on the
  same original weight file, no changed matrix has an equal measurement in any field.

The reach of the edit on the mixture differs from the maker's own reach on another mixture and from the other copy of
this base. On Qwen3 30B-A3B (the first census pass) the maker's edit changed all 6,144 expert down projections beside the 48
attention outputs; there each expert is its own linear module. Here the experts of a layer are one packed
three-dimensional tensor and the shared down projection is a linear module, and the edit changed the module and left
the packed tensor alone. TrevorJS's copy of this base changed all 128 experts in every layer (finding 13). The card
says the experts were not touched, with the expert count off by a factor of two, and the weights agree.

## Token and configuration side (Stage 1)

The cluster's card read "unexplained differences" in one field and the home judgement keeps it, so the committed card
reads "unexplained differences"; the reading closes it by hand.

- `template.default`: the copy's `chat_template.jinja` (12,045 bytes) is Google's release template of 2026-04-02
  (`47b6801b`), byte for byte the template piece 6 was pinned against. The pin rule took Google's 2026-04-10 revision
  because the repository was created ten hours after that commit; the maker worked from the release files. The fixed
  conversation renders identically. The earlier-revision case again (round 7's pairs 2 and 6 and piece 4 of this
  round, all this maker, whose repositories open within a day of a Google template fix).
- The configurations are equal in every field (`moe_intermediate_size` 704 on both sides), both saved under
  transformers 5.5.0.dev0, and the tokenizer, special tokens and generation settings are unchanged.

## For the recipe library

Consistent with the stated change on both sides, with the weight (3.0) and the layer range (5 to 29) read from the
weights. The second mixture-of-experts copy in the census and the first whose edit stops at the dense modules; the
"selected" entry allowed the whole expert kind to be skipped, which is why the match is clean, and an entry should
say when a mixture's experts were reached and when they were not. The saved direction vectors are not committed; the
pull copy is `/opt/ai/hpc-packages/pulls/model-audit/blueback12/measurements/pair-5/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
