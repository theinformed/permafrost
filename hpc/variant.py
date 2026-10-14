# variant.py -- Turn a staged round 1 into its image build or its Jean build.
# Created by Sean Egan 2026-10-14
# The default build never comes through here. Each change names the exact text
# it replaces, so a drifted round source fails the build instead of half-applying.
import datetime
import hashlib
import json
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parent.parent
TAG = '--comment=project=model-audit'
JEAN_ACCOUNT = 'NRLMR5762B403'
PAD_FIELDS = {'project': 'model-audit', 'system': 'jean', 'exit': 0, 'landed': True}


def swap(path, old, new):
    """Replace one exact passage; anything else means the source moved."""
    text = path.read_text()
    if text.count(old) != 1:
        raise ValueError('{} changed; cannot place: {}'.format(path.name, old.splitlines()[0][:60]))
    path.write_text(text.replace(old, new))


def add_image(stage, image, sha256):
    """Run every Python step of the jobs inside the pinned image."""
    if not re.fullmatch(r'/[A-Za-z0-9/._-]+\.sif', image) or '..' in image.split('/'):
        raise ValueError('image needs a plain absolute .sif path on the cluster')
    if not re.fullmatch(r'[0-9a-f]{64}', sha256 or ''):
        raise ValueError('image needs its 64-character sha256')
    (stage / 'IMAGE.txt').write_text('image: {}\nsha256: {}\n'.format(image, sha256))
    for name in ('image.sh', 'run-check.sh'):
        shutil.copyfile(str(ROOT / 'hpc/container' / name), str(stage / name))
    env = stage / 'env.sh'
    env.write_text(env.read_text() + '\n# This build runs its Python inside the round image.\n. ./image.sh\n')
    project = stage / 'jobs/project.sh'
    swap(project, "    python3 ./measure.py\n    echo 'stub projection passed'\n",
         "    image_ready 0\n    image_python ./measure.py\n    echo 'stub projection passed'\n")
    swap(project, 'compute_python\nif [ "${AUDIT_REHEARSAL:-0}" != 1 ]; then nvidia-smi; fi\n'
         '# The venv is good only for the pins it was built from; new pins rebuild it.\n'
         'pins=$(sha256sum compute-requirements.txt | cut -d\' \' -f1)\n'
         'if [ "$(cat "$AUDIT_WORK/venv/.ready" 2>/dev/null)" != "$pins" ]; then\n'
         '    echo "compute venv: building for pins $pins"\n'
         '    rm -rf -- "$AUDIT_WORK/venv"\n'
         '    python3 -m venv "$AUDIT_WORK/venv"\n'
         '    "$AUDIT_WORK/venv/bin/python" -m pip install --no-index --find-links "$AUDIT_WORK/wheels" '
         '-r compute-requirements.txt\n'
         '    echo "$pins" > "$AUDIT_WORK/venv/.ready"\n'
         'else\n'
         '    echo "compute venv: reusing pins $pins"\n'
         'fi\n',
         '# The image carries the pinned libraries; it checks them and the GPUs first.\n'
         'image_ready 4\n')
    swap(project, '"$AUDIT_WORK/venv/bin/python" ./measure.py\n', 'image_python ./measure.py\n')
    download = stage / 'jobs/download.sh'
    if download.exists():
        swap(download, '    python3 ./measure.py --seed-original\n',
             '    image_ready 0\n    image_python ./measure.py --seed-original\n')
        swap(download, 'compute_python\npython3 -m venv "$AUDIT_WORK/download-venv"\n'
             'py=$AUDIT_WORK/download-venv/bin/python\n'
             '"$py" -m pip install \'huggingface_hub==0.35.3\'\n'
             'mkdir -p "$AUDIT_WORK/wheels"\n'
             '"$py" -m pip download -r compute-requirements.txt --dest "$AUDIT_WORK/wheels"\n'
             '"$py" ./download.py\n',
             '# The image brings its own Python and hub client; no wheels are needed.\n'
             'image_ready 0\nimage_python ./download.py\n')
    # Prove the image runs here, without a GPU, before anything is queued.
    swap(stage / '20-verify.sh', "echo 'VERDICT verify OK'\n", "image_ready 0\necho 'VERDICT verify OK'\n")


def pad_proof(drop, pad_dir):
    """Read a Jean drop that reached the vps pad; return its receipt."""
    drop = Path(drop).resolve()
    if drop.parent != Path(pad_dir).resolve() or not drop.is_file():
        raise ValueError('drop must be a file in ' + str(pad_dir))
    text = drop.read_text(errors='replace')
    lines = set(text.splitlines())
    for line in ('project: model-audit', 'system: jean', 'exit: 0', 'VERDICT round 1 OK'):
        if line not in lines:
            raise ValueError('drop lacks: ' + line)
    receipt = dict(PAD_FIELDS, drop=drop.name, drop_sha256=hashlib.sha256(drop.read_bytes()).hexdigest(),
                   checked=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'))
    return receipt


def jean(stage, proof=None):
    """Projection only, on Jean's free GPU queue, from the copied original."""
    for name in ('env.sh', 'round.sh'):
        swap(stage / name, 'HPC_SYSTEM=${HPC_SYSTEM:-nautilus}', 'HPC_SYSTEM=jean')
    round_script = stage / 'round.sh'
    swap(round_script, 'export PATH=$HOME/bin:$PATH\n', 'export PATH=$HOME/bin:$PATH\n'
         '# Jean works from the original copied over from Nautilus; it never downloads.\n'
         'export AUDIT_PROJECTION_ONLY=1\n')
    if proof is None:
        swap(round_script, 'steps=(10-install-kit.sh 20-verify.sh 30-install-reporting.sh 40-submit.sh)\n',
             '# Kit and verify only: its end log proves the relay before a job is queued.\n'
             'steps=(10-install-kit.sh 20-verify.sh 30-install-reporting.sh)\n')
    else:
        receipt = json.loads(Path(proof).read_text())
        if {key: receipt.get(key) for key in PAD_FIELDS} != PAD_FIELDS:
            raise ValueError('pad proof is not a landed Jean drop for model-audit')
        (stage / 'pad-proof.json').write_text(json.dumps(receipt, indent=2) + '\n')
    (stage / 'jobs/download.sh').unlink()
    project = stage / 'jobs/project.sh'
    swap(project, '#SBATCH -p general\n#SBATCH --qos=background\n#SBATCH --constraint=mla\n'
         '#SBATCH --gres=gpu:a100:4\n#SBATCH --account=NRLMR57635502\n',
         '#SBATCH --partition=AIML_BACK\n#SBATCH --gres=gpu:4\n#SBATCH --account=' + JEAN_ACCOUNT + '\n')
    swap(project, '[ -f "$AUDIT_WORK/state/download.done" ]\n',
         '[ -f "$AUDIT_ORIGINAL/download-manifest.json" ] || { echo "no receipt in $AUDIT_ORIGINAL"; exit 1; }\n')
    verify = stage / '20-verify.sh'
    swap(verify, 'python3 ./storage.py\n',
         '# Jean is WEKA: no show_storage or lfs quota there, so df on work is the check.\n'
         'need=$(python3 -c \'import json; print(json.load(open("needs.json"))["bytes"])\')\n'
         'free=$(df -P -B1 "$WORKDIR" | awk \'NR == 2 {print $4}\')\n'
         'echo "Jean work free: $((free / 1024 ** 3)) GB; requested: $((need / 1024 ** 3)) GB"\n'
         'mkdir -p "$WORKDIR/model-audit" "$HOME/.hpc"\n'
         'printf \'%s\\t%s\\n\' "$WORKDIR/model-audit" "$(du -sk "$WORKDIR/model-audit" | cut -f1)" \\\n'
         '    > "$HOME/.hpc/model-audit-space.tsv"\n'
         '# The rehearsal stands in a roomy disk, as storage.py does.\n'
         '[ "${AUDIT_REHEARSAL:-0}" != 1 ] || free=$((3 * 1024 ** 4))\n'
         '[ "$free" -ge "$need" ] || { echo \'insufficient work space for the declared round\'; exit 1; }\n')
    swap(verify, 'for job in jobs/download.sh jobs/project.sh; do\n', 'for job in jobs/project.sh; do\n')
    swap(verify, '    sbatch --test-only "$job"\n', '    sbatch --test-only ' + TAG + ' "$job"\n')
    submit = stage / '40-submit.sh'
    swap(submit, '[ -s "$AUDIT_WORK/state/pad-confirmed" ] || { echo \'no drop has reached the desk from this system\'; exit 1; }\n',
         '# Jean reaches the desk through the relay; a landed drop is proven at home and carried here.\n'
         'python3 -c \'import json, sys; p = json.load(open("pad-proof.json")); '
         'sys.exit(0 if (p["project"], p["system"], p["exit"], p["landed"]) == ("model-audit", "jean", 0, True) else 1)\' '
         '2>/dev/null || { echo \'no landed Jean drop is carried in pad-proof.json\'; exit 1; }\n')
    swap(submit, '    [ -f "$AUDIT_WORK/state/download.done" ] || { echo "projection-only submit missing: '
         '$AUDIT_WORK/state/download.done"; exit 1; }\n',
         '    # Jean has no download marker; the job checks every copied file against the receipt.\n')
    swap(submit, 'id=$(sbatch --parsable --output=', 'id=$(sbatch --parsable ' + TAG + ' --output=')
