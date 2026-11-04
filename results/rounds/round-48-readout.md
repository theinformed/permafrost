# Round 48 read-out

## Pairs

| pair | modified | parent | changed tensors | changed layers | min singular share | mode | placement |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | DavidAU/gemma-3-12b-it-vl-Gemini-3-Pro-Preview-Heretic-Uncensored-Thinking | DreamFast/gemma-3-12b-it-heretic | 336 | 48 | 0.169 | per layer | none (new parent) |
| 2 | DavidAU/Gemma-3-4B-VL-it-Gemini-Pro-Heretic-Uncensored-Thinking | DavidAU/gemma-3-4b-it-heretic-uncensored-abliterated-Extreme | 234 | 34 | 0.279 | per layer | none (new parent) |
| 3 | DavidAU/Gemma-3-27b-it-vl-SuperBrain7x-High-Reasoning-ULTRAMIND-Heretic-Uncensored | coder3101/gemma-3-27b-it-heretic | 434 | 62 | 0.262 | mixed | none median 0.787 |
| 4 | DavidAU/gemma-3-12b-it-vl-HighIQ-Polaris-Heretic-Uncensored-Thinking | DreamFast/gemma-3-12b-it-heretic | 335 | 48 | 0.189 | per layer | none (new parent) |
| 5 | sh0ck0r/heretic-rp-vision-31b | google/gemma-4-31B-it | 410 | 60 | 0.248 | per layer | none median 0.374 |
| 6 | m-polignano/ANITA-NEXT-24B-Dolphin-Mistral-UNCENSORED-ITA | dphn/Dolphin-Mistral-24B-Venice-Edition | 6 | 4 | 0.221 | per layer | none (new parent) |
| 7 | s3nh/Ministral-3-8B-Instruct-2512-BF16-abliterated | mistralai/Ministral-3-8B-Base-2512 | 243 | 34 | 0.002 | per layer | none (new parent) |
| 8 | vulture3/G4-WanaMeroQueen-v3-31B-heretic | vulture3/G4-WanaMeroQueen-v3-31B | 27 | 21 | 0.988 | only copy of its parent | none (new parent) |

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
Pairs here with no census row: 1

## Worth a closer look

- Pair 7 (s3nh) and round 50 pair 6 (nchapman) each read 243 changed tensors over 34 layers against mistralai/Ministral-3-8B-Base-2512. Six tensor kinds print the same direction-agreement figure to every digit in both weight reports: feed_forward_gate 0.15639800731435421, feed_forward_up 0.13417251894640947, attention_key 0.13856202981570553, attention_query 0.13172628008583068, attention_value 0.12861136892372307, other 0.0254952457055848. Only feed_forward_down (0.573 and 0.999) and attention_output (0.260 and 0.997) differ. Both names say Instruct-2512; the pinned parent is Base-2512.
- Felldude/Ministral-3-8B-Uncensored, same parent, also reads 243 tensors over 34 layers, saved as float32.
- Pair 6 (m-polignano) changed 6 tensors over 4 layers, relative difference 0.00103 to 0.00168.
- Pair 5 (sh0ck0r/heretic-rp-vision-31b) places at median 0.374 against Kooten/gemma-4-31b-abliterated-v1.1, with o_share 0.725.
