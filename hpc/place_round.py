# place_round.py -- Place each new measured copy of a pulled round against the census of saved directions: nearest census copy, its family, and the layer of the parent's reference its direction matches best.
# Created by SDE
# Modified: SDE 2026-11-03  first pass: nearest census copy by median |cos|, family, reference layer placement, markdown and json.
# Modified: SDE 2026-11-03  median |cos| taken over the row's cosines list, not the signed median, so a flipped partner reads 1.000.
# Modified: SDE 2026-11-03  a parent whose census copies all carry one direction reads "<repo> (one direction)" with no best layer.
# Modified: SDE 2026-11-03  the reference is the census copy whose layers rotate per layer (adjacent |cos| >= 0.5, far <= 0.2), largest adjacent minus far; none reads "none (no per-layer copy)".
"""Place the new copies of one pulled round against the census of saved directions.

--measurements names a round's pull: pair-* folders with metadata.json and
weights.directions.safetensors. --directions names the census written by
direction_cosines: <parent id>.json files with parent and copies[] {repo, pull,
pair}. --families names families.json with families[] {parent, members[]}.
Census copies are read from --pulls DIR/<pull>/measurements/pair-<pair>/.

For each new pair folder the copy and parent repos come from metadata.json as
direction_cosines reads them. The parent's census json gives the census copies;
each is compared with the new copy as direction_cosines compares two copies
(median |cos| over shared keys, right side, absolute values) and the best
partner is kept. The family is the 1-based index of the family under the parent
whose members hold the partner. The reference is the census copy of the parent
whose layers rotate per layer: its adjacent-layer median |cos| is at least
PER_LAYER_ADJACENT and its far-pair (ten or more apart) median at most
PER_LAYER_FAR, the largest adjacent minus far winning (ties: more layers); the
new copy is placed against it with direction_layers.place. When no census copy
qualifies there is no reference: the reference reads "none (no per-layer
copy)" and best layer and cos stay none. The markdown goes to
--out and the same stem with .json beside it.
"""

import argparse
import json
import statistics
import sys
from pathlib import Path

from safetensors import safe_open

import direction_cosines
import direction_layers

PER_LAYER_ADJACENT = 0.5
PER_LAYER_FAR = 0.2

FIELDS = ('copy', 'parent', 'partner', 'median', 'keys', 'family', 'window',
          'own_spread', 'best_layer', 'cos', 'reference', 'note')


def census_copies(document):
    """Return the census copies of a parent, each repo once, first listing."""
    seen = set()
    out = []
    for copy in document.get('copies', []):
        repo = copy.get('repo')
        if repo in seen:
            continue
        seen.add(repo)
        out.append(copy)
    return out


def median_abs(copy_a, copy_b):
    """Median |cos| over the shared keys, right side, as direction_cosines compares.

    direction_cosines files a key under the side its name ends with, so the
    right side is the one ending .right; the census copy is passed as copy A
    and the new copy as copy B and the right side is read.
    """
    row = direction_cosines.compare(copy_a, copy_b)
    right = row['right']
    if right['count']:
        return median_abs_of(right), right['count']
    # A directions file holding only left vectors has no right side; the
    # comparison is then read from the left side, still absolute values.
    left = row['left']
    return median_abs_of(left), left['count']


def median_abs_of(side):
    """Median of the absolute values of a side's [key, value] cosines.

    The side's own median is of signed cosines, so a partner whose vectors
    point the other way reads -1.000; the absolute values read 1.000.
    """
    values = [abs(value) for _, value in side['cosines']]
    return statistics.median(abs(value) for value in values) if values else None


def family_of(families, parent, partner):
    index = 0
    for family in families:
        if family.get('parent') != parent:
            continue
        index += 1
        if partner in family.get('members', []):
            return index
    return 'none'


def reference_copy(copies, pulls, kind):
    """The census copy whose layers rotate per layer; ties go to more layers."""
    best = None
    for copy in copies:
        path = direction_layers.find_file(pulls, copy)
        vectors = direction_layers.load_layers(path, kind) if path else {}
        if len(vectors) < 2:
            continue
        rot = direction_layers.rotation(vectors)
        adjacent = rot['adjacent_median']
        far = rot['far_median']
        if adjacent is None or far is None:
            continue
        if adjacent < PER_LAYER_ADJACENT or far > PER_LAYER_FAR:
            continue
        key = (adjacent - far, len(vectors))
        if best is None or key > best[0]:
            best = (key, copy, vectors)
    if best is None:
        return None, {}
    return best[1], best[2]


def empty_row(copy, parent, note):
    row = {field: None for field in FIELDS}
    row.update({'copy': copy, 'parent': parent, 'family': 'none',
                'reference': 'none', 'note': note})
    return row


def place_pair(folder, census_dir, families, pulls, kind):
    copy, parent = direction_cosines.read_metadata(folder)
    weights = folder / 'weights.directions.safetensors'
    path = census_dir / f'{direction_cosines.parent_id(parent)}.json'
    if not path.is_file():
        return empty_row(copy, parent, 'new parent')
    document = json.loads(path.read_text())
    copies = census_copies(document)
    in_census = any(c.get('repo') == copy for c in copies)

    new = {'repo': copy, 'parent': parent, 'pull': '', 'pair': '', 'path': weights}
    partner = None
    best = None
    for candidate in copies:
        found = direction_layers.find_file(pulls, candidate)
        if found is None:
            continue
        other = {'repo': candidate['repo'], 'parent': parent,
                 'pull': candidate['pull'], 'pair': candidate['pair'], 'path': found}
        median, count = median_abs(other, new)
        if median is None:
            continue
        key = (median, count)
        if best is None or key > best[0]:
            best = (key, candidate)

    row = empty_row(copy, parent, 'in census' if in_census else '')
    if best is not None:
        partner = best[1]
        row['partner'] = partner['repo']
        row['median'] = best[0][0]
        row['keys'] = best[0][1]
        row['family'] = family_of(families, parent, partner['repo'])

    reference, reference_vectors = reference_copy(copies, pulls, kind)
    row['reference'] = reference['repo'] if reference is not None else 'none (no per-layer copy)'
    vectors = direction_layers.load_layers(weights, kind)
    if vectors:
        placed = direction_layers.place(vectors, reference_vectors)
        row['window'] = placed['window']
        row['own_spread'] = placed['own_spread']
        if reference is not None and placed['best']:
            row['best_layer'] = placed['best'][0]
            row['cos'] = placed['best'][1]
    return row


def three(value):
    return 'none' if value is None else f'{value:.3f}'


def whole(value):
    return 'none' if value is None else str(int(value))


def write_markdown(path, rows):
    lines = [
        f'# {path.stem} -- new copies placed against the census of saved directions.',
        '',
        '| copy | parent | partner | median | keys | family | window | own spread '
        '| best layer | cos | reference | note |',
        '| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |',
    ]
    for row in rows:
        window = ('none' if row['window'] is None
                  else f"{row['window'][0]}..{row['window'][1]}")
        lines.append(
            f"| {row['copy']} | {row['parent']} | {row['partner'] or 'none'} "
            f"| {three(row['median'])} | {whole(row['keys'])} | {row['family']} "
            f"| {window} | {three(row['own_spread'])} | {whole(row['best_layer'])} "
            f"| {three(row['cos'])} | {row['reference']} | {row['note']} |")
    path.write_text('\n'.join(lines) + '\n')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--measurements', required=True,
                        help="a round's pull: pair-* folders with metadata.json")
    parser.add_argument('--directions', required=True,
                        help='census directory of <parent id>.json files')
    parser.add_argument('--families', required=True, help='families.json')
    parser.add_argument('--pulls', nargs='+', required=True,
                        help='pull roots holding <pull>/measurements/pair-<pair> folders')
    parser.add_argument('--kind', default='o_proj', help='tensor-name suffix (default o_proj)')
    parser.add_argument('--out', required=True, help='output markdown file')
    args = parser.parse_args(argv)

    measurements = Path(args.measurements)
    if not measurements.is_dir():
        print(f'measurements folder {measurements} is missing', file=sys.stderr)
        return 2

    census_dir = Path(args.directions)
    families = json.loads(Path(args.families).read_text()).get('families', [])

    folders = sorted((f for f in measurements.glob('pair-*') if f.is_dir()),
                     key=lambda f: (int(f.name[len('pair-'):])
                                    if f.name[len('pair-'):].isdigit() else float('inf'),
                                    f.name))
    rows = []
    skipped = []
    for folder in folders:
        if not (folder / 'weights.directions.safetensors').is_file():
            skipped.append(folder.name)
            continue
        try:
            rows.append(place_pair(folder, census_dir, families, args.pulls, args.kind))
        except (OSError, ValueError, KeyError, TypeError) as error:
            first = str(error).splitlines()[0] if str(error) else type(error).__name__
            print(f'{folder.name}: {first}', file=sys.stderr)
            skipped.append(folder.name)

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    write_markdown(out, rows)
    document = {'rows': rows, 'skipped': skipped}
    out.with_suffix('.json').write_text(json.dumps(document, indent=1) + '\n')
    print(f'{out.name} {out.stat().st_size}')
    print(f'copies placed {len(rows)}, skipped {len(skipped)}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
