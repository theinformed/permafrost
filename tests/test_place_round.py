# test_place_round.py -- Check the placement of a round's new copies against the census, the markdown and json, and a missing measurements folder.
# Created by SDE
# Modified: SDE 2026-11-03  two new pairs, one placed and one under a new parent.
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

import place_round  # noqa: E402

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


def write_metadata(folder, copy, parent):
    folder.mkdir(parents=True, exist_ok=True)
    meta = {'modified': {'repo': copy}, 'original': {'repo': parent}}
    (folder / 'metadata.json').write_text(json.dumps(meta))


def build(root):
    reference = {layer: at(layer * 15) for layer in range(12)}
    write_copy(root, 't1', 1, reference)
    write_copy(root, 't1', 2, {layer: reference[7] for layer in range(5, 13)})

    census = Path(root) / 'census'
    census.mkdir()
    (census / 'org-P.json').write_text(json.dumps({
        'parent': 'org/P',
        'copies': [
            {'repo': 'ref/a', 'pull': 't1', 'pair': 1},
            {'repo': 'one/b', 'pull': 't1', 'pair': 2},
        ],
    }))
    families = Path(root) / 'families.json'
    families.write_text(json.dumps({
        'families': [{'parent': 'org/P', 'members': ['ref/a', 'one/b']}],
    }))

    round_dir = Path(root) / 'round'
    pair1 = round_dir / 'pair-1'
    write_metadata(pair1, 'new/x', 'org/P')
    save_file({key(layer): reference[7].float() for layer in range(5, 13)},
              str(pair1 / 'weights.directions.safetensors'))
    pair2 = round_dir / 'pair-2'
    write_metadata(pair2, 'new/y', 'org/Q')
    save_file({key(layer): reference[layer].float() for layer in range(4)},
              str(pair2 / 'weights.directions.safetensors'))
    return census, families, round_dir


def run(round_dir, census, families, out):
    stream = io.StringIO()
    errors = io.StringIO()
    with contextlib.redirect_stdout(stream), contextlib.redirect_stderr(errors):
        code = place_round.main(
            ['--measurements', str(round_dir), '--directions', str(census),
             '--families', str(families), '--pulls', str(round_dir.parent),
             '--out', str(out)])
    return code, stream.getvalue(), errors.getvalue()


class PlaceRoundTest(unittest.TestCase):

    def test_placement(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            census, families, round_dir = build(root)
            out = root / 'out' / 'round-54.md'
            code, _, _ = run(round_dir, census, families, out)
            self.assertEqual(code, 0)
            document = json.loads(out.with_suffix('.json').read_text())
            rows = {row['copy']: row for row in document['rows']}
            self.assertEqual(len(document['rows']), 2)
            self.assertEqual(document['skipped'], [])

            placed = rows['new/x']
            self.assertEqual(placed['parent'], 'org/P')
            self.assertEqual(placed['partner'], 'one/b')
            self.assertAlmostEqual(placed['median'], 1.0, places=6)
            self.assertEqual(placed['keys'], 8)
            self.assertEqual(placed['family'], 1)
            self.assertEqual(placed['reference'], 'ref/a')
            self.assertEqual(placed['window'], [5, 12])
            self.assertAlmostEqual(placed['own_spread'], 1.0, places=6)
            self.assertEqual(placed['best_layer'], 7)
            self.assertAlmostEqual(placed['cos'], 1.0, places=6)
            self.assertEqual(placed['note'], '')

            fresh = rows['new/y']
            self.assertEqual(fresh['parent'], 'org/Q')
            self.assertEqual(fresh['note'], 'new parent')
            self.assertIsNone(fresh['partner'])
            self.assertIsNone(fresh['best_layer'])
            self.assertEqual(fresh['family'], 'none')

    def test_markdown_rows(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            census, families, round_dir = build(root)
            out = root / 'out' / 'round-54.md'
            run(round_dir, census, families, out)
            lines = out.read_text().splitlines()
            self.assertEqual(
                lines[0],
                '# round-54 -- new copies placed against the census of saved directions.')
            self.assertEqual(lines[1], '')
            table = [line for line in lines[4:] if line.startswith('| ')]
            self.assertEqual(len(table), 2)
            self.assertTrue(table[0].startswith(
                '| new/x | org/P | one/b | 1.000 | 8 | 1 | 5..12 | 1.000 | 7 | 1.000 | ref/a |'))
            self.assertTrue(table[1].startswith(
                '| new/y | org/Q | none | none | none | none | none | none | none | none '
                '| none | new parent |'))

    def test_missing_measurements(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            census, families, round_dir = build(root)
            out = root / 'out' / 'round-54.md'
            code, _, errors = run(root / 'absent', census, families, out)
            self.assertEqual(code, 2)
            self.assertEqual(len(errors.splitlines()), 1)


if __name__ == '__main__':
    unittest.main()
