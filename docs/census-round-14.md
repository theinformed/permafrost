# Census round 14: four measured pairs, one checkpoint that could not be read, three that wait (2026-10-31)

Eight pairs were pinned as `data/batches/round-14-batch-1.json` and placed on Blueback: push card 5421 (approved
22:40Z on 10-30), round card 5423, download job 3401154 on the transfer queue (finished 2026-10-31 at 00:35Z,
every published checksum verified), compares 3401155 to 3401162 on the background queue, sweep 3401163 behind them.
Four compares measured (pairs 1, 5, 6 and 8). Compare 3401156 (pair 2) stopped reading the copy's weight files with
`duplicate tensor name: audio_projector.embedding_projection.weight`. Compares 3401157, 3401158 and 3401161 (pairs
3, 4 and 7) did not run, because round 12's sweep had deleted the originals they share; those three pairs refile
later. The sweep's condition was never met. The compares ran before the job-report fix of commit f7f4eeb and the
desk cleared them as silent on 10-31. Cards 5532 and 5533 pulled the logs and the measurements home. The four
measurements were re-scored at home with the saved direction vectors and no flag count moved; every metadata
report was judged again under transformers 5.6.2 with the originals' commit histories. Pair 2 was examined at home
from the hub's file headers alone. Each measured pair has a card and a reading note in `docs/cards/`; the
measurements are in `results/weights/` and `results/meta/`, and the direction vectors stay in the pull copy
(`/opt/ai/hpc-packages/pulls/model-audit/blueback14/measurements/pair-N/`).

| Pair | Copy | Original | Weights, as scored | On reading |
| --- | --- | --- | --- | --- |
| 1 | 3MPER0RR/Mistral-7B-v0.3-3MPER0RR-abliterated | mistralai/Mistral-7B-Instruct-v0.3 | violations, 16 flags | consistent against the instruct model: 49 matrices, one shared direction, a per-component kernel of 0.11 to 1.32 on the down projections and 1.10 to 1.35 on the attention outputs, output side; 242 tensors equal the original and the dense change of finding 8 is gone |
| 2 | DarkRomeo88/gemma-4-12b-it-heretic-comfyui | google/gemma-4-12B-it | not measured | four whole single-file quantised checkpoints of llmfan46's 12B copy under one repository, no index, no configuration; the kit's tensor loader took them as shards of one checkpoint |
| 3 | llmfan46/gemma-4-26B-A4B-it-ultra-uncensored-heretic | google/gemma-4-26B-A4B-it | did not run | refiles later |
| 4 | huihui-ai/Huihui-gemma-4-31B-it-abliterated | google/gemma-4-31B-it | did not run | refiles later |
| 5 | timfromhcs/Ministral-3-14B-abliterated | mistralai/Ministral-3-14B-Instruct-2512 | violations, 921 flags | not readable: the original is published in float8 and the copy in bfloat16, so 280 matrices read as rewritten; the pair needs a dequantised original (finding 7) |
| 6 | llmfan46/Mistral-Small-3.2-24B-Instruct-2506-ultra-uncensored-heretic | mistralai/Mistral-Small-3.2-24B-Instruct-2506 | violations, 8 flags (energy shares) | consistent: arbitrary-rank edits on eight attention outputs inside the card's layers 7 to 34, twenty more rewritten under the threshold, input side, searched weights 2.62 to 5.28; the twelfth arbitrary-rank copy |
| 7 | DuoNeural/Gemma-4-26B-A4B-Abliterated | google/gemma-4-26B-A4B-it | did not run | refiles later |
| 8 | TimelessSoul/Huihui-gemma-4-12B-it-abliterated | google/gemma-4-12B-it | match, 0 flags | a byte-identical re-upload of huihui-ai's 12B copy (round 13 pair 4): same shard checksum, every field equal |

Nothing moved outside the matrices the maker's method reaches in pairs 1 and 8 (exactly 0) and in pair 6 the
largest change outside the changed set is 0.000225, an in-range attention output the search weighted near zero.
The round's result is one question answered, one re-upload, one copy that reads as its card says, and two pairs
the pinner should not have admitted. Pair 1 is the comparison finding 8 asked for: against
mistralai/Mistral-7B-Instruct-v0.3 the 226-tensor dense change measured against the pretrained base in round 7 vanishes, 242 tensors
equal the instruct weights exactly, and what remains is the ablation round 7 read through it, with the same
leading directions (cosine median 0.9999 to round 7's on the same matrices) and the kernel now clean: 0.11 at
layer 9 rising to 1.32 at layer 24 and falling to 0.74 at layer 31 on the down projections, 1.10 to 1.35 on the
attention outputs of layers 6 to 30. The copy is an ablation of the instruct model described as an ablation of the
base. Pair 8 is huihui-ai's 12B file under another name, one commit saying "Duplicate from". Pair 6 is the second
arbitrary-rank copy on a Mistral base, with the largest searched weights on that family (layer 15 at 5.28).

Pair 5 measured raw float8 codes against bfloat16 values: the original carries a `quantization_config`, 560
tensors of scales that exist on its side only, and the comparison's 280 "changed" matrices at relative change 0.999
are the quantisation, not an edit. Finding 7 named this original as one that needs dequantising before any copy
can be compared on it. The copy's one commit is a duplicate of jenerallee78/Ministral-3-14B-abliterated of
2025-12-05, and its template is the original's 2025-12 file where the pin of 2026-07-15 carries a later one.

Pair 2 was never a weight comparison. The repository holds a README with two `base_model` entries (Google's model
and llmfan46/gemma-4-12B-it-uncensored-heretic) and four single-file safetensors checkpoints of 12.7, 13.1, 8.3 and
9.7 GB in four quantisations (float8 scaled, int8 with a rotation, w4a8, w6a8), each a whole model for a ComfyUI
text-encoder folder with no index and no configuration. Each file carries `audio_projector.embedding_projection.
weight` as a bfloat16 tensor of shape 3,840 by 640 at a different offset, so the kit's reader, which takes every
`*.safetensors` in a repository as the shards of one checkpoint, met the name four times and stopped at the first
repeat. The two later files' metadata names llmfan46's copy as their source and ComfyUI as their target. The
download verified the published checksums; the files are what the hub serves, and the hub serves four models under
one name.

Fingerprints. Pair 8 against round 13 pair 4: the one modified shard checksum (`2dd13d86`) and every field equal,
the second byte-identical re-upload in the census and the first with the source named in the commit. Pair 1
against round 7's measurement of the same copy against the base: the leading directions equal on 49 matrices and
ten largest-absolute-difference fields equal, every other field different; against richardyoung's and evolveon's
copies of the family, nothing. Pair 6 against huihui-ai's copy on the same weight file (round 13 pair 5), nothing.

## The token side

The cluster's cards read "unexplained differences" on all four measured pairs, and they stay so at home with
three fields closed by tool (pair 1's `head_dim`, pair 6's `rope_parameters` blocks) and the rest closed by hand:

- A 5.16 re-save, pair 1: 775 token fields moved into `tokenizer.json`, the rotary and head-size forms, and the
  instruct model's template in a `chat_template.jinja` of 3,959 bytes, which against this original is a moved file.
  The template that named the parent in round 7 is the parent's.
- The earlier-revision case twice, pair 8: the copy's files are the source's, Google's of 06-03, and the pin from
  the copy's creation date is Google's `707f0a3b` of 07-20, so `max_position_embeddings` reads 262,144 against
  131,072 and the template reads Google's 17,466-byte file of 06-03 against the pin's 18,683-byte "Canonical"
  file of 07-09.
- An original without a library tokenizer, pair 6: the original at `95a6d26c` ships `tekken.json`; the copy ships
  a `tokenizer.json` of 17 MB, a 423-byte tokenizer configuration re-saved under 5.3.0, unsloth's special-tokens map
  byte for byte, unsloth's template of 2025-08-26 after the removal of 299 carriage returns, `unsloth_fixed: true`
  in the configuration and the conversion's seven generation fields (1,025 fields, none a change the original can
  be compared on).
- A float8 original, pair 5: 1,004 special tokens in a 147 KB special-tokens map the copy carries and the original
  does not, `quantization_config` and `tie_word_embeddings` absent from the copy, and a 7,754-byte template that
  is the source repository's and the original's own file of 2025-12 (7,760 bytes, six bytes of line endings
  apart) before the pin's commit of 2026-07-15 replaced it with an 11,913-byte one.

Every fixed conversation renders identically.

## What the scorer learned

The flag counts are the same on the cluster and at home. Pair 5's 921 flags are a quantisation read as an edit:
first shares of 0.001 to 0.2 on 280 matrices at relative change 0.999, the signature the comparison should refuse
before it scores (an original whose configuration carries `quantization_config`, or whose tensor set carries
`weight_scale_inv` names). Pair 1's 16 flags are the floor on the weakest down projections (first share 0.806 at
layer 9, relative change 0.0022) and the within-layer cosines where the two writers' kernels differ. Pair 6's 8
flags are arbitrary rank (first shares 0.941 to 0.979, first eight 0.986 to 0.994). Pair 8 matched with none.

Three things the comparison could say by itself. Before reading a repository as one checkpoint: count the
`*.safetensors` files, require an index when there are several, and report a repeated name as "N whole files under
one repository" with the offsets, which is what the home header read did for pair 2 in a minute. Before scoring:
refuse a float8 original (pair 5). And the per-component kernel, which pair 1 now reads cleanly, as a shape test
(rise and fall over layers) beside the weight band.

## Owed to the metadata tool

The earlier-revision rule where the copy's files come from a source repository older than the copy (pair 8, two
fields); the conversion lookup (pair 6, as in round 13's pair 5); the duplicate-source rule for the batch pinner,
pairing a repository whose one commit says "Duplicate from" with that source before the stated original (pairs 5
and 8); and a refusal of repositories tagged for a single-file loader with no index and two `base_model` entries
(pair 2), or their pairing against the source copy they quantise. To the batch: pairs 3, 4 and 7 of this round,
refiled once their originals are back on the cluster; mistralai/Ministral-3-14B-Instruct-2512 dequantised at home
for pair 5 and for jenerallee78's source; and the two parent pairs finding 9 still waits on (huihui-ai's first 31B
version is pair 4 here).

Weight differences alone cannot certify the absence of hidden behavior.
