import os

ROOT = r"C:\Users\ADIB\OneDrive\Desktop\datacomm"
SKIP_DIRS = {".git", "__pycache__", "node_modules", ".venv", "venv"}

for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
    rel = os.path.relpath(dirpath, ROOT)
    depth = 0 if rel == "." else rel.count(os.sep) + 1
    print("  " * depth + "[" + (rel if rel != "." else ".") + "]")
    for f in sorted(filenames):
        p = os.path.join(dirpath, f)
        try:
            size = os.path.getsize(p)
        except OSError:
            size = -1
        print("  " * (depth + 1) + f"{f}  ({size} bytes)")
