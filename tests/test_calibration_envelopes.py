# test_calibration_envelopes.py -- Check the measured pass lines for Mistral Small 3.2.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-29  the recipe table carries both pass lines unchanged.
"""The calibration file must match its tracked reports and admit both of our own edits."""

import copy
import json
import math
import re
import statistics
import unittest
from pathlib import Path

from audit.weights import recipe_table, score_report

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'audit/calibration/mistral-small-3.2-24b.json'
KINDS = ('attention_output', 'feed_forward_down')
RUNS = ('single-projection', 'norm-preserving')
MEASURES = {
    'first_energy_share': lambda r: r['first_singular_energy_share'],
    'second_to_first_singular_value': lambda r: r['singular_values'][1] / r['singular_values'][0],
    'direction_cosine': lambda r: r['direction_cosine'],
    'relative_difference': lambda r: r['relative_difference'],
    'residual_relative': lambda r: r['difference_norm'] * math.sqrt(1 - r['first_singular_energy_share']) / r['original_norm'],
    'row_norm_max_relative_error': lambda r: r['row_norms']['max_relative_error'],
    'entries_unchanged_fraction': lambda r: 1 - r['positive_fraction'] - r['negative_fraction'],
}


def changed(report, kind):
    return [row for row in report['tensors'].values() if row['changed'] and row['kind'] == kind]


class CalibrationEnvelopeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(DATA.read_text())
        cls.reports = {run: json.loads((ROOT / cls.data['runs'][run]['report']).read_text()) for run in RUNS}

    def test_shape_and_base(self):
        data = self.data
        self.assertEqual(data['purpose'], 'calibration')
        self.assertEqual(data['created_by'], 'Sean Egan')
        self.assertTrue(re.fullmatch(r'[0-9a-f]{40}', data['base_revision']))
        self.assertEqual(len(data['base_shards_sha256']), 10)
        for digest in data['base_shards_sha256'].values():
            self.assertTrue(re.fullmatch(r'[0-9a-f]{64}', digest))
        for run in RUNS:
            self.assertEqual(self.reports[run]['original']['shards_sha256'], data['base_shards_sha256'])
            self.assertEqual(set(data['envelopes'][run]), set(KINDS))
            for kind in KINDS:
                self.assertEqual(set(data['envelopes'][run][kind]), set(MEASURES))
                for name, span in data['envelopes'][run][kind].items():
                    self.assertEqual(span['n'], 40, (run, kind, name))
                    self.assertLessEqual(span['min'], span['median'])
                    self.assertLessEqual(span['median'], span['max'])

    def test_envelopes_recompute_from_reports(self):
        for run in RUNS:
            for kind in KINDS:
                rows = changed(self.reports[run], kind)
                for name, measure in MEASURES.items():
                    values = [measure(row) for row in rows]
                    span = self.data['envelopes'][run][kind][name]
                    self.assertEqual(len(values), span['n'])
                    self.assertAlmostEqual(min(values), span['min'], places=12)
                    self.assertAlmostEqual(statistics.median(values), span['median'], places=12)
                    self.assertAlmostEqual(max(values), span['max'], places=12)

    def test_recorded_flags_match_the_reports(self):
        for run in RUNS:
            report = self.reports[run]
            record = self.data['flags_under_analytic_line'][run]
            violations = report['recipe_matching']['violations']
            self.assertEqual(len(violations), record['count'])
            self.assertTrue(all(item['rule'] == record['rule'] and item['minimum'] == record['minimum'] for item in violations))
            kinds = {}
            for item in violations:
                kind = report['tensors'][item['tensor']]['kind']
                kinds[kind] = kinds.get(kind, 0) + 1
            self.assertEqual(kinds, record['by_kind'])
        self.assertEqual(self.data['flags_under_analytic_line']['single-projection']['count'], 68)

    def test_pass_lines_admit_every_known_clean_tensor(self):
        lines = self.data['pass_lines']
        for run in RUNS:
            line = lines[run + '/mistral-small-3.2-24b']
            self.assertEqual(line['base_shards_sha256'], self.data['base_shards_sha256'])
            for kind in KINDS:
                envelope = self.data['envelopes'][run][kind]
                self.assertLess(line['first_energy_min'], envelope['first_energy_share']['min'])
                self.assertLess(line['direction_cosine_min'], envelope['direction_cosine']['min'])
                self.assertGreater(line['residual_relative_max'], envelope['residual_relative']['max'])
        row_line = lines['norm-preserving/mistral-small-3.2-24b']['row_norm_max_relative_error_max']
        for kind in KINDS:
            self.assertGreater(row_line, self.data['envelopes']['norm-preserving'][kind]['row_norm_max_relative_error']['max'])
            self.assertLess(row_line, self.data['envelopes']['single-projection'][kind]['row_norm_max_relative_error']['min'])

    def test_scorer_matches_both_edits_under_the_single_projection_line(self):
        name = 'single-projection/mistral-small-3.2-24b'
        table = copy.deepcopy(recipe_table())
        table[name] = self.data['pass_lines'][name]
        for run in RUNS:
            report = score_report(copy.deepcopy(self.reports[run]), table)
            candidate = next(item for item in report['recipe_matching']['candidates'] if item['recipe'] == name)
            self.assertEqual(candidate['violations'], [], run)
            self.assertNotIn(name, report['recipe_matching']['outside_calibrated_base'])

    def test_recipe_table_carries_both_pass_lines(self):
        table = recipe_table()
        for name, line in self.data['pass_lines'].items():
            self.assertEqual(table[name], line, name)
        self.assertEqual(table['single-projection/mistral-small-3.2-24b']['status'], 'measured')
        self.assertNotEqual(table['norm-preserving/mistral-small-3.2-24b']['status'], 'measured')


if __name__ == '__main__':
    unittest.main()
