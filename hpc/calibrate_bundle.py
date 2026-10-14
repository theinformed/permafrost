# calibrate_bundle.py -- Pack the single-job recipe calibration round.
# Created by Sean Egan 2026-10-14
# Modified: SDE 2026-10-14  keep calibration cards separate from the live round.
# Modified: SDE 2026-10-14  stop loudly if the storage check stops matching.
import argparse
import datetime
import hashlib
import io
import json
from pathlib import Path
import re
import shutil
import subprocess
import tarfile
import tempfile

from bundle import KIT_FILES, command
from needs import parse_needs

ROOT = Path(__file__).resolve().parent.parent
STEPS = ('10-install-kit.sh', '20-verify.sh', '40-submit.sh')
RECIPES = ('norm-preserving', 'single-projection')
RUN = '/p/work1/sdegan/model-audit-calibrate.sh 4'


def build(args):
    """Pack only source files and print desk cards without executing them."""
    fields, size = parse_needs(args.needs)
    if args.system != 'nautilus':
        raise ValueError('calibration builds for nautilus only')
    if fields['subproject'] != 'NRLMR57635502' or not 60 * 1024 ** 3 <= size <= 200 * 1024 ** 3:
        raise ValueError('calibration needs 60G through 200G and its approved subproject')
    if fields['for'] != '4h':
        raise ValueError('calibration requires for=4h')
    if args.recipe not in RECIPES:
        raise ValueError('unsupported recipe: ' + args.recipe)
    if args.takes and not re.fullmatch(r'[1-9][0-9]*[smh]', args.takes):
        raise ValueError('takes requires a measured duration, such as 90s')
    assert len(RUN) < 50 and not any(char in RUN for char in '=|;&')
    source = Path(args.rounds) / '4'
    for name in STEPS + ('round.sh', 'env.sh', 'jobs/calibrate.sh', 'measure.py'):
        if not (source / name).is_file():
            raise ValueError('missing round file: ' + name)
    output = Path(args.out).resolve()
    output.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='calibration-', dir=str(output)) as temporary:
        stage = Path(temporary) / 'round'
        shutil.copytree(str(source), str(stage), ignore=shutil.ignore_patterns('__pycache__'))
        for path in stage.rglob('*'):
            if path.is_symlink() or (path.is_file() and path.suffix not in ('.sh', '.py', '.json', '.txt')):
                raise ValueError('unexpected round file: ' + str(path))
        (stage / 'RECIPE.txt').write_text(args.recipe + '\n')
        (stage / 'audit/recipes').mkdir(parents=True)
        for name in ('__init__.py', 'weights.py', 'nulls.py', 'weights_cli.py', 'recipes.json',
                     'recipes/__init__.py', 'recipes/common.py', 'recipes/projection.py'):
            shutil.copyfile(str(ROOT / 'audit' / name), str(stage / 'audit' / name))
        shutil.copytree(str(ROOT / 'data/prompts'), str(stage / 'data/prompts'))
        for name in ('project.py', 'calibrate.py', 'storage.py', 'needs.py'):
            shutil.copyfile(str(ROOT / 'hpc' / name), str(stage / name))
        # The shared quota check's summary file belongs to round 1.
        storage = stage / 'storage.py'
        summary = ("    cache = Path(os.environ['HOME']) / '.hpc/model-audit-space.tsv'\n"
                   "    cache.write_text('{}\\t{}\\n'.format(project, own // 1024))\n")
        text = storage.read_text()
        if summary not in text:
            raise ValueError('storage.py changed; recheck which space summary round 4 may write')
        storage.write_text(text.replace(summary, ''))
        kit = stage / 'kit'
        kit.mkdir()
        for name in KIT_FILES:
            shutil.copyfile(str(Path(args.kit) / name), str(kit / name))
        version = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%d.%H%M%S%f')
        poll = kit / 'hpc-poll.sh'
        poll.write_text(re.sub(r'^KIT_VERSION=.*$', 'KIT_VERSION=' + version, poll.read_text(), flags=re.M))
        (kit / 'KIT_VERSION').write_text(version + '\n')
        (stage / 'needs.json').write_text(json.dumps({'fields': fields, 'bytes': size}) + '\n')
        files = sorted(path for path in stage.rglob('*') if path.is_file())
        if len(files) + 2 > 500 or sum(path.stat().st_size for path in files) > 8 * 1024 ** 2:
            raise ValueError('script bundle exceeds its 500-file, 8 MB budget')
        rows = []
        for path in files:
            if path.suffix == '.sh' or path.name == 'hpc':
                path.chmod(0o755)
                subprocess.check_call(['bash', '-n', str(path)])
            rows.append('{}  {}'.format(hashlib.sha256(path.read_bytes()).hexdigest(), path.relative_to(stage)))
        (stage / 'SHA256SUMS').write_text('\n'.join(rows) + '\n')
        manifest = {'round': 4, 'piece': 'recipe-calibration', 'recipe': args.recipe, 'system': args.system,
                    'needs': fields, 'kit_version': version, 'steps': STEPS,
                    'files': [{'path': str(path.relative_to(stage)), 'bytes': path.stat().st_size,
                               'sha256': hashlib.sha256(path.read_bytes()).hexdigest()} for path in files]}
        (stage / 'MANIFEST.json').write_text(json.dumps(manifest, indent=2) + '\n')
        files = [path for path in stage.rglob('*') if path.is_file()]
        if len(files) > 500 or sum(path.stat().st_size for path in files) > 8 * 1024 ** 2:
            raise ValueError('script bundle exceeds its 500-file, 8 MB budget')
        payload = io.BytesIO()
        with tarfile.open(fileobj=payload, mode='w') as archive:
            for path in sorted(stage.iterdir()):
                archive.add(str(path), arcname=path.name)
        tail = payload.getvalue()
        stamp = hashlib.sha256(tail).hexdigest()
        head = (ROOT / 'hpc/opener.sh').read_text().replace('__ROUND__', '4').replace('__SHA__', stamp)
        head = head.replace('model-audit-round.sh', 'model-audit-calibrate.sh')
        head = head.replace('Created by LT Sean Egan, PhD 2026-10-13', 'Created by Sean Egan 2026-10-14')
        head = head.replace('Modified: SDE 2026-10-13', 'Modified: SDE 2026-10-14')
        head = head.replace('./round.sh "$@"',
            "printf '%s\\n' '" + stamp + "' > BUILD-STAMP.txt\n./round.sh \"$@\"")
        bundle = output / 'model-audit-calibrate.sh'
        bundle.write_bytes(head.encode() + tail)
        bundle.chmod(0o755)
    staged = args.staged
    destination = '/p/work1/sdegan/model-audit-calibrate.sh'
    copy = ['hpc-send', 'push', '--no-wait', '--project', 'model-audit', '--system', args.system,
            '--round', '4', '--why', 'Install the recipe calibration piece', '--needs', args.needs,
            '--output', 'none', '--watch', '', '--by-hand',
            'scp {} nautilus.navydsrc.hpc.mil:{}'.format(staged, destination), staged, destination]
    run = ['hpc-send', 'run', '--no-wait', '--after', '$copy', '--project', 'model-audit',
           '--system', args.system, '--round', '4', '--why', 'Verify and submit the recipe calibration job',
           '--needs', 'hours=0 subproject=NRLMR57635502 queue=background for=4h',
           '--time-limit', '1800', '--output', 'verdict', '--by-hand', RUN,
           '--watch', RUN + ' > round-4.log 2>&1 &', '--watch', 'disown', '--watch', 'tail -f round-4.log']
    for step in STEPS:
        run.extend(['--steps', './' + step])
    if args.takes:
        run.extend(['--takes', args.takes])
    run.extend(['--', RUN])
    run_line = command(run).replace("'$copy'", '"$copy"')
    cards = output / 'calibration-cards.sh'
    cards.write_text('#!/bin/bash\n# calibration-cards.sh -- Queue the calibration copy and then its run.\n'
        '# Created by Sean Egan 2026-10-14\n'
        '# Modified: SDE 2026-10-14  wait for each desk result.\nset -euo pipefail\n'
        'copy=$(' + command(copy) + ')\nhpc-send wait "$copy"\nrun=$(' + run_line + ')\nhpc-send wait "$run"\n')
    cards.chmod(0o755)
    print('Bundle: ' + str(bundle))
    print('Build stamp: ' + stamp)
    print('Recipe: ' + args.recipe)
    print('Run: ' + RUN)
    print('Copy card: ' + command(copy))
    print('Run card: ' + run_line)


def main():
    """Validate build arguments before any file is staged."""
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest='command')
    pack = commands.add_parser('build')
    pack.add_argument('--needs', required=True)
    pack.add_argument('--recipe', default='norm-preserving')
    pack.add_argument('--system', default='nautilus')
    pack.add_argument('--kit', default='/root/work/hpc-kit-wt')
    pack.add_argument('--rounds', default=str(ROOT / 'hpc/rounds'))
    pack.add_argument('--out', default=str(ROOT / '.tmp/hpc/recipe-calibration'))
    pack.add_argument('--staged', default='/opt/ai/hpc-packages/bundles/model-audit/model-audit-calibrate.sh')
    pack.add_argument('--takes')
    args = parser.parse_args()
    if args.command != 'build':
        parser.error('choose build')
    try:
        build(args)
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        parser.exit(1, str(error) + '\n')


if __name__ == '__main__':
    main()
