# test_direction_layers.py -- Check the reference rotation, the per-copy placement and the markdown.
# Created by SDE
# Modified: SDE 2026-11-03  three copies, a rotating reference, a missing reference.
import contextlib
import io
import json
import math
from pathlib import Path
import sys
import tempfile
import unittest

import torch
from safetensors.torch import save_file

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'hpc'))

import direction_layers  # noqa: E402

DIM = 16
KIND = 'o_proj'


def key(layer):
    return f'model.layers.{layer}.self_attn.{KIND}.weight.left'


def basis(index):
    vector = torch.zeros(DIM, dtype=torch.float64)
    vector[index] = 1.0
    return vector


def at(degrees):
    angle = math.radians(degrees)
    return math.cos(angle) * basis(0) + math.sin(angle) * basis(1)


def write_copy(root, pull, pair, tensors):
    folder = root / pull / 'measurements' / f'pair-{pair}'
    folder.mkdir(parents=True)
    save_file({key(layer): value.float() for layer, value in tensors.items()},
              str(folder / 'weights.directions.safetensors'))


def build(root):
    reference = {layer: at(layer * 15) for layer in range(12)}
    write_copy(root, 't1', 1, reference)
    write_copy(root, 't1', 2, {layer: reference[7] for layer in range(5, 13)})
    write_copy(root, 't1', 3, {layer: reference[layer] for layer in range(3, 10)})
    group = {
        'parent': 'org/P',
        'copies': [
            {'repo': 'ref/a', 'pull': 't1', 'pair': 1},
            {'repo': 'one/b', 'pull': 't1', 'pair': 2},
            {'repo': 'per/c', 'pull': 't1', 'pair': 3},
        ],
    }
    path = Path(root) / 'org-P.json'
    path.write_text(json.dumps(group))
    return path


def run(group, root, out, reference='ref/a'):
    stream = io.StringIO()
    errors = io.StringIO()
    with contextlib.redirect_stdout(stream), contextlib.redirect_stderr(errors):
        code = direction_layers.main(
            ['--group', str(group), '--pulls', str(root), '--reference', reference,
             '--out', str(out)])
    return code, stream.getvalue(), errors.getvalue()


class DirectionLayersTest(unittest.TestCase):

    def test_rotation_and_placement(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / 'pulls'
            out = Path(tmp) / 'out' / 'org-P.md'
            group = build(root)
            code, _, _ = run(group, root, out)
            self.assertEqual(code, 0)
            document = json.loads(out.with_suffix('.json').read_text())
            rot = document['rotation']
            self.assertAlmostEqual(rot['adjacent_median'], 0.966, delta=0.01)
            self.assertEqual(rot['adjacent_count'], 11)
            # A 15 degree step repeats every 180 degrees, so the far pairs are
            # 0, 30, 60 or 90 degrees apart: median 0.866, minimum 0.866.
            self.assertLess(rot['far_median'], 0.9)
            self.assertLessEqual(rot['far_min'], 0.9)
            rows = {row['repo']: row for row in document['copies']}
            one = rows['one/b']
            self.assertAlmostEqual(one['own_spread'], 1.0, places=6)
            self.assertEqual(one['best'][0], 7)
            self.assertAlmostEqual(one['best'][1], 1.0, places=6)
            self.assertEqual(one['window'], [5, 12])
            self.assertAlmostEqual(one['adjacent'], 1.0, places=6)
            self.assertIsNone(one['far'])
            per = rows['per/c']
            self.assertLess(per['own_spread'], 0.9)
            self.assertEqual(per['best'][0], 6)
            self.assertAlmostEqual(per['best'][1], 1.0, places=6)
            self.assertIn(per['next'][0], (5, 7))
            self.assertAlmostEqual(per['adjacent'], 0.966, delta=0.01)
            self.assertIsNone(per['far'])
            self.assertEqual(document['skipped'], [])

    def test_markdown_rows(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / 'pulls'
            out = Path(tmp) / 'out' / 'org-P.md'
            group = build(root)
            run(group, root, out)
            lines = out.read_text().splitlines()
            self.assertTrue(lines[0].startswith('# org-P -- ref/a placed layer by layer'))
            self.assertEqual(lines[1], '')
            self.assertIn('adjacent layers median', lines[2])
            header = next(line for line in lines if line.startswith('| copy |'))
            self.assertEqual(header, '| copy | window | own spread | adjacent | far | '
                                     'best layer | cos | next layer | cos |')
            start = next(i for i, line in enumerate(lines) if line.startswith('| --- |'))
            table = [line for line in lines[start + 1:] if line.startswith('| ')]
            self.assertEqual(len(table), 2)
            self.assertTrue(table[0].startswith(
                '| one/b | 5..12 | 1.000 | 1.000 | none | 7 | 1.000 | '))
            self.assertNotIn(' 7.000 ', out.read_text())

    def test_missing_reference(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / 'pulls'
            out = Path(tmp) / 'out' / 'org-P.md'
            group = build(root)
            code, _, errors = run(group, root, out, reference='none/x')
            self.assertEqual(code, 2)
            self.assertEqual(len(errors.splitlines()), 1)


if __name__ == '__main__':
    unittest.main()
