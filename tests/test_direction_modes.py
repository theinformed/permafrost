# test_direction_modes.py -- Check the four edit modes, the name words, the counts line and the family row.
# Created by SDE
# Modified: SDE 2026-11-03  four copies, one family, a rotating reference and a basis ladder.
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

import direction_modes  # noqa: E402

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
    reference = {layer: at(layer * 9) for layer in range(12)}
    write_copy(root, 't1', 1, reference)
    write_copy(root, 't1', 2, {layer: reference[7] for layer in range(5, 13)})
    write_copy(root, 't1', 3, {layer: basis(layer + 2) for layer in range(12)})
    write_copy(root, 't1', 4, {layer: at(layer * 9) for layer in range(2)})
    write_copy(root, 't1', 5, {layer: basis(3) for layer in range(6)})
    census = Path(root) / 'census'
    census.mkdir()
    group = {
        'parent': 'org/P',
        'copies': [
            {'repo': 'ref/a', 'pull': 't1', 'pair': 1},
            {'repo': 'one/b-heretic', 'pull': 't1', 'pair': 2},
            {'repo': 'ara/c-abliterated', 'pull': 't1', 'pair': 3},
            {'repo': 'tiny/d', 'pull': 't1', 'pair': 4},
        ],
    }
    (census / 'org-P.json').write_text(json.dumps(group))
    other = {'parent': 'org/Q', 'copies': [{'repo': 'q/one', 'pull': 't1', 'pair': 5}]}
    (census / 'org-Q.json').write_text(json.dumps(other))
    families = {'families': [
        {'parent': 'org/Q', 'members': ['q/one']},
        {'parent': 'org/P', 'members': ['ref/a', 'one/b-heretic']},
    ]}
    path = census / 'families.json'
    path.write_text(json.dumps(families))
    return census, path


def run(census, families, root, out):
    stream = io.StringIO()
    errors = io.StringIO()
    with contextlib.redirect_stdout(stream), contextlib.redirect_stderr(errors):
        code = direction_modes.main(
            ['--directions', str(census), '--pulls', str(root),
             '--families', str(families), '--out', str(out)])
    return code, stream.getvalue(), errors.getvalue()


class DirectionModesTest(unittest.TestCase):

    def test_modes_words_and_counts(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / 'pulls'
            out = Path(tmp) / 'out' / 'modes.md'
            census, families = build(root)
            code, _, _ = run(census, families, root, out)
            self.assertEqual(code, 0)
            document = json.loads(out.with_suffix('.json').read_text())
            rows = {row['repo']: row for row in document['copies']}
            self.assertEqual(rows['ref/a']['mode'], 'per layer')
            self.assertEqual(rows['one/b-heretic']['mode'], 'one direction')
            self.assertEqual(rows['ara/c-abliterated']['mode'], 'arbitrary rank')
            self.assertEqual(rows['tiny/d']['mode'], 'few layers')
            self.assertEqual(direction_modes.name_word('one/b-heretic'), 'heretic')
            self.assertEqual(direction_modes.name_word('ara/c-abliterated'), 'abliterated')
            self.assertEqual(direction_modes.name_word('tiny/d'), 'other')
            self.assertEqual(rows['ref/a']['family'], 1)
            self.assertEqual(rows['one/b-heretic']['family'], 1)
            self.assertEqual(rows['q/one']['family'], 1)
            self.assertEqual(rows['tiny/d']['family'], 'none')
            self.assertEqual(document['counts']['per layer'], 1)
            self.assertEqual(document['counts']['no file'], 0)
            self.assertEqual(document['by_name']['one direction']['heretic'], 1)
            self.assertEqual(document['by_name']['arbitrary rank']['abliterated'], 1)

            lines = out.read_text().splitlines()
            self.assertTrue(lines[0].startswith('# modes -- every census copy sorted'))
            self.assertEqual(lines[1], '')
            self.assertEqual(lines[2], 'copies 5: per layer 1, one direction 2, '
                                       'arbitrary rank 1, mixed 0, few layers 1, no file 0')
            family = next(line for line in lines if line.startswith('| org/P | 1 |'))
            self.assertEqual(family, '| org/P | 1 | 2 | 1 | 1 | 0 | 0 | 0 |')
            family_header = next(i for i, line in enumerate(lines)
                                 if line.startswith('| parent | family |'))
            family_table = [line for line in lines[family_header + 2:]
                            if line.startswith('| ')][:2]
            self.assertEqual(len(family_table), 2)
            self.assertEqual([line.split(' | ')[1] for line in family_table], ['1', '1'])
            header = next(i for i, line in enumerate(lines)
                          if line.startswith('| parent | copy |'))
            table = [line for line in lines[header + 2:] if line.startswith('| ')]
            self.assertEqual(len(table), 5)
            self.assertTrue(table[0].startswith('| org/P | ara/c-abliterated | 12 | 0..11 |'))
            self.assertIn('| arbitrary rank | none |', table[0])


if __name__ == '__main__':
    unittest.main()
