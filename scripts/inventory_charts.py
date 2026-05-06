"""
Skrip inventarisasi chart dari PDF.
Mencari kata kunci: Grafik, Gambar, Figure, Chart, Diagram, Tabel di tiap halaman.
Output: inventory.txt dengan daftar halaman dan konteks teks sekitarnya.
"""
import pdfplumber
from pathlib import Path

PDF_PATH = Path(__file__).resolve().parent.parent.parent / "ref" / "CELIOS_Ketimpangan Ekonomi Indonesia 2026 .pdf"
OUTPUT_FILE = Path(__file__).resolve().parent.parent / "data" / "inventory.txt"

KEYWORDS = ["grafik", "gambar", "figure", "chart", "diagram", "tabel", "infografis"]

results = []

with pdfplumber.open(str(PDF_PATH)) as pdf:
    print(f"Total halaman: {len(pdf.pages)}\n")
    for i, page in enumerate(pdf.pages):
        text = page.extract_text() or ""
        text_lower = text.lower()

        hits = [kw for kw in KEYWORDS if kw in text_lower]
        if hits:
            lines = text.split("\n")
            relevant = [l.strip() for l in lines if any(kw in l.lower() for kw in KEYWORDS)]
            entry = (
                f"=== Halaman {i+1} | Keywords: {', '.join(hits)} ===\n"
                + "\n".join(f"  {l}" for l in relevant[:10])
                + "\n"
            )
            results.append(entry)
            print(f"  Halaman {i+1}: {hits}")

OUTPUT_FILE.parent.mkdir(exist_ok=True)
OUTPUT_FILE.write_text("\n".join(results), encoding="utf-8")
print(f"\n✓ Inventory disimpan ke: {OUTPUT_FILE}")
print(f"  Total halaman dengan chart/tabel: {len(results)}")
