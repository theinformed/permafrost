# measure.py -- Reject old round inputs before the checkpoint comparison reads them.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  seed on-disk tensor names and date calibration inputs.
import hashlib
import json
import os
from pathlib import Path
import sys


def checksum(path):
    """Hash one file at a time, without loading a weight shard into memory."""
    value = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            value.update(block)
    return value.hexdigest()


def fresh(paths, started):
    """A previous run does not get a fresh date just because we found its files."""
    for path in paths:
        if path.stat().st_mtime < started:
            raise ValueError('stale measurement input refused: ' + str(path))


def round_inputs():
    """Date only the derived checkpoint and report this comparison consumes."""
    derived = Path(os.environ['AUDIT_DERIVED'])
    report = Path(os.environ['AUDIT_MEASUREMENT'])
    paths = [path for path in sorted(derived.rglob('*')) if path.is_file()]
    if report.is_file():
        paths.append(report)
    return paths


def verify_original():
    """Shared originals may be old; they must still match the download receipt."""
    original = Path(os.environ['AUDIT_ORIGINAL'])
    record = json.loads((original / 'download-manifest.json').read_text())
    if record['base'] != os.environ['AUDIT_BASE'] or not record['files']:
        raise ValueError('original receipt belongs to a different or empty snapshot')
    for row in record['files']:
        path = original / row['path']
        if Path(row['path']).name != row['path'] or path.is_symlink():
            raise ValueError('unexpected original path: ' + str(path))
        if path.stat().st_size != row['size'] or checksum(path) != row['sha256']:
            raise ValueError('original checksum differs: ' + str(path))


def measurement(arguments, runner):
    """Let a failed comparison reach the shell before it writes a done marker."""
    fresh(round_inputs(), float(os.environ['AUDIT_JOB_STARTED']))
    verify_original()
    result = runner(arguments)
    if result:
        raise SystemExit(result)
    return result


def seed_original():
    """Write a small two-shard rehearsal checkpoint with pinned checksums."""
    import torch
    from safetensors.torch import save_file
    torch.set_num_threads(1)
    original = Path(os.environ['AUDIT_ORIGINAL'])
    original.mkdir(parents=True, exist_ok=True)
    generator = torch.Generator().manual_seed(7)
    tensors = {}
    for layer in range(2):
        prefix = 'language_model.model.layers.{}.'.format(layer)
        for suffix, shape in (
            ('input_layernorm', (64,)), ('post_attention_layernorm', (64,)),
            ('self_attn.q_proj', (64, 64)), ('self_attn.k_proj', (32, 64)),
            ('self_attn.v_proj', (32, 64)), ('self_attn.o_proj', (64, 64)),
            ('mlp.gate_proj', (128, 64)), ('mlp.up_proj', (128, 64)),
            ('mlp.down_proj', (64, 128))):
            tensors[prefix + suffix + '.weight'] = torch.randn(*shape, generator=generator).bfloat16()
    prefix = 'vision_tower.transformer.layers.0.'
    for suffix, shape in (
        ('attention.q_proj', (32, 32)), ('attention.k_proj', (32, 32)),
        ('attention.v_proj', (32, 32)), ('attention.o_proj', (32, 32)),
        ('attention_norm', (32,)), ('ffn_norm', (32,)),
        ('feed_forward.gate_proj', (64, 32)), ('feed_forward.up_proj', (64, 32)),
        ('feed_forward.down_proj', (32, 64))):
        tensors[prefix + suffix + '.weight'] = torch.randn(*shape, generator=generator).bfloat16()
    for name, shape in (
        ('language_model.model.embed_tokens.weight', (256, 64)),
        ('language_model.model.norm.weight', (64,)), ('language_model.lm_head.weight', (256, 64)),
        ('vision_tower.ln_pre.weight', (32,)), ('vision_tower.patch_conv.weight', (32, 3, 4, 4)),
        ('multi_modal_projector.norm.weight', (32,)),
        ('multi_modal_projector.patch_merger.merging_layer.weight', (32, 128)),
        ('multi_modal_projector.linear_1.weight', (64, 32)),
        ('multi_modal_projector.linear_2.weight', (64, 64))):
        tensors[name] = torch.randn(*shape, generator=generator).bfloat16()
    names = sorted(tensors)
    weight_map = {}
    for number, group in enumerate((names[::2], names[1::2])):
        shard = 'model-{:05d}-of-00002.safetensors'.format(number + 1)
        save_file({name: tensors[name] for name in group}, str(original / shard))
        weight_map.update({name: shard for name in group})
    index = {'metadata': {'total_size': sum(t.numel() * t.element_size() for t in tensors.values())},
             'weight_map': weight_map}
    (original / 'model.safetensors.index.json').write_text(json.dumps(index) + '\n')
    config = {'architectures': ['Mistral3ForConditionalGeneration'], 'image_token_index': 10,
              'model_type': 'mistral3', 'multimodal_projector_bias': False,
              'projector_hidden_act': 'gelu', 'spatial_merge_size': 2, 'torch_dtype': 'bfloat16',
              'transformers_version': '4.52.4', 'vision_feature_layer': -1,
              'text_config': {'attention_dropout': 0.0, 'head_dim': 32, 'hidden_act': 'silu',
                              'hidden_size': 64, 'initializer_range': 0.02, 'intermediate_size': 128,
                              'max_position_embeddings': 131072, 'model_type': 'mistral',
                              'num_attention_heads': 2, 'num_hidden_layers': 2,
                              'num_key_value_heads': 1, 'rms_norm_eps': 1e-5,
                              'rope_theta': 1000000000.0, 'sliding_window': None,
                              'use_cache': True, 'vocab_size': 256},
              'vision_config': {'attention_dropout': 0.0, 'head_dim': 16, 'hidden_act': 'silu',
                                'hidden_size': 32, 'image_size': 8, 'initializer_range': 0.02,
                                'intermediate_size': 64, 'model_type': 'pixtral',
                                'num_attention_heads': 2, 'num_channels': 3,
                                'num_hidden_layers': 1, 'patch_size': 4, 'rope_theta': 10000.0}}
    (original / 'config.json').write_text(json.dumps(config) + '\n')
    files = [path for path in sorted(original.iterdir()) if path.name != 'download-manifest.json']
    record = {'base': os.environ['AUDIT_BASE'], 'revision': 'synthetic', 'files': [
        {'path': path.name, 'size': path.stat().st_size, 'sha256': checksum(path)} for path in files]}
    (original / 'download-manifest.json').write_text(json.dumps(record) + '\n')


def main():
    """Check declared inputs before calibration and preserve comparison failures."""
    stub = os.environ.get('AUDIT_STUB') == '1' and os.environ.get('AUDIT_REHEARSAL') == '1'
    if sys.argv[1:] == ['--seed-original']:
        if not stub:
            raise ValueError('synthetic original requires stub rehearsal mode')
        seed_original()
        return
    if sys.argv[1:]:
        raise ValueError('unknown measurement argument')
    started = float(os.environ['AUDIT_JOB_STARTED'])
    fresh(round_inputs(), started)
    verify_original()
    import calibrate
    from audit import weights_cli

    def compare(arguments):
        """Send a forced fault through the same comparison exit path."""
        def runner(args):
            """Keep the forced rehearsal fault out of the real measurement."""
            if stub and os.environ.get('AUDIT_FAIL_MEASUREMENT') == '1':
                print('measurement failed: forced comparison fault', flush=True)
                return 23
            return weights_cli.main(args)
        return measurement(arguments, runner)

    calibrate.main(compare)
    fresh([Path(os.environ['AUDIT_MEASUREMENT']), Path(os.environ['AUDIT_CARD'])], started)


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError) as error:
        raise SystemExit(str(error))
