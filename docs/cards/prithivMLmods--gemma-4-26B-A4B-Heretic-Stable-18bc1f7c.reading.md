# Reading of the Stage 1 and Stage 2 result: prithivMLmods/gemma-4-26B-A4B-Heretic-Stable against google/gemma-4-26B-A4B-it (2026-11-01)

Measured on Nautilus, round 20 piece 6 (download job 4143641, compare job 4143647, 1,257 seconds, sweep 4143650).
Modified revision `f675892e` (eleven commits from 2026-05-22 22:26Z to 06-01 07:56Z: the weights at 22:54Z on the
first day as "Add files using upload-large-folder tool", the other ten commits README edits), original pinned at
`b2a81a03` (05-18), the revision current when the repository was created. The card names the model it was made
from in its first sentence, huihui-ai/Huihui-gemma-4-26B-A4B-it-abliterated, as a re-upload of that copy in a
new shard layout, and repeats huihui-ai's description of the edit. The `base_model` field names Google.

## Weights (Stage 2)

The tool's assessment was "recipe match", recipe `single-projection-selected`, 0 flags, on the cluster and after
re-scoring at home. The weights are huihui-ai's, re-saved: the copy is five shards under a transformers 5.9.0
version string where huihui-ai's file is two under 5.5.0.dev0, so no shard checksum matches the parent's, and
every measured field of all 1,013 tensors (22,021 fields) equals the round 13 report
(`results/weights/huihui-ai-Huihui-gemma-4-26B-A4B-it-abliterated.json`) and prithivMLmods's own
gemma-4-26B-A4B-it-Uncensored-MAX report of round 14, which is the same file under a third name: 50 changed, the
attention output and the shared dense down projection of layers 5 to 29, one shared direction (group cosine
0.999997 or better, within a layer 0.999995), first share 0.9985 to 0.9997, left kept fraction -1.998 to -2.004 on
all 50 (weight 3.0, huihui-ai's number on this base, finding 21), rows moved 0.08 to 0.61, the 30 packed expert
tensors and the routers unchanged, 963 tensors equal to the original. The layer table and the reading are in
`huihui-ai--Huihui-gemma-4-26B-A4B-it-abliterated-*.reading.md`; this is the fifth repository the census has
measured carrying a huihui-ai file (finding 9).

## Token and configuration side (Stage 1)

"Unexplained differences" on the cluster and at home, one field. The two version strings (5.5.0.dev0 to 5.9.0)
close as a re-save. The template is the earlier-revision case a step further back than the 12B duplicates: the
copy carries Google's 12,045-byte file of 04-02 (`2dfbfc7d`), the one huihui-ai's repository holds from its own
pin of 04-10, under a pin (05-18) whose template is the 17,466-byte revision of 06-03; the tokenizer configuration
grew by 620 bytes between the two Google files. The ninth earlier-revision case in the census; closed by hand. The
fixed conversation renders identically under both.

## For the recipe library

Nothing new on the weights: huihui-ai's 26B-A4B copy loaded and saved again under a new name, which the card says
in its first sentence. The checksum rule of finding 38 cannot see a re-save; a re-save check beside it (every
field equal to a measured report, no checksum shared) would, and so would a pinner that reads the card's first
sentence for a parent name before it reads the `base_model` field.

Weight differences alone cannot certify the absence of hidden behavior.
