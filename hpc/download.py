# download.py -- Pin a snapshot and verify its published object checksums.
# Created by LT Sean Egan, PhD 2026-10-13
# Modified: SDE 2026-10-13  the hub token is optional; only gated originals need it.
# Modified: SDE 2026-10-13  keep the hub token out of records and command lines.
import hashlib
import json
import os
from pathlib import Path
import stat
from huggingface_hub import HfApi, snapshot_download


def checksum(path, algorithm='sha256', git_blob=False):
    """Hash in blocks; small repository files use their published git object id."""
    value = hashlib.new(algorithm)
    if git_blob:
        value.update(('blob ' + str(path.stat().st_size) + '\0').encode())
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            value.update(block)
    return value.hexdigest()


def check_file(path, row):
    """Check LFS SHA-256 or the git blob id, plus the declared size."""
    if path.stat().st_size != row['size']:
        raise ValueError('download size differs: ' + row['path'])
    sha256 = checksum(path)
    if row.get('lfs_sha256'):
        if sha256 != row['lfs_sha256']:
            raise ValueError('published LFS checksum differs: ' + row['path'])
    elif checksum(path, 'sha1', True) != row['git_blob_id']:
        raise ValueError('published git object differs: ' + row['path'])
    return sha256


def main():
    """Verify the whole selected snapshot before publishing its done marker."""
    work = Path(os.environ['AUDIT_WORK'])
    original = Path(os.environ['AUDIT_ORIGINAL'])
    marker = work / 'state/download.done'
    manifest = original / 'download-manifest.json'
    base = os.environ['AUDIT_BASE']
    if os.environ.get('AUDIT_REHEARSAL') != '1' and base != 'mistralai/Mistral-Small-3.2-24B-Instruct-2506':
        raise ValueError('round 1 permits only its approved base')
    if manifest.exists():
        record = json.loads(manifest.read_text())
        if record['base'] != base:
            raise ValueError('original directory belongs to a different base')
    else:
        token_file = Path(os.environ['HOME']) / '.hpc/hf-token'
        token = False
        if token_file.exists():
            if token_file.is_symlink() or stat.S_IMODE(token_file.stat().st_mode) != 0o600:
                raise ValueError('hub token must be a regular mode-600 file')
            token = token_file.read_text().strip()
        elif os.environ.get('AUDIT_NEEDS_HUB_TOKEN') == '1':
            raise ValueError('hub token file is missing')
        api = HfApi(token=token)
        info = api.model_info(base, revision='main', files_metadata=True)
        rows = []
        for sibling in info.siblings:
            name = sibling.rfilename
            if '/' in name or not (name.endswith('.json') or name.endswith('.safetensors') or name == 'tokenizer.model'):
                continue
            lfs = sibling.lfs
            published = lfs.sha256 if lfs else None
            if name.endswith('.safetensors') and not published:
                raise ValueError('weight shard has no published LFS checksum: ' + name)
            rows.append({'path': name, 'size': sibling.size, 'lfs_sha256': published, 'git_blob_id': sibling.blob_id})
        if not any(row['path'].endswith('.safetensors') for row in rows):
            raise ValueError('snapshot has no weight shards')
        if sum(row['size'] for row in rows) > 100 * 1024 ** 3:
            raise ValueError('original exceeds the 100 GB download budget')
        snapshot_download(base, revision=info.sha, token=token, local_dir=str(original),
                          allow_patterns=[row['path'] for row in rows], max_workers=1)
        record = {'base': base, 'revision': info.sha, 'files': rows}
    for row in record['files']:
        path = original / row['path']
        if Path(row['path']).name != row['path'] or path.is_symlink():
            raise ValueError('unexpected snapshot path')
        row['sha256'] = check_file(path, row)
    manifest.write_text(json.dumps(record, indent=2) + '\n')
    marker.write_text(record['revision'] + '\n')
    print('Published checksums passed for {} files at {}'.format(len(record['files']), record['revision']))


if __name__ == '__main__':
    main()
