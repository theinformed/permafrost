# direction_cosines.py -- Compare the saved edit directions of copies that share a parent, so no agreement figure is carried by hand.
# Created by SDE
# Modified: SDE 2026-11-03  first pass: group by parent, cosine per shared key, per-parent json, index.
"""Compare the edit directions of every measured copy that shares a parent.

Each pull under --pulls holds <system>N/measurements/pair-K/ folders with
metadata.json and weights.directions.safetensors. A folder gives the copy repo,
the parent repo, the pull name and the pair number. Copies are grouped by
parent; every unordered pair of copies under a parent is compared key by key,
one copy's tensors loaded at a time. Each parent group is written as
DIR_OUT/<parent id>.json and all rows are listed in DIR_OUT/index.md.
"""

import argparse
import collections
import json
import statistics
from pathlib import Path

import torch
from safetensors import safe_open

HIGH = 0.9
IDENTICAL = 0.999999
SIDES = ('left', 'right')


def key_parts(key):
    """Return (kind, layer, side) for a directions key, or None."""
    if '.weight.' not in key:
        return None
    head, side = key.rsplit('.', 1)
    if side not in SIDES:
        return None
    before = head[:head.index('.weight')]
    kind = before.rsplit('.', 1)[-1]
    layer = None
    tokens = before.split('.')
    if 'layers' in tokens:
        at = tokens.index('layers')
        if at + 1 < len(tokens) and tokens[at + 1].isdigit():
            layer = int(tokens[at + 1])
    return kind, layer, side


def read_metadata(folder):
    meta = json.loads((folder / 'metadata.json').read_text())
    copy = meta['modified']['repo']
    parent = meta['original']['repo']
    return copy, parent


def load_vectors(path, keys):
    """Load the named keys as float64 tensors."""
    out = {}
    with safe_open(str(path), framework='pt') as handle:
        for key in keys:
            out[key] = handle.get_tensor(key).to(torch.float64)
    return out


def key_count(path):
    with safe_open(str(path), framework='pt') as handle:
        return len(handle.keys())


def cosine(a, b):
    na = float(torch.linalg.vector_norm(a))
    nb = float(torch.linalg.vector_norm(b))
    if na == 0.0 or nb == 0.0:
        return 0.0
    return float(torch.dot(a, b)) / (na * nb)


def compare(copy_a, copy_b):
    """Compare two copies, loading one copy's tensors at a time."""
    with safe_open(str(copy_a['path']), framework='pt') as handle:
        keys_a = list(handle.keys())
    with safe_open(str(copy_b['path']), framework='pt') as handle:
        keys_b = set(handle.keys())
    shared = [k for k in keys_a if k in keys_b]
    vec_a = load_vectors(copy_a['path'], shared)
    vec_b = load_vectors(copy_b['path'], shared)
    per_side = {side: [] for side in SIDES}
    per_kind = collections.defaultdict(list)
    for key in shared:
        value = cosine(vec_a[key], vec_b[key])
        parts = key_parts(key)
        side = parts[2] if parts else 'other'
        per_side.setdefault(side, []).append([key, round(value, 6)])
        if parts:
            per_kind[parts[0]].append(value)
    row = {
        'copy_a': copy_a['repo'], 'copy_b': copy_b['repo'],
        'pull_a': copy_a['pull'], 'pull_b': copy_b['pull'],
        'pair_a': copy_a['pair'], 'pair_b': copy_b['pair'],
        'same_repo': copy_a['repo'] == copy_b['repo'],
        'shared_keys': len(shared),
        'identical': bool(shared) and all(v > IDENTICAL for v in vec_cosines(per_side)),
    }
    for side in SIDES:
        values = [v for _, v in per_side[side]]
        row[side] = {
            'count': len(values),
            'median': round(statistics.median(values), 6) if values else None,
            'min': round(min(values), 6) if values else None,
            'max': round(max(values), 6) if values else None,
            'high_fraction': (round(sum(1 for v in values if abs(v) >= HIGH) / len(values), 6)
                              if values else None),
            'flip_fraction': (round(sum(1 for v in values if v <= -HIGH) / len(values), 6)
                              if values else None),
            'cosines': per_side[side],
        }
    row['kind_medians'] = {kind: round(statistics.median(vals), 6)
                           for kind, vals in sorted(per_kind.items())}
    return row


def vec_cosines(per_side):
    for side in SIDES:
        for _, value in per_side[side]:
            yield value


def collect(pulls):
    """Return (copies, read count, skipped count)."""
    copies = []
    read = 0
    skipped = 0
    for pull in pulls:
        pull = Path(pull)
        if pull.name == 'measurements':
            roots = [pull]
        else:
            roots = sorted(pull.glob('*/measurements')) + sorted(pull.glob('measurements'))
        for root in roots:
            for folder in sorted(root.glob('pair-*')):
                meta = folder / 'metadata.json'
                weights = folder / 'weights.directions.safetensors'
                if not meta.is_file() or not weights.is_file():
                    skipped += 1
                    continue
                try:
                    copy, parent = read_metadata(folder)
                except (OSError, ValueError, KeyError, TypeError):
                    skipped += 1
                    continue
                copies.append({'repo': copy, 'parent': parent,
                               'pull': root.parent.name,
                               'pair': folder.name[len('pair-'):], 'path': weights})
                read += 1
    return copies, read, skipped


def parent_id(parent):
    return parent.replace('/', '-')


def fmt(value):
    return '' if value is None else f'{value:.6f}'


def write_index(out, rows):
    lines = ['| parent | copy A | copy B | shared keys | right median | left median '
             '| |cos|>=0.9 right | identical | same repo |',
             '| --- | --- | --- | --- | --- | --- | --- | --- | --- |']
    for row in rows:
        lines.append(
            f"| {row['parent']} | {row['copy_a']} | {row['copy_b']} | {row['shared_keys']} "
            f"| {fmt(row['right']['median'])} | {fmt(row['left']['median'])} "
            f"| {fmt(row['right']['high_fraction'])} "
            f"| {'yes' if row['identical'] else 'no'} "
            f"| {'yes' if row['same_repo'] else 'no'} |")
    path = out / 'index.md'
    path.write_text('\n'.join(lines) + '\n')
    return path


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--pulls', nargs='+', required=True,
                        help='pull roots holding <system>N/measurements/pair-K folders')
    parser.add_argument('--out', required=True, help='output directory')
    parser.add_argument('--min-shared', type=int, default=1,
                        help='fewest shared keys a comparison needs (default 1)')
    args = parser.parse_args(argv)

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    copies, read, skipped = collect(args.pulls)
    groups = collections.defaultdict(list)
    for copy in copies:
        groups[copy['parent']].append(copy)
    groups = {parent: members for parent, members in groups.items() if len(members) >= 2}

    failed = 0
    rows = []
    for parent in sorted(groups):
        members = groups[parent]
        try:
            comparisons = []
            for i in range(len(members)):
                for j in range(i + 1, len(members)):
                    row = compare(members[i], members[j])
                    if row['shared_keys'] < args.min_shared:
                        continue
                    row['parent'] = parent
                    comparisons.append(row)
            comparisons.sort(key=lambda r: (r['right']['median'] is None,
                                            -(r['right']['median'] or 0.0)))
            document = {
                'parent': parent,
                'copies': [{'repo': m['repo'], 'pull': m['pull'], 'pair': m['pair'],
                            'keys': key_count(m['path'])} for m in members],
                'comparisons': comparisons,
            }
            path = out / f'{parent_id(parent)}.json'
            path.write_text(json.dumps(document, indent=1) + '\n')
            print(f'{path.name} {path.stat().st_size}')
            rows.extend(comparisons)
        except Exception as error:  # noqa: BLE001
            failed += 1
            first = str(error).splitlines()[0] if str(error) else type(error).__name__
            print(f'{parent}: {first}')

    rows.sort(key=lambda r: (r['parent'], r['right']['median'] is None,
                             -(r['right']['median'] or 0.0)))
    index = write_index(out, rows)
    print(f'{index.name} {index.stat().st_size}')
    print(f'folders read {read}, skipped {skipped}, parents with two or more copies '
          f'{len(groups)}, comparisons written {len(rows)}')
    return 1 if failed else 0


if __name__ == '__main__':
    raise SystemExit(main())
