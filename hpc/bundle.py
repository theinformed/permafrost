# bundle.py -- Assemble the small round files and keep the closing record.
# Created by LT Sean Egan, PhD 2026-10-13
# Modified: SDE 2026-10-13  hash the payload and quote the desk arguments.
import argparse
import datetime
import hashlib
import io
import json
import os
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import tarfile
import tempfile

from needs import parse_needs

ROOT = Path(__file__).resolve().parent.parent
KIT_FILES = ('hpc', 'hpc-poll.sh', 'hpc-report.sh', 'hpc_report.py', 'lib.sh',
             'lib.awk', 'cards.awk', 'jobs.sh', 'inspect.sh', 'nodes.sh', 'overview.sh',
             'queue.sh', 'storage.sh', 'usage.sh', 'sections.sh', 'cards.sh',
             'archive.sh', 'hpc_poll_parse.py', 'relay-known-hosts', 'JOB-CARD-STANDARD.md')
STEPS = ('10-install-kit.sh', '20-verify.sh', '30-install-reporting.sh', '40-submit.sh')


def command(arguments):
    """Print a shell line with each argument quoted on its own."""
    return ' '.join(shlex.quote(str(arg)) for arg in arguments)


def build(args):
    """Pack only named sources; tokens and checkpoint files stay outside."""
    fields, size = parse_needs(args.needs)
    if args.round != 1 or args.system != 'nautilus':
        raise ValueError('the first kit builds round 1 for nautilus only')
    if fields['subproject'] != 'NRLMR57635502' or size < 160 * 1024 ** 3:
        raise ValueError('round 1 needs at least 160G and its approved subproject')
    if fields['for'] != '4h':
        raise ValueError('the declared duration must match the 4h batch requests')
    source = Path(args.rounds) / str(args.round)
    reporting = source / 'hpc-poll.d/model-audit.sh'
    if not reporting.is_file() or not reporting.read_text().splitlines()[1].startswith('# version 1 '):
        raise ValueError('reporting script missing or not versioned for this round')
    for step in STEPS + ('90-cleanup.sh', 'round.sh'):
        if not (source / step).is_file():
            raise ValueError('missing step: ' + step)
    output = Path(args.out).resolve()
    output.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='permafrost-') as temporary:
        stage = Path(temporary)
        shutil.copytree(str(source), str(stage / 'round'))
        stage = stage / 'round'
        for path in stage.rglob('*'):
            if path.is_symlink() or (path.is_file() and path.suffix not in ('.sh', '.py', '.json', '.txt')):
                raise ValueError('unexpected round file: ' + str(path))
        (stage / 'audit').mkdir()
        for name in ('__init__.py', 'weights.py', 'nulls.py', 'weights_cli.py', 'recipes.json'):
            shutil.copyfile(str(ROOT / 'audit' / name), str(stage / 'audit' / name))
        shutil.copytree(str(ROOT / 'data/prompts'), str(stage / 'data/prompts'))
        for name in ('download.py', 'project.py', 'storage.py', 'cleanup.py', 'needs.py'):
            shutil.copyfile(str(ROOT / 'hpc' / name), str(stage / name))
        kit = stage / 'kit'
        kit.mkdir()
        for name in KIT_FILES:
            shutil.copyfile(str(Path(args.kit) / name), str(kit / name))
        version = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%d.%H%M%S')
        poll = kit / 'hpc-poll.sh'
        poll.write_text(re.sub(r'^KIT_VERSION=.*$', 'KIT_VERSION=' + version, poll.read_text(), flags=re.M))
        (kit / 'KIT_VERSION').write_text(version + '\n')
        (stage / 'needs.json').write_text(json.dumps({'fields': fields, 'bytes': size}) + '\n')
        files = sorted(path for path in stage.rglob('*') if path.is_file())
        if len(files) > 500 or sum(path.stat().st_size for path in files) > 8 * 1024 ** 2:
            raise ValueError('script bundle exceeds its 500-file, 8 MB budget')
        rows = []
        for path in files:
            if path.suffix == '.sh' or path.name == 'hpc':
                path.chmod(0o755)
                subprocess.check_call(['bash', '-n', str(path)])
            rows.append('{}  {}'.format(hashlib.sha256(path.read_bytes()).hexdigest(), path.relative_to(stage)))
        (stage / 'SHA256SUMS').write_text('\n'.join(rows) + '\n')
        (stage / 'MANIFEST.json').write_text(json.dumps({'round': 1, 'system': args.system, 'needs': fields,
            'kit_version': version, 'steps': STEPS, 'optional_steps': ['90-cleanup.sh'],
            'storage': {'home': 'scripts and cards only', 'work_budget_bytes': 2 * 1024 ** 4,
                        'cleanup': 'derived weights only after archive read-back and approved paths'},
            'files': [{'path': str(p.relative_to(stage)), 'bytes': p.stat().st_size,
                       'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]}, indent=2) + '\n')
        payload = io.BytesIO()
        with tarfile.open(fileobj=payload, mode='w') as archive:
            for path in sorted(stage.iterdir()):
                archive.add(str(path), arcname=path.name)
        tail = payload.getvalue()
        head = (ROOT / 'hpc/opener.sh').read_text().replace('__ROUND__', '1').replace('__SHA__', hashlib.sha256(tail).hexdigest())
        bundle = output / 'model-audit-round.sh'
        bundle.write_bytes(head.encode() + tail)
        bundle.chmod(0o755)
    destination = '/p/work1/sdegan/model-audit-round.sh'
    copy = ['hpc-send', 'push', '--no-wait', '--project', 'model-audit', '--system', args.system,
            '--round', '1', '--why', 'Install the first projection round', '--needs', args.needs,
            '--output', 'none', '--watch', '', '--by-hand',
            'scp {} nautilus.navydsrc.hpc.mil:{}'.format(bundle, destination), str(bundle), destination]
    run_needs = 'hours=0 subproject={} queue=background for={}'.format(fields['subproject'], fields['for'])
    run = ['hpc-send', 'run', '--no-wait', '--after', '$copy', '--project', 'model-audit', '--system', args.system,
           '--round', '1', '--why', 'Verify and submit the first projection chain', '--needs', run_needs,
           '--time-limit', '1800', '--output', 'verdict',
           '--by-hand', 'cd /p/work1/sdegan', '--by-hand', './model-audit-round.sh 1',
           '--watch', 'cd /p/work1/sdegan', '--watch', './model-audit-round.sh 1 > round-1.log 2>&1 &',
           '--watch', 'disown', '--watch', 'tail -f round-1.log']
    for step in STEPS:
        run.extend(['--steps', './' + step])
    if args.takes:
        if not re.fullmatch(r'[1-9][0-9]*[smh]', args.takes):
            raise ValueError('takes requires a measured duration, such as 90s')
        run.extend(['--takes', args.takes])
    run.extend(['--', 'cd /p/work1/sdegan && ./model-audit-round.sh 1'])
    run_line = command(run).replace("'$copy'", '"$copy"')
    cards = output / 'round-cards.sh'
    cards.write_text('#!/bin/bash\n# round-cards.sh -- Queue the copy, wait, then queue its run.\n'
        '# Created by LT Sean Egan, PhD 2026-10-13\n'
        '# Modified: SDE 2026-10-13  stop if the copy fails.\nset -euo pipefail\n'
        'copy=$(' + command(copy) + ')\nhpc-send wait "$copy"\nrun=$(' + run_line + ')\nhpc-send wait "$run"\n')
    cards.chmod(0o755)
    print('Bundle: ' + str(bundle))
    print('Copy: ' + command(copy))
    print('Run: ' + run_line)
    if not args.takes:
        print('Duration is unmeasured; rebuild with --takes after the Spark rehearsal.')


def record(args):
    """Close a successful round from its returned log, without contacting a system."""
    text = Path(args.log).read_text()
    if 'project: model-audit\n' not in text or 'system: ' + args.system + '\n' not in text:
        raise ValueError('log belongs to another project or system')
    if 'round: 1\n' not in text or 'VERDICT round 1 OK' not in text:
        raise ValueError('no successful round verdict')
    output = Path(args.out)
    output.mkdir(parents=True, exist_ok=True)
    (output / (args.system + '-round-1.json')).write_text(json.dumps({
        'round': 1, 'system': args.system, 'status': 'submitted', 'log_sha256': hashlib.sha256(text.encode()).hexdigest(),
        'research_complete': False}, indent=2) + '\n')
    print('Round 1 submission recorded; job measurements close the research work.')


def main():
    """Keep build and record as separate, read-only-to-the-desk commands."""
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest='command')
    pack = commands.add_parser('build')
    pack.add_argument('--round', type=int, default=1)
    pack.add_argument('--system', default='nautilus')
    pack.add_argument('--needs', required=True)
    pack.add_argument('--kit', default='/root/work/hpc-kit-wt')
    pack.add_argument('--rounds', default=str(ROOT / 'hpc/rounds'))
    pack.add_argument('--out', default=str(ROOT / '.tmp/hpc/round-1'))
    pack.add_argument('--takes', help='measured login-round duration')
    pack.set_defaults(handler=build)
    close = commands.add_parser('record')
    close.add_argument('system')
    close.add_argument('log')
    close.add_argument('--out', default=str(ROOT / '.tmp/hpc/records'))
    close.set_defaults(handler=record)
    args = parser.parse_args()
    if not hasattr(args, 'handler'):
        parser.error('choose build or record')
    try:
        args.handler(args)
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        parser.exit(1, str(error) + '\n')


if __name__ == '__main__':
    main()
