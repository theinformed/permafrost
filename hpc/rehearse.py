# rehearse.py -- Prepare a fenced local scheduler and run the bundled round.
# Created by LT Sean Egan, PhD 2026-10-13
# Modified: SDE 2026-10-13  resolve the interpreters to absolute paths before linking them.
# Modified: SDE 2026-10-13  show the last thirty lines and both chain outcomes.
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
NEEDS = 'space=160G hours=0 subproject=NRLMR57635502 queue=background for=4h'


def rehearse(args):
    """Run in a fresh folder, never inside somebody else's live work."""
    directory = Path(args.directory).resolve()
    if directory.exists() and any(directory.iterdir()):
        raise ValueError('rehearsal folder must be empty')
    directory.mkdir(parents=True, exist_ok=True)
    login = shutil.which(args.login_python)
    compute = shutil.which(args.compute_python)
    # A relative interpreter path would make a dangling link once it sits in the fake bin folder.
    login = os.path.abspath(login) if login else login
    compute = os.path.abspath(compute) if compute else compute
    if not login or not compute:
        raise ValueError('both interpreter paths must exist')
    if not args.dry_run:
        version = subprocess.check_output([login, '--version'], universal_newlines=True, stderr=subprocess.STDOUT)
        if not version.startswith('Python 3.6.'):
            raise ValueError('the full rehearsal needs --login-python pointing to Python 3.6')
    home, work, binary = [directory / name for name in ('home', 'work', 'bin')]
    for path in (home / 'bin', work, binary, directory / 'outbox'):
        path.mkdir(parents=True, exist_ok=True)
    compute_bin = directory / 'compute-bin'
    compute_bin.mkdir()
    (compute_bin / 'python3').symlink_to(compute)
    for name in ('sbatch', 'hpc'):
        target = binary / name
        shutil.copyfile(str(ROOT / 'hpc/fakes' / name), str(target))
        target.chmod(0o755)
    (binary / 'python3').symlink_to(login)
    # compute_python switches to the compute interpreter before loading packages.
    environment = dict(os.environ, HOME=str(home), WORKDIR=str(work), AUDIT_FAKE_ROOT=str(directory),
        PATH=str(binary) + ':' + str(home / 'bin') + ':' + os.environ['PATH'],
        AUDIT_REHEARSAL='1', AUDIT_STUB='1' if args.dry_run else '0', AUDIT_FAIL_SECOND='1' if args.fail_second else '0',
        AUDIT_BASE=args.base, AUDIT_NAME='rehearsal-base', AUDIT_COMPUTE_BIN=str(compute_bin), HPC_SYSTEM='fake',
        CUDA_VISIBLE_DEVICES='', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1',
        PYTHONDONTWRITEBYTECODE='1')
    bundle = directory / 'bundle'
    subprocess.check_call([login, str(ROOT / 'hpc/bundle.py'), 'build', '--needs', NEEDS, '--kit', args.kit, '--out', str(bundle)],
                          env=environment, stdout=subprocess.DEVNULL)
    log = directory / 'rehearsal.log'
    with log.open('w') as stream:
        result = subprocess.call([str(bundle / 'model-audit-round.sh'), '1'], env=environment, stdout=stream, stderr=subprocess.STDOUT)
    rows = [json.loads(line) for line in (directory / 'submissions.jsonl').read_text().splitlines()]
    expected = ['finished', 'rejected'] if args.fail_second else ['finished', 'finished']
    if [row['status'] for row in rows] != expected or bool(result) != args.fail_second:
        raise ValueError('rehearsal outcome differs from the expected chain; see ' + str(log))
    second = rows[1]['arguments']
    if '--dependency=afterok:1001' not in second or '--kill-on-invalid-dep=yes' not in second:
        raise ValueError('the projection was not protected by the first job')
    drops = list((directory / 'outbox').glob('*'))
    if args.fail_second and not any('event: failed' in path.read_text() for path in drops):
        raise ValueError('the forced failure produced no failed drop')
    with log.open('a') as stream:
        stream.write('Rehearsal: {}\n'.format('forced second submission failed as expected' if args.fail_second else 'both jobs completed'))
        stream.write('Dependency: afterok:1001; kill-on-invalid-dep=yes\n')
        stream.write('Drops: {}\n'.format(len(drops)))
        stream.write('VERDICT rehearsal OK\n')
    print('\n'.join(log.read_text().splitlines()[-30:]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('directory')
    parser.add_argument('--base', default='HuggingFaceTB/SmolLM2-135M-Instruct')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--fail-second', action='store_true')
    parser.add_argument('--kit', default='/root/work/hpc-kit-wt')
    parser.add_argument('--login-python', default='python3')
    parser.add_argument('--compute-python', default='python3')
    arguments = parser.parse_args()
    try:
        rehearse(arguments)
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        parser.exit(1, str(error) + '\n')
