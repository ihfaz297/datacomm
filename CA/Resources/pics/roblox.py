import sys
import subprocess

try:
    import fitz
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyMuPDF"])
    import fitz

pdf_path = r"C:\Users\ADIB\OneDrive\Desktop\All in one\datacomm\CA\Resources\MK.Computer.Organization.and.Design.4th.Edition.Oct.2011.pdf"
try:
    doc = fitz.open(pdf_path)
    for i in range(len(doc)):
        if(i < 400 or i > 900):
            continue
        page = doc.load_page(i)
        pix = page.get_pixmap(dpi=300)
        out_path = rf"C:\Users\ADIB\OneDrive\Desktop\All in one\datacomm\CA\Resources\pics\page_{i+1}.png"
        pix.save(out_path)
    print(f"Successfully converted {len(doc)} pages to images.")
except Exception as e:
    import traceback
    traceback.print_exc()
    print(f"Error: {e}")
