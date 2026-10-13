# project.py -- Measure a middle-layer direction and project residual writers.
# Created by LT Sean Egan, PhD 2026-10-13
# Modified: SDE 2026-10-13  save activation and tensor stages between short jobs.
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import time


def identity(original, groups):
    """Bind resumable work to the pinned source, prompts and recipe version."""
    manifest = json.loads((original / 'download-manifest.json').read_text())
    record = {'base': manifest['base'], 'base_revision': manifest['revision'],
              'recipe': 'single-projection', 'version': 1, 'prompts': groups,
              'source_sha256': {row['path']: row['sha256'] for row in manifest['files']}}
    record['fingerprint'] = hashlib.sha256(json.dumps(record, sort_keys=True).encode()).hexdigest()
    return record


def text_layers(model):
    """Find decoder layers without mistaking vision blocks for text blocks."""
    candidates = [module for name, module in model.named_modules()
                  if name.endswith('layers') and hasattr(module, '__len__')
                  and ('language_model' in name or name == 'model.layers')]
    if len(candidates) != 1:
        raise ValueError('cannot identify one text decoder')
    return candidates[0]


def activations(original, groups, stage, fingerprint, cpu):
    """Stop each forward at the middle layer; logits would only spend time."""
    import torch
    from safetensors.torch import save_file
    from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer, Mistral3ForConditionalGeneration
    config = AutoConfig.from_pretrained(str(original), local_files_only=True, trust_remote_code=False)
    loader = Mistral3ForConditionalGeneration if config.model_type == 'mistral3' else AutoModelForCausalLM
    options = {'local_files_only': True, 'trust_remote_code': False, 'use_safetensors': True,
               'torch_dtype': torch.float32 if cpu else torch.bfloat16,
               'attn_implementation': 'eager'}
    if not cpu:
        if not torch.cuda.is_available() or torch.cuda.device_count() != 4:
            raise ValueError('expected four allocated CUDA devices')
        options['device_map'] = 'auto'
        options['max_memory'] = {index: torch.cuda.get_device_properties(index).total_memory - 4 * 1024 ** 3 for index in range(4)}
        options['max_memory']['cpu'] = '16GiB'
    model = loader.from_pretrained(str(original), **options).eval()
    tokenizer = AutoTokenizer.from_pretrained(str(original), local_files_only=True, trust_remote_code=False)
    layers = text_layers(model)
    middle = len(layers) // 2
    captured = []

    class Captured(Exception):
        """End a forward once its requested residual is in hand."""

    def capture(module, arguments):
        """Read the last token at the layer input, matching the CPU null."""
        captured.append(arguments[0][0, -1].detach().double().cpu())
        raise Captured()

    hook = layers[middle].register_forward_pre_hook(capture)
    device = model.get_input_embeddings().weight.device

    def residual(instruction):
        """Render the native assistant prefix and read exactly one residual."""
        ids = tokenizer.apply_chat_template([{'role': 'user', 'content': instruction}],
                    add_generation_prompt=True, return_tensors='pt')
        if ids.shape[-1] > 512:
            raise ValueError('prompt exceeds the 512-token timing budget')
        captured[:] = []
        try:
            with torch.inference_mode():
                model(input_ids=ids.to(device), attention_mask=torch.ones_like(ids).to(device), use_cache=False)
        except Captured:
            pass
        if len(captured) != 1 or not torch.isfinite(captured[0]).all():
            raise ValueError('forward did not return a finite middle residual')
        return captured[0]

    try:
        started = time.monotonic()
        for group in ('harmful', 'harmless'):
            for prompt in groups[group][:2]:
                residual(prompt)
        timing = {'backend_up': True, 'request_errors': 0, 'prompts': 4,
                  'seconds': time.monotonic() - started, 'middle_layer': middle, 'fingerprint': fingerprint}
        (stage / 'timing.json').write_text(json.dumps(timing, indent=2) + '\n')
        print('timing: backend up; request errors 0; four prompts passed')
        for group in ('harmful', 'harmless'):
            for index, prompt in enumerate(groups[group]):
                path = stage / '{}-{:02d}.safetensors'.format(group, index)
                if path.exists():
                    continue
                vector = residual(prompt)
                temporary = str(path) + '.part'
                save_file({'residual': vector}, temporary, metadata={'fingerprint': fingerprint})
                os.replace(temporary, str(path))
                print('activation: {} {}/32'.format(group, index + 1), flush=True)
    finally:
        hook.remove()
        del model
        if not cpu:
            torch.cuda.empty_cache()
    return middle


def projection(store, direction, destination, fingerprint):
    """Write one tensor shard at a time, preserving every untouched dtype."""
    import torch
    from safetensors import safe_open
    from safetensors.torch import save_file
    from audit.weights import tensor_kind, write_json
    destination.mkdir(parents=True, exist_ok=True)
    index, touched, total = {}, [], 0
    for number, name in enumerate(sorted(store.names)):
        shard = 'tensor-{:05d}.safetensors'.format(number)
        path = destination / shard
        is_text = 'vision' not in name and 'multi_modal_projector' not in name
        change = is_text and tensor_kind(name) in ('attention_output', 'feed_forward_down')
        if change:
            touched.append(name)
        if path.exists():
            with safe_open(str(path), framework='pt') as saved:
                if saved.metadata() != {'fingerprint': fingerprint, 'tensor': name} or list(saved.keys()) != [name]:
                    raise ValueError('saved tensor belongs to a different projection')
                shape = saved.get_slice(name).get_shape()
            source = store.get(name)
            if list(source.shape) != shape:
                raise ValueError('saved tensor shape differs')
            total += source.numel() * source.element_size()
            del source
        else:
            tensor = store.get(name)
            if change:
                if tensor.ndim != 2 or tensor.shape[0] != direction.numel():
                    raise ValueError('residual writer has a different width: ' + name)
                weight = tensor.float()
                tensor = (weight - direction[:, None] * (direction @ weight)[None, :]).to(tensor.dtype)
            total += tensor.numel() * tensor.element_size()
            temporary = str(path) + '.part'
            save_file({name: tensor.contiguous()}, temporary, metadata={'fingerprint': fingerprint, 'tensor': name})
            os.replace(temporary, str(path))
            del tensor
        index[name] = shard
    for path in store.directory.iterdir():
        if path.suffix == '.json' and path.name not in ('download-manifest.json', 'model.safetensors.index.json'):
            shutil.copyfile(str(path), str(destination / path.name))
        elif path.name == 'tokenizer.model':
            shutil.copyfile(str(path), str(destination / path.name))
    write_json(destination / 'model.safetensors.index.json', {'metadata': {'total_size': total}, 'weight_map': index})
    return touched


def main():
    """Run timing, activations, projection and the existing tensor comparison."""
    import torch
    from safetensors import safe_open
    from safetensors.torch import load_file, save_file
    from audit.nulls import prompts
    from audit.weights import TensorStore, write_json
    from audit.weights_cli import main as audit_main
    torch.set_num_threads(1)
    torch.set_num_interop_threads(1)
    torch.manual_seed(0)
    original = Path(os.environ['AUDIT_ORIGINAL'])
    derived = Path(os.environ['AUDIT_DERIVED'])
    work = Path(os.environ['AUDIT_WORK'])
    stage = work / 'state/projection'
    stage.mkdir(parents=True, exist_ok=True)
    groups = prompts(Path('data/prompts'))
    card = identity(original, groups)
    context = stage / 'context.json'
    if context.exists() and json.loads(context.read_text()) != card:
        raise ValueError('saved stages use different inputs')
    write_json(context, card)
    marker = work / 'state/activations.done'
    if not marker.exists():
        middle = activations(original, groups, stage, card['fingerprint'], os.environ.get('AUDIT_REHEARSAL') == '1')
        marker.write_text(str(middle) + '\n')
        (work / 'state/timing.done').write_text(card['fingerprint'] + '\n')
    else:
        middle = int(marker.read_text())
    direction_path = stage / 'refusal-direction.safetensors'
    if not direction_path.exists():
        sums = {}
        for group in ('harmful', 'harmless'):
            vectors = []
            for index in range(32):
                path = stage / '{}-{:02d}.safetensors'.format(group, index)
                with safe_open(str(path), framework='pt') as saved:
                    if saved.metadata()['fingerprint'] != card['fingerprint']:
                        raise ValueError('activation checkpoint differs')
                    vectors.append(saved.get_tensor('residual'))
            sums[group] = torch.stack(vectors).mean(0)
        direction = (sums['harmful'] - sums['harmless']).float()
        norm = direction.norm()
        if not torch.isfinite(direction).all() or norm == 0:
            raise ValueError('activation difference has no finite direction')
        direction /= norm
        save_file({'refusal_direction': direction}, str(direction_path) + '.part')
        os.replace(str(direction_path) + '.part', str(direction_path))
    direction = load_file(str(direction_path))['refusal_direction']
    if not (work / 'state/project.done').exists():
        touched = projection(TensorStore(original), direction, derived, card['fingerprint'])
        if not touched:
            raise ValueError('no text residual writers were projected')
        recipe = dict(card, tensors_touched=touched, middle_layer=middle,
                      token_position='last token of assistant prefix',
                      precision={'weights': 'original tensor dtypes', 'projection': 'float32', 'activation_means': 'float64',
                                 'forward': 'float32' if os.environ.get('AUDIT_REHEARSAL') == '1' else 'bfloat16'},
                      date=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
        write_json(derived / 'recipe-card.json', recipe)
        (work / 'state/project.done').write_text(card['fingerprint'] + '\n')
    report = Path(os.environ['AUDIT_MEASUREMENT'])
    if not (work / 'state/compare.done').exists():
        rc = audit_main(['compare-weights', '--modified', str(derived), '--original', str(original), '--out', str(report), '--threads', '1'])
        if rc:
            raise SystemExit(rc)
        (work / 'state/compare.done').write_text(card['fingerprint'] + '\n')
    # Copy only small records into the measurement folder. Weights stay in work.
    for source in (stage / 'timing.json', derived / 'recipe-card.json', direction_path):
        shutil.copyfile(str(source), str(report.parent / source.name))
    count = int(subprocess.check_output(['du', '-sk', str(work)], universal_newlines=True).split()[0])
    (Path(os.environ['HOME']) / '.hpc/model-audit-space.tsv').write_text('{}\t{}\n'.format(work, count))
    print('Measurements complete: ' + str(report))


if __name__ == '__main__':
    main()
