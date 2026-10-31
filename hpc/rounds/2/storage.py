# storage.py -- Check the work quota, filesystem space and project budget.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  use exact bytes for acceptance and GB for the display.
# Modified: SDE 2026-10-14  check the census budget and display GB.
# Modified: SDE 2026-10-29  the quota method comes from the systems table; the size line lives in work.
# Modified: SDE 2026-10-31  lfs quota without show_storage, and free space when the quota table is unreadable.
import json
import os
from pathlib import Path
import shutil
import subprocess


def quota_numbers(text):
    """Read the block quota columns, including wrapped filesystem names."""
    for line in text.splitlines():
        fields = line.split()
        if fields and fields[0].startswith('/'):
            fields = fields[1:]
        if len(fields) >= 3 and all(value.rstrip('*').isdigit() for value in fields[:3]):
            used, soft, hard = [int(value.rstrip('*')) * 1024 for value in fields[:3]]
            ceiling = min(value for value in (soft, hard) if value) if soft or hard else None
            if ceiling is None:
                raise ValueError('quota has no finite limit')
            return used, ceiling
    raise ValueError('cannot read the work quota table')


def main():
    """Fail closed if either shared capacity or our own budget is exhausted."""
    work = os.environ['WORKDIR']
    project = Path(work) / 'model-audit'
    need = json.loads(Path('needs.json').read_text())['bytes']
    own = int(subprocess.check_output(['du', '-sk', str(project)], universal_newlines=True).split()[0]) * 1024
    # lfs: show_storage and the Lustre quota; show_storage: then free space;
    # statvfs: free space alone, for systems with neither tool.
    method = os.environ.get('AUDIT_QUOTA')
    if not method:
        method = 'show_storage' if os.environ.get('HPC_SYSTEM') == 'raider' else 'lfs'
    if os.environ.get('AUDIT_REHEARSAL') == '1':
        used, limit, free = 0, 3 * 1024 ** 4, 3 * 1024 ** 4
    elif method == 'statvfs':
        info = os.statvfs(work)
        free = info.f_bavail * info.f_frsize
        used, limit = 0, free
    elif method in ('show_storage', 'show_usage'):
        # The Navy centers print show_storage, the Army and Air Force centers show_usage; either is
        # a reading for the log, and a system with neither still gives its free space.
        tool = next((name for name in ('show_storage', 'show_usage') if shutil.which(name)), None)
        if tool:
            subprocess.call([tool, '-h'])
        else:
            print('storage tool absent on this system; free space alone')
        info = os.statvfs(work)
        free = info.f_bavail * info.f_frsize
        used, limit = 0, free
    else:
        # Lustre quota; show_storage is a reading for the log where the center has it (Raider has not).
        if shutil.which('show_storage'):
            subprocess.call(['show_storage', '-h'])
        else:
            print('show_storage absent on this system; lfs quota alone')
        info = os.statvfs(work)
        free = info.f_bavail * info.f_frsize
        try:
            text = subprocess.check_output(['lfs', 'quota', '-u', os.environ['USER'], work], universal_newlines=True)
            used, limit = quota_numbers(text)
        except (subprocess.CalledProcessError, OSError, ValueError) as error:
            print('lfs quota unreadable here ({}); free space alone'.format(error))
            used, limit = 0, free
    print('Project: {:.1f} GB; requested: {:.1f} GB'.format(own / 1024 ** 3, need / 1024 ** 3))
    print('Work quota remaining: {:.1f} GB; filesystem free: {:.1f} GB'.format((limit - used) / 1024 ** 3, free / 1024 ** 3))
    if own + need > 8 * 1024 ** 4 or min(limit - used, free) < need:
        raise SystemExit('insufficient work space for the declared round')
    # Home can be over quota; the poll fragment reads this line from work.
    cache = project / 'space.tsv'
    cache.write_text('{}\t{}\n'.format(project, own // 1024))


if __name__ == '__main__':
    main()
