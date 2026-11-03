# test_mode_sizes.py -- Check the per-copy size figures, the no-report row and the per-mode medians.
# Created by LT Sean Egan, PhD
# Modified: SDE 2026-11-03  three copies, two reports, one missing report.
# Modified: SDE 2026-11-03  a fourth copy for the quartiles, the per-parent rows and the crossings.
# Modified: SDE 2026-11-03  the crossings section by name, and a fifth copy for the other-mode low-share table.
# Modified: SDE 2026-11-03  the edited window as a fraction of each parent's depth, per copy and per mode.
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
            {'parent': 'org/P', 'repo': 'one/a', 'layers': 2, 'mode': 'per layer',
             'window': [0, 1]},
            {'parent': 'org/P', 'repo': 'two/b', 'layers': 1, 'mode': 'arbitrary rank',
             'window': [4, 4]},
            {'parent': 'org/P', 'repo': 'three/c', 'layers': 1, 'mode': 'mixed'},
            {'parent': 'org/Q', 'repo': 'four/d', 'layers': 1, 'mode': 'arbitrary rank',
             'window': [1, 1]},
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
            'model.layers.2.self_attn.o_proj.weight': {'changed': False,
                                                       'relative_difference': 0.0},
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
        high = crossings['arbitrary_high']
        self.assertIsInstance(high, list)
        self.assertEqual(len(high), 1)
        self.assertEqual(high[0]['repo'], 'four/d')
        self.assertEqual(crossings['other_low'], [])
        self.assertIn('## crossings', self.markdown)
        self.assertIn('| org/Q | four/d | arbitrary rank |', self.markdown)
        low = self.markdown.index('other-mode copies with singular share under 0.9')
        self.assertIn('none', self.markdown[low:].split('## per parent')[0])
        self.assertLess(low, self.markdown.index('## per parent'))

    def test_crossings_other_low(self):
        modes = json.loads(self.modes.read_text())
        modes['copies'].append({'parent': 'org/P', 'repo': 'five/e', 'layers': 1,
                                'mode': 'per layer', 'window': [0, 3]})
        self.modes.write_text(json.dumps(modes))
        (self.weights / 'five-e.json').write_text(json.dumps(report({
            'model.layers.0.mlp.down_proj.weight': {'changed': True,
                                                    'relative_difference': 0.2},
            'model.layers.3.mlp.down_proj.weight': {'changed': True,
                                                    'relative_difference': 0.4},
        }, 0.3, ['feed_forward_down'])))
        out = self.root / 'sizes-five.md'
        with contextlib.redirect_stdout(io.StringIO()):
            mode_sizes.main(['--modes', str(self.modes), '--weights', str(self.weights),
                             '--out', str(out)])
        document = json.loads(out.with_suffix('.json').read_text())
        low = document['crossings']['other_low']
        self.assertEqual(len(low), 1)
        self.assertEqual(low[0]['repo'], 'five/e')
        self.assertEqual(low[0]['changed_tensors'], 2)
        rows = {(row['parent'], row['repo']): row for row in document['copies']}
        self.assertEqual(rows[('org/P', 'one/a')]['changed_tensors'], 2)
        self.assertAlmostEqual(rows[('org/P', 'one/a')]['singular_share'], 0.95)
        self.assertEqual(rows[('org/P', 'two/b')]['changed_tensors'], 1)
        self.assertAlmostEqual(rows[('org/P', 'two/b')]['singular_share'], 0.6)
        self.assertIn('| org/P | five/e | per layer | 2.000 | 2.000 | 0.300 |', out.read_text())

    def test_windows(self):
        one = self.rows[('org/P', 'one/a')]
        self.assertEqual(one['depth'], 2)
        self.assertAlmostEqual(one['start'], 0.0)
        self.assertAlmostEqual(one['end'], 1.0)
        self.assertAlmostEqual(one['span'], 1.0)
        self.assertIs(one['to_last'], True)
        two = self.rows[('org/P', 'two/b')]
        self.assertAlmostEqual(two['start'], 0.8)
        self.assertAlmostEqual(two['end'], 1.0)
        self.assertAlmostEqual(two['span'], 0.2)
        self.assertIs(two['to_last'], True)
        four = self.rows[('org/Q', 'four/d')]
        self.assertAlmostEqual(four['start'], 0.3333, places=3)
        self.assertAlmostEqual(four['end'], 0.6667, places=3)
        self.assertAlmostEqual(four['span'], 0.3333, places=3)
        self.assertIs(four['to_last'], False)
        three = self.rows[('org/P', 'three/c')]
        self.assertIsNone(three['start'])
        self.assertIsNone(three['to_last'])

    def test_window_per_mode(self):
        figures = self.document['modes']['arbitrary rank']
        self.assertAlmostEqual(figures['start'], 0.5667, places=3)
        self.assertAlmostEqual(figures['end'], 0.8333, places=3)
        self.assertEqual(figures['to_last'], 1)
        self.assertEqual(figures['windowed'], 2)
        self.assertIn('| window start (q1 / median / q3) |', self.markdown)
        self.assertIn('1 of 2', self.markdown)

    def test_per_parent(self):
        parents = self.document['parents']
        self.assertIn({'parent': 'org/Q', 'mode': 'arbitrary rank', 'copies': 1,
                       'changed_tensors': 1, 'median_relative': 0.7,
                       'singular_share': 0.95}, parents)
        self.assertIn('## per parent', self.markdown)


if __name__ == '__main__':
    unittest.main()
