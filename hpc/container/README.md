# The round image

<!-- Created by Sean Egan 2026-10-14 -->

One Apptainer image holds the Python every model round runs on: Python 3.11.15,
the exact pins in `hpc/rounds/1/compute-requirements.txt` (rounds 2 and 4 use
the same pins), torch 2.8.0 built for CUDA 12.8, and the versions those pins pull
in. That's all it holds. The audit code rides in the round bundle, so a code fix
never needs a new image. The home rehearsal and the cluster job run the same
libraries, which is the point.

## Rebuild

On proc1, from a checkout of this repo:

```bash
hpc/container/build.sh            # writes /opt/ai/hpc-packages/images/model-audit/permafrost-<VERSION>.sif
```

Bump `VERSION` first; the script won't overwrite an image that already exists.
It writes the `.sha256` beside the image and prints the size. Inside the image,
`/etc/permafrost-image.txt` records the version, the build time and the sha256 of
the requirements file it was built from. If the pins change, change the list in
`permafrost.def` too; the build stops when the two disagree, and so does
`tests/test_container.py`.

## How a round uses it

Copy the image to the cluster once with a push card, then build the round with it:

```bash
python3 hpc/bundle.py build --needs '...' \
    --image /p/work1/sdegan/images/permafrost-1.sif --image-sha256 <sha256>
```

The jobs then run their Python through `apptainer exec --nv --cleanenv` with
work, home and the originals bound, instead of building a venv from the
wheelhouse. Every job starts with `run-check.sh`: it checks the image's sha256,
compares every installed version with the round's pins, prints torch, CUDA and
the driver, and stops in one short line if torch can't see the GPUs. The
verify step runs the same check without a GPU on the login node before anything
is queued. A system with only podman gets a plain refusal.

Without `--image` the bundle is built exactly as before.

## Jean

Jean takes the original copied over from Nautilus and runs projection only, on
AIML_BACK. Jean can't reach the desk directly, so the first Jean round is
kit-and-verify (`--system jean --kit-and-verify`, steps 10 to 30, no job). Once
its end log lands on the pad, make the pad proof and build the real round:

```bash
python3 hpc/bundle.py pad-proof /srv/hpcpad/in/model-audit/jean/<end log>
python3 hpc/bundle.py build --system jean --pad-proof .tmp/hpc/jean-pad-proof.json --image ... --needs '...'
```

## Rehearse

`hpc/rehearse_image.py <empty folder> --dry-run --image <sif> --image-sha256 <sha>`
runs the stub round with every Python step inside the image: the Nautilus image
build, both Jean rounds, a damaged copy and a missing pad proof. It needs
apptainer, so run it on proc1.
