"""Markdown hygiene check for the DSP/study pack.

- table blocks must have the same number of pipes in every row
- flags mojibake (double-encoded UTF-8) in the raw bytes
- reports UTF-8 decode errors and BOMs

Run:  python .scratch/md_tables.py
"""
import glob
import io
import os
import re

PIPE = re.compile(r"(?<!\\)\|")           # a real cell delimiter, not an escaped \| inside a cell


def ncols(row):
    return len(PIPE.findall(row))


BAD = []

for path in sorted(glob.glob(os.path.join("DSP", "study", "*.md"))):
    raw = open(path, "rb").read()
    name = os.path.basename(path)
    if raw.startswith(b"\xef\xbb\xbf"):
        BAD.append(f"{name}: has a UTF-8 BOM")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as e:
        BAD.append(f"{name}: NOT valid UTF-8 -> {e}")
        continue
    for bad_seq in ("\u00c3\u00a2\u20ac", "\u00c2\u00a7", "\u00ce\u00b1", "\u00cf\u20ac", "\\u00"):
        if bad_seq in text:
            BAD.append(f"{name}: mojibake {bad_seq!r}")
    lines = text.split("\n")
    i, ntab = 0, 0
    while i < len(lines):
        if lines[i].lstrip().startswith("|") and lines[i].count("|") >= 2:
            block = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                block.append((i + 1, lines[i]))
                i += 1
            ntab += 1
            counts = {ln: ncols(row) for ln, row in block}
            uniq = sorted(set(counts.values()))
            if len(uniq) > 1:
                detail = ", ".join(f"line {ln}: {c} pipes" for ln, c in sorted(counts.items()))
                BAD.append(f"{name}: table #{ntab} (starts line {block[0][0]}) uneven -> {detail}")
        else:
            i += 1
    print(f"{name:34s} utf-8 ok, {ntab} tables, {len(text.splitlines())} lines")

print("\n" + "=" * 80)
print("TABLE/ENCODING PROBLEMS:" if BAD else "NO TABLE OR ENCODING PROBLEMS")
for b in BAD:
    print("  -", b)
