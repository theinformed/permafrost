# pin_census.py -- Record public lineage and the original available at creation.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  keep dates and full revisions beside each pair.
# Modified: SDE 2026-10-29  a new manifest takes its round from its name; the names command
#                           writes rehearsal fixtures from published headers, never weights.
# Modified: SDE 2026-10-30  a parent that is itself a copy: the undeclared ancestor both sides share is
#                           the publisher root, so a copy compares against its stated parent.
# Modified: SDE 2026-10-31  an original whose surviving history starts after the copy was created pins to the
#   copy's revision date and says so in the record.
# Modified: SDE 2026-10-31  a quantised original and a repository of several weight files with no index are refused
#   at the names step.
# Modified: SDE  a copy whose weight files the census has already measured is refused before it is pinned;
#   a hub duplicate with later edits is pinned with its parent noted.
# Modified: SDE  a pair whose tensor names no pairing rule matches is refused at the names step, with the
#   counts, before the rehearsal reads an empty comparison.
# Modified: SDE  a hub id already measured at the same revision is refused with the round that measured it.
# Modified: SDE  a copy named qat whose card names the instruct model is pinned against the QAT checkpoint of
#   that size when the hub has one, with the card's field kept beside a note.
# Modified: SDE  a repository the card's first heading or sentence names, other than the field's, is recorded as
#   card_parent with a warning; the pinned original does not change for it.
import argparse
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import struct
import sys
import tempfile
from huggingface_hub import HfApi

ROOT = Path(__file__).resolve().parent.parent
DUPLICATE = 'Duplicate from'


def audit_root():
    """Make the audit package importable from the kit's own folder."""
    root = str(ROOT)
    if root not in sys.path:
        sys.path.insert(0, root)


class Duplicate(ValueError):
    """The copy's weight files are a measurement the census already holds."""


def duplicate_source(history):
    """The parent the hub's duplicate function named in the repository's first commit title, or None."""
    first = min(history, key=lambda row: row.created_at)
    title = (getattr(first, 'title', None) or '').strip()
    if title.startswith(DUPLICATE):
        return title[len(DUPLICATE):].strip() or None
    return None


def lfs_weights(info):
    """The LFS sha256 of every safetensors file in a repository listing, before any byte is downloaded."""
    weights = {}
    for item in getattr(info, 'siblings', None) or []:
        if not item.rfilename.endswith('.safetensors'):
            continue
        lfs = getattr(item, 'lfs', None)
        digest = lfs.get('sha256') if isinstance(lfs, dict) else getattr(lfs, 'sha256', None)
        if digest:
            weights[item.rfilename] = digest
    return weights


def measured_copies(root=ROOT):
    """Every copy whose weight files are measured at home, then every pair pinned with its hub checksums."""
    root = Path(root)
    rows = []
    for path in sorted((root / 'results/weights').glob('*.json')):
        report = json.loads(path.read_text())
        modified = report.get('modified') or {}
        shards = modified.get('shards_sha256') or {}
        if not shards:
            continue
        census = (report.get('census') or {}).get('modified') or {}
        match = re.search(r'/rounds/([0-9]+)/', modified.get('source') or '')
        rows.append({'hub_id': census.get('hub_id') or path.stem, 'state': 'measured', 'revision': census.get('revision'),
                     'round': int(match.group(1)) if match else None, 'sha256': set(shards.values())})
    for path in sorted((root / 'data/batches').glob('*.json')):
        record = json.loads(path.read_text())
        for row in record['pairs']:
            shards = row['modified'].get('weight_files_sha256') or {}
            if shards:
                rows.append({'hub_id': row['modified']['hub_id'], 'state': 'pinned', 'revision': row['modified'].get('revision'),
                             'round': record.get('round'), 'sha256': set(shards.values())})
    return rows


def same_weights(weights, known):
    """The measured or pinned copy whose weight files carry exactly these checksums, if any."""
    digests = set(weights.values())
    if not digests:
        return None
    matches = [row for row in known if row['sha256'] == digests]
    # The earliest measurement names the copy: a third upload of one file points at the first, not the second.
    return min(matches, key=lambda row: (row['round'] is None, row['round'] or 0)) if matches else None


def already_measured(hub_id, revision, known):
    """The earliest measurement of this hub id at this revision, if the census holds one.

    A batch note once called a copy unmeasured that round 13 had measured, and round 22 measured it
    again to the last digit; the hub id and revision in a saved report settle it, whatever a note says."""
    matches = [row for row in known if revision and row['state'] == 'measured' and row.get('revision') == revision
               and row['hub_id'].lower() == hub_id.lower()]
    return min(matches, key=lambda row: (row['round'] is None, row['round'] or 0)) if matches else None


def where(match):
    return 'in round {}'.format(match['round']) if match['round'] is not None else 'at home'


def describe(match):
    return '{} {} {}'.format(match['hub_id'], match['state'], where(match))


def declared(info):
    """Keep the card's declaration, including a list used for merges."""
    card = info.card_data.to_dict() if info.card_data else {}
    return card.get('base_model')


QAT = '-qat-q4_0-unquantized'
SIZE = re.compile(r'(?<![a-z0-9])(e?[0-9]+b(?:-a[0-9]+b)?)(?![a-z0-9])')


def size_of(hub_id):
    """The size token in a repository name (12b, e4b, 26b-a4b), or None."""
    match = SIZE.search(hub_id.split('/')[-1].lower())
    return match.group(1) if match else None


def repo_exists(api, repo):
    try:
        api.model_info(repo)
    except Exception:
        return False
    return True


def qat_original(api, modified, original, bases):
    """The QAT checkpoint a qat-named copy stands on, with the note for its record, or the original as given.

    A quantisation-aware export's generated card carries its original's header, and the QAT
    checkpoints' own cards name the instruct model as their base, so a copy named qat declares the
    instruct model one step up. When the caller followed that field on a copy whose name says qat,
    the field naming the instruct model of the copy's size, the pair is pinned against that size's
    QAT checkpoint where the hub has one. A caller who names any other original is followed."""
    declared = bases if isinstance(bases, str) else bases[0] if isinstance(bases, list) and len(bases) == 1 else None
    name = modified.split('/')[-1].lower()
    if 'qat' not in name or 'qat' in original.lower() or not declared or declared.lower() != original.lower():
        return original, None
    if not declared.lower().endswith('-it') or size_of(declared) is None or size_of(declared) != size_of(name):
        return original, None
    candidate = declared + QAT
    if not repo_exists(api, candidate):
        return original, None
    return candidate, 'base_model names {}; the copy name says qat and {} exists, so the pair is pinned against it'.format(
        declared, candidate)


HUB_ID = re.compile(r'(?<![A-Za-z0-9_/.-])([A-Za-z0-9][A-Za-z0-9_-]*)/([A-Za-z0-9][A-Za-z0-9_.-]*)')
HUB_LINK = re.compile(r'https?://(?:huggingface\.co|hf\.co)/')


def card_body(api, repo, revision):
    """The text of a repository's card after its header block, or '' when it has none."""
    download = getattr(api, 'hf_hub_download', None)
    if download is None:
        return ''
    try:
        path = download(repo_id=repo, filename='README.md', revision=revision)
    except Exception:
        return ''
    text = Path(path).read_text(encoding='utf-8', errors='replace')
    if text.startswith('---'):
        end = text.find('\n---', 3)
        if end >= 0:
            text = text[end + 4:]
    return text


def card_opening(text):
    """A card's first heading and its first sentence, past badges, images and tables."""
    heading = sentence = ''
    for line in text.splitlines():
        line = line.strip()
        if not line or line[0] in '<|!':
            continue
        if line.startswith('#'):
            if not heading:
                heading = line.lstrip('#').strip()
            continue
        sentence = re.split(r'(?<=[.!?])\s', line, 1)[0]
        break
    return heading, sentence


def card_parent(api, text, modified, bases):
    """The first repository a card's opening names that is neither the copy nor a declared base, if it exists.

    Three copies named their true parent in the README's title or first sentence while the field
    named the model under it; the person pinning sees both and chooses, the pin itself follows the
    field."""
    named = {modified.lower()} | {name.lower() for name in (bases if isinstance(bases, list) else [bases]) if isinstance(name, str)}
    for part in card_opening(text):
        for owner, name in HUB_ID.findall(HUB_LINK.sub('', part)):
            candidate = owner + '/' + name.rstrip('.,:;')
            if candidate.lower() not in named and repo_exists(api, candidate):
                return candidate
    return None


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


def pin(api, modified, original, known=(), allow_duplicate=False):
    """Choose the newest original commit no later than the copy's creation.

    A copy whose weight files carry the checksums of a copy already measured (or pinned) is its
    parent's measurement and is refused before the lineage is read, unless the caller allows it; a
    repository the hub duplicated whose weights since changed is pinned with its parent recorded."""
    copy = api.model_info(modified, files_metadata=True)
    copy_history = api.list_repo_commits(modified)
    copy_commit = next(row for row in copy_history if row.commit_id == copy.sha)
    weights = lfs_weights(copy)
    source = duplicate_source(copy_history)
    measured = already_measured(modified, copy.sha, known)
    if measured and not allow_duplicate:
        raise Duplicate('already measured ' + where(measured))
    match = same_weights(weights, known)
    if match and not allow_duplicate:
        raise Duplicate('same weight files as ' + describe(match))
    original, note = qat_original(api, modified, original, declared(copy))
    history = api.list_repo_commits(original)
    cutoff, rule = copy.created_at, 'latest commit at or before modified repository creation'
    eligible = [row for row in history if row.created_at <= cutoff]
    if not eligible:
        # The original's surviving history starts after the copy was created: the publisher rewrote it
        # (google/gemma-4-12B-it keeps no commit older than OpenYourMind's copy of it, by about an hour).
        # The copy's measured revision then sets the cutoff and the record says so.
        cutoff, rule = copy_commit.created_at, ('latest commit at or before the modified revision; the original '
                                                'history starts after the modified repository was created')
        eligible = [row for row in history if row.created_at <= cutoff]
    if not eligible:
        raise ValueError('no original revision predates creation or the modified revision: ' + modified)
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
    node['weight_files_sha256'] = weights
    if note:
        node['original_note'] = note
    parent = card_parent(api, card_body(api, modified, copy.sha), modified, declared(copy))
    if parent:
        node['card_parent'] = parent
    if source:
        node['duplicate_of'] = source
    if measured:
        node['measured_in'] = {'round': measured['round']}
        node['allow_duplicate'] = True
    if match:
        node['same_weights_as'] = {'hub_id': match['hub_id'], 'round': match['round'], 'state': match['state']}
        node['allow_duplicate'] = True
    base = lineage(original, commit.commit_id)
    base['revision_date'] = commit.created_at.isoformat()
    settle_roots(node, base)
    return {'modified': node, 'original': base,
        'original_selection': {'cutoff': cutoff.isoformat(), 'rule': rule,
            'history_commits_read': len(history),
            'original_history_starts': min(history, key=lambda row: row.created_at).created_at.isoformat()}}


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


def weight_files(hub, repo, revision):
    """The safetensors files a repository publishes at one revision, from the hub's file list."""
    from urllib.parse import quote
    hub.pause()
    url = 'https://huggingface.co/api/models/{}/revision/{}'.format(quote(repo, safe='/'), quote(revision, safe=''))
    response = hub.session.get(url, timeout=15)
    response.raise_for_status()
    return sorted(item['rfilename'] for item in response.json().get('siblings', [])
                  if item['rfilename'].endswith('.safetensors'))


def quantised(config):
    """True when a config declares quantised weights; such an original cannot be compared raw."""
    return bool(config.get('quantization_config') or config.get('text_config', {}).get('quantization_config'))


def fixture(hub, model):
    """Names, shapes and shard of every tensor at one pinned revision, with its config.

    A repository with no index and several weight files publishes several checkpoints under
    one name (DarkRomeo88's four quantised files of one copy, round 14); it is refused here
    rather than read as one checkpoint with repeated tensor names on the cluster.
    """
    repo, revision = model['hub_id'], model['revision']
    text = bounded_get(hub, repo, revision, INDEX)
    weight_map = json.loads(text.decode('utf-8'))['weight_map'] if text else None
    if weight_map:
        shards = sorted(set(weight_map.values()))
    else:
        shards = weight_files(hub, repo, revision)
        if len(shards) != 1:
            raise ValueError('{} weight files and no index: {} publishes {} under one name'.format(
                len(shards), repo, 'several checkpoints' if shards else 'no safetensors weights'))
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


SCALE = re.compile(r'\.(weight_scale|weight_scale_inv|activation_scale|input_scale)(_inv)?$')


def scale_tensors(tensors):
    """Names of the per-tensor scales a float8 checkpoint carries beside its weights."""
    return sorted(name for name in tensors if SCALE.search(name))


def wrappers(names):
    """How many names start under each first segment, the most common first."""
    counts = Counter(name.split('.')[0] + '.' for name in names)
    return ', '.join('{:,} under {}'.format(count, wrapper) for wrapper, count in counts.most_common(3))


def pairing(original_names, modified_names):
    """Pair the two sides' tensor names as the comparison will: one wrapper rule, else the plain match.

    The rules each pair every modified name or nothing, so a modified name left over is one the
    comparison would never read; the counts say how far the layouts are apart."""
    audit_root()
    from audit.weights import recipe_table, wrapper_mapping
    original_names, modified_names = set(original_names), set(modified_names)
    mapping = wrapper_mapping(original_names, modified_names, recipe_table())
    names = mapping['names'] if mapping else {name: name for name in original_names & modified_names}
    return {'paired': len(names), 'original_only': sorted(original_names - set(names)),
            'modified_only': sorted(modified_names - set(names.values())),
            'mapping': {key: mapping[key] for key in ('prefix', 'carried_by', 'renamed')} if mapping else None}


def unpaired(original, modified):
    """The refusal for two fixtures whose names the comparison cannot pair, or None when it can.

    One diffusion copy saves 1,674 tensors under decoder. and encoder. where the original saves
    1,047 under model.; no rule pairs them, and the rehearsal read an empty changed set. The names
    step says so first, with the counts on both sides."""
    result = pairing(original['tensors'], modified['tensors'])
    if not result['modified_only']:
        return partial_export(original, modified, result)
    return ('tensor names cannot be paired: {:,} of {:,} modified names pair with the {:,} original names '
            '(modified {}; original {}); {:,} modified and {:,} original names unpaired: {} against {}').format(
        result['paired'], len(modified['tensors']), len(original['tensors']), wrappers(modified['tensors']),
        wrappers(original['tensors']), len(result['modified_only']), len(result['original_only']),
        modified['hub_id'], original['hub_id'])


LAYER = re.compile(r'^(.*?layers\.)([0-9]+)\.')


def dropped_layers(original_names, result):
    """The original's layer indices the copy never carries, per tower the copy does carry.

    A copy may drop a whole tower (vision, audio) or the shared-kv tensors a layer never reads and
    still measure; a copy that stops at layer 17 of 35 is a partial export and cannot."""
    paired = set(original_names) - set(result['original_only'])
    carried = {}
    for name in paired:
        match = LAYER.match(name)
        if match:
            carried.setdefault(match.group(1), set()).add(int(match.group(2)))
    missing = {}
    for name in result['original_only']:
        match = LAYER.match(name)
        if match and match.group(1) in carried and int(match.group(2)) not in carried[match.group(1)]:
            missing.setdefault(match.group(1), set()).add(int(match.group(2)))
    return carried, missing


def partial_export(original, modified, result):
    """The refusal for a copy that carries only some of the original's layers, or None.

    One E2B copy saves 164 tensors, eighteen layers of thirty-five and no towers: every name pairs,
    so the pairing rule passes it, and the rehearsal then reads half the writers it expects."""
    carried, missing = dropped_layers(original['tensors'], result)
    if not missing:
        return None
    parts = []
    for tower in sorted(missing):
        have, lost = carried[tower], sorted(missing[tower])
        parts.append('{:,} of {:,} layers under {} (layers {} to {} missing)'.format(
            len(have), len(have) + len(lost), tower, lost[0], lost[-1]))
    return 'the copy is a partial export carrying {}: {} against {}'.format('; '.join(parts), modified['hub_id'], original['hub_id'])


def fixture_path(out, model):
    return Path(out) / (model['revision'][:12] + '.json')


def unpaired_pairs(pairs, out):
    """Every pair in the batch whose two fixtures are on disk and whose names cannot be paired."""
    refused = []
    for number, row in enumerate(pairs, 1):
        paths = [fixture_path(out, row[side]) for side in ('original', 'modified')]
        if not all(path.exists() for path in paths):
            continue
        original, modified = (json.loads(path.read_text()) for path in paths)
        reason = unpaired(original, modified)
        if reason:
            refused.append('pair {} names: {}'.format(number, reason))
    return refused


def names(manifest, out, hub=None):
    """Write one fixture per pinned checkpoint in the batch, both sides, skipping ones on disk.

    A pair whose two fixtures the comparison cannot pair by name is refused here, before the
    rehearsal, with the counts on both sides."""
    if hub is None:
        audit_root()
        from audit.hub import Hub
        hub = Hub()
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    written = []
    refused = []
    seen = set()
    pairs = json.loads(Path(manifest).read_text())['pairs']
    for number, row in enumerate(pairs, 1):
        for side in ('original', 'modified'):
            model = row[side]
            target = fixture_path(out, model)
            if model['revision'] in seen or target.exists():
                continue
            seen.add(model['revision'])
            # One refused checkpoint does not stop the screen: the rest of the batch still gets its
            # fixtures, and every refusal is reported together at the end.
            try:
                record = fixture(hub, model)
                if side == 'original' and quantised(record['config']):
                    # Finding 37: a float8 original compared raw reads as 280 changed matrices and 560 scale
                    # tensors; the pair waits for a dequantised copy made at home.
                    raise ValueError('original is quantised (quantization_config): ' + model['hub_id'])
                scales = scale_tensors(record['tensors']) if side == 'original' else []
                if scales:
                    # The same checkpoint without the config block: the scales in the names say so.
                    raise ValueError('original is quantised ({} scale tensors, {} first): {}'.format(len(scales), scales[0], model['hub_id']))
            except ValueError as error:
                refused.append('pair {} {}: {}'.format(number, side, error))
                print('refused ' + refused[-1])
                continue
            with tempfile.NamedTemporaryFile('w', dir=str(out), delete=False, suffix='.tmp') as stream:
                stream.write(json.dumps(record, sort_keys=True, separators=(',', ':')) + '\n')
            Path(stream.name).replace(target)
            written.append(target)
            print('{}: {} tensors, {}'.format(target.name, len(record['tensors']), model['hub_id']))
    for reason in unpaired_pairs(pairs, out):
        refused.append(reason)
        print('refused ' + reason)
    print('fixtures written: {}'.format(len(written)))
    if refused:
        raise ValueError('{} checkpoint(s) refused; '.format(len(refused)) + '; '.join(refused))
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
    parser.add_argument('--allow-duplicate', action='store_true',
                        help='pin a copy the census has already measured, at this revision or by its weight files')
    args = parser.parse_args()
    path = Path(args.manifest)
    record = json.loads(path.read_text()) if path.exists() else new_record(path, args)
    if any(row['modified']['hub_id'] == args.pair[0] for row in record['pairs']):
        raise ValueError('pair already pinned: ' + args.pair[0])
    try:
        row = pin(HfApi(), *args.pair, known=measured_copies(), allow_duplicate=args.allow_duplicate)
    except Duplicate as error:
        print('refused {}: {}'.format(args.pair[0], error))
        sys.exit(1)
    copy = row['modified']
    if copy.get('card_parent') and copy['card_parent'].lower() != row['original']['hub_id'].lower():
        print('warning: {} card names {} where base_model names {}; pinned against {}'.format(
            args.pair[0], copy['card_parent'], copy['declared_base_model'], row['original']['hub_id']))
    if copy.get('original_note'):
        print('note: {} {}'.format(args.pair[0], copy['original_note']))
    if copy.get('measured_in'):
        print('pinned as allowed: {} already measured {}'.format(args.pair[0], where(copy['measured_in'])))
    elif copy.get('same_weights_as'):
        print('pinned as allowed: {} has the {}'.format(args.pair[0], 'same weight files as ' + describe(copy['same_weights_as'])))
    elif copy.get('duplicate_of'):
        print('note: {} was duplicated from {} and its weight files differ; pinned'.format(args.pair[0], copy['duplicate_of']))
    record['pairs'].append(row)
    record['pinned_at'] = datetime.now(timezone.utc).isoformat()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(record, indent=2) + '\n')


if __name__ == '__main__':
    main()
