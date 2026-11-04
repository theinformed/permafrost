# round_readout.py -- Write one census round's read-out table: each pair's weight change, mode and placement, then the census change.
# Created by LT Sean Egan, PhD
# Modified: SDE 2026-11-04  first pass: the pairs table from the per-pair weight reports, the mode and placement cells, the census change.
"""Write one census round's read-out table.

--measurements names a folder of pair-1..pair-N folders; --batch names a json
whose pairs[i-1] gives pair-i's modified.hub_id and original.hub_id. Each
pair's changed tensor count, changed layer count and minimum first singular
energy share come only from its weights.json. The mode cell comes from
--modes (copies[] of {repo, parent, mode}) and the placement cell from
--placement (rows[] of {copy, family, median, note} and skipped[] of a string
or {copy, reason}). The census change section compares --before and --modes
counts and copies. The markdown goes to --out.
"""

import argparse
import json
import re
from pathlib import Path

LAYER = re.compile(r'layers\.(\d+)\.')

MISSING = 'missing'
ONLY_COPY = 'only copy of its parent'
NOT_PLACED = 'not placed'


def load(path):
    return json.loads(Path(path).read_text())


def pair_folders(folder, count):
    """Return the pair-i folders in numeric order."""
    return [Path(folder) / f'pair-{index}' for index in range(1, count + 1)]


def weight_cells(folder):
    """Return the changed tensors, changed layers and singular share cells."""
    path = Path(folder) / 'weights.json'
    if not path.is_file():
        return MISSING, MISSING, MISSING
    report = load(path)
    tensors = report.get('tensors') or {}
    changed = [name for name, record in tensors.items()
               if isinstance(record, dict) and record.get('changed') is True]
    layers = set()
    for name in changed:
        match = LAYER.search(name)
        if match:
            layers.add(int(match.group(1)))
    share = (report.get('summary') or {}).get('min_first_singular_energy_share')
    share_cell = 'n/a' if share is None else f'{share:.3f}'
    return str(len(changed)), str(len(layers)), share_cell


def find_copy(copies, repo, parent):
    """Return the copy row matched on repo and parent, else on repo alone, else None."""
    for copy in copies:
        if copy.get('repo') == repo and copy.get('parent') == parent:
            return copy
    for copy in copies:
        if copy.get('repo') == repo:
            return copy
    return None


def mode_cell(copies, repo, parent):
    copy = find_copy(copies, repo, parent)
    if copy is None:
        return ONLY_COPY
    mode = copy.get('mode')
    return 'no file' if mode == 'no file' else str(mode)


def placement_cell(placement, repo):
    for row in placement.get('rows') or []:
        if row.get('copy') != repo:
            continue
        text = str(row.get('family'))
        median = row.get('median')
        if median is not None:
            text += f' median {median:.3f}'
        note = row.get('note')
        if note:
            text += f' ({note})'
        return text
    for entry in placement.get('skipped') or []:
        if isinstance(entry, str):
            continue
        if entry.get('copy') == repo:
            return str(entry.get('reason'))
    return NOT_PLACED


def counts_line(label, counts):
    return f"{label}: " + ', '.join(f'{name} {value}' for name, value in counts.items())


def census_change(before, modes, pairs):
    """Return the census change lines."""
    lines = [
        counts_line('Before', before.get('counts') or {}),
        counts_line('After', modes.get('counts') or {}),
        'Mode changes:',
    ]
    changes = []
    for copy in modes.get('copies') or []:
        old = find_copy(before.get('copies') or [], copy.get('repo'), copy.get('parent'))
        if old is None:
            continue
        if old.get('mode') != copy.get('mode'):
            changes.append(f"- {copy.get('repo')}: {old.get('mode')} -> {copy.get('mode')}")
    lines += changes or ['none']
    lines.append('New copies:')
    new = []
    for copy in modes.get('copies') or []:
        if find_copy(before.get('copies') or [], copy.get('repo'), copy.get('parent')) is None:
            new.append(f"- {copy.get('repo')} ({copy.get('parent')}): {copy.get('mode')}")
    lines += new or ['none']
    unrowed = sum(1 for pair in pairs
                  if find_copy(modes.get('copies') or [], pair['modified'],
                               pair['original']) is None)
    lines.append(f'Pairs here with no census row: {unrowed}')
    return lines


def write_markdown(path, number, rows, change_lines):
    lines = [
        f'# Round {number} read-out',
        '',
        '## Pairs',
        '',
        '| pair | modified | parent | changed tensors | changed layers '
        '| min singular share | mode | placement |',
        '| --- | --- | --- | --- | --- | --- | --- | --- |',
    ]
    for row in rows:
        lines.append(
            f"| {row['pair']} | {row['modified']} | {row['original']} "
            f"| {row['tensors']} | {row['layers']} | {row['share']} "
            f"| {row['mode']} | {row['placement']} |")
    lines += ['', '## Census change', ''] + change_lines
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('\n'.join(lines) + '\n')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--measurements', required=True,
                        help='folder of pair-1..pair-N measurement folders')
    parser.add_argument('--batch', required=True,
                        help='json whose pairs[i-1] names pair-i')
    parser.add_argument('--placement', required=True,
                        help='json with rows[] and skipped[]')
    parser.add_argument('--modes', required=True,
                        help='json with copies[] and counts')
    parser.add_argument('--before', required=True,
                        help='json with copies[] and counts for the earlier census')
    parser.add_argument('--round', required=True, type=int, help='round number')
    parser.add_argument('--out', required=True, help='output markdown file')
    args = parser.parse_args(argv)

    batch = load(args.batch)
    modes = load(args.modes)
    placement = load(args.placement)
    before = load(args.before)
    copies = modes.get('copies') or []

    pairs = []
    for index, entry in enumerate(batch.get('pairs') or [], start=1):
        pairs.append({'pair': index,
                      'modified': entry.get('modified', {}).get('hub_id'),
                      'original': entry.get('original', {}).get('hub_id')})

    rows = []
    for pair, folder in zip(pairs, pair_folders(args.measurements, len(pairs))):
        tensors, layers, share = weight_cells(folder)
        rows.append({
            'pair': pair['pair'],
            'modified': pair['modified'],
            'original': pair['original'],
            'tensors': tensors,
            'layers': layers,
            'share': share,
            'mode': mode_cell(copies, pair['modified'], pair['original']),
            'placement': placement_cell(placement, pair['modified']),
        })

    write_markdown(args.out, args.round, rows, census_change(before, modes, pairs))
    print(f'{Path(args.out).name} {len(rows)} pairs')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
