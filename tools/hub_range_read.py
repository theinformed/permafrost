#!/usr/bin/env python3
# hub_range_read.py -- Read one tensor from several hub repositories by byte range and compare the copies.
# Created by LT Sean Egan, PhD
"""Fetch the same tensor from two or more safetensors checkpoints on the hub without downloading them.

Each repository is given as ``owner/name@revision``. The script reads the shard index (or the single
``model.safetensors`` header when there is no index), locates the tensor's byte range from the shard header,
fetches that range with an HTTP range request, decodes it (bfloat16, float16 or float32) and prints, for every
pair of repositories in the order given, the relative difference and whether the bytes are equal. For each copy
it also prints the number of distinct values per block of 64 entries (median and maximum over the first N
blocks) and the fraction of entries that are exactly zero, the signature of a 4-bit round trip.

A hub token is read from the ``HF_TOKEN`` environment variable when present and is never printed.

Example:
    HF_TOKEN=$(cat ~/.hpc/hf-token) tools/hub_range_read.py \\
        --tensor model.language_model.layers.30.self_attn.k_proj.weight \\
        google/gemma-4-31B-it@842da379 TheDrummer/Artemis-31B-v1.1@d613e5a4 sh0ck0r/Artemis-31B-v1.1-heretic@b3bdce6a
"""
import argparse
import json
import os
import struct
import sys

import numpy as np
import requests
from huggingface_hub import hf_hub_url

INDEX_FILE = "model.safetensors.index.json"
SINGLE_FILE = "model.safetensors"


def _headers():
    token = os.environ.get("HF_TOKEN")
    return {"Authorization": "Bearer " + token} if token else {}


def _get(url, byte_range):
    response = requests.get(url, headers={**_headers(), "Range": byte_range}, allow_redirects=True, timeout=120)
    response.raise_for_status()
    return response.content


def safetensors_header(repo, revision, filename):
    """Return (url, header_length, header) for one safetensors file."""
    url = hf_hub_url(repo, filename, revision=revision)
    length = struct.unpack("<Q", _get(url, "bytes=0-7")[:8])[0]
    header = json.loads(_get(url, f"bytes=8-{8 + length - 1}"))
    return url, length, header


def shard_for(repo, revision, name):
    """Name the shard that holds the tensor, from the index when the repository has one."""
    try:
        index = json.loads(_get(hf_hub_url(repo, INDEX_FILE, revision=revision), "bytes=0-"))
    except requests.HTTPError:
        return SINGLE_FILE
    try:
        return index["weight_map"][name]
    except KeyError:
        raise SystemExit(f"{repo}@{revision}: no tensor named {name} in {INDEX_FILE}")


def read_tensor(repo, revision, name):
    """Fetch one tensor by byte range and return it as a float32 array."""
    filename = shard_for(repo, revision, name)
    url, length, header = safetensors_header(repo, revision, filename)
    if name not in header:
        raise SystemExit(f"{repo}@{revision}: no tensor named {name} in {filename}")
    meta = header[name]
    start, end = meta["data_offsets"]
    raw = _get(url, f"bytes={8 + length + start}-{8 + length + end - 1}")
    dtype = meta["dtype"]
    if dtype == "BF16":
        bits = np.frombuffer(raw, dtype=np.uint16).astype(np.uint32) << 16
        values = bits.view(np.float32)
    elif dtype == "F16":
        values = np.frombuffer(raw, dtype=np.float16).astype(np.float32)
    elif dtype == "F32":
        values = np.frombuffer(raw, dtype=np.float32)
    else:
        raise SystemExit(f"{repo}@{revision}: {name} is stored as {dtype}, which this script does not decode")
    return values.reshape(meta["shape"]), dtype


def block_statistics(values, blocks, width=64):
    """Distinct values per block (median, maximum) over the first ``blocks`` blocks, and the zero fraction."""
    flat = values.reshape(-1)
    usable = (flat.size // width) * width
    rows = flat[:usable].reshape(-1, width)[:blocks]
    distinct = np.array([np.unique(row).size for row in rows])
    return float(np.median(distinct)), int(distinct.max()), float((values == 0).mean())


def relative_difference(a, b):
    return float(np.linalg.norm(a - b) / np.linalg.norm(a))


def parse_repo(spec):
    if "@" not in spec:
        raise SystemExit(f"{spec}: give the repository as owner/name@revision")
    repo, revision = spec.split("@", 1)
    return repo, revision


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--tensor", action="append", required=True, help="tensor name; repeat for several")
    parser.add_argument("--blocks", type=int, default=4000, help="blocks of 64 to count distinct values over")
    parser.add_argument("repos", nargs="+", help="owner/name@revision, two or more")
    args = parser.parse_args(argv)
    repos = [parse_repo(spec) for spec in args.repos]
    if len(repos) < 2:
        parser.error("give at least two repositories")
    for name in args.tensor:
        print(name)
        tensors = {}
        for repo, revision in repos:
            tensors[(repo, revision)], dtype = read_tensor(repo, revision, name)
            shape = "x".join(str(n) for n in tensors[(repo, revision)].shape)
            print(f"  {repo}@{revision[:8]}: {dtype} {shape}")
        keys = list(tensors)
        for i, left in enumerate(keys):
            for right in keys[i + 1:]:
                a, b = tensors[left], tensors[right]
                equal = a.shape == b.shape and np.array_equal(a, b)
                diff = relative_difference(a, b) if a.shape == b.shape else float("nan")
                print(f"  {left[0]} -> {right[0]}: relative difference {diff:.5f}, bytes equal {equal}")
        for key, values in tensors.items():
            if values.ndim < 2:
                continue
            median, largest, zeros = block_statistics(values, args.blocks)
            print(f"  {key[0]}: distinct values per block of 64: median {median:g}, max {largest}; "
                  f"zero fraction {zeros:.4f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
