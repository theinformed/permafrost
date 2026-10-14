# measure.py -- Reject old round inputs before the checkpoint comparison reads them.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  check file ages and shared originals on every measurement read.
# Modified: SDE 2026-10-14  date declared comparison inputs, not retry scratch.
import hashlib
import json
import os
from pathlib import Path
import runpy
import sys


def checksum(path):
    """Hash one file at a time, without loading a weight shard into memory."""
    value = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            value.update(block)
    return value.hexdigest()


def fresh(paths, started):
    """A previous run does not get a fresh date just because we found its files."""
    for path in paths:
        if path.stat().st_mtime < started:
            raise ValueError('stale measurement input refused: ' + str(path))


def round_inputs():
    """Date only the derived checkpoint and report this comparison consumes."""
    derived = Path(os.environ['AUDIT_DERIVED'])
    report = Path(os.environ['AUDIT_MEASUREMENT'])
    paths = [path for path in sorted(derived.rglob('*')) if path.is_file()]
    if report.is_file():
        paths.append(report)
    return paths


def verify_original():
    """Shared originals may be old; they must still match the download receipt."""
    original = Path(os.environ['AUDIT_ORIGINAL'])
    record = json.loads((original / 'download-manifest.json').read_text())
    if record['base'] != os.environ['AUDIT_BASE'] or not record['files']:
        raise ValueError('original receipt belongs to a different or empty snapshot')
    for row in record['files']:
        path = original / row['path']
        if Path(row['path']).name != row['path'] or path.is_symlink():
            raise ValueError('unexpected original path: ' + str(path))
        if path.stat().st_size != row['size'] or checksum(path) != row['sha256']:
            raise ValueError('original checksum differs: ' + str(path))


def measurement(arguments, runner):
    """Let a failed comparison reach the shell before it writes a done marker."""
    fresh(round_inputs(), float(os.environ['AUDIT_JOB_STARTED']))
    verify_original()
    result = runner(arguments)
    if result:
        raise SystemExit(result)
    return result


def seed_original():
    """The dry run uses a few bytes and the same checksum read as a real job."""
    original = Path(os.environ['AUDIT_ORIGINAL'])
    original.mkdir(parents=True, exist_ok=True)
    path = original / 'stub.txt'
    path.write_text('a small original checkpoint\n')
    record = {'base': os.environ['AUDIT_BASE'], 'revision': 'stub', 'files': [
        {'path': path.name, 'size': path.stat().st_size, 'sha256': checksum(path)}]}
    (original / 'download-manifest.json').write_text(json.dumps(record) + '\n')


def main():
    """Use the same refusal and exit path for the dry run and real comparison."""
    stub = os.environ.get('AUDIT_STUB') == '1' and os.environ.get('AUDIT_REHEARSAL') == '1'
    if sys.argv[1:] == ['--seed-original'] and stub:
        seed_original()
        return
    fresh(round_inputs(), float(os.environ['AUDIT_JOB_STARTED']))
    verify_original()
    if stub:
        derived = Path(os.environ['AUDIT_DERIVED'])
        derived.mkdir(parents=True, exist_ok=True)
        (derived / 'stub.txt').write_text('a small projected checkpoint\n')

        def compare(arguments):
            """A forced comparison fault follows the real job's nonzero exit path."""
            if os.environ.get('AUDIT_FAIL_MEASUREMENT') == '1':
                print('measurement failed: forced comparison fault', flush=True)
                return 23
            report = Path(os.environ['AUDIT_MEASUREMENT'])
            report.parent.mkdir(parents=True, exist_ok=True)
            report.write_text('{"status": "complete"}\n')
            print('measurement passed: ' + str(report), flush=True)
            return 0

        measurement([], compare)
    else:
        from audit import weights_cli
        compare = weights_cli.main
        weights_cli.main = lambda arguments=None: measurement(arguments, compare)
        runpy.run_path('project.py', run_name='__main__')
    fresh([Path(os.environ['AUDIT_MEASUREMENT'])], float(os.environ['AUDIT_JOB_STARTED']))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError) as error:
        raise SystemExit(str(error))
