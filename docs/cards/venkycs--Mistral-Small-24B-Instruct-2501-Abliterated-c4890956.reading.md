# Reading of the Stage 1 and Stage 2 result: venkycs/Mistral-Small-24B-Instruct-2501-Abliterated against mistralai/Mistral-Small-24B-Instruct-2501 (2026-10-31)

Measured on Nautilus, round 16 piece 7 (push card 5433, round card 5434, download job 4120061, compare job 4120068 on
the background queue, sweep 4120069; pulled home by card 5467). Modified revision `dfaba929` (2025-03-12, "Upload
tokenizer_config.json"; the repository was created on 2025-01-30 at 16:32Z, the weights uploaded on 2025-02-25 and
the tokenizer files on 03-11 and 03-12), original pinned at `21b49d4b` (2025-01-30 at 16:30Z, two minutes before the
copy's repository was created; Mistral's repository has 54 commits, 38 of them that day). The maker's card is
huihui-ai's card for huihui-ai/Mistral-Small-24B-Instruct-2501-abliterated, copied with its title, its method line
(the remove-refusals script) and its ollama pull command; the `library_name` is vllm.

## Weights (Stage 2)

The tool's assessment was "recipe violations", nearest recipe `single-projection-selected`, 56 flags, on the cluster
and after re-scoring at home. All 56 flags are first energy shares at the storage floor. On reading, the copy is a
plain shared-direction projection at weight 1.0 on every layer but the first.

- 78 of 363 tensors changed: the attention output and the down projection of layers 1 to 39. Layer 0's two read
  exactly 0, and the largest relative change outside the changed set is exactly 0.
- One shared direction (cross-layer cosine 0.99999 or more on all 78, within-layer 1.000), rank one at the floor
  (first share 0.986 to 0.994, the first singular value 55 to 88 times the second, leftover 0.0015 to 0.0016 of
  the norm on changes of 0.013 to 0.019; the 56 flags are the 56 matrices whose first share sits under the
  envelope's line, the storage floor of finding 3).
- Weight 1.0, output side: along the leading direction the copy keeps −0.004 to −0.002 of the original's action on
  the left of all 78 and 0.25 to 0.89 on the right. Row norms moved by 0.003 to 0.023.

| Layer | Relative change | E1 | E8 | Left, direction 1 | Right, direction 1 | Row norms | Cross-layer cosine | Within-layer cosine |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.014 | 0.988 | 0.989 | -0.00 | 0.78 | 0.0045 | 1.00 | 1.000 |
| 2 | 0.014 | 0.989 | 0.989 | -0.00 | 0.80 | 0.0075 | 1.00 | 1.000 |
| 3 | 0.015 | 0.989 | 0.990 | -0.00 | 0.82 | 0.0091 | 1.00 | 1.000 |
| 4 | 0.014 | 0.988 | 0.989 | -0.00 | 0.79 | 0.0105 | 1.00 | 1.000 |
| 5 | 0.015 | 0.989 | 0.990 | -0.00 | 0.71 | 0.0127 | 1.00 | 1.000 |
| 6 | 0.015 | 0.990 | 0.991 | -0.00 | 0.80 | 0.0076 | 1.00 | 1.000 |
| 7 | 0.014 | 0.989 | 0.989 | -0.00 | 0.75 | 0.0092 | 1.00 | 1.000 |
| 8 | 0.015 | 0.989 | 0.990 | -0.00 | 0.75 | 0.0066 | 1.00 | 1.000 |
| 9 | 0.015 | 0.990 | 0.991 | -0.00 | 0.77 | 0.0109 | 1.00 | 1.000 |
| 10 | 0.015 | 0.989 | 0.990 | -0.00 | 0.76 | 0.0112 | 1.00 | 1.000 |
| 11 | 0.016 | 0.990 | 0.991 | -0.00 | 0.74 | 0.0083 | 1.00 | 1.000 |
| 12 | 0.015 | 0.990 | 0.991 | -0.00 | 0.78 | 0.0085 | 1.00 | 1.000 |
| 13 | 0.016 | 0.991 | 0.992 | -0.00 | 0.76 | 0.0135 | 1.00 | 1.000 |
| 14 | 0.017 | 0.991 | 0.992 | -0.00 | 0.81 | 0.0161 | 1.00 | 1.000 |
| 15 | 0.018 | 0.992 | 0.993 | -0.00 | 0.76 | 0.0172 | 1.00 | 1.000 |
| 16 | 0.018 | 0.992 | 0.993 | -0.00 | 0.73 | 0.0134 | 1.00 | 1.000 |
| 17 | 0.019 | 0.994 | 0.994 | -0.00 | 0.69 | 0.0234 | 1.00 | 1.000 |
| 18 | 0.017 | 0.992 | 0.992 | -0.00 | 0.79 | 0.0198 | 1.00 | 1.000 |
| 19 | 0.016 | 0.991 | 0.992 | -0.00 | 0.74 | 0.0202 | 1.00 | 1.000 |
| 20 | 0.017 | 0.992 | 0.992 | -0.00 | 0.73 | 0.0209 | 1.00 | 1.000 |
| 21 | 0.017 | 0.992 | 0.992 | -0.00 | 0.73 | 0.0177 | 1.00 | 1.000 |
| 22 | 0.013 | 0.986 | 0.987 | -0.00 | 0.80 | 0.0077 | 1.00 | 1.000 |
| 23 | 0.016 | 0.990 | 0.991 | -0.00 | 0.76 | 0.0162 | 1.00 | 1.000 |
| 24 | 0.015 | 0.990 | 0.991 | -0.00 | 0.78 | 0.0120 | 1.00 | 1.000 |
| 25 | 0.015 | 0.990 | 0.991 | -0.00 | 0.71 | 0.0107 | 1.00 | 1.000 |
| 26 | 0.015 | 0.990 | 0.990 | -0.00 | 0.68 | 0.0134 | 1.00 | 1.000 |
| 27 | 0.016 | 0.991 | 0.991 | -0.00 | 0.74 | 0.0110 | 1.00 | 1.000 |
| 28 | 0.014 | 0.988 | 0.989 | -0.00 | 0.80 | 0.0127 | 1.00 | 1.000 |
| 29 | 0.015 | 0.990 | 0.990 | -0.00 | 0.71 | 0.0101 | 1.00 | 1.000 |
| 30 | 0.014 | 0.987 | 0.988 | -0.00 | 0.74 | 0.0056 | 1.00 | 1.000 |
| 31 | 0.014 | 0.987 | 0.988 | -0.00 | 0.70 | 0.0056 | 1.00 | 1.000 |
| 32 | 0.014 | 0.987 | 0.988 | -0.00 | 0.67 | 0.0042 | 1.00 | 1.000 |
| 33 | 0.013 | 0.987 | 0.988 | -0.00 | 0.71 | 0.0062 | 1.00 | 1.000 |
| 34 | 0.014 | 0.988 | 0.988 | -0.00 | 0.71 | 0.0051 | 1.00 | 1.000 |
| 35 | 0.013 | 0.987 | 0.988 | -0.00 | 0.77 | 0.0047 | 1.00 | 1.000 |
| 36 | 0.014 | 0.988 | 0.989 | -0.00 | 0.87 | 0.0116 | 1.00 | 1.000 |
| 37 | 0.014 | 0.988 | 0.988 | -0.00 | 0.86 | 0.0054 | 1.00 | 1.000 |
| 38 | 0.014 | 0.987 | 0.988 | -0.00 | 0.89 | 0.0063 | 1.00 | 1.000 |
| 39 | 0.014 | 0.988 | 0.989 | -0.00 | 0.84 | 0.0073 | 1.00 | 1.000 |

The down projections:

| Layer | Relative change | E1 | E8 | Left, direction 1 | Right, direction 1 | Row norms | Cross-layer cosine | Within-layer cosine |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.014 | 0.988 | 0.989 | -0.00 | 0.38 | 0.0044 | 1.00 | 1.000 |
| 2 | 0.014 | 0.988 | 0.989 | -0.00 | 0.43 | 0.0043 | 1.00 | 1.000 |
| 3 | 0.014 | 0.988 | 0.988 | -0.00 | 0.33 | 0.0040 | 1.00 | 1.000 |
| 4 | 0.014 | 0.988 | 0.989 | -0.00 | 0.32 | 0.0058 | 1.00 | 1.000 |
| 5 | 0.014 | 0.988 | 0.989 | -0.00 | 0.40 | 0.0049 | 1.00 | 1.000 |
| 6 | 0.014 | 0.988 | 0.989 | -0.00 | 0.51 | 0.0062 | 1.00 | 1.000 |
| 7 | 0.014 | 0.988 | 0.989 | -0.00 | 0.37 | 0.0064 | 1.00 | 1.000 |
| 8 | 0.014 | 0.989 | 0.989 | -0.00 | 0.36 | 0.0066 | 1.00 | 1.000 |
| 9 | 0.014 | 0.989 | 0.989 | -0.00 | 0.36 | 0.0036 | 1.00 | 1.000 |
| 10 | 0.015 | 0.989 | 0.990 | -0.00 | 0.40 | 0.0027 | 1.00 | 1.000 |
| 11 | 0.015 | 0.990 | 0.990 | -0.00 | 0.48 | 0.0049 | 1.00 | 1.000 |
| 12 | 0.015 | 0.990 | 0.991 | -0.00 | 0.50 | 0.0059 | 1.00 | 1.000 |
| 13 | 0.016 | 0.990 | 0.991 | -0.00 | 0.56 | 0.0071 | 1.00 | 1.000 |
| 14 | 0.016 | 0.991 | 0.991 | -0.00 | 0.56 | 0.0120 | 1.00 | 1.000 |
| 15 | 0.017 | 0.992 | 0.992 | -0.00 | 0.59 | 0.0128 | 1.00 | 1.000 |
| 16 | 0.016 | 0.991 | 0.992 | -0.00 | 0.61 | 0.0118 | 1.00 | 1.000 |
| 17 | 0.018 | 0.993 | 0.993 | -0.00 | 0.75 | 0.0088 | 1.00 | 1.000 |
| 18 | 0.017 | 0.992 | 0.992 | -0.00 | 0.57 | 0.0140 | 1.00 | 1.000 |
| 19 | 0.016 | 0.991 | 0.991 | -0.00 | 0.62 | 0.0168 | 1.00 | 1.000 |
| 20 | 0.015 | 0.990 | 0.991 | -0.00 | 0.40 | 0.0086 | 1.00 | 1.000 |
| 21 | 0.015 | 0.989 | 0.990 | -0.00 | 0.44 | 0.0092 | 1.00 | 1.000 |
| 22 | 0.014 | 0.989 | 0.989 | -0.00 | 0.39 | 0.0089 | 1.00 | 1.000 |
| 23 | 0.014 | 0.988 | 0.989 | -0.00 | 0.31 | 0.0058 | 1.00 | 1.000 |
| 24 | 0.014 | 0.988 | 0.989 | -0.00 | 0.35 | 0.0057 | 1.00 | 1.000 |
| 25 | 0.014 | 0.988 | 0.989 | -0.00 | 0.25 | 0.0034 | 1.00 | 1.000 |
| 26 | 0.014 | 0.988 | 0.989 | -0.00 | 0.26 | 0.0038 | 1.00 | 1.000 |
| 27 | 0.014 | 0.988 | 0.989 | -0.00 | 0.26 | 0.0038 | 1.00 | 1.000 |
| 28 | 0.014 | 0.988 | 0.989 | -0.00 | 0.29 | 0.0039 | 1.00 | 1.000 |
| 29 | 0.014 | 0.988 | 0.988 | -0.00 | 0.33 | 0.0038 | 1.00 | 1.000 |
| 30 | 0.014 | 0.988 | 0.988 | -0.00 | 0.36 | 0.0057 | 1.00 | 1.000 |
| 31 | 0.014 | 0.987 | 0.988 | -0.00 | 0.40 | 0.0035 | 1.00 | 1.000 |
| 32 | 0.014 | 0.988 | 0.988 | -0.00 | 0.47 | 0.0053 | 1.00 | 1.000 |
| 33 | 0.014 | 0.988 | 0.988 | -0.00 | 0.47 | 0.0054 | 1.00 | 1.000 |
| 34 | 0.014 | 0.988 | 0.988 | -0.00 | 0.42 | 0.0044 | 1.00 | 1.000 |
| 35 | 0.014 | 0.988 | 0.989 | -0.00 | 0.64 | 0.0093 | 1.00 | 1.000 |
| 36 | 0.014 | 0.988 | 0.989 | -0.00 | 0.53 | 0.0067 | 1.00 | 1.000 |
| 37 | 0.014 | 0.988 | 0.989 | -0.00 | 0.51 | 0.0061 | 1.00 | 1.000 |
| 38 | 0.014 | 0.987 | 0.988 | -0.00 | 0.67 | 0.0049 | 1.00 | 1.000 |
| 39 | 0.014 | 0.989 | 0.989 | -0.00 | 0.69 | 0.0058 | 1.00 | 1.000 |

The card is huihui-ai's and the footprint is the shape huihui-ai's script leaves (every attention output and down
projection, one direction, weight 1.0, no norm restoration, as on that maker's Qwen3-4B copy of round 1). huihui-ai's own copy of this base is not measured, so whether the two are one file cannot be said from the
weights yet; the fingerprint test needs that pair.

## Token and configuration side (Stage 1)

The cluster's card read "unexplained differences" in seven fields and the home judgement keeps them (the
later-revision rule does not run when the fixed conversation renders differently), so the committed card reads
"unexplained differences"; the reading sorts them into five later-revision effects and one real change.

- `special_tokens.special_tokens_map.json:bos_token`, `eos_token`, `unk_token` written as objects and
  `additional_special_tokens` written as strings (the pin has the reverse), and `generation.do_sample` true added:
  Mistral's commit `e969dcf1` of 2025-01-30 at 17:11Z, 41 minutes after the pin, wrote exactly these forms and
  values into both files, and every later revision carries them. The maker downloaded after that commit (the weights
  went up on 02-25). Later-revision effects, which the rule would have closed had the template allowed it to run.
- `template.default` and `rendered_template.default`: the copy's template (3,959 bytes, in `tokenizer_config.json`)
  matches none of the 2501 repository's 54 revisions (423 bytes at creation, 415 from 12:36Z, 1,597 from 17:11Z on).
  It equals mistralai/Mistral-Small-Instruct-2409's template byte for byte, the previous model's: the old
  `[INST] ... [/INST]` form with spaces, the system message folded into the last user turn, and the tool blocks.
  The fixed conversation renders differently: the copy writes `<s>[INST] What is two plus two?[/INST] Four.</s>[INST]
  You are a careful assistant.` followed by two newlines and `Write that as a word.[/INST]`, where the pinned
  original writes `<s>[SYSTEM_PROMPT]You are a careful assistant.[/SYSTEM_PROMPT][INST]What is two plus
  two?[/INST]Four.</s>[INST]Write that as a word.[/INST]`. The 2501 model was trained with the system-prompt block
  and without the spaces; a conversation through this copy is formatted as the 2409 model's. A real change, from the
  maker's tokenizer upload of 2025-03-12.

## For the recipe library

Consistent with the card's method on the weight side (the `single-projection` entry at weight 1.0, layers 1 to 39,
the 56 floor flags being the envelope's line and not the edit). Not consistent on the token side: the template is
the previous model's and changes every rendered conversation. The saved direction vectors are not committed; the
pull copy is `/opt/ai/hpc-packages/pulls/model-audit/nautilus16/measurements/pair-7/weights.directions.safetensors`.

Weight differences alone cannot certify the absence of hidden behavior.
