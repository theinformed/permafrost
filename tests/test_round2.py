# test_round2.py -- Check census pins, lineage holds and queued CPU pieces.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  test failures before they can become scheduler successes.
# Modified: SDE 2026-10-15  real tensor names, round 1's pins, the lean measure, the census bundle name.
import ast
from datetime import datetime, timezone
import hashlib
import importlib.util
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
from rehearse_round2 import BUNDLE, CensusRehearsal, fixture_kit, NAMES, NEEDS


def module(name):
    spec = importlib.util.spec_from_file_location('census_' + name, ROUND / (name + '.py'))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def manifest():
    return json.loads((ROOT / 'data/batches/round-2-batch-1.json').read_text())


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
            def model_info(self, repo, revision=None):
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

    def test_queued_chain_has_six_pinned_cpu_jobs_and_duplicate_guard(self):
        run = self.fixture()
        self.assertEqual(run.run(), 0, run.log.read_text())
        rows = run.rows()
        self.assertEqual(len(rows), 6)
        self.assertFalse(any(arg.startswith('--dependency') for arg in rows[0]['arguments']))
        for previous, row in zip(rows, rows[1:]):
            self.assertIn('--dependency=afterok:' + previous['job'], row['arguments'])
            self.assertIn('--kill-on-invalid-dep=yes', row['arguments'])
            self.assertIn('--qos=background', row['arguments'])
            self.assertIn('--constraint=standard', row['arguments'])
        for row in rows:
            self.assertIn('--comment=project=model-audit', row['arguments'])
            self.assertTrue(row['cwd'].startswith(str(run.results / 'submissions')))
            self.assertEqual(row['environment']['AUDIT_PINNED_ROUND'], row['cwd'])
        self.assertNotEqual(run.call(['./round.sh', '--only', '40-submit.sh'], run.round), 0)
        self.assertEqual(len(run.rows()), 6)
        self.assertIn('already submitted', run.log.read_text())
        self.assertEqual([row['environment']['AUDIT_PAIR'] for row in rows[1:]], ['1', '2', '3', '4', '5'])

    def test_bundle_excludes_credentials_and_prints_plain_short_run(self):
        run = self.fixture()
        self.assertFalse((run.bundle / 'model-audit-round.sh').exists())
        head, payload = (run.bundle / BUNDLE).read_bytes().split(b'__PAYLOAD__\n', 1)
        self.assertIn(b"[ \"${1:-}\" = '2' ]", head)
        self.assertIn(b'folder=$HOME/model-audit/rounds/2', head)
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
        result = subprocess.run([sys.executable, str(ROUND / 'bundle.py'), 'build', '--system', 'raider',
                                 '--kit', str(self.kit), '--out', str(self.directory / 'raider'), '--needs', NEEDS],
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        self.assertEqual(result.returncode, 0, result.stdout.decode())
        self.assertIn('--system raider', result.stdout.decode())
        env = (ROUND / 'env.sh').read_text().split('queue_args() {', 1)[1].split('mkdir -p', 1)[0]
        self.assertIn('--partition=transfer', env)
        self.assertIn('--qos=$1', env)
        self.assertNotIn('--partition=background', env)

    def test_round_end_uses_the_bundled_system(self):
        run = self.fixture()
        self.assertEqual(run.run(), 0)
        (run.round / 'system.sh').write_text('export HPC_SYSTEM=raider\n')
        (run.round / '10-install-kit.sh').write_text('#!/bin/bash\necho local-install-check\n')
        self.assertEqual(run.call(['./round.sh', '--only', '10-install-kit.sh'], run.round), 0)
        drop = (run.directory / 'outbox/round-2-only-10-install-kit-end.log').read_text()
        self.assertIn('system: raider\n', drop)
        self.assertIn('VERDICT round 2 OK', drop)

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
        self.assertEqual(len(rows), 7)
        self.assertEqual(rows[-1]['environment']['AUDIT_PAIR'], '3')
        self.assertTrue(rows[-1]['arguments'][-1].endswith('/jobs/project.sh'))
        self.assertFalse(any(arg.startswith('--dependency') for arg in rows[-1]['arguments']))

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
        self.assertEqual(len(run.rows()), 12)


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
                   'AUDIT_JOB_STARTED': str(time.time()), 'AUDIT_REHEARSAL': '1', 'AUDIT_STUB': '1'}
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
                    self.assertFalse(original.exists())
                    self.assertFalse(incoming.exists())
                    self.assertFalse(Path(env['AUDIT_DERIVED']).exists())
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
        # The shared table at HEAD alone leaves them unnamed; the census adds the on-disk form.
        from audit.weights import recipe_table
        self.assertEqual(self.tensor_kind(packed[0], recipe_table()), 'other')

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
                    self.assertEqual(value['preserved_equal'], lean[key]['preserved_equal'])
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

    def test_venv_ready_marker_is_the_pin_hash(self):
        text = (ROUND / 'jobs/project.sh').read_text()
        self.assertIn('pins=$(sha256sum compute-requirements.txt', text)
        self.assertIn('echo "$pins" > "$AUDIT_WORK/venv/.ready"', text)
        self.assertNotIn('touch "$AUDIT_WORK/venv/.ready"', text)
        self.assertNotIn('ulimit -v', text)

    def test_card_tools_load_under_the_pinned_hub_library(self):
        # audit.hub wants a newer hub client than the pins carry; the census loads metadata without it.
        python = ROOT / '.venv-cluster/bin/python'
        if not python.exists():
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
        # The plain import is what fails under the pins; this shows the stand-in is needed.
        self.assertNotEqual(plain.returncode, 0)

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
            self.assertIn('--time=03:55:00', text)
        self.assertIn('--mem=60G', (ROUND / 'jobs/project.sh').read_text())


if __name__ == '__main__':
    unittest.main()
