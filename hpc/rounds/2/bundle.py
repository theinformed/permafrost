# bundle.py -- Assemble the small round files and keep the closing record.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  package the CPU census and keep its token on a separate card.
# Modified: SDE 2026-10-13  hash the payload and quote the desk arguments.
# Modified: SDE 2026-10-15  its own bundle name and cluster path, apart from round 1's.
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

import sys
sys.path.append(str(Path(__file__).resolve().parents[2]))
from needs import parse_needs

ROOT = Path(__file__).resolve().parents[3]
KIT_FILES = ('hpc', 'hpc-poll.sh', 'hpc-report.sh', 'hpc_report.py', 'lib.sh',
             'lib.awk', 'cards.awk', 'jobs.sh', 'inspect.sh', 'nodes.sh', 'overview.sh',
             'queue.sh', 'storage.sh', 'usage.sh', 'sections.sh', 'cards.sh',
             'archive.sh', 'hpc_poll_parse.py', 'relay-known-hosts', 'JOB-CARD-STANDARD.md')
STEPS = ('10-install-kit.sh', '20-verify.sh', '30-install-reporting.sh', '40-submit.sh')
# Round 1 stages model-audit-round.sh; the census must never land on that name.
NAME = 'model-audit-census.sh'
DESTINATION = '/p/work1/sdegan/' + NAME


def command(arguments):
    """Print a shell line with each argument quoted on its own."""
    return ' '.join(shlex.quote(str(arg)) for arg in arguments)


def build(args):
    """Pack only named sources; tokens and checkpoint files stay outside."""
    fields, size = parse_needs(args.needs)
    if args.round != 2 or args.system not in ('nautilus', 'raider'):
        raise ValueError('the census builds round 2 for nautilus or raider')
    if fields['subproject'] != 'NRLMR57635502' or size < 1024 ** 4:
        raise ValueError('round 2 needs at least 1T and its approved subproject')
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
        shutil.copytree(str(source), str(stage / 'round'), ignore=shutil.ignore_patterns('__pycache__'))
        stage = stage / 'round'
        for path in stage.rglob('*'):
            if path.is_symlink() or (path.is_file() and path.suffix not in ('.sh', '.py', '.json', '.txt')):
                raise ValueError('unexpected round file: ' + str(path))
        (stage / 'audit').mkdir()
        for name in ('__init__.py', 'weights.py', 'nulls.py', 'weights_cli.py', 'recipes.json',
                     'metadata.py', 'compare.py', 'gguf.py', 'hub.py', 'template_worker.py'):
            shutil.copyfile(str(ROOT / 'audit' / name), str(stage / 'audit' / name))
        (stage / 'audit/recipes').mkdir()
        for name in ('__init__.py', 'common.py'):
            shutil.copyfile(str(ROOT / 'audit/recipes' / name), str(stage / 'audit/recipes' / name))
        shutil.copyfile(str(ROOT / 'hpc/project.py'), str(stage / 'project.py'))
        for name in ('lineage.py', 'banned-makers.txt'):
            shutil.copyfile(str(ROOT / 'hpc' / name), str(stage / name))
        manifest = json.loads(Path(args.manifest).read_text())
        from lineage import screen
        if screen(manifest, ROOT / 'hpc/banned-makers.txt') != 5:
            raise ValueError('round 2 requires exactly five pairs')
        (stage / 'batch.json').write_text(json.dumps(manifest, indent=2) + '\n')
        (stage / 'system.sh').write_text('# system.sh -- Select the scheduler queues for this bundle.\n'
            '# Created by Sean Egan 2026-10-14\n'
            '# Modified: SDE 2026-10-14  bind the submission system at build.\n'
            '[ "${AUDIT_REHEARSAL:-0}" = 1 ] || export HPC_SYSTEM=' + args.system + '\n')
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
        (stage / 'MANIFEST.json').write_text(json.dumps({'round': 2, 'system': args.system, 'needs': fields,
            'kit_version': version, 'steps': STEPS, 'optional_steps': ['90-cleanup.sh'],
            'storage': {'home': 'scripts and cards only', 'work_budget_bytes': 8 * 1024 ** 4,
                        'submissions': {'copies': 64, 'files_per_copy': 500, 'source_bytes_per_copy': 8 * 1024 ** 2,
                                        'tar_budget_bytes': 512 * 1024 ** 2, 'total_budget_bytes': 1024 ** 3,
                                        'retention': 'through round archive read-back; preserve job references'},
                        'purge_days': 21 if args.system == 'nautilus' else 30,
                        'cleanup': 'both checkpoints after successful reports; measurements through archive read-back'},
            'files': [{'path': str(p.relative_to(stage)), 'bytes': p.stat().st_size,
                       'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]}, indent=2) + '\n')
        payload = io.BytesIO()
        with tarfile.open(fileobj=payload, mode='w') as archive:
            for path in sorted(stage.iterdir()):
                archive.add(str(path), arcname=path.name)
        tail = payload.getvalue()
        stamp = hashlib.sha256(tail).hexdigest()
        head = (ROOT / 'hpc/opener.sh').read_text().replace('__ROUND__', '2').replace('__SHA__', stamp)
        head = re.sub(r'^# Created by .* ([0-9]{4}-[0-9]{2}-[0-9]{2})$', r'# Created by Sean Egan \1', head, flags=re.M)
        head = head.replace('# model-audit-round.sh -- ', '# ' + NAME + ' -- ', 1)
        head = head.replace('./round.sh "$@"',
                            "printf '%s\\n' '" + stamp + "' > BUILD-STAMP.txt\n./round.sh \"$@\"")
        bundle = output / NAME
        bundle.write_bytes(head.encode() + tail)
        bundle.chmod(0o755)
    destination = DESTINATION
    common = ['--no-wait', '--project', 'model-audit', '--system', args.system, '--round', '2']
    copy = ['hpc-send', 'push'] + common + ['--why', 'Install the CPU census round',
            '--needs', args.needs, '--output', 'none', '--watch', '', str(bundle), destination]
    token_card = ['hpc-send', 'push'] + common + ['--why', 'Install the read-only licensed hub token',
                 '--needs', args.needs, '--output', 'none', '--watch', '',
                 args.token_source, '/p/home/sdegan/.hpc/hf-token']
    run_needs = 'hours=0 subproject={} queue=background for={}'.format(fields['subproject'], fields['for'])
    script = destination + ' 2'
    if args.piece and not args.projection_only:
        raise ValueError('--piece needs --projection-only')
    if args.projection_only:
        script += ' projection'
        if args.piece:
            script += ' ' + str(args.piece)
    if len(script) >= 50:
        raise ValueError('desk script call must be under 50 characters')
    run = ['hpc-send', 'run', '--after', '$copy'] + common + [
           '--why', 'Verify and submit five CPU comparisons', '--needs', run_needs,
           '--time-limit', '1800', '--output', 'verdict', '--by-hand', script]
    for step in STEPS:
        run.extend(['--steps', './' + step])
    if args.takes:
        if not re.fullmatch(r'[1-9][0-9]*[smh]', args.takes):
            raise ValueError('takes requires a measured duration, such as 90s')
        run.extend(['--takes', args.takes])
    run.extend(['--', script])
    run_line = command(run).replace("'$copy'", '\"$copy\"')
    cards = output / 'round-cards.sh'
    cards.write_text('#!/bin/bash\n# round-cards.sh -- Stage credentials separately, then the census scripts.\n'
        '# Created by Sean Egan 2026-10-14\n'
        '# Modified: SDE 2026-10-14  wait for each completed push before the run.\nset -euo pipefail\n'
        'token=$(' + command(token_card) + ')\nhpc-send wait "$token"\n'
        'copy=$(' + command(copy) + ')\nhpc-send wait "$copy"\n'
        'run=$(' + run_line + ')\nhpc-send wait "$run"\n')
    cards.chmod(0o755)
    print('Bundle: ' + str(bundle))
    print('Token: ' + command(token_card))
    print('Copy: ' + command(copy))
    print('Run: ' + run_line)
    print('Preference: nautilus background CPU; raider background CPU overflow; work peak at most 8 TB.')
    if not args.takes:
        print('Duration is unmeasured; supply --takes after the local rehearsal.')


def record(args):
    """Close a successful round from its returned log, without contacting a system."""
    text = Path(args.log).read_text()
    if 'project: model-audit\n' not in text or 'system: ' + args.system + '\n' not in text:
        raise ValueError('log belongs to another project or system')
    if 'round: 2\n' not in text or 'VERDICT round 2 OK' not in text:
        raise ValueError('no successful round verdict')
    output = Path(args.out)
    output.mkdir(parents=True, exist_ok=True)
    (output / (args.system + '-round-2.json')).write_text(json.dumps({
        'round': 2, 'system': args.system, 'status': 'submitted', 'log_sha256': hashlib.sha256(text.encode()).hexdigest(),
        'research_complete': False}, indent=2) + '\n')
    print('Round 2 submission recorded; job measurements close the research work.')


def main():
    """Keep build and record as separate, read-only-to-the-desk commands."""
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest='command')
    pack = commands.add_parser('build')
    pack.add_argument('--round', type=int, default=2)
    pack.add_argument('--system', default='nautilus')
    pack.add_argument('--needs', required=True)
    pack.add_argument('--kit', default='/root/work/hpc-kit-wt')
    pack.add_argument('--rounds', default=str(ROOT / 'hpc/rounds'))
    pack.add_argument('--out', default=str(ROOT / '.tmp/hpc/round-2'))
    pack.add_argument('--projection-only', action='store_true')
    pack.add_argument('--piece', type=int, choices=range(1, 6))
    pack.add_argument('--manifest', default=str(ROOT / 'data/batches/round-2-batch-1.json'))
    pack.add_argument('--token-source', default=str(Path.home() / '.hpc/hf-token'))
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
