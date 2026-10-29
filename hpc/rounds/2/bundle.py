# bundle.py -- Assemble the small round files and keep the closing record.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  package the CPU census and keep its token on a separate card.
# Modified: SDE 2026-10-13  hash the payload and quote the desk arguments.
# Modified: SDE 2026-10-15  its own bundle name and cluster path, apart from round 1's.
# Modified: SDE 2026-10-29  the by-hand form is a cd and the script, as the desk reads it.
# Modified: SDE 2026-10-29  any census round and system: the batch sets the round and pair count,
#                           hpc/systems.json the scheduler, queues and work root; optional image.
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
# The census kit lives in rounds/2 and serves every census round; the batch names the round.
KIT = '2'
SYSTEMS = ROOT / 'hpc/systems.json'
LIMIT = 24
FIELDS = ('scheduler', 'work', 'subproject', 'transfer', 'background', 'time_limit', 'purge_days',
          'quota', 'token_file', 'image')
WORD = re.compile(r'[A-Za-z0-9_.,=:/-]+')
CLOCK = re.compile(r'[0-9]{2}:[0-5][0-9]:[0-5][0-9]')


def unfinished(value, path=''):
    """Names of the table fields still marked TBD."""
    if isinstance(value, dict):
        return [name for key, item in value.items() for name in unfinished(item, path + key + '.')]
    if isinstance(value, list):
        return [name for item in value for name in unfinished(item, path)]
    return [path.rstrip('.')] if isinstance(value, str) and 'TBD' in value else []


def system_entry(table, name):
    """One system's entry, refused while a value still waits on the desk."""
    if name not in table:
        raise ValueError('unknown system {}; the table has {}'.format(name, ', '.join(sorted(table))))
    entry = table[name]
    waiting = sorted(set(unfinished(entry)))
    if waiting:
        raise ValueError('systems table entry for {} still has TBD values: {}'.format(name, ', '.join(waiting)))
    missing = [field for field in FIELDS if field not in entry]
    if missing:
        raise ValueError('systems table entry for {} lacks: {}'.format(name, ', '.join(missing)))
    if entry['scheduler'] not in ('slurm', 'pbs'):
        raise ValueError('scheduler must be slurm or pbs, not ' + str(entry['scheduler']))
    if entry['quota'] not in ('lfs', 'show_storage', 'show_usage', 'statvfs') or entry['image'] not in ('optional', 'required'):
        raise ValueError('quota or image setting not understood for ' + name)
    for field in ('transfer', 'background'):
        words = entry[field]
        if not words or not all(isinstance(word, str) and WORD.fullmatch(word) for word in words):
            raise ValueError('{} queue words for {} must be plain words'.format(field, name))
    for field in ('time_limit', 'transfer_time_limit'):
        if field in entry and not CLOCK.fullmatch(entry[field]):
            raise ValueError('{} for {} must read HH:MM:SS'.format(field, name))
    for field in ('work', 'token_file'):
        if not re.fullmatch(r'/[A-Za-z0-9/._-]+', entry[field]) or '..' in entry[field].split('/'):
            raise ValueError('{} for {} must be a plain absolute path'.format(field, name))
    if not re.fullmatch(r'[A-Za-z0-9_-]+', entry['subproject']):
        raise ValueError('invalid subproject for ' + name)
    if entry['scheduler'] == 'pbs':
        # A system that shares nodes names memory per piece; one that hands out whole nodes names mpiprocs.
        memory = entry.get('mem', {})
        select = entry.get('select', {})
        whole_node = isinstance(entry.get('mpiprocs'), int) and entry['mpiprocs'] >= 1
        if not isinstance(entry.get('ncpus'), int) or entry['ncpus'] < 1:
            raise ValueError('a PBS system needs ncpus')
        if select and (set(select) != {'transfer', 'background'} or not all(
                re.fullmatch(r'select=1:ncpus=[1-9][0-9]*(:mpiprocs=[1-9][0-9]*)?', value) for value in select.values())):
            raise ValueError('a PBS select form is select=1:ncpus=N[:mpiprocs=M], one for transfer and one for background')
        if not select and not whole_node and (set(memory) != {'download', 'project', 'sweep'}
                               or not all(re.fullmatch(r'[1-9][0-9]*[kmgt]?b', value) for value in memory.values())):
            raise ValueError('a PBS system names select per queue, or mpiprocs for whole nodes, or mem per piece')
    return entry


def minutes(clock):
    hours, mins, _ = clock.split(':')
    return int(hours) * 60 + int(mins)


def system_script(name, entry, image=None, image_sha256=None):
    """system.sh: the bound system, its scheduler words and limits, one word per line."""
    def value(text):
        return shlex.quote(str(text))
    lines = ['# system.sh -- Select the scheduler queues for this bundle.',
             '# Created by Sean Egan 2026-10-14',
             '# Modified: SDE 2026-10-14  bind the submission system at build.',
             '# Modified: SDE 2026-10-29  scheduler, queue words and limits from hpc/systems.json.',
             '[ "${AUDIT_REHEARSAL:-0}" = 1 ] || export HPC_SYSTEM=' + name,
             'export AUDIT_SCHEDULER={} AUDIT_SUBPROJECT={}'.format(value(entry['scheduler']), value(entry['subproject'])),
             'export AUDIT_TIME_LIMIT={} AUDIT_TRANSFER_TIME_LIMIT={}'.format(
                 value(entry['time_limit']), value(entry.get('transfer_time_limit', entry['time_limit']))),
             'export AUDIT_QUOTA={} AUDIT_TOKEN_FILE={}'.format(value(entry['quota']), value(entry['token_file'])),
             'AUDIT_TRANSFER_ARGS=' + value('\n'.join(entry['transfer'])),
             'AUDIT_BACKGROUND_ARGS=' + value('\n'.join(entry['background'])),
             'export AUDIT_TRANSFER_ARGS AUDIT_BACKGROUND_ARGS']
    if entry['scheduler'] == 'pbs':
        # A system that hands out whole nodes names ncpus and mpiprocs and no memory word.
        memory = entry.get('mem', {})
        select = entry.get('select', {})
        lines.append('export AUDIT_PBS_SELECT_TRANSFER={} AUDIT_PBS_SELECT_BACKGROUND={}'.format(
            value(select.get('transfer', '')), value(select.get('background', ''))))
        lines.append('export AUDIT_PBS_NCPUS={} AUDIT_PBS_MPIPROCS={} AUDIT_PBS_MEM_DOWNLOAD={} '
                     'AUDIT_PBS_MEM_PROJECT={} AUDIT_PBS_MEM_SWEEP={}'.format(
                         entry['ncpus'], value(entry.get('mpiprocs', '')),
                         *(value(memory.get(piece, '')) for piece in ('download', 'project', 'sweep'))))
    if image:
        lines.append('export AUDIT_IMAGE={} AUDIT_IMAGE_SHA256={}'.format(value(image), value(image_sha256)))
    return '\n'.join(lines) + '\n'


def command(arguments):
    """Print a shell line with each argument quoted on its own."""
    return ' '.join(shlex.quote(str(arg)) for arg in arguments)


def build(args):
    """Pack only named sources; tokens and checkpoint files stay outside."""
    fields, size = parse_needs(args.needs)
    table = json.loads(Path(args.systems).read_text())
    entry = system_entry(table, args.system)
    manifest_path = Path(args.manifest or ROOT / 'data/batches/round-{}-batch-1.json'.format(args.round))
    manifest = json.loads(manifest_path.read_text())
    if manifest.get('round') != args.round:
        raise ValueError('the batch is round {}, not round {}'.format(manifest.get('round'), args.round))
    if fields['subproject'] != entry['subproject'] or size < 1024 ** 4:
        raise ValueError('the census needs at least 1T and the subproject of ' + args.system)
    match = re.fullmatch(r'([1-9][0-9]*)([mh])', fields['for'])
    declared = int(match.group(1)) * (60 if match.group(2) == 'h' else 1)
    if not 0 <= declared - minutes(entry['time_limit']) < 60:
        raise ValueError('the declared duration must match the {} job limit'.format(entry['time_limit']))
    if bool(args.image) != bool(args.image_sha256):
        raise ValueError('--image and --image-sha256 go together')
    if entry['image'] == 'required' and not args.image:
        raise ValueError(args.system + ' runs the census inside the image; give --image and --image-sha256')
    if args.image and (not re.fullmatch(r'/[A-Za-z0-9/._-]+\.sif', args.image) or '..' in args.image.split('/')):
        raise ValueError('image needs a plain absolute .sif path on the cluster')
    if args.image and not re.fullmatch(r'[0-9a-f]{64}', args.image_sha256):
        raise ValueError('image needs its 64-character sha256')
    source = Path(args.rounds) / KIT
    reporting = source / 'hpc-poll.d/model-audit.sh'
    if not reporting.is_file() or not reporting.read_text().splitlines()[1].startswith('# version 1 '):
        raise ValueError('reporting script missing or not versioned for this round')
    for step in STEPS + ('90-cleanup.sh', 'round.sh'):
        if not (source / step).is_file():
            raise ValueError('missing step: ' + step)
    from lineage import screen
    count = screen(manifest, ROOT / 'hpc/banned-makers.txt')
    if count != len(manifest['pairs']) or not 1 <= count <= LIMIT:
        raise ValueError('a census batch holds 1 to {} pairs'.format(LIMIT))
    if args.piece and not 1 <= args.piece <= count:
        raise ValueError('--piece must be 1 through {}'.format(count))
    output = Path(args.out or ROOT / '.tmp/hpc/round-{}'.format(args.round)).resolve()
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
        shutil.copyfile(str(ROOT / 'hpc/lineage.py'), str(stage / 'lineage.py'))
        # The names stay at home; the node screens with their hashes.
        from lineage import guard_text
        (stage / 'maker-guard.sha256').write_text(guard_text(ROOT / 'hpc/banned-makers.txt'))
        (stage / 'batch.json').write_text(json.dumps(manifest, indent=2) + '\n')
        (stage / 'systems.json').write_text(json.dumps(table, indent=2) + '\n')
        (stage / 'system.sh').write_text(system_script(args.system, entry, args.image, args.image_sha256))
        if args.image:
            (stage / 'IMAGE.txt').write_text('image: {}\nsha256: {}\n'.format(args.image, args.image_sha256))
            for name in ('image.sh', 'run-check.sh'):
                shutil.copyfile(str(ROOT / 'hpc/container' / name), str(stage / name))
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
        (stage / 'MANIFEST.json').write_text(json.dumps({'round': args.round, 'system': args.system,
            'scheduler': entry['scheduler'], 'pairs': count, 'needs': fields, 'image': args.image,
            'kit_version': version, 'steps': STEPS, 'optional_steps': ['90-cleanup.sh'],
            'storage': {'home': 'scripts and cards only', 'work_budget_bytes': 8 * 1024 ** 4,
                        'submissions': {'copies': 64, 'files_per_copy': 500, 'source_bytes_per_copy': 8 * 1024 ** 2,
                                        'tar_budget_bytes': 512 * 1024 ** 2, 'total_budget_bytes': 1024 ** 3,
                                        'retention': 'through round archive read-back; preserve job references'},
                        'purge_days': entry['purge_days'],
                        'cleanup': 'each modified copy after its reports; each original once every pair '
                                   'reading it has reports; measurements through archive read-back'},
            'files': [{'path': str(p.relative_to(stage)), 'bytes': p.stat().st_size,
                       'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]}, indent=2) + '\n')
        payload = io.BytesIO()
        with tarfile.open(fileobj=payload, mode='w') as archive:
            for path in sorted(stage.iterdir()):
                archive.add(str(path), arcname=path.name)
        tail = payload.getvalue()
        stamp = hashlib.sha256(tail).hexdigest()
        number = str(args.round)
        head = (ROOT / 'hpc/opener.sh').read_text()
        # Home can be over quota; the scripts open in work, beside the round's results.
        head = head.replace('folder=$HOME/model-audit/rounds/__ROUND__',
                            'folder=$WORKDIR/model-audit/rounds/__ROUND__/scripts', 1)
        if 'folder=$WORKDIR/' not in head:
            raise ValueError('the opener no longer names its folder the way this build expects')
        head = head.replace('__ROUND__', number).replace('__SHA__', stamp)
        head = re.sub(r'^# Created by .* ([0-9]{4}-[0-9]{2}-[0-9]{2})$', r'# Created by Sean Egan \1', head, flags=re.M)
        head = head.replace('# model-audit-round.sh -- ', '# ' + NAME + ' -- ', 1)
        head = head.replace('./round.sh "$@"',
                            "printf '%s\\n' '" + stamp + "' > BUILD-STAMP.txt\n./round.sh \"$@\"")
        bundle = output / NAME
        bundle.write_bytes(head.encode() + tail)
        bundle.chmod(0o755)
    destination = entry['work'] + '/' + NAME
    common = ['--no-wait', '--project', 'model-audit', '--system', args.system, '--round', number]
    copy = ['hpc-send', 'push'] + common + ['--why', 'Install the CPU census round',
            '--needs', args.needs, '--output', 'none', '--watch', '', str(bundle), destination]
    token_card = ['hpc-send', 'push'] + common + ['--why', 'Install the read-only licensed hub token',
                 '--needs', args.needs, '--output', 'none', '--watch', '',
                 args.token_source, entry['token_file']]
    run_needs = 'hours=0 subproject={} queue=background for={}'.format(fields['subproject'], fields['for'])
    script = destination + ' ' + number
    if args.piece and not args.projection_only:
        raise ValueError('--piece needs --projection-only')
    if args.projection_only:
        script += ' projection'
        if args.piece:
            script += ' ' + str(args.piece)
    if len(script) >= 50:
        raise ValueError('desk script call must be under 50 characters')
    run = ['hpc-send', 'run', '--after', '$copy'] + common + [
           '--why', 'Verify and submit {} CPU comparisons'.format(count), '--needs', run_needs,
           '--time-limit', '1800', '--output', 'verdict', '--by-hand', 'cd ' + entry['work'],
           '--by-hand', './' + NAME + script[len(destination):]]
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
    print('Preference: {} background CPU, {} pairs; work peak at most 8 TB.'.format(args.system, count))
    if not args.takes:
        print('Duration is unmeasured; supply --takes after the local rehearsal.')


def record(args):
    """Close a successful round from its returned log, without contacting a system."""
    text = Path(args.log).read_text()
    if 'project: model-audit\n' not in text or 'system: ' + args.system + '\n' not in text:
        raise ValueError('log belongs to another project or system')
    match = re.search(r'^round: ([0-9]+)$', text, re.M)
    if not match or 'VERDICT round {} OK'.format(match.group(1)) not in text:
        raise ValueError('no successful round verdict')
    number = int(match.group(1))
    output = Path(args.out)
    output.mkdir(parents=True, exist_ok=True)
    (output / '{}-round-{}.json'.format(args.system, number)).write_text(json.dumps({
        'round': number, 'system': args.system, 'status': 'submitted', 'log_sha256': hashlib.sha256(text.encode()).hexdigest(),
        'research_complete': False}, indent=2) + '\n')
    print('Round {} submission recorded; job measurements close the research work.'.format(number))


def main():
    """Keep build and record as separate, read-only-to-the-desk commands."""
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest='command')
    pack = commands.add_parser('build')
    pack.add_argument('--round', type=int, required=True, help='must match the batch manifest')
    pack.add_argument('--system', default='nautilus', help='any system in hpc/systems.json')
    pack.add_argument('--systems', default=str(SYSTEMS))
    pack.add_argument('--needs', required=True)
    pack.add_argument('--kit', default='/root/work/hpc-kit-wt')
    pack.add_argument('--rounds', default=str(ROOT / 'hpc/rounds'))
    pack.add_argument('--out', help='default .tmp/hpc/round-N')
    pack.add_argument('--projection-only', action='store_true')
    pack.add_argument('--piece', type=int, help='1 through the batch pair count')
    pack.add_argument('--manifest', help='default data/batches/round-N-batch-1.json')
    pack.add_argument('--token-source', default=str(Path.home() / '.hpc/hf-token'))
    pack.add_argument('--takes', help='measured login-round duration')
    pack.add_argument('--image', help='the round image path on the cluster')
    pack.add_argument('--image-sha256', help='that image file\'s sha256')
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
    except (ValueError, KeyError, OSError, subprocess.CalledProcessError) as error:
        parser.exit(1, str(error) + '\n')


if __name__ == '__main__':
    main()
