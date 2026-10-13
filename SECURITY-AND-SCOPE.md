# Permafrost: scope, safety posture, and disclosure

Permafrost is a transparency audit. It asks whether a publicly posted, community-modified open-weight model differs
from the original it names only in the way its own card claims. The goal is to help people who download these models,
and the people who host them, see what actually changed.

## What the project works on
- Only models that are already public, and their stated public originals. Nothing private, nothing a person did not publish.
- The measurements are: a tensor-by-tensor comparison of the weights; a comparison of the chat template, tokenizer and
  special tokens; and a read of how the two models answer ordinary, harmless prompts.

## What the project does not do
- It does not create a harmful or deceptive model, and it distributes no model weights.
- Where it needs a "clean" reference to compare against, it reproduces openly published modification methods on an open
  base, only to calibrate what an honest change looks like.
- Where it needs to test whether the audit can catch a tampered upload, it uses existing, peer-reviewed, published
  ground-truth datasets as inputs. It manufactures no new tampering.
- It publishes methods and measurements, not working recipes for abuse. Released: the measurement code, the per-model
  cards, the minimal-pair prompt sets. Not released: anything whose only use is to plant hidden behavior.

## How findings are handled
- A difference a model's card does not explain is reported as "unexplained," never "malicious," unless there is strong,
  reproduced evidence.
- A finding on a real model goes privately to the hosting platform's security contact and to the model's creator first,
  with the evidence and a window to respond, before any public card names it.
- Every card names both models by their exact revision, so the finding stays checkable after a creator updates.

## Good faith
This is defensive security research. It follows the norms of the published work it builds on (the refusal-direction
literature, NIST TrojAI, BackdoorLLM) and the disclosure practice those authors set. Questions about scope or a specific
card are welcome through the repository's issues.
