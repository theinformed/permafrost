# direction_layers.py -- Place every copy's saved edit direction against a per-layer reference copy, layer by layer, and measure how the reference's own direction rotates with depth.
# Created by SDE
# Modified: SDE 2026-11-03  first pass: reference rotation, per-copy window and best layer, markdown and json.
# Modified: SDE 2026-11-03  print layer numbers as whole integers (whole), not three-decimal cosines.
"""Place the edit directions of every copy of one parent against a reference copy.

--group names a results/directions/<parent>.json with a parent and a copies[]
list of {repo, pull, pair}. For each copy the file is found as
DIR/<pull>/measurements/pair-<pair>/weights.directions.safetensors under the
first --pulls DIR where it exists. Vectors are the keys matching
layers.<n>. whose name ends with <kind>.weight.left, loaded as float64 unit
vectors; cosines are absolute dot products. The reference's own rotation with
depth is measured over all unordered layer pairs, and each other copy's middle
layer vector is placed against every reference layer. The markdown goes to
--out and the same stem with .json beside it.
"""

import argparse
import itertools
import json
import re
import statistics
import sys
from pathlib import Path

import torch
from safetensors import safe_open

LAYER = re.compile(r'layers\.(\d+)\.')
ADJACENT = 1
FAR = 10


def find_file(pulls, copy):
    """Return the first DIR/<pull>/measurements/pair-<pair>/weights.directions.safetensors."""
    for root in pulls:
        path = (Path(root) / str(copy['pull']) / 'measurements'
                / f"pair-{copy['pair']}" / 'weights.directions.safetensors')
        if path.is_file():
            return path
    return None


def load_layers(path, kind):
    """Return {layer: float64 unit vector} for the keys of the given kind."""
    suffix = f'{kind}.weight.left'
    out = {}
    with safe_open(str(path), framework='pt') as handle:
        for key in handle.keys():
            if not key.endswith(suffix):
                continue
            match = LAYER.search(key)
            if not match:
                continue
            vector = handle.get_tensor(key).to(torch.float64)
            norm = float(torch.linalg.vector_norm(vector))
            if norm == 0.0:
                continue
            out[int(match.group(1))] = vector / norm
    return out


def abs_cos(a, b):
    return abs(float(torch.dot(a, b)))


def rotation(vectors):
    """Median |cos| for adjacent and far layer pairs, with counts and far minimum."""
    layers = sorted(vectors)
    adjacent = []
    far = []
    for lo, hi in itertools.combinations(layers, 2):
        value = abs_cos(vectors[lo], vectors[hi])
        if hi - lo == ADJACENT:
            adjacent.append(value)
        if hi - lo >= FAR:
            far.append(value)
    return {
        'adjacent_median': statistics.median(adjacent) if adjacent else None,
        'adjacent_count': len(adjacent),
        'far_median': statistics.median(far) if far else None,
        'far_count': len(far),
        'far_min': min(far) if far else None,
    }


def place(vectors, reference):
    """Window, own spread and the middle layer placed against every reference layer."""
    layers = sorted(vectors)
    window = [layers[0], layers[-1]]
    own = [abs_cos(vectors[a], vectors[b]) for a, b in itertools.combinations(layers, 2)]
    own_spread = statistics.median(own) if len(own) >= 2 else None
    middle = vectors[layers[len(layers) // 2]]
    scored = sorted(((abs_cos(middle, reference[layer]), layer) for layer in sorted(reference)),
                    key=lambda item: (-item[0], item[1]))
    best = [scored[0][1], scored[0][0]] if scored else None
    nxt = [scored[1][1], scored[1][0]] if len(scored) > 1 else None
    return {'window': window, 'own_spread': own_spread, 'best': best, 'next': nxt}


def three(value):
    return 'none' if value is None else f'{value:.3f}'


def whole(value):
    return 'none' if value is None else str(int(value))


def write_markdown(path, reference, parent, rot, rows):
    adjacent = (f"adjacent layers median {three(rot['adjacent_median'])} "
                f"on {rot['adjacent_count']} pairs")
    far = (f"ten or more apart median {three(rot['far_median'])} "
           f"on {rot['far_count']} pairs, minimum {three(rot['far_min'])}")
    lines = [
        f'# {path.stem} -- {reference} placed layer by layer against every other copy of {parent}.',
        '',
        f'{adjacent}; {far}',
        '',
        '| copy | window | own spread | best layer | cos | next layer | cos |',
        '| --- | --- | --- | --- | --- | --- | --- |',
    ]
    for row in rows:
        window = 'none' if row['window'] is None else f"{row['window'][0]}..{row['window'][1]}"
        best = row['best'] or [None, None]
        nxt = row['next'] or [None, None]
        lines.append(
            f"| {row['repo']} | {window} | {three(row['own_spread'])} "
            f"| {whole(best[0])} | {three(best[1])} "
            f"| {whole(nxt[0])} | {three(nxt[1])} |")
    path.write_text('\n'.join(lines) + '\n')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--group', required=True,
                        help='results/directions/<parent>.json with parent and copies[]')
    parser.add_argument('--pulls', nargs='+', required=True,
                        help='pull roots holding <pull>/measurements/pair-<pair> folders')
    parser.add_argument('--reference', required=True, help='a copy repo in the group')
    parser.add_argument('--kind', default='o_proj', help='tensor-name suffix (default o_proj)')
    parser.add_argument('--out', required=True, help='output markdown file')
    args = parser.parse_args(argv)

    group = json.loads(Path(args.group).read_text())
    parent = group['parent']
    copies = group.get('copies', [])
    repos = []
    for copy in copies:
        if copy['repo'] not in repos:
            repos.append(copy['repo'])
    if args.reference not in repos:
        print(f'reference {args.reference} is not in the group of {parent}', file=sys.stderr)
        return 2

    reference_path = find_file(args.pulls, next(c for c in copies
                                                if c['repo'] == args.reference))
    reference = load_layers(reference_path, args.kind) if reference_path else {}
    if not reference:
        print(f'reference {args.reference} has no {args.kind} layer keys', file=sys.stderr)
        return 2

    rot = rotation(reference)
    rows = []
    skipped = []
    for repo in sorted(r for r in repos if r != args.reference):
        copy = next(c for c in copies if c['repo'] == repo)
        path = find_file(args.pulls, copy)
        vectors = load_layers(path, args.kind) if path else {}
        if not vectors:
            skipped.append(repo)
            rows.append({'repo': repo, 'window': None, 'own_spread': None,
                         'best': None, 'next': None})
            continue
        row = {'repo': repo}
        row.update(place(vectors, reference))
        rows.append(row)

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    write_markdown(out, args.reference, parent, rot, rows)
    document = {
        'parent': parent,
        'reference': args.reference,
        'kind': args.kind,
        'rotation': rot,
        'copies': rows,
        'skipped': skipped,
    }
    out.with_suffix('.json').write_text(json.dumps(document, indent=1) + '\n')
    print(f'{out.name} {out.stat().st_size}')
    print(f'copies {len(rows)}, skipped {len(skipped)}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
