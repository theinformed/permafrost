# test_mode_sizes.py -- Check the per-copy size figures, the no-report row and the per-mode medians.
# Created by LT Sean Egan, PhD
# Modified: SDE 2026-11-03  three copies, two reports, one missing report.
# Modified: SDE 2026-11-03  a fourth copy for the quartiles, the per-parent rows and the crossings.
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
            {'parent': 'org/Q', 'repo': 'four/d', 'layers': 1, 'mode': 'arbitrary rank'},
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
        (self.weights / 'four-d.json').write_text(json.dumps(report({
            'model.layers.2.mlp.down_proj.weight': {'changed': True,
                                                    'relative_difference': 0.7},
        }, 0.95, ['feed_forward_down'])))
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

    def test_arbitrary_rank_quartiles(self):
        figures = self.document['modes']['arbitrary rank']
        self.assertEqual(figures['copies'], 2)
        self.assertEqual(figures['changed_tensors_q1'], 1)
        self.assertEqual(figures['changed_tensors_q3'], 1)
        self.assertAlmostEqual(figures['singular_share_q1'], 0.6875)
        self.assertAlmostEqual(figures['singular_share_q3'], 0.8625)
        self.assertAlmostEqual(figures['median_relative'], 0.6)

    def test_crossings(self):
        crossings = self.document['crossings']
        self.assertEqual(crossings['arbitrary_high_share'], 1)
        self.assertEqual(crossings['arbitrary_measured'], 2)
        self.assertEqual(crossings['other_low_share'], 0)
        self.assertEqual(crossings['other_measured'], 1)
        self.assertIn('arbitrary rank copies with singular share 0.9 or more: 1 of 2',
                      self.markdown)

    def test_per_parent(self):
        parents = self.document['parents']
        self.assertIn({'parent': 'org/Q', 'mode': 'arbitrary rank', 'copies': 1,
                       'changed_tensors': 1, 'median_relative': 0.7,
                       'singular_share': 0.95}, parents)
        self.assertIn('## per parent', self.markdown)


if __name__ == '__main__':
    unittest.main()
