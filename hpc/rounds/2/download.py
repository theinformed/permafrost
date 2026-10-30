# download.py -- Stage every pinned snapshot of the batch in one transfer job.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  verify published objects before saving the batch receipt.
# Modified: SDE 2026-10-15  leave the duplicate consolidated shards behind; fold messages.
# Modified: SDE 2026-10-29  any pair count, shared originals once, and a probe before any shard.
# Modified: SDE 2026-10-30  fetch a checkpoint three times before giving up, naming the hub's own error.
import hashlib
import json
import os
from pathlib import Path
import shutil
import time
from huggingface_hub import HfApi, snapshot_download
from census import batch, checksum, count, pair, paths, token, verify
from lineage import screen
from say import fold


def selected(info):
    """Take native shards and small metadata, leaving alternate formats behind."""
    rows = []
    for item in info.siblings:
        name = item.rfilename
        if '/' in name or not (name.endswith(('.safetensors', '.json', '.jinja')) or name == 'tokenizer.model'):
            continue
        # Mistral repos carry a second copy of every weight in their own format.
        if name.startswith('consolidated'):
            continue
        if name.endswith('.safetensors') and not item.lfs:
            raise ValueError(fold('weight shard has no published LFS checksum:', name))
        if item.size is None:
            raise ValueError(fold('snapshot file size is unknown:', name))
        rows.append({'path': name, 'size': item.size,
                     'lfs_sha256': item.lfs.sha256 if item.lfs else None, 'git_blob_id': item.blob_id})
    if not any(row['path'].endswith('.safetensors') for row in rows):
        raise ValueError(fold('snapshot has no native shards:', info.id))
    return rows


def check_file(path, row):
    """Small files have git blob hashes; shards have LFS hashes."""
    if path.is_symlink() or path.stat().st_size != row['size']:
        raise ValueError(fold('download size differs:', row['path']))
    sha = checksum(path)
    if row.get('lfs_sha256'):
        if sha != row['lfs_sha256']:
            raise ValueError(fold('published LFS checksum differs:', row['path']))
    else:
        value = hashlib.sha1(('blob ' + str(row['size']) + '\0').encode())
        with path.open('rb') as stream:
            for block in iter(lambda: stream.read(1024 * 1024), b''):
                value.update(block)
        if value.hexdigest() != row['git_blob_id']:
            raise ValueError(fold('published git object differs:', row['path']))
    return sha


def probe(api, credential):
    """Fetch one small published file through the same client before any shard.

    The desk reads the PROBE line from the drop: it says whether this node reaches the hub.
    """
    model = pair(1)['original']
    row = None
    try:
        info = api.model_info(model['hub_id'], revision=model['revision'], files_metadata=True)
        listed = [item for item in info.siblings if '/' not in item.rfilename
                  and item.rfilename.endswith('.json') and item.size is not None]
        if not listed:
            raise ValueError('no top-level .json file is listed')
        item = min(listed, key=lambda entry: (entry.size, entry.rfilename))
        row = {'path': item.rfilename, 'size': item.size, 'git_blob_id': item.blob_id,
               'lfs_sha256': item.lfs.sha256 if item.lfs else None}
        folder = Path(os.environ['AUDIT_WORK']) / 'probe'
        if folder.exists():
            shutil.rmtree(str(folder))
        snapshot_download(model['hub_id'], revision=model['revision'], token=credential,
                          local_dir=str(folder), allow_patterns=[row['path']], max_workers=1)
        check_file(folder / row['path'], row)
        shutil.rmtree(str(folder))
    except Exception as error:
        lines = str(error).splitlines() or ['']
        print('PROBE FAIL {}: {}'.format(type(error).__name__, lines[0])[:100], flush=True)
        if len(lines) > 1 or len(lines[0]) > 80:
            print(fold('probe error text:', None, None, str(error)), flush=True)
        raise SystemExit(1)
    print('PROBE OK {} {}'.format(row['size'], model['hub_id'])[:100], flush=True)


def fetch(model, directory, rows, credential, tries=3, pause=120):
    """Download one pinned snapshot; a hub or network fault gets two more tries after a pause.

    The hub client turns any failed repository lookup (a dropped connection, a 429, a 5xx) into one
    message about locating files on the Hub; the cause it chains is printed so the log names the fault.
    A retry resumes the files already on disk (Blueback 3392481 died on its third checkpoint, 23 min in).
    """
    for attempt in range(1, tries + 1):
        try:
            snapshot_download(model['hub_id'], revision=model['revision'], token=credential,
                              local_dir=str(directory), allow_patterns=[row['path'] for row in rows], max_workers=1)
            return
        except Exception as error:
            cause = error.__cause__ or error.__context__
            detail = '{}: {}'.format(type(error).__name__, str(error).split('\n')[0])
            if cause is not None:
                detail += ' <- {}: {}'.format(type(cause).__name__, str(cause).split('\n')[0])
            print(fold('hub fetch {} of {} failed for {}:'.format(attempt, tries, model['hub_id']), detail), flush=True)
            if attempt == tries:
                raise ValueError('checkpoint fetch failed after {} tries: {}'.format(tries, detail))
            time.sleep(pause)


def main():
    screen(batch(), 'maker-guard.sha256')
    marker = Path(os.environ['AUDIT_WORK']) / 'state/download.done'
    if marker.exists():
        marker.unlink()
    credential = token()
    api = HfApi(token=credential)
    probe(api, credential)
    plans = []
    seen = set()
    for number in range(1, count() + 1):
        for side, directory in zip(('original', 'modified'), paths(number)):
            # Pairs that share an original share its folder: one plan, one download.
            if str(directory) in seen:
                continue
            seen.add(str(directory))
            model = pair(number)[side]
            info = api.model_info(model['hub_id'], revision=model['revision'], files_metadata=True)
            if info.sha != model['revision']:
                raise ValueError('hub revision differs from census pin')
            plans.append((model, directory, selected(info)))
    size = sum(row['size'] for _, _, rows in plans for row in rows)
    work = Path(os.environ['WORKDIR']) / 'model-audit'
    requested = json.loads(Path('needs.json').read_text())['bytes']
    # Hard links in compare scratch add no second checkpoint copy.
    if size > requested or size > 8 * 1024 ** 4:
        raise ValueError('batch exceeds declared work space')
    free = os.statvfs(str(work))
    if size > free.f_bavail * free.f_frsize:
        raise ValueError('batch exceeds filesystem free space')
    print('Batch download plan: {:.1f} GB'.format(size / 1024 ** 3), flush=True)
    for model, directory, rows in plans:
        directory.mkdir(parents=True, exist_ok=True)
        manifest = directory / 'download-manifest.json'
        if manifest.exists():
            verify(directory, model)
            record = json.loads(manifest.read_text())
            published = [{key: row[key] for key in ('path', 'size', 'lfs_sha256', 'git_blob_id')}
                         for row in record['files']]
            if published != rows:
                raise ValueError('saved receipt differs from pinned hub objects')
        else:
            fetch(model, directory, rows, credential)
        for row in rows:
            row['sha256'] = check_file(directory / row['path'], row)
        manifest.write_text(json.dumps({'base': model['hub_id'], 'revision': model['revision'],
                                        'files': rows}, indent=2) + '\n')
        print(fold('Published checksums passed:', model['hub_id']), flush=True)
    marker.write_text(checksum(Path('batch.json')) + '\n')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError) as error:
        raise SystemExit(str(error))
