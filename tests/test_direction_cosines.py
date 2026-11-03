# test_direction_cosines.py -- Check the parent grouping, the cosines and the index.
# Created by SDE 2026-11-03
# Modified: SDE 2026-11-03  four copies, two parents, a corrupt file, a folder without metadata.
import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest

import torch
from safetensors.torch import save_file

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'hpc'))

import direction_cosines  # noqa: E402

KEYS = [
    'model.layers.0.mlp.down_proj.weight.left',
    'model.layers.0.mlp.down_proj.weight.right',
    'model.layers.1.mlp.down_proj.weight.left',
    'model.layers.1.mlp.down_proj.weight.right',
    'model.layers.0.self_attn.o_proj.weight.left',
    'model.layers.0.self_attn.o_proj.weight.right',
]
EXTRA = 'model.layers.2.mlp.down_proj.weight.left'


def unit(seed):
    generator = torch.Generator().manual_seed(seed)
    vector = torch.randn(8, generator=generator)
    return vector / vector.norm()


def vectors(seed):
    return {key: unit(seed + i) for i, key in enumerate(KEYS)}


def write_pair(root, pull, number, copy, parent, tensors, metadata=True):
    folder = root / pull / 'measurements' / f'pair-{number}'
    folder.mkdir(parents=True)
    if metadata:
        (folder / 'metadata.json').write_text(json.dumps({
            'modified': {'repo': copy}, 'original': {'repo': parent}}))
    save_file(tensors, str(folder / 'weights.directions.safetensors'))
    return folder


def build(root):
    base = vectors(1)
    negated = {key: -value for key, value in base.items()}
    negated[EXTRA] = unit(99)
    write_pair(root, 'sys1', 1, 'maker/A', 'org/P', base)
    write_pair(root, 'sys1', 2, 'maker/B', 'org/P', base)
    write_pair(root, 'sys2', 3, 'maker/C', 'org/P', negated)
    write_pair(root, 'sys2', 4, 'maker/D', 'org/Q', base)


def run(root, out):
    stream = io.StringIO()
    with contextlib.redirect_stdout(stream):
        code = direction_cosines.main(
            ['--pulls', str(root / 'sys1'), str(root / 'sys2'), '--out', str(out)])
    return code, stream.getvalue()


class DirectionCosinesTest(unittest.TestCase):

    def test_groups_and_cosines(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / 'pulls'
            out = Path(tmp) / 'out'
            build(root)
            code, text = run(root, out)
            self.assertEqual(code, 0)
            document = json.loads((out / 'org-P.json').read_text())
            self.assertEqual(document['parent'], 'org/P')
            self.assertEqual(len(document['comparisons']), 3)
            self.assertFalse((out / 'org-Q.json').exists())
            rows = {(r['copy_a'], r['copy_b']): r for r in document['comparisons']}
            ab = rows[('maker/A', 'maker/B')]
            self.assertTrue(ab['identical'])
            self.assertEqual(ab['right']['median'], 1.0)
            bc = rows[('maker/B', 'maker/C')]
            self.assertEqual(bc['right']['median'], -1.0)
            self.assertEqual(bc['right']['flip_fraction'], 1.0)
            self.assertEqual(bc['shared_keys'], len(KEYS))
            self.assertEqual(len(bc['right']['cosines']), 3)
            index = (out / 'index.md').read_text().splitlines()
            self.assertEqual(len(index), 5)
            self.assertIn('folders read 4, skipped 0, parents with two or more copies 1, '
                          'comparisons written 3', text)

    def test_corrupt_and_missing_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / 'pulls'
            out = Path(tmp) / 'out'
            build(root)
            corrupt = write_pair(root, 'sys1', 5, 'maker/E', 'org/R', vectors(5))
            (corrupt / 'weights.directions.safetensors').write_bytes(b'not a safetensors file')
            write_pair(root, 'sys1', 6, 'maker/F', 'org/R', vectors(6))
            write_pair(root, 'sys1', 7, 'maker/G', 'org/S', vectors(7), metadata=False)
            code, text = run(root, out)
            self.assertEqual(code, 1)
            self.assertTrue((out / 'org-P.json').exists())
            self.assertFalse((out / 'org-R.json').exists())
            self.assertIn('skipped 1', text)


if __name__ == '__main__':
    unittest.main()
