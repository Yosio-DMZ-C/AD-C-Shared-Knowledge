#!/usr/bin/env python3
"""Read-only JTD/OLE2 text extractor (experimental, not layout preserving).
Input is never changed; output .txt is created exclusively (no overwrite).
Algorithm follows the locally verified 2026-11-16 Ichitaro recovery prototype.
"""
import pathlib
import re
import struct
import sys

FREE = 0xFFFFFFFF
END = 0xFFFFFFFE


def get_stream(path, wanted="DocumentText"):
    data = pathlib.Path(path).read_bytes()
    if data[:8] != bytes.fromhex("D0CF11E0A1B11AE1"):
        raise ValueError("Not an OLE2 compound document")
    sector_size = 1 << struct.unpack_from("<H", data, 30)[0]
    mini_size = 1 << struct.unpack_from("<H", data, 32)[0]
    if sector_size not in (512, 4096) or mini_size != 64:
        raise ValueError("Unsupported OLE sector layout")

    def sector(i):
        off = (i + 1) * sector_size
        if i >= 0xFFFFFFFA or off + sector_size > len(data):
            raise ValueError("Invalid OLE sector index")
        return data[off:off + sector_size]

    difat = list(struct.unpack_from("<109I", data, 76))
    nxt = struct.unpack_from("<I", data, 68)[0]
    for _ in range(struct.unpack_from("<I", data, 72)[0]):
        raw = sector(nxt)
        difat.extend(struct.unpack_from("<" + "I" * (sector_size // 4 - 1), raw))
        nxt = struct.unpack_from("<I", raw, sector_size - 4)[0]
    fat_bytes = b"".join(sector(i) for i in difat if i < 0xFFFFFFFA)
    fat = struct.unpack("<" + "I" * (len(fat_bytes) // 4), fat_bytes)

    def chain(start, mapping, limit=100000):
        seen = set()
        cur = start
        while cur not in (END, FREE) and cur < 0xFFFFFFFA:
            if cur in seen or cur >= len(mapping) or len(seen) >= limit:
                raise ValueError("Invalid or cyclic OLE allocation chain")
            seen.add(cur)
            yield cur
            cur = mapping[cur]

    directory = b"".join(sector(i) for i in chain(struct.unpack_from("<I", data, 48)[0], fat))
    entries = []
    for offset in range(0, len(directory), 128):
        row = directory[offset:offset + 128]
        if len(row) != 128:
            continue
        length = struct.unpack_from("<H", row, 64)[0]
        if not 2 <= length <= 64:
            continue
        name = row[:length - 2].decode("utf-16le", "replace")
        entries.append((name, row[66], struct.unpack_from("<I", row, 116)[0],
                        struct.unpack_from("<Q", row, 120)[0]))
    entry = next((e for e in entries if e[0] == wanted), None)
    if entry is None:
        raise ValueError("DocumentText stream not found")
    _, _, start, size = entry
    cutoff = struct.unpack_from("<I", data, 56)[0]
    if size >= cutoff:
        return b"".join(sector(i) for i in chain(start, fat))[:size]

    root = next(e for e in entries if e[1] == 5)
    mini_data = b"".join(sector(i) for i in chain(root[2], fat))[:root[3]]
    mini_first = struct.unpack_from("<I", data, 60)[0]
    mini_fat_raw = b"".join(sector(i) for i in chain(mini_first, fat))
    mini_fat = struct.unpack("<" + "I" * (len(mini_fat_raw) // 4), mini_fat_raw)
    return b"".join(mini_data[i * mini_size:(i + 1) * mini_size]
                    for i in chain(start, mini_fat))[:size]


def extract_text(stream):
    if not stream.startswith(b"SsmgV.01"):
        raise ValueError("Unrecognized Ichitaro DocumentText version")
    at = stream.find(b"CTextV.01")
    marker_len = 9
    if at < 0:
        at = stream.find(b"TextV.01")
        marker_len = 8
    if at < 0:
        raise ValueError("JTD text section marker missing")
    index = at + marker_len + 1
    index += index % 2
    lines, current = [], []
    active = False

    def flush():
        if "".join(current).strip():
            lines.append("".join(current))
        current.clear()

    while index + 1 < len(stream):
        val = (stream[index] << 8) | stream[index + 1]
        if val == 0x1C:
            flush()
            index += 2
            while index + 1 < len(stream) and ((stream[index] << 8) | stream[index + 1]) != 0x1F:
                index += 2
            index += 2
            active = True
            continue
        if val == 0x1F:
            active = True
            index += 2
            continue
        if not active:
            index += 2
            continue
        if val in (0xA, 0xE):
            flush()
            active = val != 0xE
            index += 2
            continue
        if val >= 32 and not 0xD800 <= val <= 0xDFFF:
            current.append(chr(val))
        index += 2
    flush()
    while lines and not re.search("[\u3040-\u30ff\u4e00-\u9fff]", lines[-1]):
        lines.pop()
    return "\n".join(lines)


def main(argv):
    if len(argv) < 2:
        print("Usage: python jtd_text_extract.py COPY1.jtd [COPY2.jtd ...]", file=sys.stderr)
        return 2
    failed = 0
    for name in argv[1:]:
        src = pathlib.Path(name)
        dest = src.with_suffix(".txt")
        try:
            if src.resolve() == dest.resolve():
                raise ValueError("Input would equal output")
            body = extract_text(get_stream(src))
            if not body.strip():
                raise ValueError("Empty text extraction")
            with dest.open("x", encoding="utf-8") as file:
                file.write(body)
            print(f"PASS {src} -> {dest} {len(body)} chars, {len(body.splitlines())} lines")
        except Exception as exc:
            failed += 1
            print(f"FAIL {src}: {exc}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
