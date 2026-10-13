# training.py -- Merge a small instruction or preference adapter into a copy.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  add a benign control and a short preference repair pass.
"""One-epoch adapters with saved training examples and merged weights."""

import json
from pathlib import Path

import torch

from audit.nulls import prompts
from audit.weights import digest
from .common import finish, instruction_ids, load_runtime, log, prepare, release, response, save_merged
from .projection import build_projection


def read_examples(path, preference):
    """Require real responses; an instruction alone is not a training target."""
    fields = ("prompt", "chosen", "rejected") if preference else ("prompt", "response")
    rows = [json.loads(line) for line in Path(path).read_text().splitlines() if line.strip()]
    if not rows:
        raise ValueError("training data is empty")
    for row in rows:
        if any(not isinstance(row.get(key), str) or not row[key].strip() for key in fields):
            raise ValueError("training examples need nonempty " + "/".join(fields))
        if preference and row["chosen"] == row["rejected"]:
            raise ValueError("chosen and rejected responses are identical")
    return rows


def make_examples(base, projected, args, resources):
    """Distill benign base answers; preference pairs compare base and projected replies."""
    harmless = prompts(args.prompts)["harmless"][:args.train_prompts]
    variations = ("", " Please be brief.", " Give a practical example.", " Use plain language.",
                  " Write two sentences.", " Explain it to a beginner.", " Focus on the main point.",
                  " Answer in a short paragraph.", " Give one useful detail.", " Use a friendly tone.",
                  " Give a direct answer.", " Start with the useful part.", " Keep the advice simple.",
                  " Explain why it helps.", " Use everyday words.", " Include one short example.",
                  " Avoid technical jargon.", " Give a concrete suggestion.", " Make the answer easy to follow.",
                  " Use a calm tone.", " Suggest a first step.", " Write a brief explanation.",
                  " Answer in three sentences.", " Keep the focus on the question.")
    count = args.pairs * (2 if projected is not None else 1)
    if count > len(harmless) * len(variations):
        raise ValueError("requested pairs exceed the available prompt variations")
    instructions = [item + suffix for suffix in variations for item in harmless][:count]
    runtime, tokenizer = load_runtime(base, resources)
    chosen = []
    try:
        for index, item in enumerate(instructions):
            log(f"Collect benign target {index + 1}/{len(instructions)}")
            chosen.append(response(runtime, tokenizer, item, args, resources))
    finally:
        del runtime
        release(None)
    if projected is None:
        return [{"prompt": item, "response": answer} for item, answer in zip(instructions, chosen) if answer]
    runtime, tokenizer = load_runtime(projected, resources)
    rows = []
    try:
        for index, (item, answer) in enumerate(zip(instructions, chosen)):
            log(f"Collect projected reply {index + 1}/{len(instructions)}")
            rejected = response(runtime, tokenizer, item, args, resources)
            if answer and rejected and answer != rejected:
                rows.append({"prompt": item, "chosen": answer, "rejected": rejected})
    finally:
        del runtime
        release(None)
    return rows


def supervised(runtime, tokenizer, rows, args, resources):
    """Train answer tokens only; padding and the user question carry no loss."""
    from peft import LoraConfig, get_peft_model

    runtime = get_peft_model(runtime, LoraConfig(r=args.rank, lora_alpha=args.rank * 2,
                              target_modules=["q_proj", "v_proj"], lora_dropout=0,
                              bias="none", task_type="CAUSAL_LM"))
    runtime.train()
    runtime.config.use_cache = False
    optimizer = torch.optim.AdamW((p for p in runtime.parameters() if p.requires_grad), lr=args.learning_rate)
    for index, row in enumerate(rows):
        resources.check()
        prompt = instruction_ids(tokenizer, row["prompt"], resources.device, args.max_length)["input_ids"]
        answer = tokenizer(row["response"], add_special_tokens=False)["input_ids"] + [tokenizer.eos_token_id]
        answer = answer[:args.max_length - prompt.shape[1]]
        if not answer:
            raise ValueError("no room for answer tokens")
        ids = torch.cat((prompt, torch.tensor([answer], device=resources.device)), dim=1)
        labels = ids.clone()
        labels[:, :prompt.shape[1]] = -100
        optimizer.zero_grad(set_to_none=True)
        loss = runtime(input_ids=ids, attention_mask=torch.ones_like(ids), labels=labels).loss
        if not torch.isfinite(loss):
            raise ValueError("training loss is nonfinite")
        loss.backward()
        torch.nn.utils.clip_grad_norm_((p for p in runtime.parameters() if p.requires_grad), 1)
        optimizer.step()
        log(f"Instruction step {index + 1}/{len(rows)}; loss {float(loss.detach()):.4f}")
    del optimizer
    return runtime


def preference(runtime, tokenizer, rows, args, resources, out):
    """Use the unmodified adapter base as the reference, avoiding a second checkpoint."""
    from datasets import Dataset
    from peft import LoraConfig
    from transformers import TrainerCallback
    from trl import DPOConfig, DPOTrainer

    class Progress(TrainerCallback):
        """Check memory at each training step and keep the log readable."""

        def on_step_begin(self, args, state, control, **kwargs):
            resources.check()
            log(f"Preference step {state.global_step + 1}")

    training_rows = [{"prompt": [{"role": "user", "content": row["prompt"]}],
                      "chosen": [{"role": "assistant", "content": row["chosen"]}],
                      "rejected": [{"role": "assistant", "content": row["rejected"]}]} for row in rows]
    config = DPOConfig(output_dir=str(out / "training"), num_train_epochs=1,
                       per_device_train_batch_size=1, gradient_accumulation_steps=1,
                       learning_rate=args.learning_rate, max_length=args.max_length,
                       beta=0.1, bf16=resources.device.type == "cuda", use_cpu=resources.device.type == "cpu",
                       save_strategy="no", report_to="none", logging_steps=1, disable_tqdm=True,
                       dataloader_num_workers=0, seed=args.seed, gradient_checkpointing=True)
    trainer = DPOTrainer(runtime, ref_model=None, args=config, processing_class=tokenizer,
                         train_dataset=Dataset.from_list(training_rows), callbacks=[Progress()],
                         peft_config=LoraConfig(r=args.rank, lora_alpha=args.rank * 2,
                         target_modules=["q_proj", "v_proj"], lora_dropout=0, bias="none", task_type="CAUSAL_LM"))
    trainer.train()
    return trainer.model


def run(args, resources, method):
    """Build the chosen control and merge its one-epoch adapter before completion."""
    torch.manual_seed(args.seed)
    directory, out, card = prepare(args, method)
    healing = method == "projection-plus-healing"
    projected = None
    if healing:
        projected = out / "projection-work"
        projected.mkdir()
        build_projection(directory, projected, card, args, resources, "single-projection")
    log("Read or collect the training examples")
    rows = read_examples(args.training_data, healing) if args.training_data else make_examples(directory, projected, args, resources)
    if args.training_data:
        harmless = prompts(args.prompts)["harmless"]
        if any(not any(row["prompt"] == item or row["prompt"].startswith(item + " ") for item in harmless) for row in rows):
            raise ValueError("external training prompts must come from the harmless prompt list")
    rows = rows[:args.pairs]
    evidence = out / "evidence"
    evidence.mkdir(exist_ok=True)
    data = evidence / "training.jsonl"
    data.write_text("".join(json.dumps(row) + "\n" for row in rows))
    card["training"] = {"epochs": 1, "examples": len(rows), "sha256": digest(data),
                        "objective": "dpo" if healing else "answer-token-cross-entropy",
                        "target_modules": ["q_proj", "v_proj"], "reference": "adapter-disabled projected base" if healing else None,
                        "source": "external JSONL" if args.training_data else "base answers to harmless prompt variations",
                        "beta": 0.1 if healing else None}
    from audit.weights import write_json
    write_json(out / "recipe-card.json", card)
    if not rows or (healing and len(rows) < args.pairs):
        raise ValueError(f"only {len(rows)} distinct training examples; saved {data}; supply --training-data or request fewer pairs")
    runtime, tokenizer = load_runtime(projected or directory, resources)
    log(f"Train one epoch on {len(rows)} examples")
    adapted = preference(runtime, tokenizer, rows, args, resources, out) if healing else supervised(runtime, tokenizer, rows, args, resources)
    del runtime
    log("Merge the adapter and save the derived checkpoint")
    merged = adapted.merge_and_unload()
    save_merged(merged, tokenizer, out, directory)
    del merged, adapted
    release(None)
    if healing:
        # Keep the direction evidence, then remove the regenerable intermediate copy.
        import shutil
        shutil.copyfile(projected / "evidence/direction.safetensors", evidence / "direction.safetensors")
        shutil.rmtree(projected)
    finish(out, card, directory)
