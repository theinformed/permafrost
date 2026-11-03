# mode_sizes.py -- Join each census copy's edit mode with the size of its measured weight change, per mode and per copy.
# Created by LT Sean Egan, PhD
# Modified: SDE 2026-11-03  first pass: per-copy size figures from the weight report, medians per mode, markdown and json.
# Modified: SDE 2026-11-03  quartiles beside the per-mode medians, a per-parent table and the singular-share crossings line.
# Modified: SDE 2026-11-03  a crossings section listing the arbitrary-rank high-share and other-mode low-share copies by name.
"""Join each census copy's edit mode with the size of its measured weight change.

--modes names a json whose copies[] list has rows {parent, repo, layers, mode}.
Each copy's weight report is --weights DIR/<repo with every '/' replaced by
'-'>.json; a copy with no such file is listed with "no report" and skipped
from the medians. From the report, "tensors" maps a tensor name to a record
with "changed" and "relative_difference", and "summary" carries
min_first_singular_energy_share and changed_kinds. Per copy the changed
tensor count, the count of distinct layers among the changed names, the
median and max relative difference over the changed records, the singular
share and the kinds are taken. The markdown goes to --out with a per-mode
table (quartiles beside the medians), a crossings section (the count line,
then the arbitrary-rank copies at singular share 0.9 or more and the
other-mode copies under 0.9, by name), a per-parent table and a per-copy
table, and the same stem with .json beside it.
"""

import argparse
import json
import re
import statistics
from pathlib import Path

LAYER = re.compile(r'layers\.(\d+)\.')


def report_path(folder, repo):
    """Return the weight report path for a copy repo."""
    return Path(folder) / (repo.replace('/', '-') + '.json')


def copy_figures(report):
    """Return the size figures of one weight report."""
    tensors = report.get('tensors') or {}
    summary = report.get('summary') or {}
    changed = [record for record in tensors.values() if record.get('changed')]
    layers = set()
    for name, record in tensors.items():
        if not record.get('changed'):
            continue
        match = LAYER.search(name)
        if match:
            layers.add(int(match.group(1)))
    values = [record.get('relative_difference') for record in changed]
    values = [value for value in values if value is not None]
    kinds = summary.get('changed_kinds') or []
    return {
        'changed_tensors': len(changed),
        'changed_layers': len(layers),
        'median_relative': statistics.median(values) if values else None,
        'max_relative': max(values) if values else None,
        'singular_share': summary.get('min_first_singular_energy_share'),
        'kinds': ', '.join(kinds),
    }


def median_of(values):
    """Return the median of the non-None values, else None."""
    values = [value for value in values if value is not None]
    return statistics.median(values) if values else None


def three(value):
    return 'none' if value is None else f'{value:.3f}'


def quartiles(values):
    """Return the lower and upper quartiles of the non-None values, else (None, None)."""
    values = [value for value in values if value is not None]
    if not values:
        return None, None
    if len(values) < 2:
        return values[0], values[0]
    q1, _, q3 = statistics.quantiles(values, n=4, method='inclusive')
    return q1, q3


def triple(q1, median, q3):
    return f'{three(q1)} / {three(median)} / {three(q3)}'


CROSSING_COLUMNS = ('parent', 'repo', 'mode', 'changed_tensors', 'changed_layers',
                    'singular_share', 'kinds')


def crossing_table(rows):
    """Return the markdown lines of one crossings table, or 'none' when empty."""
    if not rows:
        return ['none']
    lines = [
        '| parent | copy | mode | changed tensors | changed layers | singular share | kinds |',
        '| --- | --- | --- | --- | --- | --- | --- |',
    ]
    for row in rows:
        lines.append(
            f"| {row['parent']} | {row['repo']} | {row['mode']} "
            f"| {three(row['changed_tensors'])} | {three(row['changed_layers'])} "
            f"| {three(row['singular_share'])} | {row['kinds']} |")
    return lines


def write_markdown(path, mode_rows, parent_rows, crossings, crossing_rows, rows):
    lines = [
        f'# {path.stem} -- every census copy joined to the size of its measured weight change.',
        '',
        '| mode | copies | changed tensors (q1 / median / q3) | changed layers '
        '| median relative (q1 / median / q3) | max relative '
        '| singular share (q1 / median / q3) |',
        '| --- | --- | --- | --- | --- | --- | --- |',
    ]
    for mode, figures in mode_rows:
        lines.append(
            f"| {mode} | {figures['copies']} "
            f"| {triple(figures['changed_tensors_q1'], figures['changed_tensors'], figures['changed_tensors_q3'])} "
            f"| {three(figures['changed_layers'])} "
            f"| {triple(figures['median_relative_q1'], figures['median_relative'], figures['median_relative_q3'])} "
            f"| {three(figures['max_relative'])} "
            f"| {triple(figures['singular_share_q1'], figures['singular_share'], figures['singular_share_q3'])} |")
    lines += [
        '',
        crossings,
        '',
        '## crossings',
        '',
        'arbitrary rank copies with singular share 0.9 or more',
        '',
    ]
    lines += crossing_table(crossing_rows['arbitrary_high'])
    lines += [
        '',
        'other-mode copies with singular share under 0.9',
        '',
    ]
    lines += crossing_table(crossing_rows['other_low'])
    lines += [
        '',
        '## per parent',
        '',
        '| parent | mode | copies | changed tensors | median relative | singular share |',
        '| --- | --- | --- | --- | --- | --- |',
    ]
    for row in parent_rows:
        lines.append(
            f"| {row['parent']} | {row['mode']} | {row['copies']} "
            f"| {three(row['changed_tensors'])} | {three(row['median_relative'])} "
            f"| {three(row['singular_share'])} |")
    lines += [
        '',
        '## per copy',
        '',
        '| parent | copy | mode | changed tensors | changed layers | median relative '
        '| max relative | singular share | kinds |',
        '| --- | --- | --- | --- | --- | --- | --- | --- | --- |',
    ]
    for row in rows:
        lines.append(
            f"| {row['parent']} | {row['repo']} | {row['mode']} "
            f"| {three(row['changed_tensors'])} | {three(row['changed_layers'])} "
            f"| {three(row['median_relative'])} | {three(row['max_relative'])} "
            f"| {three(row['singular_share'])} | {row['kinds']} |")
    path.write_text('\n'.join(lines) + '\n')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--modes', required=True,
                        help='json with a copies[] list of {parent, repo, layers, mode}')
    parser.add_argument('--weights', required=True,
                        help='folder of <repo with / as ->.json weight reports')
    parser.add_argument('--out', required=True, help='output markdown file')
    args = parser.parse_args(argv)

    copies = json.loads(Path(args.modes).read_text()).get('copies', [])
    rows = []
    for copy in copies:
        repo = copy.get('repo')
        if repo is None:
            continue
        row = {'parent': copy.get('parent'), 'repo': repo, 'mode': copy.get('mode')}
        path = report_path(args.weights, repo)
        if path.is_file():
            row.update(copy_figures(json.loads(path.read_text())))
        else:
            row.update({'changed_tensors': None, 'changed_layers': None,
                        'median_relative': None, 'max_relative': None,
                        'singular_share': None, 'kinds': 'no report'})
        rows.append(row)
    rows.sort(key=lambda r: (str(r['parent']), r['repo']))

    modes = sorted({row['mode'] for row in rows}, key=str)
    mode_rows = []
    for mode in modes:
        measured = [row for row in rows if row['mode'] == mode and row['kinds'] != 'no report']
        figures = {'copies': len(measured)}
        for key in ('changed_tensors', 'changed_layers', 'median_relative',
                    'max_relative', 'singular_share'):
            figures[key] = median_of([row[key] for row in measured])
        for key in ('changed_tensors', 'median_relative', 'singular_share'):
            q1, q3 = quartiles([row[key] for row in measured])
            figures[key + '_q1'] = q1
            figures[key + '_q3'] = q3
        mode_rows.append((mode, figures))

    parent_rows = []
    pairs = sorted({(str(row['parent']), str(row['mode'])) for row in rows
                    if row['kinds'] != 'no report'})
    for parent, mode in pairs:
        measured = [row for row in rows if str(row['parent']) == parent
                    and str(row['mode']) == mode and row['kinds'] != 'no report']
        parent_rows.append({
            'parent': parent,
            'mode': mode,
            'copies': len(measured),
            'changed_tensors': median_of([row['changed_tensors'] for row in measured]),
            'median_relative': median_of([row['median_relative'] for row in measured]),
            'singular_share': median_of([row['singular_share'] for row in measured]),
        })

    arbitrary = [row for row in rows
                 if row['mode'] == 'arbitrary rank' and row['kinds'] != 'no report']
    other = [row for row in rows
             if row['mode'] != 'arbitrary rank' and row['mode'] != 'no file'
             and row['kinds'] != 'no report']
    crossings = {
        'arbitrary_high_share': sum(1 for row in arbitrary
                                    if row['singular_share'] is not None
                                    and row['singular_share'] >= 0.9),
        'arbitrary_measured': len(arbitrary),
        'other_low_share': sum(1 for row in other
                               if row['singular_share'] is not None
                               and row['singular_share'] < 0.9),
        'other_measured': len(other),
    }
    arbitrary_high = sorted(
        (row for row in arbitrary
         if row['singular_share'] is not None and row['singular_share'] >= 0.9),
        key=lambda r: (str(r['parent']), r['repo']))
    other_low = sorted(
        (row for row in other
         if row['singular_share'] is not None and row['singular_share'] < 0.9),
        key=lambda r: (str(r['mode']), -r['changed_tensors'], r['repo']))
    crossing_rows = {'arbitrary_high': arbitrary_high, 'other_low': other_low}
    crossings['arbitrary_high'] = arbitrary_high
    crossings['other_low'] = other_low
    crossings_line = (
        f"arbitrary rank copies with singular share 0.9 or more: "
        f"{crossings['arbitrary_high_share']} of {crossings['arbitrary_measured']}; "
        f"other-mode copies under 0.9: "
        f"{crossings['other_low_share']} of {crossings['other_measured']}")

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    write_markdown(out, mode_rows, parent_rows, crossings_line, crossing_rows, rows)
    document = {
        'modes': {mode: figures for mode, figures in mode_rows},
        'parents': parent_rows,
        'crossings': crossings,
        'copies': rows,
    }
    out.with_suffix('.json').write_text(json.dumps(document, indent=1) + '\n')
    print(f'{out.name} {out.stat().st_size}')
    print(f"copies {len(rows)}: " + ', '.join(f'{mode} {figures["copies"]}'
                                              for mode, figures in mode_rows))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
