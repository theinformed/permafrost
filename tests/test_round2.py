# test_round2.py -- Check census pins, lineage holds and queued CPU pieces.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  test failures before they can become scheduler successes.
# Modified: SDE 2026-10-15  real tensor names, round 1's pins, the lean measure, the census bundle name.
# Modified: SDE 2026-10-29  the shared table names packed experts and audit.hub loads under the pins.
# Modified: SDE 2026-10-29  batches of any size, parallel compares and the sweep, systems table, PBS.
# Modified: SDE 2026-10-30  a copy pinned against its stated parent, itself a copy, passes the screen.
# Modified: SDE  the pin stubs take the listing flag the duplicate check passes.
# Modified: SDE  the names fixture test stubs the published weight file list.
import ast
from datetime import datetime, timezone
import hashlib
import importlib.util
import contextlib
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time
from types import SimpleNamespace
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
ROUND = ROOT / 'hpc/rounds/2'
sys.path.insert(0, str(ROOT / 'hpc'))
sys.path.append(str(ROUND))
from lineage import screen
from pin_census import pin
from rehearse_round2 import BUNDLE, CensusRehearsal, CLUSTER_PYTHON, dependency, fixture_kit, NAMES, NEEDS, SYSTEMS


def module(name):
    spec = importlib.util.spec_from_file_location('census_' + name, ROUND / (name + '.py'))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def manifest():
    return json.loads((ROOT / 'data/batches/round-2-batch-1.json').read_text())


def bigger_manifest(count, number=7):
    """A batch of COUNT pairs on round 2's pinned rows: later copies reuse an earlier original.

    Each extra copy keeps its row's revisions, so the real-name fixtures still apply, and its
    original is the same folder as the row it came from.
    """
    record = manifest()
    rows = record['pairs']
    pairs = [json.loads(json.dumps(rows[index % len(rows)])) for index in range(count)]
    for index, row in enumerate(pairs[len(rows):], len(rows) + 1):
        row['modified']['hub_id'] += '-copy-' + str(index)
    record.update(round=number, pairs=pairs)
    return record


def opened(bundle, folder):
    """Unpack a built bundle's payload the way the opener does, for reading its files."""
    folder.mkdir(parents=True)
    payload = bundle.read_bytes().split(b'__PAYLOAD__\n', 1)[1]
    (folder / 'payload.tar').write_bytes(payload)
    subprocess.check_call(['tar', '-xf', 'payload.tar'], cwd=str(folder))
    return folder


class LineageTests(unittest.TestCase):
    def test_five_pinned_pairs_pass(self):
        record = manifest()
        self.assertEqual(screen(record, ROOT / 'hpc/banned-makers.txt'), 5)
        for pair in record['pairs']:
            for side in ('original', 'modified'):
                self.assertRegex(pair[side]['revision'], r'^[0-9a-f]{40}$')
            cutoff = datetime.fromisoformat(pair['original_selection']['cutoff'])
            self.assertLessEqual(datetime.fromisoformat(pair['original']['revision_date']), cutoff)
            self.assertEqual(cutoff, datetime.fromisoformat(pair['modified']['created_at']))

    def test_planted_parent_fails_cli_and_names_copy(self):
        record = manifest()
        copy = record['pairs'][0]['modified']
        copy['declared_base_model'] = 'Qwen/planted-base'
        with tempfile.TemporaryDirectory(dir=ROOT / '.tmp') as folder:
            path = Path(folder) / 'batch.json'
            path.write_text(json.dumps(record))
            result = subprocess.run([sys.executable, str(ROOT / 'hpc/lineage.py'), str(path),
                                     str(ROOT / 'hpc/banned-makers.txt')], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(copy['hub_id'], result.stdout.decode())
        self.assertIn('banned lineage', result.stdout.decode())

    def test_nested_merge_and_maker_are_screened(self):
        for field in ('maker', 'hub_id'):
            record = manifest()
            node = record['pairs'][0]['modified']['base_model_chain'][0]
            node[field] = 'upstream-QwEn-experiment'
            with self.assertRaisesRegex(ValueError, record['pairs'][0]['modified']['hub_id']):
                screen(record, ROOT / 'hpc/banned-makers.txt')

    def test_unknown_and_incomplete_chains_are_held(self):
        for key, value in (('declared_base_model', None), ('lineage_known', False), ('base_model_chain', [])):
            record = manifest()
            record['pairs'][0]['modified'][key] = value
            with self.assertRaisesRegex(ValueError, 'held: '):
                screen(record, ROOT / 'hpc/banned-makers.txt')


class PinTests(unittest.TestCase):
    def test_history_selects_latest_before_creation_and_keeps_declaration(self):
        created = datetime(2026, 1, 2, tzinfo=timezone.utc)
        history = [SimpleNamespace(commit_id='a' * 40, created_at=datetime(2026, 1, 1, tzinfo=timezone.utc)),
                   SimpleNamespace(commit_id='b' * 40, created_at=datetime(2026, 1, 3, tzinfo=timezone.utc))]
        class API:
            def model_info(self, repo, revision=None, **kwargs):
                card = {'base_model': 'publisher/base'} if repo == 'owner/copy' else {}
                return SimpleNamespace(sha=revision or 'c' * 40, created_at=created,
                                       card_data=SimpleNamespace(to_dict=lambda: card))
            def list_repo_commits(self, repo):
                if repo == 'owner/copy':
                    return [SimpleNamespace(commit_id='c' * 40, created_at=created)]
                return history
        row = pin(API(), 'owner/copy', 'publisher/base')
        self.assertEqual(row['original']['revision'], 'a' * 40)
        self.assertEqual(row['modified']['declared_base_model'], 'publisher/base')
        self.assertEqual(row['original_selection']['cutoff'], created.isoformat())
        history[:] = history[1:]
        with self.assertRaisesRegex(ValueError, 'predates creation'):
            pin(API(), 'owner/copy', 'publisher/base')

    def test_a_rewritten_original_history_pins_to_the_copy_revision_and_says_so(self):
        # google/gemma-4-12B-it keeps no commit older than OpenYourMind's copy of it, which was created about an
        # hour before the oldest surviving original commit and revised two weeks later. The pin takes the latest
        # original commit no later than the copy's measured revision and records where the history starts.
        created = datetime(2026, 6, 3, 19, 57, tzinfo=timezone.utc)
        revised = datetime(2026, 6, 16, 9, 28, tzinfo=timezone.utc)
        history = [SimpleNamespace(commit_id='a' * 40, created_at=datetime(2026, 6, 3, 21, 14, tzinfo=timezone.utc)),
                   SimpleNamespace(commit_id='b' * 40, created_at=datetime(2026, 6, 20, tzinfo=timezone.utc))]
        class API:
            def model_info(self, repo, revision=None, **kwargs):
                card = {'base_model': 'publisher/base'} if repo == 'owner/copy' else {}
                return SimpleNamespace(sha=revision or 'c' * 40, created_at=created,
                                       card_data=SimpleNamespace(to_dict=lambda: card))
            def list_repo_commits(self, repo):
                if repo == 'owner/copy':
                    return [SimpleNamespace(commit_id='c' * 40, created_at=revised)]
                return history
        row = pin(API(), 'owner/copy', 'publisher/base')
        self.assertEqual(row['original']['revision'], 'a' * 40)
        selection = row['original_selection']
        self.assertEqual(selection['cutoff'], revised.isoformat())
        self.assertIn('history starts after', selection['rule'])
        self.assertEqual(selection['original_history_starts'], history[0].created_at.isoformat())

    def test_a_parent_that_is_itself_a_copy_pins_and_passes_the_screen(self):
        created = datetime(2026, 1, 2, tzinfo=timezone.utc)
        cards = {'rich/coder-heretic': 'maker/model-it', 'yu/coder': 'maker/model-it',
                 'maker/model-it': ['maker/model'], 'own/copy-v2': 'own/copy-v1'}

        class API:
            def model_info(self, repo, revision=None, **kwargs):
                card = {'base_model': cards[repo]} if repo in cards else {}
                return SimpleNamespace(sha=revision or 'c' * 40, created_at=created,
                                       card_data=SimpleNamespace(to_dict=lambda: card))

            def list_repo_commits(self, repo):
                return [SimpleNamespace(commit_id='c' * 40, created_at=created)]

        banned = ROOT / 'hpc/banned-makers.txt'
        row = pin(API(), 'rich/coder-heretic', 'yu/coder')
        for side in ('modified', 'original'):
            leaf = row[side]['base_model_chain'][0]['base_model_chain'][0]
            self.assertEqual(leaf['hub_id'], 'maker/model')
            self.assertTrue(leaf['publisher_root'] and leaf['lineage_known'])
            self.assertFalse(row[side]['publisher_root'])
        self.assertTrue(row['original']['lineage_known'])
        self.assertEqual(screen({'pairs': [row]}, banned), 1)
        # the maker's own instruct model as the original still pins as before
        plain = pin(API(), 'rich/coder-heretic', 'maker/model-it')
        self.assertTrue(plain['original']['base_model_chain'][0]['publisher_root'])
        self.assertEqual(screen({'pairs': [plain]}, banned), 1)
        # an undeclared ancestor on the copy's side alone is still held
        held = pin(API(), 'own/copy-v2', 'maker/model-it')
        self.assertFalse(held['modified']['base_model_chain'][0]['lineage_known'])
        with self.assertRaisesRegex(ValueError, 'held: own/copy-v2'):
            screen({'pairs': [held]}, banned)


class BundleTests(unittest.TestCase):
    def setUp(self):
        (ROOT / '.tmp').mkdir(exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=ROOT / '.tmp')
        self.addCleanup(self.temporary.cleanup)
        self.directory = Path(self.temporary.name)
        self.kit = fixture_kit(self.directory / 'kit')
        self.args = SimpleNamespace(login_python=sys.executable, compute_python=sys.executable,
                                    dry_run=True, base='synthetic/stub', kit=str(self.kit))

    def fixture(self):
        run = CensusRehearsal(self.args, self.directory / 'case')
        run.environment['AUDIT_FAKE_DEFER'] = '1'
        return run

    def test_queued_round_has_parallel_pinned_cpu_jobs_a_sweep_and_duplicate_guard(self):
        run = self.fixture()
        self.assertEqual(run.run(), 0, run.log.read_text())
        rows = run.shape(run.rows())
        self.assertEqual(len(rows), 7)
        for row in rows[1:-1]:
            self.assertEqual(dependency(row), 'afterok:1001')
            self.assertIn('--kill-on-invalid-dep=yes', row['arguments'])
            self.assertIn('--qos=background', row['arguments'])
            self.assertIn('--constraint=standard', row['arguments'])
            self.assertIn('--account=NRLMR57635502', row['arguments'])
            self.assertIn('--time=03:55:00', row['arguments'])
        self.assertIn('--qos=transfer', rows[0]['arguments'])
        self.assertEqual(dependency(rows[-1]), 'afterok:1002:1003:1004:1005:1006')
        self.assertIn('--time=00:30:00', rows[-1]['arguments'])
        for row in rows:
            self.assertIn('--comment=project=model-audit', row['arguments'])
            self.assertTrue(row['cwd'].startswith(str(run.results / 'submissions')))
            self.assertEqual(row['environment']['AUDIT_PINNED_ROUND'], row['cwd'])
        # One pinned copy serves the whole submission.
        self.assertEqual(len({row['cwd'] for row in rows}), 1)
        self.assertNotEqual(run.call(['./round.sh', '--only', '40-submit.sh'], run.round), 0)
        self.assertEqual(len(run.rows()), 7)
        self.assertIn('already submitted', run.log.read_text())
        self.assertEqual([row['environment']['AUDIT_PAIR'] for row in rows[1:-1]], ['1', '2', '3', '4', '5'])

    def test_bundle_excludes_credentials_and_prints_plain_short_run(self):
        run = self.fixture()
        self.assertFalse((run.bundle / 'model-audit-round.sh').exists())
        head, payload = (run.bundle / BUNDLE).read_bytes().split(b'__PAYLOAD__\n', 1)
        self.assertIn(b"[ \"${1:-}\" = '2' ]", head)
        self.assertIn(b'folder=$WORKDIR/model-audit/rounds/2/scripts', head)
        self.assertIn(b'else export WORKDIR=/p/work1/sdegan; echo "workdir: $WORKDIR from the systems table"', head)
        self.assertNotIn(b'$HOME', head)
        self.assertNotIn(b'hf-secret-fixture', payload)
        # Open only the locally built script; all scheduler work stays deferred.
        self.assertEqual(run.run(), 0)
        stamp = (run.round / 'BUILD-STAMP.txt').read_text().strip()
        self.assertEqual(stamp, hashlib.sha256(payload).hexdigest())
        cards = (run.directory / 'builder.log').read_text()
        self.assertIn('Token: hpc-send push', cards)
        run_line = next(line for line in cards.splitlines() if line.startswith('Run: '))
        script = run_line.split(' -- ', 1)[1].strip("'")
        self.assertLess(len(script), 50)
        self.assertEqual(script, '/p/work1/sdegan/model-audit-census.sh 2')
        copy_line = next(line for line in cards.splitlines() if line.startswith('Copy: '))
        self.assertTrue(copy_line.endswith('/model-audit-census.sh /p/work1/sdegan/model-audit-census.sh'))
        self.assertNotIn('model-audit-round.sh', cards)
        self.assertNotIn('=', script)
        self.assertNotIn(' && ', script)

    def test_raider_bundle_uses_transfer_partition_and_background_qos(self):
        result = subprocess.run([sys.executable, str(ROUND / 'bundle.py'), 'build', '--round', '2', '--system', 'raider',
                                 '--kit', str(self.kit), '--out', str(self.directory / 'raider'), '--needs', NEEDS],
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        self.assertEqual(result.returncode, 0, result.stdout.decode())
        self.assertIn('--system raider', result.stdout.decode())
        self.assertIn('Preference: raider background CPU', result.stdout.decode())
        folder = opened(self.directory / 'raider' / BUNDLE, self.directory / 'raider-open')
        words = subprocess.run(['bash', '-c', '. ./system.sh; printf "%s|%s" "$AUDIT_TRANSFER_ARGS" '
                                '"$AUDIT_BACKGROUND_ARGS"'], cwd=str(folder), stdout=subprocess.PIPE,
                               universal_newlines=True, check=True).stdout
        transfer, background = (part.splitlines() for part in words.split('|'))
        self.assertEqual(transfer, ['--qos=transfer', '--partition=transfer', '--constraint=xfer'])
        self.assertEqual(background, ['--qos=background', '--constraint=standard'])
        self.assertTrue((folder / 'systems.json').is_file())

    def test_round_end_uses_the_bundled_system(self):
        run = self.fixture()
        self.assertEqual(run.run(), 0)
        (run.round / 'system.sh').write_text('export HPC_SYSTEM=raider\n')
        (run.round / '10-install-kit.sh').write_text('#!/bin/bash\necho local-install-check\n')
        self.assertEqual(run.call(['./round.sh', '--only', '10-install-kit.sh'], run.round), 0)
        drop = (run.directory / 'outbox/round-2-only-10-install-kit-end.log').read_text()
        self.assertIn('system: raider\n', drop)
        self.assertIn('VERDICT round 2 OK', drop)

    def test_the_hashed_guard_screens_like_the_names(self):
        from lineage import guard_text
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        guard = Path(folder.name) / 'maker-guard.sha256'
        guard.write_text(guard_text(ROOT / 'hpc/banned-makers.txt'))
        self.assertNotIn('deepseek', guard.read_text())
        record = manifest()
        self.assertEqual(screen(record, guard), 5)
        planted = json.loads(json.dumps(record))
        planted['pairs'][0]['modified']['declared_base_model'] = ['Qwen/Qwen2.5-7B']
        with self.assertRaises(ValueError) as held:
            screen(planted, guard)
        self.assertIn('pair 1 (guard ', str(held.exception))
        self.assertNotIn('qwen', str(held.exception).lower())
        self.assertNotIn('gemma', str(held.exception).lower())

    def test_the_install_step_clears_a_stale_list_beside_the_scripts(self):
        run = self.fixture()
        self.assertEqual(run.run(), 0)
        stale = run.round / 'banned-makers.txt'
        stale.write_text('# left by an earlier round\n')
        self.assertEqual(run.call(['./round.sh', '--only', '10'], run.round), 0)
        self.assertFalse(stale.exists())
        self.assertFalse((run.round / 'maker-guard.sha256').read_text().count('deepseek'))

    def test_the_timing_step_queues_one_small_job_by_name(self):
        run = self.fixture()
        self.assertEqual(run.run(), 0)
        self.assertEqual(run.call(['./round.sh', 'timing'], run.round), 0)
        log = (run.directory / 'outbox/round-2-only-15-timing-end.log').read_text()
        self.assertIn('timing job: ', log)
        self.assertIn('VERDICT timing OK', log)
        self.assertNotIn('15-timing', (run.directory / 'outbox/round-2-end.log').read_text())

    def test_the_probe_step_queues_one_transfer_job_by_name(self):
        run = self.fixture()
        self.assertEqual(run.run(), 0)
        self.assertEqual(run.call(['./round.sh', 'probe'], run.round), 0)
        log = (run.directory / 'outbox/round-2-only-16-probe-end.log').read_text()
        self.assertIn('probe job: ', log)
        self.assertIn('VERDICT probe OK', log)
        self.assertNotIn('16-probe', (run.directory / 'outbox/round-2-end.log').read_text())
        # The probe asks the transfer queue, as the download does.
        rows = [row for row in run.rows() if '--job-name=model-audit-census-probe' in row['arguments']]
        self.assertEqual(len(rows), 1, run.rows())
        self.assertIn('--qos=transfer', rows[0]['arguments'])
        self.assertIn('--time=00:10:00', rows[0]['arguments'])

    def test_the_compute_probe_queues_the_same_job_on_the_background_queue(self):
        """Wheat's login node opened the image and its transfer node did not; the compute nodes get the same
        ten-minute question before eight compares depend on the answer."""
        run = self.fixture()
        self.assertEqual(run.run(), 0)
        self.assertEqual(run.call(['./round.sh', 'probe-compute'], run.round), 0)
        log = (run.directory / 'outbox/round-2-only-16-probe-compute-end.log').read_text()
        self.assertIn('probe job: ', log)
        self.assertIn('probe queue: background', log)
        self.assertIn('VERDICT probe OK', log)
        rows = [row for row in run.rows() if '--job-name=model-audit-census-probe-compute' in row['arguments']]
        self.assertEqual(len(rows), 1, run.rows())
        self.assertIn('--qos=background', rows[0]['arguments'])
        self.assertIn('--time=00:10:00', rows[0]['arguments'])
        probe = (ROUND / 'jobs/probe.sh').read_text()
        self.assertIn('if standalone_python; then', probe)
        self.assertIn('echo "pypi answers: $pypi"', probe)
        env = (ROUND / 'env.sh').read_text()
        self.assertIn('standalone_python() {', env)
        self.assertIn('tar -xzf "$tar" -C "$part" --strip-components=1', env)
        self.assertIn('dir=$WORKDIR/model-audit/python/${sum:0:16}', env)

    def test_a_step_may_be_named_by_its_number(self):
        run = self.fixture()
        self.assertEqual(run.run(), 0)
        (run.round / '10-install-kit.sh').write_text('#!/bin/bash\necho local-install-check\n')
        self.assertEqual(run.call(['./round.sh', '--only', '10'], run.round), 0)
        drop = (run.directory / 'outbox/round-2-only-10-install-kit-end.log').read_text()
        self.assertIn('VERDICT round 2 OK', drop)
        self.assertNotEqual(run.call(['./round.sh', '--only', '11'], run.round), 0)

    def test_projection_only_requires_verified_batch(self):
        run = self.fixture()
        result = run.call([str(run.bundle / BUNDLE), '2', 'projection'])
        self.assertNotEqual(result, 0)
        self.assertEqual(run.rows(), [])
        self.assertIn('projection-only submit missing:', run.log.read_text())

    def test_piece_retry_submits_one_compare_using_its_verified_download(self):
        run = self.fixture()
        self.assertEqual(run.run(), 0)
        cwd = Path.cwd()
        try:
            os.chdir(run.round)
            with patch.dict(os.environ, run.environment):
                os.environ['AUDIT_WORK'] = str(run.results)
                census = module('census')
                row = census.pair(3)
                for side, directory in zip(('original', 'modified'), census.paths(3)):
                    directory.mkdir(parents=True)
                    path = directory / 'stub.txt'
                    path.write_text('verified download')
                    (directory / 'download-manifest.json').write_text(json.dumps({
                        'base': row[side]['hub_id'], 'revision': row[side]['revision'], 'files': [{
                            'path': path.name, 'size': path.stat().st_size, 'sha256': census.checksum(path)}]}))
        finally:
            os.chdir(cwd)
        (run.results / 'state/download.done').touch()
        rounds = self.directory / 'retry-sources'
        shutil.copytree(ROUND, rounds / '2', ignore=shutil.ignore_patterns('__pycache__'))
        with (rounds / '2/login.py').open('a') as stream:
            stream.write("\nprint('piece retry')\n")
        run.build(rounds)
        self.assertEqual(run.call([str(run.bundle / BUNDLE), '2', 'projection', '3']), 0, run.log.read_text())
        rows = run.rows()
        self.assertEqual(len(rows), 9)
        self.assertEqual(rows[-2]['environment']['AUDIT_PAIR'], '3')
        self.assertTrue(rows[-2]['arguments'][-1].endswith('/jobs/project.sh'))
        self.assertIsNone(dependency(rows[-2]))
        self.assertTrue(rows[-1]['arguments'][-1].endswith('/jobs/sweep.sh'))
        self.assertEqual(dependency(rows[-1]), 'afterok:' + rows[-2]['job'])

    def test_piece_past_the_batch_is_refused(self):
        run = self.fixture()
        self.assertEqual(run.call([str(run.bundle / BUNDLE), '2', 'projection', '6']), 2)
        self.assertEqual(run.rows(), [])
        result = subprocess.run([sys.executable, str(ROUND / 'bundle.py'), 'build', '--round', '2', '--projection-only',
                                 '--piece', '6', '--kit', str(self.kit), '--out', str(self.directory / 'six'),
                                 '--needs', NEEDS], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                universal_newlines=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('--piece must be 1 through 5', result.stdout)

    def test_rebuilt_stamp_keeps_earlier_ids(self):
        run = self.fixture()
        self.assertEqual(run.run(), 0)
        first = (run.round / 'BUILD-STAMP.txt').read_text().strip()
        rounds = self.directory / 'sources'
        shutil.copytree(ROUND, rounds / '2', ignore=shutil.ignore_patterns('__pycache__'))
        with (rounds / '2/login.py').open('a') as stream:
            stream.write("\nprint('new login check')\n")
        run.build(rounds)
        self.assertEqual(run.run(), 0)
        second = (run.round / 'BUILD-STAMP.txt').read_text().strip()
        self.assertNotEqual(first, second)
        state = (run.results / 'state/round-2-submissions').read_text()
        self.assertIn(first, state)
        self.assertIn(second, state)
        self.assertEqual(len(run.rows()), 14)


class ReadTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(dir=ROOT / '.tmp')
        self.addCleanup(self.temporary.cleanup)
        self.directory = Path(self.temporary.name)
        self.module = module('measure')
        self.base = self.directory / 'original'
        self.base.mkdir()
        (self.base / 'stub.txt').write_text('tiny original')
        (self.base / 'download-manifest.json').write_text(json.dumps({'base': 'fixture/base', 'files': [
            {'path': 'stub.txt', 'size': 13, 'sha256': self.module.checksum(self.base / 'stub.txt')}]}))
        self.env = patch.dict(os.environ, {'AUDIT_ORIGINAL': str(self.base), 'AUDIT_BASE': 'fixture/base',
            'AUDIT_DERIVED': str(self.directory / 'derived'), 'AUDIT_MEASUREMENT': str(self.directory / 'report.json'),
            'AUDIT_JOB_STARTED': str(time.time()), 'AUDIT_WORK': str(self.directory)})
        self.env.start()
        self.addCleanup(self.env.stop)

    def test_a_published_config_with_a_trailing_comma_is_read_and_recorded(self):
        # Round 13 pair 5 on Blueback died in the metadata step: the original's generation_config.json
        # (mistralai, 1483f238) ends its last field with a comma. The compare reads it anyway and keeps the fact.
        folder = self.directory / 'pinned'
        folder.mkdir()
        (folder / 'config.json').write_text('{"model_type": "mistral"}')
        (folder / 'generation_config.json').write_text('{\n  "bos_token_id": 1,\n  "temperature": 0.15,\n}\n')
        model = {'hub_id': 'maker/model', 'revision': 'abc'}
        documents, record = self.module.metadata(folder, model)
        self.assertEqual(documents['generation_config.json'], {'bos_token_id': 1, 'temperature': 0.15})
        self.assertEqual(list(record['invalid_json']), ['generation_config.json'])
        self.assertIn('trailing comma dropped', record['invalid_json']['generation_config.json'])
        (folder / 'generation_config.json').write_text('{"temperature": }')
        documents, record = self.module.metadata(folder, model)
        self.assertEqual(documents['generation_config.json'], {})
        self.assertTrue(record['invalid_json']['generation_config.json'].endswith('not read'))

    def test_old_state_markers_do_not_enter_freshness_inputs(self):
        (self.directory / 'state/projection').mkdir(parents=True)
        prior = self.directory / 'state/projection/context.json'
        prior.write_text('{}')
        os.utime(prior, (1, 1))
        self.assertEqual(self.module.round_inputs(), [])
        self.assertEqual(self.module.measurement([], lambda args: 0), 0)

    def test_stale_checkpoint_and_report_name_offending_path(self):
        for path in (self.directory / 'derived/stub.txt', self.directory / 'report.json'):
            path.parent.mkdir(exist_ok=True)
            path.write_text('old')
            os.utime(path, (1, 1))
            with self.assertRaisesRegex(ValueError, str(path)):
                self.module.measurement([], lambda args: 0)
            path.unlink()

    def test_corrupt_original_and_failed_comparison_propagate(self):
        with self.assertRaises(SystemExit) as error:
            self.module.measurement([], lambda args: 23)
        self.assertEqual(error.exception.code, 23)
        census = module('census')
        model = {'hub_id': 'fixture/base', 'revision': 'r' * 40}
        record = json.loads((self.base / 'download-manifest.json').read_text())
        record['revision'] = model['revision']
        (self.base / 'download-manifest.json').write_text(json.dumps(record))
        census.verify(self.base, model)
        (self.base / 'stub.txt').write_text('tampered')
        with self.assertRaisesRegex(ValueError, 'snapshot checksum differs'):
            census.verify(self.base, model)

    def test_lfs_and_git_blob_must_match(self):
        download = module('download')
        path = self.base / 'stub.txt'
        value = path.read_bytes()
        row = {'path': path.name, 'size': len(value), 'lfs_sha256': hashlib.sha256(value).hexdigest()}
        self.assertEqual(download.check_file(path, row), row['lfs_sha256'])
        row['lfs_sha256'] = 'bad'
        with self.assertRaisesRegex(ValueError, 'LFS checksum'):
            download.check_file(path, row)
        row['lfs_sha256'] = None
        row['git_blob_id'] = hashlib.sha1(('blob ' + str(len(value)) + '\0').encode() + value).hexdigest()
        download.check_file(path, row)
        row['git_blob_id'] = 'bad'
        with self.assertRaisesRegex(ValueError, 'git object'):
            download.check_file(path, row)

    def test_token_requires_a_regular_private_file(self):
        census = module('census')
        token = self.directory / '.hpc/hf-token'
        token.parent.mkdir()
        token.write_text('fixture-secret')
        with patch.dict(os.environ, {'HOME': str(self.directory)}):
            token.chmod(0o644)
            with self.assertRaisesRegex(ValueError, 'mode-600'):
                census.token()
            token.chmod(0o600)
            self.assertEqual(census.token(), 'fixture-secret')


class TensorPieceTests(unittest.TestCase):
    def test_synthetic_pair_uses_both_audits_and_deletes_only_its_weights(self):
        with tempfile.TemporaryDirectory(dir=ROOT / '.tmp') as temporary:
            directory = Path(temporary)
            work = directory / 'work'
            work.mkdir()
            audit_work = work / 'model-audit/rounds/2'
            report = audit_work / 'measurements/pair-1/weights.json'
            (directory / 'batch.json').write_text(json.dumps(manifest()))
            (directory / 'audit').symlink_to(ROOT / 'audit', target_is_directory=True)
            env = {'WORKDIR': str(work), 'AUDIT_WORK': str(audit_work), 'AUDIT_PAIR': '1',
                   'AUDIT_PIECE_WORK': str(audit_work / 'pieces/pair-1'),
                   'AUDIT_DERIVED': str(audit_work / 'derived/pair-1'), 'AUDIT_MEASUREMENT': str(report),
                   # File times come from the kernel's coarse clock, a few ms behind time.time().
                   'AUDIT_JOB_STARTED': str(time.time() - 1), 'AUDIT_REHEARSAL': '1', 'AUDIT_STUB': '1'}
            cwd = Path.cwd()
            try:
                os.chdir(directory)
                with patch.dict(os.environ, env):
                    measure = module('measure')
                    measure.seed_original()
                    census = module('census')
                    row = census.pair(1)
                    original, incoming = census.paths(1)
                    os.environ['AUDIT_BASE'] = row['original']['hub_id']
                    os.environ['AUDIT_ORIGINAL'] = str(original)
                    with patch.object(sys, 'argv', ['measure.py']):
                        measure.main()
                    weights = json.loads(report.read_text())
                    self.assertEqual(weights['summary']['assessment'], 'recipe_match')
                    self.assertEqual(weights['census']['modified']['revision'], row['modified']['revision'])
                    metadata = json.loads((report.parent / 'metadata.json').read_text())
                    self.assertTrue(any(change['class'] == 'explained by re-save' for change in metadata['differences']))
                    self.assertTrue((report.parent / 'card.md').is_file())
                    # The original waits for the sweep; the modified copy and its links are gone.
                    self.assertTrue(original.exists())
                    self.assertFalse(incoming.exists())
                    self.assertFalse(Path(env['AUDIT_DERIVED']).exists())
                    receipt = json.loads((report.parent / 'receipt.json').read_text())
                    self.assertEqual(receipt['deleted_checkpoints'], [str(incoming), env['AUDIT_DERIVED']])
                    self.assertFalse(receipt['shared_original'])
                    self.assertTrue(census.paths(2)[0].exists())
                    self.assertTrue(census.paths(2)[1].exists())
            finally:
                os.chdir(cwd)


class RealNamesTests(unittest.TestCase):
    """The published names of all ten checkpoints: the residual writers the census scores.

    The fixtures hold each pinned revision's safetensors header (names, shapes, shard) and its
    config.json, fetched without weights. A round that only ever saw invented names could score
    the wrong tensors on the cluster, so these pin the count and kind per base.
    """

    WRITERS = {'attention_output', 'feed_forward_down', 'expert_down'}

    def setUp(self):
        sys.path.insert(0, str(ROOT))
        from audit.weights import recipe_table, residual_kinds, tensor_kind
        self.tensor_kind = tensor_kind
        self.table = module('measure').census_kinds(recipe_table())
        self.writers = residual_kinds(self.table)

    def names(self, model):
        record = json.loads((NAMES / (model['revision'][:12] + '.json')).read_text())
        self.assertEqual(record['revision'], model['revision'])
        return record

    def test_each_base_scores_every_text_layer_and_nothing_else(self):
        expected = {'google/gemma-4-31B-it': (60, False), 'google/gemma-3-27b-it': (62, False),
                    'google/gemma-4-E4B-it': (42, False), 'google/gemma-4-26B-A4B-it': (30, True),
                    'mistralai/Mistral-Small-Instruct-2409': (56, False)}
        for pair in manifest()['pairs']:
            record = self.names(pair['original'])
            config = record['config'].get('text_config', record['config'])
            layers, experts = expected[record['hub_id']]
            self.assertEqual(config['num_hidden_layers'], layers, record['hub_id'])
            counts = {}
            for name in record['tensors']:
                kind = self.tensor_kind(name, self.table)
                if kind in self.writers:
                    counts[kind] = counts.get(kind, 0) + 1
                    # Vision, audio and projector weights never count as text residual writers.
                    self.assertNotRegex(name, 'vision|audio|multi_modal|embed_vision', name)
                    self.assertRegex(name, r'(^|\.)layers\.\d+\.', name)
            wanted = {'attention_output': layers, 'feed_forward_down': layers}
            if experts:
                wanted['expert_down'] = layers
            self.assertEqual(counts, wanted, record['hub_id'])
            self.assertTrue(set(counts) <= self.WRITERS)

    def test_packed_expert_outputs_are_named_not_other(self):
        record = self.names(manifest()['pairs'][3]['original'])
        packed = [name for name in record['tensors'] if name.endswith('.experts.down_proj')]
        self.assertEqual(len(packed), 30)
        for name in packed:
            self.assertEqual(self.tensor_kind(name, self.table), 'expert_down')
            self.assertEqual(len(record['tensors'][name]['shape']), 3)
        # The shared table carries the on-disk form too, since the round 2 read-out.
        from audit.weights import recipe_table
        self.assertEqual(self.tensor_kind(packed[0], recipe_table()), 'expert_down')

    def test_each_copy_has_the_same_names_and_shapes_as_its_original(self):
        for pair in manifest()['pairs']:
            original = self.names(pair['original'])['tensors']
            copy = self.names(pair['modified'])['tensors']
            self.assertEqual(set(original), set(copy), pair['modified']['hub_id'])
            for name, row in original.items():
                self.assertEqual(row['shape'], copy[name]['shape'], name)

    def test_largest_tensor_fits_the_lean_budget(self):
        measure = module('measure')
        largest = 0
        for pair in manifest()['pairs']:
            for side in ('original', 'modified'):
                for row in self.names(pair[side])['tensors'].values():
                    count = 1
                    for width in row['shape']:
                        count *= width
                    largest = max(largest, count)
        # Gemma 4 E4B's per-layer embedding table: 2.8 billion values.
        self.assertGreater(largest, measure.LEAN_ELEMENTS)
        self.assertLess(largest * 8, measure.CEILING)


class LeanMeasureTests(unittest.TestCase):
    """The row-block path must give the shared measure's answer for the embeddings it takes."""

    def test_lean_matches_shared_measure(self):
        import torch
        sys.path.insert(0, str(ROOT))
        from audit import weights
        measure = module('measure')
        generator = torch.Generator().manual_seed(3)
        for shape in ((300, 50), (40, 7, 9), (257,)):
            base = torch.randn(shape, generator=generator).to(torch.bfloat16)
            copy = base.clone()
            copy.select(-2 if copy.ndim > 1 else 0, 3).mul_(0.5)
            full, full_vectors = weights.measure_tensor(base, copy, 1e-3, 0)
            lean, lean_vectors = measure.lean_measure(base, copy, 1e-3, 0, chunk=97)
            self.assertTrue(lean.pop('lean'))
            self.assertEqual(set(full), set(lean))
            for key, value in full.items():
                if isinstance(value, float):
                    self.assertAlmostEqual(value, lean[key], delta=1e-6 * max(1.0, abs(value)), msg=key)
                elif isinstance(value, list) and value and isinstance(value[0], float):
                    for left, right in zip(value, lean[key]):
                        self.assertAlmostEqual(left, right, delta=1e-6 * max(1.0, abs(left)), msg=key)
                elif isinstance(value, dict):
                    self.assertEqual(json.dumps(value, sort_keys=True), json.dumps(lean[key], sort_keys=True), key)
                else:
                    self.assertEqual(value, lean[key], key)
            if full_vectors is not None:
                for left, right in zip(full_vectors, lean_vectors):
                    self.assertTrue(torch.equal(left, right))

    def test_nonfinite_inputs_and_shape_change_are_reported_like_the_shared_measure(self):
        import torch
        measure = module('measure')
        base = torch.zeros(6, 4)
        broken = base.clone()
        broken[5, 1] = float('nan')
        self.assertEqual(measure.lean_measure(base, broken, chunk=4)[0]['status'], 'nonfinite')
        self.assertEqual(measure.lean_measure(base, torch.zeros(4, 6))[0]['status'], 'shape_mismatch')

    def test_only_tensors_past_the_switch_take_the_lean_path(self):
        import torch
        from types import ModuleType
        measure = module('measure')
        calls = []
        fake = ModuleType('fake_weights')
        fake.measure_tensor = lambda *args: calls.append('full') or ({}, None)
        with patch.dict(os.environ, {'AUDIT_REHEARSAL': '1', 'AUDIT_LEAN_ELEMENTS': '20'}):
            measure.install_lean(fake)
        fake.measure_tensor(torch.zeros(4, 4), torch.zeros(4, 4))
        row, _ = fake.measure_tensor(torch.zeros(8, 4), torch.ones(8, 4))
        self.assertEqual(calls, ['full'])
        self.assertTrue(row['lean'])


class PinTests2(unittest.TestCase):
    def test_compute_pins_match_round_one_exactly(self):
        def pins(path):
            return [line for line in path.read_text().splitlines() if line and not line.startswith('#')]
        self.assertEqual(pins(ROUND / 'compute-requirements.txt'), pins(ROOT / 'hpc/rounds/1/compute-requirements.txt'))
        self.assertIn('mistral-common==1.8.5', pins(ROUND / 'compute-requirements.txt'))
        self.assertIn('protobuf==6.32.1', pins(ROUND / 'compute-requirements.txt'))
        self.assertIn("huggingface_hub==0.35.3", (ROUND / 'jobs/download.sh').read_text())

    def test_the_download_job_bounds_pip_and_stages_wheels_once_per_system(self):
        """Nautilus 4138542 and 4138717 finished their wheel step and then wrote nothing for three hours,
        pip still alive at the wall. Every step is stamped, each pip call has a bound that names the step
        when it passes, pip's temp sits on the node's disk, and the wheels are staged once per system."""
        env = (ROUND / 'env.sh').read_text()
        self.assertIn('step() {\n    echo "$(date -u +%FT%TZ) step: $*"', env)
        self.assertIn('timeout -k 30 "$limit" "$@" && return 0', env)
        self.assertIn('echo "step over its $limit s bound: $*"', env)
        self.assertIn('export AUDIT_WHEELS=$WORKDIR/model-audit/wheels/$(sha256sum compute-requirements.txt 2>/dev/null | cut -c1-16)', env)
        self.assertIn('if [ -f "$AUDIT_WHEELS/.complete" ]; then', env)
        self.assertIn('bounded 1800 "$1" -m pip download --disable-pip-version-check', env)
        download = (ROUND / 'jobs/download.sh').read_text()
        self.assertIn('tmp=$(mktemp -d /tmp/model-audit-XXXXXX 2>/dev/null) && export TMPDIR=$tmp', download)
        self.assertIn("bounded 600 \"$py\" -m pip install --disable-pip-version-check 'huggingface_hub==0.35.3'", download)
        self.assertIn('stage_wheels "$py"', download)
        self.assertNotIn('"$AUDIT_WORK/wheels"', download)
        self.assertEqual(download.count('step "'), 4)
        self.assertLess(download.index('step "hub fetch: $count pairs"'), download.index('"$py" ./download.py'))
        project = (ROUND / 'jobs/project.sh').read_text()
        self.assertIn('--find-links "$AUDIT_WHEELS"', project)
        self.assertNotIn('$AUDIT_WORK/wheels', project)

    def test_compares_starting_together_build_the_venv_once(self):
        """Six compares released in one second raced the venv build on Blueback (round 9): a mkdir lock serializes it."""
        text = (ROUND / 'jobs/project.sh').read_text()
        self.assertIn('until mkdir "$venv_lock" 2>/dev/null; do', text)
        self.assertLess(text.index('until mkdir "$venv_lock"'), text.index('rm -rf -- "$AUDIT_WORK/venv"'))
        self.assertIn('rmdir "$venv_lock" 2>/dev/null\n', text)
        self.assertIn('taking it over', text)

    def test_the_login_half_of_a_round_asks_the_scheduler_nothing_slow(self):
        """Round 18's verify held the Nautilus login for 294 s of a 328 s card, and round 19's clock put
        296 s of its login half in storage.py (a du over the project tree on Lustre). The login half is
        clocked and keeps syntax, request words, lineage and the Python floor; the storage probe and the
        scheduler's test run in the download job, and a failed submission withdraws what it queued."""
        verify = (ROUND / '20-verify.sh').read_text()
        self.assertNotIn('test_submission', verify)
        self.assertIn('clocked check_submission "$piece" "jobs/$piece.sh"', verify)
        self.assertNotIn('python3 ./storage.py', verify)
        download = (ROUND / 'jobs/download.sh').read_text()
        self.assertIn('python3 ./storage.py', download)
        self.assertLess(download.index('python3 ./storage.py'), download.index('test_submission "$piece"'))
        self.assertIn('took $((SECONDS - t0)) s', verify)
        scheduler = (ROUND / 'scheduler.sh').read_text()
        self.assertIn('check_submission() {', scheduler)
        self.assertIn('cancel_batch() {', scheduler)
        self.assertNotIn('--test-only', scheduler[scheduler.index('check_submission() {'):scheduler.index('cancel_batch() {')])
        download = (ROUND / 'jobs/download.sh').read_text()
        self.assertIn('test_submission "$piece" "jobs/$piece.sh" || echo', download)
        storage = (ROUND / 'storage.py').read_text()
        lfs_branch = storage[storage.index('    else:\n        # Lustre quota alone'):]
        self.assertNotIn("show_storage'", lfs_branch.split('lfs quota unreadable')[0])
        submit = (ROUND / '40-submit.sh').read_text()
        self.assertEqual(submit.count('|| fail_submit'), 4)
        self.assertIn('cancel_batch "${queued[@]}"', submit)
        self.assertLess(submit.index('queued+=("$download")'), submit.index('echo "download job: $download"'))

    def test_no_job_script_sets_its_own_exit_trap(self):
        """The lock's own EXIT trap replaced the reporting kit's, so every compare from round 12 on ended
        without a drop while its sweep ran afterok (Nautilus 4120062-4120068, 10-31). The EXIT trap belongs
        to start_piece and hpc_report_on_exit; a job script never sets or clears one."""
        import re
        for script in sorted((ROUND / 'jobs').glob('*.sh')):
            text = script.read_text()
            self.assertIsNone(re.search(r'^\s*trap\b', text, re.M), script.name)

    def test_six_compares_released_together_build_the_venv_once_and_wait(self):
        """Rehearse the Blueback round 9 start: six compares at once, one build, five waits, six reuse."""
        import subprocess, tempfile, concurrent.futures
        text = (ROOT / 'hpc/rounds/2/jobs/project.sh').read_text()
        start = text.index('    pins=$(sha256sum compute-requirements.txt')
        end = text.index('    "$AUDIT_WORK/venv/bin/python" ./measure.py')
        block = text[start:end]
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            (tmp / 'compute-requirements.txt').write_text('torch==0\n')
            harness = tmp / 'harness.sh'
            harness.write_text('#!/bin/bash\nset -euo pipefail\ncd "$(dirname "$0")"\nexport AUDIT_WORK=$PWD/work AUDIT_WHEELS=$PWD/work/wheels\nmkdir -p "$AUDIT_WORK"\ntrap \'echo "finish $1"\' EXIT\n'
                               'python3() { if [ "${1:-}" = -m ] && [ "${2:-}" = venv ]; then mkdir -p "$3/bin" && printf \'#!/bin/bash\\nsleep 2\\n\' > "$3/bin/python" && chmod +x "$3/bin/python"; else command python3 "$@"; fi; }\n'
                               + block + 'echo "compare $1 done"\n')
            harness.chmod(0o755)
            def run(i):
                return subprocess.run(['bash', str(harness), str(i)], capture_output=True, text=True, timeout=120)
            with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
                results = list(pool.map(run, range(1, 7)))
        out = '\n'.join(r.stdout + r.stderr for r in results)
        self.assertTrue(all(r.returncode == 0 for r in results), out)
        self.assertEqual(out.count('compute venv: building for pins'), 1, out)
        self.assertEqual(out.count('another compare is building it; waiting'), 5, out)
        self.assertEqual(out.count('compute venv: reusing pins'), 5, out)
        self.assertEqual(out.count('finish '), 6, 'the exit trap set before the lock block must survive it: ' + out)

    def test_venv_ready_marker_is_the_pin_hash(self):
        text = (ROUND / 'jobs/project.sh').read_text()
        self.assertIn('pins=$(sha256sum compute-requirements.txt', text)
        self.assertIn('echo "$pins" > "$AUDIT_WORK/venv/.ready"', text)
        self.assertNotIn('touch "$AUDIT_WORK/venv/.ready"', text)
        self.assertNotIn('ulimit -v', text)

    def test_card_tools_load_under_the_pinned_hub_library(self):
        # audit.hub wants a newer hub client than the pins carry; the census loads metadata without it.
        python = ROOT / '.venv-cluster/bin/python'
        try:
            present = python.exists() and os.access(python, os.X_OK)
        except PermissionError:
            present = False
        if not present:
            self.skipTest('no venv built from the cluster pins on this machine')
        code = ("import sys; sys.path.insert(0, 'hpc/rounds/2'); import huggingface_hub, measure; "
                "tools = measure.card_tools(); from audit.hub import SMALL_FILES; "
                "print(huggingface_hub.__version__, callable(tools.card_text), 'config.json' in SMALL_FILES)")
        result = subprocess.run([str(python), '-c', code], cwd=str(ROOT), stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, universal_newlines=True)
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertEqual(result.stdout.split()[-3:], ['0.35.3', 'True', 'True'])
        plain = subprocess.run([str(python), '-c', 'import audit.metadata'], cwd=str(ROOT),
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        # The plain import loads under the pins now that audit.hub defers its httpx import.
        self.assertEqual(plain.returncode, 0, plain.stdout)

    def test_download_skips_the_consolidated_copy(self):
        download = module('download')
        item = lambda name, lfs=True: SimpleNamespace(rfilename=name, size=10, blob_id='b',
                                                      lfs=SimpleNamespace(sha256='s') if lfs else None)
        info = SimpleNamespace(id='x/y', siblings=[item('consolidated.safetensors'), item('model-00001-of-00002.safetensors'),
                                                    item('config.json', False), item('original/params.json', False)])
        self.assertEqual([row['path'] for row in download.selected(info)], ['model-00001-of-00002.safetensors', 'config.json'])


class SyntaxTests(unittest.TestCase):
    def test_shells_and_login_python36_grammar(self):
        for path in ROUND.rglob('*.sh'):
            self.assertEqual(subprocess.call(['bash', '-n', str(path)]), 0, str(path))
        for path in list(ROUND.rglob('*.py')) + [ROOT / 'hpc/lineage.py', ROOT / 'hpc/pin_census.py', ROOT / 'hpc/rehearse_round2.py']:
            ast.parse(path.read_text(), feature_version=(3, 6))
        for path in (ROUND / 'jobs').glob('*.sh'):
            text = path.read_text()
            self.assertIn('set -euo pipefail', text)
            self.assertNotIn('--gres', text)
            self.assertNotIn('nvidia-smi', text)
            # Account and time differ by system; the submit line carries them.
            self.assertNotIn('#SBATCH --account', text)
            self.assertNotIn('#SBATCH --time', text)
        self.assertIn('--mem=60G', (ROUND / 'jobs/project.sh').read_text())
        self.assertEqual(sorted(path.name for path in (ROUND / 'jobs').glob('*.sh')),
                         ['download.sh', 'probe.sh', 'project.sh', 'sweep.sh', 'timing.sh'])


class BatchCountTests(unittest.TestCase):
    """The round and the piece count come from batch.json, never from the kit."""

    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(dir=ROOT / '.tmp')
        self.addCleanup(self.temporary.cleanup)
        self.directory = Path(self.temporary.name)
        self.cwd = Path.cwd()
        self.addCleanup(os.chdir, str(self.cwd))
        os.chdir(str(self.directory))

    def write(self, record):
        (self.directory / 'batch.json').write_text(json.dumps(record))

    def test_count_and_round_follow_the_manifest(self):
        census = module('census')
        self.write(bigger_manifest(9))
        self.assertEqual(census.count(), 9)
        self.assertEqual(census.round_number(), 7)
        self.assertEqual(census.pair(9)['modified']['hub_id'], manifest()['pairs'][3]['modified']['hub_id'] + '-copy-9')
        with self.assertRaisesRegex(ValueError, '1 through 9'):
            census.pair(10)
        for line, wanted in (('round', '7'), ('count', '9')):
            result = subprocess.run([sys.executable, str(ROUND / 'census.py'), line], stdout=subprocess.PIPE,
                                    universal_newlines=True, check=True)
            self.assertEqual(result.stdout.strip(), wanted)

    def test_more_than_twenty_four_pairs_are_refused(self):
        census = module('census')
        self.write(bigger_manifest(25))
        with self.assertRaisesRegex(ValueError, '1 to 24 pairs'):
            census.count()
        self.assertEqual(screen(bigger_manifest(25), ROOT / 'hpc/banned-makers.txt'), 25)

    def test_a_copy_keeps_its_input_folder_when_a_refile_renumbers_it(self):
        census = module('census')
        with patch.dict(os.environ, {'WORKDIR': str(self.directory), 'AUDIT_WORK': str(self.directory / 'r')}):
            self.write(bigger_manifest(9))
            before = {number: census.paths(number)[1] for number in (1, 2, 7)}
            refiled = bigger_manifest(9)
            refiled['pairs'] = [refiled['pairs'][index] for index in (0, 1, 6, 7)]
            self.write(refiled)
            # Batch 2 of round 31 put the seventh copy at number 3, where the withdrawn first chain had left the
            # third copy's download; the folder now follows the copy, not the number.
            self.assertEqual(census.paths(3)[1], before[7])
            self.assertEqual(census.paths(1)[1], before[1])
            self.assertEqual(census.paths(2)[1], before[2])
            self.assertEqual(census.paths(3)[1].parent, self.directory / 'r' / 'inputs')
            self.assertNotIn('pair-', census.paths(3)[1].name)
            self.assertEqual(len({census.paths(number)[1] for number in (1, 2, 3, 4)}), 4)

    def test_shared_originals_group_their_pairs(self):
        census = module('census')
        self.write(bigger_manifest(9))
        with patch.dict(os.environ, {'WORKDIR': str(self.directory), 'AUDIT_WORK': str(self.directory / 'r')}):
            groups = census.originals()
            self.assertEqual([group['pairs'] for group in groups], [[1, 6], [2, 7], [3, 8], [4, 9], [5]])
            self.assertTrue(census.shares_original(6))
            self.assertFalse(census.shares_original(5))
            # Round 12's sweep on Blueback deleted originals round 14 still read: the folder was shared across
            # rounds. An original now lives under its own round's work, where only that round's sweep looks.
            self.assertEqual(census.paths(1)[0].parent, self.directory / 'r' / 'originals')
        for path in sorted(ROUND.glob('*.py')) + sorted(ROUND.glob('*.sh')) + sorted(ROUND.glob('jobs/*.sh')):
            self.assertNotIn("'model-audit/originals'", path.read_text(), path.name)


class SweepTests(unittest.TestCase):
    """An original goes only when every pair that reads it has its reports."""

    def test_sweep_keeps_an_original_until_every_reader_reports(self):
        census = module('census')
        with tempfile.TemporaryDirectory(dir=ROOT / '.tmp') as temporary:
            directory = Path(temporary)
            (directory / 'batch.json').write_text(json.dumps(bigger_manifest(7)))
            work = directory / 'work'
            audit_work = work / 'model-audit/rounds/7'
            cwd = Path.cwd()
            try:
                os.chdir(str(directory))
                with patch.dict(os.environ, {'WORKDIR': str(work), 'AUDIT_WORK': str(audit_work)}):
                    for number in range(1, 8):
                        census.paths(number)[0].mkdir(parents=True, exist_ok=True)
                    def report(number):
                        folder = audit_work / 'measurements' / ('pair-' + str(number))
                        folder.mkdir(parents=True, exist_ok=True)
                        (folder / 'receipt.json').write_text(json.dumps({'pair': number}))
                    for number in (1, 2, 3, 4, 5):
                        report(number)
                    first = census.sweep()
                    kept = {tuple(group['pairs']): group['missing'] for group in first['kept']}
                    self.assertEqual(kept, {(1, 6): [6], (2, 7): [7]})
                    self.assertEqual(sorted(tuple(group['pairs']) for group in first['deleted']), [(3,), (4,), (5,)])
                    self.assertTrue(census.paths(6)[0].is_dir())
                    self.assertFalse(census.paths(3)[0].exists())
                    saved = json.loads((audit_work / 'measurements/sweep.json').read_text())
                    self.assertEqual(saved, json.loads(json.dumps(first)))
                    report(6)
                    report(7)
                    second = census.sweep()
                    self.assertEqual(len(second['deleted']), 2)
                    self.assertEqual(len(second['absent']), 3)
                    self.assertFalse(second['kept'])
                    self.assertFalse(census.paths(6)[0].exists())
            finally:
                os.chdir(str(cwd))

    def test_compare_of_a_shared_original_leaves_it_for_the_sweep(self):
        with tempfile.TemporaryDirectory(dir=ROOT / '.tmp') as temporary:
            directory = Path(temporary)
            work = directory / 'work'
            work.mkdir()
            record = manifest()
            copy = json.loads(json.dumps(record['pairs'][0]))
            copy['modified']['hub_id'] += '-copy'
            record['pairs'] = [record['pairs'][0], copy]
            (directory / 'batch.json').write_text(json.dumps(record))
            (directory / 'audit').symlink_to(ROOT / 'audit', target_is_directory=True)
            audit_work = work / 'model-audit/rounds/2'
            report = audit_work / 'measurements/pair-1/weights.json'
            env = {'WORKDIR': str(work), 'AUDIT_WORK': str(audit_work), 'AUDIT_PAIR': '1',
                   'AUDIT_PIECE_WORK': str(audit_work / 'pieces/pair-1'),
                   'AUDIT_DERIVED': str(audit_work / 'derived/pair-1'), 'AUDIT_MEASUREMENT': str(report),
                   # File times come from the kernel's coarse clock, a few ms behind time.time().
                   'AUDIT_JOB_STARTED': str(time.time() - 1), 'AUDIT_REHEARSAL': '1', 'AUDIT_STUB': '1'}
            cwd = Path.cwd()
            try:
                os.chdir(str(directory))
                with patch.dict(os.environ, env):
                    measure = module('measure')
                    measure.seed_original()
                    census = module('census')
                    original = census.paths(1)[0]
                    self.assertEqual(original, census.paths(2)[0])
                    with patch.object(sys, 'argv', ['measure.py']):
                        measure.main()
                    receipt = json.loads((report.parent / 'receipt.json').read_text())
                    self.assertTrue(receipt['shared_original'])
                    self.assertNotIn(str(original), receipt['deleted_checkpoints'])
                    self.assertTrue(original.is_dir())
                    self.assertTrue(census.paths(2)[1].is_dir())
                    record = census.sweep()
                    self.assertEqual(record['kept'][0]['missing'], [2])
                    self.assertTrue(original.is_dir())
            finally:
                os.chdir(str(cwd))


class SystemsTableTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(dir=ROOT / '.tmp')
        self.addCleanup(self.temporary.cleanup)
        self.directory = Path(self.temporary.name)
        self.kit = fixture_kit(self.directory / 'kit')

    def build(self, *extra, round_number='2'):
        # The needs line names the system's own subproject, as the desk requires.
        needs = NEEDS
        if '--system' in extra:
            system = extra[extra.index('--system') + 1]
            if system in SYSTEMS:
                needs = NEEDS.replace(SYSTEMS['nautilus']['subproject'], SYSTEMS[system]['subproject'])
        return subprocess.run([sys.executable, str(ROUND / 'bundle.py'), 'build', '--round', round_number,
                               '--kit', str(self.kit), '--out', str(self.directory / 'out'), '--needs', needs]
                              + list(extra), stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                              universal_newlines=True)

    def test_every_entry_is_complete_and_the_builder_reads_it(self):
        sys.path.insert(0, str(ROUND))
        import bundle
        table = json.loads((ROOT / 'hpc/systems.json').read_text())
        self.assertEqual(set(table), {'nautilus', 'raider', 'jean', 'wheat', 'fran', 'blueback', 'makau'})
        for name in table:
            entry = bundle.system_entry(table, name)
            self.assertLess(len(entry['work'] + '/model-audit-census.sh 24'), 50, name)
        self.assertEqual(table['wheat']['scheduler'], 'pbs')
        self.assertEqual(table['jean']['transfer_time_limit'], '23:55:00')

    def test_verify_refuses_an_old_python_without_an_image(self):
        text = (ROUND / '20-verify.sh').read_text()
        self.assertIn('build this system with --image', text)
        self.assertLess(text.index('AUDIT_IMAGE:-'), text.index('floor_python ||'))
        env = (ROUND / 'env.sh').read_text()
        self.assertIn('sys.version_info < (3, 10)', env)
        # Nautilus names no interpreter in the table and its login python3 is 3.6: the check reads the module
        # the jobs load, in a subshell, so the login shell keeps its own Python; the home rehearsal reads python3.
        floor = env[env.index('floor_python() {'):env.index('python_module() {')]
        self.assertIn('"$AUDIT_PYTHON" -c "$floor"', floor)
        # The home rehearsal reaches the floor with its own python3 before the table's interpreter is consulted
        # (round 22's Blueback rehearsal failed at home looking for /usr/bin/python3.11).
        self.assertLess(floor.index('AUDIT_REHEARSAL:-0'), floor.index('"$AUDIT_PYTHON" -c "$floor"'))
        self.assertIn('( python_module && python3 -c "$floor" )', floor)
        self.assertLess(floor.index('AUDIT_REHEARSAL:-0}" = 1'), floor.index('( python_module'))
        module = env[env.index('python_module() {'):env.index('compute_python() {')]
        self.assertIn('module load "$candidate"', module)
        # Raider and the other Cray systems name the module cray-python
        self.assertIn("module -t avail python/3.1 cray-python/3.1", module)
        self.assertIn("grep -E '^(cray-)?python/3\\.1'", module)
        compute = env[env.index('compute_python() {'):]
        self.assertIn('python_module || return 1', compute)
        self.assertNotIn('module load', compute)

    def test_blueback_bundle_names_its_compute_python(self):
        result = self.build('--system', 'blueback')
        self.assertEqual(result.returncode, 0, result.stdout)
        folder = opened(self.directory / 'out' / BUNDLE, self.directory / 'blueback-open')
        words = subprocess.run(['bash', '-c', '. ./system.sh; printf "%s|%s|%s" "$AUDIT_TRANSFER_ARGS" '
                                '"$AUDIT_BACKGROUND_ARGS" "$AUDIT_PYTHON"'], cwd=str(folder), stdout=subprocess.PIPE,
                               universal_newlines=True, check=True).stdout
        transfer, background, python = words.split('|')
        self.assertEqual(transfer.splitlines(), ['--partition=general', '--qos=transfer', '--constraint=xfer'])
        self.assertEqual(background.splitlines(), ['--partition=general', '--qos=background', '--constraint=standard'])
        self.assertEqual(python, '/usr/bin/python3.11')
        env = (ROUND / 'env.sh').read_text()
        self.assertIn('ln -sfn "$found" "$AUDIT_WORK/pybin/python3"', env)
        self.assertLess(env.index('AUDIT_PYTHON:-'), env.index('module load'))
        self.assertIn('compute_python', (ROUND / 'jobs/timing.sh').read_text())

    def test_a_checkpoint_fetch_gets_three_tries_and_names_the_hub_error(self):
        sys.path.insert(0, str(ROUND))
        import download
        calls = []

        def flaky(hub_id, **kwargs):
            calls.append(hub_id)
            if len(calls) < 3:
                try:
                    raise ConnectionError('connection reset')
                except ConnectionError as cause:
                    raise OSError('cannot find the appropriate snapshot folder') from cause
        original = download.snapshot_download
        download.snapshot_download = flaky
        try:
            with contextlib.redirect_stdout(io.StringIO()) as out:
                download.fetch({'hub_id': 'maker/model', 'revision': 'a' * 40}, Path('/nonexistent'), [], None, pause=0)
            self.assertEqual(len(calls), 3)
            self.assertIn('hub fetch 2 of 3 failed', out.getvalue())
            self.assertIn('ConnectionError: connection reset', out.getvalue())
            calls.clear()
            download.snapshot_download = lambda hub_id, **kwargs: (_ for _ in ()).throw(OSError('down'))
            with contextlib.redirect_stdout(io.StringIO()), self.assertRaises(ValueError) as refused:
                download.fetch({'hub_id': 'maker/model', 'revision': 'a' * 40}, Path('/nonexistent'), [], None, pause=0)
            self.assertIn('after 3 tries', str(refused.exception))
        finally:
            download.snapshot_download = original

    def test_kit_files_move_into_place_instead_of_overwriting_a_running_one(self):
        text = (ROUND / '10-install-kit.sh').read_text()
        self.assertNotIn('cp kit/* ', text)
        self.assertIn('mv -f "$HOME/metoc/jobs/hpc/.${file##*/}.new" "$HOME/metoc/jobs/hpc/${file##*/}"', text)

    def test_makau_bundle_names_the_gres_every_job_there_must_carry(self):
        result = self.build('--system', 'makau')
        self.assertEqual(result.returncode, 0, result.stdout)
        folder = opened(self.directory / 'out' / BUNDLE, self.directory / 'makau-open')
        words = subprocess.run(['bash', '-c', '. ./system.sh; printf "%s|%s|%s" "$AUDIT_TRANSFER_ARGS" '
                                '"$AUDIT_BACKGROUND_ARGS" "$AUDIT_PYTHON"'], cwd=str(folder), stdout=subprocess.PIPE,
                               universal_newlines=True, check=True).stdout
        transfer, background, python = words.split('|')
        self.assertEqual(transfer.splitlines(), ['--partition=transfer', '--qos=transfer'])
        self.assertEqual(background.splitlines(), ['--partition=background', '--gres=gpu:h100_nvl:1'])
        self.assertEqual(python, '/usr/bin/python3.11')
        self.assertIn('/p/work/sdegan/model-audit-census.sh', result.stdout)

    def test_sweep_waits_for_every_compare_to_finish_well_and_the_drop_drains_the_log(self):
        submit = (ROUND / '40-submit.sh').read_text()
        self.assertIn('submit_job sweep "afterok:$ids"', submit)
        self.assertNotIn('afterany', submit)
        env = (ROUND / 'env.sh').read_text()
        self.assertIn('PIECE_PIPE=$!', env)
        self.assertLess(env.index('wait "$PIECE_PIPE"'), env.index('tail -n 200 "$PIECE_LOG"'))
        table = json.loads((ROOT / 'hpc/systems.json').read_text())
        table['blueback']['python'] = 'perl'
        path = self.directory / 'systems.json'
        path.write_text(json.dumps(table))
        self.assertIn('python for blueback must be', self.build('--system', 'blueback', '--systems', str(path)).stdout)

    def test_a_system_with_tbd_values_is_refused(self):
        table = json.loads((ROOT / 'hpc/systems.json').read_text())
        table['wheat']['subproject'] = 'TBD'
        table['wheat']['transfer'] = ['TBD']
        path = self.directory / 'systems.json'
        path.write_text(json.dumps(table))
        result = self.build('--system', 'wheat', '--systems', str(path), '--image', '/p/work/sdegan/x.sif',
                            '--image-sha256', 'a' * 64)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('wheat still has TBD values: subproject, transfer', result.stdout)
        self.assertFalse((self.directory / 'out' / BUNDLE).exists())
        # The other systems still build from the same table.
        self.assertEqual(self.build('--systems', str(path)).returncode, 0)

    def test_round_mismatch_unknown_system_and_missing_image_are_refused(self):
        result = self.build('--manifest', str(ROOT / 'data/batches/round-2-batch-1.json'), round_number='5')
        self.assertIn('the batch is round 2, not round 5', result.stdout)
        self.assertIn('unknown system narwhal', self.build('--system', 'narwhal').stdout)
        self.assertIn('jean runs the census inside the image', self.build('--system', 'jean').stdout)

    def test_round_five_builds_from_its_own_manifest(self):
        result = self.build('--system', 'wheat', '--image', '/p/work/sdegan/permafrost-1.sif',
                            '--image-sha256', 'b' * 64, round_number='5')
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("--by-hand 'cd /p/work/sdegan' --by-hand './model-audit-census.sh 5'", result.stdout)
        self.assertIn("'Verify and submit 8 CPU comparisons'", result.stdout)
        self.assertIn('/p/work/sdegan/hf-token', result.stdout)
        folder = opened(self.directory / 'out' / BUNDLE, self.directory / 'open')
        self.assertEqual(json.loads((folder / 'batch.json').read_text())['round'], 5)
        self.assertIn('export AUDIT_SCHEDULER=pbs', (folder / 'system.sh').read_text())
        self.assertTrue((folder / 'image.sh').is_file() and (folder / 'IMAGE.txt').is_file())

    def test_record_reads_the_round_from_the_log(self):
        sys.path.insert(0, str(ROUND))
        import bundle
        log = self.directory / 'end.log'
        log.write_text('project: model-audit\nsystem: wheat\nround: 5\nVERDICT round 5 OK\n')
        bundle.record(SimpleNamespace(log=str(log), system='wheat', out=str(self.directory / 'records')))
        self.assertEqual(json.loads((self.directory / 'records/wheat-round-5.json').read_text())['round'], 5)


class BiggerBatchTests(unittest.TestCase):
    """Nine pairs on Nautilus and the round 2 shape on Wheat's PBS, through the fake schedulers."""

    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(dir=ROOT / '.tmp')
        self.addCleanup(self.temporary.cleanup)
        self.directory = Path(self.temporary.name)
        self.kit = fixture_kit(self.directory / 'kit')

    def args(self, **extra):
        compute = str(CLUSTER_PYTHON) if CLUSTER_PYTHON.exists() else sys.executable
        return SimpleNamespace(login_python=sys.executable, compute_python=compute, dry_run=True,
                               base='synthetic/stub', kit=str(self.kit), **extra)

    def test_nine_pairs_submit_in_parallel_with_a_sweep(self):
        path = self.directory / 'round-7-batch-1.json'
        path.write_text(json.dumps(bigger_manifest(9)))
        run = CensusRehearsal(self.args(manifest=str(path)), self.directory / 'nine')
        rows = run.queued()
        self.assertEqual(len(rows), 11)
        self.assertEqual(dependency(rows[-1]), 'afterok:' + ':'.join(str(job) for job in range(1002, 1011)))
        self.assertIn("'Verify and submit 9 CPU comparisons'", (run.directory / 'builder.log').read_text())
        cards = [path.read_text() for path in (run.home / '.hpc/jobs').glob('round-7-submit-*.json')]
        self.assertTrue(any('Submit the transfer, 9 CPU comparisons and the sweep' in card for card in cards))
        self.assertTrue((run.work / 'model-audit/rounds/7/scripts/batch.json').is_file())

    def test_wheat_without_the_image_carries_its_own_python(self):
        """Wheat's transfer nodes refuse user namespaces (rounds 5 and 30), so the round brings a standalone
        CPython tar instead of the image; the login half only sees the tar, the jobs unpack it."""
        run = CensusRehearsal(self.args(system='wheat'), self.directory / 'wheat-tar')
        rows = run.queued()
        text = run.log.read_text()
        self.assertIn('python tar: ', text)
        self.assertIn('; the jobs unpack it', text)
        self.assertNotIn('VERDICT image', text)
        system = (run.round / 'system.sh').read_text()
        self.assertIn('export AUDIT_PYTHON_TAR=', system)
        self.assertNotIn('AUDIT_PYTHON=', system.replace('AUDIT_PYTHON_TAR', ''))
        self.assertNotIn('AUDIT_IMAGE', system)
        self.assertEqual(rows[0]['arguments'][rows[0]['arguments'].index('-q') + 1], 'transfer')
        self.assertIn('select=1:ncpus=92:mpiprocs=1', rows[1]['arguments'])
        self.assertEqual(len(rows), run.count + 2)
        result = CensusRehearsal(self.args(system='wheat'), self.directory / 'wheat-bare')
        result.python_tar = False
        built = result.build(check=False)
        self.assertIn('wheat carries its own Python; give --python-tar', built.stdout)

    def test_wheat_queues_the_same_shape_through_pbs_and_the_image(self):
        if not CLUSTER_PYTHON.exists():
            self.skipTest('the image check needs the venv built from the cluster pins')
        run = CensusRehearsal(self.args(system='wheat', image=True), self.directory / 'wheat')
        rows = run.queued()
        text = run.log.read_text()
        self.assertIn('PBS request: qsub -v HPC_PROJECT=model-audit,', text)
        self.assertIn('VERDICT image OK', text)
        for row in rows:
            self.assertEqual(row['scheduler'], 'pbs')
            arguments = row['arguments']
            self.assertEqual(arguments[arguments.index('-A') + 1], 'NRLMR5762B403')
            self.assertTrue(arguments[arguments.index('-v') + 1].startswith('HPC_PROJECT=model-audit,'))
        self.assertEqual(rows[0]['arguments'][rows[0]['arguments'].index('-q') + 1], 'transfer')
        self.assertIn('select=1:ncpus=1', rows[0]['arguments'])
        self.assertIn('select=1:ncpus=92:mpiprocs=1', rows[1]['arguments'])
        self.assertIn('select=1:ncpus=92:mpiprocs=1', rows[-1]['arguments'])
        self.assertFalse(any('mem=' in word for word in rows[1]['arguments']))
        self.assertIn('walltime=00:30:00', rows[-1]['arguments'])
        self.assertTrue(rows[0]['job'].endswith('.fake-pbs'))
        self.assertEqual(run.call([str(run.binary / 'sbatch'), '--run-pending']), 0, run.log.read_text())
        rows = run.rows()
        self.assertTrue(all(row['status'] == 'finished' for row in rows), run.log.read_text())
        self.assertIn('image: permafrost-rehearsal.sif', Path(rows[1]['log']).read_text())
        self.assertFalse(run.sweep()['kept'])


class ProbeTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(dir=ROOT / '.tmp')
        self.addCleanup(self.temporary.cleanup)
        self.directory = Path(self.temporary.name)
        (self.directory / 'batch.json').write_text(json.dumps(manifest()))
        self.cwd = Path.cwd()
        self.addCleanup(os.chdir, str(self.cwd))
        os.chdir(str(self.directory))
        self.body = b'{"bos_token_id": 2}\n'
        blob = hashlib.sha1(('blob ' + str(len(self.body)) + '\0').encode() + self.body).hexdigest()
        item = lambda name, size: SimpleNamespace(rfilename=name, size=size, blob_id=blob, lfs=None)
        self.info = SimpleNamespace(siblings=[item('config.json', 900), item('generation_config.json', len(self.body)),
                                              item('model.safetensors', 10 ** 9), item('sub/x.json', 1)])

    def api(self, error=None):
        info = self.info

        class API:
            def model_info(self, *args, **kwargs):
                if error:
                    raise error
                return info
        return API()

    def test_probe_prints_ok_with_the_bytes_and_the_original(self):
        download = module('download')
        fetched = []

        def fetch(repo, revision=None, token=None, local_dir=None, allow_patterns=None, max_workers=None):
            fetched.append(allow_patterns)
            Path(local_dir).mkdir(parents=True, exist_ok=True)
            (Path(local_dir) / allow_patterns[0]).write_bytes(self.body)
        with patch.dict(os.environ, {'AUDIT_WORK': str(self.directory)}), patch.object(download, 'snapshot_download', fetch), \
                patch('builtins.print') as printed:
            download.probe(self.api(), 'token')
        self.assertEqual(fetched, [['generation_config.json']])
        lines = [call.args[0] for call in printed.call_args_list]
        self.assertEqual(lines[-1], 'PROBE OK {} google/gemma-4-31B-it'.format(len(self.body)))
        self.assertFalse((self.directory / 'probe').exists())

    def test_probe_failure_prints_one_parsed_line_and_exits(self):
        download = module('download')
        with patch.dict(os.environ, {'AUDIT_WORK': str(self.directory)}), patch('builtins.print') as printed:
            with self.assertRaises(SystemExit) as stopped:
                download.probe(self.api(OSError('cannot create SSL context')), 'token')
        self.assertNotEqual(stopped.exception.code, 0)
        first = printed.call_args_list[0].args[0]
        self.assertEqual(first, 'PROBE FAIL OSError: cannot create SSL context')


class GuardTests(unittest.TestCase):
    def shell(self, function, call, env):
        source = (ROUND / 'env.sh').read_text()
        import re
        body = re.search(r'^' + function + r'\(\) \{\n.*?^\}\n', source, re.S | re.M).group(0)
        return subprocess.run(['bash', '-c', 'set -euo pipefail\n' + body + call], env=dict(os.environ, **env),
                              stdout=subprocess.PIPE, universal_newlines=True, check=True).stdout

    def test_fips_guard_is_a_no_op_when_fips_is_off_and_sets_the_default_provider_when_on(self):
        with tempfile.TemporaryDirectory(dir=ROOT / '.tmp') as temporary:
            flag = Path(temporary) / 'fips_enabled'
            flag.write_text('0\n')
            env = {'FIPS_PROC_FILE': str(flag), 'AUDIT_WORK': temporary, 'HPC_JOB_ID': '77'}
            out = self.shell('fips_guard', 'fips_guard; echo "conf=${OPENSSL_CONF:-none}"\n', env)
            self.assertEqual(out, 'fips: off, nothing applied\nconf=none\n')
            flag.write_text('1\n')
            out = self.shell('fips_guard', 'fips_guard; echo "$OPENSSL_CONF $APPTAINERENV_OPENSSL_CONF"\n', env)
            conf = Path(temporary) / 'fips/openssl-77.cnf'
            self.assertIn('fips: on', out)
            self.assertIn('{0} {0}'.format(conf), out)
            self.assertIn('activate = 1', conf.read_text())

    def test_node_facts_are_single_lines(self):
        out = self.shell('node_facts', 'node_facts {}\n'.format(sys.executable), {})
        lines = out.splitlines()
        self.assertEqual([line.split(':', 1)[0] for line in lines], ['node', 'cores', 'memory', 'python'])
        self.assertTrue(all(len(line) <= 100 for line in lines))


class NamesFixtureTests(unittest.TestCase):
    def test_fixture_matches_the_stored_format_and_skips_existing_files(self):
        import pin_census
        stored = json.loads((NAMES / '419b2efe4219.json').read_text())
        weight_map = {name: row['file'] for name, row in stored['tensors'].items()}
        headers = {}
        for name, row in stored['tensors'].items():
            headers.setdefault(row['file'], {})[name] = {'dtype': row['dtype'], 'shape': row['shape'],
                                                          'data_offsets': [0, 0]}

        def get(hub, repo, revision, filename, limit=None):
            if filename == pin_census.INDEX:
                return json.dumps({'metadata': {}, 'weight_map': weight_map}).encode()
            return json.dumps(stored['config']).encode()
        model = {'hub_id': stored['hub_id'], 'revision': stored['revision']}
        published = sorted(set(weight_map.values()))
        with patch.object(pin_census, 'bounded_get', get), \
                patch.object(pin_census, 'shard_header', lambda hub, repo, revision, shard: dict(headers[shard])), \
                patch.object(pin_census, 'weight_files', lambda hub, repo, revision: list(published)):
            self.assertEqual(pin_census.fixture(object(), model), stored)
            with tempfile.TemporaryDirectory(dir=ROOT / '.tmp') as temporary:
                path = Path(temporary) / 'batch.json'
                record = manifest()
                record['pairs'] = [{'original': model, 'modified': model}]
                path.write_text(json.dumps(record))
                with patch('builtins.print'), \
                        patch.object(pin_census, 'bounded_get', get), \
                        patch.object(pin_census, 'shard_header', lambda hub, repo, revision, shard: dict(headers[shard])), \
                        patch.object(pin_census, 'weight_files', lambda hub, repo, revision: list(published)):
                    written = pin_census.names(path, temporary, hub=object())
                self.assertEqual([item.name for item in written], ['419b2efe4219.json'])
                self.assertEqual(written[0].read_text(), (NAMES / '419b2efe4219.json').read_text())
                with patch('builtins.print'), \
                        patch.object(pin_census, 'bounded_get', get), \
                        patch.object(pin_census, 'shard_header', lambda hub, repo, revision, shard: dict(headers[shard])), \
                        patch.object(pin_census, 'weight_files', lambda hub, repo, revision: list(published)):
                    self.assertEqual(pin_census.names(path, temporary, hub=object()), [])

    def test_one_refused_checkpoint_does_not_stop_the_names_step(self):
        import pin_census
        stored = json.loads((NAMES / '419b2efe4219.json').read_text())
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        directory = Path(temporary.name)
        manifest = directory / 'batch.json'
        other = {'hub_id': 'someone/copy', 'revision': 'b' * 40}
        manifest.write_text(json.dumps({'round': 2, 'batch': 1, 'pairs': [
            {'original': {'hub_id': stored['hub_id'], 'revision': stored['revision']}, 'modified': other},
            {'original': {'hub_id': 'maker/next', 'revision': 'c' * 40}, 'modified': {'hub_id': 'x/y', 'revision': 'd' * 40}}]}))

        def fixture(hub, model):
            if model['revision'] == stored['revision']:
                raise ValueError('2 weight files and no index: several checkpoints under one name')
            tensors = {'a': {'file': 'm.safetensors', 'dtype': 'BF16', 'shape': [2]}}
            if model['revision'] == 'c' * 40:
                # A float8 original without the config block still carries its scales in the names.
                tensors['language_model.model.layers.0.mlp.down_proj.activation_scale'] = {'file': 'm.safetensors', 'dtype': 'BF16', 'shape': [1]}
            return {'hub_id': model['hub_id'], 'revision': model['revision'], 'config': {}, 'tensors': tensors}
        out = directory / 'fixtures'
        with patch.object(pin_census, 'fixture', fixture), self.assertRaisesRegex(ValueError, '2 checkpoint.* refused; pair 1 original: 2 weight files.*; pair 2 original: original is quantised .1 scale tensors'):
            pin_census.names(str(manifest), str(out), hub=object())
        self.assertEqual(sorted(path.name for path in out.iterdir()), ['bbbbbbbbbbbb.json', 'dddddddddddd.json'])

    def test_quantised_originals_and_several_files_without_an_index_are_refused(self):
        import pin_census
        stored = json.loads((NAMES / '419b2efe4219.json').read_text())
        headers = {}
        for name, row in stored['tensors'].items():
            headers.setdefault(row['file'], {})[name] = {'dtype': row['dtype'], 'shape': row['shape'],
                                                          'data_offsets': [0, 0]}
        single = next(iter(headers))
        files = ['odd-name.safetensors']

        def get(hub, repo, revision, filename, limit=None):
            if filename == pin_census.INDEX:
                return None
            return json.dumps({**stored['config'], **extra}).encode()
        model = {'hub_id': stored['hub_id'], 'revision': stored['revision']}
        with patch.object(pin_census, 'bounded_get', get), \
                patch.object(pin_census, 'weight_files', lambda hub, repo, revision: list(files)), \
                patch.object(pin_census, 'shard_header', lambda hub, repo, revision, shard: dict(headers[single])):
            # One weight file under another name is that checkpoint.
            extra = {}
            record = pin_census.fixture(object(), model)
            self.assertEqual({row['file'] for row in record['tensors'].values()}, {'odd-name.safetensors'})
            # Several files and no index are several checkpoints (DarkRomeo88, round 14).
            files.append('second.safetensors')
            with self.assertRaisesRegex(ValueError, 'several checkpoints under one name'):
                pin_census.fixture(object(), model)
            files.clear()
            with self.assertRaisesRegex(ValueError, 'no safetensors weights'):
                pin_census.fixture(object(), model)
            # A quantised original is refused at the names step (finding 37); a quantised copy is not.
            files.append('odd-name.safetensors')
            extra = {'quantization_config': {'quant_method': 'fp8'}}
            with tempfile.TemporaryDirectory(dir=ROOT / '.tmp') as temporary:
                path = Path(temporary) / 'batch.json'
                record = manifest()
                record['pairs'] = [{'original': model, 'modified': model}]
                path.write_text(json.dumps(record))
                with patch('builtins.print'), self.assertRaisesRegex(ValueError, 'original is quantised'):
                    pin_census.names(path, temporary, hub=object())
                copy = {'hub_id': 'owner/copy', 'revision': 'f' * 40}
                record['pairs'] = [{'original': {**model, 'revision': 'e' * 40}, 'modified': copy}]
                path.write_text(json.dumps(record))
                extra = {}
                with patch('builtins.print'):
                    self.assertEqual(len(pin_census.names(path, temporary, hub=object())), 2)

if __name__ == '__main__':
    unittest.main()


class RateLimitWaitTests(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.saved = {key: os.environ.get(key) for key in ('AUDIT_WORK', 'WORKDIR')}
        os.environ['AUDIT_WORK'] = self.folder.name
        os.environ['WORKDIR'] = self.folder.name
        self.addCleanup(self.restore)
        self.download = module('download')

    def restore(self):
        for key, value in self.saved.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value

    def run_fetch(self, errors, tries=1):
        calls = []
        sleeps = []
        directory = os.path.join(self.folder.name, 'fetch')
        os.makedirs(directory)

        def flaky(hub_id, **kwargs):
            calls.append(hub_id)
            if len(calls) <= errors:
                raise Exception('429 Client Error: Too Many Requests for url: x')
            Path(directory, 'config.json').write_text('')

        with patch.object(self.download, 'snapshot_download', flaky), \
                patch.object(self.download.time, 'sleep', sleeps.append), \
                contextlib.redirect_stdout(io.StringIO()):
            self.download.fetch({'hub_id': 'a/b', 'revision': 'r'}, directory,
                                [{'path': 'config.json'}], 'tok', tries=tries, pause=0)
        return calls, sleeps

    def test_two_rate_limits_wait_and_then_return(self):
        calls, sleeps = self.run_fetch(2)
        self.assertEqual(sleeps, [310, 310])
        self.assertEqual(len(calls), 3)

    def test_four_rate_limits_give_up_after_three_waits(self):
        calls = []
        sleeps = []
        directory = os.path.join(self.folder.name, 'fetch')
        os.makedirs(directory)

        def flaky(hub_id, **kwargs):
            calls.append(hub_id)
            raise Exception('429 Client Error: Too Many Requests for url: x')

        with patch.object(self.download, 'snapshot_download', flaky), \
                patch.object(self.download.time, 'sleep', sleeps.append), \
                contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaises((ValueError, Exception)):
                self.download.fetch({'hub_id': 'a/b', 'revision': 'r'}, directory,
                                    [{'path': 'config.json'}], 'tok', tries=1, pause=0)
        self.assertEqual(sleeps, [310, 310, 310])

    def test_other_errors_do_not_wait(self):
        sleeps = []
        directory = os.path.join(self.folder.name, 'fetch')
        os.makedirs(directory)

        def broken(hub_id, **kwargs):
            raise Exception('boom')

        with patch.object(self.download, 'snapshot_download', broken), \
                patch.object(self.download.time, 'sleep', sleeps.append), \
                contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaises(ValueError):
                self.download.fetch({'hub_id': 'a/b', 'revision': 'r'}, directory,
                                    [{'path': 'config.json'}], 'tok', tries=1, pause=0)
        self.assertNotIn(310, sleeps)

    def test_a_silent_partial_return_waits_like_a_rate_limit(self):
        calls = []
        sleeps = []
        directory = os.path.join(self.folder.name, 'fetch')
        os.makedirs(directory)

        def silent(hub_id, **kwargs):
            calls.append(hub_id)
            if len(calls) > 1:
                Path(directory, 'config.json').write_text('')

        with patch.object(self.download, 'snapshot_download', silent), \
                patch.object(self.download.time, 'sleep', sleeps.append), \
                contextlib.redirect_stdout(io.StringIO()):
            self.download.fetch({'hub_id': 'a/b', 'revision': 'r'}, directory,
                                [{'path': 'config.json'}], 'tok', tries=1, pause=0)
        self.assertEqual(sleeps, [310])
        self.assertEqual(len(calls), 2)

    def test_a_silent_partial_return_gives_up_after_three_waits(self):
        calls = []
        sleeps = []
        directory = os.path.join(self.folder.name, 'fetch')
        os.makedirs(directory)

        def silent(hub_id, **kwargs):
            calls.append(hub_id)

        with patch.object(self.download, 'snapshot_download', silent), \
                patch.object(self.download.time, 'sleep', sleeps.append), \
                contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaises((ValueError, Exception)):
                self.download.fetch({'hub_id': 'a/b', 'revision': 'r'}, directory,
                                    [{'path': 'config.json'}], 'tok', tries=1, pause=0)
        self.assertEqual(sleeps, [310, 310, 310])
