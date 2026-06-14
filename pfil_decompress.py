#!/usr/bin/env python3
"""
Decompressor for "Against Rome" (2003) PFIL-wrapped data files.

Reverse-engineered directly from Against_Rome.exe:
 - Header check happens around VA 0x581ee0 (magic 'PFIL')
 - Compression type 2 dispatches to an LZSS codec (codec init at
   VA ~0x565c00, decode loop at VA ~0x565d90-0x566100)

FILE LAYOUT (CONFIRMED):
  - 32-byte PFIL header (8 little-endian dwords):
      magic, field1, version, comp_type, uncompressed_size,
      field5, field6, field7
    `field1` == 64 == TOTAL header size (PFIL header + sub-header),
    NOT the size of the PFIL header alone.
  - 32-byte sub-header (purpose still unknown / unparsed) at offset 32.
  - LZSS-compressed payload starts at offset 64.

  Previous versions of this script started the LZSS stream at offset 32,
  which fed the 32-byte sub-header into the decoder as if it were
  compressed data. This desynced the very first flag byte and back-
  reference, producing output that was technically "decoded" but mostly
  garbage (92%+ literal 0x20 bytes for objdata.dat). Starting at offset
  64 instead produces a clean decode (verified byte-for-byte against
  boden.ini, which decodes to fully readable INI text; objdata.dat
  decodes to exactly `uncompressed_size` bytes with the expected
  [float32 1.0][byte 0x01][float32 stat] record pattern).

Algorithm = classic Haruhiko Okumura LZSS:
  N (window size)   = 4096  (0x1000)
  F (max match len) = 18
  THRESHOLD         = 2
  text_buf size     = N + F - 1, positions [0, N-F-1] pre-filled with 0x20
  r starts at N - F = 4078

Flag byte: bit=1 -> literal byte follows
           bit=0 -> 2-byte back-reference:
               i = byte1 | ((byte2 & 0xF0) << 4)
               len = (byte2 & 0x0F) + THRESHOLD + 1   (i.e. 3..18)
               copy `len` bytes from text_buf[(i+k) & 0xFFF]
"""

import struct
import sys

N = 4096
F = 18
THRESHOLD = 2

PFIL_HEADER_SIZE = 32      # the 8-dword magic/version/etc. header
TOTAL_HEADER_SIZE = 64     # PFIL header + 32-byte sub-header before payload


def lzss_decompress(src: bytes, expected_size: int = None) -> bytes:
    text_buf = bytearray(b' ' * (N + F - 1))
    r = N - F
    out = bytearray()
    flags = 0
    i = 0
    n = len(src)

    while i < n:
        flags >>= 1
        if (flags & 0x100) == 0:
            if i >= n:
                break
            flags = src[i] | 0xFF00
            i += 1

        if flags & 1:
            # literal
            if i >= n:
                break
            c = src[i]
            i += 1
            out.append(c)
            text_buf[r] = c
            r = (r + 1) & (N - 1)
        else:
            # back-reference
            if i + 1 >= n:
                break
            b1 = src[i]
            b2 = src[i + 1]
            i += 2
            pos = b1 | ((b2 & 0xF0) << 4)
            length = (b2 & 0x0F) + THRESHOLD + 1  # 3..18
            for k in range(length):
                c = text_buf[(pos + k) & (N - 1)]
                out.append(c)
                text_buf[r] = c
                r = (r + 1) & (N - 1)

        if expected_size is not None and len(out) >= expected_size:
            break

    if expected_size is not None:
        out = out[:expected_size]
    return bytes(out)


def decode_pfil(data: bytes):
    """Parse the PFIL header + sub-header and decompress the payload."""
    if data[:4] != b'PFIL':
        raise ValueError("Not a PFIL file")

    # 8 little-endian dwords = 32-byte PFIL header
    hdr = struct.unpack_from('<8I', data, 0)
    magic, field1, version, comp_type, uncompressed_size, field5, field6, field7 = hdr

    # field1 (==64 in observed files) is the TOTAL size of
    # PFIL header + sub-header. Fall back to 64 if it looks bogus.
    header_total = field1 if field1 >= PFIL_HEADER_SIZE else TOTAL_HEADER_SIZE
    payload = data[header_total:]

    if comp_type == 2:
        out = lzss_decompress(payload, expected_size=uncompressed_size)
    elif comp_type in (0, 1):
        # Possibly stored/raw - just slice to expected size
        out = payload[:uncompressed_size]
    else:
        raise ValueError(f"Unknown compression type {comp_type}")

    return out, hdr


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("usage: pfil_decompress.py <file> [outfile]")
        sys.exit(1)

    data = open(sys.argv[1], 'rb').read()
    out, hdr = decode_pfil(data)
    print(f"header: magic={hdr[0]:#x} field1={hdr[1]} version={hdr[2]} "
          f"comp_type={hdr[3]} uncompressed_size={hdr[4]} "
          f"field5={hdr[5]} field6={hdr[6]} field7={hdr[7]:#x}")
    print(f"decoded {len(out)} bytes")

    if len(sys.argv) > 2:
        with open(sys.argv[2], 'wb') as f:
            f.write(out)
    else:
        try:
            print(out.decode('latin-1'))
        except Exception as e:
            print("decode error:", e)
