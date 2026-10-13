# test_hpc.py -- Check round packaging and scheduler failures in local folders.
# Created by LT Sean Egan, PhD 2026-10-13
# Modified: SDE 2026-10-13  check login syntax and the protected submission chain.
import ast
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import types
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
NEEDS = 'space=160G hours=0 subproject=NRLMR57635502 queue=background for=4h'


def load_module(name):
    """Read a standalone helper without changing the installed package path."""
    spec = importlib.util.spec_from_file_location(name, ROOT / 'hpc' / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class NeedsTests(unittest.TestCase):
    """The declaration is a small language, not a shell fragment."""

    def test_good_declaration(self):
        fields, size = load_module('needs').parse_needs(NEEDS)
        self.assertEqual(size, 160 * 1024 ** 3)
        self.assertEqual(fields['hours'], '0')

    def test_bad_declarations(self):
        parse = load_module('needs').parse_needs
        for text in ('', NEEDS + ' space=1G', NEEDS + ' deletes=yes', NEEDS.replace('hours=0', 'hours=1'),
                     NEEDS.replace('160G', '3T'), NEEDS.replace('160G', '0G'),
                     NEEDS.replace('for=4h', 'for=5h'), NEEDS.replace('background', 'debug'),
                     NEEDS.replace('NRLMR57635502', 'X;touch'), NEEDS.replace('hours=0 ', '')):
            with self.subTest(text=text), self.assertRaises(ValueError):
                parse(text)

    def test_quota_wrapped_and_starred(self):
        parse = load_module('storage').quota_numbers
        self.assertEqual(parse('/work\n 123* 1000 2000 - 1 0 0 -'), (123 * 1024, 1000 * 1024))
        with self.assertRaises(ValueError):
            parse('/work 123 0 0 - 1 0 0 -')


class RoundTests(unittest.TestCase):
    """Run the scripts with a toy kit and a scheduler that has no network."""

    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.directory = Path(self.temporary.name)
        self.kit = self.directory / 'kit'
        self.kit.mkdir()
        # A tiny reporting fixture keeps these checks independent of an estate checkout.
        source = (ROOT / 'hpc/bundle.py').read_text()
        tree = ast.parse(source)
        assignment = next(node for node in tree.body if isinstance(node, ast.Assign) and node.targets[0].id == 'KIT_FILES')
        for name in ast.literal_eval(assignment.value):
            (self.kit / name).write_text('#!/bin/bash\n# test fixture\nKIT_VERSION=0\n')
        (self.kit / 'hpc-report.sh').write_text('''#!/bin/bash
hpc_job_start() {
    mkdir -p "$HOME/.hpc/jobs"
    printf '{"v":1,"job":"%s","project": "model-audit"}\n' "$HPC_JOB_ID" > "$HOME/.hpc/jobs/$HPC_JOB_ID.json"
}
hpc_job_finish() { :; }
hpc_job_fail() { :; }
''')

    def run_command(self, arguments, **kwargs):
        """Capture failures as data so the expected refusal can be checked."""
        return subprocess.run(arguments, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, **kwargs)

    def build(self, *extra):
        return self.run_command([sys.executable, str(ROOT / 'hpc/bundle.py'), 'build', '--needs', NEEDS,
                                 '--kit', str(self.kit), '--out', str(self.directory / 'bundle')] + list(extra))

    def rehearse(self, failed=False):
        args = [str(ROOT / 'hpc/rehearse.sh'), str(self.directory / 'rehearsal'), '--kit', str(self.kit), '--dry-run']
        if failed:
            args.append('--fail-second')
        result = self.run_command(args)
        self.assertEqual(result.returncode, 0, result.stdout)
        return result, self.directory / 'rehearsal'

    def test_bundle_and_step_list(self):
        result = self.build()
        self.assertEqual(result.returncode, 0, result.stdout)
        environment = dict(os.environ, HOME=str(self.directory / 'home'), WORKDIR=str(self.directory))
        bundle = self.directory / 'bundle/model-audit-round.sh'
        result = self.run_command([str(bundle), '1', '--list'], env=environment)
        self.assertEqual(result.returncode, 0, result.stdout)
        for step in ('10-install-kit.sh', '20-verify.sh', '30-install-reporting.sh', '40-submit.sh', '90-cleanup.sh'):
            self.assertIn(step, result.stdout)
        self.assertIn('optional', result.stdout)
        manifest = json.loads((self.directory / 'home/model-audit/rounds/1/MANIFEST.json').read_text())
        self.assertNotIn('90-cleanup.sh', manifest['steps'])
        self.assertEqual(manifest['needs']['hours'], '0')
        paths = [row['path'] for row in manifest['files']]
        self.assertFalse(any('token' in Path(name).name and name.endswith('-token') for name in paths))

    def test_wrong_missing_round_and_corrupt_payload(self):
        self.assertEqual(self.build().returncode, 0)
        bundle = self.directory / 'bundle/model-audit-round.sh'
        for arguments in ([], ['2']):
            self.assertEqual(self.run_command([str(bundle)] + arguments).returncode, 2)
        data = bundle.read_bytes()
        bundle.write_bytes(data[:-50])
        env = dict(os.environ, HOME=str(self.directory / 'home'), WORKDIR=str(self.directory))
        self.assertNotEqual(self.run_command([str(bundle), '1'], env=env).returncode, 0)

    def test_missing_reporting_and_needs(self):
        rounds = self.directory / 'rounds'
        shutil.copytree(str(ROOT / 'hpc/rounds/1'), str(rounds / '1'))
        (rounds / '1/hpc-poll.d/model-audit.sh').unlink()
        result = self.build('--rounds', str(rounds))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('reporting script', result.stdout)
        self.assertNotEqual(self.run_command([sys.executable, str(ROOT / 'hpc/bundle.py'), 'build']).returncode, 0)

    def test_card_wait_and_by_hand_forms(self):
        self.assertEqual(self.build('--takes', '12s').returncode, 0)
        cards = (self.directory / 'bundle/round-cards.sh').read_text()
        self.assertLess(cards.index('hpc-send wait "$copy"'), cards.index('run=$(hpc-send run'))
        self.assertIn('--after "$copy"', cards)
        self.assertIn('--round 1', cards)
        self.assertIn('--takes 12s', cards)
        self.assertIn("--by-hand './model-audit-round.sh 1'", cards)
        self.assertIn('hours=0', cards)
        self.assertEqual(cards.count('space=160G'), 1)

    def test_happy_chain(self):
        result, directory = self.rehearse()
        self.assertIn('both jobs completed', result.stdout)
        rows = [json.loads(line) for line in (directory / 'submissions.jsonl').read_text().splitlines()]
        self.assertEqual(len(rows), 2)
        self.assertIn('--dependency=afterok:1001', rows[1]['arguments'])
        self.assertIn('--kill-on-invalid-dep=yes', rows[1]['arguments'])
        self.assertEqual(len(list((directory / 'outbox').iterdir())), 7)
        self.assertTrue((directory / 'work/model-audit/state/compare.done').exists())
        self.assertFalse((directory / 'work/model-audit/ARCHIVED').exists())

    def test_failed_second_submission(self):
        result, directory = self.rehearse(True)
        self.assertIn('VERDICT round 1 FAIL', result.stdout)
        self.assertIn('VERDICT rehearsal OK', result.stdout)
        self.assertFalse((directory / 'work/model-audit/state/project.done').exists())
        drops = [path.read_text() for path in (directory / 'outbox').iterdir()]
        self.assertTrue(any('event: failed' in drop for drop in drops))
        self.assertEqual(len(drops), 6)

    def test_invalid_dependency_is_cancelled(self):
        root = self.directory / 'scheduler'
        root.mkdir()
        env = dict(os.environ, AUDIT_FAKE_ROOT=str(root))
        job = root / 'job.sh'
        job.write_text('#!/bin/bash\nexit 1\n')
        fake = str(ROOT / 'hpc/fakes/sbatch')
        self.assertEqual(self.run_command([fake, '--parsable', str(job)], env=env).returncode, 0)
        self.assertEqual(self.run_command([fake, '--parsable', '--dependency=afterok:1001', '--kill-on-invalid-dep=yes', str(job)], env=env).returncode, 0)
        rows = [json.loads(line) for line in (root / 'submissions.jsonl').read_text().splitlines()]
        self.assertEqual(rows[1]['status'], 'cancelled-invalid-dependency')

    def test_rerun_cannot_duplicate_submissions(self):
        result, directory = self.rehearse()
        env = dict(os.environ, HOME=str(directory / 'home'), WORKDIR=str(directory / 'work'), AUDIT_REHEARSAL='1',
                   AUDIT_FAKE_ROOT=str(directory), PATH=str(directory / 'bin') + ':' + os.environ['PATH'], HPC_SYSTEM='fake')
        result = self.run_command(['./round.sh', '--only', '40-submit.sh'], cwd=directory / 'home/model-audit/rounds/1', env=env)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('already submitted', result.stdout)
        self.assertEqual(len((directory / 'submissions.jsonl').read_text().splitlines()), 2)

    def test_record_accepts_only_the_matching_success_log(self):
        _, directory = self.rehearse()
        log = directory / 'outbox/round-1-end.log'
        out = directory / 'records'
        result = self.run_command([sys.executable, str(ROOT / 'hpc/bundle.py'), 'record', 'fake', str(log), '--out', str(out)])
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertFalse(json.loads((out / 'fake-round-1.json').read_text())['research_complete'])
        result = self.run_command([sys.executable, str(ROOT / 'hpc/bundle.py'), 'record', 'other', str(log), '--out', str(out)])
        self.assertNotEqual(result.returncode, 0)


class LoginSyntaxTests(unittest.TestCase):
    """Use the old grammar and a source list for later standard-library traps."""

    def test_python36_grammar_and_banned_constructs(self):
        banned = (r':=', r'\bdataclasses\b', r'\bmatch\s+\w+\s*:', r'\bmissing_ok\s*=',
                  r'\bis_relative_to\s*\(', r'\bfile_digest\s*\(', r'\bcapture_output\s*=',
                  r'\btext\s*=\s*(?:True|False)', r'\bsubprocess\.run\b', r'\bfrom __future__ import annotations\b')
        paths = list((ROOT / 'hpc').rglob('*.py')) + [ROOT / 'hpc/fakes/sbatch', ROOT / 'hpc/fakes/hpc']
        for path in paths:
            with self.subTest(path=path):
                source = path.read_text()
                ast.parse(source, filename=str(path), feature_version=(3, 6))
                for pattern in banned:
                    self.assertIsNone(re.search(pattern, source), '{}: {}'.format(path, pattern))

    def test_shell_syntax(self):
        for path in list((ROOT / 'hpc').rglob('*.sh')) + [ROOT / 'tools/bundle-permafrost.sh']:
            self.assertEqual(subprocess.call(['bash', '-n', str(path)]), 0, str(path))


class CleanupTests(unittest.TestCase):
    """A delete needs the exact paths and copies that passed read-back."""

    def test_missing_approval_and_mismatched_archive(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / 'derived'
            target = root / 'base/single-projection'
            target.mkdir(parents=True)
            ruling, receipt = Path(directory) / 'ruling.md', Path(directory) / 'receipt.json'
            ruling.write_text('no approved paths\n')
            receipt.write_text('{}')
            cleanup = load_module('cleanup').cleanup
            with self.assertRaises(ValueError):
                cleanup(ruling, receipt, root)
            ruling.write_text('# Cleanup\n\n## approved paths\n- ' + str(target) + '\n')
            with self.assertRaises(ValueError):
                cleanup(ruling, receipt, root)
            self.assertTrue(target.exists())

    def test_read_back_precedes_the_exact_delete(self):
        with tempfile.TemporaryDirectory() as directory:
            work = Path(directory) / 'work'
            root, measurements = work / 'derived', work / 'measurements/base'
            target, archive = root / 'base/single-projection', Path(directory) / 'archive'
            for path in (target, measurements, archive):
                path.mkdir(parents=True)
            keep = root / 'other'
            keep.mkdir()
            rows = []
            for name in ('single-projection.json', 'single-projection.directions.safetensors'):
                source, saved = measurements / name, archive / name
                source.write_bytes(b'checked measurement')
                saved.write_bytes(source.read_bytes())
                rows.append({'source': str(source), 'archive': str(saved), 'sha256': hashlib.sha256(source.read_bytes()).hexdigest()})
            ruling, receipt = Path(directory) / 'ruling.md', Path(directory) / 'receipt.json'
            ruling.write_text('# Cleanup\n\n## approved paths\n- ' + str(target) + '\n')
            receipt.write_text(json.dumps({'project': 'model-audit', 'round': 1, 'read_back': True,
                'approved_paths': [str(target)], 'measurements': rows, 'archived_at': '2026-10-13T00:00:00Z'}))
            cleanup = load_module('cleanup').cleanup
            with patch.dict(os.environ, {'ARCHIVE_HOME': str(archive)}):
                (archive / 'single-projection.json').write_bytes(b'bad archive')
                with self.assertRaises(ValueError):
                    cleanup(ruling, receipt, root)
                self.assertTrue(target.exists())
                (archive / 'single-projection.json').write_bytes(b'checked measurement')
                cleanup(ruling, receipt, root)
            self.assertFalse(target.exists())
            self.assertTrue(keep.exists())
            self.assertTrue(measurements.exists())


class DownloadTests(unittest.TestCase):
    """A checksum fault cannot publish a finished download."""

    def test_lfs_and_small_git_objects(self):
        hub = types.ModuleType('huggingface_hub')
        hub.HfApi = object
        hub.snapshot_download = object
        with patch.dict(sys.modules, {'huggingface_hub': hub}):
            module = load_module('download')
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'config.json'
            path.write_bytes(b'abc')
            row = {'path': path.name, 'size': 3, 'lfs_sha256': hashlib.sha256(b'abc').hexdigest()}
            self.assertEqual(module.check_file(path, row), row['lfs_sha256'])
            row['lfs_sha256'] = 'wrong'
            with self.assertRaises(ValueError):
                module.check_file(path, row)
            row = {'path': path.name, 'size': 3, 'git_blob_id': hashlib.sha1(b'blob 3\0abc').hexdigest()}
            self.assertEqual(module.check_file(path, row), hashlib.sha256(b'abc').hexdigest())
            row['size'] = 4
            with self.assertRaises(ValueError):
                module.check_file(path, row)


@unittest.skipUnless(importlib.util.find_spec('torch'), 'tensor runtime is not installed')
class ProjectionTests(unittest.TestCase):
    """Small matrices check the projection formula and unchanged vision weights."""

    def test_text_only_projection_preserves_other_weights_and_resumes(self):
        import torch
        from safetensors.torch import save_file
        from audit.weights import TensorStore
        torch.set_num_threads(1)
        project = load_module('project')
        with tempfile.TemporaryDirectory() as directory:
            original, derived = Path(directory) / 'original', Path(directory) / 'derived'
            original.mkdir()
            names = ('model.language_model.layers.0.self_attn.o_proj.weight',
                     'model.language_model.layers.0.mlp.down_proj.weight',
                     'model.vision_tower.layers.0.self_attn.o_proj.weight',
                     'model.language_model.layers.0.self_attn.q_proj.weight')
            weights = {name: torch.eye(4).to(torch.bfloat16) for name in names}
            save_file(weights, str(original / 'model.safetensors'))
            (original / 'config.json').write_text('{"torch_dtype":"bfloat16"}')
            direction = torch.tensor([1., 0., 0., 0.])
            touched = project.projection(TensorStore(original), direction, derived, 'fixture')
            self.assertEqual(set(touched), set(names[:2]))
            store = TensorStore(derived)
            expected = weights[names[0]].clone()
            expected[0] = 0
            for name in names:
                self.assertTrue(torch.equal(store.get(name), expected if name in names[:2] else weights[name]))
                self.assertEqual(store.get(name).dtype, torch.bfloat16)
            self.assertEqual(project.projection(TensorStore(original), direction, derived, 'fixture'), touched)
            with self.assertRaises(ValueError):
                project.projection(TensorStore(original), direction, derived, 'different')


if __name__ == '__main__':
    unittest.main()
