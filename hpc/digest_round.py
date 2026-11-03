# digest_round.py -- Write the per-pair digests a census read-out starts from, so no figure is carried by hand.
# Created by SDE
# Modified: SDE 2026-11-03  first pass: pair, metadata, weights, tensors, directions, oddities, index.
"""Write one digest per measurement pair and an index for the round.

Each pair folder under --measurements holds card.md, metadata.json, receipt.json
and weights.json, with an optional sweep.json beside the pair folders. The
digest reads the hub ids from metadata.json, the job fields from
receipt.json, and the tensor rows from weights.json. Nothing is recomputed; the
digest only lays out what the files carry.
"""

import argparse
import json
import statistics
from pathlib import Path

KIND_SUFFIXES = (
    ('q_proj', 'q_proj'), ('k_proj', 'k_proj'), ('v_proj', 'v_proj'),
    ('o_proj', 'o_proj'), ('gate_proj', 'gate_proj'), ('up_proj', 'up_proj'),
    ('down_proj', 'down_proj'), ('embed', 'embed'), ('norm', 'norm'),
)

KIND_ORDER = ('q_proj', 'k_proj', 'v_proj', 'o_proj', 'gate_proj', 'up_proj',
              'down_proj', 'embed', 'norm', 'other')

SECTIONS = ('## Pair', '## Metadata', '## Weights assessment',
            '## Changed tensors', '## Directions', '## Oddities')

DIFF_CAP = 20
TENSOR_CAP = 30
ODDITY_CAP = 20


def kind_of(name, row):
    kind = row.get('kind')
    if isinstance(kind, str) and kind:
        return kind
    for suffix, label in KIND_SUFFIXES:
        if suffix in name:
            return label
    return 'other'


def layer_of(name):
    parts = name.split('.')
    for i, part in enumerate(parts[:-1]):
        if part == 'layers' and parts[i + 1].isdigit():
            return int(parts[i + 1])
    return None


def fmt(value):
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if isinstance(value, float):
        return f'{value:.4g}'
    return str(value)


def short(value, limit=60):
    text = fmt(value).replace('\n', ' ')
    return text if len(text) <= limit else text[:limit - 3] + '...'


def stats(values):
    if not values:
        return 'n/a'
    return (f'{fmt(min(values))} / {fmt(statistics.median(values))} / '
            f'{fmt(max(values))}')


def load_json(path):
    return json.loads(path.read_text())


def section_pair(pair_no, meta, receipt, sweep):
    lines = ['## Pair']
    for side in ('modified', 'original'):
        block = meta.get(side) or {}
        lines.append(f'- {side}: {block.get("repo", "?")} @ {block.get("sha", "?")}')
    if receipt is None:
        lines.append('- receipt: not carried')
    else:
        sha = str(receipt.get('measurement_sha256') or '')
        lines.append(f'- receipt: pair {receipt.get("pair", "?")}, '
                     f'measurement_sha256 {sha[:8] or "?"}')
        job = receipt.get('job_id') or receipt.get('job_ids')
        node = receipt.get('node')
        seconds = receipt.get('seconds')
        if job is None and sweep is not None:
            job = sweep.get('job_id') or sweep.get('job_ids')
            node = node if node is not None else sweep.get('node')
            seconds = seconds if seconds is not None else sweep.get('seconds')
        if job is None and node is None and seconds is None:
            lines.append('- job, node, seconds: not carried')
        else:
            if isinstance(job, list):
                job = ', '.join(str(j) for j in job)
            lines.append(f'- job {fmt(job)}, node {fmt(node)}, seconds {fmt(seconds)}')
    return lines


def section_metadata(meta, card_headings):
    lines = ['## Metadata']
    lines.append(f'- verdict: {meta.get("verdict", "?")}')
    diffs = meta.get('differences') or []
    classes = {}
    for diff in diffs:
        cls = diff.get('class', '?')
        classes[cls] = classes.get(cls, 0) + 1
    by_class = ', '.join(f'{k} {v}' for k, v in sorted(classes.items())) or 'none'
    lines.append(f'- differences: {len(diffs)} ({by_class})')
    for diff in diffs[:DIFF_CAP]:
        lines.append(f'  - {diff.get("path", "?")}: {short(diff.get("original"))}'
                     f' -> {short(diff.get("modified"))}')
    if len(diffs) > DIFF_CAP:
        lines.append(f'  - and {len(diffs) - DIFF_CAP} more')
    missing = meta.get('missing') or []
    if missing:
        lines.append(f'- missing: {"; ".join(str(m) for m in missing)}')
    limitation = meta.get('limitation')
    if limitation:
        lines.append(f'- limitation: {limitation}')
    lines.append(f'- card headings: {", ".join(card_headings) or "none"}')
    return lines


def section_weights(weights):
    lines = ['## Weights assessment']
    summary = weights.get('summary') or {}
    scalars = []
    for key, value in summary.items():
        if isinstance(value, (dict, list)):
            continue
        scalars.append(f'{key} {fmt(value)}')
    lines.append(f'- summary: {", ".join(scalars) or "none"}')
    lines.append(f'- threshold: {fmt(weights.get("threshold"))}')
    matching = weights.get('recipe_matching') or {}
    lines.append(f'- nearest recipe: {matching.get("nearest_recipe", "?")}, '
                 f'matched {fmt(matching.get("matched"))}')
    for cand in matching.get('candidates') or []:
        count = len(cand.get('violations') or [])
        lines.append(f'  - {cand.get("recipe", "?")}: matched '
                     f'{fmt(cand.get("matched"))}, {count} violations')
    lines.append(f'- schema_version {fmt(weights.get("schema_version"))}; '
                 f'scope: {weights.get("scope", "?")}')
    return lines


def section_tensors(weights):
    lines = ['## Changed tensors']
    tensors = weights.get('tensors') or {}
    groups = {}
    for name, row in tensors.items():
        if not isinstance(row, dict):
            continue
        kind = kind_of(name, row)
        group = groups.setdefault(kind, {'changed': 0, 'total': 0, 'layers': [],
                                         'rel': [], 'share': [], 'positive': [],
                                         'zero': 0})
        group['total'] += 1
        if not row.get('changed'):
            continue
        group['changed'] += 1
        rel = row.get('relative_difference')
        if isinstance(rel, (int, float)):
            group['rel'].append(rel)
            if rel == 0:
                group['zero'] += 1
        layer = layer_of(name)
        if layer is not None:
            group['layers'].append(layer)
        share = row.get('first_singular_energy_share')
        if isinstance(share, (int, float)):
            group['share'].append(share)
        positive = row.get('positive_fraction')
        if isinstance(positive, (int, float)):
            group['positive'].append(positive)
    order = [k for k in KIND_ORDER if k in groups and groups[k]['changed']]
    order += sorted(k for k in groups
                    if k not in KIND_ORDER and groups[k]['changed'])
    quiet = [k for k in KIND_ORDER if k in groups and not groups[k]['changed']]
    quiet += sorted(k for k in groups
                    if k not in KIND_ORDER and not groups[k]['changed'])
    if not order:
        lines.append('- none')
        return lines
    columns = ['kind', 'changed/total', 'layers', 'relative change']
    if any(groups[k]['share'] for k in order):
        columns.append('first share')
    if any(groups[k]['positive'] for k in order):
        columns.append('positive fraction')
    lines.append('| ' + ' | '.join(columns) + ' |')
    lines.append('| ' + ' | '.join('---' for _ in columns) + ' |')
    for kind in order:
        group = groups[kind]
        if group['layers']:
            layers = f'{min(group["layers"])}-{max(group["layers"])}'
        else:
            layers = 'n/a'
        cells = [kind, f'{group["changed"]}/{group["total"]}', layers,
                 stats(group['rel'])]
        if 'first share' in columns:
            cells.append(stats(group['share']))
        if 'positive fraction' in columns:
            cells.append(stats(group['positive']))
        lines.append('| ' + ' | '.join(cells) + ' |')
    if quiet:
        lines.append('- unchanged kinds: ' + ', '.join(
            f'{kind} 0/{groups[kind]["total"]}' for kind in quiet))
    zero_parts = [f'{kind} {groups[kind]["zero"]}' for kind in order
                  if groups[kind]['zero']]
    lines.append(f'- exactly-0 changed tensors: {", ".join(zero_parts) or "none"}')
    if len(lines) > TENSOR_CAP:
        lines = lines[:TENSOR_CAP - 1] + [f'- and {len(lines) - TENSOR_CAP + 1} more lines']
    return lines


def section_directions(weights):
    lines = ['## Directions']
    summary = weights.get('summary') or {}
    agreement = summary.get('direction_agreement') or {}
    groups = agreement.get('groups') or {}
    if groups:
        lines.append('| group | count | median cosine | min cosine | median_direction_defined |')
        lines.append('| --- | --- | --- | --- | --- |')
        for name, group in groups.items():
            lines.append(f'| {name} | {fmt(group.get("count"))} | '
                         f'{fmt(group.get("median_cosine"))} | '
                         f'{fmt(group.get("min_cosine"))} | '
                         f'{fmt(group.get("median_direction_defined"))} |')
    else:
        lines.append('- direction groups: none')
    svd = weights.get('svd')
    if isinstance(svd, dict) and svd:
        lines.append('- svd: ' + ', '.join(f'{k} {fmt(v)}' for k, v in svd.items()))
    counts = []
    for key in ('unused_shared_kv', 'original_only', 'modified_only',
                'dropped_towers', 'dropped_statistics'):
        value = weights.get(key)
        counts.append(f'{key} {len(value) if isinstance(value, (list, dict)) else 0}')
    lines.append('- ' + ', '.join(counts))
    return lines


def section_oddities(weights):
    lines = ['## Oddities']
    tensors = weights.get('tensors') or {}
    found = []
    for name, row in tensors.items():
        if not isinstance(row, dict):
            found.append(f'{name}: row is not an object')
            continue
        rel = row.get('relative_difference')
        if isinstance(rel, (int, float)) and rel > 0.5:
            found.append(f'{name}: layer {fmt(layer_of(name))}, relative change {fmt(rel)}')
        for key, value in row.items():
            if value is None:
                found.append(f'{name}: {key} is null')
            elif isinstance(value, float) and value != value:
                found.append(f'{name}: {key} is NaN')
    seen = {}
    for name in tensors:
        seen[name] = seen.get(name, 0) + 1
    for name, count in seen.items():
        if count > 1:
            found.append(f'{name}: duplicated {count} times')
    by_kind = {}
    for name, row in tensors.items():
        if not isinstance(row, dict) or not row.get('changed'):
            continue
        kind = kind_of(name, row)
        layer = layer_of(name)
        if layer is None:
            continue
        entry = by_kind.setdefault(kind, {})
        entry.setdefault(layer, set()).add(row.get('relative_difference') == 0)
    for kind, layers in by_kind.items():
        if any(len(flags) > 1 for flags in layers.values()):
            found.append(f'{kind}: changed and exactly-0 tensors mixed inside one layer range')
    if not found:
        lines.append('- none')
        return lines
    for item in found[:ODDITY_CAP]:
        lines.append(f'- {item}')
    if len(found) > ODDITY_CAP:
        lines.append(f'- and {len(found) - ODDITY_CAP} more')
    return lines


def digest_pair(pair_no, folder, sweep):
    meta = load_json(folder / 'metadata.json')
    weights = load_json(folder / 'weights.json')
    receipt_path = folder / 'receipt.json'
    receipt = load_json(receipt_path) if receipt_path.exists() else None
    card_path = folder / 'card.md'
    headings = []
    if card_path.exists():
        headings = [line.strip() for line in card_path.read_text().splitlines()
                    if line.startswith('##')]
    lines = [f'# Pair {pair_no} digest', '']
    for section in (section_pair(pair_no, meta, receipt, sweep),
                    section_metadata(meta, headings),
                    section_weights(weights),
                    section_tensors(weights),
                    section_directions(weights),
                    section_oddities(weights)):
        lines.extend(section)
        lines.append('')
    return '\n'.join(lines).rstrip('\n') + '\n'


def headline(weights):
    matching = weights.get('recipe_matching') or {}
    nearest = matching.get('nearest_recipe', '?')
    count = len(matching.get('violations') or [])
    return f'{nearest}, {count} violations'


def write_index(out, rows, sweep):
    lines = ['# Round index', '',
             '| pair | modified hub id | verdict | weights | changed tensors | bytes |',
             '| --- | --- | --- | --- | --- | --- |']
    for row in rows:
        lines.append(f'| {row["pair"]} | {row["hub"]} | {row["verdict"]} | '
                     f'{row["headline"]} | {row["changed"]} | {row["bytes"]} |')
    lines.append('')
    if sweep is None:
        lines.append('- sweep.json absent')
    else:
        parts = []
        for key in ('deleted', 'kept', 'absent'):
            value = sweep.get(key)
            parts.append(f'{key} {len(value) if isinstance(value, list) else 0}')
        lines.append('- sweep: ' + ', '.join(parts))
    path = out / 'index.md'
    path.write_text('\n'.join(lines) + '\n')
    return path


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--measurements', required=True, type=Path)
    parser.add_argument('--out', required=True, type=Path)
    parser.add_argument('--round', required=True, type=int)
    args = parser.parse_args(argv)

    out = args.out
    out.mkdir(parents=True, exist_ok=True)
    sweep_path = args.measurements / 'sweep.json'
    sweep = None
    if sweep_path.exists():
        try:
            sweep = load_json(sweep_path)
        except (OSError, ValueError):
            sweep = None

    folders = sorted((p for p in args.measurements.glob('pair-*') if p.is_dir()),
                     key=lambda p: int(p.name.split('-', 1)[1])
                     if p.name.split('-', 1)[1].isdigit() else 0)
    rows = []
    failed = False
    for folder in folders:
        pair_no = folder.name.split('-', 1)[1]
        try:
            text = digest_pair(pair_no, folder, sweep)
            path = out / f'pair-{pair_no}.digest.md'
            path.write_text(text)
            weights = load_json(folder / 'weights.json')
            meta = load_json(folder / 'metadata.json')
            changed = sum(1 for row in (weights.get('tensors') or {}).values()
                          if isinstance(row, dict) and row.get('changed'))
            rows.append({'pair': pair_no,
                         'hub': (meta.get('modified') or {}).get('repo', '?'),
                         'verdict': meta.get('verdict', '?'),
                         'headline': headline(weights),
                         'changed': changed,
                         'bytes': len(text.encode())})
            print(f'{path.name} {len(text.encode())}')
        except Exception as error:  # noqa: BLE001 - one bad pair must not stop the rest
            failed = True
            first = str(error).splitlines()[0] if str(error) else type(error).__name__
            print(f'pair-{pair_no}: {first}')
    index = write_index(out, rows, sweep)
    print(f'{index.name} {index.stat().st_size}')
    return 1 if failed else 0


if __name__ == '__main__':
    raise SystemExit(main())
