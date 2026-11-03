# test_place_round.py -- Check the placement of a round's new copies against the census, the markdown and json, and a missing measurements folder.
# Created by SDE
# Modified: SDE 2026-11-03  two new pairs, one placed and one under a new parent.
# Modified: SDE 2026-11-03  a flipped census copy and a flipped new pair, both read at median 1.000.
# Modified: SDE 2026-11-03  a parent whose only census copy carries one direction, placed with no best layer.
# Modified: SDE 2026-11-03  the reference is a per-layer copy (9 degrees a layer); a parent with no per-layer copy reads "none (no per-layer copy)".
# Modified: SDE 2026-11-03  --batches: same, different and missing weight-file checksums; without it every row reads "none".
# Modified: SDE 2026-11-03  a pair read from down_proj by its weights.json with and without --weights, and a pair read from o_proj.
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


def down_key(layer):
    return f'model.layers.{layer}.mlp.down_proj.weight.left'


def write_copy(root, pull, pair, tensors, down=None):
    folder = root / pull / 'measurements' / f'pair-{pair}'
    folder.mkdir(parents=True)
    saved = {key(layer): value.float() for layer, value in tensors.items()}
    if down is not None:
        saved.update({down_key(layer): value.float() for layer, value in down.items()})
    save_file(saved, str(folder / 'weights.directions.safetensors'))


def write_weights(folder, o_share, down_share):
    folder.mkdir(parents=True, exist_ok=True)
    (folder / 'weights.json').write_text(json.dumps({'tensors': {
        'model.layers.0.self_attn.o_proj.weight': {
            'changed': True, 'kind': 'attention_output',
            'first_singular_energy_share': o_share},
        'model.layers.0.mlp.down_proj.weight': {
            'changed': True, 'kind': 'feed_forward_down',
            'first_singular_energy_share': down_share},
    }}))


def write_metadata(folder, copy, parent):
    folder.mkdir(parents=True, exist_ok=True)
    meta = {'modified': {'repo': copy}, 'original': {'repo': parent}}
    (folder / 'metadata.json').write_text(json.dumps(meta))


def build(root):
    reference = {layer: at(layer * 9) for layer in range(12)}
    write_copy(root, 't1', 1, reference)
    write_copy(root, 't1', 2, {layer: reference[7] for layer in range(5, 13)})
    write_copy(root, 'flip', 3, {layer: -reference[7] for layer in range(5, 13)})
    write_copy(root, 'single', 4, {layer: reference[7] for layer in range(2, 10)})
    write_copy(root, 'down', 5, {layer: basis(layer + 2) for layer in range(5, 9)},
               down={layer: at(layer * 9) for layer in range(5, 9)})

    census = Path(root) / 'census'
    census.mkdir()
    (census / 'org-P.json').write_text(json.dumps({
        'parent': 'org/P',
        'copies': [
            {'repo': 'ref/a', 'pull': 't1', 'pair': 1},
            {'repo': 'one/b', 'pull': 't1', 'pair': 2},
            {'repo': 'flip/d', 'pull': 'flip', 'pair': 3},
            {'repo': 'down/f', 'pull': 'down', 'pair': 5},
        ],
    }))
    (census / 'org-R.json').write_text(json.dumps({
        'parent': 'org/R',
        'copies': [
            {'repo': 'single/e', 'pull': 'single', 'pair': 4},
        ],
    }))
    families = Path(root) / 'families.json'
    families.write_text(json.dumps({
        'families': [{'parent': 'org/P',
                      'members': ['ref/a', 'one/b', 'flip/d', 'down/f']},
                     {'parent': 'org/R', 'members': ['single/e']}],
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
    pair3 = round_dir / 'pair-3'
    write_metadata(pair3, 'new/z', 'org/P')
    save_file({key(layer): (-reference[7]).float() for layer in range(5, 13)},
              str(pair3 / 'weights.directions.safetensors'))
    pair4 = round_dir / 'pair-4'
    write_metadata(pair4, 'new/w', 'org/R')
    save_file({key(layer): reference[7].float() for layer in range(2, 10)},
              str(pair4 / 'weights.directions.safetensors'))
    pair5 = round_dir / 'pair-5'
    write_metadata(pair5, 'new/v', 'org/P')
    save_file({key(layer): reference[7].float() for layer in range(5, 13)},
              str(pair5 / 'weights.directions.safetensors'))
    pair6 = round_dir / 'pair-6'
    write_metadata(pair6, 'new/u', 'org/P')
    save_file({key(layer): basis(layer + 2).float() for layer in range(5, 9)},
              str(pair6 / 'weights.directions.safetensors'))
    write_weights(pair6, 0.1, 0.95)
    pair7 = round_dir / 'pair-7'
    write_metadata(pair7, 'new/t', 'org/P')
    save_file({key(layer): basis(layer + 2).float() for layer in range(5, 9)},
              str(pair7 / 'weights.directions.safetensors'))

    batches = Path(root) / 'batches'
    batches.mkdir()
    (batches / 'round-1-batch-1.json').write_text(json.dumps({'pairs': [
        {'modified': {'hub_id': 'one/b', 'revision': 'r1',
                      'weight_files_sha256': {'a.safetensors': 'aa',
                                              'b.safetensors': 'bb'}},
         'original': {'hub_id': 'org/P', 'revision': 'r0'}},
        {'modified': {'hub_id': 'new/x', 'revision': 'r2',
                      'weight_files_sha256': {'a.safetensors': 'aa',
                                              'b.safetensors': 'bb'}},
         'original': {'hub_id': 'org/P', 'revision': 'r0'}},
    ]}))
    (batches / 'round-2-batch-1.json').write_text(json.dumps({'pairs': [
        {'modified': {'hub_id': 'new/z', 'revision': 'r3',
                      'weight_files_sha256': {'a.safetensors': 'cc'}},
         'original': {'hub_id': 'org/P', 'revision': 'r0'}},
    ]}))
    return census, families, round_dir, batches


def run(round_dir, census, families, out, batches=None, weights=None):
    stream = io.StringIO()
    errors = io.StringIO()
    argv = ['--measurements', str(round_dir), '--directions', str(census),
            '--families', str(families), '--pulls', str(round_dir.parent),
            '--out', str(out)]
    if batches is not None:
        argv += ['--batches', str(batches)]
    if weights is not None:
        argv += ['--weights', str(weights)]
    with contextlib.redirect_stdout(stream), contextlib.redirect_stderr(errors):
        code = place_round.main(argv)
    return code, stream.getvalue(), errors.getvalue()


class PlaceRoundTest(unittest.TestCase):

    def test_placement(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            census, families, round_dir, batches = build(root)
            out = root / 'out' / 'round-54.md'
            code, _, _ = run(round_dir, census, families, out, batches)
            self.assertEqual(code, 0)
            document = json.loads(out.with_suffix('.json').read_text())
            rows = {row['copy']: row for row in document['rows']}
            self.assertEqual(len(document['rows']), 7)
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
            self.assertEqual(placed['checksums'], 'same weight files')

            flipped = rows['new/z']
            self.assertEqual(flipped['parent'], 'org/P')
            self.assertEqual(flipped['partner'], 'one/b')
            self.assertAlmostEqual(flipped['median'], 1.0, places=6)
            self.assertEqual(flipped['keys'], 8)
            self.assertEqual(flipped['family'], 1)
            self.assertEqual(flipped['checksums'], 'different weight files')

            missing = rows['new/v']
            self.assertEqual(missing['parent'], 'org/P')
            self.assertEqual(missing['partner'], 'one/b')
            self.assertAlmostEqual(missing['median'], 1.0, places=6)
            self.assertEqual(missing['checksums'], 'checksums missing for copy')

            fresh = rows['new/y']
            self.assertEqual(fresh['parent'], 'org/Q')
            self.assertEqual(fresh['note'], 'new parent')
            self.assertIsNone(fresh['partner'])
            self.assertIsNone(fresh['best_layer'])
            self.assertEqual(fresh['family'], 'none')
            self.assertEqual(fresh['checksums'], 'none')

            single = rows['new/w']
            self.assertEqual(single['parent'], 'org/R')
            self.assertEqual(single['reference'], 'none (no per-layer copy)')
            self.assertIsNone(single['best_layer'])
            self.assertIsNone(single['cos'])
            self.assertEqual(single['window'], [2, 9])
            self.assertAlmostEqual(single['own_spread'], 1.0, places=6)
            self.assertEqual(single['partner'], 'single/e')
            self.assertAlmostEqual(single['median'], 1.0, places=6)
            self.assertEqual(single['family'], 1)
            self.assertEqual(single['checksums'], 'checksums missing for both')

    def test_checksums_without_batches(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            census, families, round_dir, _ = build(root)
            out = root / 'out' / 'round-54.md'
            code, _, _ = run(round_dir, census, families, out)
            self.assertEqual(code, 0)
            document = json.loads(out.with_suffix('.json').read_text())
            self.assertEqual(len(document['rows']), 7)
            for row in document['rows']:
                self.assertEqual(row['checksums'], 'none')

    def test_markdown_rows(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            census, families, round_dir, batches = build(root)
            out = root / 'out' / 'round-54.md'
            run(round_dir, census, families, out, batches)
            lines = out.read_text().splitlines()
            self.assertEqual(
                lines[0],
                '# round-54 -- new copies placed against the census of saved directions.')
            self.assertEqual(lines[1], '')
            table = [line for line in lines[4:] if line.startswith('| ')]
            self.assertEqual(len(table), 7)
            rows = {line.split(' | ')[0][2:]: line for line in table}
            self.assertTrue(rows['new/x'].startswith(
                '| new/x | org/P | one/b | 1.000 | 8 | 1 | 5..12 | 1.000 | 7 | 1.000 '
                '| ref/a | o_proj | same weight files |'))
            self.assertTrue(rows['new/y'].startswith(
                '| new/y | org/Q | none | none | none | none | none | none | none | none '
                '| none | none | none | new parent |'))
            self.assertTrue(rows['new/z'].startswith(
                '| new/z | org/P | one/b | 1.000 | 8 | 1 | 5..12 | 1.000 | 7 | 1.000 '
                '| ref/a | o_proj | different weight files |'))
            self.assertTrue(rows['new/w'].startswith(
                '| new/w | org/R | single/e | 1.000 | 8 | 1 | 2..9 | 1.000 | none | none '
                '| none (no per-layer copy) | o_proj | checksums missing for both |'))
            self.assertTrue(rows['new/v'].startswith(
                '| new/v | org/P | one/b | 1.000 | 8 | 1 | 5..12 | 1.000 | 7 | 1.000 '
                '| ref/a | o_proj | checksums missing for copy |'))
            self.assertTrue(rows['new/u'].startswith(
                '| new/u | org/P | down/f | 1.000 | 4 | 1 | none | none | none | none '
                '| ref/a | down_proj | checksums missing for both |'))
            self.assertTrue(rows['new/t'].startswith(
                '| new/t | org/P | down/f | 1.000 | 4 | 1 | 5..8 | 0.000 | 0 | 0.000 '
                '| ref/a | o_proj | checksums missing for both |'))

    def test_read_from_down_proj(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            census, families, round_dir, batches = build(root)
            empty = root / 'no-reports'
            empty.mkdir()
            documents = []
            for weights in (None, empty):
                out = root / 'out' / 'round-54.md'
                code, _, _ = run(round_dir, census, families, out, batches, weights)
                self.assertEqual(code, 0)
                documents.append(json.loads(out.with_suffix('.json').read_text()))
            for document in documents:
                rows = {row['copy']: row for row in document['rows']}
                self.assertEqual(rows['new/u']['read_from'], 'down_proj')
                self.assertGreater(rows['new/u']['median'], 0.98)
                self.assertIsNone(rows['new/u']['window'])
                self.assertEqual(rows['new/t']['window'], [5, 8])
                self.assertEqual(rows['new/t']['read_from'], 'o_proj')
                self.assertLess(rows['new/t']['own_spread'], 0.01)
            first = {row['copy']: row['reference'] for row in documents[0]['rows']}
            second = {row['copy']: row['reference'] for row in documents[1]['rows']}
            self.assertEqual(first, second)

    def test_constants(self):
        self.assertEqual(place_round.PER_LAYER_ADJACENT, 0.5)
        self.assertEqual(place_round.PER_LAYER_FAR, 0.2)

    def test_missing_measurements(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            census, families, round_dir, _ = build(root)
            out = root / 'out' / 'round-54.md'
            code, _, errors = run(root / 'absent', census, families, out)
            self.assertEqual(code, 2)
            self.assertEqual(len(errors.splitlines()), 1)


if __name__ == '__main__':
    unittest.main()
