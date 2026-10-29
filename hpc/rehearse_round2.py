# rehearse_round2.py -- Exercise a census batch with artificial tensors on a fake scheduler.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  read pass, cancellation and broken-step outcomes from logs.
# Modified: SDE 2026-10-15  real tensor names, the tested pins, lineage, stale, stamp and pinned cases.
# Modified: SDE 2026-10-15  check that no printed line runs past 100 columns.
# Modified: SDE 2026-10-29  any batch and system: parallel compares, the sweep, PBS and the image.
import argparse
import ast
import hashlib
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

BUNDLE = 'model-audit-census.sh'
NAMES = ROOT / 'tests/fixtures/round2'
MANIFEST = ROOT / 'data/batches/round-2-batch-1.json'
SYSTEMS = json.loads((ROOT / 'hpc/systems.json').read_text())
NEEDS = 'space=1T hours=0 subproject={} queue=background for=4h'.format(SYSTEMS['nautilus']['subproject'])
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
    (directory / 'hpc-report.sh').write_text("""#!/bin/bash
# hpc-report.sh -- Write local rehearsal cards without a network.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  retain the job description and its exit event.
hpc_job_start() {
    mkdir -p "$HOME/.hpc/jobs"
    printf '{"v":1,"job":"%s","description":"%s","project":"model-audit"}\\n' "$HPC_JOB_ID" "$1" > "$HOME/.hpc/jobs/$HPC_JOB_ID.json"
}
hpc_job_finish() { echo "card event: finished; $*"; }
hpc_job_fail() { echo "card event: failed; $*"; }
""")
    return directory


def fixture_image(directory):
    """A stand-in image file and the record run-check.sh reads inside a real image."""
    directory.mkdir(parents=True, exist_ok=True)
    image = directory / 'permafrost-rehearsal.sif'
    image.write_text('rehearsal stand-in for the round image\n')
    requirements = ROOT / 'hpc/rounds/2/compute-requirements.txt'
    (directory / 'permafrost-image.txt').write_text(
        'image: permafrost\nversion: rehearsal\nbuilt: rehearsal\nrequirements sha256: {}\n'.format(
            hashlib.sha256(requirements.read_bytes()).hexdigest()))
    return image, hashlib.sha256(image.read_bytes()).hexdigest()


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


def plain_id(job):
    """A PBS id carries its server after a dot; cards and drops use the number alone."""
    return job.split('.', 1)[0]


def dependency(row):
    """The dependency of a recorded submission in either scheduler's spelling, or None."""
    arguments = row['arguments']
    for index, argument in enumerate(arguments):
        if argument.startswith('--dependency='):
            return argument.split('=', 1)[1]
        if argument == '-W' and arguments[index + 1].startswith('depend='):
            return arguments[index + 1].split('=', 1)[1]
    return None


def owned(row):
    """Slurm carries the owner in --comment; PBS in its variable list and the job name."""
    arguments = row['arguments']
    if row.get('scheduler') == 'pbs':
        variables = arguments[arguments.index('-v') + 1]
        name = arguments[arguments.index('-N') + 1]
        return variables.startswith('HPC_PROJECT=model-audit,') and name.startswith('model-audit-census-')
    return '--comment=project=model-audit' in arguments


class CensusRehearsal(Rehearsal):
    """Use round 1's fake scheduler and drop transport, without running round 1."""

    def __init__(self, args, directory):
        self.manifest = Path(getattr(args, 'manifest', None) or MANIFEST)
        self.batch = json.loads(self.manifest.read_text())
        self.number = self.batch['round']
        self.count = len(self.batch['pairs'])
        self.system = getattr(args, 'system', None) or 'nautilus'
        self.image = getattr(args, 'image', False) or SYSTEMS[self.system]['image'] == 'required'
        super().__init__(args, directory)
        wrapper(self.binary / 'python3', self.login)
        self.compute = os.path.abspath(args.compute_python)
        wrapper(self.directory / 'compute-bin/python3', self.compute)
        for name in ('qsub', 'apptainer'):
            target = self.binary / name
            shutil.copyfile(str(ROOT / 'hpc/fakes' / name), str(target))
            target.chmod(0o755)
        self.environment.update(AUDIT_STUB_NAMES=str(NAMES), AUDIT_LEAN_ELEMENTS='32',
                                FAKE_IMAGE_RECORD=str(self.directory / 'images/permafrost-image.txt'))

    def build(self, rounds=None, manifest=None, check=True):
        self.round = self.work / 'model-audit/rounds' / str(self.number) / 'scripts'
        self.results = self.work / 'model-audit/rounds' / str(self.number)
        entry = SYSTEMS[self.system]
        needs = 'space=1T hours=0 subproject={} queue=background for=4h'.format(entry['subproject'])
        command = [self.login, str(ROOT / 'hpc/rounds/2/bundle.py'), 'build', '--round', str(self.number),
                   '--system', self.system, '--needs', needs, '--kit', self.args.kit, '--out', str(self.bundle),
                   '--manifest', str(manifest or self.manifest)]
        if rounds is not None:
            command += ['--rounds', str(rounds)]
        if self.image:
            image, sha = fixture_image(self.directory / 'images')
            command += ['--image', str(image), '--image-sha256', sha]
        result = captured(command, env=self.environment)
        (self.directory / 'builder.log').write_text(result.stdout)
        if check and result.returncode:
            raise ValueError('bundle build failed: ' + result.stdout)
        return result

    def run(self, *extra):
        return self.call([str(self.bundle / BUNDLE), str(self.number)] + list(extra))

    def card(self, row):
        return json.loads((self.home / '.hpc/jobs' / (plain_id(row['job']) + '.json')).read_text())

    def shape(self, rows):
        """One download, one compare per pair after the download alone, then the sweep after all."""
        self.expect(len(rows) == self.count + 2, 'expected one transfer, {} pieces and the sweep'.format(self.count))
        download, compares, sweep = rows[0], rows[1:-1], rows[-1]
        self.expect(dependency(download) is None, 'the download has a dependency')
        self.expect(download['arguments'][-1].endswith('/jobs/download.sh'), 'the first job is not the download')
        for row in compares:
            self.expect(row['arguments'][-1].endswith('/jobs/project.sh'), 'a piece is not a compare')
            self.expect(dependency(row) == 'afterok:' + download['job'], 'a compare does not wait on the download alone')
            if row.get('scheduler') != 'pbs':
                self.expect('--kill-on-invalid-dep=yes' in row['arguments'], 'a compare lacks the kill instruction')
        self.expect(sweep['arguments'][-1].endswith('/jobs/sweep.sh'), 'the last job is not the sweep')
        self.expect(dependency(sweep) == 'afterany:' + ':'.join(row['job'] for row in compares),
                    'the sweep does not wait on every compare')
        self.expect([row['environment']['AUDIT_PAIR'] for row in compares] ==
                    [str(number) for number in range(1, self.count + 1)], 'compare pieces out of order')
        for row in rows:
            pinned = row['environment']['AUDIT_PINNED_ROUND']
            self.expect(pinned.startswith(str(self.results / 'submissions')), 'job lacks pinned snapshot')
            self.expect(owned(row), 'job lacks the owner tag')
        return rows

    def queued(self):
        """Submit with the scheduler holding everything, then check the parallel shape."""
        self.environment['AUDIT_FAKE_DEFER'] = '1'
        self.expect(self.run() == 0, 'round {} submission failed'.format(self.number))
        rows = self.rows()
        self.expect(all(row['status'] == 'queued' for row in rows), 'a job ran while the queue was held')
        return self.shape(rows)

    def checked(self):
        self.queued()
        return self.call([str(self.binary / 'sbatch'), '--run-pending'])

    def sweep(self):
        return json.loads((self.results / 'measurements/sweep.json').read_text())

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

    def failed_pair_kept(self, rows):
        """Pair 1 failed: its siblings finish, the sweep runs and keeps pair 1's original."""
        self.expect(all(row['status'] == 'finished' for row in rows[2:]), 'a sibling or the sweep did not finish')
        record = self.sweep()
        kept = [group for group in record['kept'] if 1 in group['pairs']]
        self.expect(len(kept) == 1 and 1 in kept[0]['missing'] and Path(kept[0]['path']).is_dir(),
                    "the sweep did not keep the failed pair's original")
        others = [group for group in record['deleted'] if 1 not in group['pairs']]
        self.expect(all(not Path(group['path']).exists() for group in others), 'a finished original survived')
        self.append('sweep kept {} for pair 1; deleted {}; kept {}'.format(
            kept[0]['hub_id'], len(record['deleted']), len(record['kept'])))


def expected_writers(manifest, number):
    """Residual writers counted from the published names of the pair's original."""
    sys.path.insert(0, str(ROOT))
    sys.path.insert(0, str(ROOT / 'hpc/rounds/2'))
    from audit.weights import recipe_table, tensor_kind
    from measure import census_kinds
    batch = json.loads(Path(manifest).read_text())
    model = batch['pairs'][number - 1]['original']
    names = json.loads((NAMES / (model['revision'][:12] + '.json')).read_text())['tensors']
    table = census_kinds(recipe_table())
    counts = {}
    for name in names:
        kind = tensor_kind(name, table)
        if kind in WRITERS:
            counts[kind] = counts.get(kind, 0) + 1
    return model['hub_id'], counts


def planted_manifest(directory, manifest=MANIFEST):
    """A Qwen-based copy slipped into the batch; the screen has to stop it."""
    record = json.loads(Path(manifest).read_text())
    copy = record['pairs'][-1]['modified']
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
    count = clean.count
    clean.append('compute interpreter: ' + clean.compute)
    clean.append('system: {}; scheduler {}; image {}; round {}; {} pairs'.format(
        clean.system, SYSTEMS[clean.system]['scheduler'], 'yes' if clean.image else 'no', clean.number, count))
    clean.expect(clean.checked() == 0, 'round {} jobs did not complete'.format(clean.number))
    rows = clean.rows()
    clean.expect(all(row['status'] == 'finished' for row in rows), 'a clean piece failed')
    for number in range(1, count + 1):
        measurement = clean.results / 'measurements' / ('pair-' + str(number))
        receipt = json.loads((measurement / 'receipt.json').read_text())
        clean.expect(all(not Path(path).exists() for path in receipt['deleted_checkpoints']), 'weights survived compare')
        clean.expect((measurement / 'metadata.json').is_file() and (measurement / 'card.md').is_file(), 'reports are missing')
        card = clean.card(rows[number])
        clean.expect(card['snapshot']['sha256'] == rows[number]['started_snapshot_sha256'], 'card snapshot differs')
        report = json.loads((measurement / 'weights.json').read_text())
        model, wanted = expected_writers(clean.manifest, number)
        found = {}
        for name in report['summary']['changed_set']:
            kind = report['tensors'][name]['kind']
            found[kind] = found.get(kind, 0) + 1
        lean = sum(1 for row in report['tensors'].values() if row.get('lean'))
        clean.expect(found == wanted and all(wanted.values()), 'changed writers differ from the real names')
        clean.expect(not report['original_only'] and not report['modified_only'], 'tensor names differ across a pair')
        clean.append('pair {} {}: {} tensors; changed {}; lean {}; {}{}'.format(
            number, model.split('/')[1], len(report['tensors']), json.dumps(found, sort_keys=True), lean,
            report['summary']['assessment'], '; shared original' if receipt['shared_original'] else ''))
    record = clean.sweep()
    clean.expect(not record['kept'] and all(not Path(group['path']).exists() for group in record['deleted']),
                 'the sweep left an original whose pairs all reported')
    clean.append('sweep: {} originals deleted after {} compares; none kept'.format(len(record['deleted']), count))
    clean.scheduler_tail()
    wide_count, wide = clean.wide_lines()
    clean.expect(not wide, 'printed lines over 100 columns: ' + '; '.join(wide[:5]))
    clean.append('line width: {} logs, longest printed line within 100 columns'.format(wide_count))
    clean.append('owner tag: all {} jobs carry it'.format(len(rows)))
    clean.tail('round-{} pass'.format(clean.number), 14 + count)

    screen = CensusRehearsal(args, directory / 'lineage')
    planted = planted_manifest(screen.directory, screen.manifest)
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
    forced.expect(rows[1]['exit'] == 23 and rows[1]['status'] == 'failed', 'the forced fault did not fail pair 1')
    forced.expect(not (forced.results / 'pieces/pair-1/state/compare.done').exists(), 'failed compare wrote a done marker')
    for line in Path(rows[1]['log']).read_text().splitlines():
        if 'measurement failed:' in line:
            forced.append(line)
    forced.failed_pair_kept(rows)
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
    for line in log.splitlines():
        if 'stale measurement input refused' in line:
            stale.append(line)
    stale.append('  the refusal names the planted file: derived/pair-1/' + planted.name)
    stale.failed_pair_kept(rows)
    stale.scheduler_tail()
    stale.tail('stale input')

    guard = CensusRehearsal(args, directory / 'guard')
    guard.queued()
    jobs = count + 2
    old = (guard.round / 'BUILD-STAMP.txt').read_text().strip()
    result = guard.call(['./round.sh', '--only', '40-submit.sh'], guard.round)
    guard.expect(result != 0 and len(guard.rows()) == jobs and 'already submitted' in guard.log.read_text(),
                 'same build was not refused')
    guard.append('same build refused: exit {}; scheduler rows still {}'.format(result, len(guard.rows())))
    guard.changed(lambda folder: (folder / 'login.py').write_text((folder / 'login.py').read_text() + "\nprint('rebuilt')\n"))
    guard.expect(guard.run() == 0 and len(guard.rows()) == 2 * jobs, 'rebuilt bundle was not allowed')
    guard.shape(guard.rows()[jobs:])
    new = (guard.round / 'BUILD-STAMP.txt').read_text().strip()
    state = (guard.results / 'state/round-{}-submissions'.format(guard.number)).read_text()
    guard.expect(new != old and old in state and new in state, 'build history was lost')
    guard.append('new build allowed: {}...; both stamps kept'.format(new[:16]))
    guard.tail('build stamp same/new')

    pinned = CensusRehearsal(args, directory / 'pinned')
    pinned.queued()
    shutil.rmtree(str(pinned.round))
    pinned.round.mkdir(parents=True)
    (pinned.round / 'env.sh').write_text("echo 'overwritten opened copy ran'; exit 99\n")
    result = pinned.call([str(pinned.binary / 'sbatch'), '--run-pending'])
    rows = pinned.rows()
    pinned.expect(result == 0 and all(row['status'] == 'finished' for row in rows), 'pinned jobs failed after overwrite')
    for row in rows:
        card = pinned.card(row)
        sha = row['started_snapshot_sha256']
        pinned.expect(sha == row['snapshot']['sha256'] == card['snapshot']['sha256'], 'pinned hash differs')
        drop = (pinned.directory / 'outbox' / (plain_id(row['job']) + '-drop.txt')).read_text()
        pinned.expect(sha in drop, 'snapshot hash was not delivered')
        pinned.append('job {} pinned hash matches: {}...'.format(row['job'], sha[:16]))
    pinned.tail('pinned snapshot', 4 + count)

    broken = CensusRehearsal(args, directory / 'self-test')
    broken.broken()
    result = broken.run()
    text = broken.log.read_text()
    verdict = 'VERDICT round {} '.format(broken.number)
    broken.expect(result == 31 and verdict + 'FAIL' in text and not broken.rows(), 'self-test missed the broken step')
    observed = next(line for line in text.splitlines() if line.startswith(verdict))
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
    parser.add_argument('--manifest', default=str(MANIFEST), help='the batch to rehearse')
    parser.add_argument('--system', default='nautilus', choices=sorted(SYSTEMS))
    parser.add_argument('--image', action='store_true', help='run the compute steps through the image')
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
                                      dry_run=True, base='synthetic/stub', kit=str(kit),
                                      manifest=args.manifest, system=args.system, image=args.image)
        suite(settings, directory)


if __name__ == '__main__':
    main()
