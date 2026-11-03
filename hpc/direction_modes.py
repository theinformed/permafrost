# direction_modes.py -- Sort every census copy into an edit mode by how its own directions rotate with depth, then count the modes by name word and by family.
# Created by SDE
# Modified: SDE 2026-11-03  first pass: per-copy mode from own rotation, counts by name word and family, markdown and json.
# Modified: SDE 2026-11-03  number a family by its 1-based position among the families of the same parent, not the whole list.
# Modified: SDE 2026-11-03  skip the command's own modes.json and any copies list without pull and pair when reading the census.
# Modified: SDE 2026-11-03  add the pair figure: median |cos| between the copy's o_proj and down_proj left vectors of the same layer.
"""Sort every census copy into an edit mode by its own layer rotation.

--directions names a census folder of <parent id>.json files, each with a
parent and a copies[] list of {repo, pull, pair}; families.json and files
without a copies list are skipped. Each copy's <kind>.weight.left vectors are
loaded from the first --pulls DIR holding them, and direction_layers.place
gives the copy's own window, spread, adjacent and far medians. The mode is
"few layers" under three layers, "one direction" when the far median (or the
own spread when there is no far pair) is at least 0.9, "per layer" when the
adjacent median is at least 0.5 and the far median at most 0.2, "arbitrary
rank" when the adjacent median is under 0.2, and "mixed" otherwise. The pair
figure is the median |cos| between the copy's --kind left vector and its
down_proj left vector (o_proj when --kind is down_proj) of the same layer,
over the layers carrying both, and none when no layer carries both. The
markdown goes to --out and the same stem with .json beside it.
"""

import argparse
import json
import statistics
from pathlib import Path

from direction_layers import find_file, load_layers, place

ONE_DIRECTION = 0.9
PER_LAYER_ADJACENT = 0.5
PER_LAYER_FAR = 0.2
ARBITRARY_ADJACENT = 0.2

MODES = ('per layer', 'one direction', 'arbitrary rank', 'mixed', 'few layers', 'no file')
WORDS = ('heretic', 'abliterated', 'uncensored', 'other')


def mode_of(layers, figures):
    """Return the edit mode of a copy from its layer count and own figures."""
    if layers < 3:
        return 'few layers'
    far = figures['far']
    if (far is not None and far >= ONE_DIRECTION) or (
            far is None and figures['own_spread'] is not None
            and figures['own_spread'] >= ONE_DIRECTION):
        return 'one direction'
    adjacent = figures['adjacent']
    if adjacent is not None and adjacent >= PER_LAYER_ADJACENT and (
            far is None or far <= PER_LAYER_FAR):
        return 'per layer'
    if adjacent is not None and adjacent < ARBITRARY_ADJACENT:
        return 'arbitrary rank'
    return 'mixed'


def pair_of(vectors, other):
    """Return the median |cos| between same-layer vectors of two kinds, else None."""
    values = []
    for layer, vector in vectors.items():
        if layer not in other:
            continue
        a = vector.double().flatten()
        b = other[layer].double().flatten()
        norm = float(a.norm() * b.norm())
        if norm == 0.0:
            continue
        values.append(abs(float(a @ b)) / norm)
    return statistics.median(values) if values else None


def name_word(repo):
    """Return the name word of a copy repo."""
    name = repo.lower()
    if 'heretic' in name:
        return 'heretic'
    if 'abliterat' in name:
        return 'abliterated'
    if 'uncensor' in name:
        return 'uncensored'
    return 'other'


def family_numbers(families):
    """Return {(parent, member): per-parent 1-based family index} in families.json order."""
    numbers = {}
    seen = {}
    for family in families:
        parent = family.get('parent')
        seen[parent] = seen.get(parent, 0) + 1
        for member in family.get('members', []):
            numbers.setdefault((parent, member), seen[parent])
    return numbers


def family_of(numbers, parent, repo):
    """Return the 1-based family index under the parent holding the repo, else 'none'."""
    return numbers.get((parent, repo), 'none')


def read_census(folder, out=None):
    """Return [(parent, copies)] for every census file with a copies list.

    A census group file has a string parent and copies that all carry repo,
    pull and pair. The command's own output (the --out stem plus .json) sits
    in the same folder and is skipped, as is any file whose copies list is
    empty or whose first copy lacks pull or pair.
    """
    skip = set()
    if out is not None:
        skip.add(Path(out).stem + '.json')
    groups = []
    for path in sorted(Path(folder).glob('*.json')):
        if path.name == 'families.json' or path.name in skip:
            continue
        try:
            document = json.loads(path.read_text())
        except (OSError, ValueError):
            continue
        if not isinstance(document, dict) or not isinstance(document.get('copies'), list):
            continue
        copies = document['copies']
        if not copies or not isinstance(copies[0], dict):
            continue
        if 'pull' not in copies[0] or 'pair' not in copies[0]:
            continue
        groups.append((document.get('parent'), copies))
    return groups


def three(value):
    return 'none' if value is None else f'{value:.3f}'


def write_markdown(path, rows, counts, by_name, family_rows):
    total = sum(counts.values())
    lines = [
        f'# {path.stem} -- every census copy sorted into an edit mode by how its own '
        'directions rotate with depth.',
        '',
        f"copies {total}: " + ', '.join(f'{mode} {counts[mode]}' for mode in MODES),
        '',
        '| mode | heretic | abliterated | uncensored | other | total |',
        '| --- | --- | --- | --- | --- | --- |',
    ]
    for mode in MODES:
        lines.append(f"| {mode} | " + ' | '.join(str(by_name[mode][word]) for word in WORDS)
                     + f' | {counts[mode]} |')
    lines.append('| total | ' + ' | '.join(str(sum(by_name[mode][word] for mode in MODES))
                                           for word in WORDS) + f' | {total} |')
    lines += [
        '',
        '| parent | family | members | per layer | one direction | arbitrary rank '
        '| mixed | few layers |',
        '| --- | --- | --- | --- | --- | --- | --- | --- |',
    ]
    for row in family_rows:
        lines.append(f"| {row['parent']} | {row['family']} | {row['members']} | "
                     + ' | '.join(str(row['counts'][mode]) for mode in MODES[:5]) + ' |')
    lines += [
        '',
        '| parent | copy | layers | window | own spread | adjacent | far | pair | mode | family |',
        '| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |',
    ]
    for row in rows:
        window = 'none' if row['window'] is None else f"{row['window'][0]}..{row['window'][1]}"
        lines.append(
            f"| {row['parent']} | {row['repo']} | {row['layers']} | {window} "
            f"| {three(row['own_spread'])} | {three(row['adjacent'])} | {three(row['far'])} "
            f"| {three(row['pair'])} | {row['mode']} | {row['family']} |")
    path.write_text('\n'.join(lines) + '\n')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--directions', required=True,
                        help='census folder of <parent id>.json files with parent and copies[]')
    parser.add_argument('--pulls', nargs='+', required=True,
                        help='pull roots holding <pull>/measurements/pair-<pair> folders')
    parser.add_argument('--families', help='families.json with families[] {parent, members[]}')
    parser.add_argument('--kind', default='o_proj', help='tensor-name suffix (default o_proj)')
    parser.add_argument('--out', required=True, help='output markdown file')
    args = parser.parse_args(argv)

    families = []
    if args.families:
        families = json.loads(Path(args.families).read_text()).get('families', [])
    numbers = family_numbers(families)
    other_kind = 'down_proj' if args.kind == 'o_proj' else 'o_proj'

    rows = []
    seen = set()
    for parent, copies in read_census(args.directions, args.out):
        for copy in copies:
            repo = copy.get('repo')
            if repo is None or (parent, repo) in seen:
                continue
            seen.add((parent, repo))
            path = find_file(args.pulls, copy)
            vectors = load_layers(path, args.kind) if path else {}
            other = load_layers(path, other_kind) if path else {}
            row = {'parent': parent, 'repo': repo, 'layers': len(vectors),
                   'window': None, 'own_spread': None, 'adjacent': None, 'far': None,
                   'pair': pair_of(vectors, other),
                   'mode': 'no file', 'family': family_of(numbers, parent, repo)}
            if vectors:
                figures = place(vectors, {})
                row.update({key: figures[key]
                            for key in ('window', 'own_spread', 'adjacent', 'far')})
                row['mode'] = mode_of(len(vectors), figures)
            rows.append(row)
    rows.sort(key=lambda r: (str(r['parent']), r['repo']))

    counts = {mode: 0 for mode in MODES}
    by_name = {mode: {word: 0 for word in WORDS} for mode in MODES}
    for row in rows:
        counts[row['mode']] += 1
        by_name[row['mode']][name_word(row['repo'])] += 1

    family_rows = []
    for family in families:
        parent = family.get('parent')
        members = family.get('members', [])
        measured = [row for row in rows if row['parent'] == parent and row['repo'] in members]
        family_counts = {mode: 0 for mode in MODES}
        for row in measured:
            family_counts[row['mode']] += 1
        index = numbers.get((parent, members[0])) if members else 'none'
        family_rows.append({'parent': parent, 'family': index, 'members': len(measured),
                            'counts': family_counts})

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    write_markdown(out, rows, counts, by_name, family_rows)
    document = {
        'counts': counts,
        'by_name': by_name,
        'families': family_rows,
        'copies': rows,
    }
    out.with_suffix('.json').write_text(json.dumps(document, indent=1) + '\n')
    print(f'{out.name} {out.stat().st_size}')
    print(f"copies {len(rows)}: " + ', '.join(f'{mode} {counts[mode]}' for mode in MODES))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
