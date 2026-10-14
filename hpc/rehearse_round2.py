# rehearse_round2.py -- Exercise the five-piece census with artificial tensors.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  read pass, cancellation and broken-step outcomes from logs.
# Modified: SDE 2026-10-15  real tensor names, the tested pins, lineage, stale, stamp and pinned cases.
# Modified: SDE 2026-10-15  check that no printed line runs past 100 columns.
import argparse
import ast
import json
import os
from pathlib import Path
import shutil
import shlex
import subprocess
import sys
import tempfile
import time
from rehearse import Rehearsal, ROOT

NEEDS = 'space=1T hours=0 subproject=NRLMR57635502 queue=background for=4h'
BUNDLE = 'model-audit-census.sh'
NAMES = ROOT / 'tests/fixtures/round2'
# The venv built from the cluster pins, when this machine has one.
CLUSTER_PYTHON = ROOT / '.venv-cluster/bin/python'
WRITERS = ('attention_output', 'feed_forward_down', 'expert_down')


def fixture_kit(directory):
    """The rehearsal's reporting helper writes real cards into its fake home."""
    directory.mkdir(parents=True)
    tree = ast.parse((ROOT / 'hpc/rounds/2/bundle.py').read_text())
    assignment = next(node for node in tree.body if isinstance(node, ast.Assign) and node.targets[0].id == 'KIT_FILES')
    for name in ast.literal_eval(assignment.value):
        (directory / name).write_text('#!/bin/bash\n# Local reporting fixture.\nKIT_VERSION=0\n')
    (directory / 'hpc-report.sh').write_text('''#!/bin/bash
# hpc-report.sh -- Write local rehearsal cards without a network.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  retain the job description and its exit event.
hpc_job_start() {
    mkdir -p "$HOME/.hpc/jobs"
    printf '{"v":1,"job":"%s","description":"%s","project":"model-audit"}\\n' "$HPC_JOB_ID" "$1" > "$HOME/.hpc/jobs/$HPC_JOB_ID.json"
}
hpc_job_finish() { echo "card event: finished; $*"; }
hpc_job_fail() { echo "card event: failed; $*"; }
''')
    return directory


def captured(command, env=None):
    """Run a command and keep its exit and combined output."""
    process = subprocess.Popen(command, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                               universal_newlines=True)
    output = process.communicate()[0]
    return argparse.Namespace(returncode=process.returncode, stdout=output)


def wrapper(path, target, prelude=''):
    """A venv interpreter loses its packages behind a symlink, so call it through a script."""
    if path.exists() or path.is_symlink():
        path.unlink()
    path.write_text('#!/bin/bash\nset -euo pipefail\n' + prelude + 'exec ' + shlex.quote(target) + ' "$@"\n')
    path.chmod(0o755)


class CensusRehearsal(Rehearsal):
    """Use round 1's fake scheduler and drop transport, without running round 1."""

    def __init__(self, args, directory):
        super().__init__(args, directory)
        wrapper(self.binary / 'python3', self.login)
        self.compute = os.path.abspath(args.compute_python)
        wrapper(self.directory / 'compute-bin/python3', self.compute)
        self.environment.update(AUDIT_STUB_NAMES=str(NAMES), AUDIT_LEAN_ELEMENTS='32')

    def build(self, rounds=None, manifest=None, check=True):
        self.round = self.home / 'model-audit/rounds/2'
        self.results = self.work / 'model-audit/rounds/2'
        command = [self.login, str(ROOT / 'hpc/rounds/2/bundle.py'), 'build', '--round', '2',
                   '--system', 'nautilus', '--needs', NEEDS, '--kit', self.args.kit, '--out', str(self.bundle)]
        if rounds is not None:
            command += ['--rounds', str(rounds)]
        if manifest is not None:
            command += ['--manifest', str(manifest)]
        result = captured(command, env=self.environment)
        (self.directory / 'builder.log').write_text(result.stdout)
        if check and result.returncode:
            raise ValueError('bundle build failed: ' + result.stdout)
        return result

    def run(self, *extra):
        return self.call([str(self.bundle / BUNDLE), '2'] + list(extra))

    def queued(self):
        """Submit with the scheduler holding everything, then check the chain's shape."""
        self.environment['AUDIT_FAKE_DEFER'] = '1'
        self.expect(self.run() == 0, 'round 2 submission failed')
        rows = self.rows()
        self.expect(len(rows) == 6 and all(row['status'] == 'queued' for row in rows), 'expected one transfer and five pieces')
        self.expect(not any(arg.startswith('--dependency') for arg in rows[0]['arguments']), 'first job has a dependency')
        for previous, row in zip(rows, rows[1:]):
            self.expect('--dependency=afterok:' + previous['job'] in row['arguments'] and
                        '--kill-on-invalid-dep=yes' in row['arguments'], 'afterok chain is missing')
        for row in rows:
            self.expect(row['cwd'].startswith(str(self.results / 'submissions')), 'job lacks pinned snapshot')
            self.expect('--comment=project=model-audit' in row['arguments'], 'job lacks the owner tag')
        return rows

    def checked(self):
        self.queued()
        return self.call([str(self.binary / 'sbatch'), '--run-pending'])

    def tail(self, label, count=8):
        """Show the actual ending of this case's log."""
        print('--- ' + label + ' ---')
        print('\n'.join(self.log.read_text().splitlines()[-count:]))

    def scheduler_tail(self):
        for row in self.rows():
            self.append('scheduler job {}: {}; exit {}'.format(row['job'], row['status'], row.get('exit', 'not-started')))

    def changed(self, edit):
        """Rebuild from a changed copy of the round, never the repository files."""
        rounds = self.directory / ('sources-' + str(len(list(self.directory.glob('sources-*')))))
        shutil.copytree(str(ROOT / 'hpc/rounds/2'), str(rounds / '2'), ignore=shutil.ignore_patterns('__pycache__'))
        edit(rounds / '2')
        self.build(rounds)

    def broken(self):
        def edit(folder):
            path = folder / '20-verify.sh'
            path.write_text(path.read_text().replace('python3 ./login.py', "echo 'broken verify step'; exit 31"))
        self.changed(edit)

    def wide_lines(self):
        """Every line our scripts printed: piece logs and the round's end logs."""
        found = []
        logs = list((self.results / 'logs').glob('*.out')) + list((self.directory / 'outbox').glob('*end.log'))
        for path in logs:
            for line in path.read_text().splitlines():
                if len(line) > 100:
                    found.append('{} ({} chars): {}'.format(path.name, len(line), line[:60]))
        return len(logs), found


def expected_writers(number):
    """Residual writers counted from the published names of the pair's original."""
    sys.path.insert(0, str(ROOT))
    sys.path.insert(0, str(ROOT / 'hpc/rounds/2'))
    from audit.weights import recipe_table, tensor_kind
    from measure import census_kinds
    batch = json.loads((ROOT / 'data/batches/round-2-batch-1.json').read_text())
    model = batch['pairs'][number - 1]['original']
    names = json.loads((NAMES / (model['revision'][:12] + '.json')).read_text())['tensors']
    table = census_kinds(recipe_table())
    counts = {}
    for name in names:
        kind = tensor_kind(name, table)
        if kind in WRITERS:
            counts[kind] = counts.get(kind, 0) + 1
    return model['hub_id'], counts


def planted_manifest(directory):
    """A Qwen-based copy slipped into the batch; the screen has to stop it."""
    record = json.loads((ROOT / 'data/batches/round-2-batch-1.json').read_text())
    copy = record['pairs'][4]['modified']
    copy['hub_id'] = 'someone/Qwen2.5-7B-Instruct-abliterated'
    copy['maker'] = 'someone'
    copy['declared_base_model'] = 'Qwen/Qwen2.5-7B-Instruct'
    copy['base_model_chain'] = [{'hub_id': 'Qwen/Qwen2.5-7B-Instruct', 'maker': 'qwen', 'revision': 'a' * 40,
                                 'declared_base_model': None, 'base_model_chain': [], 'lineage_known': True,
                                 'publisher_root': True}]
    path = directory / 'planted-batch.json'
    path.write_text(json.dumps(record, indent=2) + '\n')
    return path


def suite(args, directory):
    started = time.monotonic()
    clean = CensusRehearsal(args, directory / 'pass')
    clean.append('compute interpreter: ' + clean.compute)
    clean.expect(clean.checked() == 0, 'round 2 jobs did not complete')
    clean.expect(all(row['status'] == 'finished' for row in clean.rows()), 'a clean piece failed')
    for number in range(1, 6):
        measurement = clean.results / 'measurements' / ('pair-' + str(number))
        receipt = json.loads((measurement / 'receipt.json').read_text())
        clean.expect(all(not Path(path).exists() for path in receipt['deleted_checkpoints']), 'weights survived compare')
        clean.expect((measurement / 'metadata.json').is_file() and (measurement / 'card.md').is_file(), 'reports are missing')
        card = json.loads((clean.home / '.hpc/jobs' / (str(1001 + number) + '.json')).read_text())
        clean.expect(card['snapshot']['sha256'] == clean.rows()[number]['started_snapshot_sha256'], 'card snapshot differs')
        report = json.loads((measurement / 'weights.json').read_text())
        model, wanted = expected_writers(number)
        found = {}
        for name in report['summary']['changed_set']:
            kind = report['tensors'][name]['kind']
            found[kind] = found.get(kind, 0) + 1
        lean = sum(1 for row in report['tensors'].values() if row.get('lean'))
        clean.expect(found == wanted and all(wanted.values()), 'changed writers differ from the real names')
        clean.expect(not report['original_only'] and not report['modified_only'], 'tensor names differ across a pair')
        clean.append('pair {} {}: {} tensors; changed {}; lean {}; {}'.format(
            number, model.split('/')[1], len(report['tensors']), json.dumps(found, sort_keys=True), lean,
            report['summary']['assessment']))
    clean.scheduler_tail()
    count, wide = clean.wide_lines()
    clean.expect(not wide, 'printed lines over 100 columns: ' + '; '.join(wide[:5]))
    clean.append('line width: {} logs, longest printed line within 100 columns'.format(count))
    clean.append('owner tag: all {} jobs carry --comment=project=model-audit'.format(len(clean.rows())))
    clean.tail('round-2 pass', 14)

    screen = CensusRehearsal(args, directory / 'lineage')
    planted = planted_manifest(screen.directory)
    result = screen.build(manifest=planted, check=False)
    screen.expect(result.returncode != 0 and 'banned lineage refused' in result.stdout, 'planted Qwen row was built')
    screen.append('builder refused the planted row: exit {}'.format(result.returncode))
    for line in result.stdout.splitlines():
        screen.append('  ' + line)
    refused = captured([screen.login, str(ROOT / 'hpc/lineage.py'), str(planted), str(ROOT / 'hpc/banned-makers.txt')])
    screen.expect(refused.returncode != 0 and 'Qwen' in refused.stdout, 'job-side screen passed the planted row')
    screen.append('job-side screen: exit {}; scheduler rows {}'.format(refused.returncode, len(screen.rows())))
    screen.tail('lineage refusal')

    forced = CensusRehearsal(args, directory / 'forced')
    forced.environment['AUDIT_FAIL_MEASUREMENT'] = '1'
    forced.expect(forced.checked() != 0, 'forced comparison unexpectedly passed')
    rows = forced.rows()
    forced.expect(rows[1]['exit'] == 23 and rows[1]['status'] == 'failed' and
                  all(row['status'] == 'cancelled-invalid-dependency' for row in rows[2:]), 'failure did not cancel the chain')
    forced.expect(not (forced.results / 'pieces/pair-1/state/compare.done').exists(), 'failed compare wrote a done marker')
    for line in Path(rows[1]['log']).read_text().splitlines():
        if 'measurement failed:' in line:
            forced.append(line)
    forced.scheduler_tail()
    forced.tail('forced failure')

    stale = CensusRehearsal(args, directory / 'stale')
    planted = stale.results / 'derived/pair-1/previous-try.safetensors'
    # Plant the old file at the measurement read, after the job's own start-of-try cleanup.
    wrapper(stale.directory / 'compute-bin/python3', stale.compute,
            'if [ "${1:-}" = ./measure.py ] && [ $# = 1 ] && [ "${AUDIT_PAIR:-}" = 1 ]; then\n'
            '    mkdir -p ' + shlex.quote(str(planted.parent)) + '\n'
            '    printf "previous try\\n" > ' + shlex.quote(str(planted)) + '\n'
            '    touch -d @1 ' + shlex.quote(str(planted)) + '\nfi\n')
    stale.checked()
    rows = stale.rows()
    log = Path(rows[1]['log']).read_text()
    stale.expect(rows[1]['status'] == 'failed' and rows[1]['exit'] != 0, 'stale file did not fail the job')
    joined = ''.join(line.strip() for line in log.splitlines())
    stale.expect('stale measurement input refused:' in log and str(planted) in joined,
                 'stale refusal did not name the input')
    stale.expect(all(row['status'] == 'cancelled-invalid-dependency' for row in rows[2:]), 'stale failure left the chain')
    for line in log.splitlines():
        if 'stale measurement input refused' in line:
            stale.append(line)
    stale.append('  the refusal names the planted file: derived/pair-1/' + planted.name)
    stale.scheduler_tail()
    stale.tail('stale input')

    guard = CensusRehearsal(args, directory / 'guard')
    guard.queued()
    old = (guard.round / 'BUILD-STAMP.txt').read_text().strip()
    result = guard.call(['./round.sh', '--only', '40-submit.sh'], guard.round)
    guard.expect(result != 0 and len(guard.rows()) == 6 and 'already submitted' in guard.log.read_text(),
                 'same build was not refused')
    guard.append('same build refused: exit {}; scheduler rows still {}'.format(result, len(guard.rows())))
    guard.changed(lambda folder: (folder / 'login.py').write_text((folder / 'login.py').read_text() + "\nprint('rebuilt')\n"))
    guard.expect(guard.run() == 0 and len(guard.rows()) == 12, 'rebuilt bundle was not allowed')
    new = (guard.round / 'BUILD-STAMP.txt').read_text().strip()
    state = (guard.results / 'state/round-2-submissions').read_text()
    guard.expect(new != old and old in state and new in state, 'build history was lost')
    guard.append('new build allowed: {}...; both stamps kept'.format(new[:16]))
    guard.tail('build stamp same/new')

    pinned = CensusRehearsal(args, directory / 'pinned')
    pinned.queued()
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
        pinned.append('job {} pinned hash matches: {}...'.format(row['job'], sha[:16]))
    pinned.tail('pinned snapshot')

    broken = CensusRehearsal(args, directory / 'self-test')
    broken.broken()
    result = broken.run()
    text = broken.log.read_text()
    broken.expect(result == 31 and 'VERDICT round 2 FAIL' in text and not broken.rows(), 'self-test missed the broken step')
    observed = next(line for line in text.splitlines() if line.startswith('VERDICT round 2 '))
    broken.append('self-test observed: ' + observed + '; exit ' + str(result) + '; scheduler rows 0')
    broken.append('VERDICT self-test FAIL')
    broken.tail('self-test FAIL')
    elapsed = time.monotonic() - started
    print('Rehearsal elapsed: {:.2f} minutes'.format(elapsed / 60))
    print('All seven observed outcomes matched the requested cases.')
    print((clean.directory / 'builder.log').read_text(), end='')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', help='keep logs in this fresh folder within the repository')
    args = parser.parse_args()
    scratch = ROOT / '.tmp'
    scratch.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='round2-', dir=str(scratch)) as temporary:
        directory = Path(args.out).resolve() if args.out else Path(temporary)
        if not str(directory).startswith(str(ROOT) + '/'):
            raise ValueError('rehearsal output must stay within the repository')
        if args.out:
            directory.mkdir(parents=True)
        kit = fixture_kit(directory / 'kit')
        compute = str(CLUSTER_PYTHON) if CLUSTER_PYTHON.exists() else sys.executable
        settings = argparse.Namespace(login_python=sys.executable, compute_python=compute,
                                      dry_run=True, base='synthetic/stub', kit=str(kit))
        suite(settings, directory)


if __name__ == '__main__':
    main()
