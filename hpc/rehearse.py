# rehearse.py -- Run the bundled round against a small local scheduler.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  exercise build retries, queued copies and failed measurements.
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import resource
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
NEEDS = 'space=160G hours=0 subproject=NRLMR57635502 queue=background for=4h'


class Rehearsal:
    """Keep every fixture in one disposable folder with no network tools."""

    def __init__(self, args, directory):
        self.args = args
        self.directory = Path(directory).resolve()
        if self.directory.exists() and any(self.directory.iterdir()):
            raise ValueError('rehearsal folder must be empty')
        self.directory.mkdir(parents=True, exist_ok=True)
        login = shutil.which(args.login_python)
        compute = shutil.which(args.compute_python)
        if not login or not compute:
            raise ValueError('both interpreter paths must exist')
        self.login, compute = os.path.abspath(login), os.path.abspath(compute)
        if not args.dry_run:
            raise ValueError('this rehearsal requires --dry-run; it uses only the stub checkpoint')
        self.home, self.work, self.binary = [self.directory / name for name in ('home', 'work', 'bin')]
        for path in (self.home / 'bin', self.work, self.binary, self.directory / 'outbox'):
            path.mkdir(parents=True, exist_ok=True)
        compute_bin = self.directory / 'compute-bin'
        compute_bin.mkdir()
        (compute_bin / 'python3').symlink_to(compute)
        for name in ('sbatch', 'hpc'):
            target = self.binary / name
            shutil.copyfile(str(ROOT / 'hpc/fakes' / name), str(target))
            target.chmod(0o755)
        (self.binary / 'python3').symlink_to(self.login)
        self.environment = dict(os.environ, HOME=str(self.home), WORKDIR=str(self.work),
            AUDIT_FAKE_ROOT=str(self.directory), PATH=str(self.binary) + ':' + os.environ['PATH'],
            AUDIT_REHEARSAL='1', AUDIT_STUB='1', AUDIT_FAIL_SECOND='0', AUDIT_FAIL_MEASUREMENT='0',
            AUDIT_FAKE_DEFER='0', AUDIT_BASE=args.base, AUDIT_NAME='rehearsal-base',
            AUDIT_COMPUTE_BIN=str(compute_bin), HPC_SYSTEM='fake', CUDA_VISIBLE_DEVICES='',
            OMP_NUM_THREADS='1', MKL_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1', PYTHONDONTWRITEBYTECODE='1')
        self.round = self.home / 'model-audit/rounds/1'
        self.results = self.work / 'model-audit/rounds/1'
        self.bundle = self.directory / 'bundle'
        self.log = self.directory / 'rehearsal.log'
        self.build()

    def build(self, rounds=None):
        """Build locally; printed desk cards are never executed."""
        command = [self.login, str(ROOT / 'hpc/bundle.py'), 'build', '--needs', NEEDS,
                   '--kit', self.args.kit, '--out', str(self.bundle)]
        if rounds is not None:
            command += ['--rounds', str(rounds)]
        subprocess.check_call(command, env=self.environment, stdout=subprocess.DEVNULL)

    def call(self, command, cwd=None):
        """Append the actual step output, including an expected refusal."""
        with self.log.open('a') as stream:
            result = subprocess.call(command, cwd=str(cwd) if cwd else None, env=self.environment,
                                     stdout=stream, stderr=subprocess.STDOUT)
        output = self.log.read_text()
        if result in (-9, 137) or any(word in output for word in ('MemoryError', 'Cannot allocate memory', 'out of memory')):
            raise ValueError('rehearsal step memory ceiling exceeded; see ' + str(self.log))
        return result

    def run(self):
        """Open the verified bundle in its fake home and run all numbered steps."""
        return self.call([str(self.bundle / 'model-audit-round.sh'), '1'])

    def rows(self):
        """Scheduler records, rather than a hand-written outcome list, are the evidence."""
        ledger = self.directory / 'submissions.jsonl'
        return [json.loads(line) for line in ledger.read_text().splitlines()] if ledger.exists() else []

    def append(self, line):
        with self.log.open('a') as stream:
            stream.write(line + '\n')

    def tail(self, label):
        """Show the actual ending of this case's log."""
        print('--- ' + label + ' ---')
        print('\n'.join(self.log.read_text().splitlines()[-8:]))

    def expect(self, condition, message):
        if not condition:
            raise ValueError(message + '; see ' + str(self.log))

    def clean(self):
        """Check both job exits, the dependency and the round's returned verdict."""
        result = self.run()
        rows = self.rows()
        self.expect(result == 0 and [row['status'] for row in rows] == ['finished', 'finished'],
                    'clean rehearsal failed')
        second = rows[1]['arguments']
        self.expect('--dependency=afterok:1001' in second and '--kill-on-invalid-dep=yes' in second,
                    'projection dependency is missing')
        self.expect('VERDICT round 1 OK' in self.log.read_text(), 'round success was not logged')
        self.append('Rehearsal: both jobs completed; job exits ' + str([row['exit'] for row in rows]))
        self.append('VERDICT rehearsal OK')

    def changed_sources(self, broken=False):
        """Rebuild from changed content, without editing the repository fixture."""
        rounds = self.directory / 'sources'
        shutil.copytree(str(ROOT / 'hpc/rounds/1'), str(rounds / '1'))
        if broken:
            path = rounds / '1/20-verify.sh'
            path.write_text(path.read_text().replace('python3 ./login.py', "echo 'broken verify step'; exit 31"))
        else:
            path = rounds / '1/login.py'
            path.write_text(path.read_text() + "\nprint('rebuilt login check')\n")
        self.build(rounds)

    def dependent_probe(self):
        """A measurement failure must cancel a later afterok job too."""
        probe = self.directory / 'after-measure.sh'
        probe.write_text('#!/bin/bash\nset -euo pipefail\necho unexpected-dependent-start\n')
        self.call([str(self.binary / 'sbatch'), '--parsable', '--dependency=afterok:1002',
                   '--kill-on-invalid-dep=yes', str(probe)])
        self.expect(self.rows()[-1]['status'] == 'cancelled-invalid-dependency',
                    'failed measurement allowed an afterok child to start')
        self.append('afterok child: ' + self.rows()[-1]['status'])


def suite(args):
    """Run every requested counterexample and check its recorded outcome."""
    directory = Path(args.directory).resolve()
    if directory.exists() and any(directory.iterdir()):
        raise ValueError('rehearsal folder must be empty')
    directory.mkdir(parents=True, exist_ok=True)
    clean = Rehearsal(args, directory / 'clean')
    clean.clean()
    clean.tail('clean pass')

    guard = Rehearsal(args, directory / 'guard')
    guard.environment['AUDIT_FAKE_DEFER'] = '1'
    guard.expect(guard.run() == 0, 'first build submission failed')
    before = guard.rows()
    old_stamp = (guard.round / 'BUILD-STAMP.txt').read_text().strip()
    result = guard.call(['./round.sh', '--only', '40-submit.sh'], guard.round)
    guard.expect(result != 0 and len(guard.rows()) == len(before) and 'already submitted' in guard.log.read_text(),
                 'same build was not refused')
    guard.tail('guard same-build-refused')
    guard.changed_sources()
    guard.expect(guard.run() == 0 and len(guard.rows()) == 4, 'rebuilt bundle was not allowed')
    stamp = (guard.round / 'BUILD-STAMP.txt').read_text().strip()
    state = (guard.results / 'state/round-1-submissions').read_text()
    guard.expect(stamp != old_stamp and old_stamp in state and stamp in state, 'build history was lost')
    guard.append('new build submitted: ' + stamp)
    guard.append('scheduler states: ' + ', '.join(row['status'] for row in guard.rows()))
    guard.tail('guard new-build-allowed')

    pinned = Rehearsal(args, directory / 'pinned')
    pinned.environment['AUDIT_FAKE_DEFER'] = '1'
    pinned.expect(pinned.run() == 0, 'queued submission failed')
    shutil.rmtree(str(pinned.round))
    pinned.round.mkdir(parents=True)
    (pinned.round / 'env.sh').write_text("echo 'overwritten home copy ran'; exit 99\n")
    result = pinned.call([str(pinned.binary / 'sbatch'), '--run-pending'])
    rows = pinned.rows()
    pinned.expect(result == 0 and all(row['status'] == 'finished' for row in rows), 'pinned jobs failed after overwrite')
    for row in rows:
        card = json.loads((pinned.home / '.hpc/jobs' / (row['job'] + '.json')).read_text())
        sha = row['started_snapshot_sha256']
        pinned.expect(sha == row['snapshot']['sha256'] == card['snapshot']['sha256'], 'pinned hash differs')
        drop = (pinned.directory / 'outbox' / (row['job'] + '-drop.txt')).read_text()
        pinned.expect(sha in drop, 'snapshot hash was not delivered')
        pinned.append('job {} pinned hash matches: {}'.format(row['job'], sha))
    pinned.tail('overwrite-pinned')

    stale = Rehearsal(args, directory / 'stale')
    stale.environment['AUDIT_FAKE_DEFER'] = '1'
    stale.expect(stale.run() == 0, 'stale case submission failed')
    planted = stale.results / 'derived/rehearsal-base/single-projection/previous-round.txt'
    planted.parent.mkdir(parents=True)
    planted.write_text('left over from a previous round\n')
    os.utime(str(planted), (1, 1))
    stale.call([str(stale.binary / 'sbatch'), '--run-pending'])
    rows = stale.rows()
    stale.expect(rows[1]['status'] == 'failed' and rows[1]['exit'] != 0, 'stale file did not fail the job')
    stale.expect('stale measurement input refused: ' + str(planted) in Path(rows[1]['log']).read_text(),
                 'stale refusal did not name the input')
    stale.environment['AUDIT_FAKE_DEFER'] = '0'
    stale.dependent_probe()
    stale.tail('stale-fails')

    forced = Rehearsal(args, directory / 'forced')
    forced.environment['AUDIT_FAIL_MEASUREMENT'] = '1'
    forced.run()
    rows = forced.rows()
    forced.expect(len(rows) == 2 and rows[1]['status'] == 'failed' and rows[1]['exit'] == 23,
                  'forced measurement fault did not fail the job')
    forced.expect(not (forced.results / 'state/compare.done').exists(), 'failed measurement wrote a done marker')
    for line in Path(rows[1]['log']).read_text().splitlines()[-4:]:
        forced.append(line)
    forced.dependent_probe()
    forced.append('measurement job: {}; exit {}'.format(rows[1]['status'], rows[1]['exit']))
    forced.tail('forced-failure')

    broken = Rehearsal(args, directory / 'broken')
    broken.changed_sources(broken=True)
    try:
        broken.clean()
    except ValueError as error:
        broken.expect('VERDICT round 1 FAIL' in broken.log.read_text() and not broken.rows(),
                      'broken round reached submission or lacked a failed verdict')
        broken.append('VERDICT self-test FAIL: ' + str(error))
    else:
        raise ValueError('self-test accepted a deliberately broken round')
    broken.tail('self-test FAIL')
    print('All seven observed outcomes matched the requested cases.')


def rehearse(args):
    """Keep the single-case command useful for the unit tests as well."""
    if args.suite:
        suite(args)
        return
    run = Rehearsal(args, args.directory)
    if args.fail_second:
        run.environment['AUDIT_FAIL_SECOND'] = '1'
        result = run.run()
        run.expect(result != 0 and [row['status'] for row in run.rows()] == ['finished', 'rejected'],
                   'forced submission failure did not fail the round')
        run.append('VERDICT rehearsal OK')
    else:
        run.clean()
    print('\n'.join(run.log.read_text().splitlines()[-30:]))


if __name__ == '__main__':
    limit = resource.getrlimit(resource.RLIMIT_AS)[0]
    if limit == resource.RLIM_INFINITY or limit > 4000000 * 1024:
        wrapper = str(ROOT / 'hpc/rehearse.sh')
        os.execv(wrapper, [wrapper, '--memory-command', sys.executable, str(Path(__file__).resolve())] + sys.argv[1:])
    parser = argparse.ArgumentParser()
    parser.add_argument('directory')
    parser.add_argument('--base', default='rehearsal/stub')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--suite', action='store_true')
    parser.add_argument('--fail-second', action='store_true')
    parser.add_argument('--kit', default='/root/work/hpc-kit-wt')
    parser.add_argument('--login-python', default='python3')
    parser.add_argument('--compute-python', default='python3')
    arguments = parser.parse_args()
    try:
        rehearse(arguments)
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        parser.exit(1, str(error) + '\n')
