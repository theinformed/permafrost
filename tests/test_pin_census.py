# test_pin_census.py -- Check the pinner's duplicate check against a stubbed hub listing.
# Created by Sean Egan
# Modified: SDE  the names step refuses a pair whose tensor names no rule pairs, with the counts.
# Modified: SDE  a hub id measured at the same revision is refused with its round.
# Modified: SDE  a qat-named copy whose card names the instruct model pins against the QAT checkpoint.
# Modified: SDE  a parent the card's opening names, other than the field's, is recorded with a warning.
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
from huggingface_hub.utils import RepositoryNotFoundError
from pin_census import already_measured, card_opening, card_parent, Duplicate, measured_copies, names, pin, pairing, qat_original, same_weights, size_of, unpaired

FIXTURES = ROOT / 'tests/fixtures/round2'

CREATED = datetime(2026, 1, 2, tzinfo=timezone.utc)
SHA_A = 'a' * 64
SHA_B = 'b' * 64
KNOWN = [{'hub_id': 'first/copy', 'state': 'measured', 'round': 8, 'sha256': {SHA_A}},
         {'hub_id': 'third/copy', 'state': 'measured', 'round': 19, 'sha256': {SHA_A}}]
# The copy itself, measured at the revision the stubbed hub serves, on other weight files than KNOWN's.
MEASURED = [{'hub_id': 'owner/copy', 'state': 'measured', 'round': 13, 'revision': 'c' * 40, 'sha256': {SHA_B}},
            {'hub_id': 'owner/copy', 'state': 'measured', 'round': 22, 'revision': 'c' * 40, 'sha256': {SHA_B}},
            {'hub_id': 'owner/copy', 'state': 'pinned', 'round': 40, 'revision': 'c' * 40, 'sha256': {SHA_B}}]


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
                'census': {'modified': {'hub_id': 'first/copy', 'revision': 'f' * 40}}}))
            (root / 'results/weights/unnamed.json').write_text(json.dumps({'modified': {'shards_sha256': {'a': SHA_B}}}))
            (root / 'results/weights/no-shards.json').write_text(json.dumps({'modified': {}}))
            (root / 'data/batches/round-31-batch-1.json').write_text(json.dumps({'round': 31, 'pairs': [
                {'modified': {'hub_id': 'pinned/copy', 'revision': 'e' * 40, 'weight_files_sha256': {'model.safetensors': 'c' * 64}}},
                {'modified': {'hub_id': 'older/pin'}}]}))
            rows = measured_copies(root)
        self.assertEqual([(row['hub_id'], row['state'], row['round']) for row in rows],
                         [('first/copy', 'measured', 8), ('unnamed', 'measured', None), ('pinned/copy', 'pinned', 31)])
        self.assertEqual(rows[2]['sha256'], {'c' * 64})
        self.assertEqual([row['revision'] for row in rows], ['f' * 40, None, 'e' * 40])

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


class MeasuredRevisionTests(unittest.TestCase):
    def test_the_same_hub_id_at_a_measured_revision_is_refused_naming_the_first_round(self):
        with self.assertRaisesRegex(Duplicate, '^already measured in round 13$'):
            pin(api('Upload', sha=SHA_A), 'owner/copy', 'publisher/base', known=MEASURED)
        self.assertEqual(already_measured('Owner/Copy', 'c' * 40, MEASURED)['round'], 13)
        # Another revision of the same repository, or a pin not yet measured, is not a measurement.
        self.assertIsNone(already_measured('owner/copy', 'd' * 40, MEASURED))
        self.assertIsNone(already_measured('owner/copy', 'c' * 40, MEASURED[2:]))
        self.assertIsNone(already_measured('owner/copy', None, [{'hub_id': 'owner/copy', 'state': 'measured', 'round': 1}]))

    def test_an_allowed_re_measure_records_the_round_that_measured_it(self):
        row = pin(api('Upload', sha=SHA_A), 'owner/copy', 'publisher/base', known=MEASURED, allow_duplicate=True)
        self.assertEqual(row['modified']['measured_in'], {'round': 13})
        self.assertTrue(row['modified']['allow_duplicate'])
        self.assertNotIn('same_weights_as', row['modified'])

    def test_command_refuses_the_measured_revision_in_one_line_and_pins_with_the_flag(self):
        with tempfile.TemporaryDirectory() as temporary:
            manifest = Path(temporary) / 'round-41-batch-1.json'
            argv = ['pin_census.py', str(manifest), '--pair', 'owner/copy', 'publisher/base']
            with patch.object(pin_census, 'HfApi', lambda: api('Upload', sha=SHA_B)), \
                    patch.object(pin_census, 'measured_copies', lambda: MEASURED):
                out = io.StringIO()
                with patch.object(sys, 'argv', argv), contextlib.redirect_stdout(out), self.assertRaises(SystemExit) as stop:
                    pin_census.main()
                self.assertEqual(stop.exception.code, 1)
                self.assertEqual(out.getvalue().strip(), 'refused owner/copy: already measured in round 13')
                self.assertFalse(manifest.exists())
                out = io.StringIO()
                with patch.object(sys, 'argv', argv + ['--allow-duplicate']), contextlib.redirect_stdout(out):
                    pin_census.main()
            record = json.loads(manifest.read_text())
            self.assertEqual(record['pairs'][0]['modified']['measured_in'], {'round': 13})
            self.assertEqual(record['pairs'][0]['modified']['same_weights_as'], {'hub_id': 'owner/copy', 'round': 13, 'state': 'measured'})
            self.assertEqual(out.getvalue().strip(), 'pinned as allowed: owner/copy already measured in round 13')


INSTRUCT = 'google/gemma-4-12B-it'
QAT = 'google/gemma-4-12B-it-qat-q4_0-unquantized'
CARDS = {'owner/gemma-4-12B-it-qat-heretic': INSTRUCT, 'owner/gemma-4-12B-it-heretic': INSTRUCT,
         'owner/gemma-4-E4B-it-qat-heretic': INSTRUCT, 'owner/gemma-4-31B-it-qat-heretic': 'google/gemma-4-31B-it',
         INSTRUCT: 'google/gemma-4-12B', QAT: INSTRUCT, 'google/gemma-4-31B-it': 'google/gemma-4-31B',
         'google/gemma-4-12B': None, 'google/gemma-4-31B': None, 'other/fine-tune': INSTRUCT}


def gemma_api():
    """A hub that knows the repositories in CARDS and nothing else; the 31B has no QAT checkpoint."""
    class API:
        def model_info(self, repo, revision=None, **kwargs):
            if repo not in CARDS:
                raise ValueError('404: ' + repo)
            card = {'base_model': CARDS[repo]} if CARDS[repo] else {}
            siblings = [SimpleNamespace(rfilename='model.safetensors', lfs=SimpleNamespace(sha256=SHA_B, size=1, pointer_size=1))]
            return SimpleNamespace(sha=revision or 'c' * 40, created_at=CREATED, siblings=siblings if repo.startswith('owner/') else [],
                                   card_data=SimpleNamespace(to_dict=lambda: card))

        def list_repo_commits(self, repo):
            if repo.startswith('owner/'):
                return [SimpleNamespace(commit_id='c' * 40, created_at=CREATED, title='Upload')]
            return [SimpleNamespace(commit_id='a' * 40, created_at=datetime(2026, 1, 1, tzinfo=timezone.utc), title='Upload')]
    return API()


def missing_base_api(cards):
    """The gemma hub with extra copies whose cards name bases ending in 'gone', which the hub does not serve."""
    inner = gemma_api()

    class API:
        def model_info(self, repo, revision=None, **kwargs):
            if repo.endswith('gone'):
                raise RepositoryNotFoundError('404: ' + repo, response=SimpleNamespace(status_code=404, headers={}, url=repo, request=None))
            if repo in cards:
                siblings = [SimpleNamespace(rfilename='model.safetensors', lfs=SimpleNamespace(sha256=SHA_B, size=1, pointer_size=1))]
                return SimpleNamespace(sha=revision or 'c' * 40, created_at=CREATED, siblings=siblings,
                                       card_data=SimpleNamespace(to_dict=lambda: {'base_model': cards[repo]}))
            return inner.model_info(repo, revision, **kwargs)

        def list_repo_commits(self, repo):
            return inner.list_repo_commits(repo)
    return API()


class MissingBaseTests(unittest.TestCase):
    def test_a_declared_base_the_hub_does_not_serve_is_recorded_as_missing(self):
        api = missing_base_api({'owner/two-bases': ['google/gemma-4-12B-gone', INSTRUCT],
                                'owner/one-base': 'google/gemma-4-12B-gone', 'owner/own-base': 'owner/gone'})
        row = pin(api, 'owner/two-bases', INSTRUCT)
        chain = row['modified']['base_model_chain']
        self.assertEqual([node['hub_id'] for node in chain], ['google/gemma-4-12B-gone', INSTRUCT])
        self.assertTrue(chain[0]['missing'])
        self.assertEqual(chain[0]['base_model_chain'], [])
        self.assertIsNone(chain[0]['revision'])
        self.assertTrue(chain[0]['publisher_root'])
        self.assertTrue(chain[0]['lineage_known'])
        self.assertTrue(row['modified']['lineage_known'])
        row = pin(api, 'owner/one-base', INSTRUCT)
        self.assertTrue(row['modified']['base_model_chain'][0]['publisher_root'])
        # A missing base under the copy's own name is nobody's publisher root and stays unknown.
        row = pin(api, 'owner/own-base', INSTRUCT)
        self.assertFalse(row['modified']['base_model_chain'][0]['publisher_root'])
        self.assertFalse(row['modified']['base_model_chain'][0]['lineage_known'])

    def test_the_screen_passes_a_missing_publisher_base_and_holds_an_own_one(self):
        import lineage
        api = missing_base_api({'owner/one-base': 'google/gemma-4-12B-gone', 'owner/own-base': 'owner/gone'})
        with tempfile.TemporaryDirectory() as folder:
            banned = Path(folder) / 'banned.txt'
            banned.write_text('qwen\n')
            self.assertEqual(lineage.screen({'pairs': [pin(api, 'owner/one-base', INSTRUCT)]}, banned), 1)
            with self.assertRaises(ValueError) as held:
                lineage.screen({'pairs': [pin(api, 'owner/own-base', INSTRUCT)]}, banned)
            self.assertEqual(str(held.exception), 'unknown base held: owner/own-base')


class QatOriginalTests(unittest.TestCase):
    def test_sizes_read_from_names(self):
        self.assertEqual([size_of(name) for name in ('google/gemma-4-12B-it', 'owner/gemma-4-E4B-it-qat-heretic',
                                                      'google/gemma-4-26B-A4B-it-qat-q4_0-unquantized', 'owner/Mistral-7B-v0.3-x', 'owner/no-size')],
                         ['12b', 'e4b', '26b-a4b', '7b', None])

    def test_a_qat_named_copy_pinned_by_its_card_moves_to_the_qat_checkpoint(self):
        api = gemma_api()
        self.assertEqual(qat_original(api, 'owner/gemma-4-12B-it-qat-heretic', INSTRUCT, INSTRUCT)[0], QAT)
        self.assertEqual(qat_original(api, 'owner/gemma-4-12B-it-qat-heretic', INSTRUCT, [INSTRUCT])[0], QAT)
        # Named by the caller: the QAT checkpoint itself, or another original, is followed as given.
        self.assertEqual(qat_original(api, 'owner/gemma-4-12B-it-qat-heretic', QAT, INSTRUCT), (QAT, None))
        self.assertEqual(qat_original(api, 'owner/gemma-4-12B-it-qat-heretic', 'other/fine-tune', INSTRUCT), ('other/fine-tune', None))
        # No qat in the name, a card of another size, a card naming the pretrained base, no QAT checkpoint on the hub.
        self.assertEqual(qat_original(api, 'owner/gemma-4-12B-it-heretic', INSTRUCT, INSTRUCT), (INSTRUCT, None))
        self.assertEqual(qat_original(api, 'owner/gemma-4-E4B-it-qat-heretic', INSTRUCT, INSTRUCT), (INSTRUCT, None))
        self.assertEqual(qat_original(api, 'owner/gemma-4-12B-it-qat-heretic', 'google/gemma-4-12B', 'google/gemma-4-12B'),
                         ('google/gemma-4-12B', None))
        self.assertEqual(qat_original(api, 'owner/gemma-4-31B-it-qat-heretic', 'google/gemma-4-31B-it', 'google/gemma-4-31B-it'),
                         ('google/gemma-4-31B-it', None))

    def test_the_pin_records_the_declared_field_beside_the_note(self):
        row = pin(gemma_api(), 'owner/gemma-4-12B-it-qat-heretic', INSTRUCT)
        self.assertEqual(row['original']['hub_id'], QAT)
        self.assertEqual(row['original']['declared_base_model'], INSTRUCT)
        self.assertEqual(row['modified']['declared_base_model'], INSTRUCT)
        self.assertEqual(row['modified']['original_note'],
                         'base_model names google/gemma-4-12B-it; the copy name says qat and '
                         'google/gemma-4-12B-it-qat-q4_0-unquantized exists, so the pair is pinned against it')
        self.assertTrue(row['modified']['lineage_known'])
        plain = pin(gemma_api(), 'owner/gemma-4-12B-it-heretic', INSTRUCT)
        self.assertEqual(plain['original']['hub_id'], INSTRUCT)
        self.assertNotIn('original_note', plain['modified'])

    def test_command_prints_the_note(self):
        with tempfile.TemporaryDirectory() as temporary:
            manifest = Path(temporary) / 'round-42-batch-1.json'
            argv = ['pin_census.py', str(manifest), '--pair', 'owner/gemma-4-12B-it-qat-heretic', INSTRUCT]
            out = io.StringIO()
            with patch.object(pin_census, 'HfApi', gemma_api), patch.object(pin_census, 'measured_copies', lambda: []), \
                    patch.object(sys, 'argv', argv), contextlib.redirect_stdout(out):
                pin_census.main()
            self.assertEqual(out.getvalue().strip(), 'note: owner/gemma-4-12B-it-qat-heretic base_model names google/gemma-4-12B-it; '
                             'the copy name says qat and google/gemma-4-12B-it-qat-q4_0-unquantized exists, so the pair is pinned against it')
            self.assertEqual(json.loads(manifest.read_text())['pairs'][0]['original']['hub_id'], QAT)


ARTEMIS = 'TheDrummer/Artemis-31B-v1.1'
README = '''---
base_model: google/gemma-4-31B-it
license: gemma
---
<img src="banner.png">
![badge](https://img.shields.io/x)
| a | b |

# owner/Artemis-31B-v1.1-heretic

This is {} (https://huggingface.co/TheDrummer/Artemis-31B-v1.1) decensored with the tool 1/2 of nobody/knows. Second sentence names other/fine-tune.
'''.format(ARTEMIS)


def card_api(readme=README, known=(ARTEMIS, 'other/fine-tune', 'google/gemma-4-31B-it', 'google/gemma-4-31B', 'owner/Artemis-31B-v1.1-heretic')):
    """A hub that serves one card for the copy and knows the repositories in KNOWN."""
    base = gemma_api()

    class API:
        def model_info(self, repo, revision=None, **kwargs):
            if repo not in known:
                raise ValueError('404: ' + repo)
            card = {'base_model': 'google/gemma-4-31B-it'} if repo.startswith('owner/') else {'base_model': 'google/gemma-4-31B'} if repo.endswith('-it') else {}
            if repo == ARTEMIS or repo == 'other/fine-tune':
                card = {'base_model': 'google/gemma-4-31B-it'}
            siblings = [SimpleNamespace(rfilename='model.safetensors', lfs=SimpleNamespace(sha256=SHA_B, size=1, pointer_size=1))]
            return SimpleNamespace(sha=revision or 'c' * 40, created_at=CREATED, siblings=siblings if repo.startswith('owner/') else [],
                                   card_data=SimpleNamespace(to_dict=lambda: card))

        list_repo_commits = base.list_repo_commits

        def hf_hub_download(self, repo_id, filename, revision=None):
            if readme is None:
                raise FileNotFoundError(filename)
            path = Path(tempfile.mkdtemp()) / filename
            path.write_text(readme)
            return str(path)
    return API()


class CardParentTests(unittest.TestCase):
    def test_the_opening_is_the_first_heading_and_the_first_sentence_past_the_header(self):
        from pin_census import card_body
        hub = card_api()
        text = card_body(hub, 'owner/Artemis-31B-v1.1-heretic', 'c' * 40)
        self.assertFalse(text.lstrip().startswith('---'))
        self.assertEqual(card_opening(text), ('owner/Artemis-31B-v1.1-heretic',
                         'This is TheDrummer/Artemis-31B-v1.1 (https://huggingface.co/TheDrummer/Artemis-31B-v1.1) decensored with the tool 1/2 of nobody/knows.'))
        self.assertEqual(card_opening('Plain card naming maker/model first.\n# Heading later'), ('', 'Plain card naming maker/model first.'))
        self.assertEqual(card_body(card_api(readme=None), 'owner/Artemis-31B-v1.1-heretic', 'c' * 40), '')
        self.assertEqual(card_body(api('Upload'), 'owner/copy', 'c' * 40), '')

    def test_the_first_existing_repository_named_beside_the_copy_and_its_field_is_the_card_parent(self):
        hub = card_api()
        text = README.split('---\n', 2)[2]
        self.assertEqual(card_parent(hub, text, 'owner/Artemis-31B-v1.1-heretic', 'google/gemma-4-31B-it'), ARTEMIS)
        self.assertEqual(card_parent(hub, text, 'owner/Artemis-31B-v1.1-heretic', ['google/gemma-4-31B-it', ARTEMIS]), None)
        self.assertIsNone(card_parent(hub, '# owner/Artemis-31B-v1.1-heretic\n\nA decensored google/gemma-4-31B-it.\n',
                                      'owner/Artemis-31B-v1.1-heretic', 'google/gemma-4-31B-it'))
        self.assertIsNone(card_parent(hub, 'Made with nobody/knows and 1/2 of the data.', 'owner/x', None))
        self.assertEqual(card_parent(hub, '# [TheDrummer/Artemis-31B-v1.1](https://hf.co/TheDrummer/Artemis-31B-v1.1), decensored\n', 'owner/x', None), ARTEMIS)

    def test_the_pin_records_the_card_parent_and_the_command_warns_without_changing_the_original(self):
        row = pin(card_api(), 'owner/Artemis-31B-v1.1-heretic', 'google/gemma-4-31B-it')
        self.assertEqual(row['modified']['card_parent'], ARTEMIS)
        self.assertEqual(row['original']['hub_id'], 'google/gemma-4-31B-it')
        self.assertNotIn('card_parent', pin(card_api(readme=None), 'owner/Artemis-31B-v1.1-heretic', 'google/gemma-4-31B-it')['modified'])
        with tempfile.TemporaryDirectory() as temporary:
            manifest = Path(temporary) / 'round-43-batch-1.json'
            argv = ['pin_census.py', str(manifest), '--pair', 'owner/Artemis-31B-v1.1-heretic', 'google/gemma-4-31B-it']
            out = io.StringIO()
            with patch.object(pin_census, 'HfApi', card_api), patch.object(pin_census, 'measured_copies', lambda: []), \
                    patch.object(sys, 'argv', argv), contextlib.redirect_stdout(out):
                pin_census.main()
            self.assertEqual(out.getvalue().strip(), 'warning: owner/Artemis-31B-v1.1-heretic card names TheDrummer/Artemis-31B-v1.1 '
                             'where base_model names google/gemma-4-31B-it; pinned against google/gemma-4-31B-it')
            self.assertEqual(json.loads(manifest.read_text())['pairs'][0]['modified']['card_parent'], ARTEMIS)
            # Pinned against the card's parent by hand: recorded, nothing to warn about.
            manifest.unlink()
            out = io.StringIO()
            with patch.object(pin_census, 'HfApi', card_api), patch.object(pin_census, 'measured_copies', lambda: []), \
                    patch.object(sys, 'argv', argv[:-1] + [ARTEMIS]), contextlib.redirect_stdout(out):
                pin_census.main()
            self.assertEqual(out.getvalue().strip(), '')
            self.assertEqual(json.loads(manifest.read_text())['pairs'][0]['modified']['card_parent'], ARTEMIS)


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

    def test_a_copy_whose_only_other_shape_is_its_token_table_is_a_resized_vocabulary(self):
        original = json.loads((FIXTURES / '70af34e20bd4.json').read_text())
        copy = json.loads((FIXTURES / '84c7f4804575.json').read_text())
        mapping = pairing(original['tensors'], copy['tensors'])['names']
        same = {other: dict(copy['tensors'][other], shape=original['tensors'][name]['shape']) for name, other in mapping.items()}
        for name in list(copy['tensors']):
            same.setdefault(name, copy['tensors'][name])
        table = next(name for name in same if name.endswith('embed_tokens.weight'))
        rows, width = same[table]['shape']
        same[table] = dict(same[table], shape=[rows - 63, width])
        reason = unpaired(original, dict(copy, tensors=same))
        self.assertTrue(reason.startswith('the copy carries a resized vocabulary: its token table has {:,} rows against the original\'s {:,} '
                                          '({} is [{}, {}] against [{}, {}]), which no pairing rule covers yet'.format(
                                              rows - 63, rows, next(name for name in original['tensors'] if name.endswith('embed_tokens.weight')), rows - 63, width, rows, width)), reason)
        self.assertTrue(reason.endswith('TurkishCodeMan/gemma-4-e2b-it-abliterated against google/gemma-4-E2B-it'), reason)

    def test_a_copy_of_another_model_is_refused_on_its_shapes_before_its_layer_count(self):
        original = json.loads((FIXTURES / '70af34e20bd4.json').read_text())
        copy = json.loads((FIXTURES / '84c7f4804575.json').read_text())
        reason = unpaired(original, copy)
        self.assertTrue(reason.startswith('the copy is an export of another model: 164 of 164 paired tensors differ in shape '
                                          '(model.language_model.embed_tokens.weight is [256000, 2048] against [262144, 1536])'), reason)
        self.assertTrue(reason.endswith('TurkishCodeMan/gemma-4-e2b-it-abliterated against google/gemma-4-E2B-it'), reason)
        # The same names with the original's shapes are a partial export, reported as before.
        mapping = pairing(original['tensors'], copy['tensors'])['names']
        same = {other: dict(copy['tensors'][other], shape=original['tensors'][name]['shape']) for name, other in mapping.items()}
        reason = unpaired(original, dict(copy, tensors=same))
        self.assertTrue(reason.startswith('the copy is a partial export carrying 18 of 35 layers'), reason)

    def test_a_copy_carrying_some_of_the_layers_is_refused_as_a_partial_export(self):
        two_layers = ['model.' + name for name in LAYERS if '.2.' not in name]
        reason = unpaired(record('maker/base', 'a' * 40, ORIGINAL), record('owner/copy', 'b' * 40, two_layers))
        self.assertEqual(reason, 'the copy is a partial export carrying 2 of 3 layers under model.language_model.layers. '
                                 '(layers 2 to 2 missing): owner/copy against maker/base')
        # Every layer carried, towers and one shared-kv tensor dropped: whole, and left to the comparison.
        whole = ['model.' + name for name in LAYERS if name != 'layers.2.self_attn.o_proj.weight']
        self.assertIsNone(unpaired(record('maker/base', 'a' * 40, ORIGINAL), record('owner/copy', 'b' * 40, whole)))

    def test_an_index_naming_unpublished_shards_is_refused_with_the_file_list(self):
        index = json.dumps({'weight_map': {'a': 'model-00001-of-00002.safetensors', 'b': 'model-00002-of-00002.safetensors'}}).encode()
        gets = {'model.safetensors.index.json': index, 'config.json': b'{}'}
        with patch.object(pin_census, 'bounded_get', lambda hub, repo, revision, filename: gets.get(filename)), \
                patch.object(pin_census, 'weight_files', lambda hub, repo, revision: ['consolidated.safetensors', 'model.safetensors']), \
                self.assertRaises(ValueError) as stop:
            pin_census.fixture(object(), {'hub_id': 'owner/copy', 'revision': 'b' * 40})
        self.assertEqual(str(stop.exception), 'index names 2 shard(s) the repository does not publish (model-00001-of-00002.safetensors first); '
                                              'it publishes consolidated.safetensors, model.safetensors: owner/copy')

    def test_the_names_step_writes_every_fixture_then_refuses_the_unpaired_pair(self):
        records = {'a' * 40: record('maker/base', 'a' * 40, ORIGINAL),
                   'b' * 40: record('owner/copy', 'b' * 40, ORIGINAL),
                   'c' * 40: record('owner/other', 'c' * 40, SPLIT),
                   'd' * 40: record('maker/eight-bit', 'd' * 40, ORIGINAL),
                   'e' * 40: record('owner/third', 'e' * 40, SPLIT)}

        def fixture(hub, model):
            if model['hub_id'] == 'maker/eight-bit':
                raise ValueError('original is quantised (quantization_config): maker/eight-bit')
            if model['hub_id'] == 'owner/gone':
                raise OSError('404 Client Error: Not Found for url: https://huggingface.co/owner/gone/resolve/f/model-00001-of-00008.safetensors')
            return records[model['revision']]

        def side(hub_id, revision):
            return {'hub_id': hub_id, 'revision': revision}
        manifest = {'round': 40, 'pairs': [
            {'original': side('maker/base', 'a' * 40), 'modified': side('owner/copy', 'b' * 40)},
            {'original': side('maker/base', 'a' * 40), 'modified': side('owner/other', 'c' * 40)},
            {'original': side('maker/eight-bit', 'd' * 40), 'modified': side('owner/third', 'e' * 40)},
            {'original': side('maker/base', 'a' * 40), 'modified': side('owner/gone', 'f' * 40)}]}
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
        self.assertTrue(message.startswith('3 checkpoint(s) refused; pair 3 original: original is quantised'), message)
        self.assertIn('; pair 4 modified: 404 Client Error', message)
        self.assertIn('; pair 2 names: tensor names cannot be paired: 0 of 12 modified names pair with the 7 original names', message)
        self.assertNotIn('pair 3 names', message)
        self.assertIn('refused pair 2 names: tensor names cannot be paired', out.getvalue())


if __name__ == '__main__':
    unittest.main()
