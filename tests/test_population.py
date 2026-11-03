# test_population.py -- Rebuild the population header's counts from the weights reports, so no sum is carried by hand.
# Created by SDE
from pathlib import Path
import subprocess
import sys
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
        self.assertEqual(population.publishers(PUBLISHERS), {'google', 'mistralai', 'essentialai'})
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


if __name__ == '__main__':
    unittest.main()
