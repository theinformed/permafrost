# census.py -- Name pinned batch inputs and verify them before every comparison.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  separate download inputs from each try's scratch.
# Modified: SDE 2026-10-15  a login-side check of the download records that reads sizes, not weights.
# Modified: SDE 2026-10-29  any batch of 1 to 24 pairs; shared originals and the sweep that clears them.
import hashlib
import json
import os
from pathlib import Path
import shlex
import shutil
import stat
import sys

from say import fold


def batch():
    return json.loads(Path('batch.json').read_text())


LIMIT = 24


def count():
    """The batch's pair count, which every piece number and job list follows."""
    pairs = batch()['pairs']
    if not 1 <= len(pairs) <= LIMIT:
        raise ValueError('a census batch holds 1 to {} pairs, not {}'.format(LIMIT, len(pairs)))
    return len(pairs)


def round_number():
    value = batch()['round']
    if not isinstance(value, int) or isinstance(value, bool) or value < 1:
        raise ValueError('batch.json names no round number')
    return value


def pair(number):
    total = count()
    if not 1 <= number <= total:
        raise ValueError('census piece must be 1 through {}, not {}'.format(total, number))
    return batch()['pairs'][number - 1]


def paths(number):
    row = pair(number)
    base = row['original']
    key = hashlib.sha256((base['hub_id'] + '@' + base['revision']).encode()).hexdigest()
    original = Path(os.environ['WORKDIR']) / 'model-audit/originals' / key
    modified = Path(os.environ['AUDIT_WORK']) / 'inputs' / ('pair-' + str(number))
    return original, modified


def originals():
    """Each original folder with its pinned identity and the pairs that read it, in pair order."""
    groups = {}
    for number in range(1, count() + 1):
        model = pair(number)['original']
        folder = str(paths(number)[0])
        group = groups.setdefault(folder, {'path': folder, 'hub_id': model['hub_id'],
                                           'revision': model['revision'], 'pairs': []})
        group['pairs'].append(number)
    return list(groups.values())


def shares_original(number):
    """True when another pair in the batch reads the same original folder."""
    return any(number in group['pairs'] and len(group['pairs']) > 1 for group in originals())


def reported(number):
    """A pair counts as done once its compare job wrote the record naming it."""
    path = Path(os.environ['AUDIT_WORK']) / 'measurements' / ('pair-' + str(number)) / 'receipt.json'
    try:
        return json.loads(path.read_text()).get('pair') == number
    except (OSError, ValueError):
        return False


def sweep():
    """Delete an original only when every pair that reads it has its reports; list the rest."""
    work = Path(os.environ['AUDIT_WORK'])
    root = Path(os.environ['WORKDIR']).resolve()
    record = {'deleted': [], 'kept': [], 'absent': []}
    for group in originals():
        path = Path(group['path'])
        missing = [number for number in group['pairs'] if not reported(number)]
        numbers = ' '.join(str(number) for number in group['pairs'])
        if missing:
            record['kept'].append(dict(group, missing=missing))
            print(fold('original kept: ' + group['hub_id'],
                       'pairs without a receipt: ' + ' '.join(str(number) for number in missing)))
        elif not path.exists():
            record['absent'].append(group)
            print(fold('original already gone: ' + group['hub_id'], 'pairs ' + numbers))
        else:
            if path.is_symlink() or not str(path.resolve()).startswith(str(root) + '/'):
                raise ValueError(fold('original path outside work:', str(path)))
            shutil.rmtree(str(path))
            record['deleted'].append(group)
            print(fold('original deleted: ' + group['hub_id'], 'pairs ' + numbers))
    target = work / 'measurements/sweep.json'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(record, indent=2) + '\n')
    print('sweep: {} deleted, {} kept, {} already gone'.format(
        len(record['deleted']), len(record['kept']), len(record['absent'])))
    return record


def token():
    """Only this regular file supplies credentials; ambient tokens are ignored."""
    path = Path(os.environ.get('AUDIT_TOKEN_FILE') or Path(os.environ['HOME']) / '.hpc/hf-token')
    if path.is_symlink() or not path.is_file() or stat.S_IMODE(path.stat().st_mode) != 0o600:
        raise ValueError(fold('hub token must be a regular mode-600 file:', str(path)))
    value = path.read_text().strip()
    if not value:
        raise ValueError('hub token file is empty')
    return value


def checksum(path):
    value = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            value.update(block)
    return value.hexdigest()


def verify(directory, model):
    """A locally saved download record must still agree with the pinned hub identity."""
    record = json.loads((directory / 'download-manifest.json').read_text())
    if record['base'] != model['hub_id'] or record['revision'] != model['revision'] or not record['files']:
        raise ValueError(fold('snapshot receipt differs from manifest:', model['hub_id']))
    for row in record['files']:
        path = directory / row['path']
        if Path(row['path']).name != row['path'] or path.is_symlink():
            raise ValueError(fold('unexpected snapshot path:', str(path)))
        sha = checksum(path)
        if path.stat().st_size != row['size'] or sha != row['sha256']:
            raise ValueError(fold('snapshot checksum differs:', str(path)))
        if row.get('lfs_sha256') and sha != row['lfs_sha256']:
            raise ValueError(fold('published LFS checksum differs:', str(path)))


def receipts(numbers):
    """Login nodes check that each download record and file is present at its size; jobs hash."""
    for number in numbers:
        row = pair(number)
        for side, directory in zip(('original', 'modified'), paths(number)):
            manifest = directory / 'download-manifest.json'
            if not manifest.is_file():
                raise ValueError(fold('projection-only submit is missing a download receipt:', str(manifest)))
            record = json.loads(manifest.read_text())
            if record['base'] != row[side]['hub_id'] or record['revision'] != row[side]['revision']:
                raise ValueError(fold('download receipt names another snapshot:', str(manifest)))
            for item in record['files']:
                path = directory / item['path']
                if not path.is_file() or path.stat().st_size != item['size']:
                    raise ValueError(fold('downloaded file missing or a different size:', str(path)))
    print('Download receipts present: pairs ' + ' '.join(str(number) for number in numbers))


def verify_batch():
    total = count()
    for number in range(1, total + 1):
        row = pair(number)
        for side, directory in zip(('original', 'modified'), paths(number)):
            verify(directory, row[side])
    print('Verified download receipts: {} pairs'.format(total))


def main():
    if sys.argv[1] == 'env':
        number = int(sys.argv[2])
        row = pair(number)
        original, modified = paths(number)
        values = {'AUDIT_BASE': row['original']['hub_id'], 'AUDIT_ORIGINAL': str(original),
                  'AUDIT_INPUT_MODIFIED': str(modified)}
        for name, value in values.items():
            print('export {}={}'.format(name, shlex.quote(value)))
    elif sys.argv[1] == 'token-check':
        token()
        print('Hub token file: mode 600')
    elif sys.argv[1] == 'verify-pair':
        number = int(sys.argv[2])
        row = pair(number)
        for side, directory in zip(('original', 'modified'), paths(number)):
            verify(directory, row[side])
        print('Verified download receipts: pair ' + str(number))
    elif sys.argv[1] == 'receipts':
        receipts([int(value) for value in sys.argv[2:]] or list(range(1, count() + 1)))
    elif sys.argv[1] == 'verify-batch':
        verify_batch()
    elif sys.argv[1] == 'round':
        print(round_number())
    elif sys.argv[1] == 'count':
        print(count())
    elif sys.argv[1] == 'sweep':
        sweep()
    else:
        raise ValueError('unknown census operation')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, KeyError) as error:
        raise SystemExit(str(error))
