# census.py -- Name pinned batch inputs and verify them before every comparison.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  separate download inputs from each try's scratch.
# Modified: SDE 2026-10-15  a login-side check of the download records that reads sizes, not weights.
import hashlib
import json
import os
from pathlib import Path
import shlex
import stat
import sys

from say import fold


def batch():
    return json.loads(Path('batch.json').read_text())


def pair(number):
    pairs = batch()['pairs']
    if len(pairs) != 5 or not 1 <= number <= 5:
        raise ValueError('census requires five pairs and a piece from 1 through 5')
    return pairs[number - 1]


def paths(number):
    row = pair(number)
    base = row['original']
    key = hashlib.sha256((base['hub_id'] + '@' + base['revision']).encode()).hexdigest()
    original = Path(os.environ['WORKDIR']) / 'model-audit/originals' / key
    modified = Path(os.environ['AUDIT_WORK']) / 'inputs' / ('pair-' + str(number))
    return original, modified


def token():
    """Only this regular file supplies credentials; ambient tokens are ignored."""
    path = Path(os.environ['HOME']) / '.hpc/hf-token'
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
    for number in range(1, 6):
        row = pair(number)
        for side, directory in zip(('original', 'modified'), paths(number)):
            verify(directory, row[side])
    print('Verified download receipts: five pairs')


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
        receipts([int(value) for value in sys.argv[2:]] or [1, 2, 3, 4, 5])
    elif sys.argv[1] == 'verify-batch':
        verify_batch()
    else:
        raise ValueError('unknown census operation')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, KeyError) as error:
        raise SystemExit(str(error))
