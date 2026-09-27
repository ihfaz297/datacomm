"""Dump text of the DSP/ML/CE PDFs into .scratch so I can grep the real syllabus."""
import pathlib
import fitz

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / ".scratch"
TARGETS = [
    "DSP/Chapter 2.pdf",
    "DSP/Chapter 3_z_Transform.pdf",
    "DSP/Chapter 4 Problems.pdf",
    "DSP/Chapter 4.8.6_4.8.7.pdf",
    "DSP/DSP_Chapter4_Frequency_Analysis_CTFT.pdf",
    "DSP/Whole-syllabus-course.pdf",
    "DSP/CSE 0714 3276- Assignment 1.pdf",
    "DSP/CSE 0714 3276- Assignment 2.pdf",
    "DSP/CSE 0714 3276- Assignment 3.pdf",
    "DSP/CSE 0714 3276- Assignment 4.pdf",
    "CE/Copy of SolnCSE630 SUST_TT1.pdf",
    "ML/Questions/19_tt1.pdf",
    "ML/Questions/19_tt2.pdf",
    "ML/Questions/machine learning .pdf",
]

for rel in TARGETS:
    src = ROOT / rel
    if not src.exists():
        print(f"MISSING {rel}")
        continue
    try:
        doc = fitz.open(src)
        pages = [pg.get_text() for pg in doc]
        doc.close()
    except Exception as exc:  # noqa: BLE001
        print(f"FAIL {rel}: {exc}")
        continue
    dest = OUT / (src.stem.replace(" ", "_") + ".txt")
    dest.write_text("\n\n=== PAGE BREAK ===\n\n".join(pages), encoding="utf-8")
    print(f"{rel} -> {dest.name} : {len(pages)} pages, {sum(len(p) for p in pages)} chars")
