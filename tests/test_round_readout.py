# test_round_readout.py -- Check the pairs table, the mode and placement cells and the census change lines.
# Created by LT Sean Egan, PhD
# Modified: SDE 2026-11-04  first pass: two pairs, one measured and one missing, a mode change and a new copy.
import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'hpc'))

import round_readout  # noqa: E402


class RoundReadoutTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.measurements = self.root / 'measurements'
        (self.measurements / 'pair-1').mkdir(parents=True)
        (self.measurements / 'pair-2').mkdir()
        (self.measurements / 'pair-1' / 'weights.json').write_text(json.dumps({
            'tensors': {
                'model.layers.3.x': {'changed': True},
                'model.layers.4.x': {'changed': True},
                'model.layers.5.x': {'changed': False},
            },
            'summary': {'min_first_singular_energy_share': None},
        }))
        self.batch = self.root / 'batch.json'
        self.batch.write_text(json.dumps({'pairs': [
            {'modified': {'hub_id': 'a/one'}, 'original': {'hub_id': 'b/p'}},
            {'modified': {'hub_id': 'a/two'}, 'original': {'hub_id': 'b/p'}},
        ]}))
        self.before = self.root / 'before.json'
        self.before.write_text(json.dumps({
            'copies': [{'repo': 'a/two', 'parent': 'b/p', 'mode': 'mixed'}],
            'counts': {'mixed': 1},
        }))
        self.modes = self.root / 'modes.json'
        self.modes.write_text(json.dumps({
            'copies': [
                {'repo': 'a/two', 'parent': 'b/p', 'mode': 'per layer'},
                {'repo': 'a/three', 'parent': 'b/q', 'mode': 'mixed'},
            ],
            'counts': {'per layer': 1, 'mixed': 1},
        }))
        self.placement = self.root / 'placement.json'
        self.placement.write_text(json.dumps({'rows': [], 'skipped': []}))
        self.out = self.root / 'readout.md'
        with contextlib.redirect_stdout(io.StringIO()):
            round_readout.main([
                '--measurements', str(self.measurements),
                '--batch', str(self.batch),
                '--placement', str(self.placement),
                '--modes', str(self.modes),
                '--before', str(self.before),
                '--round', '7',
                '--out', str(self.out),
            ])
        self.markdown = self.out.read_text()
        self.rows = {}
        for line in self.markdown.splitlines():
            if line.startswith('| ') and not line.startswith('| pair') \
                    and not line.startswith('| ---'):
                cells = [cell.strip() for cell in line.strip('|').split('|')]
                self.rows[cells[1]] = cells

    def test_heading(self):
        self.assertTrue(self.markdown.startswith('# Round 7 read-out\n'))
        self.assertIn('## Pairs', self.markdown)
        self.assertIn('## Census change', self.markdown)

    def test_one(self):
        row = self.rows['a/one']
        self.assertIn('| 2 | 2 | n/a |', self.markdown)
        self.assertEqual(row[3:6], ['2', '2', 'n/a'])
        self.assertIn('only copy of its parent', row[6])
        self.assertEqual(row[7], 'not placed')
        self.assertIn('Pairs here with no census row: 1', self.markdown)

    def test_two(self):
        row = self.rows['a/two']
        self.assertEqual(row[3:6], ['missing', 'missing', 'missing'])
        self.assertEqual(row[6], 'per layer')

    def test_census_change(self):
        self.assertIn('Before: mixed 1', self.markdown)
        self.assertIn('After: per layer 1, mixed 1', self.markdown)
        self.assertIn('- a/two: mixed -> per layer', self.markdown)
        self.assertIn('- a/three (b/q): mixed', self.markdown)


if __name__ == '__main__':
    unittest.main()
