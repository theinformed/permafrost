# place_round.py -- Place each new measured copy of a pulled round against the census of saved directions: nearest census copy, its family, and the layer of the parent's reference its direction matches best.
# Created by SDE
# Modified: SDE 2026-11-03  first pass: nearest census copy by median |cos|, family, reference layer placement, markdown and json.
# Modified: SDE 2026-11-03  median |cos| taken over the row's cosines list, not the signed median, so a flipped partner reads 1.000.
# Modified: SDE 2026-11-03  a parent whose census copies all carry one direction reads "<repo> (one direction)" with no best layer.
# Modified: SDE 2026-11-03  the reference is the census copy whose layers rotate per layer (adjacent |cos| >= 0.5, far <= 0.2), largest adjacent minus far; none reads "none (no per-layer copy)".
# Modified: SDE 2026-11-03  --batches reads the pin records; a row at median 0.9999 or more says whether it and its partner carry the same weight files.
# Modified: SDE 2026-11-03  a copy whose o_proj change is noise and whose down_proj change is clear is read from down_proj, as direction_modes does; --weights names the census weight reports and the row says which kind it was read from.
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

--batches names a folder of pin records (round-N-batch-1.json), each with a
pairs[] list whose modified entries carry hub_id and weight_files_sha256 (a
mapping of file name to sha256, or a list of values, null in older records).
Every *.json with a pairs list is read in sorted file order and the last
non-null mapping per hub_id is kept. When a row's partner median is at least
CHECKSUM_MEDIAN the row's checksums field says whether the copy and its partner
carry the same weight files: "same weight files", "different weight files",
"overlapping weight files", or "checksums missing for <copy|partner|both>";
without --batches, or under the median, it reads "none".

--weights names a folder of census weight reports (<repo with '/' as
'-'>.json, as direction_modes writes them) and governs the census copies only.
A copy is read from down_proj instead of the --kind when its o_proj change is
noise (median first_singular_energy_share under OPROJ_NOISE) and its down_proj
change is clear (at least DOWN_CLEAR), the rule direction_modes applies. The
pulled copy is independent of --weights: when <pair folder>/weights.json
exists it is read as that copy's report, with or without --weights. The row's
read from field says which kind was used.
"""

import argparse
import json
import statistics
import sys
from pathlib import Path

from safetensors import safe_open

import direction_cosines
import direction_layers
import direction_modes

PER_LAYER_ADJACENT = 0.5
PER_LAYER_FAR = 0.2
CHECKSUM_MEDIAN = 0.9999

FIELDS = ('copy', 'parent', 'partner', 'median', 'keys', 'family', 'window',
          'own_spread', 'best_layer', 'cos', 'reference', 'read_from',
          'checksums', 'note')


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


def kind_of(report, kind):
    """The kind a copy is read from: down_proj when its o_proj change is noise and its down_proj change is clear."""
    if kind == 'o_proj' and report is not None:
        o_share = direction_modes.share_of(report, 'attention_output')
        down_share = direction_modes.share_of(report, 'feed_forward_down')
        if (o_share is not None and o_share < direction_modes.OPROJ_NOISE
                and down_share is not None and down_share >= direction_modes.DOWN_CLEAR):
            return 'down_proj'
    return kind


def reference_copy(copies, pulls, kind, weights=None):
    """The census copy whose layers rotate per layer; ties go to more layers."""
    best = None
    for copy in copies:
        path = direction_layers.find_file(pulls, copy)
        report = direction_modes.read_report(weights, copy['repo']) if weights else None
        vectors = direction_layers.load_layers(path, kind_of(report, kind)) if path else {}
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
                'reference': 'none', 'checksums': 'none', 'note': note})
    return row


def checksum_values(record):
    """The sha256 values of a pin record's weight_files_sha256, or None."""
    if not isinstance(record, dict):
        return None
    files = record.get('weight_files_sha256')
    if isinstance(files, dict):
        return set(files.values())
    if isinstance(files, list):
        return set(files)
    return None


def read_batches(folder):
    """Map hub_id to its weight-file sha256 set from the pin records.

    Every *.json with a pairs list is read in sorted file order; per hub_id the
    last record with a non-null mapping wins, and a hub_id seen only with null
    mappings maps to None.
    """
    known = {}
    for path in sorted(Path(folder).glob('*.json')):
        try:
            document = json.loads(path.read_text())
        except (OSError, ValueError):
            continue
        if not isinstance(document, dict) or not isinstance(document.get('pairs'), list):
            continue
        for pair in document['pairs']:
            if not isinstance(pair, dict):
                continue
            record = pair.get('modified')
            if not isinstance(record, dict):
                continue
            hub_id = record.get('hub_id')
            if hub_id is None:
                continue
            values = checksum_values(record)
            if values is not None or hub_id not in known:
                known[hub_id] = values
    return known


def checksums_of(copy, partner, batches):
    """Whether the copy and its partner carry the same weight files."""
    if batches is None:
        return 'none'
    mine = batches.get(copy)
    theirs = batches.get(partner)
    if mine is None and theirs is None:
        return 'checksums missing for both'
    if mine is None:
        return 'checksums missing for copy'
    if theirs is None:
        return 'checksums missing for partner'
    if mine == theirs:
        return 'same weight files'
    if mine & theirs:
        return 'overlapping weight files'
    return 'different weight files'


def place_pair(folder, census_dir, families, pulls, kind, batches=None, weights=None):
    copy, parent = direction_cosines.read_metadata(folder)
    weights_path = folder / 'weights.directions.safetensors'
    path = census_dir / f'{direction_cosines.parent_id(parent)}.json'
    if not path.is_file():
        return empty_row(copy, parent, 'new parent')
    document = json.loads(path.read_text())
    copies = census_copies(document)
    in_census = any(c.get('repo') == copy for c in copies)

    new = {'repo': copy, 'parent': parent, 'pull': '', 'pair': '', 'path': weights_path}
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
        if row['median'] >= CHECKSUM_MEDIAN:
            row['checksums'] = checksums_of(copy, partner['repo'], batches)

    reference, reference_vectors = reference_copy(copies, pulls, kind, weights)
    row['reference'] = reference['repo'] if reference is not None else 'none (no per-layer copy)'
    report_path = folder / 'weights.json'
    report = json.loads(report_path.read_text()) if report_path.is_file() else None
    read_from = kind_of(report, kind)
    row['read_from'] = read_from
    vectors = direction_layers.load_layers(weights_path, read_from)
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
        '| best layer | cos | reference | read from | checksums | note |',
        '| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |',
    ]
    for row in rows:
        window = ('none' if row['window'] is None
                  else f"{row['window'][0]}..{row['window'][1]}")
        lines.append(
            f"| {row['copy']} | {row['parent']} | {row['partner'] or 'none'} "
            f"| {three(row['median'])} | {whole(row['keys'])} | {row['family']} "
            f"| {window} | {three(row['own_spread'])} | {whole(row['best_layer'])} "
            f"| {three(row['cos'])} | {row['reference']} | {row['read_from'] or 'none'} "
            f"| {row['checksums']} "
            f"| {row['note']} |")
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
    parser.add_argument('--batches', default=None,
                        help='folder of pin records (round-N-batch-1.json) with pairs[]')
    parser.add_argument('--weights', default=None,
                        help='folder of census weight reports (<repo with / as ->.json)')
    parser.add_argument('--out', required=True, help='output markdown file')
    args = parser.parse_args(argv)

    measurements = Path(args.measurements)
    if not measurements.is_dir():
        print(f'measurements folder {measurements} is missing', file=sys.stderr)
        return 2

    census_dir = Path(args.directions)
    families = json.loads(Path(args.families).read_text()).get('families', [])
    batches = read_batches(args.batches) if args.batches else None

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
            rows.append(place_pair(folder, census_dir, families, args.pulls,
                                   args.kind, batches, args.weights))
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
