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


def get_stream(path, wanted="DocumentText", occurrence=0):
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
    matches = [e for e in entries if e[0] == wanted]
    entry = matches[occurrence] if 0 <= occurrence < len(matches) else None
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



# Conservative optional postprocessors; the original raw text is preserved.
TABLE_SEPARATOR = re.compile(r'^\x8f\xa0(?:D\$\$|@@)\uffff$')


def readable_lines(text):
    """Viewing-only copy without known table tokens or observed binary trailer."""
    lines = []
    for line in text.splitlines():
        if TABLE_SEPARATOR.fullmatch(line.strip()):
            continue
        if len(line) > 300 and line.count('Ȃ') > 20 and line.count('￿') > 20:
            break
        lines.append(line.rstrip())
    return '\n'.join(lines).strip()


def reconstruct_staff_tables(text):
    """Tentatively reconstruct 1999 GEAR three-column staff tables by row markers."""
    if '受　付　内　容' not in text or '設　営　内　容' not in text:
        return ''
    items = text.splitlines()
    sections = [('受付', '受　付　内　容', '設　営　内　容'),
                ('設営', '設　営　内　容', '設営する所')]
    result = ['# 推定復元した三列表（GEARスタッフ原本の公式ビューア画像で主要行を照合済み）',
              '※線・セル結合・順序は確認できていない。数字と欄の対応は原本表示で照合。']
    for title, start, end in sections:
        try:
            a = next(i for i,v in enumerate(items) if start in v)
            b = next(i for i,v in enumerate(items[a+1:], a+1) if end in v)
        except StopIteration:
            continue
        rows, row = [], []
        for value in items[a+3:b]:
            v = value.strip()
            if TABLE_SEPARATOR.fullmatch(v):
                if row:
                    rows.append(row)
                    row = []
                continue
            if v:
                row.append(v)
        if row:
            rows.append(row)
        result += [f'\n## {title}', '| 内容 | 時間帯 | 備考 |', '|---|---|---|']
        for row in rows:
            row += [''] * (3-len(row))
            result.append('| ' + ' | '.join(x.replace('|', '\\|') for x in row) + ' |')
    return '\n'.join(result).strip() + '\n'


def embed_inventory(path):
    """Inventory binary Sanshiro OLE streams. No worksheet cell values decoded."""
    import hashlib
    import json
    streams = {}
    for name in ('EmbeddingInfo', 'Book', 'WorkSheet1', 'WorkSheet2', 'WorkSheet3'):
        try:
            blob = get_stream(path, name)
        except ValueError:
            continue
        streams[name] = {'bytes': len(blob), 'sha256': hashlib.sha256(blob).hexdigest()}
    if not streams:
        return ''
    marker = ('SNS.Worksheet.8' if 'EmbeddingInfo' in streams
              and 'SNS.Worksheet.8' in get_stream(path, 'EmbeddingInfo').decode('utf-16le', 'ignore')
              else 'unverified')
    return json.dumps({'embedded_sheet_type': marker,
                       'warning': 'Binary workbook streams found; sheet cell values NOT decoded',
                       'streams': streams}, ensure_ascii=False, indent=2) + '\n'



def embedded_snapshot_text(path):
    """Recover JSSnapShot32 display labels and amounts; not worksheet cells."""
    parts = []
    for occurrence in range(12):
        try:
            blob = get_stream(path, "\x03EmbeddedPress", occurrence)
        except ValueError:
            break
        if not blob.startswith(b"JSSnapShot32"):
            continue
        decoded = blob[:len(blob)//2*2].decode("utf-16le", "replace")
        candidates = re.findall(r"[ぁ-んァ-ヶー一-龠々Ａ-Ｚａ-ｚ０-９A-Za-z0-9\\¥,　 （）／・－:：]+", decoded)
        for value in candidates:
            value = value.strip()
            if value and value not in ("ゴシック",) and re.search("[ぁ-んァ-ヶ一-龠]|[0-9][0-9,]{2,}", value):
                parts.append(value)
    return "\n".join(parts).strip()


def fallback_text(stream):
    """Last-resort UTF-16BE text fallback, potentially truncated/garbled."""
    at = stream.find(b'TextV.01')
    if at < 0:
        return ''
    data = stream[at+10:]
    data = data[:len(data)//2*2]
    decoded = data.decode('utf-16be', 'replace')
    decoded = re.split(r'\x00[\x00-\x1f][\ue000-\uf8ff]', decoded, maxsplit=1)[0]
    return decoded.split('\x00', 1)[0].strip()


def main(argv=None):
    import argparse
    args = argparse.ArgumentParser(description='Read-only experimental JTD text extraction')
    args.add_argument('files', nargs='+', help='JTD copies (not originals)')
    args.add_argument('--fallback', action='store_true',
                      help='Try incomplete UTF16BE fallback on empty JTD')
    args.add_argument('--enhance', action='store_true',
                      help='Also create cleaned text and tentative table Markdown')
    args.add_argument('--inspect-embedded', action='store_true',
                      help='Write inventory of embedded OLE worksheet streams')
    args.add_argument('--snapshot-text', action='store_true', help='Write JSSnapShot32 displayed text; layout unverified')
    ns = args.parse_args(argv)
    failures = 0
    for name in ns.files:
        try:
            p = pathlib.Path(name)
            raw = extract_text(get_stream(p))
            source = 'primary'
            if not raw.strip() and ns.fallback:
                raw = fallback_text(get_stream(p))
                source = 'fallback_partial'
            if not raw.strip():
                raise ValueError('Empty raw extract')
            with p.with_suffix('.txt').open('x', encoding='utf-8') as out:
                out.write(raw)
            if ns.enhance:
                with p.with_suffix('.clean.txt').open('x', encoding='utf-8') as out:
                    out.write(readable_lines(raw))
                table = reconstruct_staff_tables(raw)
                if table:
                    with p.with_suffix('.tables.md').open('x', encoding='utf-8') as out:
                        out.write(table)
            if ns.snapshot_text:
                snap = embedded_snapshot_text(p)
                if snap:
                    with p.with_suffix('.snapshot.txt').open('x', encoding='utf-8') as out:
                        out.write(snap)
            if ns.inspect_embedded:
                info = embed_inventory(p)
                if info:
                    with p.with_suffix('.embedded.json').open('x', encoding='utf-8') as out:
                        out.write(info)
            print('PASS', p.name, len(raw), 'characters', source)
        except Exception as exc:
            failures += 1
            print('FAIL', name, str(exc), file=sys.stderr)
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
