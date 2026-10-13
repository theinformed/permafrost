# gguf.py -- Read the metadata prefix of a packed checkpoint, not its tensors.
# Created by LT Sean Egan, PhD 2026-10-13
# Modified: SDE 2026-10-13  parse typed values through bounded HTTP ranges.
import io
import re
import struct
import time

from huggingface_hub import hf_hub_url
from .hub import BudgetExpired

MAX_HEADER = 64 * 1024 * 1024
MAX_ITEMS = 2_000_000
SCALARS = {0: "B", 1: "b", 2: "H", 3: "h", 4: "I", 5: "i", 6: "f",
           7: "?", 10: "Q", 11: "q", 12: "d"}


class RangeReader:
    """Fetch only bytes the metadata parser asks for; reject ignored ranges."""

    def __init__(self, hub, repo, revision, filename):
        self.hub = hub
        self.url = hf_hub_url(repo, filename, revision=revision)
        self.position = 0
        self.requests = 0
        self.buffer = bytearray()
        self.reserve = 0

    def read(self, size):
        """Require a matching partial reply before reading any response body."""
        if size == 0:
            return b""
        if len(self.buffer) >= size:
            result = bytes(self.buffer[:size])
            del self.buffer[:size]
            return result
        start = self.position
        # The parser knows a lower bound for metadata still to come. Read ahead
        # within that bound so a token array does not cost a request per word.
        length = max(size - len(self.buffer), min(65536, size + self.reserve - len(self.buffer)))
        end = start + length - 1
        if size < 0 or end >= MAX_HEADER or self.requests >= 1000:
            raise ValueError("GGUF metadata exceeds the read budget")
        self.hub.pause()
        with self.hub.session.get(self.url, headers={
            "Range": f"bytes={start}-{end}", "Accept-Encoding": "identity",
        }, stream=True, timeout=15) as response:
            response.raise_for_status()
            match = re.fullmatch(r"bytes (\d+)-(\d+)/(\d+|\*)", response.headers.get("Content-Range", ""))
            if response.status_code != 206 or not match or tuple(map(int, match.groups()[:2])) != (start, end):
                raise ValueError("server did not honor the metadata byte range")
            if response.headers.get("Content-Encoding", "identity") != "identity":
                raise ValueError("compressed GGUF byte range")
            result = bytearray()
            for chunk in response.iter_content(min(length + 1, 65536)):
                if getattr(self.hub, "deadline", None) and time.monotonic() >= self.hub.deadline:
                    raise BudgetExpired("GGUF metadata read reached the time budget")
                result.extend(chunk)
                if len(result) > length:
                    raise ValueError("GGUF range reply exceeds requested bytes")
        if len(result) != length:
            raise ValueError("truncated GGUF byte range")
        self.position += length
        self.requests += 1
        self.buffer.extend(result)
        result = bytes(self.buffer[:size])
        del self.buffer[:size]
        return result


class Parser:
    """Decode metadata types and stop before the tensor directory."""

    def __init__(self, stream):
        self.stream = stream
        self.endian = "<"
        self.position = 0
        self.reserve = 0

    def take(self, size):
        """Reject lengths from corrupt headers before allocating their contents."""
        if size < 0 or self.position + size > MAX_HEADER:
            raise ValueError("GGUF metadata exceeds 64 MiB")
        if isinstance(self.stream, RangeReader):
            self.stream.reserve = self.reserve
        data = self.stream.read(size)
        self.position += len(data)
        if len(data) != size:
            raise ValueError("truncated GGUF header")
        return data

    def number(self, kind):
        """Read one scalar with the file's byte order."""
        return struct.unpack(self.endian + kind, self.take(struct.calcsize(kind)))[0]

    def string(self):
        """Decode a length-prefixed UTF-8 field."""
        return self.take(self.number("Q")).decode("utf-8")

    def value(self, kind):
        """Read flat arrays too; nested arrays are outside the file format."""
        if kind in SCALARS:
            return self.number(SCALARS[kind])
        if kind == 8:
            return self.string()
        if kind != 9:
            raise ValueError(f"unknown GGUF metadata type {kind}")
        item_type, count = self.number("I"), self.number("Q")
        if count > MAX_ITEMS or item_type not in (*SCALARS, 8):
            raise ValueError("invalid GGUF array")
        if item_type in SCALARS:
            code = SCALARS[item_type]
            data = self.take(count * struct.calcsize(code))
            return [item[0] for item in struct.iter_unpack(self.endian + code, data)]
        result = []
        outer = self.reserve
        for index in range(count):
            self.reserve = outer + (count - index - 1) * 8
            result.append(self.string())
        self.reserve = outer
        return result


def parse_header(source):
    """Return header metadata and the exact offset where it ends."""
    parser = Parser(io.BytesIO(source) if isinstance(source, bytes) else source)
    magic = parser.take(4)
    if magic not in (b"GGUF", b"FUGG"):
        raise ValueError("invalid GGUF magic")
    parser.endian = ">" if magic == b"FUGG" else "<"
    version = parser.number("I")
    if version not in (2, 3):
        raise ValueError(f"unsupported GGUF version {version}")
    tensors, count = parser.number("Q"), parser.number("Q")
    if count > MAX_ITEMS:
        raise ValueError("too many GGUF metadata entries")
    metadata = {}
    for index in range(count):
        parser.reserve = (count - index - 1) * 13
        key = parser.string()
        if key in metadata:
            raise ValueError("duplicate GGUF metadata key")
        metadata[key] = parser.value(parser.number("I"))
    return {"version": version, "tensor_count": tensors, "metadata": metadata,
            "metadata_bytes": parser.position}
