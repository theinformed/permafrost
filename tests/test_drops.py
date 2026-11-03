# test_drops.py -- Read the pad's drop files for a round into one table: job, kind, event, exit, judgement line, time.
# Created by SDE
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'hpc'))
import drops

DIR = ROOT / 'tests/fixtures/drops/wheat'
COMPARE = DIR / '20261103T004530Z-387624-drop.txt'
KIT = DIR / '20261102T232108Z-round-51-kit-1839902-drop.txt'


class ParseTests(unittest.TestCase):
    def test_a_compare_drop_gives_its_header_and_judgement(self):
        row = drops.parse(COMPARE)
        self.assertEqual(row['job'], '387624')
        self.assertEqual(row['round'], 51)
        self.assertEqual(row['system'], 'wheat')
        self.assertEqual(row['host'], 'wheat-r15-cp39a')
        self.assertEqual(row['event'], 'finished')
        self.assertEqual(row['exit'], 0)
        self.assertEqual(row['when'], '2026-11-03T00:45:28Z')
        self.assertEqual(row['kind'], 'compare')
        self.assertEqual(row['what'], 'Compare checkpoint pair 1 on CPU')
        self.assertEqual(row['judgement'], 'consistent with re-save noted')

    def test_the_other_compare_reads_unexplained_differences(self):
        row = drops.parse(DIR / '20261103T003858Z-387625-drop.txt')
        self.assertEqual((row['job'], row['kind'], row['judgement']), ('387625', 'compare', 'unexplained differences'))

    def test_a_kit_drop_is_kind_kit_with_its_upper_case_line(self):
        row = drops.parse(KIT)
        self.assertEqual(row['kind'], 'kit')
        self.assertEqual(row['job'], 'round-51-kit-1839902')
        self.assertEqual(row['judgement'], 'kit OK')
        self.assertEqual(row['exit'], 0)

    def test_a_drop_without_a_judgement_line_gives_none(self):
        row = drops.parse(DIR / '20261103T001903Z-387623-drop.txt')
        self.assertEqual(row['job'], '387623')
        self.assertIsNone(row['judgement'])


class TableTests(unittest.TestCase):
    def test_latest_finds_the_newest_drop_for_a_job(self):
        self.assertEqual(drops.latest(DIR, '387624'), COMPARE)
        self.assertIsNone(drops.latest(DIR, '999999'))

    def test_table_keeps_the_order_asked_and_marks_missing_jobs(self):
        rows = drops.table(DIR, ['387625', '999999', '387624'])
        self.assertEqual([r['job'] for r in rows], ['387625', '999999', '387624'])
        self.assertIsNone(rows[1]['event'])
        self.assertEqual(rows[0]['judgement'], 'unexplained differences')

    def test_round_lists_every_drop_of_that_round_by_time(self):
        rows = drops.for_round(DIR, 51)
        self.assertEqual([r['job'] for r in rows], ['round-51-kit-1839902', '387623', '387625', '387624'])


class CommandTests(unittest.TestCase):
    def test_command_prints_one_line_per_job_with_dashes_for_missing(self):
        out = subprocess.run([sys.executable, str(ROOT / 'hpc/drops.py'), str(DIR), '387624', '999999'],
                             capture_output=True, text=True, check=True).stdout.splitlines()
        self.assertEqual(out[0].split('\t'), ['387624', 'compare', 'finished', '0', 'consistent with re-save noted', '2026-11-03T00:45:28Z'])
        self.assertEqual(out[1].split('\t'), ['999999', '-', '-', '-', '-', '-'])

    def test_command_round_flag_lists_the_round(self):
        out = subprocess.run([sys.executable, str(ROOT / 'hpc/drops.py'), str(DIR), '--round', '51'],
                             capture_output=True, text=True, check=True).stdout.splitlines()
        self.assertEqual(len(out), 4)
        self.assertTrue(out[0].startswith('round-51-kit-1839902\tkit\t'))


if __name__ == '__main__':
    unittest.main()
