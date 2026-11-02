# test_pin_census.py -- Check the pinner's duplicate check against a stubbed hub listing.
# Created by Sean Egan
# Modified: SDE  the names step refuses a pair whose tensor names no rule pairs, with the counts.
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
from pin_census import Duplicate, measured_copies, names, pin, pairing, same_weights, unpaired

FIXTURES = ROOT / 'tests/fixtures/round2'

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


def record(hub_id, revision, tensors):
    """A names fixture as the names step writes it, with one shape for every tensor."""
    return {'hub_id': hub_id, 'revision': revision, 'config': {},
            'tensors': {name: {'dtype': 'BF16', 'file': 'model.safetensors', 'shape': [4, 4]} for name in tensors}}


LAYERS = ['layers.{}.{}.weight'.format(layer, part) for layer in range(3) for part in ('self_attn.o_proj', 'mlp.down_proj')]
ORIGINAL = ['model.language_model.' + name for name in LAYERS] + ['model.vision_tower.patch.weight']
# A layout no rule reaches: the same tensors twice, under two wrappers, as one diffusion copy saves them.
SPLIT = ['decoder.' + name for name in LAYERS] + ['encoder.' + name for name in LAYERS]


class NamePairingTests(unittest.TestCase):
    def test_names_the_rules_pair_pass_whatever_the_original_keeps_besides(self):
        exact = pairing(ORIGINAL, ORIGINAL)
        self.assertEqual((exact['paired'], exact['modified_only'], exact['mapping']), (7, [], None))
        swapped = pairing(ORIGINAL, ['language_model.model.' + name for name in LAYERS])
        self.assertEqual((swapped['paired'], swapped['modified_only'], len(swapped['original_only'])), (6, [], 1))
        self.assertEqual(swapped['mapping']['carried_by'], 'swap')
        self.assertIsNone(unpaired(record('maker/base', 'a' * 40, ORIGINAL),
                                   record('owner/copy', 'b' * 40, ['language_model.model.' + name for name in LAYERS])))

    def test_a_modified_name_no_rule_reaches_refuses_the_pair_with_the_counts(self):
        reason = unpaired(record('maker/base', 'a' * 40, ORIGINAL), record('owner/copy', 'b' * 40, SPLIT))
        self.assertEqual(reason, 'tensor names cannot be paired: 0 of 12 modified names pair with the 7 original names '
                                 '(modified 6 under decoder., 6 under encoder.; original 7 under model.); '
                                 '12 modified and 7 original names unpaired: owner/copy against maker/base')
        one_more = unpaired(record('maker/base', 'a' * 40, ORIGINAL), record('owner/copy', 'b' * 40, ORIGINAL + ['lm_head.weight']))
        self.assertIn('7 of 8 modified names pair with the 7 original names', one_more)
        self.assertIn('1 modified and 0 original names unpaired', one_more)

    def test_the_diffusion_copy_is_refused_on_its_committed_fixtures(self):
        original = json.loads((FIXTURES / 'f7f5b7f5fa82.json').read_text())
        copy = json.loads((FIXTURES / 'ddbe96533046.json').read_text())
        reason = unpaired(original, copy)
        self.assertTrue(reason.startswith('tensor names cannot be paired: 0 of 1,674 modified names pair with the 1,047 original names '
                                          '(modified 1,013 under encoder., 661 under decoder.; original 1,047 under model.)'), reason)
        self.assertTrue(reason.endswith('DuoNeural/diffusiongemma-26B-A4B-it-abliterated against google/diffusiongemma-26B-A4B-it'))
        heretic = json.loads((FIXTURES / 'e4b182fe68a5.json').read_text())
        self.assertIsNone(unpaired(original, heretic))

    def test_the_names_step_writes_every_fixture_then_refuses_the_unpaired_pair(self):
        records = {'a' * 40: record('maker/base', 'a' * 40, ORIGINAL),
                   'b' * 40: record('owner/copy', 'b' * 40, ORIGINAL),
                   'c' * 40: record('owner/other', 'c' * 40, SPLIT),
                   'd' * 40: record('maker/eight-bit', 'd' * 40, ORIGINAL),
                   'e' * 40: record('owner/third', 'e' * 40, SPLIT)}

        def fixture(hub, model):
            if model['hub_id'] == 'maker/eight-bit':
                raise ValueError('original is quantised (quantization_config): maker/eight-bit')
            return records[model['revision']]

        def side(hub_id, revision):
            return {'hub_id': hub_id, 'revision': revision}
        manifest = {'round': 40, 'pairs': [
            {'original': side('maker/base', 'a' * 40), 'modified': side('owner/copy', 'b' * 40)},
            {'original': side('maker/base', 'a' * 40), 'modified': side('owner/other', 'c' * 40)},
            {'original': side('maker/eight-bit', 'd' * 40), 'modified': side('owner/third', 'e' * 40)}]}
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / 'round-40-batch-1.json'
            path.write_text(json.dumps(manifest))
            out = io.StringIO()
            with patch.object(pin_census, 'fixture', fixture), contextlib.redirect_stdout(out), \
                    self.assertRaises(ValueError) as stop:
                names(path, Path(temporary) / 'names', hub=object())
            written = sorted(item.name for item in (Path(temporary) / 'names').iterdir())
        self.assertEqual(written, ['aaaaaaaaaaaa.json', 'bbbbbbbbbbbb.json', 'cccccccccccc.json', 'eeeeeeeeeeee.json'])
        message = str(stop.exception)
        self.assertTrue(message.startswith('2 checkpoint(s) refused; pair 3 original: original is quantised'), message)
        self.assertIn('; pair 2 names: tensor names cannot be paired: 0 of 12 modified names pair with the 7 original names', message)
        self.assertNotIn('pair 3 names', message)
        self.assertIn('refused pair 2 names: tensor names cannot be paired', out.getvalue())


if __name__ == '__main__':
    unittest.main()
