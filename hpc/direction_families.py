# direction_families.py -- Turn the per-parent comparison files into census-wide tables of agreement, families and name classes.
# Created by SDE
# Modified: SDE 2026-11-03  first pass: counts, distribution, per parent, families, classes, single-direction rows, sign note.
"""Turn the per-parent comparison files into census-wide tables.

Each file under --directions is one parent group written by direction_cosines:
the copies under the parent and one row per compared pair, with the right and
left cosines per shared key. A row's agreement is the median of its absolute
right cosines. The report gives the counts, the agreement distribution, a table
per parent, the families of copies joined by rows at 0.9 or more, a table by
name class, the same figures restricted to rows whose keys sit on tensors that
one direction carries, and the rows whose signed and absolute medians differ.
The report is written as OUT.md and the same figures as OUT.json.
"""

import argparse
import collections
import json
import statistics
from pathlib import Path

HIGH = 0.9
LOW = 0.2
SINGLE = 0.5
ENERGY = 0.9
MIN_KEYS = 3
BINS = 10


def name_class(repo):
    """Return the name class of a copy repo."""
    name = repo.lower()
    if 'heretic' in name:
        return 'heretic'
    if 'abliterat' in name:
        return 'abliterated'
    if 'uncensored' in name:
        return 'uncensored'
    return 'other'


def tensor_name(key):
    """Return the tensor name of a directions key."""
    return key.rsplit('.', 1)[0]


def median(values):
    """Return the median of a list, or None when it is empty."""
    return statistics.median(values) if values else None


def bin_index(value):
    """Return the 0.1 bin of an agreement value, 0 to 9."""
    at = int(value * BINS)
    return min(max(at, 0), BINS - 1)


def distribution(values):
    """Return the ten-bin counts of agreement values."""
    counts = [0] * BINS
    for value in values:
        counts[bin_index(value)] += 1
    return counts


def load_directions(folder):
    """Return the parent groups read from every json file in a folder."""
    groups = []
    for path in sorted(Path(folder).glob('*.json')):
        with open(path) as handle:
            groups.append(json.load(handle))
    return groups


def load_weights(folder):
    """Return the changed-tensor energy shares by report file stem, skipping absent ones."""
    reports = {}
    if folder is None:
        return reports
    for path in sorted(Path(folder).glob('*.json')):
        with open(path) as handle:
            report = json.load(handle)
        reports[path.stem] = {
            name: entry.get('first_singular_energy_share')
            for name, entry in (report.get('tensors') or {}).items()
            if entry.get('changed')
        }
    return reports


def rows_of(groups):
    """Return the rows of every group with their parent and agreement."""
    rows = []
    for group in groups:
        parent = group.get('parent')
        for row in group.get('comparisons', []):
            cosines = [abs(value) for _, value in (row.get('right') or {}).get('cosines', [])]
            rows.append({
                'parent': parent,
                'copy_a': row.get('copy_a'),
                'copy_b': row.get('copy_b'),
                'right': (row.get('right') or {}).get('cosines', []),
                'agreement': median(cosines),
            })
    return rows


def copies_of(groups):
    """Return the copies of every group as (parent, repo) pairs."""
    copies = []
    for group in groups:
        for copy in group.get('copies', []):
            copies.append((group.get('parent'), copy.get('repo')))
    return copies


def components(repos, edges):
    """Return the connected components of repos joined by edges, largest first."""
    parent = {repo: repo for repo in repos}

    def find(repo):
        while parent[repo] != repo:
            parent[repo] = parent[parent[repo]]
            repo = parent[repo]
        return repo

    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
    groups = collections.defaultdict(list)
    for repo in repos:
        groups[find(repo)].append(repo)
    sizes = [sorted(members) for members in groups.values() if len(members) > 1]
    return sorted(sizes, key=lambda members: (-len(members), members))


def parent_table(groups, rows):
    """Return the per-parent figures."""
    table = []
    for group in groups:
        parent = group.get('parent')
        repos = [copy.get('repo') for copy in group.get('copies', [])]
        mine = [row for row in rows if row['parent'] == parent and row['agreement'] is not None]
        edges = [(row['copy_a'], row['copy_b']) for row in mine if row['agreement'] >= HIGH]
        alone = sorted(repo for repo in repos
                       if not any(row['agreement'] >= SINGLE and repo in (row['copy_a'], row['copy_b'])
                                  for row in mine))
        table.append({
            'parent': parent,
            'copies': len(repos),
            'rows': len(mine),
            'median': median([row['agreement'] for row in mine]),
            'high': sum(1 for row in mine if row['agreement'] >= HIGH),
            'low': sum(1 for row in mine if row['agreement'] < LOW),
            'families': components(repos, edges),
            'alone': alone,
        })
    return table


def class_table(rows):
    """Return the figures per unordered class pair over rows with an agreement."""
    pairs = collections.defaultdict(list)
    for row in rows:
        if row['agreement'] is None:
            continue
        a = name_class(row['copy_a'])
        b = name_class(row['copy_b'])
        pairs[tuple(sorted((a, b)))].append(row['agreement'])
    table = []
    for (a, b), values in sorted(pairs.items()):
        table.append({
            'class_a': a,
            'class_b': b,
            'rows': len(values),
            'median': median(values),
            'high': sum(1 for value in values if value >= HIGH),
            'low': sum(1 for value in values if value < LOW),
        })
    return table


def single_rows(rows, reports):
    """Return the rows kept by the single-direction restriction and the drop counts."""
    kept = []
    missing = 0
    few = 0
    for row in rows:
        if row['agreement'] is None:
            continue
        share_map_a = reports.get(row['copy_a'].replace('/', '-'))
        share_map_b = reports.get(row['copy_b'].replace('/', '-'))
        if share_map_a is None or share_map_b is None:
            missing += 1
            continue
        values = []
        for key, value in row['right']:
            name = tensor_name(key)
            shares = []
            for share_map in (share_map_a, share_map_b):
                shares.append(share_map.get(name))
            if all(share is not None and share >= ENERGY for share in shares):
                values.append(abs(value))
        if len(values) < MIN_KEYS:
            few += 1
            continue
        kept.append(dict(row, agreement=median(values)))
    return kept, missing, few


def sign_rows(rows):
    """Return the rows whose signed and absolute medians differ by more than 0.5."""
    found = []
    for row in rows:
        signed = median([value for _, value in row['right']])
        absolute = median([abs(value) for _, value in row['right']])
        if signed is None or absolute is None:
            continue
        if abs(signed - absolute) > 0.5:
            found.append(row)
    return found


def build(groups, reports):
    """Return the report figures as nested objects."""
    rows = rows_of(groups)
    copies = copies_of(groups)
    measured = [row for row in rows if row['agreement'] is not None]
    skipped = len(rows) - len(measured)
    repos = sorted({repo for _, repo in copies})
    missing = sum(1 for repo in repos if repo.replace('/', '-') not in reports)
    pooled = [abs(value) for row in measured for _, value in row['right']]
    kept, drop_missing, drop_few = single_rows(rows, reports)
    signs = sign_rows(measured)
    return {
        'counts': {
            'parents': len(groups),
            'copies': len(copies),
            'rows': len(rows),
            'skipped': skipped,
            'reports_missing': missing,
        },
        'distribution': {
            'bins': distribution([row['agreement'] for row in measured]),
            'keys': len(pooled),
            'median': median(pooled),
            'mean': statistics.fmean(pooled) if pooled else None,
            'under_low': (sum(1 for value in pooled if value < 0.1) / len(pooled)) if pooled else None,
            'over_high': (sum(1 for value in pooled if value > HIGH) / len(pooled)) if pooled else None,
        },
        'parents': parent_table(groups, rows),
        'families': [
            {'parent': entry['parent'], 'members': members}
            for entry in parent_table(groups, rows)
            for members in entry['families']
        ],
        'classes': class_table(measured),
        'single': {
            'kept': len(kept),
            'drop_missing': drop_missing,
            'drop_few': drop_few,
            'bins': distribution([row['agreement'] for row in kept]),
            'high': sum(1 for row in kept if row['agreement'] >= HIGH),
            'low': sum(1 for row in kept if row['agreement'] < LOW),
            'classes': class_table(kept),
        },
        'sign': {
            'count': len(signs),
            'rows': ['%s ~ %s' % (row['copy_a'], row['copy_b']) for row in signs[:10]],
        },
    }


def number(value):
    """Return a figure as text."""
    if value is None:
        return '-'
    if isinstance(value, float):
        return '%.3f' % value
    return str(value)


def render(report):
    """Return the markdown report."""
    counts = report['counts']
    dist = report['distribution']
    lines = ['# Direction families', '']
    lines.append('## Counts')
    lines.append('')
    lines.append('| parents | copies | rows | rows skipped | weights reports missing |')
    lines.append('| --- | --- | --- | --- | --- |')
    lines.append('| %d | %d | %d | %d | %d |' % (
        counts['parents'], counts['copies'], counts['rows'],
        counts['skipped'], counts['reports_missing']))
    lines.append('')
    lines.append('## Distribution')
    lines.append('')
    lines.append('| bin | rows |')
    lines.append('| --- | --- |')
    for at, count in enumerate(dist['bins']):
        lines.append('| %.1f to %.1f | %d |' % (at / BINS, (at + 1) / BINS, count))
    lines.append('')
    lines.append('Pooled per-key |cosine|: %d keys, median %s, mean %s, under 0.1 %s, over 0.9 %s.' % (
        dist['keys'], number(dist['median']), number(dist['mean']),
        number(dist['under_low']), number(dist['over_high'])))
    lines.append('')
    lines.append('## Per parent')
    lines.append('')
    lines.append('| parent | copies | rows | median agreement | at 0.9 or more | under 0.2 | families at 0.9 | alone at 0.5 |')
    lines.append('| --- | --- | --- | --- | --- | --- | --- | --- |')
    for entry in report['parents']:
        families = '; '.join('%d: %s' % (len(members), ', '.join(members)) for members in entry['families']) or '-'
        alone = ', '.join(entry['alone']) or '-'
        lines.append('| %s | %d | %d | %s | %d | %d | %s | %s |' % (
            entry['parent'], entry['copies'], entry['rows'], number(entry['median']),
            entry['high'], entry['low'], families, alone))
    lines.append('')
    lines.append('## Families')
    lines.append('')
    if report['families']:
        for entry in report['families']:
            lines.append('- %s: %s' % (entry['parent'], ', '.join(entry['members'])))
    else:
        lines.append('No family of two or more at 0.9.')
    lines.append('')
    lines.append('## By name class')
    lines.append('')
    lines.append('| class pair | rows | median agreement | at 0.9 or more | under 0.2 |')
    lines.append('| --- | --- | --- | --- | --- |')
    for entry in report['classes']:
        lines.append('| %s - %s | %d | %s | %d | %d |' % (
            entry['class_a'], entry['class_b'], entry['rows'],
            number(entry['median']), entry['high'], entry['low']))
    lines.append('')
    single = report['single']
    lines.append('## Single-direction restriction')
    lines.append('')
    lines.append('Rows kept %d, dropped for a missing report %d, dropped for fewer than %d keys %d.' % (
        single['kept'], single['drop_missing'], MIN_KEYS, single['drop_few']))
    lines.append('')
    lines.append('| bin | rows |')
    lines.append('| --- | --- |')
    for at, count in enumerate(single['bins']):
        lines.append('| %.1f to %.1f | %d |' % (at / BINS, (at + 1) / BINS, count))
    lines.append('')
    lines.append('Rows at 0.9 or more %d, rows under 0.2 %d.' % (single['high'], single['low']))
    lines.append('')
    lines.append('| class pair | rows | median agreement | at 0.9 or more | under 0.2 |')
    lines.append('| --- | --- | --- | --- | --- |')
    for entry in single['classes']:
        lines.append('| %s - %s | %d | %s | %d | %d |' % (
            entry['class_a'], entry['class_b'], entry['rows'],
            number(entry['median']), entry['high'], entry['low']))
    lines.append('')
    lines.append('## Sign note')
    lines.append('')
    lines.append('Rows whose signed and absolute medians differ by more than 0.5: %d.' % report['sign']['count'])
    lines.append('')
    for text in report['sign']['rows']:
        lines.append('- %s' % text)
    lines.append('')
    return '\n'.join(lines)


def main(argv=None):
    """Write the report and its json, print the two names with sizes."""
    parser = argparse.ArgumentParser(description='Turn the per-parent comparison files into census-wide tables.')
    parser.add_argument('--directions', required=True, help='folder of per-parent comparison json files')
    parser.add_argument('--weights', default=None, help='folder of per-copy weights reports')
    parser.add_argument('--out', required=True, help='markdown report path; the json takes the same stem')
    args = parser.parse_args(argv)
    groups = load_directions(args.directions)
    if not groups:
        return 1
    reports = load_weights(args.weights)
    report = build(groups, reports)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(report))
    side = out.with_suffix('.json')
    side.write_text(json.dumps(report, indent=2) + '\n')
    for path in (out, side):
        print('%s %d' % (path, path.stat().st_size))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
