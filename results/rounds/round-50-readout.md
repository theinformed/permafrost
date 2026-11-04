# Round 50 read-out

## Pairs

| pair | modified | parent | changed tensors | changed layers | min singular share | mode | placement |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | darkc0de/gemma-4-31B-it-Claude-Opus-Distill-v2-heretic | unsloth/gemma-4-31B-it | 251 | 60 | 0.127 | only copy of its parent | none (new parent) |
| 2 | coder3101/gemma-4-19b-a4b-it-REAP-heretic | 0xSero/Gemma-4-19B | 10 | 10 | 0.006 | only copy of its parent | none (new parent) |
| 3 | keithtyser/Gemopus-4-26B-A4B-it-local-abliterated-sota-internal-r7-selected-t34-transfer | Jackrong/Gemopus-4-26B-A4B-it | 35 | 18 | 0.832 | only copy of its parent | none (new parent) |
| 4 | Naphula/Quill-v1-abliterated | sam-paech/Quill-v1 | 84 | 42 | 0.995 | only copy of its parent | none (new parent) |
| 5 | nbeerbower/A0l-12B-heretic | nbeerbower/Schreiber-mistral-nemo-12B | 280 | 40 | 0.087 | only copy of its parent | none (new parent) |
| 6 | nchapman/Ministral-3-8B-Instruct-2512-heretic-BF16 | mistralai/Ministral-3-8B-Base-2512 | 243 | 34 | 0.003 | one direction | none (new parent) |
| 7 | grayarea/Mistral-Small-3.2-24B-Instruct-2506-Heretic-v1.2-2 | unsloth/Mistral-Small-3.2-24B-Instruct-2506 | 55 | 32 | 0.992 | only copy of its parent | none (new parent) |
| 8 | llmfan46/Omega-Darker-Gaslight_The-Final-Forgotten-Fever-Dream-24B-ultra-uncensored-heretic-v1 | ReadyArt/Omega-Darker-Gaslight_The-Final-Forgotten-Fever-Dream-24B | 11 | 11 | 0.913 | arbitrary rank | none (new parent) |

## Census change

Before: per layer 69, one direction 55, arbitrary rank 65, mixed 11, few layers 0, no file 1
After: per layer 76, one direction 56, arbitrary rank 67, mixed 13, few layers 0, no file 2
Mode changes:
none
New copies:
- DavidAU/Gemma-3-4B-VL-it-Gemini-Pro-Heretic-Uncensored-Thinking (DavidAU/gemma-3-4b-it-heretic-uncensored-abliterated-Extreme): per layer
- DavidAU/gemma-3-4b-it-vl-Heretic-4-Horsemen-Uncensored (DavidAU/gemma-3-4b-it-heretic-uncensored-abliterated-Extreme): per layer
- DavidAU/gemma-3-12b-it-vl-Gemini-3-Pro-Preview-Heretic-Uncensored-Thinking (DreamFast/gemma-3-12b-it-heretic): per layer
- DavidAU/gemma-3-12b-it-vl-HighIQ-Polaris-Heretic-Uncensored-Thinking (DreamFast/gemma-3-12b-it-heretic): per layer
- llmfan46/Omega-Darker-Gaslight_The-Final-Forgotten-Fever-Dream-24B-ultra-uncensored-heretic-v1 (ReadyArt/Omega-Darker-Gaslight_The-Final-Forgotten-Fever-Dream-24B): arbitrary rank
- llmfan46/Omega-Darker-Gaslight_The-Final-Forgotten-Fever-Dream-24B-ultra-uncensored-heretic-v2 (ReadyArt/Omega-Darker-Gaslight_The-Final-Forgotten-Fever-Dream-24B): arbitrary rank
- DavidAU/Gemma-3-27b-it-vl-SuperBrain7x-High-Reasoning-ULTRAMIND-Heretic-Uncensored (coder3101/gemma-3-27b-it-heretic): mixed
- AskVenice/venice-uncensored (dphn/Dolphin-Mistral-24B-Venice-Edition): no file
- m-polignano/ANITA-NEXT-24B-Dolphin-Mistral-UNCENSORED-ITA (dphn/Dolphin-Mistral-24B-Venice-Edition): per layer
- sh0ck0r/heretic-rp-vision-31b (google/gemma-4-31B-it): per layer
- Felldude/Ministral-3-8B-Uncensored (mistralai/Ministral-3-8B-Base-2512): mixed
- nchapman/Ministral-3-8B-Instruct-2512-heretic-BF16 (mistralai/Ministral-3-8B-Base-2512): one direction
- s3nh/Ministral-3-8B-Instruct-2512-BF16-abliterated (mistralai/Ministral-3-8B-Base-2512): per layer
Pairs here with no census row: 6

## Worth a closer look

- Pair 6 (nchapman) shares six tensor kinds to every digit with round 48 pair 7 (s3nh) against mistralai/Ministral-3-8B-Base-2512; see the round 48 read-out. Its mode row reads one direction with pair 0.996 and o_share 0.058.
- Pair 2 (coder3101, parent 0xSero/Gemma-4-19B) changed 10 tensors over 10 layers with min singular share 0.006.
- Pair 4 (Naphula/Quill-v1-abliterated) changed 84 tensors over 42 layers with min singular share 0.995; pair 7 (grayarea) changed 55 over 32 with 0.992.
