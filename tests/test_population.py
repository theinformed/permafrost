# test_population.py -- Rebuild the population header's counts from the weights reports, so no sum is carried by hand.
# Created by SDE
# Modified: SDE add cases for the early reports, second passes and the judged lists.
from pathlib import Path
import json
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'hpc'))
import population

FIX = ROOT / 'tests/fixtures/population'
PUBLISHERS = ROOT / 'data/publishers.txt'


class RowTests(unittest.TestCase):
    def test_every_report_gives_a_row_and_reports_without_a_census_block_are_marked(self):
        rows = population.reports(FIX)
        self.assertEqual(len(rows), 5)
        by_file = {r['file']: r for r in rows}
        self.assertIsNone(by_file['calibration-x.json']['copy'])
        row = by_file['Beta-copy-two.json']
        self.assertEqual((row['copy'], row['original'], row['round']), ('Beta/copy-two', 'google/gemma-x', 47))
        self.assertEqual(row['outside_max'], 0.0007)
        self.assertEqual(row['assessment'], 'recipe_violations')
        self.assertEqual(row['nearest_recipe'], 'single-projection-selected')
        self.assertFalse(row['matched'])
        self.assertEqual(row['changed'], 2)
        self.assertIsNone(row['same_weights_as'])
        self.assertEqual(by_file['Gamma-copy-three.json']['same_weights_as'], 'Alpha/copy-one')

    def test_publishers_are_read_from_the_list_in_lower_case(self):
        self.assertEqual(population.publishers(PUBLISHERS), {'google', 'mistralai', 'essentialai', 'qwen'})
        rows = {r['file']: r for r in population.reports(FIX)}
        self.assertTrue(population.is_publisher(rows['Alpha-copy-one.json'], {'google'}))
        self.assertFalse(population.is_publisher(rows['Gamma-copy-three.json'], {'google'}))


class CountTests(unittest.TestCase):
    def test_counts_follow_the_stated_rules(self):
        counts = population.counts(population.reports(FIX), {'google', 'mistralai'})
        self.assertEqual(counts['reports'], 5)
        self.assertEqual(counts['measurements'], 4)
        self.assertEqual(counts['distinct_copies'], 3)
        self.assertEqual(counts['repeated_measurements'], 1)
        self.assertEqual(counts['originals'], 1)
        self.assertEqual(counts['community_parents'], 1)
        self.assertEqual(counts['copies_on_community_parents'], 1)
        self.assertEqual(counts['re_uploads'], 1)
        self.assertEqual(counts['exactly_zero_outside'], 3)
        self.assertEqual(counts['without_census_block'], 1)
        self.assertEqual(counts['original_ids'], ['google/gemma-x'])
        self.assertEqual(counts['community_parent_ids'], ['Comm/parent-ft'])


class CommandTests(unittest.TestCase):
    def test_command_prints_counts_as_tab_separated_lines(self):
        out = subprocess.run([sys.executable, str(ROOT / 'hpc/population.py'), '--root', str(FIX), '--publishers', str(PUBLISHERS)],
                             capture_output=True, text=True, check=True).stdout
        lines = dict(line.split('\t', 1) for line in out.splitlines() if '\t' in line)
        self.assertEqual(lines['measurements'], '4')
        self.assertEqual(lines['distinct_copies'], '3')
        self.assertEqual(lines['originals'], '1')

    def test_table_flag_prints_one_row_per_report_with_a_header(self):
        out = subprocess.run([sys.executable, str(ROOT / 'hpc/population.py'), '--root', str(FIX), '--publishers', str(PUBLISHERS), '--table'],
                             capture_output=True, text=True, check=True).stdout.splitlines()
        self.assertEqual(len(out), 6)
        self.assertTrue(out[0].startswith('file\tround\tcopy\toriginal\tpublisher\toutside_max'))


def _report(folder, name, modified, original, outside=0.0, census=None):
    data = {'schema_version': 1, 'modified': {'source': modified}, 'original': {'source': original},
            'summary': {'max_relative_difference_outside_changed_set': outside}}
    if census:
        data['census'] = census
    (folder / name).write_text(json.dumps(data), encoding='utf-8')


def _census(copy, original, **extra):
    return {'modified': dict({'hub_id': copy}, **extra), 'original': {'hub_id': original}}


class ExtendedTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        weights = self.root / 'results' / 'weights'
        weights.mkdir(parents=True)
        # An early report: no census block, hub ids as sources.
        _report(weights, 'Owner-early.json', 'Owner/early', 'Qwen/base-x')
        # A second pass over the same two folders, and a measurement against a parent.
        _report(weights, 'A-one.json', '/w/rounds/2/derived/pair-1', '/w/originals/g', 0.0,
                _census('A/one', 'google/gemma-x'))
        _report(weights, 'A-one.pass-2.json', '/w/rounds/2/derived/pair-1', '/w/originals/g', 0.0,
                _census('A/one', 'google/gemma-x'))
        _report(weights, 'A-one.vs-parent.json', '/w/rounds/35/derived/pair-1', '/w/rounds/35/originals/p', 0.0,
                _census('A/one', 'Comm/parent', same_weights_as={'hub_id': 'A/one', 'round': 2}))
        # A duplicate, a copy with a small outside value and a calibration report.
        _report(weights, 'B-dup.json', '/w/rounds/5/derived/pair-1', '/w/rounds/5/originals/g', 0.0,
                _census('B/dup', 'google/gemma-x', duplicate_of='A/one'))
        _report(weights, 'C-small.json', '/w/rounds/5/derived/pair-2', '/w/rounds/5/originals/g', 0.0004,
                _census('C/small', 'google/gemma-x'))
        _report(weights, 'calibration-y.json', '/w/rounds/1/derived/x', '/w/originals/x')
        self.rows = population.reports(self.root)

    def tearDown(self):
        self.tmp.cleanup()

    def test_early_reports_name_their_copy_and_second_passes_fold(self):
        counts = population.counts(self.rows, {'google', 'qwen'})
        self.assertEqual(counts['reports'], 7)
        self.assertEqual(counts['second_passes'], 1)
        self.assertEqual(counts['measurements'], 5)
        self.assertEqual(counts['distinct_copies'], 4)
        self.assertEqual(counts['repeated_measurements'], 1)
        self.assertEqual(counts['copies_on_two_originals'], 1)
        self.assertEqual(counts['originals'], 2)
        self.assertEqual(counts['original_ids'], ['Qwen/base-x', 'google/gemma-x'])
        self.assertEqual(counts['copies_on_community_parents'], 1)
        self.assertEqual(counts['copies_only_on_community_parents'], 0)
        self.assertEqual(counts['re_uploads'], 1)
        self.assertEqual(counts['without_census_block'], 2)

    def test_judged_lists_combine_with_the_reports(self):
        lists = {name: [] for name in population.GROUPS}
        lists['not-read'] = ['B/dup']
        lists['training'] = ['Owner/early']
        lists['small-outside'] = ['C/small']
        out = population.judged(self.rows, lists)
        self.assertEqual((out['read'], out['matching'], out['ablations']), (3, 3, 2))
        self.assertEqual((out['matching_zero_outside'], out['matching_other_nonzero']), (2, 0))
        self.assertEqual(out['problems'], [])
        lists['small-outside'] = ['A/one', 'Z/unknown']
        problems = population.judged(self.rows, lists)['problems']
        self.assertIn('small-outside: Z/unknown is not a measured copy', problems)
        self.assertIn('small-outside: A/one is not a matching copy with a nonzero outside value', problems)

    def test_command_reads_the_lists_and_fails_on_a_problem(self):
        folder = self.root / 'data' / 'population'
        folder.mkdir(parents=True)
        (folder / 'not-read.txt').write_text('# header\nB/dup\n', encoding='utf-8')
        command = [sys.executable, str(ROOT / 'hpc/population.py'), '--root', str(self.root), '--publishers', str(PUBLISHERS)]
        done = subprocess.run(command, capture_output=True, text=True)
        lines = dict(line.split('\t', 1) for line in done.stdout.splitlines() if '\t' in line)
        self.assertEqual(done.returncode, 0)
        self.assertEqual((lines['read'], lines['listed_not-read']), ('3', '1'))
        (folder / 'training.txt').write_text('Z/unknown\n', encoding='utf-8')
        self.assertEqual(subprocess.run(command, capture_output=True, text=True).returncode, 1)


if __name__ == '__main__':
    unittest.main()
