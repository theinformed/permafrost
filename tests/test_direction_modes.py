# test_direction_modes.py -- Check the four edit modes, the name words, the counts line and the family row.
# Created by SDE
# Modified: SDE 2026-11-03  four copies, one family, a rotating reference and a basis ladder.
# Modified: SDE 2026-11-03  a stale modes.json in the census folder is skipped, even when --out writes beside it.
# Modified: SDE 2026-11-03  down_proj keys give the pair figure: 1.000, 0.000 and none.
# Modified: SDE 2026-11-03  read a copy's mode from down_proj when its o_proj change has no leading direction and its down_proj change has one.
# Modified: SDE 2026-11-03  a switched copy before the pull t1 pair 2 copy leaves that copy's pair at 0.0 read from o_proj.
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


def key(layer, kind=KIND):
    return f'model.layers.{layer}.self_attn.{kind}.weight.left'


def basis(index):
    vector = torch.zeros(DIM, dtype=torch.float64)
    vector[index] = 1.0
    return vector


def at(degrees):
    angle = math.radians(degrees)
    return math.cos(angle) * basis(0) + math.sin(angle) * basis(1)


def write_copy(root, pull, pair, tensors, down=None):
    folder = root / pull / 'measurements' / f'pair-{pair}'
    folder.mkdir(parents=True)
    saved = {key(layer): value.float() for layer, value in tensors.items()}
    saved.update({key(layer, 'down_proj'): value.float()
                  for layer, value in (down or {}).items()})
    save_file(saved, str(folder / 'weights.directions.safetensors'))


def build(root):
    reference = {layer: at(layer * 9) for layer in range(12)}
    write_copy(root, 't1', 1, reference, down=dict(reference))
    write_copy(root, 't1', 2, {layer: reference[7] for layer in range(5, 13)},
               down={layer: basis(3) for layer in range(5, 13)})
    write_copy(root, 't1', 3, {layer: basis(layer + 2) for layer in range(12)})
    write_copy(root, 't1', 4, {layer: at(layer * 9) for layer in range(2)})
    write_copy(root, 't1', 5, {layer: basis(3) for layer in range(6)})
    write_copy(root, 't1', 6, {layer: basis(layer + 2) for layer in range(12)},
               down={layer: basis(3) for layer in range(12)})
    census = Path(root) / 'census'
    census.mkdir()
    group = {
        'parent': 'org/P',
        'copies': [
            {'repo': 'ref/a', 'pull': 't1', 'pair': 1},
            {'repo': 'one/b-heretic', 'pull': 't1', 'pair': 2},
            {'repo': 'ara/c-abliterated', 'pull': 't1', 'pair': 3},
            {'repo': 'tiny/d', 'pull': 't1', 'pair': 4},
            {'repo': 'six/guard', 'pull': 't1', 'pair': 6},
        ],
    }
    (census / 'org-P.json').write_text(json.dumps(group))
    other = {'parent': 'org/Q', 'copies': [{'repo': 'q/one', 'pull': 't1', 'pair': 5}]}
    (census / 'org-Q.json').write_text(json.dumps(other))
    families = {'families': [
        {'parent': 'org/Q', 'members': ['q/one']},
        {'parent': 'org/P', 'members': ['ref/a', 'one/b-heretic', 'six/guard']},
    ]}
    path = census / 'families.json'
    path.write_text(json.dumps(families))
    return census, path


def build_guard_first(root):
    """Return build's census with six/guard listed first in org/P's copies."""
    census, families = build(root)
    path = census / 'org-P.json'
    group = json.loads(path.read_text())
    guard = next(copy for copy in group['copies'] if copy['repo'] == 'six/guard')
    group['copies'] = [guard] + [copy for copy in group['copies'] if copy is not guard]
    path.write_text(json.dumps(group))
    return census, families


def run(census, families, root, out, weights=None):
    stream = io.StringIO()
    errors = io.StringIO()
    extra = [] if weights is None else ['--weights', str(weights)]
    with contextlib.redirect_stdout(stream), contextlib.redirect_stderr(errors):
        code = direction_modes.main(
            ['--directions', str(census), '--pulls', str(root),
             '--families', str(families), '--out', str(out)] + extra)
    return code, stream.getvalue(), errors.getvalue()


def write_weights(folder):
    folder.mkdir(parents=True)
    report = {'tensors': {
        'model.layers.0.self_attn.o_proj.weight': {
            'changed': True, 'kind': 'attention_output',
            'first_singular_energy_share': 0.1},
        'model.layers.0.mlp.down_proj.weight': {
            'changed': True, 'kind': 'feed_forward_down',
            'first_singular_energy_share': 0.95},
    }}
    (folder / 'six-guard.json').write_text(json.dumps(report))
    return folder


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
            self.assertEqual(rows['six/guard']['mode'], 'arbitrary rank')
            self.assertEqual(rows['six/guard']['read_from'], 'o_proj')
            self.assertIsNone(rows['six/guard']['o_share'])
            self.assertIsNone(rows['six/guard']['down_share'])
            self.assertEqual(direction_modes.name_word('one/b-heretic'), 'heretic')
            self.assertEqual(direction_modes.name_word('ara/c-abliterated'), 'abliterated')
            self.assertEqual(direction_modes.name_word('tiny/d'), 'other')
            self.assertEqual(rows['ref/a']['family'], 1)
            self.assertEqual(rows['one/b-heretic']['family'], 1)
            self.assertEqual(rows['q/one']['family'], 1)
            self.assertEqual(rows['tiny/d']['family'], 'none')
            self.assertAlmostEqual(rows['ref/a']['pair'], 1.0, places=3)
            self.assertAlmostEqual(rows['one/b-heretic']['pair'], 0.0, places=3)
            self.assertIsNone(rows['ara/c-abliterated']['pair'])
            self.assertEqual(document['counts']['per layer'], 1)
            self.assertEqual(document['counts']['no file'], 0)
            self.assertEqual(document['by_name']['one direction']['heretic'], 1)
            self.assertEqual(document['by_name']['arbitrary rank']['abliterated'], 1)
            self.assertEqual(document['by_name']['arbitrary rank']['other'], 1)

            lines = out.read_text().splitlines()
            self.assertTrue(lines[0].startswith('# modes -- every census copy sorted'))
            self.assertEqual(lines[1], '')
            self.assertEqual(lines[2], 'copies 6: per layer 1, one direction 2, '
                                       'arbitrary rank 2, mixed 0, few layers 1, no file 0')
            family = next(line for line in lines if line.startswith('| org/P | 1 |'))
            self.assertEqual(family, '| org/P | 1 | 3 | 1 | 1 | 1 | 0 | 0 |')
            family_header = next(i for i, line in enumerate(lines)
                                 if line.startswith('| parent | family |'))
            family_table = [line for line in lines[family_header + 2:]
                            if line.startswith('| ')][:2]
            self.assertEqual(len(family_table), 2)
            self.assertEqual([line.split(' | ')[1] for line in family_table], ['1', '1'])
            header = next(i for i, line in enumerate(lines)
                          if line.startswith('| parent | copy |'))
            self.assertEqual(lines[header],
                             '| parent | copy | layers | window | own spread | adjacent '
                             '| far | pair | read from | o share | down share '
                             '| mode | family |')
            table = [line for line in lines[header + 2:] if line.startswith('| ')]
            self.assertEqual(len(table), 6)
            self.assertTrue(table[0].startswith('| org/P | ara/c-abliterated | 12 | 0..11 |'))
            self.assertIn('| arbitrary rank | none |', table[0])

    def test_weights_switch_the_read_to_down_proj(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / 'pulls'
            out = Path(tmp) / 'out' / 'modes.md'
            census, families = build(root)
            weights = write_weights(Path(tmp) / 'weights')
            code, _, _ = run(census, families, root, out, weights=weights)
            self.assertEqual(code, 0)
            document = json.loads(out.with_suffix('.json').read_text())
            rows = {row['repo']: row for row in document['copies']}
            self.assertEqual(rows['six/guard']['mode'], 'one direction')
            self.assertEqual(rows['six/guard']['read_from'], 'down_proj')
            self.assertAlmostEqual(rows['six/guard']['o_share'], 0.1, places=6)
            self.assertAlmostEqual(rows['six/guard']['down_share'], 0.95, places=6)
            self.assertEqual(rows['ara/c-abliterated']['read_from'], 'o_proj')
            self.assertIsNone(rows['ara/c-abliterated']['o_share'])
            self.assertIsNone(rows['ara/c-abliterated']['down_share'])
            self.assertEqual(rows['ara/c-abliterated']['mode'], 'arbitrary rank')
            self.assertEqual(document['counts']['one direction'], 3)
            self.assertEqual(document['counts']['arbitrary rank'], 1)
            self.assertIn('| read from | o share | down share |', out.read_text())

    def test_switched_copy_does_not_leak_into_the_next(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / 'pulls'
            out = Path(tmp) / 'out' / 'modes.md'
            census, families = build_guard_first(root)
            weights = write_weights(Path(tmp) / 'weights')
            code, _, _ = run(census, families, root, out, weights=weights)
            self.assertEqual(code, 0)
            document = json.loads(out.with_suffix('.json').read_text())
            rows = {row['repo']: row for row in document['copies']}
            self.assertEqual(rows['six/guard']['read_from'], 'down_proj')
            self.assertEqual(rows['one/b-heretic']['read_from'], 'o_proj')
            self.assertAlmostEqual(rows['one/b-heretic']['pair'], 0.0, delta=1e-6)

    def test_own_output_in_census_folder_is_skipped(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / 'pulls'
            out = Path(tmp) / 'out' / 'modes.md'
            census, families = build(root)
            stale = {'counts': {}, 'copies': [
                {'parent': 'org/P', 'repo': 'ref/a', 'mode': 'per layer'}]}
            (census / 'modes.json').write_text(json.dumps(stale))
            code, _, _ = run(census, families, root, out)
            self.assertEqual(code, 0)
            first = json.loads(out.with_suffix('.json').read_text())
            self.assertEqual(len(first['copies']), 6)

            code, _, _ = run(census, families, root, census / 'modes.md')
            self.assertEqual(code, 0)
            again = json.loads((census / 'modes.json').read_text())
            self.assertEqual(len(again['copies']), len(first['copies']))


if __name__ == '__main__':
    unittest.main()
