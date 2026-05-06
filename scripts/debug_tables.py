import pdfplumber
from pathlib import Path

PDF_PATH = Path(__file__).resolve().parent.parent.parent / "ref" / "CELIOS_Ketimpangan Ekonomi Indonesia 2026 .pdf"
OUTPUT_DIR = Path(__file__).resolve().parent.parent.parent / "ref" / "debug"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

with pdfplumber.open(str(PDF_PATH)) as pdf:
    print(f"Total halaman: {len(pdf.pages)}\n")
    for i, page in enumerate(pdf.pages):
        tables = page.extract_tables()
        status = f"{len(tables)} tabel ditemukan" if tables else "tidak ada tabel"
        print(f"  Halaman {i+1:3d}: {status}")

        im = page.to_image(resolution=120)
        im.debug_tablefinder()
        im.save(OUTPUT_DIR / f"debug_page_{i+1:03d}.png")

print(f"\nDebug selesai. Cek folder: {OUTPUT_DIR}")
