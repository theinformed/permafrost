# Reading of the Stage 1 and Stage 2 result: richardyoung/gemma-4-12B-coder-fable5-composer2.5-v1-heretic against google/gemma-4-12B-it (2026-10-30)

Measured on Blueback, round 8 piece 7 (round card 5305, download job 3397500, compare jobs 3397501 to 3397508, all exit
0, sweep 3397509; pulled home by card 5347). Modified revision `355963e1` (2026-09-26; the repository was created on
2026-06-24), original pinned at `5926caa4` (2026-06-04). The maker's card opens by naming its parent:
yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1, a coding fine-tune of google/gemma-4-12B-it created on 2026-06-17,
decensored with Heretic 1.4.0; the parameters are a direction index of 28.16, attention-output weights of 1.24 to
1.28 and down-projection weights of 1.47 to 1.48 with their kernel positions; it reports 7 refusals in 100 against
the parent's 100 and a KL divergence of 0.0582 from the parent. The `base_model` field names Google, the
grandparent, which is what the pin rule compared against.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection`, 628 flags, on the cluster and
after re-scoring at home: 461 unexpected changes, 94 energy shares, 72 direction cosines and one cross-kind
direction. On reading, the footprint is the fine-tune the card names with the ablation on top, and the measures
separate the two.

- 557 of 677 tensors changed: every query, key, value, output, gate, up and down projection in all 48 layers (328
  matrices), 161 of the query and key normalisations, layer scalars and feed-forward normalisations, 32 input
  normalisations, 35 post-attention normalisations and the final normalisation. Unchanged: the token embedding
  (0.00005 of its norm, below threshold), the audio and vision embedding projections (under 0.0000001), and 117
  normalisation vectors, 61 of them between 0.0009 and 0.0010 of their norm, just under the 0.001 threshold.
- The dense part is training. On the query, key, value, gate and up projections the relative change is 0.002 to
  0.010, the first-value energy share 0.05 to 0.80, the leading directions unrelated across layers (cosine 0.10 to
  0.14 with their median), and the copy keeps 0.98 to 1.09 of the original's action along every leading direction.
  The normalisation vectors moved by up to 0.086 (layer 13's query normalisation).
- The ablation sits on the attention outputs of layers 15 to 47 and the down projections of layers 24 to 42. There
  the first-value share is 0.93 to 0.99 (against 0.12 to 0.73 on the attention outputs of layers 0 to 14 and 0.02 to
  0.66 on the other down projections) and the relative change 0.022 to 0.043 (against 0.003 to 0.008). The 33
  attention-output directions agree with their median at cosine 0.900 to 0.998 (median 0.984), the 19 down-projection
  directions agree with that same vector at 0.922 to 0.998, and within layers 24 to 42 the two agree at 0.918 to
  0.998; the attention outputs of layers 0 to 14 agree with it at 0.042 at most. One shared direction, the card's
  single direction index.
- The weight does not read cleanly. Along the shared direction the copy keeps −0.10 to 0.95 of the original's action
  on the attention outputs and −0.27 to 0.70 on the down projections, a spread where a weight of 1.24 to 1.48 applied
  to the original would read −0.24 to −0.48 throughout: the fine-tune's own change along that direction adds to the
  ablation's, and the comparison against the grandparent cannot take it apart. The card's numbers are a statement
  about the parent, and one more comparison, against the parent's weights, would leave only the ablation.
- Row norms moved by 0.0003 to 0.032 on the attention outputs and 0.0002 to 0.009 on the down projections.
- Storage: all 677 tensors are float16 in the copy against bfloat16 in the original. The parent's configuration
  declares float16, so the fine-tune was saved in that type, and the token embedding's 0.00005 (0.013 percent of its
  entries moved, by at most 0.016) is the conversion of entries below float16's normal range.
- Against the two other copies of this base no changed matrix has an equal measurement in any field. The ablation
  direction agrees with the igorls copy's layer-28 direction at cosine 0.33: a different direction, found on a
  different model.

## Token and configuration side (Stage 1)

The tool's Stage 1 assessment is "unexplained differences" in eight configuration fields before and after the home
re-judgment; the reading closes all eight as the parent's. The copy was saved with transformers 5.12.1 against the
original's 5.10.0.dev0 and the parent's 5.10.2.

- The copy's `config.json` equals the parent's in every field but `transformers_version`. The eight differences from
  Google are the parent's: `dtype` float16 at the top level and repeated into the text, audio and vision
  sub-configurations, and the four audio and vision values (640, 640, 640, 48) absent, which are the defaults of the
  library's unified Gemma 4 classes under 5.10 and later and load back unchanged (see piece 6).
- The chat template (17,466 bytes) equals Google's at the pinned revision and the parent's byte for byte; the
  generation settings equal both.

## For the recipe library

Consistent with the card, which names the fine-tune and the tool; the `base_model` field names the grandparent, the
second time in the census a field and a card disagree on the parent (the first was the re-upload in round 7). The
comparison separates an ablation from the training under it by the first-value share, the cross-layer agreement of
the leading directions and the remaining fraction, and it cannot read the ablation's weight through the training;
the pair against the parent, yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1 at `237e5d8e`, should be pinned in the
next batch, as the 3MPER0RR pair against its instruct parent was owed from round 7. A dense-change line in the
scorer would name this copy before any projection entry is tried. The saved direction vectors are not committed; the
pull copy is `/opt/ai/hpc-packages/pulls/model-audit/blueback8/measurements/pair-7/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
