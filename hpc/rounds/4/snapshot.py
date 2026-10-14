# snapshot.py -- Pin the submitted scripts and attach their hash to the job card.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  pin the calibration scripts and job card.
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tarfile
import uuid


def digest(path):
    """Read in blocks; the tar is small, but there is no prize for copying it."""
    value = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            value.update(block)
    return value.hexdigest()


def plan():
    """Keep at most 64 script copies until the round archive has been read back."""
    source = Path.cwd()
    files = [path for path in source.rglob('*') if path.is_file()
             and 'logs' not in path.relative_to(source).parts and path.suffix != '.log']
    if any(path.is_symlink() for path in source.rglob('*')):
        raise ValueError('round snapshot refuses symbolic links')
    size = sum(path.stat().st_size for path in files)
    if len(files) > 500 or size > 8 * 1024 ** 2:
        raise ValueError('round snapshot exceeds 500 files or 8 MB')
    saved = Path(os.environ['AUDIT_WORK']) / 'submissions'
    archives = list(saved.glob('*/round.tar'))
    if len(archives) >= 64 or sum(path.stat().st_size for path in archives) + size > 512 * 1024 ** 2:
        raise ValueError('round submissions exceed 64 copies or the 512 MB tar budget')
    return files, size


def create():
    """Save one checked copy per submission, outside the interactive home folder."""
    source = Path.cwd()
    plan()
    subprocess.check_call(['sha256sum', '-c', 'SHA256SUMS'], stdout=subprocess.DEVNULL)
    name = datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%S.%fZ-') + uuid.uuid4().hex[:8]
    saved = Path(os.environ['AUDIT_WORK']) / 'submissions' / name
    saved.mkdir(parents=True)
    archive = saved / 'round.tar'
    # Logs change while submit runs. They are records, not queued job inputs.
    with tarfile.open(str(archive), 'w') as stream:
        for path in sorted(source.iterdir()):
            if path.name == 'logs' or path.name.endswith('.log'):
                continue
            stream.add(str(path), arcname=path.name)
    saved_bytes = sum(path.stat().st_size for path in saved.parent.glob('*/round.tar'))
    if saved_bytes > 512 * 1024 ** 2:
        archive.unlink()
        saved.rmdir()
        raise ValueError('round submissions exceed the 512 MB tar budget')
    sha = digest(archive)
    (saved / 'snapshot.sha256').write_text(sha + '  round.tar\n')
    pinned = saved / 'round'
    pinned.mkdir()
    with tarfile.open(str(archive)) as stream:
        stream.extractall(str(pinned))
    record = {'sha256': sha, 'archive': str(archive), 'directory': str(pinned),
              'build_stamp': (pinned / 'BUILD-STAMP.txt').read_text().strip()}
    (saved / 'snapshot.json').write_text(json.dumps(record, indent=2) + '\n')
    print(pinned)


def metadata():
    """Read the metadata belonging to this job's pinned directory."""
    pinned = Path(os.environ['AUDIT_PINNED_ROUND']).resolve()
    record = json.loads((pinned.parent / 'snapshot.json').read_text())
    if record['directory'] != str(pinned):
        raise ValueError('snapshot directory differs from its receipt')
    return record


def verify():
    """Refuse changed scripts as well as a changed tar."""
    record = metadata()
    if digest(Path(record['archive'])) != record['sha256']:
        raise ValueError('snapshot tar checksum differs: ' + record['archive'])
    pinned = Path(record['directory'])
    with tarfile.open(record['archive']) as stream:
        for member in stream.getmembers():
            if member.isfile():
                path = pinned / member.name
                if path.is_symlink() or digest(path) != hashlib.sha256(stream.extractfile(member).read()).hexdigest():
                    raise ValueError('pinned file checksum differs: ' + str(path))
    subprocess.check_call(['sha256sum', '-c', 'SHA256SUMS'], cwd=str(pinned), stdout=subprocess.DEVNULL)
    print('snapshot verified: ' + record['sha256'])


def card(path):
    """Keep the reporting helper's fields and add the submitted copy's receipt."""
    record = json.loads(path.read_text())
    record['snapshot'] = metadata()
    record['build_stamp'] = record['snapshot']['build_stamp']
    record['job_started_epoch'] = os.environ['AUDIT_JOB_STARTED']
    path.write_text(json.dumps(record, indent=2) + '\n')


if __name__ == '__main__':
    try:
        if sys.argv[1] == 'plan':
            files, size = plan()
            print('snapshot plan: {} files, {:.1f} MB; retained through archive read-back'.format(len(files), size / 1024 ** 2))
        elif sys.argv[1] == 'create':
            create()
        elif sys.argv[1] == 'verify':
            verify()
        elif sys.argv[1] == 'card':
            card(Path(sys.argv[2]))
        else:
            raise ValueError('unknown snapshot operation')
    except (ValueError, OSError) as error:
        raise SystemExit(str(error))
