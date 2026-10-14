#!/bin/bash
# run-check.sh -- Check the image, its pins and the GPUs before a job does any work.
# Created by Sean Egan 2026-10-14
# Runs inside the image: run-check.sh <compute-requirements.txt>
# AUDIT_EXPECT_GPUS=N makes N visible GPUs a must; 0 or unset skips the GPU part.
set -uo pipefail
wanted=${1:?usage: run-check.sh compute-requirements.txt}
image=${PERMAFROST_IMAGE:-/etc/permafrost-image.txt}
[ -r "$image" ] || { echo "FAIL not inside the permafrost image (no $image)"; exit 2; }
[ -r "$wanted" ] || { echo "FAIL cannot read $wanted"; exit 2; }
echo "image: $(sed -n 's/^version: //p' "$image") built $(sed -n 's/^built: //p' "$image")"
python3 - "$wanted" "$image" <<'PY'
import hashlib
import importlib.metadata as meta
import re
import sys

wanted, image = sys.argv[1], sys.argv[2]
record = dict(line.split(': ', 1) for line in open(image).read().splitlines() if ': ' in line)
print('python: ' + sys.version.split()[0])
digest = hashlib.sha256(open(wanted, 'rb').read()).hexdigest()
if digest == record.get('requirements sha256'):
    print('requirements: same file the image was built from')
else:
    print('requirements: changed since the image build; checking pin by pin')
bad = 0
count = 0
for line in open(wanted).read().splitlines():
    line = line.split('#', 1)[0].strip()
    if not line:
        continue
    match = re.fullmatch(r'([A-Za-z0-9._-]+)==([A-Za-z0-9._+!-]+)', line)
    if not match:
        print('FAIL pin is not exact: ' + line[:80])
        bad += 1
        continue
    name, version = match.groups()
    count += 1
    try:
        have = meta.version(name)
    except meta.PackageNotFoundError:
        have = 'missing'
    if have.split('+')[0] != version.split('+')[0]:
        print('FAIL {} is {}, pinned {}'.format(name, have, version)[:100])
        bad += 1
if bad:
    print('FAIL {} of {} pins differ from {}'.format(bad, count, wanted.rsplit('/', 1)[-1])[:100])
    raise SystemExit(3)
print('pins: all {} match'.format(count))
PY
rc=$?
[ "$rc" = 0 ] || exit "$rc"
driver=none
if command -v nvidia-smi >/dev/null 2>&1; then
    driver=$(nvidia-smi --query-gpu=driver_version --format=csv,noheader 2>/dev/null | head -1)
elif [ -r /proc/driver/nvidia/version ]; then
    driver=$(grep -o 'Kernel Module  *[0-9.]*' /proc/driver/nvidia/version | awk '{print $3}')
fi
echo "driver: ${driver:-none}"
python3 - "${AUDIT_EXPECT_GPUS:-0}" "${driver:-none}" <<'PY'
import sys

expect, driver = int(sys.argv[1]), sys.argv[2]
import torch
print('torch: {} built for CUDA {}'.format(torch.__version__, torch.version.cuda))
if expect <= 0:
    print('GPU check skipped: this job expects no GPU')
    raise SystemExit(0)
try:
    seen = torch.cuda.device_count() if torch.cuda.is_available() else 0
except Exception as error:
    seen = 0
    print('cuda error: ' + str(error).splitlines()[0][:88])
if seen < expect:
    print('FAIL torch sees {} of {} GPUs (driver {}, CUDA {})'.format(seen, expect, driver, torch.version.cuda)[:100])
    raise SystemExit(4)
for index in range(seen):
    try:
        x = torch.ones(256, 256, device='cuda:{}'.format(index))
        total = float((x @ x).sum())
        assert total == 256.0 ** 3, total
    except Exception as error:
        print('FAIL GPU {} cannot run a matmul: {}'.format(index, str(error).splitlines()[0])[:100])
        raise SystemExit(4)
    print('GPU {}: {} ok'.format(index, torch.cuda.get_device_name(index))[:100])
print('GPUs: {} of {} ready'.format(seen, expect))
PY
rc=$?
[ "$rc" = 0 ] || exit "$rc"
echo 'VERDICT image OK'
