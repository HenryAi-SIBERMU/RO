import pypdfium2 as pdfium
from pathlib import Path

PDF_PATH = Path(__file__).resolve().parent.parent.parent / "ref" / "CELIOS_Ketimpangan Ekonomi Indonesia 2026 .pdf"
OUTPUT_DIR = Path(__file__).resolve().parent.parent.parent / "ref" / "pages"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

pdf = pdfium.PdfDocument(str(PDF_PATH))
print(f"Total halaman: {len(pdf)}")

for i, page in enumerate(pdf):
    bitmap = page.render(scale=2.5)
    img = bitmap.to_pil()
    output_path = OUTPUT_DIR / f"page_{i+1:03d}.png"
    img.save(output_path, "PNG")
    print(f"  ✓ Halaman {i+1} → {output_path.name}")

print(f"\nSelesai. Cek folder: {OUTPUT_DIR}")
