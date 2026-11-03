# test_mode_sizes.py -- Check the per-copy size figures, the no-report row and the per-mode medians.
# Created by LT Sean Egan, PhD
# Modified: SDE 2026-11-03  three copies, two reports, one missing report.
import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'hpc'))

import mode_sizes  # noqa: E402


def report(tensors, share, kinds):
    return {'tensors': tensors, 'summary': {'min_first_singular_energy_share': share,
                                            'changed_kinds': kinds}}


class ModeSizesTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.weights = self.root / 'weights'
        self.weights.mkdir()
        modes = {'copies': [
            {'parent': 'org/P', 'repo': 'one/a', 'layers': 2, 'mode': 'per layer'},
            {'parent': 'org/P', 'repo': 'two/b', 'layers': 1, 'mode': 'arbitrary rank'},
            {'parent': 'org/P', 'repo': 'three/c', 'layers': 1, 'mode': 'mixed'},
        ]}
        self.modes = self.root / 'modes.json'
        self.modes.write_text(json.dumps(modes))
        (self.weights / 'one-a.json').write_text(json.dumps(report({
            'model.layers.0.self_attn.o_proj.weight': {'changed': True,
                                                       'relative_difference': 0.1},
            'model.layers.1.self_attn.o_proj.weight': {'changed': True,
                                                       'relative_difference': 0.3},
            'model.layers.1.mlp.down_proj.weight': {'changed': False,
                                                    'relative_difference': 0.0},
        }, 0.95, ['attention_output'])))
        (self.weights / 'two-b.json').write_text(json.dumps(report({
            'model.layers.4.mlp.down_proj.weight': {'changed': True,
                                                    'relative_difference': 0.5},
        }, 0.6, ['feed_forward_down'])))
        self.out = self.root / 'sizes.md'
        with contextlib.redirect_stdout(io.StringIO()):
            mode_sizes.main(['--modes', str(self.modes), '--weights', str(self.weights),
                             '--out', str(self.out)])
        self.document = json.loads(self.out.with_suffix('.json').read_text())
        self.rows = {(row['parent'], row['repo']): row for row in self.document['copies']}
        self.markdown = self.out.read_text()

    def test_one_a(self):
        row = self.rows[('org/P', 'one/a')]
        self.assertEqual(row['changed_tensors'], 2)
        self.assertEqual(row['changed_layers'], 2)
        self.assertAlmostEqual(row['median_relative'], 0.2)
        self.assertAlmostEqual(row['max_relative'], 0.3)
        self.assertAlmostEqual(row['singular_share'], 0.95)

    def test_two_b(self):
        row = self.rows[('org/P', 'two/b')]
        self.assertEqual(row['changed_tensors'], 1)
        self.assertEqual(row['changed_layers'], 1)
        self.assertAlmostEqual(row['median_relative'], 0.5)
        self.assertAlmostEqual(row['max_relative'], 0.5)
        self.assertAlmostEqual(row['singular_share'], 0.6)

    def test_no_report(self):
        row = self.rows[('org/P', 'three/c')]
        self.assertIn('no report', row['kinds'])
        self.assertIsNone(row['changed_tensors'])
        self.assertIn('no report', self.markdown)

    def test_per_mode(self):
        figures = self.document['modes']['per layer']
        self.assertEqual(figures['copies'], 1)
        self.assertEqual(figures['changed_tensors'], 2)
        self.assertAlmostEqual(figures['median_relative'], 0.2)
        self.assertIn('## per copy', self.markdown)


if __name__ == '__main__':
    unittest.main()
