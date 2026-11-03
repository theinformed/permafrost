# population.py -- Rebuild the census population counts from the weights reports, so no sum is carried by hand.
# Created by SDE
# Modified: SDE read the early reports without a census block, fold second passes, and count the judged lists.
"""Read the weights reports under a root and count the census population.

Every report in <root>/results/weights/*.json becomes one row. A row names a
copy when its census block gives one, or, for the early reports written before
the census block existed, when its modified source is a hub id; a calibration
report names neither and is a report only. The judged groups are lists under
<root>/data/population/, one hub id per line. The rules are in the section
"How the population is counted" of docs/weights-method.md.
"""

import argparse
import json
import re
from pathlib import Path

ROUND = re.compile(r'/rounds/(\d+)/')

TABLE_COLUMNS = ('file', 'round', 'copy', 'original', 'publisher', 'outside_max',
                 'assessment', 'nearest_recipe', 'matched', 'energy_share', 'changed',
                 'same_weights_as', 'duplicate_of')

# The judged groups, each a list file data/population/<name>.txt.
GROUPS = ('re-uploads', 'not-read', 'differs', 'training', 'parent-files',
          'small-outside', 'instruct-on-pretrained')


def _get(data, *keys):
    """Walk nested dicts, returning None as soon as a key is missing."""
    for key in keys:
        if not isinstance(data, dict):
            return None
        data = data.get(key)
    return data


def _round_of(*sources):
    for source in sources:
        if isinstance(source, str):
            found = ROUND.search(source)
            if found:
                return int(found.group(1))
    return None


def _hub_id(source):
    """A source that is a hub id (owner/name) rather than a cluster path."""
    if isinstance(source, str) and '/' in source and not source.startswith('/'):
        return source
    return None


def _row(path):
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
    except (OSError, ValueError):
        data = {}
    if not isinstance(data, dict):
        data = {}
    changed_set = _get(data, 'summary', 'changed_set')
    same = _get(data, 'census', 'modified', 'same_weights_as')
    modified_source = _get(data, 'modified', 'source')
    original_source = _get(data, 'original', 'source')
    census = isinstance(data.get('census'), dict)
    copy = _get(data, 'census', 'modified', 'hub_id')
    original = _get(data, 'census', 'original', 'hub_id')
    if not census:
        copy = _hub_id(modified_source)
        original = _hub_id(original_source) if copy else None
    return {
        'file': path.name,
        'round': _round_of(original_source, modified_source),
        'copy': copy,
        'revision': _get(data, 'census', 'modified', 'revision'),
        'original': original,
        'census': census,
        'modified_source': modified_source,
        'original_source': original_source,
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


def _measurement_key(row):
    """Two reports over the same two folders are one measurement read twice."""
    if row.get('modified_source') or row.get('original_source'):
        return (row.get('modified_source'), row.get('original_source'))
    return (row['file'],)


def measurements(rows):
    """The first report of each measurement, in file order."""
    seen = {}
    for row in rows:
        if row.get('copy'):
            seen.setdefault(_measurement_key(row), row)
    return list(seen.values())


def first_measurement(rows):
    """Each copy's reading measurement: the report named after the copy, else its first report."""
    chosen = {}
    for row in rows:
        copy = row.get('copy')
        if not copy:
            continue
        own = row['file'] == copy.replace('/', '-') + '.json'
        if copy not in chosen or (own and chosen[copy]['file'] != copy.replace('/', '-') + '.json'):
            chosen[copy] = row
    return chosen


def counts(rows, publishers):
    """The population counts, following the rules in the method section."""
    measured = measurements(rows)
    copies = {r['copy'] for r in measured}
    original_ids = {r['original'] for r in measured if r.get('original')}
    publisher_ids = {o for o in original_ids if o.split('/', 1)[0].lower() in publishers}
    community_ids = original_ids - publisher_ids
    on_community = {r['copy'] for r in measured if r.get('original') in community_ids}
    on_publisher = {r['copy'] for r in measured if r.get('original') in publisher_ids}
    originals_per_copy = {}
    for r in measured:
        originals_per_copy.setdefault(r['copy'], []).append(r.get('original'))
    marked = {r['copy'] for r in measured
              if r.get('duplicate_of') or (r.get('same_weights_as') and r['same_weights_as'] != r['copy'])}
    return {
        'reports': len(rows),
        'measurements': len(measured),
        'second_passes': sum(1 for r in rows if r.get('copy')) - len(measured),
        'distinct_copies': len(copies),
        'repeated_measurements': len(measured) - len(copies),
        'copies_on_two_originals': sum(1 for o in originals_per_copy.values() if len(set(o)) > 1),
        'copies_twice_on_one_original': sum(1 for o in originals_per_copy.values() if len(o) > len(set(o))),
        'originals': len(publisher_ids),
        'community_parents': len(community_ids),
        'copies_on_community_parents': len(on_community),
        'copies_only_on_community_parents': len(on_community - on_publisher),
        're_uploads': len(marked),
        'exactly_zero_outside': sum(1 for r in measured if r.get('outside_max') == 0),
        'without_census_block': sum(1 for r in rows if not r.get('census')),
        'original_ids': sorted(publisher_ids),
        'community_parent_ids': sorted(community_ids),
    }


def groups(folder):
    """The judged lists under folder, as {name: [hub id, ...]}; a missing list is empty."""
    found = {}
    for name in GROUPS:
        path = Path(folder) / f'{name}.txt'
        members = []
        if path.is_file():
            for line in path.read_text(encoding='utf-8').splitlines():
                line = line.strip()
                if line and not line.startswith('#'):
                    members.append(line)
        found[name] = members
    return found


def judged(rows, lists):
    """Counts that combine the reports with the judged lists, and the checks between them."""
    first = first_measurement(rows)
    copies = set(first)
    sets = {name: set(members) for name, members in lists.items()}
    read = copies - sets['not-read']
    matching = read - sets['differs']
    ablations = matching - sets['training'] - sets['parent-files']
    zero = {c for c in matching if first[c].get('outside_max') == 0}
    nonzero = matching - zero
    out = {f'listed_{name}': len(members) for name, members in lists.items()}
    out.update({
        'read': len(read),
        'matching': len(matching),
        'ablations': len(ablations),
        'matching_zero_outside': len(zero),
        'matching_other_nonzero': len(nonzero - sets['small-outside']),
    })
    problems = []
    for name, members in lists.items():
        if len(members) != len(set(members)):
            problems.append(f'{name}: a member is listed twice')
        for member in sorted(set(members) - copies):
            problems.append(f'{name}: {member} is not a measured copy')
    for member in sorted(sets['small-outside'] - nonzero):
        problems.append(f'small-outside: {member} is not a matching copy with a nonzero outside value')
    for name in ('differs', 'training', 'parent-files'):
        for member in sorted(sets[name] & sets['not-read']):
            problems.append(f'{name}: {member} is also in not-read')
    for member in sorted(sets['training'] & sets['parent-files']):
        problems.append(f'training: {member} is also in parent-files')
    out['problems'] = problems
    return out


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
    parser.add_argument('--groups', default=None, help='folder of judged lists (default: data/population under the root)')
    parser.add_argument('--table', action='store_true', help='print one row per report instead of the counts')
    args = parser.parse_args(argv)

    root = Path(args.root)
    publisher_path = Path(args.publishers) if args.publishers else root / 'data' / 'publishers.txt'
    group_path = Path(args.groups) if args.groups else root / 'data' / 'population'
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
    if not group_path.is_dir():
        return 0
    result = judged(rows, groups(group_path))
    problems = result.pop('problems')
    for key, value in result.items():
        print(f'{key}\t{value}')
    for problem in problems:
        print(f'problem\t{problem}')
    return 1 if problems else 0


if __name__ == '__main__':
    raise SystemExit(main())
