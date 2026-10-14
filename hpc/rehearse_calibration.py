# rehearse_calibration.py -- Read calibration outcomes from a local scheduler.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  check missing wheels and count the real text writers.
# Modified: SDE 2026-10-14  exercise one job, clean retries and pinned submissions.
import argparse
import json
import os
from pathlib import Path
import resource
import shlex
import shutil
import subprocess
import sys

from rehearse import Rehearsal

ROOT = Path(__file__).resolve().parent.parent
NEEDS = 'space=80G hours=0 subproject=NRLMR57635502 queue=background for=4h'


def header(name, purpose):
    """Sign the small scripts written into disposable rehearsal folders."""
    return ('#!/bin/bash\n# {} -- {}\n# Created by Sean Egan 2026-10-14\n'
            '# Modified: SDE 2026-10-14  check a local failure case.\n').format(name, purpose)


class CalibrationRehearsal(Rehearsal):
    """Reuse the fenced scheduler and keep all calibration evidence together."""

    def __init__(self, args, directory):
        """Build the round and seed its read-only shared-download fixture."""
        super().__init__(args, directory)
        self.compute = os.path.abspath(os.readlink(str(Path(self.environment['AUDIT_COMPUTE_BIN']) / 'python3')))
        self.compute_version = subprocess.check_output([self.compute, '--version'], universal_newlines=True).strip()
        self.compute_wrapper()
        self.original = self.work / 'model-audit/originals/rehearsal-base'
        self.receipt = self.work / 'model-audit/rounds/1/state/download.done'
        self.report = self.results / 'measurements/rehearsal-base/norm-preserving.json'
        self.card = self.report.with_name('norm-preserving.card.json')
        self.derived = self.results / 'derived/rehearsal-base/norm-preserving'
        environment = dict(self.environment, AUDIT_ORIGINAL=str(self.original))
        subprocess.check_call(['nice', '-n', '19', self.compute,
            str(ROOT / 'hpc/rounds/4/measure.py'), '--seed-original'], env=environment)
        self.receipt.parent.mkdir(parents=True, exist_ok=True)
        self.receipt.write_text('synthetic verified download\n')
        wheels = self.receipt.parent.parent / 'wheels'
        wheels.mkdir()
        self.wheels = wheels
        self.wheel_pins = []
        for line in (ROOT / 'hpc/rounds/4/compute-requirements.txt').read_text().splitlines():
            line = line.strip()
            if line and not line.startswith('#'):
                name, version = line.split('==')
                filename = '{}-{}-py3-none-any.whl'.format(name.replace('-', '_'), version)
                (wheels / filename).write_bytes(b'')
                self.wheel_pins.append((line, filename))

    def compute_wrapper(self, planted=None):
        """Use installed rehearsal packages without applying the wheel-install version check."""
        interpreter = Path(self.environment['AUDIT_COMPUTE_BIN']) / 'python3'
        if interpreter.exists():
            interpreter.unlink()
        body = header('python3', 'Run the installed synthetic rehearsal interpreter.')
        body += ('set -euo pipefail\nif [ "${1:-}" = ./runtime.py ]; then\n'
                 '    echo ' + shlex.quote('synthetic rehearsal interpreter: ' + self.compute_version) +
                 '\n    exit 0\nfi\n')
        if planted is not None:
            body += ('if [ "${1:-}" = ./measure.py ]; then\n'
                     '    mkdir -p ' + shlex.quote(str(planted.parent)) + '\n'
                     '    printf "old input\\n" > ' + shlex.quote(str(planted)) + '\n'
                     '    touch -d @1 ' + shlex.quote(str(planted)) + '\nfi\n')
        interpreter.write_text(body + 'exec ' + shlex.quote(self.compute) + ' "$@"\n')
        interpreter.chmod(0o755)

    def build(self, rounds=None):
        """Build cards locally; their commands are only printed."""
        self.round = self.home / 'model-audit/rounds/4'
        self.results = self.work / 'model-audit/rounds/4'
        arguments = ['nice', '-n', '19', self.login, str(ROOT / 'hpc/calibrate_bundle.py'),
                     'build', '--needs', NEEDS, '--kit', self.args.kit, '--out', str(self.bundle)]
        if rounds is not None:
            arguments += ['--rounds', str(rounds)]
        subprocess.check_call(arguments, env=self.environment, stdout=subprocess.DEVNULL)

    def run(self):
        """Open round 4 through its calibration bundle."""
        return self.call([str(self.bundle / 'model-audit-calibrate.sh'), '4'])

    def observed_job(self, row):
        """Append scheduler status and the relevant lines from the job log."""
        self.append('scheduler job {}: {}; exit {}'.format(row['job'], row['status'], row.get('exit')))
        if 'log' in row:
            for line in Path(row['log']).read_text().splitlines():
                if any(word in line for word in ('fingerprint:', 'checksum differs', 'stale measurement',
                                                 'measurement failed', 'snapshot verified:',
                                                 'no text residual writers were projected')):
                    self.append(line)

    def clean(self):
        """Check the one-job result, card contents and untouched vision weights."""
        result = self.run()
        rows = self.rows()
        for row in rows:
            self.observed_job(row)
        if any(row['status'] != 'finished' or row['exit'] != 0 for row in rows):
            print('\n'.join(self.log.read_text().splitlines()[-30:]))
        self.expect(result == 0 and len(rows) == 1 and rows[0]['status'] == 'finished'
                    and rows[0]['exit'] == 0, 'clean rehearsal failed')
        row = rows[0]
        self.expect(not any(arg.startswith('--dependency') for arg in row['arguments'])
                    and row['arguments'][-1].endswith('/jobs/calibrate.sh'), 'calibration submission differs')
        self.expect('VERDICT round 4 OK' in self.log.read_text(), 'round success was not logged')
        self.expect(self.report.is_file() and self.card.is_file(), 'comparison or fingerprint card missing')
        card = json.loads(self.card.read_text())
        self.expect(card['changed_outside_recipe'] == [], 'unexpected changed tensors')
        for kind in ('attention_output', 'feed_forward_down'):
            self.expect(kind in card['per_kind'], 'missing tensor kind: ' + kind)
            values = card['per_kind'][kind]
            self.append('{}: changed {}'.format(kind, values['changed']))
            self.expect(values['changed'] == 2, 'expected two changed text writers: ' + kind)
            self.append('{}: row_norm_max_relative_error {}; min first_singular_energy_share {}'.format(
                kind, values['row_norm_max_relative_error'], values['first_singular_energy_share']['min']))
        code = ("from audit.weights import TensorStore\nimport torch\ntorch.set_num_threads(1)\n"
                "a = TensorStore({!r}); b = TensorStore({!r})\n"
                "names = [n for n in a.names if 'vision' in n or 'multi_modal_projector' in n]\n"
                "assert names\nassert all(torch.equal(a.get(n), b.get(n)) for n in names)\n"
                "print('vision and projector tensors: bit-identical')\n").format(str(self.original), str(self.derived))
        self.expect(self.call(['nice', '-n', '19', self.compute, '-c', code], ROOT) == 0,
                    'vision or projector tensor changed')
        self.append('VERDICT rehearsal OK')

    def changed_sources(self, broken=False):
        """Make a second stamp from changed sources without editing the repo."""
        rounds = self.directory / 'sources'
        shutil.copytree(str(ROOT / 'hpc/rounds/4'), str(rounds / '4'))
        if broken:
            path = rounds / '4/20-verify.sh'
            lines = path.read_text().splitlines(True)
            lines.insert(4, "echo 'broken verify step'; exit 31\n")
            path.write_text(''.join(lines))
        else:
            path = rounds / '4/login.py'
            path.write_text(path.read_text() + "\nprint('rebuilt login check')\n")
        self.build(rounds)

    def pending(self):
        """Run queued fake jobs and inspect their ledger rather than the submit exit."""
        self.call([str(self.binary / 'sbatch'), '--run-pending'])
        row = self.rows()[-1]
        self.observed_job(row)
        return row

    def prior_try(self):
        """Check scratch cleanup and preserve round 1's original and completion time."""
        self.clean()
        manifest = (self.original / 'download-manifest.json').read_bytes()
        download_time = self.receipt.stat().st_mtime_ns
        paths = [self.results / ('state/calibration/' + name) for name in (
            'context.json', 'harmful-00.safetensors', 'refusal-direction.safetensors', 'timing.json')]
        paths += [self.results / ('state/' + name) for name in (
            'calibrate-activations.done', 'calibrate-transform.done', 'calibrate-compare.done', 'calibrate.done')]
        paths += [self.derived / 'stale.txt', self.report, self.card]
        for path in paths:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text('{}\n')
            os.utime(str(path), (1, 1))
        self.changed_sources()
        self.environment['AUDIT_FAKE_DEFER'] = '1'
        self.expect(self.run() == 0 and len(self.rows()) == 2, 'retry submission failed')
        row = self.pending()
        self.expect(row['status'] == 'finished' and row['exit'] == 0, 'retry job failed')
        self.expect(all(not path.exists() or path.stat().st_mtime > 1 for path in paths), 'old-dated file survived')
        self.expect((self.original / 'download-manifest.json').read_bytes() == manifest
                    and self.receipt.stat().st_mtime_ns == download_time, 'verified download changed')
        self.append('prior-try-state-cleared: old-dated files absent; original manifest and download time unchanged')

    def missing_receipt(self):
        """Read a missing-download refusal before any scheduler row appears."""
        self.receipt.unlink()
        result = self.run()
        text = self.log.read_text()
        self.expect(result != 0 and 'VERDICT round 4 FAIL' in text
                    and str(self.receipt) in text and not self.rows(), 'missing download was not refused')
        self.append('round exit {}; scheduler rows {}'.format(result, len(self.rows())))

    def missing_wheel(self):
        """Refuse an incomplete wheelhouse before a scheduler row is written."""
        pin, filename = self.wheel_pins[0]
        (self.wheels / filename).unlink()
        result = self.run()
        text = self.log.read_text()
        self.expect(result != 0 and 'VERDICT round 4 FAIL' in text
                    and 'wheel missing: ' + pin in text and not self.rows(),
                    'missing wheel was not refused')
        self.append('wheel missing: ' + pin)
        self.append('round exit {}; scheduler rows {}'.format(result, len(self.rows())))

    def corrupt_original(self):
        """Corrupt one queued input and read the checksum refusal from its log."""
        self.environment['AUDIT_FAKE_DEFER'] = '1'
        self.expect(self.run() == 0, 'corrupt case submission failed')
        shard = next(self.original.glob('*.safetensors'))
        with shard.open('r+b') as stream:
            stream.seek(-1, 2)
            byte = stream.read(1)
            stream.seek(-1, 2)
            stream.write(bytes([byte[0] ^ 1]))
        row = self.pending()
        self.expect(row['status'] == 'failed' and row['exit'] != 0
                    and 'original checksum differs' in Path(row['log']).read_text(), 'corrupt original was accepted')

    def stale_input(self):
        """Plant an old input at the compute read after job cleanup has finished."""
        self.environment['AUDIT_FAKE_DEFER'] = '1'
        self.expect(self.run() == 0, 'stale case submission failed')
        planted = self.derived / 'previous-try.txt'
        self.compute_wrapper(planted)
        row = self.pending()
        self.expect(row['status'] == 'failed' and row['exit'] != 0 and
                    'stale measurement input refused: ' + str(planted) in Path(row['log']).read_text(),
                    'stale input was not named and refused')

    def forced_failure(self):
        """Preserve exit 23 and leave comparison completion and the card absent."""
        self.environment['AUDIT_FAIL_MEASUREMENT'] = '1'
        self.run()
        rows = self.rows()
        self.expect(len(rows) == 1 and rows[0]['status'] == 'failed' and rows[0]['exit'] == 23,
                    'forced comparison exit was lost')
        self.expect(not (self.results / 'state/calibrate-compare.done').exists()
                    and not self.card.exists(), 'failed comparison wrote a completion record')
        self.observed_job(rows[0])

    def guard(self):
        """Reject a repeated stamp and retain both stamps after a rebuild."""
        self.environment['AUDIT_FAKE_DEFER'] = '1'
        self.expect(self.run() == 0, 'guard first submission failed')
        before = self.rows()
        old_stamp = (self.round / 'BUILD-STAMP.txt').read_text().strip()
        result = self.call(['./round.sh', '--only', '40-submit.sh'], self.round)
        self.expect(result != 0 and self.rows() == before and
                    'This build already submitted a job: ' + old_stamp in self.log.read_text(),
                    'same stamp was not refused')
        refusal = next(line for line in self.log.read_text().splitlines()
                       if line.startswith('This build already submitted a job:'))
        self.changed_sources()
        self.expect(self.run() == 0 and len(self.rows()) == 2, 'new build was not allowed')
        new_stamp = (self.round / 'BUILD-STAMP.txt').read_text().strip()
        state = (self.results / 'state/round-4-submissions').read_text()
        self.expect(old_stamp != new_stamp and old_stamp in state and new_stamp in state, 'build history was lost')
        self.append(refusal)
        self.append('retained build stamps: ' + old_stamp + ' ' + new_stamp)
        self.append('scheduler rows: ' + str(len(self.rows())))

    def overwrite_pinned(self):
        """Start a queued snapshot after the interactive round folder is replaced."""
        self.environment['AUDIT_FAKE_DEFER'] = '1'
        self.expect(self.run() == 0, 'pinned submission failed')
        shutil.rmtree(str(self.round))
        self.round.mkdir(parents=True)
        (self.round / 'env.sh').write_text(header('env.sh', 'Refuse use of the overwritten home copy.') +
                                          "echo 'overwritten home copy ran'; exit 99\n")
        row = self.pending()
        self.expect(row['status'] == 'finished' and row['exit'] == 0, 'pinned job failed after overwrite')
        card = json.loads((self.home / '.hpc/jobs' / (row['job'] + '.json')).read_text())
        sha = row['started_snapshot_sha256']
        self.expect(sha == row['snapshot']['sha256'] == card['snapshot']['sha256'], 'pinned hash differs')
        self.expect(sha in (self.directory / 'outbox' / (row['job'] + '-drop.txt')).read_text(),
                    'snapshot hash missing from outbox drop')
        self.append('job {} pinned hash matches: {}'.format(row['job'], sha))

    def self_test(self):
        """A deliberately broken verify step must fail the clean expectation."""
        self.changed_sources(broken=True)
        try:
            self.clean()
        except ValueError as error:
            self.expect('VERDICT round 4 FAIL' in self.log.read_text() and not self.rows(),
                        'broken round reached submission or lacked a failed verdict')
            self.append('VERDICT self-test FAIL: ' + str(error))
        else:
            raise ValueError('self-test accepted a deliberately broken round')


def suite(args):
    """Count cases only after their recorded outcomes match the requested result."""
    directory = Path(args.directory).resolve()
    if directory.exists() and any(directory.iterdir()):
        raise ValueError('rehearsal folder must be empty')
    directory.mkdir(parents=True, exist_ok=True)
    cases = (('clean pass', 'clean'), ('prior-try-state-cleared', 'prior_try'),
             ('missing-wheel', 'missing_wheel'),
             ('missing-download-receipt', 'missing_receipt'), ('corrupt-original', 'corrupt_original'),
             ('stale-input', 'stale_input'), ('forced-failure', 'forced_failure'), ('guard', 'guard'),
             ('overwrite-pinned', 'overwrite_pinned'), ('self-test', 'self_test'))
    matched = 0
    for label, method in cases:
        run = CalibrationRehearsal(args, directory / method)
        getattr(run, method)()
        matched += 1
        run.tail(label)
    print('All ten observed outcomes matched the requested cases.' if matched == 10 else
          '{} observed outcomes matched the requested cases.'.format(matched))


def main():
    """Run one clean case by default and fence every child under the memory cap."""
    limit = resource.getrlimit(resource.RLIMIT_AS)[0]
    if limit == resource.RLIM_INFINITY or limit > 4000000 * 1024:
        wrapper = str(ROOT / 'hpc/rehearse.sh')
        os.execv(wrapper, [wrapper, '--memory-command', 'nice', '-n', '19',
                          sys.executable, str(Path(__file__).resolve())] + sys.argv[1:])
    parser = argparse.ArgumentParser()
    parser.add_argument('directory')
    parser.add_argument('--suite', action='store_true')
    parser.add_argument('--kit', default='/root/work/hpc-kit-wt')
    parser.add_argument('--login-python', default='python3')
    parser.add_argument('--compute-python', default=str(ROOT / '.venv/bin/python'))
    parser.add_argument('--dry-run', action='store_true', required=True)
    parser.add_argument('--base', default='rehearsal/synthetic')
    args = parser.parse_args()
    try:
        if args.suite:
            suite(args)
        else:
            run = CalibrationRehearsal(args, args.directory)
            run.clean()
            print('\n'.join(run.log.read_text().splitlines()[-30:]))
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        parser.exit(1, str(error) + '\n')


if __name__ == '__main__':
    main()
