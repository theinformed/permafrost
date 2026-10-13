# cleanup.py -- Delete exact approved derivative paths after archive read-back.
# Created by LT Sean Egan, PhD 2026-10-13
# Modified: SDE 2026-10-13  compare archive hashes before removing any checkpoint.
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil


def digest(path):
    """Read an archived measurement without loading it all at once."""
    checksum = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            checksum.update(block)
    return checksum.hexdigest()


def cleanup(ruling, receipt, root):
    """Allow only exact, absolute derived paths with verified archive copies."""
    text = Path(ruling).read_text()
    if '\n## approved paths\n' not in text:
        raise ValueError('no approved paths in the controller ruling')
    section = text.split('\n## approved paths\n', 1)[1].split('\n## ', 1)[0]
    approved = [line[2:].strip().strip('`') for line in section.splitlines() if line.startswith('- ')]
    if not approved:
        raise ValueError('approved paths section is empty')
    root = Path(root).resolve()
    paths = []
    for name in approved:
        path = Path(name)
        resolved = path.resolve()
        if not path.is_absolute() or str(path) != str(resolved) or path.is_symlink() or root not in resolved.parents:
            raise ValueError('approved path must be an exact child of derived/')
        paths.append(resolved)
    proof = json.loads(Path(receipt).read_text())
    if proof.get('project') != 'model-audit' or proof.get('round') != 1 or proof.get('read_back') is not True:
        raise ValueError('archive receipt has not passed read-back')
    if set(proof.get('approved_paths', [])) != set(str(path) for path in paths):
        raise ValueError('archive receipt names different paths')
    records = proof.get('measurements', [])
    if len(records) < 2 or not any(row['source'].endswith('.json') for row in records) or not any(row['source'].endswith('.directions.safetensors') for row in records):
        raise ValueError('archive receipt needs the report and direction measurements')
    archive_root = Path(os.environ['ARCHIVE_HOME']).resolve()
    measurement_root = root.parent / 'measurements'
    for row in records:
        source, archive = Path(row['source']).resolve(), Path(row['archive']).resolve()
        if measurement_root not in source.parents or archive_root not in archive.parents:
            raise ValueError('measurement or archive path is outside its storage area')
        if digest(source) != row['sha256'] or digest(archive) != row['sha256']:
            raise ValueError('archive read-back differs from the local measurement')
    for path in paths:
        if path.exists():
            shutil.rmtree(str(path))
    (root.parent / 'ARCHIVED').write_text(proof['archived_at'] + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ruling', required=True)
    parser.add_argument('--receipt', required=True)
    args = parser.parse_args()
    cleanup(args.ruling, args.receipt, Path(os.environ['WORKDIR']) / 'model-audit/derived')
