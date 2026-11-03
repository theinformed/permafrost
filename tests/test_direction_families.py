# test_direction_families.py -- Check the counts, families, classes, single-direction rows and sign note.
# Created by SDE
# Modified: SDE 2026-11-03  two parents, six copies, three weights reports, an empty folder.
import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'hpc'))

import direction_families  # noqa: E402

KEYS = [
    'model.layers.0.mlp.down_proj.weight.left',
    'model.layers.0.mlp.down_proj.weight.right',
    'model.layers.1.mlp.down_proj.weight.left',
    'model.layers.1.mlp.down_proj.weight.right',
    'model.layers.0.self_attn.o_proj.weight.left',
    'model.layers.0.self_attn.o_proj.weight.right',
]
NAMES = [
    'model.layers.0.mlp.down_proj.weight',
    'model.layers.1.mlp.down_proj.weight',
    'model.layers.0.self_attn.o_proj.weight',
]
A = 'm/a-heretic'
B = 'm/b-heretic'
C = 'm/c-abliterated'
D = 'm/d-uncensored'
E = 'm/e-heretic'
F = 'm/f-other'


def row(a, b, values):
    cosines = [[key, value] for key, value in zip(KEYS, values)]
    return {
        'copy_a': a,
        'copy_b': b,
        'pull_a': 'p1',
        'pull_b': 'p1',
        'shared_keys': len(KEYS),
        'identical': 0,
        'same_repo': False,
        'right': {'cosines': cosines, 'kind_medians': {}},
        'left': {'cosines': cosines, 'kind_medians': {}},
        'kind_medians': {},
    }


def group(parent, repos, rows):
    return {
        'parent': parent,
        'copies': [{'repo': repo, 'pull': 'p1', 'pair': 1, 'keys': len(KEYS)} for repo in repos],
        'comparisons': rows,
    }


class DirectionFamiliesTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.directions = self.root / 'directions'
        self.weights = self.root / 'weights'
        self.directions.mkdir()
        self.weights.mkdir()
        p = group('P', [A, B, C, D], [
            row(A, B, [0.95, -0.95, 0.95, -0.95, 0.95, -0.95]),
            row(A, C, [0.02] * 6),
            row(B, C, [0.02] * 6),
            row(A, D, [0.6] * 6),
            row(B, D, [0.1] * 6),
            row(C, D, [0.1] * 6),
        ])
        q = group('Q', [E, F], [row(E, F, [0.99] * 4 + [0.0, 0.0])])
        (self.directions / 'P.json').write_text(json.dumps(p))
        (self.directions / 'Q.json').write_text(json.dumps(q))
        for repo in (A, B, C):
            tensors = {}
            for at, name in enumerate(NAMES):
                tensors[name] = {'first_singular_energy_share': 0.99 if at < 2 else 0.5, 'changed': True}
            report = {'tensors': tensors}
            (self.weights / (repo.replace('/', '-') + '.json')).write_text(json.dumps(report))
        self.out = self.root / 'out' / 'report.md'

    def tearDown(self):
        self.tmp.cleanup()

    def run_main(self, directions=None):
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            code = direction_families.main([
                '--directions', str(directions or self.directions),
                '--weights', str(self.weights),
                '--out', str(self.out),
            ])
        return code, stream.getvalue()

    def report(self):
        code, text = self.run_main()
        self.assertEqual(code, 0)
        self.assertTrue(self.out.exists())
        self.assertTrue(self.out.with_suffix('.json').exists())
        self.assertEqual(len(text.strip().splitlines()), 2)
        return json.loads(self.out.with_suffix('.json').read_text())

    def test_counts(self):
        report = self.report()
        counts = report['counts']
        self.assertEqual(counts['rows'], 7)
        self.assertEqual(counts['skipped'], 0)
        self.assertEqual(counts['reports_missing'], 3)
        self.assertEqual(counts['parents'], 2)
        self.assertEqual(counts['copies'], 6)

    def test_families_and_alone(self):
        report = self.report()
        families = [(entry['parent'], entry['members']) for entry in report['families']]
        self.assertEqual(families, [('P', [A, B]), ('Q', [E, F])])
        parents = {entry['parent']: entry for entry in report['parents']}
        self.assertEqual(parents['P']['alone'], [C])

    def test_classes(self):
        report = self.report()
        pairs = {(entry['class_a'], entry['class_b']): entry for entry in report['classes']}
        self.assertEqual(pairs[('heretic', 'heretic')]['rows'], 1)
        self.assertEqual(pairs[('heretic', 'other')]['rows'], 1)

    def test_single(self):
        report = self.report()
        single = report['single']
        self.assertEqual(single['kept'], 3)
        self.assertEqual(single['drop_missing'], 4)
        self.assertEqual(single['drop_few'], 0)
        kept = {(entry['class_a'], entry['class_b']): entry for entry in single['classes']}
        self.assertEqual(kept[('heretic', 'heretic')]['median'], 0.95)
        self.assertEqual(kept[('abliterated', 'heretic')]['median'], 0.02)

    def test_sign_note(self):
        report = self.report()
        self.assertEqual(report['sign']['rows'], ['%s ~ %s' % (A, B)])
        self.assertEqual(report['sign']['count'], 1)

    def test_empty_folder(self):
        empty = self.root / 'empty'
        empty.mkdir()
        code, text = self.run_main(empty)
        self.assertEqual(code, 1)
        self.assertEqual(text, '')


if __name__ == '__main__':
    unittest.main()
