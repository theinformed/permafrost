# population.py -- Rebuild the census population counts from the weights reports, so no sum is carried by hand.
# Created by SDE
"""Read the weights reports under a root and count the census population.

Every report in <root>/results/weights/*.json becomes one row. A row with a
census block for the modified model is a measurement of a copy; a row without
one (a calibration report) is a report only. The counts follow the rules in
the population header of docs/findings.md.
"""

import argparse
import json
import re
from pathlib import Path

ROUND = re.compile(r'/rounds/(\d+)/')

TABLE_COLUMNS = ('file', 'round', 'copy', 'original', 'publisher', 'outside_max',
                 'assessment', 'nearest_recipe', 'matched', 'energy_share', 'changed',
                 'same_weights_as', 'duplicate_of')


def _get(data, *keys):
    """Walk nested dicts, returning None as soon as a key is missing."""
    for key in keys:
        if not isinstance(data, dict):
            return None
        data = data.get(key)
    return data


def _round_of(source):
    if not isinstance(source, str):
        return None
    found = ROUND.search(source)
    return int(found.group(1)) if found else None


def _row(path):
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
    except (OSError, ValueError):
        data = {}
    if not isinstance(data, dict):
        data = {}
    changed_set = _get(data, 'summary', 'changed_set')
    same = _get(data, 'census', 'modified', 'same_weights_as')
    return {
        'file': path.name,
        'round': _round_of(_get(data, 'original', 'source')),
        'copy': _get(data, 'census', 'modified', 'hub_id'),
        'revision': _get(data, 'census', 'modified', 'revision'),
        'original': _get(data, 'census', 'original', 'hub_id'),
        'outside_max': _get(data, 'summary', 'max_relative_difference_outside_changed_set'),
        'assessment': _get(data, 'summary', 'assessment'),
        'nearest_recipe': _get(data, 'recipe_matching', 'nearest_recipe'),
        'matched': _get(data, 'recipe_matching', 'matched'),
        'energy_share': _get(data, 'summary', 'min_first_singular_energy_share'),
        'changed': len(changed_set) if isinstance(changed_set, list) else None,
        'same_weights_as': _get(same, 'hub_id'),
        'duplicate_of': _get(data, 'census', 'modified', 'duplicate_of'),
    }


def reports(root):
    """One row per weights report under root, sorted by file name."""
    folder = Path(root) / 'results' / 'weights'
    if not folder.is_dir():
        return []
    return [_row(path) for path in sorted(folder.glob('*.json'), key=lambda p: p.name)]


def publishers(path):
    """The publisher organisations, lower case, from a one-name-per-line list."""
    names = set()
    for line in Path(path).read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if line and not line.startswith('#'):
            names.add(line.lower())
    return names


def is_publisher(row, publishers):
    """True when the original's organisation is in the publisher set."""
    original = row.get('original')
    if not original:
        return False
    return original.split('/', 1)[0].lower() in publishers


def counts(rows, publishers):
    """The population counts, following the rules in the header."""
    measurements = [r for r in rows if r.get('copy')]
    copies = {r['copy'] for r in measurements}
    original_ids = {r['original'] for r in rows if r.get('original')}
    publisher_ids = {o for o in original_ids if o.split('/', 1)[0].lower() in publishers}
    community_ids = original_ids - publisher_ids
    community_copies = {r['copy'] for r in measurements
                        if r.get('original') and r['original'] in community_ids}
    return {
        'reports': len(rows),
        'measurements': len(measurements),
        'distinct_copies': len(copies),
        'repeated_measurements': len(measurements) - len(copies),
        'originals': len(publisher_ids),
        'community_parents': len(community_ids),
        'copies_on_community_parents': len(community_copies),
        're_uploads': sum(1 for r in measurements if r.get('same_weights_as')),
        'exactly_zero_outside': sum(1 for r in measurements if r.get('outside_max') == 0),
        'without_census_block': sum(1 for r in rows if not r.get('copy')),
        'original_ids': sorted(publisher_ids),
        'community_parent_ids': sorted(community_ids),
    }


def _cell(value):
    if value is None:
        return '-'
    if isinstance(value, bool):
        return 'true' if value else 'false'
    return str(value)


def main(argv=None):
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description='Rebuild the census population counts from the weights reports.')
    parser.add_argument('--root', default=str(here.parent), help='repository root holding results/weights')
    parser.add_argument('--publishers', default=None, help='publisher list (default: data/publishers.txt under the root)')
    parser.add_argument('--table', action='store_true', help='print one row per report instead of the counts')
    args = parser.parse_args(argv)

    root = Path(args.root)
    publisher_path = Path(args.publishers) if args.publishers else root / 'data' / 'publishers.txt'
    names = publishers(publisher_path)
    rows = reports(root)

    if args.table:
        print('\t'.join(TABLE_COLUMNS))
        for row in rows:
            values = dict(row, publisher=is_publisher(row, names))
            print('\t'.join(_cell(values.get(column)) for column in TABLE_COLUMNS))
        return 0

    for key, value in counts(rows, names).items():
        if isinstance(value, list):
            value = ', '.join(value)
        print(f'{key}\t{value}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
