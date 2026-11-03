# Reading of the Stage 1 and Stage 2 result: DavidAU/Gemma-3-27b-it-Gemini-Heretic-Uncensored-Deeper-Reasoning-Series2 against coder3101/gemma-3-27b-it-heretic (2026-11-03)

Measured on Wheat, round 49 piece 7 (download job 387515, compare job 387522, sweep 387524; the pull carries the
measurements and the sweep record and no job log). Modified revision `d3a1a45e` (created 2026-01-26 02:07Z, the
weights uploaded at 03:24Z and unchanged since, the two templates replaced on 02-16 and 02-21 and the card edited
to 02-21), parent pinned at `b9449797` of 2025-11-28, coder3101's Heretic 1.0.1 edit of google/gemma-3-27b-it. The
census has measured that edit only as a parent, in round 42 under Justbackup's hub duplicate of the maker's first
pass (finding 121), and not against Google, so the batch note's "measured" means measured as a parent. The card:
"a fully uncensored, full deep thinking Gemma 27B fine tune via Unsloth", trained on TeichAI's
gemini-3-pro-preview-high-reasoning-1000x ("Larger dataset than series 1 (250 vs 1000)"), printing coder3101's
refusal table (a KL divergence of 0.07, 9 refusals in 100 against 98) and two benchmark rows. The maker's first pass,
DavidAU/Gemma-3-27b-it-Uncensored-HERETIC-Gemini-Deep-Reasoning (created a day earlier on the 250-row set), is the
file Justbackup's copy carries; its weight files are not this copy's. The parent counts as neither an original nor a
copy (finding 117).

## Weights (Stage 2)

The tool's assessment was violations against `single-projection`, 557 flags (308 unexpected changes, 124 first
shares, 124 direction cosines, 1 cross-kind cosine), on the cluster and after re-scoring at home. On reading, the copy
is training on every linear map of every layer and no direction, and the maker's first pass is inside it.

- 432 of 1,247 tensors changed: the query, attention output, gate, up and down projections of all 62 layers and the
  key and value projections of 61; layer 1's key and value moved by 0.00082 and 0.00085, the largest relative change
  outside the changed set. The 437 vision tensors, the embedding and every normalisation vector read exactly 0.
- No direction: first shares 0.28 to 0.985, the right kept fraction 0.86 to 1.06 and the left 0.68 to 1.31 (the
  extremes on the gate projections).
- Relative changes 0.0011 to 0.0698 (median 0.0064), with layer 0's down projection at 0.0399 and layer 4's query
  projection at 0.0698. Rows moved 0.00008 to 1.277: by byte range, 40 rows of the layer 4 query projection, in heads
  19, 20 and 28, moved by more than 0.01, and six rows of head 28 grew by 0.59 to 1.28, three of them to more than
  twice their norm, where the maker's first pass moved the same rows by 0.0003. The layer 0 down projection's rows
  moved by up to 0.237.

| Kind | Matrices | This copy's change | First pass's change | Directions to the first pass (left, median) |
| --- | --- | --- | --- | --- |
| Query projection | 62 | 0.0021 to 0.0698 | 0.0013 to 0.0058 | 0.472 |
| Key projection | 61 | 0.0014 to 0.0065 | 0.0010 to 0.0027 | 0.480 (48 shared) |
| Value projection | 61 | 0.0011 to 0.0066 | 0.0010 to 0.0037 | 0.679 (60 shared) |
| Attention output | 62 | 0.0044 to 0.0123 | 0.0023 to 0.0084 | 0.591 |
| Gate projection | 62 | 0.0035 to 0.0154 | 0.0017 to 0.0045 | 0.404 |
| Up projection | 62 | 0.0032 to 0.0125 | 0.0018 to 0.0049 | 0.454 |
| Down projection | 62 | 0.0039 to 0.0399 | 0.0027 to 0.0407 | 0.664 |

Two trainings on one base. Both copies are measured against coder3101's edit at the same revision, so their
reports and saved vectors compare directly. On the 418 names both changed the leading vectors stand at 0.491 on the
left and 0.779 on the right at the median, and both against mlabonne's 27B projection at 0.083 or less. By byte range
on the layer 30 attention output, down projection and query projection, this copy stands 0.0082, 0.0110 and 0.0065
from coder3101's, the first pass 0.0044, 0.0066 and 0.0029, and the two 0.0071, 0.0097 and 0.0061 from each other.
This copy's change carries the first pass's change at a coefficient of 0.962, 0.828 and 0.821, and what it adds
beyond the first pass stands at -0.024, -0.117 and -0.084 to it, 1.61, 1.48 and 2.12 times its size: the second
copy is the first copy's training, nearly whole, plus a second training at about right angles to it. The weights
cannot say whether that is a second pass laid over the first copy's weights or one longer run from the edit on a
dataset that begins with the first one's; either way the two trainings agree where they overlap and the second is
the larger.

The edit under it. coder3101's edit stands 0.0218 and 0.0199 from Google's on the layer 30 attention output and down
projection (first shares 0.995 and 0.994) and leaves the query projection Google's bytes. This copy's change moves
along the edit by -0.00073 and -0.0075 of it (the first pass by -0.00002 and -0.0008), so the training takes back
less than one percent of the edit on the matrices read, and the copy stands 0.0233 and 0.0226 from Google's.

## Token and configuration side (Stage 1)

"Consistent with re-save noted" on the cluster and at home: the version strings move from 4.57.3 to 4.57.6. The
template (1,532 bytes), `tokenizer.json`, `tokenizer.model` and the preprocessor file are the parent's by object id;
the copy adds a 2,409-byte `chat_template_thinking.jinja` and a processor file, and its other token files are
rewritten in forms the tool reads as equal. The token ids are the Gemma 3 instruct checkpoint's through the parent
(`eos_token_id` `[1, 106]` in the configuration and the generation file, `bos_token_id` 2, `pad_token_id` 0) and the
vocabulary is 262,208.

## For the recipe library

No entry reads training; a training entry would read the copy as its card says. A line that compares a training
pair's change with a sibling training's on the same parent would read "contains the first pass" from the reports.
The pinner should queue coder3101's 27B edit against Google so that the edit under both of the maker's passes is
read. The direction vectors stay in the pull copy at
`/opt/ai/hpc-packages/pulls/model-audit/wheat49/measurements/pair-7/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
