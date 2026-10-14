# rehearse_image.py -- Rehearse round 1 with every Python step inside the image.
# Created by Sean Egan 2026-10-14
# Needs apptainer and the built image (run it on proc1). Stub checkpoint only;
# nothing leaves the machine. Cases: the Nautilus image build, the Jean
# kit-and-verify round, the Jean projection from a copied original, and two refusals.
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys

from rehearse import NEEDS, ROOT, Rehearsal

JEAN_NEEDS = NEEDS.replace('NRLMR57635502', 'NRLMR5762B403')


class ImageRehearsal(Rehearsal):
    """The plain rehearsal, built with the image and Jean options."""

    def __init__(self, args, directory, extra, needs=NEEDS):
        self.extra, self.needs = list(extra), needs
        super().__init__(args, directory)

    def build(self, rounds=None):
        command = [self.login, str(ROOT / 'hpc/bundle.py'), 'build', '--needs', self.needs,
                   '--kit', self.args.kit, '--out', str(self.bundle)] + self.extra
        if rounds is not None:
            command += ['--rounds', str(rounds)]
        subprocess.check_call(command, env=self.environment, stdout=subprocess.DEVNULL)

    def job_lines(self, row, *needles):
        """Outcome lines read from a job's own log."""
        lines = Path(row['log']).read_text().splitlines()
        return [line for line in lines if any(needle in line for needle in needles)]


def show(label, lines):
    print('--- ' + label + ' ---')
    for line in lines:
        print(line)


def run(args):
    directory = Path(args.directory).resolve()
    if directory.exists() and any(directory.iterdir()):
        raise ValueError('rehearsal folder must be empty')
    image = ['--image', args.image, '--image-sha256', args.image_sha256]
    evidence = ('runtime:', 'image:', 'python:', 'requirements:', 'pins:', 'driver:', 'torch:',
                'GPU check', 'VERDICT image', 'stub', 'measurement passed', 'FAIL', 'original checksum')

    # 1. Nautilus, image build: both jobs run their Python inside the image.
    nautilus = ImageRehearsal(args, directory / 'nautilus', image)
    nautilus.clean()
    rows = nautilus.rows()
    for row in rows:
        lines = nautilus.job_lines(row, *evidence)
        nautilus.expect(any('VERDICT image OK' in line for line in lines), 'job {} skipped the image check'.format(row['job']))
        show('nautilus image job {} ({})'.format(row['job'], row['arguments'][-1].rsplit('/', 1)[-1]), lines)
    show('nautilus image round', [line for line in nautilus.log.read_text().splitlines()
                                  if line.startswith(('VERDICT', 'Rehearsal:'))][-4:])

    # 2. Jean kit-and-verify: steps 10 to 30, no job, an end log labeled jean.
    jean = ['--system', 'jean'] + image
    check = ImageRehearsal(args, directory / 'jean-kit', jean + ['--kit-and-verify'], JEAN_NEEDS)
    check.expect(check.run() == 0 and not check.rows(), 'kit-and-verify failed or queued a job')
    end = (check.directory / 'outbox/round-1-end.log').read_text()
    check.expect('system: jean\n' in end and 'VERDICT round 1 OK' in end, 'end log is not a good Jean drop')
    show('jean kit-and-verify', [line for line in end.splitlines()
                                 if line.startswith(('system:', 'step:', 'Jean work', 'pins:', 'VERDICT'))])

    # The relay lands that end log on the pad; the pad proof is made from it at home.
    pad = directory / 'pad/model-audit/jean'
    pad.mkdir(parents=True)
    shutil.copyfile(str(check.directory / 'outbox/round-1-end.log'), str(pad / '20261014T000000Z-round-1-end.log'))
    proof = directory / 'jean-pad-proof.json'
    subprocess.check_call([sys.executable, str(ROOT / 'hpc/bundle.py'), 'pad-proof', '--pad', str(pad),
                           '--out', str(proof), str(pad / '20261014T000000Z-round-1-end.log')])

    # 3. Jean projection from the original copied over from Nautilus.
    def copied(name):
        case = ImageRehearsal(args, directory / name, jean + ['--pad-proof', str(proof)], JEAN_NEEDS)
        source = nautilus.work / 'model-audit/originals'
        shutil.copytree(str(source), str(case.work / 'model-audit/originals'))
        return case

    project = copied('jean-projection')
    project.expect(project.run() == 0, 'Jean projection round failed')
    rows = project.rows()
    project.expect(len(rows) == 1 and rows[0]['arguments'][-1].endswith('/jobs/project.sh'),
                   'Jean round did not queue exactly one projection job')
    project.expect('--comment=project=model-audit' in rows[0]['arguments'], 'Jean job lacks the owner tag')
    project.expect(rows[0]['status'] == 'finished' and rows[0]['exit'] == 0, 'Jean projection job failed')
    header = (project.round / 'jobs/project.sh').read_text()
    project.expect('#SBATCH --partition=AIML_BACK\n' in header and '--qos' not in header, 'Jean header is wrong')
    show('jean projection job {}'.format(rows[0]['job']), project.job_lines(rows[0], *evidence) +
         ['arguments: ' + ' '.join(rows[0]['arguments'][:3])])

    # 4. A damaged copy fails the job and names the file.
    damaged = copied('jean-damaged')
    stub = damaged.work / 'model-audit/originals/rehearsal-base/stub.txt'
    stub.write_text(stub.read_text().replace('small', 'SMALL'))
    damaged.run()
    rows = damaged.rows()
    damaged.expect(len(rows) == 1 and rows[0]['status'] == 'failed', 'damaged copy did not fail the job')
    lines = damaged.job_lines(rows[0], 'original checksum differs', 'VERDICT image')
    damaged.expect(any('original checksum differs' in line for line in lines), 'refusal did not name the file')
    show('jean damaged copy job {} exit {}'.format(rows[0]['job'], rows[0]['exit']), lines)

    # 5. Without the carried pad proof the submit step refuses.
    (project.round / 'pad-proof.json').unlink()
    before = len(project.rows())
    result = project.call(['./round.sh', '--only', '40-submit.sh'], project.round)
    tail = project.log.read_text().splitlines()
    project.expect(result != 0 and len(project.rows()) == before and
                   'no landed Jean drop is carried in pad-proof.json' in tail, 'missing receipt was not refused')
    show('jean submit without receipt', [line for line in tail[-12:] if 'pad-proof' in line or 'VERDICT' in line])
    print('All five image cases matched.')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('directory')
    parser.add_argument('--image', required=True, help='the built .sif on this machine')
    parser.add_argument('--image-sha256', required=True)
    parser.add_argument('--base', default='rehearsal/stub')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--kit', default='/root/work/hpc-kit-wt')
    parser.add_argument('--login-python', default='python3')
    parser.add_argument('--compute-python', default='python3')
    args = parser.parse_args()
    try:
        run(args)
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        parser.exit(1, str(error) + '\n')


if __name__ == '__main__':
    main()
