# drops.py -- Read the pad's drop files for a round into one table: job, kind, event, exit, judgement line, time.
# Created by SDE
import argparse
import json
import re
from pathlib import Path

HEADER_KEYS = ('project', 'system', 'host', 'round', 'job', 'event', 'exit', 'when',
               'build', 'snapshot', 'pinned')
KINDS = ('kit', 'verify', 'reporting', 'submit')
VERDICT_BOLD = re.compile(r'Verdict:\s*\*\*(.+?)\*\*')
VERDICT_WORD = re.compile(r'^VERDICT\s+(\S+)\s+(OK|FAIL)\s*$')


def _header(lines):
    out = {}
    for line in lines:
        if line.startswith('{'):
            break
        if ':' in line:
            key, value = line.split(':', 1)
            out[key.strip()] = value.strip()
    return out


def _json_block(lines):
    start = None
    for i, line in enumerate(lines):
        if line.startswith('{'):
            start = i
            break
    if start is None:
        return None
    end = None
    for i in range(start, len(lines)):
        if lines[i].startswith('}'):
            end = i
            break
    if end is None:
        return None
    try:
        return json.loads('\n'.join(lines[start:end + 1]))
    except ValueError:
        return None


def _kind(job, what):
    for word in KINDS:
        if re.search(r'round-\d+-' + word + r'-', job):
            return word
    if what:
        if what.startswith('Compare'):
            return 'compare'
        if 'ownload' in what:
            return 'download'
        if 'weep' in what:
            return 'sweep'
    return 'job'


def _judgement(lines):
    for line in lines:
        m = VERDICT_BOLD.search(line)
        if m:
            return m.group(1).strip()
    for line in lines:
        m = VERDICT_WORD.match(line.strip())
        if m:
            return m.group(1) + ' ' + m.group(2)
    return None


def parse(path):
    lines = Path(path).read_text().splitlines()
    head = _header(lines)
    block = _json_block(lines)
    what = block.get('what') if isinstance(block, dict) else None
    job = head.get('job', '')
    exit_text = head.get('exit')
    round_text = head.get('round')
    return {
        'project': head.get('project'),
        'system': head.get('system'),
        'host': head.get('host'),
        'round': int(round_text) if round_text not in (None, '') else None,
        'job': job,
        'event': head.get('event'),
        'exit': int(exit_text) if exit_text not in (None, '') else None,
        'when': head.get('when'),
        'what': what,
        'kind': _kind(job, what),
        'judgement': _judgement(lines),
    }


def latest(folder, job):
    found = sorted(Path(folder).glob('*-' + job + '-drop.txt'))
    return found[-1] if found else None


def table(folder, jobs):
    rows = []
    for job in jobs:
        path = latest(folder, job)
        if path is None:
            rows.append({'project': None, 'system': None, 'host': None, 'round': None,
                         'job': job, 'event': None, 'exit': None, 'when': None,
                         'what': None, 'kind': None, 'judgement': None})
        else:
            rows.append(parse(path))
    return rows


def for_round(folder, number):
    rows = []
    for path in sorted(Path(folder).glob('*-drop.txt')):
        row = parse(path)
        if row['round'] == number:
            rows.append(row)
    rows.sort(key=lambda r: r['when'] or '')
    return rows


def _line(row):
    def show(value):
        return '-' if value is None else str(value)
    return '\t'.join(show(row[k]) for k in ('job', 'kind', 'event', 'exit', 'judgement', 'when'))


def main(argv=None):
    ap = argparse.ArgumentParser(description='Read the pad drop files for a round.')
    ap.add_argument('folder')
    ap.add_argument('jobs', nargs='*')
    ap.add_argument('--round', type=int, default=None)
    args = ap.parse_args(argv)
    if args.round is not None:
        rows = for_round(args.folder, args.round)
    else:
        rows = table(args.folder, args.jobs)
    for row in rows:
        print(_line(row))


if __name__ == '__main__':
    main()
