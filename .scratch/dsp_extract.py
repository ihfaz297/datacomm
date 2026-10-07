"""Recon helper: full file listing + PDF text extraction -> .scratch reports.

Writes everything to files (and prints a short summary) because raw stdout from
long listings has been unreliable in this environment.
"""
import pathlib
import fitz  # PyMuPDF

ROOT = pathlib.Path(r"C:\Users\ADIB\OneDrive\Desktop\datacomm")
SCRATCH = ROOT / ".scratch"
SKIP_DIRS = {".git"}

listing = []
for p in sorted(ROOT.rglob("*")):
    if p.is_dir() or any(part in SKIP_DIRS for part in p.parts):
        continue
    try:
        listing.append(f"{p.relative_to(ROOT)}\t{p.stat().st_size}")
    except OSError as e:
        listing.append(f"{p.relative_to(ROOT)}\tERROR {e}")
(SCRATCH / "listing.txt").write_text("\n".join(listing), encoding="utf-8")

report = [f"files: {len(listing)}", ""]
for p in sorted(ROOT.rglob("*.pdf")):
    if any(part in SKIP_DIRS for part in p.parts):
        continue
    try:
        doc = fitz.open(p)
        pages = [page.get_text("text") for page in doc]
        doc.close()
    except Exception as e:  # noqa: BLE001
        report.append(f"PDF FAIL {p.name}: {type(e).__name__}: {e}")
        continue
    text = "\n=== PAGE BREAK ===\n".join(pages)
    target = SCRATCH / (p.stem.replace(" ", "_") + ".txt")
    target.write_text(text, encoding="utf-8")
    images = sum(len(page.get_images(full=True)) for page in fitz.open(p))
    report.append(f"{p.name}\tpages={len(pages)}\tchars={len(text.strip())}"
                  f"\timages={images}\t-> {target.name}")
    report.append("   head: " + " ".join(text.split())[:200])
(SCRATCH / "pdf_report.txt").write_text("\n".join(report), encoding="utf-8")
print("\n".join(report))
