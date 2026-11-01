# test_pin_census.py -- Check the pinner's duplicate check against a stubbed hub listing.
# Created by Sean Egan
import contextlib
from datetime import datetime, timezone
import io
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'hpc'))
import pin_census
from pin_census import Duplicate, measured_copies, pin, same_weights

CREATED = datetime(2026, 1, 2, tzinfo=timezone.utc)
SHA_A = 'a' * 64
SHA_B = 'b' * 64
KNOWN = [{'hub_id': 'first/copy', 'state': 'measured', 'round': 8, 'sha256': {SHA_A}},
         {'hub_id': 'third/copy', 'state': 'measured', 'round': 19, 'sha256': {SHA_A}}]


def api(first_title, sha=SHA_A):
    """A hub whose copy has one weight file and a first commit with the given title."""
    history = [SimpleNamespace(commit_id='a' * 40, created_at=datetime(2026, 1, 1, tzinfo=timezone.utc), title='Upload')]
    siblings = [SimpleNamespace(rfilename='model.safetensors', lfs=SimpleNamespace(sha256=sha, size=1, pointer_size=1)),
                SimpleNamespace(rfilename='config.json', lfs=None)]

    class API:
        def model_info(self, repo, revision=None, **kwargs):
            card = {'base_model': 'publisher/base'} if repo == 'owner/copy' else {}
            return SimpleNamespace(sha=revision or 'c' * 40, created_at=CREATED, siblings=siblings if repo == 'owner/copy' else [],
                                   card_data=SimpleNamespace(to_dict=lambda: card))

        def list_repo_commits(self, repo):
            if repo == 'owner/copy':
                return [SimpleNamespace(commit_id='d' * 40, created_at=datetime(2026, 1, 3, tzinfo=timezone.utc), title='Later edit'),
                        SimpleNamespace(commit_id='c' * 40, created_at=CREATED, title=first_title)]
            return history
    return API()


class DuplicateCheckTests(unittest.TestCase):
    def test_measured_weight_files_are_refused_naming_the_earliest_copy(self):
        with self.assertRaisesRegex(Duplicate, 'same weight files as first/copy measured in round 8'):
            pin(api('Duplicate from first/copy'), 'owner/copy', 'publisher/base', known=KNOWN)
        with self.assertRaisesRegex(Duplicate, 'first/copy measured in round 8'):
            pin(api('Upload'), 'owner/copy', 'publisher/base', known=KNOWN)

    def test_a_duplicate_with_later_edits_is_pinned_with_its_parent_noted(self):
        row = pin(api('Duplicate from first/copy', sha=SHA_B), 'owner/copy', 'publisher/base', known=KNOWN)
        self.assertEqual(row['modified']['duplicate_of'], 'first/copy')
        self.assertEqual(row['modified']['weight_files_sha256'], {'model.safetensors': SHA_B})
        self.assertNotIn('same_weights_as', row['modified'])
        self.assertNotIn('allow_duplicate', row['modified'])

    def test_allowed_duplicate_is_pinned_and_says_so(self):
        row = pin(api('Upload'), 'owner/copy', 'publisher/base', known=KNOWN, allow_duplicate=True)
        self.assertTrue(row['modified']['allow_duplicate'])
        self.assertEqual(row['modified']['same_weights_as'], {'hub_id': 'first/copy', 'round': 8, 'state': 'measured'})
        self.assertEqual(row['modified']['weight_files_sha256'], {'model.safetensors': SHA_A})

    def test_a_pinned_pair_without_hub_checksums_is_not_a_match(self):
        self.assertIsNone(same_weights({}, KNOWN))
        self.assertIsNone(same_weights({'model.safetensors': SHA_B}, KNOWN))
        self.assertEqual(same_weights({'x.safetensors': SHA_A}, KNOWN)['round'], 8)

    def test_measured_copies_read_reports_and_pinned_batches(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / 'results/weights').mkdir(parents=True)
            (root / 'data/batches').mkdir(parents=True)
            (root / 'results/weights/first-copy.json').write_text(json.dumps({
                'modified': {'source': '/work/rounds/8/derived/pair-1', 'shards_sha256': {'model.safetensors': SHA_A}},
                'census': {'modified': {'hub_id': 'first/copy'}}}))
            (root / 'results/weights/unnamed.json').write_text(json.dumps({'modified': {'shards_sha256': {'a': SHA_B}}}))
            (root / 'results/weights/no-shards.json').write_text(json.dumps({'modified': {}}))
            (root / 'data/batches/round-31-batch-1.json').write_text(json.dumps({'round': 31, 'pairs': [
                {'modified': {'hub_id': 'pinned/copy', 'weight_files_sha256': {'model.safetensors': 'c' * 64}}},
                {'modified': {'hub_id': 'older/pin'}}]}))
            rows = measured_copies(root)
        self.assertEqual([(row['hub_id'], row['state'], row['round']) for row in rows],
                         [('first/copy', 'measured', 8), ('unnamed', 'measured', None), ('pinned/copy', 'pinned', 31)])
        self.assertEqual(rows[2]['sha256'], {'c' * 64})

    def test_command_refuses_in_one_line_and_pins_with_the_flag(self):
        with tempfile.TemporaryDirectory() as temporary:
            manifest = Path(temporary) / 'round-40-batch-1.json'
            argv = ['pin_census.py', str(manifest), '--pair', 'owner/copy', 'publisher/base']
            with patch.object(pin_census, 'HfApi', lambda: api('Duplicate from first/copy')), \
                    patch.object(pin_census, 'measured_copies', lambda: KNOWN):
                out = io.StringIO()
                with patch.object(sys, 'argv', argv), contextlib.redirect_stdout(out), self.assertRaises(SystemExit) as stop:
                    pin_census.main()
                self.assertEqual(stop.exception.code, 1)
                self.assertEqual(out.getvalue().strip(), 'refused owner/copy: same weight files as first/copy measured in round 8')
                self.assertFalse(manifest.exists())
                out = io.StringIO()
                with patch.object(sys, 'argv', argv + ['--allow-duplicate']), contextlib.redirect_stdout(out):
                    pin_census.main()
            record = json.loads(manifest.read_text())
            self.assertEqual(record['round'], 40)
            self.assertTrue(record['pairs'][0]['modified']['allow_duplicate'])
            self.assertEqual(record['pairs'][0]['modified']['duplicate_of'], 'first/copy')
            self.assertIn('pinned as allowed: owner/copy has the same weight files as first/copy measured in round 8', out.getvalue())

    def test_command_notes_a_duplicate_whose_weights_changed(self):
        with tempfile.TemporaryDirectory() as temporary:
            manifest = Path(temporary) / 'round-40-batch-1.json'
            argv = ['pin_census.py', str(manifest), '--pair', 'owner/copy', 'publisher/base']
            out = io.StringIO()
            with patch.object(pin_census, 'HfApi', lambda: api('Duplicate from first/copy', sha=SHA_B)), \
                    patch.object(pin_census, 'measured_copies', lambda: KNOWN), \
                    patch.object(sys, 'argv', argv), contextlib.redirect_stdout(out):
                pin_census.main()
            self.assertEqual(out.getvalue().strip(),
                             'note: owner/copy was duplicated from first/copy and its weight files differ; pinned')
            record = json.loads(manifest.read_text())
            self.assertEqual(record['pairs'][0]['modified']['duplicate_of'], 'first/copy')
            self.assertNotIn('allow_duplicate', record['pairs'][0]['modified'])


if __name__ == '__main__':
    unittest.main()
