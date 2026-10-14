# test_tokenizer_real_files.py -- Load the real round-1 tokenizer and tensor names.
# Created by Sean Egan 2026-10-14
"""The published files, read by the libraries pinned for the cluster.

Earlier tests mocked the tokenizer and used in-memory tensor names, so two
faults reached the cluster. These read what the job reads: tekken.json,
config.json and model.safetensors.index.json at the pinned revision (about
19 MB, cached under .tmp, never weights). They skip when the hub is out of
reach, and the tokenizer checks skip unless transformers matches the pin.
"""
import importlib.metadata
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parent.parent
BASE = 'mistralai/Mistral-Small-3.2-24B-Instruct-2506'
REVISION = '95a6d26c4bfb886c58daf9d3f7332c857cb27b43'
CACHE = ROOT / '.tmp/real-files' / REVISION[:12]
PINS = ROOT / 'hpc/rounds/1/compute-requirements.txt'

# The loader as it stood in retry 5, run with mistral-common hidden.
OLD_FORM = r'''
import sys
sys.modules['mistral_common'] = None
from transformers import AutoConfig, AutoTokenizer
config = AutoConfig.from_pretrained(sys.argv[1], local_files_only=True, trust_remote_code=False)
text_config = getattr(config, 'get_text_config', lambda: config)()
try:
    AutoTokenizer.from_pretrained(sys.argv[1], config=text_config, local_files_only=True, trust_remote_code=False)
    print('loaded')
except Exception as error:
    while error is not None:
        print('{}: {}'.format(type(error).__name__, str(error).strip()[:120]))
        error = error.__cause__ or error.__context__
'''


def fetch(*names):
    """Fetch small published files once; skip when the hub is out of reach."""
    for name in names:
        if not (CACHE / name).exists():
            try:
                from huggingface_hub import hf_hub_download
                hf_hub_download(BASE, name, revision=REVISION, local_dir=str(CACHE))
            except Exception as error:
                raise unittest.SkipTest('cannot fetch {}: {}'.format(name, error))
    return CACHE


def pin(package):
    """Read one exact pin from the cluster's requirements."""
    for line in PINS.read_text().splitlines():
        if line.lower().startswith(package + '=='):
            return line.split('==', 1)[1].strip()
    return None


def installed(package):
    try:
        return importlib.metadata.version(package)
    except importlib.metadata.PackageNotFoundError:
        return None


def cluster_libraries():
    """Tokenizer behavior depends on the version; test only the pinned one."""
    if installed('transformers') != pin('transformers'):
        raise unittest.SkipTest('transformers {} is not the pinned {}'.format(installed('transformers'), pin('transformers')))


class PinnedTokenizerTests(unittest.TestCase):
    """The tekken-only checkpoint needs mistral-common at the pinned version."""

    def test_pins_name_the_tekken_reader(self):
        self.assertIsNotNone(pin('mistral-common'), 'mistral-common is not pinned')
        self.assertIsNotNone(pin('protobuf'), 'protobuf is not pinned')
        cluster_libraries()
        for package in ('mistral-common', 'protobuf', 'sentencepiece', 'tokenizers', 'torch'):
            with self.subTest(package=package):
                self.assertEqual((installed(package) or '').split('+')[0], pin(package) or installed(package))

    def test_checkpoint_ships_only_tekken(self):
        directory = fetch('config.json', 'tekken.json')
        self.assertFalse((directory / 'tokenizer.json').exists())
        self.assertFalse((directory / 'tokenizer.model').exists())

    def test_old_loader_without_mistral_common_fails(self):
        cluster_libraries()
        directory = fetch('config.json', 'tekken.json')
        result = subprocess.run([sys.executable, '-I', '-c', OLD_FORM, str(directory)],
                                capture_output=True, text=True, timeout=300)
        print('\nold loader: ' + ' <- '.join(result.stdout.strip().splitlines()))
        self.assertIn('not a string', result.stdout)
        self.assertNotIn('loaded', result.stdout)

    def test_new_loader_reads_tekken(self):
        cluster_libraries()
        from hpc.project import chat_ids, load_tokenizer
        tokenizer = load_tokenizer(fetch('config.json', 'tekken.json'))
        self.assertEqual(type(tokenizer).__name__, 'MistralCommonTokenizer')
        ids = tokenizer.encode('The quick brown fox', add_special_tokens=False)
        self.assertTrue(ids)
        self.assertEqual(tokenizer.decode(ids), 'The quick brown fox')
        prompt = chat_ids(tokenizer, 'How do I bake bread?')
        self.assertEqual(prompt.dim(), 2)
        self.assertEqual(prompt.shape[0], 1)
        rendered = tokenizer.decode(prompt[0].tolist())
        print('\nnew loader: {} ids {} -> {!r}'.format(type(tokenizer).__name__, prompt.shape[-1], rendered))
        self.assertEqual(rendered, '<s>[INST]How do I bake bread?[/INST]')
        # The old chat call passed a flag this tokenizer refuses.
        with self.assertRaises(ValueError):
            tokenizer.apply_chat_template([{'role': 'user', 'content': 'x'}],
                                          add_generation_prompt=True, return_tensors='pt')


class RealTensorNameTests(unittest.TestCase):
    """The shard index names tensors the way they sit on disk."""

    def test_projection_selects_every_text_residual_writer(self):
        from audit.weights import tensor_kind
        from hpc.project import projected
        directory = fetch('config.json', 'model.safetensors.index.json')
        names = sorted(json.loads((directory / 'model.safetensors.index.json').read_text())['weight_map'])
        layers = json.loads((directory / 'config.json').read_text())['text_config']['num_hidden_layers']
        chosen = [name for name in names if projected(name)]
        kinds = {}
        for name in chosen:
            kinds[tensor_kind(name)] = kinds.get(tensor_kind(name), 0) + 1
        print('\nreal index: {} tensors, {} text layers, {} projected {}'.format(len(names), layers, len(chosen), kinds))
        self.assertEqual(len(names), 585)
        self.assertEqual(layers, 40)
        self.assertEqual(kinds, {'attention_output': layers, 'feed_forward_down': layers})
        for name in names:
            if name.startswith('language_model.'):
                with self.subTest(name=name):
                    self.assertNotEqual(tensor_kind(name), 'other')
        self.assertEqual(tensor_kind('language_model.model.layers.0.self_attn.o_proj.weight'), 'attention_output')
        self.assertEqual(tensor_kind('language_model.model.layers.0.mlp.down_proj.weight'), 'feed_forward_down')


if __name__ == '__main__':
    unittest.main()
