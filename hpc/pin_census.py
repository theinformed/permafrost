# pin_census.py -- Record public lineage and the original available at creation.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  keep dates and full revisions beside each pair.
# Modified: SDE 2026-10-29  a new manifest takes its round from its name; the names command
#                           writes rehearsal fixtures from published headers, never weights.
# Modified: SDE 2026-10-30  a parent that is itself a copy: the undeclared ancestor both sides share is
#                           the publisher root, so a copy compares against its stated parent.
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import struct
import sys
import tempfile
from huggingface_hub import HfApi


def declared(info):
    """Keep the card's declaration, including a list used for merges."""
    card = info.card_data.to_dict() if info.card_data else {}
    return card.get('base_model')


def leaves(node):
    """Every ancestor in the tree that declares no base of its own."""
    if not node['base_model_chain']:
        return [node]
    return [leaf for child in node['base_model_chain'] for leaf in leaves(child)]


def settle_roots(copy, base):
    """Mark the publisher roots of both trees and what each node's lineage settles.

    An undeclared ancestor is a publisher root when the original's publisher put it out, or when
    both sides descend from it and neither party to the comparison published it; that second case
    is a copy compared with its stated parent, itself a copy of the maker's model. An undeclared
    ancestor on one side alone stays unknown and the screen holds the pair."""
    parties = {copy['maker'], base['maker']}
    shared = {leaf['hub_id'] for leaf in leaves(copy)} & {leaf['hub_id'] for leaf in leaves(base)}

    def walk(node, root=False):
        undeclared = not node['base_model_chain']
        node['publisher_root'] = bool(undeclared and not root and (
            node['maker'] == base['maker'] or (node['hub_id'] in shared and node['maker'] not in parties)))
        node['lineage_known'] = not undeclared or node['publisher_root']
        for child in node['base_model_chain']:
            walk(child)

    walk(copy, root=True)
    walk(base)


def pin(api, modified, original):
    """Choose the newest original commit no later than the copy's creation."""
    copy = api.model_info(modified)
    copy_history = api.list_repo_commits(modified)
    copy_commit = next(row for row in copy_history if row.commit_id == copy.sha)
    history = api.list_repo_commits(original)
    eligible = [row for row in history if row.created_at <= copy.created_at]
    if not eligible:
        raise ValueError('no original revision predates creation: ' + modified)
    commit = max(eligible, key=lambda row: row.created_at)
    seen = set()

    def lineage(repo, revision, root=False):
        """Follow every declared parent; a missing declaration on a copy is held."""
        if (repo, revision) in seen:
            raise ValueError('lineage cycle: ' + repo)
        seen.add((repo, revision))
        info = api.model_info(repo, revision=revision)
        bases = declared(info)
        names = bases if isinstance(bases, list) else [bases] if bases else []
        nodes = []
        for name in names:
            if not isinstance(name, str) or '/' not in name:
                raise ValueError('unknown base declaration: ' + repo)
            parent = api.model_info(name)
            nodes.append(lineage(name, parent.sha))
        seen.remove((repo, revision))
        return {'hub_id': repo, 'maker': repo.split('/')[0].lower(), 'revision': info.sha,
                'declared_base_model': bases, 'base_model_chain': nodes,
                'created_at': info.created_at.isoformat()}

    node = lineage(modified, copy.sha, root=True)
    if not node['base_model_chain']:
        raise ValueError('modified base unknown: ' + modified)
    node['revision_date'] = copy_commit.created_at.isoformat()
    base = lineage(original, commit.commit_id)
    base['revision_date'] = commit.created_at.isoformat()
    settle_roots(node, base)
    return {'modified': node, 'original': base,
        'original_selection': {'cutoff': copy.created_at.isoformat(),
            'rule': 'latest commit at or before modified repository creation',
            'history_commits_read': len(history)}}


INDEX = 'model.safetensors.index.json'
SINGLE = 'model.safetensors'
HEADER_LIMIT = 64 * 1024 * 1024


def bounded_get(hub, repo, revision, filename, limit=HEADER_LIMIT):
    """One small published file at the pinned revision, or None when the repository has none."""
    from huggingface_hub import hf_hub_url
    hub.pause()
    with hub.session.get(hf_hub_url(repo, filename, revision=revision), stream=True, timeout=15) as response:
        if response.status_code == 404:
            return None
        response.raise_for_status()
        data = bytearray()
        for chunk in response.iter_content(65536):
            data.extend(chunk)
            if len(data) > limit:
                raise ValueError('{} exceeds {} bytes: {}'.format(filename, limit, repo))
    return bytes(data)


def shard_header(hub, repo, revision, filename):
    """The safetensors header alone: eight length bytes, then that much JSON, by byte range."""
    from audit.gguf import RangeReader
    reader = RangeReader(hub, repo, revision, filename)
    size = struct.unpack('<Q', reader.read(8))[0]
    if not 0 < size < HEADER_LIMIT - 8:
        raise ValueError('safetensors header length out of range: {} {}'.format(repo, filename))
    header = json.loads(reader.read(size).decode('utf-8'))
    header.pop('__metadata__', None)
    return header


def fixture(hub, model):
    """Names, shapes and shard of every tensor at one pinned revision, with its config."""
    repo, revision = model['hub_id'], model['revision']
    text = bounded_get(hub, repo, revision, INDEX)
    weight_map = json.loads(text.decode('utf-8'))['weight_map'] if text else None
    shards = sorted(set(weight_map.values())) if weight_map else [SINGLE]
    tensors = {}
    for shard in shards:
        for name, row in shard_header(hub, repo, revision, shard).items():
            tensors[name] = {'dtype': row['dtype'], 'file': shard, 'shape': row['shape']}
    config = bounded_get(hub, repo, revision, 'config.json')
    record = {'config': json.loads(config.decode('utf-8')) if config else {}, 'hub_id': repo,
              'revision': revision,
              'source': 'published safetensors headers at this revision (names and shapes only; no weights)',
              'tensors': dict(sorted(tensors.items()))}
    if weight_map is not None:
        record['index_weight_map_matches'] = weight_map == {name: row['file'] for name, row in tensors.items()}
    return record


def names(manifest, out, hub=None):
    """Write one fixture per pinned checkpoint in the batch, both sides, skipping ones on disk."""
    if hub is None:
        root = str(Path(__file__).resolve().parent.parent)
        if root not in sys.path:
            sys.path.insert(0, root)
        from audit.hub import Hub
        hub = Hub()
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    written = []
    seen = set()
    for row in json.loads(Path(manifest).read_text())['pairs']:
        for side in ('original', 'modified'):
            model = row[side]
            target = out / (model['revision'][:12] + '.json')
            if model['revision'] in seen or target.exists():
                continue
            seen.add(model['revision'])
            record = fixture(hub, model)
            with tempfile.NamedTemporaryFile('w', dir=str(out), delete=False, suffix='.tmp') as stream:
                stream.write(json.dumps(record, sort_keys=True, separators=(',', ':')) + '\n')
            Path(stream.name).replace(target)
            written.append(target)
            print('{}: {} tensors, {}'.format(target.name, len(record['tensors']), model['hub_id']))
    print('fixtures written: {}'.format(len(written)))
    return written


def new_record(path, args):
    """A new manifest's round and batch come from its name, round-N-batch-M.json, or the flags."""
    match = re.fullmatch(r'round-([0-9]+)-batch-([0-9]+)\.json', path.name)
    number = args.round or (int(match.group(1)) if match else 2)
    batch = args.batch or (int(match.group(2)) if match else 1)
    return {'round': number, 'batch': batch, 'pairs': []}


def main():
    if sys.argv[1:2] == ['names']:
        parser = argparse.ArgumentParser(prog='pin_census.py names')
        parser.add_argument('manifest')
        parser.add_argument('--out', required=True, help='for example tests/fixtures/round2')
        args = parser.parse_args(sys.argv[2:])
        names(args.manifest, args.out)
        return
    parser = argparse.ArgumentParser()
    parser.add_argument('manifest')
    parser.add_argument('--pair', nargs=2, required=True)
    parser.add_argument('--round', type=int, help='for a new manifest')
    parser.add_argument('--batch', type=int, help='for a new manifest')
    args = parser.parse_args()
    path = Path(args.manifest)
    record = json.loads(path.read_text()) if path.exists() else new_record(path, args)
    if any(row['modified']['hub_id'] == args.pair[0] for row in record['pairs']):
        raise ValueError('pair already pinned: ' + args.pair[0])
    record['pairs'].append(pin(HfApi(), *args.pair))
    record['pinned_at'] = datetime.now(timezone.utc).isoformat()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(record, indent=2) + '\n')


if __name__ == '__main__':
    main()
