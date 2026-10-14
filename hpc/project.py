# project.py -- Measure a middle-layer direction and project residual writers.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  save activation and tensor stages between short jobs.
# Modified: SDE 2026-10-14  resolve tokenizers from the text configuration.
# Modified: SDE 2026-10-14  load tekken-only tokenizers and skip their generation flag.
# Modified: SDE 2026-10-14  name the projection filter so tests can run it on real names.
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


def load_tokenizer(original, config=None):
    """Use the text configuration; the vision wrapper has no tokenizer."""
    import importlib.util
    from transformers import AutoConfig, AutoTokenizer
    original = Path(original)
    # A tekken.json-only checkpoint needs mistral-common; without it the
    # sentencepiece fallback dies on a missing file ("not a string").
    if (original / 'tekken.json').exists() and not (original / 'tokenizer.json').exists() \
            and importlib.util.find_spec('mistral_common') is None:
        raise RuntimeError('tokenizer: {} has only tekken.json; install mistral-common'.format(original))
    if config is None:
        config = AutoConfig.from_pretrained(str(original), local_files_only=True, trust_remote_code=False)
    text_config = getattr(config, 'get_text_config', lambda: config)()
    try:
        return AutoTokenizer.from_pretrained(str(original), config=text_config,
                                            local_files_only=True, trust_remote_code=False)
    except (ImportError, OSError, TypeError, ValueError) as error:
        raise RuntimeError('tokenizer: cannot load one from {}: {}: {}'.format(
            original, type(error).__name__, error)) from error


def chat_ids(tokenizer, instruction):
    """Render one user turn up to the assistant prefix as a 1 x n tensor."""
    messages = [{'role': 'user', 'content': instruction}]
    if type(tokenizer).__name__ == 'MistralCommonTokenizer':
        # mistral-common refuses the flag; a user turn already ends at [/INST].
        ids = tokenizer.apply_chat_template(messages, return_tensors='pt')
    else:
        ids = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors='pt')
    if hasattr(ids, 'keys'):
        ids = ids['input_ids']
    return ids if ids.dim() == 2 else ids.unsqueeze(0)


def activations(original, groups, stage, fingerprint, cpu):
    """Stop each forward at the middle layer; logits would only spend time."""
    import torch
    from safetensors.torch import save_file
    from transformers import AutoConfig, AutoModelForCausalLM, Mistral3ForConditionalGeneration
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
    tokenizer = load_tokenizer(original, config)
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
        ids = chat_ids(tokenizer, instruction)
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


def projected(name):
    """Change text residual writers only; vision and its projector stay put."""
    from audit.weights import tensor_kind
    is_text = 'vision' not in name and 'multi_modal_projector' not in name
    return is_text and tensor_kind(name) in ('attention_output', 'feed_forward_down')


def projection(store, direction, destination, fingerprint):
    """Write one tensor shard at a time, preserving every untouched dtype."""
    import torch
    from safetensors import safe_open
    from safetensors.torch import save_file
    from audit.weights import write_json
    destination.mkdir(parents=True, exist_ok=True)
    index, touched, total = {}, [], 0
    for number, name in enumerate(sorted(store.names)):
        shard = 'tensor-{:05d}.safetensors'.format(number)
        path = destination / shard
        change = projected(name)
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
