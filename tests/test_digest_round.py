# test_digest_round.py -- Check the per-pair digests and the round index.
# Created by SDE 2026-11-03
# Modified: SDE 2026-11-03  two pairs, both share headings, the 0.7 row, the unreadable pair.
import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'hpc'))

import digest_round  # noqa: E402

SECTIONS = ['## Pair', '## Metadata', '## Weights assessment',
            '## Changed tensors', '## Directions', '## Oddities']


def tensor_row(kind, changed, relative, share=None, positive=None):
    row = {'kind': kind, 'changed': changed, 'relative_difference': relative,
           'status': 'ok', 'positive_fraction': positive}
    if share is not None:
        row['first_singular_energy_share'] = share
    return row


def write_pair(root, number, with_share=True):
    folder = root / f'pair-{number}'
    folder.mkdir()
    (folder / 'card.md').write_text('# Card\n\n## Verdict\n\n## Notes\n')
    meta = {
        'schema_version': 1,
        'modified': {'repo': f'maker/copy-{number}', 'sha': 'a' * 40},
        'original': {'repo': 'google/base', 'sha': 'b' * 40},
        'differences': [
            {'path': 'config.transformers_version', 'original': '5.5.0.dev0',
             'modified': '5.5.0', 'class': 'explained by re-save'},
            {'path': 'template.default', 'original': None,
             'modified': 'x', 'class': 'unexplained'},
        ],
        'missing': [],
        'limitation': 'This metadata audit does not certify the absence of hidden behavior.',
        'verdict': 'unexplained differences',
    }
    (folder / 'metadata.json').write_text(json.dumps(meta))
    (folder / 'receipt.json').write_text(json.dumps({
        'pair': number, 'measurement_sha256': 'c' * 64,
        'card_sha256': 'd' * 64, 'metadata_sha256': 'e' * 64,
        'deleted_checkpoints': [], 'shared_original': False}))
    tensors = {
        'model.language_model.layers.3.self_attn.o_proj.weight':
            tensor_row('attention_output', True, 0.7,
                       share=0.99 if with_share else None, positive=0.4),
        'model.language_model.layers.4.self_attn.o_proj.weight':
            tensor_row('attention_output', True, 0.0,
                       share=0.98 if with_share else None, positive=0.5),
        'model.language_model.layers.5.mlp.down_proj.weight':
            tensor_row('feed_forward_down', True, 0.02,
                       share=0.995 if with_share else None, positive=0.3),
        'model.language_model.layers.6.mlp.down_proj.weight':
            tensor_row('feed_forward_down', False, 0.0,
                       share=0.997 if with_share else None, positive=0.0),
    }
    weights = {
        'schema_version': 1,
        'original': {'source': '/p/original', 'revision': None,
                     'shards_sha256': {'model.safetensors': 'f' * 64}},
        'modified': {'source': '/p/modified', 'revision': None,
                     'shards_sha256': {'model.safetensors': 'f' * 64}},
        'threshold': 0.001,
        'svd': {'seed': 0, 'top_k': 8, 'sketch_columns': 12, 'power_iterations': 4},
        'original_only': [], 'modified_only': [], 'unused_shared_kv': [],
        'dropped_towers': {}, 'dropped_statistics': [],
        'tensors': tensors,
        'summary': {
            'direction_agreement': {'groups': {
                'attention_output:2560': {'count': 2, 'median_direction_defined': True,
                                          'median_cosine': 0.5, 'min_cosine': 0.1},
                'feed_forward_down:2560': {'count': 2, 'median_direction_defined': True,
                                           'median_cosine': 0.9, 'min_cosine': 0.8},
            }},
            'assessment': 'recipe_violations',
        },
        'scope': 'Weight differences alone cannot certify the absence of hidden behavior.',
        'recipe_matching': {
            'nearest_recipe': 'directional-per-layer-selected', 'matched': False,
            'violations': [{'rule': 'first_energy_share'}],
            'candidates': [
                {'recipe': 'directional-per-layer-selected', 'matched': False,
                 'violations': [{'rule': 'first_energy_share'}]},
                {'recipe': 'single-projection', 'matched': False,
                 'violations': [{'rule': 'a'}, {'rule': 'b'}]},
            ],
        },
    }
    (folder / 'weights.json').write_text(json.dumps(weights))
    return folder


def run(measurements, out):
    stream = io.StringIO()
    with contextlib.redirect_stdout(stream):
        code = digest_round.main(['--measurements', str(measurements),
                                  '--out', str(out), '--round', '46'])
    return code, stream.getvalue()


class DigestRoundTest(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.measurements = self.root / 'measurements'
        self.measurements.mkdir()
        write_pair(self.measurements, 1)
        write_pair(self.measurements, 2, with_share=False)
        (self.measurements / 'sweep.json').write_text(json.dumps({
            'deleted': [{'path': '/p/a', 'hub_id': 'google/base',
                         'revision': 'b' * 40, 'pairs': [1]}],
            'kept': [{'path': '/p/b', 'hub_id': 'google/base',
                      'revision': 'b' * 40, 'pairs': [2]}],
            'absent': []}))
        self.out = self.root / 'out'

    def tearDown(self):
        self.tmp.cleanup()

    def test_digests_and_index(self):
        code, printed = run(self.measurements, self.out)
        self.assertEqual(code, 0)
        self.assertEqual(len(printed.strip().splitlines()), 3)
        for name in ('pair-1.digest.md', 'pair-2.digest.md', 'index.md'):
            self.assertTrue((self.out / name).exists(), name)

        text = (self.out / 'pair-1.digest.md').read_text()
        positions = [text.index(heading) for heading in SECTIONS]
        self.assertEqual(positions, sorted(positions))
        self.assertIn('first share', text)
        self.assertIn('positive fraction', text)
        self.assertIn('0.7', text.split('## Oddities')[1])
        self.assertIn('attention_output 1', text)
        self.assertIn('maker/copy-1', text)
        self.assertIn('google/base', text)
        self.assertIn('cccccccc', text)
        self.assertIn('not carried', text)
        self.assertIn('directional-per-layer-selected', text)
        self.assertIn('attention_output:2560', text)

        other = (self.out / 'pair-2.digest.md').read_text()
        self.assertNotIn('first share', other)
        self.assertIn('positive fraction', other)

        index = (self.out / 'index.md').read_text()
        rows = [line for line in index.splitlines()
                if line.startswith('| ') and 'maker/copy' in line]
        self.assertEqual(len(rows), 2)
        self.assertIn('deleted 1', index)
        self.assertIn('kept 1', index)
        self.assertIn('absent 0', index)

    def test_unreadable_pair(self):
        (self.measurements / 'pair-2' / 'weights.json').write_text('{not json')
        code, printed = run(self.measurements, self.out)
        self.assertEqual(code, 1)
        self.assertTrue((self.out / 'pair-1.digest.md').exists())
        self.assertFalse((self.out / 'pair-2.digest.md').exists())
        self.assertIn('pair-2', printed)


if __name__ == '__main__':
    unittest.main()
