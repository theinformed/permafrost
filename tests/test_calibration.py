# test_calibration.py -- Check recipe math, packaging and a fenced local job.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  check disk tensor names, shared pins and wheelhouse gaps.
# Modified: SDE 2026-10-14  exercise dtype preservation and failed comparison reads.
import ast
import hashlib
import importlib.util
import io
from contextlib import redirect_stdout
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import time
import unittest
from unittest.mock import patch

import torch
from safetensors import safe_open
from safetensors.torch import save_file
from audit.nulls import project_tensor
from audit.weights import TensorStore, compare_weights

ROOT = Path(__file__).resolve().parents[1]
NEEDS = 'space=80G hours=0 subproject=NRLMR57635502 queue=background for=4h'
torch.set_num_threads(1)


def load(name, path=None):
    """Load standalone helpers without installing the round as a package."""
    spec = importlib.util.spec_from_file_location(name, path or ROOT / 'hpc' / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


calibrate = load('calibrate')
measure = load('calibration_measure', ROOT / 'hpc/rounds/4/measure.py')
wheels = load('calibration_wheels', ROOT / 'hpc/rounds/4/wheels.py')
FIXTURES = ROOT / 'tests/fixtures/calibration'


def scratch(case):
    """Keep disposable test files in the authorized workspace."""
    folder = ROOT / '.tmp'
    folder.mkdir(exist_ok=True)
    temporary = tempfile.TemporaryDirectory(prefix='calibration-', dir=str(folder))
    case.addCleanup(temporary.cleanup)
    return Path(temporary.name)


def toy_kit(directory):
    """Write just enough reporting code for the scheduler's local cards."""
    directory.mkdir()
    tree = ast.parse((ROOT / 'hpc/bundle.py').read_text())
    assignment = next(node for node in tree.body if isinstance(node, ast.Assign)
                      and isinstance(node.targets[0], ast.Name) and node.targets[0].id == 'KIT_FILES')
    for name in ast.literal_eval(assignment.value):
        (directory / name).write_text('#!/bin/bash\n# ' + name + ' -- Local reporting fixture.\n'
            '# Created by Sean Egan 2026-10-14\n# Modified: SDE 2026-10-14  keep the fixture small.\nKIT_VERSION=0\n')
    (directory / 'hpc-report.sh').write_text('''#!/bin/bash
# hpc-report.sh -- Write a local job card for the rehearsal.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  omit network delivery.
hpc_job_start() {
    mkdir -p "$HOME/.hpc/jobs"
    printf '{"v":1,"job":"%s","project":"model-audit"}\n' "$HPC_JOB_ID" > "$HOME/.hpc/jobs/$HPC_JOB_ID.json"
}
hpc_job_finish() { :; }
hpc_job_fail() { :; }
''')
    return directory


def checkpoint(directory):
    """Use random bf16 tensors with a substantial direction component."""
    directory.mkdir()
    generator = torch.Generator().manual_seed(12)
    tensors = {}
    for name in ('language_model.model.layers.0.self_attn.o_proj.weight',
                 'language_model.model.layers.0.mlp.down_proj.weight',
                 'language_model.model.layers.0.self_attn.q_proj.weight',
                 'vision_tower.transformer.layers.0.attention.o_proj.weight',
                 'multi_modal_projector.linear_1.weight',
                 'language_model.model.embed_tokens.weight'):
        value = torch.randn(8, 8, generator=generator)
        value[:2] *= 4
        tensors[name] = value.bfloat16()
    tensors['language_model.model.norm.weight'] = torch.randn(8, generator=generator)
    save_file(tensors, str(directory / 'weights.safetensors'))
    (directory / 'config.json').write_text('{"torch_dtype":"bfloat16"}\n')
    (directory / 'tokenizer.model').write_bytes(b'tokenizer fixture')
    files = list(directory.iterdir())
    (directory / 'download-manifest.json').write_text(json.dumps({'base': 'test/base', 'revision': 'test',
        'files': [{'path': path.name, 'size': path.stat().st_size,
                   'sha256': hashlib.sha256(path.read_bytes()).hexdigest()} for path in files]}))
    direction = torch.zeros(8)
    direction[:2] = 2 ** -0.5
    return tensors, direction


class RealIndexTests(unittest.TestCase):
    """Check the seed and selection against the published disk index."""

    def test_real_name_selection(self):
        """Select exactly two text residual writers from each of forty layers."""
        names = json.loads((FIXTURES / 'mistral-small-3.2-24b-index.json').read_text())['weight_map']
        expected = {'language_model.model.layers.{}.{}.weight'.format(layer, suffix)
                    for layer in range(40) for suffix in ('self_attn.o_proj', 'mlp.down_proj')}
        selected = {name for name in names if calibrate.selects(name)}
        self.assertEqual(len(expected), 80)
        self.assertEqual(selected, expected)
        self.assertFalse(any('vision_tower' in name or 'multi_modal_projector' in name for name in selected))

    def test_seed_names_shapes_and_config(self):
        """Use real names with consistent tiny shapes and a repeatable two-shard receipt."""
        directory = scratch(self)
        original = directory / 'original'
        with patch.dict(os.environ, AUDIT_ORIGINAL=str(original), AUDIT_BASE='test/base'):
            measure.seed_original()
            measure.verify_original()
            first = (original / 'download-manifest.json').read_bytes()
            measure.seed_original()
            self.assertEqual(first, (original / 'download-manifest.json').read_bytes())
        real = json.loads((FIXTURES / 'mistral-small-3.2-24b-index.json').read_text())['weight_map']
        store = TensorStore(original)
        self.assertEqual(len(store.names), 36)
        self.assertTrue(set(store.names).issubset(real), sorted(set(store.names) - set(real)))
        self.assertEqual(len(list(original.glob('*.safetensors'))), 2)
        shapes = {}
        for layer in range(2):
            prefix = 'language_model.model.layers.{}.'.format(layer)
            for suffix, shape in (
                ('input_layernorm', (64,)), ('post_attention_layernorm', (64,)),
                ('self_attn.q_proj', (64, 64)), ('self_attn.k_proj', (32, 64)),
                ('self_attn.v_proj', (32, 64)), ('self_attn.o_proj', (64, 64)),
                ('mlp.gate_proj', (128, 64)), ('mlp.up_proj', (128, 64)), ('mlp.down_proj', (64, 128))):
                shapes[prefix + suffix + '.weight'] = shape
        prefix = 'vision_tower.transformer.layers.0.'
        for suffix, shape in (
            ('attention.q_proj', (32, 32)), ('attention.k_proj', (32, 32)),
            ('attention.v_proj', (32, 32)), ('attention.o_proj', (32, 32)),
            ('attention_norm', (32,)), ('ffn_norm', (32,)), ('feed_forward.gate_proj', (64, 32)),
            ('feed_forward.up_proj', (64, 32)), ('feed_forward.down_proj', (32, 64))):
            shapes[prefix + suffix + '.weight'] = shape
        shapes.update({'language_model.model.embed_tokens.weight': (256, 64),
                       'language_model.model.norm.weight': (64,), 'language_model.lm_head.weight': (256, 64),
                       'vision_tower.ln_pre.weight': (32,), 'vision_tower.patch_conv.weight': (32, 3, 4, 4),
                       'multi_modal_projector.norm.weight': (32,),
                       'multi_modal_projector.patch_merger.merging_layer.weight': (32, 128),
                       'multi_modal_projector.linear_1.weight': (64, 32),
                       'multi_modal_projector.linear_2.weight': (64, 64)})
        self.assertEqual(set(store.names), set(shapes))
        for name, shape in shapes.items():
            tensor = store.get(name)
            self.assertEqual(tuple(tensor.shape), shape, name)
            self.assertEqual(tensor.dtype, torch.bfloat16, name)
        config = json.loads((original / 'config.json').read_text())
        real_config = json.loads((FIXTURES / 'mistral-small-3.2-24b-config.json').read_text())
        self.assertEqual(set(config), set(real_config))
        self.assertEqual(config['model_type'], real_config['model_type'])
        self.assertEqual(config['architectures'], real_config['architectures'])
        for section in ('text_config', 'vision_config'):
            self.assertEqual(set(config[section]), set(real_config[section]))
            settings = config[section]
            self.assertEqual(settings['num_attention_heads'] * settings['head_dim'], settings['hidden_size'])
        self.assertEqual(config['text_config']['num_key_value_heads'], 1)
        self.assertEqual(config['text_config']['vocab_size'], 256)


class WheelhouseTests(unittest.TestCase):
    """Check the login refusal and keep the two rounds' runtime pins together."""

    def setUp(self):
        """Prepare a pinned requirement file and a disposable wheelhouse."""
        self.directory = scratch(self)
        self.requirements = self.directory / 'compute-requirements.txt'
        self.requirements.write_text('# fixture\n\nfirst==1.2\nsecond==3.4\n')
        self.wheelhouse = self.directory / 'wheels'
        self.wheelhouse.mkdir()
        for name in ('first-1.2-py3-none-any.whl', 'second-3.4-py3-none-any.whl'):
            (self.wheelhouse / name).write_bytes(b'')

    def run_check(self):
        """Use the login entry point so both printed gaps and exit status are checked."""
        return subprocess.run([sys.executable, str(ROOT / 'hpc/rounds/4/wheels.py')],
                              cwd=self.directory, env=dict(os.environ, AUDIT_WHEELS=str(self.wheelhouse)),
                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    def test_all_present(self):
        """Accept every pinned wheel, ignoring comments and blank lines."""
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertEqual(result.stdout.strip(), 'wheelhouse: 2 pins found in ' + str(self.wheelhouse))

    def test_missing_pin(self):
        """Report the exact missing pin and return a nonzero login exit."""
        (self.wheelhouse / 'second-3.4-py3-none-any.whl').unlink()
        result = self.run_check()
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout.strip(), 'wheel missing: second==3.4')

    def test_wrong_version(self):
        """A different installed version does not satisfy the runtime pin."""
        path = self.wheelhouse / 'second-3.4-py3-none-any.whl'
        path.rename(self.wheelhouse / 'second-3.5-py3-none-any.whl')
        self.assertEqual(self.run_check().stdout.strip(), 'wheel missing: second==3.4')

    def test_name_normalization(self):
        """Compare case, underscores and hyphens in distribution names."""
        self.requirements.write_text('Jinja2==3.1.6\ntyping-extensions==4.15.0\nmistral-common==1.8.5\n')
        for name in ('jinja2-3.1.6', 'typing_extensions-4.15.0', 'mistral_common-1.8.5'):
            (self.wheelhouse / (name + '-py3-none-any.whl')).write_bytes(b'')
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertEqual(wheels.canonical('typing_extensions'), wheels.canonical('typing-extensions'))
        self.assertEqual(wheels.canonical('mistral_common'), wheels.canonical('mistral-common'))
        self.assertEqual(wheels.canonical('one..__--two'), 'one-two')

    def test_pins_follow_round_one(self):
        """Keep runtime pins equal because round four uses round one's wheels."""
        self.assertEqual(set(wheels.pins(ROOT / 'hpc/rounds/4/compute-requirements.txt')),
                         set(wheels.pins(ROOT / 'hpc/rounds/1/compute-requirements.txt')))


class TransformTests(unittest.TestCase):
    """Check the published formulas without loading a runtime or using a GPU."""

    def setUp(self):
        """Prepare one small checkpoint for both recipes."""
        self.directory = scratch(self)
        self.original = self.directory / 'original'
        self.tensors, self.direction = checkpoint(self.original)
        self.store = TensorStore(self.original)

    def test_single_projection_math_and_other_bits(self):
        """Touch only text residual writers and preserve each tensor's dtype."""
        derived = self.directory / 'derived'
        touched = calibrate.write_derived(self.store, self.direction, derived, 'fingerprint', 'single-projection')
        expected = [name for name in self.tensors if 'language_model.model.layers' in name
                    and ('o_proj' in name or 'down_proj' in name)]
        self.assertEqual(sorted(touched), sorted(expected))
        other = TensorStore(derived)
        for name, source in self.tensors.items():
            target = other.get(name)
            self.assertEqual(source.dtype, target.dtype)
            if name in touched:
                self.assertTrue(torch.equal(target, project_tensor(source, self.direction).to(source.dtype)))
            else:
                self.assertTrue(torch.equal(target, source), name)
            with safe_open(str(other.names[name]), framework='pt') as shard:
                self.assertEqual(shard.metadata(), {'fingerprint': 'fingerprint', 'tensor': name})
        self.assertEqual(len(list(derived.glob('*.safetensors'))), len(self.tensors))
        self.assertFalse(list(derived.glob('*.part')))
        self.assertFalse((derived / 'download-manifest.json').exists())
        self.assertEqual((derived / 'tokenizer.model').read_bytes(), b'tokenizer fixture')
        self.assertEqual((derived / 'config.json').read_bytes(), (self.original / 'config.json').read_bytes())
        index = json.loads((derived / 'model.safetensors.index.json').read_text())
        self.assertEqual(index['metadata']['total_size'], sum(t.numel() * t.element_size() for t in self.tensors.values()))

    def test_restored_row_norms_and_control(self):
        """Check the bf16 tolerance and the control's substantial norm loss."""
        name = 'language_model.model.layers.0.self_attn.o_proj.weight'
        source = self.tensors[name]
        restored, touched = calibrate.transform(name, source, self.direction, 'norm-preserving')
        projected, _ = calibrate.transform(name, source, self.direction, 'single-projection')
        norms = source.float().norm(dim=1)
        self.assertTrue(touched)
        self.assertEqual(restored.dtype, torch.bfloat16)
        self.assertTrue(torch.allclose(restored.float().norm(dim=1), norms, rtol=1e-2))
        self.assertGreater(float(((projected.float().norm(dim=1) - norms).abs() / norms).max()), 0.1)

    def test_collapsed_row_is_refused(self):
        """A zeroed nonzero row has no norm to rescale."""
        direction = torch.tensor([1.0, 0.0])
        with self.assertRaisesRegex(ValueError, 'collapsed'):
            calibrate.transform('model.layers.0.self_attn.o_proj.weight', torch.eye(2), direction, 'norm-preserving')

    def test_unknown_recipe_is_refused(self):
        """Reject unsupported recipes even on an untouched tensor."""
        for recipe in ('unknown', '', None):
            with self.subTest(recipe=recipe), self.assertRaisesRegex(ValueError, 'unsupported recipe'):
                calibrate.transform('embedding', torch.ones(2), self.direction, recipe)

    def test_identity_binds_recipe_version(self):
        """Use different fingerprints for the two published formulas."""
        first = calibrate.identity(self.original, {'harmful': [], 'harmless': []}, 'norm-preserving')
        second = calibrate.identity(self.original, {'harmful': [], 'harmless': []}, 'single-projection')
        self.assertEqual(first['recipe_version'], 'projection-then-row-rescale-v1')
        self.assertEqual(second['recipe_version'], '1')
        self.assertNotEqual(first['fingerprint'], second['fingerprint'])

    def test_real_report_card(self):
        """Summarize measured tensor kinds, hashes and changes from both recipes."""
        for recipe in calibrate.RECIPES:
            with self.subTest(recipe=recipe):
                derived = self.directory / recipe
                touched = calibrate.write_derived(self.store, self.direction, derived, 'fp', recipe)
                path = self.directory / (recipe + '.json')
                report = compare_weights(str(derived), str(self.original), path)
                record = calibrate.identity(self.original, {}, recipe)
                record['tensors_touched'] = touched
                card = calibrate.fingerprint_card(path, record, {'measured_at': 'test-date'})
                self.assertEqual(card['schema_version'], 1)
                self.assertEqual(card['base_revision'], 'test')
                self.assertEqual(card['measured_at'], 'test-date')
                self.assertEqual(card['changed_outside_recipe'], [])
                self.assertEqual(card['report_sha256'], hashlib.sha256(path.read_bytes()).hexdigest())
                self.assertEqual(card['directions_sha256'], hashlib.sha256(path.with_suffix('.directions.safetensors').read_bytes()).hexdigest())
                self.assertEqual(card['summary']['changed_tensors'], 2)
                self.assertEqual(card['summary']['matched_tensors'], len(self.tensors))
                self.assertEqual(card['summary']['violation_count'], len(report['recipe_matching']['violations']))
                attention = card['per_kind']['attention_output']
                self.assertEqual((attention['count'], attention['changed']), (1, 1))
                self.assertEqual(card['per_kind']['feed_forward_down']['count'], 1)
                self.assertIsNotNone(attention['first_singular_energy_share']['min'])
                self.assertIsNotNone(attention['row_norm_max_relative_error'])
                record['tensors_touched'] = []
                self.assertEqual(len(calibrate.fingerprint_card(path, record, {})['changed_outside_recipe']), 2)

    def main_environment(self, recipe):
        """Name every calibration output in this test's disposable folder."""
        return dict(AUDIT_ORIGINAL=str(self.original), AUDIT_DERIVED=str(self.directory / 'derived'),
                    AUDIT_WORK=str(self.directory), AUDIT_MEASUREMENT=str(self.directory / 'report.json'),
                    AUDIT_CARD=str(self.directory / 'card.json'), AUDIT_RECIPE=recipe,
                    AUDIT_NAME='test', AUDIT_STUB='1', AUDIT_REHEARSAL='1')

    def test_main_failed_comparison_has_no_card_or_compare_marker(self):
        """A comparison fault leaves only the stages that completed successfully."""
        with patch.dict(os.environ, self.main_environment('norm-preserving')):
            with self.assertRaises(SystemExit) as caught:
                calibrate.main(lambda args: 23)
        self.assertEqual(caught.exception.code, 23)
        state = self.directory / 'state'
        self.assertTrue((state / 'calibrate-activations.done').is_file())
        self.assertTrue((state / 'calibrate-transform.done').is_file())
        self.assertFalse((state / 'calibrate-compare.done').exists())
        self.assertFalse((state / 'calibrate.done').exists())
        self.assertFalse((self.directory / 'card.json').exists())

    def test_main_keeps_assessment_as_data(self):
        """Complete the cards and markers even when the audit reports violations."""
        from audit.weights_cli import main as compare
        output = io.StringIO()
        with patch.dict(os.environ, self.main_environment('norm-preserving')), redirect_stdout(output):
            self.assertIsNone(calibrate.main(compare))
        card = json.loads((self.directory / 'card.json').read_text())
        self.assertEqual(card['summary']['assessment'], 'recipe_violations')
        self.assertTrue((self.directory / 'state/calibrate.done').is_file())
        self.assertTrue((self.directory / 'norm-preserving.recipe-card.json').is_file())
        self.assertTrue((self.directory / 'norm-preserving.direction.safetensors').is_file())
        self.assertIn('fingerprint: norm-preserving on test/base:', output.getvalue())


class RoundArgumentTests(unittest.TestCase):
    """Run argument parsing with disposable steps and a fake reporting command."""

    steps = ('10-install-kit.sh', '20-verify.sh', '40-submit.sh')

    def setUp(self):
        """Create local steps that record their names."""
        self.directory = scratch(self)
        shutil.copy2(ROOT / 'hpc/rounds/4/round.sh', self.directory / 'round.sh')
        for name in self.steps:
            path = self.directory / name
            path.write_text('#!/bin/bash\necho "${0##*/}" >> "$ROUND_RECORD"\n')
            path.chmod(0o755)
        binary = self.directory / 'bin'
        binary.mkdir()
        reporter = binary / 'hpc'
        reporter.write_text('#!/bin/bash\necho "is on the desk"\n')
        reporter.chmod(0o755)
        self.record = self.directory / 'steps.txt'
        self.environment = dict(os.environ, HOME=str(self.directory / 'home'),
                                PATH=str(binary) + ':' + os.environ['PATH'],
                                ROUND_RECORD=str(self.record), HPC_SYSTEM='fake')

    def run_round(self, *args):
        """Capture argument refusals as well as successful step output."""
        return subprocess.run(['./round.sh'] + list(args), cwd=self.directory, env=self.environment,
                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    def test_default(self):
        """Run exactly the three calibration steps."""
        result = self.run_round()
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertEqual(self.record.read_text().splitlines(), list(self.steps))

    def test_only(self):
        """Run a single named step."""
        result = self.run_round('--only', './20-verify.sh')
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertEqual(self.record.read_text().splitlines(), ['20-verify.sh'])

    def test_from(self):
        """Resume at a named step without adding reporting or cleanup."""
        result = self.run_round('--from', '20-verify.sh')
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertEqual(self.record.read_text().splitlines(), list(self.steps[1:]))

    def test_list_and_bad_args(self):
        """List only allowed steps and reject extra or unknown arguments."""
        result = self.run_round('--list')
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.splitlines(), list(self.steps))
        for args in (('projection',), ('--only',), ('--from', 'unknown'), ('--list', 'extra'),
                     ('--only', '90-cleanup.sh'), ('--only', '40-submit.sh', 'extra')):
            with self.subTest(args=args):
                self.assertEqual(self.run_round(*args).returncode, 2)
        self.assertFalse(self.record.exists())


class BundleTests(unittest.TestCase):
    """Check the payload and desk lines without running any desk command."""

    def setUp(self):
        """Use a tiny local reporting kit."""
        self.directory = scratch(self)
        self.kit = toy_kit(self.directory / 'kit')

    def build(self, *extra):
        """Capture bundle output and refusals."""
        return subprocess.run([sys.executable, str(ROOT / 'hpc/calibrate_bundle.py'), 'build',
            '--needs', NEEDS, '--kit', str(self.kit), '--out', str(self.directory / 'bundle')] + list(extra),
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    def test_needs_and_recipe_refusals(self):
        """Reject incomplete needs, wrong duration, wrong system and unknown recipes."""
        for args in (('--needs', NEEDS.replace('space=80G ', '')), ('--needs', NEEDS.replace('for=4h', 'for=3h')),
                     ('--needs', NEEDS.replace('80G', '59G')), ('--needs', NEEDS.replace('80G', '201G')),
                     ('--recipe', 'unknown'), ('--system', 'fake'),
                     ('--needs', NEEDS.replace('NRLMR57635502', 'wrong'))):
            with self.subTest(args=args):
                self.assertNotEqual(self.build(*args).returncode, 0)

    def test_payload_stamp_and_cards(self):
        """Keep the short run command, recipe selection and payload hash together."""
        result = self.build('--recipe', 'single-projection')
        self.assertEqual(result.returncode, 0, result.stdout)
        bundle = self.directory / 'bundle/model-audit-calibrate.sh'
        self.assertTrue(bundle.is_file())
        head, tail = bundle.read_bytes().split(b'__PAYLOAD__\n', 1)
        stamp = hashlib.sha256(tail).hexdigest()
        self.assertIn(stamp.encode(), head)
        self.assertRegex(stamp, r'^[a-f0-9]{64}$')
        with tarfile.open(fileobj=io.BytesIO(tail)) as archive:
            self.assertEqual(archive.extractfile('RECIPE.txt').read(), b'single-projection\n')
            manifest = json.load(archive.extractfile('MANIFEST.json'))
            self.assertEqual(manifest['round'], 4)
            self.assertEqual(manifest['piece'], 'recipe-calibration')
            self.assertEqual(manifest['steps'], list(RoundArgumentTests.steps))
            self.assertNotIn('cache.write_text', archive.extractfile('storage.py').read().decode())
        run = next(line[5:] for line in result.stdout.splitlines() if line.startswith('Run: '))
        self.assertEqual(run, '/p/work1/sdegan/model-audit-calibrate.sh 4')
        self.assertLess(len(run), 50)
        self.assertFalse(any(char in run for char in '=|;&'))
        self.assertNotIn('model-audit-round.sh', result.stdout)
        cards = (self.directory / 'bundle/calibration-cards.sh').read_text()
        self.assertIn('hpc-send wait "$copy"', cards)
        self.assertIn('--after "$copy"', cards)
        self.assertEqual(subprocess.call(['bash', '-n', str(self.directory / 'bundle/calibration-cards.sh')]), 0)
        sources = self.directory / 'sources'
        shutil.copytree(ROOT / 'hpc/rounds/4', sources / '4')
        path = sources / '4/login.py'
        path.write_text(path.read_text() + "\nprint('changed source')\n")
        second = self.build('--rounds', str(sources))
        self.assertEqual(second.returncode, 0, second.stdout)
        second_tail = bundle.read_bytes().split(b'__PAYLOAD__\n', 1)[1]
        self.assertNotEqual(hashlib.sha256(second_tail).hexdigest(), stamp)

    def test_clean_rehearsal_with_memory_ceiling(self):
        """Run one small end-to-end job through the existing memory wrapper."""
        result = subprocess.run(['nice', '-n', '19', sys.executable, str(ROOT / 'hpc/rehearse_calibration.py'),
            str(self.directory / 'rehearsal'), '--dry-run', '--kit', str(self.kit)],
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn('Memory ceiling:', result.stdout)
        self.assertIn('VERDICT round 4 OK', result.stdout)
        self.assertIn('fingerprint:', result.stdout)
        self.assertIn('vision and projector tensors: bit-identical', result.stdout)
        self.assertIn('attention_output: changed 2', result.stdout)
        self.assertIn('feed_forward_down: changed 2', result.stdout)
        self.assertFalse((self.directory / 'rehearsal/home/.hpc/model-audit-space.tsv').exists())

    def test_missing_wheel_rehearsal(self):
        """Stop the local round at login when the first pinned wheel is absent."""
        code = ('import argparse, sys\n'
                'sys.path.insert(0, {!r})\n'
                'from rehearse_calibration import CalibrationRehearsal\n'
                'args = argparse.Namespace(kit={!r}, login_python="python3", compute_python={!r}, '
                'base="rehearsal/synthetic", dry_run=True)\n'
                'run = CalibrationRehearsal(args, {!r})\n'
                'run.missing_wheel()\n'
                'print(run.log.read_text())\n').format(
                    str(ROOT / 'hpc'), str(self.kit), sys.executable, str(self.directory / 'missing-wheel'))
        result = subprocess.run(['nice', '-n', '19', str(ROOT / 'hpc/rehearse.sh'), '--memory-command',
                                 'nice', '-n', '19', sys.executable, '-c', code],
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        self.assertEqual(result.returncode, 0, result.stdout)
        pin = '=='.join(wheels.pins(ROOT / 'hpc/rounds/4/compute-requirements.txt')[0])
        self.assertIn('wheel missing: ' + pin, result.stdout)
        self.assertIn('VERDICT round 4 FAIL', result.stdout)
        self.assertIn('scheduler rows 0', result.stdout)


class MeasurementTests(unittest.TestCase):
    """Check the read-time freshness and checksum refusals without a runtime."""

    def setUp(self):
        """Prepare an old verified original and fresh declared outputs."""
        self.directory = scratch(self)
        self.original = self.directory / 'original'
        self.original.mkdir()
        self.input = self.original / 'source.bin'
        self.input.write_bytes(b'original')
        manifest = {'base': 'test/base', 'files': [{'path': self.input.name, 'size': self.input.stat().st_size,
                    'sha256': hashlib.sha256(self.input.read_bytes()).hexdigest()}]}
        (self.original / 'download-manifest.json').write_text(json.dumps(manifest))
        os.utime(self.input, (1, 1))
        self.derived = self.directory / 'derived'
        self.derived.mkdir()
        self.started = time.time() - 10
        self.environment = dict(AUDIT_BASE='test/base', AUDIT_ORIGINAL=str(self.original),
            AUDIT_DERIVED=str(self.derived), AUDIT_WORK=str(self.directory),
            AUDIT_MEASUREMENT=str(self.directory / 'report.json'), AUDIT_JOB_STARTED=str(self.started))
        self.context = patch.dict(os.environ, self.environment)
        self.context.start()
        self.addCleanup(self.context.stop)

    def test_stale_declared_input(self):
        """Name the old file rather than quietly reusing it."""
        path = self.derived / 'old.txt'
        path.write_text('old')
        os.utime(path, (1, 1))
        with self.assertRaisesRegex(ValueError, 'stale measurement input refused: ' + str(path)):
            measure.measurement([], lambda args: 0)

    def test_corrupt_original(self):
        """Reject different bytes even if the original's size stays the same."""
        self.input.write_bytes(b'changed!')
        with self.assertRaisesRegex(ValueError, 'original checksum differs'):
            measure.verify_original()

    def test_prior_try_scratch_is_not_dated(self):
        """Scratch gets cleared by the job and is outside the comparison inputs."""
        path = self.directory / 'state/calibration/context.json'
        path.parent.mkdir(parents=True)
        path.write_text('{}')
        os.utime(path, (1, 1))
        self.assertEqual(measure.round_inputs(), [])
        self.assertEqual(measure.measurement([], lambda args: 0), 0)

    def test_compare_exit_is_preserved(self):
        """Pass the comparison's nonzero exit to the calling shell."""
        with self.assertRaises(SystemExit) as caught:
            measure.measurement([], lambda args: 23)
        self.assertEqual(caught.exception.code, 23)


if __name__ == '__main__':
    unittest.main()
