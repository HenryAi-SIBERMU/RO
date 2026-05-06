import pdfplumber
import pandas as pd
from pathlib import Path

PDF_PATH = Path(__file__).resolve().parent.parent.parent / "ref" / "CELIOS_Ketimpangan Ekonomi Indonesia 2026 .pdf"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "data"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

table_count = 0

with pdfplumber.open(str(PDF_PATH)) as pdf:
    print(f"Total halaman: {len(pdf.pages)}\n")
    for i, page in enumerate(pdf.pages):
        tables = page.extract_tables()
        if not tables:
            continue

        for j, table in enumerate(tables):
            if not table or len(table) < 2:
                continue
            try:
                headers = table[0]
                rows = table[1:]
                df = pd.DataFrame(rows, columns=headers)
                df = df.dropna(how="all")

                filename = OUTPUT_DIR / f"page{i+1:03d}_table{j+1}.csv"
                df.to_csv(filename, index=False, encoding="utf-8")
                table_count += 1
                print(f"  ✓ Halaman {i+1}, Tabel {j+1} → {filename.name} ({len(df)} baris)")
            except Exception as e:
                print(f"  ✗ Halaman {i+1}, Tabel {j+1}: {e}")

print(f"\nTotal {table_count} tabel berhasil diekstrak ke: {OUTPUT_DIR}")
