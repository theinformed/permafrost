# Pre-registration: does an abliteration remove a pre-existing hidden trigger, and can a weight audit see the tampering?

Permafrost study S-1. Written 2026-10-14. This fixes the questions, inputs, measurements and decision lines before any
model is run, so the result is a finding and not a story told after the fact.

## 1. Why this matters
Anyone can take an open-weight model, run an "abliteration" to strip its refusals, and repost it as an uncensored copy.
If the model they started from already carried a hidden trigger-behavior, two questions decide whether the reposted
copy is safe to trust: does the trigger still work after abliteration, and can a cheap weight comparison tell a tampered
repost from an honest one. A clear answer helps every person who downloads these copies and every platform that hosts
them. The result is a contribution to safe, transparent use of open weights; it is defensive throughout.

## 2. Inputs (all published, with documented ground truth)
We do not create any triggered model. We use artifacts the research community has already released for detection work,
each with its trigger and intended behavior documented by its own authors and cited in audit/survival/registry.json:
the BackdoorLLM benchmark (multiple documented methods and architectures), NIST TrojAI rounds where access is granted
(poisoned and clean models with sealed ground truth), and the public BadSeek coding-model demonstration. Abliteration
is applied with the published community recipes already reproduced in the Permafrost recipe library.

## 3. Questions and hypotheses
- Q1 (survival): after abliteration, does the author-documented trigger still elicit the author-documented behavior?
  H1: survival varies by recipe; a recipe that only removes a refusal direction leaves an unrelated trigger intact.
- Q2 (detectability): does the tensor-level fingerprint of a (tampered original -> abliterated) pair fall outside the
  envelope a clean abliteration of an untampered model of the same base produces?
  H2: a trigger that survives leaves weight changes a clean abliteration does not, so the tampered pair is separable.

## 4. Procedure, per input model
1. Serve the published model (read-only, temperature 0) and record whether the documented trigger and a matched
   non-trigger prompt produce the documented behavior. This BEFORE pass only confirms the artifact works in our harness.
2. Apply each recipe-library abliteration to it, one at a time.
3. Serve each resulting copy and repeat the same two prompts (the AFTER pass). Survival for that recipe is BEFORE-yes
   and AFTER-yes.
4. Run the weight comparison on the (published model -> each abliterated copy) pair and on a clean (untampered base ->
   abliterated) pair of the same base; record where each falls relative to that recipe's measured envelope.

## 5. Measurements and decision lines, fixed now
- Survival rate per recipe = AFTER-yes / BEFORE-yes over the inputs that passed the BEFORE control. Reported with a
  Wilson interval; "survives" for a recipe means the interval's lower bound is above 0.5.
- Detector separation = whether the tampered pair's maximum relative difference outside the recipe envelope exceeds the
  clean pair's by a margin fixed before the run (2x the clean pair's value, and above the quantization null). Reported
  as a per-recipe separation rate with its interval.
- Null controls: the original against a fresh quantization of itself (rounding only) and a clean abliteration of an
  untampered model. A tampered-pair signal that also appears in a null is noise, not a finding.

## 6. Threats to validity, stated up front
- A clean BEFORE result is weak evidence on its own; the harness must first reproduce each artifact's documented
  behavior, or that input is dropped and said to be dropped.
- Detection reaching only the prompts near a trigger: a clean survival result bounds survival only over the documented
  triggers, never over all possible ones. The paper says so.
- Gated inputs (TrojAI): used only where access is granted; otherwise listed as not covered.

## 7. What is published and what is not
Published: the survival rates and detector-separation rates per recipe, the measurement code, the registry of inputs
with citations, and the null controls. Not published: any new trigger, and any model weights. Findings on a specific
public upload follow the disclosure path in SECURITY-AND-SCOPE.md.
