"""Probe DSP PDFs: page count, how many pages carry real text, and samples."""
import os
import fitz

REPO = r"C:\Users\ADIB\OneDrive\Desktop\datacomm\DSP"

targets = [
    ("MITRA", "Sanjit K Mitra Digital Signal Processing A Computer-Based Approach, 2e with DSP Laboratory using MATLAB.pdf"),
    ("Z", "Chapter 3_z_Transform.pdf"),
    ("CH4P", "Chapter 4 Problems.pdf"),
    ("486", "Chapter 4.8.6_4.8.7.pdf"),
    ("CTFT", "DSP_Chapter4_Frequency_Analysis_CTFT.pdf"),
    ("CH2", "Chapter 2.pdf"),
    ("SYL", "Whole-syllabus-course.pdf"),
    ("A1", "CSE 0714 3276- Assignment 1.pdf"),
    ("A2", "CSE 0714 3276- Assignment 2.pdf"),
    ("A3", "CSE 0714 3276- Assignment 3.pdf"),
    ("A4", "CSE 0714 3276- Assignment 4.pdf"),
]

out = []
for tag, name in targets:
    path = os.path.join(REPO, name)
    out.append("=" * 72)
    out.append("{}  ::  {}".format(tag, name))
    if not os.path.exists(path):
        out.append("  MISSING")
        continue
    try:
        doc = fitz.open(path)
    except Exception as exc:  # noqa
        out.append("  OPEN ERROR: {}".format(exc))
        continue
    out.append("  pages: {}".format(doc.page_count))
    rich, samples = [], []
    for i in range(doc.page_count):
        try:
            t = doc[i].get_text().strip()
        except Exception:
            t = ""
        if len(t) > 40:
            rich.append(i + 1)
            if len(samples) < 5:
                samples.append("  --- p{} ---\n{}".format(i + 1, t[:600]))
    out.append("  pages_with_text({}): {}".format(
        len(rich), rich[:60] if len(rich) > 60 else rich))
    out.extend(samples)
    doc.close()

# also probe HEIC headers so we know what tools are needed
out.append("=" * 72)
for extra in [r"TT\TT2.HEIC", r"Final Question\IMG_6120.HEIC",
              r"Final Question\IMG_6121.HEIC"]:
    p = os.path.join(REPO, extra)
    out.append("{}  exists={}  size={}".format(
        extra, os.path.exists(p), os.path.getsize(p) if os.path.exists(p) else "-"))

dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "probe_out.txt")
with open(dest, "w", encoding="utf-8") as fh:
    fh.write("\n".join(out))
print("wrote", dest)
