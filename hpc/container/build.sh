#!/bin/bash
# build.sh -- Bake the round image on proc1 and write its checksum beside it.
# Created by Sean Egan 2026-10-14
# Usage: hpc/container/build.sh [output folder]   (bump VERSION for a new image)
set -euo pipefail
root=$(cd "$(dirname "$0")/../.." && pwd)
cd "$root"
out=${1:-/opt/ai/hpc-packages/images/model-audit}
version=$(cat hpc/container/VERSION)
[[ "$version" =~ ^[0-9A-Za-z.]+$ ]] || { echo "bad version: $version"; exit 2; }
rt=$(command -v apptainer || command -v singularity) || { echo 'no apptainer here; build on proc1'; exit 2; }
sif=$out/permafrost-$version.sif
# An image name is a promise; a new build gets a new version.
[ ! -e "$sif" ] || { echo "already built: $sif (bump hpc/container/VERSION)"; exit 1; }
mkdir -p "$out/.build/tmp" "$out/.build/cache"
# Big scratch goes to disk, not the RAM-backed /tmp.
export APPTAINER_TMPDIR=$out/.build/tmp APPTAINER_CACHEDIR=$out/.build/cache
echo "building $sif with $("$rt" --version)"
nice -n 19 "$rt" build --fakeroot --build-arg "VERSION=$version" "$sif.part" hpc/container/permafrost.def
mv "$sif.part" "$sif"
(cd "$out" && sha256sum "permafrost-$version.sif" > "permafrost-$version.sif.sha256")
"$rt" exec "$sif" cat /etc/permafrost-image.txt > "$out/permafrost-$version.txt"
cat "$out/permafrost-$version.txt"
echo "sha256: $(cut -d' ' -f1 "$sif.sha256")"
echo "size: $(du -B1 "$sif" | awk '{printf "%.2f GB", $1 / 1e9}')"
