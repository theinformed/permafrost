# test_container.py -- Check the round image's pins, its run check and the image builds.
# Created by Sean Egan 2026-10-14
"""The image must carry exactly the round's pins, and a bundle built without
--image must come out the same as it did before images existed."""
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
CONTAINER = ROOT / 'hpc/container'
NEEDS = 'space=160G hours=0 subproject=NRLMR57635502 queue=background for=4h'
JEAN_NEEDS = NEEDS.replace('NRLMR57635502', 'NRLMR5762B403')
IMAGE = '/p/work1/sdegan/images/permafrost-1.sif'
SHA = 'ab' * 32
BEFORE_IMAGES = 'a86ca09'


def pins(text):
    """Exact pins, comments and blanks dropped."""
    return [line.strip() for line in text.splitlines() if line.strip() and not line.startswith('#')]


def heredoc(text, word):
    match = re.search(r"<<'{0}'\n(.*?)\n{0}\n".format(word), text, re.S)
    return match.group(1)


def code(text):
    """Shell lines with the comments left out."""
    return '\n'.join(line for line in text.splitlines() if not line.lstrip().startswith('#'))


def run(arguments, **kwargs):
    return subprocess.run(arguments, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, **kwargs)


def payload(bundle, into):
    """Open a built round the way the opener does, without running it."""
    into.mkdir(parents=True)
    data = bundle.read_bytes()
    head, tail = data.split(b'\n__PAYLOAD__\n', 1)
    archive = into.parent / (into.name + '.tar')
    archive.write_bytes(tail)
    subprocess.check_call(['tar', '-xf', str(archive), '-C', str(into)])
    return head.decode()


class DefinitionTests(unittest.TestCase):
    """The image is the requirements file, nothing more and nothing floating."""

    def setUp(self):
        self.definition = (CONTAINER / 'permafrost.def').read_text()

    def test_def_pins_equal_every_round_requirements(self):
        baked = pins(heredoc(self.definition, 'PINS'))
        for number in (1, 2, 4):
            with self.subTest(round=number):
                wanted = pins((ROOT / 'hpc/rounds/{}/compute-requirements.txt'.format(number)).read_text())
                self.assertEqual(baked, wanted)
        self.assertTrue(all(re.fullmatch(r'[A-Za-z0-9._-]+==[0-9][A-Za-z0-9.]*', line) for line in baked))

    def test_held_versions_are_exact_and_do_not_repeat_pins(self):
        held = pins(heredoc(self.definition, 'HELD'))
        names = {re.sub(r'[-_.]+', '-', line.split('==')[0].lower()) for line in pins(heredoc(self.definition, 'PINS'))}
        for line in held:
            self.assertRegex(line, r'^[A-Za-z0-9._-]+==[0-9][A-Za-z0-9.]*$')
            self.assertNotIn(re.sub(r'[-_.]+', '-', line.split('==')[0].lower()), names)

    def test_base_by_digest_wheels_only_no_extra_index(self):
        self.assertRegex(self.definition, r'\nFrom: python@sha256:[0-9a-f]{64}\n')
        self.assertIn('--only-binary=:all:', self.definition)
        self.assertNotIn('index-url', self.definition)
        self.assertIn('hpc/rounds/1/compute-requirements.txt /opt/permafrost/compute-requirements.txt', self.definition)
        self.assertIn('/etc/permafrost-image.txt', self.definition)
        # The audit code rides the bundle, never the image.
        self.assertNotRegex(self.definition, r'\n\s+(audit|hpc/[a-z_]+\.py)\b')


class RunCheckTests(unittest.TestCase):
    """The pin comparison fails fast, with short lines, on any drift."""

    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.directory = Path(temporary.name)
        binary = self.directory / 'bin'
        binary.mkdir()
        (binary / 'python3').symlink_to(sys.executable)
        self.record = self.directory / 'permafrost-image.txt'
        self.record.write_text('image: permafrost\nversion: test\nbuilt: now\nrequirements sha256: none\n')
        self.environment = dict(os.environ, PATH=str(binary) + ':' + os.environ['PATH'],
                                PERMAFROST_IMAGE=str(self.record), AUDIT_EXPECT_GPUS='0')

    def check(self, requirements):
        path = self.directory / 'requirements.txt'
        path.write_text(requirements)
        return run(['bash', str(CONTAINER / 'run-check.sh'), str(path)], env=self.environment)

    def test_fake_mismatch_fails(self):
        import importlib.metadata
        have = importlib.metadata.version('pip')
        result = self.check('# pins\npip==0.0.1\n')
        self.assertEqual(result.returncode, 3, result.stdout)
        self.assertIn('FAIL pip is {}, pinned 0.0.1'.format(have), result.stdout)
        self.assertIn('FAIL 1 of 1 pins differ', result.stdout)
        self.assertNotIn('VERDICT image OK', result.stdout)
        self.assertTrue(all(len(line) <= 100 for line in result.stdout.splitlines()))

    def test_missing_and_loose_pins_fail(self):
        result = self.check('no-such-package-here==1.0\npip>=1\n')
        self.assertEqual(result.returncode, 3, result.stdout)
        self.assertIn('FAIL no-such-package-here is missing, pinned 1.0', result.stdout)
        self.assertIn('FAIL pin is not exact: pip>=1', result.stdout)

    def test_matching_pins_pass_the_pin_stage(self):
        import importlib.metadata
        result = self.check('pip=={}\n'.format(importlib.metadata.version('pip')))
        self.assertIn('pins: all 1 match', result.stdout)

    def test_outside_the_image_refuses(self):
        self.environment['PERMAFROST_IMAGE'] = str(self.directory / 'absent.txt')
        result = self.check('pip==1\n')
        self.assertEqual(result.returncode, 2)
        self.assertIn('FAIL not inside the permafrost image', result.stdout)


class BundleTests(unittest.TestCase):
    """Image and Jean builds change only what they name; the default does not change."""

    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.directory = Path(temporary.name)
        self.kit = self.directory / 'kit'
        self.kit.mkdir()
        source = (ROOT / 'hpc/bundle.py').read_text()
        names = re.search(r'KIT_FILES = \((.*?)\)\n', source, re.S).group(1)
        for name in re.findall(r"'([^']+)'", names):
            (self.kit / name).write_text('#!/bin/bash\n# test fixture\nKIT_VERSION=0\n')

    def build(self, out, *extra, needs=NEEDS, script=ROOT / 'hpc/bundle.py'):
        return run([sys.executable, str(script), 'build', '--needs', needs, '--kit', str(self.kit),
                    '--out', str(self.directory / out), '--rounds', str(ROOT / 'hpc/rounds')] + list(extra))

    def opened(self, out, *extra, needs=NEEDS):
        result = self.build(out, *extra, needs=needs)
        self.assertEqual(result.returncode, 0, result.stdout)
        head = payload(self.directory / out / 'model-audit-round.sh', self.directory / (out + '-open'))
        return result, head, self.directory / (out + '-open')

    def test_default_build_matches_the_build_before_images(self):
        old = self.directory / 'before'
        (old / 'hpc').mkdir(parents=True)
        shown = run(['git', '-C', str(ROOT), 'show', BEFORE_IMAGES + ':hpc/bundle.py']) if shutil.which('git') else None
        if shown is None or shown.returncode != 0:
            self.skipTest('no git history here to compare against')
        (old / 'hpc/bundle.py').write_text(shown.stdout)
        for name in ('needs.py', 'opener.sh', 'download.py', 'project.py', 'storage.py', 'cleanup.py'):
            (old / 'hpc' / name).symlink_to(ROOT / 'hpc' / name)
        for name in ('audit', 'data'):
            (old / name).symlink_to(ROOT / name)
        trees, outputs = [], []
        for script in (old / 'hpc/bundle.py', ROOT / 'hpc/bundle.py'):
            out = self.directory / 'same-out'
            if out.exists():
                shutil.rmtree(str(out))
            result = self.build('same-out', script=script)
            self.assertEqual(result.returncode, 0, result.stdout)
            opened = self.directory / ('open-{}'.format(len(trees)))
            head = payload(out / 'model-audit-round.sh', opened)
            version = (opened / 'kit/KIT_VERSION').read_text().strip()
            files = {}
            for path in sorted(opened.rglob('*')):
                if path.is_file():
                    files[str(path.relative_to(opened))] = path.read_bytes().replace(version.encode(), b'VERSION')
            # The kit version moves the per-file hashes; compare them without it.
            for name in ('SHA256SUMS', 'MANIFEST.json'):
                files[name] = re.sub(rb'[0-9a-f]{64}', b'HASH', files[name])
            trees.append(files)
            outputs.append((re.sub(r'[0-9a-f]{64}', 'SHA', head), result.stdout,
                            (out / 'round-cards.sh').read_text()))
        self.assertEqual(sorted(trees[0]), sorted(trees[1]))
        for name in trees[0]:
            with self.subTest(file=name):
                self.assertEqual(trees[0][name], trees[1][name])
        self.assertEqual(outputs[0], outputs[1])

    def test_default_build_has_no_image_parts(self):
        _, head, opened = self.opened('plain')
        for name in ('IMAGE.txt', 'image.sh', 'run-check.sh', 'pad-proof.json'):
            self.assertFalse((opened / name).exists())
        self.assertIn('"$AUDIT_WORK/venv/bin/python" ./measure.py', (opened / 'jobs/project.sh').read_text())

    def test_image_build_runs_python_in_the_image(self):
        _, _, opened = self.opened('image', '--image', IMAGE, '--image-sha256', SHA)
        self.assertEqual((opened / 'IMAGE.txt').read_text(), 'image: {}\nsha256: {}\n'.format(IMAGE, SHA))
        for name in ('image.sh', 'run-check.sh'):
            self.assertEqual((opened / name).read_bytes(), (CONTAINER / name).read_bytes())
        project = (opened / 'jobs/project.sh').read_text()
        self.assertIn('image_ready 4\n', project)
        self.assertIn('image_python ./measure.py\n', project)
        self.assertNotIn('venv/bin/python', project)
        self.assertNotIn('pip install', project)
        self.assertIn('clear_projection_state\n', project)
        download = (opened / 'jobs/download.sh').read_text()
        self.assertNotIn('pip ', code(download))
        self.assertNotIn('compute_python', download)
        self.assertIn('image_python ./download.py\n', download)
        self.assertTrue((opened / 'env.sh').read_text().endswith('. ./image.sh\n'))
        self.assertIn('image_ready 0\necho \'VERDICT verify OK\'', (opened / '20-verify.sh').read_text())
        self.assertIn('HPC_SYSTEM=${HPC_SYSTEM:-nautilus}', (opened / 'env.sh').read_text())

    def test_image_needs_its_checksum_and_a_plain_path(self):
        for extra in (['--image', IMAGE], ['--image', IMAGE, '--image-sha256', 'abc'],
                      ['--image', '/p/work1/x y.sif', '--image-sha256', SHA],
                      ['--image', 'relative.sif', '--image-sha256', SHA]):
            with self.subTest(extra=extra):
                self.assertNotEqual(self.build('bad', *extra).returncode, 0)

    def test_drifted_source_fails_instead_of_half_applying(self):
        rounds = self.directory / 'rounds'
        shutil.copytree(str(ROOT / 'hpc/rounds/1'), str(rounds / '1'))
        job = rounds / '1/jobs/project.sh'
        job.write_text(job.read_text().replace('image_python', 'x').replace('compute_python\n', 'compute_python  \n'))
        result = self.build('drift', '--image', IMAGE, '--image-sha256', SHA, '--rounds', str(rounds))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('project.sh changed; cannot place', result.stdout)

    def test_jean_needs_image_and_one_of_proof_or_kit_and_verify(self):
        image = ['--image', IMAGE, '--image-sha256', SHA]
        for extra in ([], ['--kit-and-verify'], image, image + ['--kit-and-verify', '--pad-proof', 'x.json']):
            with self.subTest(extra=extra):
                result = self.build('jean', '--system', 'jean', *extra, needs=JEAN_NEEDS)
                self.assertNotEqual(result.returncode, 0)
        result = self.build('jean', '--system', 'jean', '--kit-and-verify', *image)
        self.assertIn('approved subproject', result.stdout)
        self.assertNotEqual(self.build('naut', '--kit-and-verify', *image).returncode, 0)

    def test_jean_kit_and_verify_round(self):
        result, _, opened = self.opened('kv', '--system', 'jean', '--kit-and-verify', '--image', IMAGE,
                                        '--image-sha256', SHA, needs=JEAN_NEEDS)
        round_script = (opened / 'round.sh').read_text()
        self.assertIn('steps=(10-install-kit.sh 20-verify.sh 30-install-reporting.sh)\n', round_script)
        self.assertIn('HPC_SYSTEM=jean\n', round_script)
        self.assertIn('export AUDIT_PROJECTION_ONLY=1\n', round_script)
        self.assertNotIn('40-submit', result.stdout.split('Run: ', 1)[1].split(' -- ')[0])
        self.assertIn('jean.arl.hpc.mil:/p/work1/sdegan/model-audit-round.sh', result.stdout)
        self.assertEqual(json.loads((opened / 'MANIFEST.json').read_text())['steps'],
                         ['10-install-kit.sh', '20-verify.sh', '30-install-reporting.sh'])
        verify = (opened / '20-verify.sh').read_text()
        self.assertNotIn('python3 ./storage.py', verify)
        self.assertNotIn('show_storage', code(verify))
        self.assertNotIn('lfs quota', code(verify))
        self.assertIn('df -P -B1 "$WORKDIR"', verify)

    def test_pad_proof_reads_only_a_good_landed_jean_drop(self):
        pad = self.directory / 'pad'
        pad.mkdir()
        good = 'project: model-audit\nsystem: jean\nround: 1\nexit: 0\nVERDICT round 1 OK\n'
        cases = {'good.log': good, 'nautilus.log': good.replace('jean', 'nautilus'),
                 'failed.log': good.replace('exit: 0', 'exit: 1').replace(' OK', ' FAIL')}
        for name, text in cases.items():
            (pad / name).write_text(text)
        outside = self.directory / 'outside.log'
        outside.write_text(good)
        proof = self.directory / 'proof.json'

        def make(drop):
            return run([sys.executable, str(ROOT / 'hpc/bundle.py'), 'pad-proof', '--pad', str(pad),
                        '--out', str(proof), str(drop)])
        for drop in (pad / 'nautilus.log', pad / 'failed.log', outside):
            with self.subTest(drop=drop.name):
                self.assertNotEqual(make(drop).returncode, 0)
        self.assertEqual(make(pad / 'good.log').returncode, 0)
        receipt = json.loads(proof.read_text())
        self.assertEqual({key: receipt[key] for key in ('project', 'system', 'exit', 'landed')},
                         {'project': 'model-audit', 'system': 'jean', 'exit': 0, 'landed': True})
        self.assertEqual(receipt['drop'], 'good.log')
        return proof

    def test_jean_projection_round(self):
        proof = self.test_pad_proof_reads_only_a_good_landed_jean_drop()
        _, _, opened = self.opened('jp', '--system', 'jean', '--pad-proof', str(proof), '--image', IMAGE,
                                   '--image-sha256', SHA, needs=JEAN_NEEDS)
        self.assertTrue((opened / 'pad-proof.json').exists())
        self.assertFalse((opened / 'jobs/download.sh').exists())
        project = (opened / 'jobs/project.sh').read_text()
        header = [line for line in project.splitlines() if line.startswith('#SBATCH')]
        self.assertIn('#SBATCH --partition=AIML_BACK', header)
        self.assertIn('#SBATCH --gres=gpu:4', header)
        self.assertIn('#SBATCH --account=NRLMR5762B403', header)
        self.assertFalse(any('--qos' in line or '--constraint' in line for line in header))
        self.assertIn('image_ready 4\n', project)
        submit = (opened / '40-submit.sh').read_text()
        self.assertIn('sbatch --parsable --comment=project=model-audit ', submit)
        self.assertNotIn('pad-confirmed', submit)
        self.assertIn('build $stamp', submit)
        self.assertIn('HPC_SYSTEM=jean', (opened / 'env.sh').read_text())
        self.assertIn('--steps ./40-submit.sh', (self.directory / 'jp/round-cards.sh').read_text())
        damaged = self.directory / 'damaged.json'
        damaged.write_text(proof.read_text().replace('"landed": true', '"landed": false'))
        self.assertNotEqual(self.build('jp2', '--system', 'jean', '--pad-proof', str(damaged), '--image', IMAGE,
                                       '--image-sha256', SHA, needs=JEAN_NEEDS).returncode, 0)


class ImageShellTests(unittest.TestCase):
    """The exec line, its binds and the runtime refusal, with stand-in runtimes."""

    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.directory = Path(temporary.name)
        for name in ('work/round', 'home', 'originals/base', 'bin'):
            (self.directory / name).mkdir(parents=True)
        (self.directory / 'work/round/IMAGE.txt').write_text('image: {}\nsha256: {}\n'.format(IMAGE, SHA))
        shutil.copyfile(str(CONTAINER / 'image.sh'), str(self.directory / 'work/round/image.sh'))
        self.environment = {'PATH': str(self.directory / 'bin') + ':/usr/bin:/bin', 'HOME': str(self.directory / 'home'),
                            'WORKDIR': str(self.directory / 'work'), 'HF_HOME': str(self.directory / 'work/cache'),
                            'AUDIT_ORIGINAL': str(self.directory / 'originals/base'), 'AUDIT_WORK': 'x',
                            'CUDA_VISIBLE_DEVICES': '0,1', 'SECRET_THING': 'no'}

    def shell(self, text):
        return run(['bash', '-c', '. ./image.sh\n' + text], cwd=str(self.directory / 'work/round'), env=self.environment)

    def fake(self, name, body):
        path = self.directory / 'bin' / name
        path.write_text('#!/bin/bash\n' + body)
        path.chmod(0o755)

    def test_exec_line_binds_and_environment(self):
        self.fake('apptainer', 'echo "args: $*"\nenv | grep "^APPTAINERENV_" | sort\n')
        result = self.shell('IMAGE_NV=(--nv); image_python ./measure.py')
        self.assertEqual(result.returncode, 0, result.stdout)
        work, home = self.directory / 'work', self.directory / 'home'
        self.assertIn('args: exec --nv --cleanenv --home {} --bind {},{} --pwd {} {} python3 ./measure.py'.format(
            home, work, self.directory / 'originals/base', work / 'round', IMAGE), result.stdout)
        self.assertIn('APPTAINERENV_CUDA_VISIBLE_DEVICES=0,1', result.stdout)
        self.assertIn('APPTAINERENV_AUDIT_ORIGINAL=', result.stdout)
        self.assertNotIn('SECRET_THING', result.stdout)

    def test_singularity_name_is_accepted(self):
        self.fake('singularity', 'echo "args: $1"\nenv | grep -c "^SINGULARITYENV_"\n')
        result = self.shell('image_python -V')
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn('args: exec', result.stdout)

    def test_podman_only_system_refuses_clearly(self):
        self.fake('podman', 'echo podman should not run\n')
        result = self.shell('image_python -V')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('has podman only; this round needs apptainer', result.stdout)
        self.assertNotIn('should not run', result.stdout)

    def test_wrong_image_checksum_fails_before_running(self):
        self.fake('apptainer', 'echo ran\n')
        image = self.directory / 'image.sif'
        image.write_text('not the image\n')
        (self.directory / 'work/round/IMAGE.txt').write_text('image: {}\nsha256: {}\n'.format(image, SHA))
        result = self.shell('image_ready 0')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('FAIL image sha256', result.stdout)
        self.assertNotIn('\nran', result.stdout)


if __name__ == '__main__':
    unittest.main()
