# Inventarisasi Visualisasi — CELIOS Ketimpangan Ekonomi Indonesia 2026

**Sumber PDF:** `CELIOS_Ketimpangan Ekonomi Indonesia 2026 .pdf`  
**Total halaman:** 86  
**Total visualisasi ditemukan:** 52  
**Tanggal scan:** 29 April 2026  
**Metode:** `pdfplumber` text extraction + keyword matching

---

## Ringkasan

| Tipe | Jumlah | Keterangan |
|---|---|---|
| 📊 Chart Interaktif | 35 | Dapat direkonstruksi dengan Plotly |
| 🖼️ Infografik / Diagram | 10 | Kemungkinan perlu static image |
| 📋 Tabel | 9 | Dapat dijadikan tabel interaktif |
| **Total** | **52** | |

---

## 📊 Chart Interaktif (35 item)

> Dapat direkonstruksi ulang dengan Plotly Express / Plotly Graph Objects.  
> Status: ⏳ = belum diinput data | ✅ = selesai | 🔍 = perlu cek visual PDF

### Seksi A — Ketimpangan Kekayaan (Hal. 12–17)

| No | ID PDF | Judul | Tipe Chart | Hal. | Page File | Status |
|---|---|---|---|---|---|---|
| 1 | Gambar 3 | Total Kekayaan 50 Triliuner di Indonesia (2019–2025) | line / bar | 12 | `02_Kekayaan_Triliuner.py` | ⏳ |
| 2 | Gambar 2 | Proyeksi Median Kekayaan 50 Superkaya hingga 2050 | line | 16 | `02_Kekayaan_Triliuner.py` | ⏳ |
| 3 | Gambar 4 | Lini Bisnis Sumber Kekayaan 50 Superkaya | treemap / pie | 14–16 | `03_Sektor_Ekstraktif.py` | ⏳ |
| 4 | Gambar 5 | Ketimpangan Pendapatan dan Kekayaan, Indonesia 1965–2024 | line (area) | 16 | `04_Ketimpangan_Historis.py` | ⏳ |
| 5 | Gambar 6 | Superkaya Indonesia vs Triliuner Terkaya Berbagai Negara | bar horizontal | 17 | `05_Komparasi_Global.py` | ⏳ |

### Seksi B — Pejabat Publik & Oligarki Politik (Hal. 20–27)

| No | ID PDF | Judul | Tipe Chart | Hal. | Page File | Status |
|---|---|---|---|---|---|---|
| 6 | Gambar 7 | Total Harta Pejabat Publik Kabinet (2019–2025) | bar grouped | 20 | `06_Harta_Pejabat.py` | ⏳ |
| 7 | Gambar 8 | Klasemen Pejabat Terkaya Kabinet Merah Putih 2025 | bar horizontal | 21 | `06_Harta_Pejabat.py` | ⏳ |
| 8 | Gambar 9 | Peta Partai Politik: Jumlah Kursi vs Konsentrasi Kekayaan | scatter / bubble | 23 | `07_Oligarki_Parpol.py` | ⏳ |
| 9 | Gambar 10 | Perbandingan Rata-Rata Kekayaan Elite vs Masyarakat Umum | bar comparison | 25 | `07_Oligarki_Parpol.py` | ⏳ |
| 10 | Gambar X | Distribusi Kekayaan Seluruh Pejabat Publik per Dapil | choropleth / bar | 25 | `07_Oligarki_Parpol.py` | 🔍 |

### Seksi C — Ketimpangan Pendapatan & Perbankan (Hal. 28–31)

| No | ID PDF | Judul | Tipe Chart | Hal. | Page File | Status |
|---|---|---|---|---|---|---|
| 11 | Gambar 11 | Ketimpangan dan Kemiskinan Regional berdasarkan Pulau | map / bar | 27–28 | `08_Ketimpangan_Regional.py` | ⏳ |
| 12 | Gambar 12 | Distribusi Pendapatan dan Kekayaan di Indonesia | distribution / area | 28 | `08_Ketimpangan_Regional.py` | ⏳ |
| 13 | Gambar 13 | Peningkatan Rata-Rata Upah Buruh Nasional | line | 29 | `09_Upah_Tabungan.py` | ⏳ |
| 14 | Gambar 14 | Simpanan Bank Umum Berdasarkan Jumlah Nominal | bar / pie | 29 | `09_Upah_Tabungan.py` | ⏳ |
| 15 | Gambar 15 | Rata-rata Simpanan Bank Umum Berdasarkan Nominal Tabungan | bar | 30 | `09_Upah_Tabungan.py` | ⏳ |
| 16 | Gambar 16 | Proporsi Pendapatan 1% Teratas vs PPh Badan terhadap PDB | line dual-axis | 31 | `10_Pajak_Pendapatan.py` | ⏳ |

### Seksi D — Generasi Muda & Ketenagakerjaan (Hal. 36–43)

| No | ID PDF | Judul | Tipe Chart | Hal. | Page File | Status |
|---|---|---|---|---|---|---|
| 17 | Gambar 20 | Faktor Kesenjangan Upah antara Gen Z dan Non-Gen Z | bar | 36 | `11_GenZ_Ketenagakerjaan.py` | ⏳ |
| 18 | Gambar 21 | Perlindungan Pekerja di Indonesia | bar / radar | 37 | `11_GenZ_Ketenagakerjaan.py` | ⏳ |
| 19 | Gambar 22 | Cuti Tidak Berbayar Generasi Muda | bar | 38 | `11_GenZ_Ketenagakerjaan.py` | ⏳ |
| 20 | Gambar 24 | UMR yang Tidak Cukup untuk Menghidupi Keluarga | bar comparison | 43 | `12_UMR_Kebutuhan.py` | ⏳ |

### Seksi E — Gig Economy & Ojek Online (Hal. 46)

| No | ID PDF | Judul | Tipe Chart | Hal. | Page File | Status |
|---|---|---|---|---|---|---|
| 21 | Gambar 25 | Mekanisme Pembagian Komisi Platform vs Pengemudi | waterfall / bar | 46 | `13_Gig_Economy_Ojol.py` | ⏳ |

### Seksi F — Ketimpangan Gender (Hal. 52–55)

| No | ID PDF | Judul | Tipe Chart | Hal. | Page File | Status |
|---|---|---|---|---|---|---|
| 22 | Gambar 27 | Simulasi Beban Ganda Ibu Bekerja | bar comparison | 52 | `14_Ketimpangan_Gender.py` | ⏳ |
| 23 | Gambar 28 | Simulasi Nilai Ekonomi Kerja Ibu WFH | bar comparison | 52 | `14_Ketimpangan_Gender.py` | ⏳ |
| 24 | Gambar 30 | Lebih Banyak Perempuan Bekerja di Sektor Informal | bar / line | 54 | `14_Ketimpangan_Gender.py` | ⏳ |
| 25 | Gambar 31 | Kesenjangan Upah Berdasarkan Gender | line | 54 | `14_Ketimpangan_Gender.py` | ⏳ |
| 26 | Gambar 32 | Banyak Perempuan Putus Asa Mencari Kerja | bar | 55 | `14_Ketimpangan_Gender.py` | ⏳ |

### Seksi G — Militer & Kepolisian (Hal. 59)

| No | ID PDF | Judul | Tipe Chart | Hal. | Page File | Status |
|---|---|---|---|---|---|---|
| 27 | Gambar 33 | Ketimpangan Tunjangan Kinerja di Lingkungan TNI | bar | 59 | `15_TNI_Polri.py` | ⏳ |
| 28 | Gambar 34 | Ketimpangan Tunjangan Kinerja di Lingkungan Polri | bar | 59 | `15_TNI_Polri.py` | ⏳ |

### Seksi H — Reformasi Fiskal & Pajak Kekayaan (Hal. 64–79)

| No | ID PDF | Judul | Tipe Chart | Hal. | Page File | Status |
|---|---|---|---|---|---|---|
| 29 | Gambar 36 | Peta Parpol Dikuasai Oligarki Politik | bubble / bar | 64 | `16_Reformasi_Fiskal.py` | ⏳ |
| 30 | Gambar 39 | Dukungan Publik terhadap Penerapan Pajak Kekayaan | bar / pie | 70 | `17_Pajak_Kekayaan.py` | ⏳ |
| 31 | Gambar 40 | Persepsi Publik terhadap Dampak Pajak Kekayaan | bar / pie | 70 | `17_Pajak_Kekayaan.py` | ⏳ |
| 32 | Gambar 41 | Potensi Pajak Kekayaan 50 Triliuner (2019–2026) | bar / line | 71–72 | `17_Pajak_Kekayaan.py` | ⏳ |
| 33 | Gambar 42 | Pajak Kekayaan Pejabat Eksekutif dan Legislatif | bar | 72 | `17_Pajak_Kekayaan.py` | ⏳ |
| 34 | Gambar 51 | Persepsi Publik terhadap Dampak Pajak Kekayaan dalam Mengurangi (Ketimpangan) | bar / pie | 74 | `17_Pajak_Kekayaan.py` | 🔍 |
| 35 | Gambar 45 | Donasi Korporasi ke Partai Politik | bar / line | 78–79 | `18_Pembiayaan_Parpol.py` | ⏳ |

---

## 🖼️ Infografik / Diagram (10 item)

> Kemungkinan besar berbentuk gambar vektor atau desain custom di PDF.  
> **Strategi:** Tampilkan sebagai gambar PNG hasil render `pypdfium2` (crop area), atau rekonstruksi manual.

| No | ID PDF | Judul | Hal. | Strategi | Page File | Status |
|---|---|---|---|---|---|---|
| 1 | Gambar 1 | Framework Oligarki dan Ketimpangan Ekonomi di Indonesia | 9 | Static image (render PNG) | `01_Framework_Oligarki.py` | ⏳ |
| 2 | Gambar 17 | Generasi Muda yang Terhimpit Sistem Oligarki | 34 | Static image | `11_GenZ_Ketenagakerjaan.py` | ⏳ |
| 3 | Gambar 18 | Peluang Kerja Generasi Muda | 35 | Static image | `11_GenZ_Ketenagakerjaan.py` | ⏳ |
| 4 | Gambar 19 | Stabilitas Posisi Elite: Minimnya Mobilitas Sosial | 35 | Static image | `11_GenZ_Ketenagakerjaan.py` | ⏳ |
| 5 | Gambar 23 | Generasi Muda Menanggung Beban Ekonomi yang Timpang | 39 | Static image | `11_GenZ_Ketenagakerjaan.py` | ⏳ |
| 6 | Gambar 26 | Siklus Kehidupan Pengemudi Ojol | 47 | Static image | `13_Gig_Economy_Ojol.py` | ⏳ |
| 7 | Gambar 29 | Identifikasi Masalah yang Dihadapi Perempuan di Sistem Oligarki | 53 | Static image | `14_Ketimpangan_Gender.py` | ⏳ |
| 8 | Gambar 35 | Oligarki dalam Pakaian Demokrasi: Bagaimana Elite Mengakuisisi Partai | 62 | Static image | `16_Reformasi_Fiskal.py` | ⏳ |
| 9 | Gambar 37 | Rekomendasi: Mengurangi Ketimpangan dan Pengaruh Oligarki | 68 | Static image | `16_Reformasi_Fiskal.py` | ⏳ |
| 10 | Gambar 43 | Skema Tax Benefit untuk Mengurangi Ketimpangan Ekonomi | 75 | Static image | `17_Pajak_Kekayaan.py` | ⏳ |

> **Catatan untuk infografik:**  
> Jalankan `scripts/render_pages.py` → buka PNG di `ref/pages/` → crop manual area infografik → simpan ke `assets/infografik/gambarXX.png` → embed di page dengan `st.image()`.

---

## 📋 Tabel Interaktif (9 item)

> Dapat dijadikan tabel interaktif dengan `st.dataframe()` atau diplot sebagai grouped bar chart.

| No | ID PDF | Judul | Hal. | Baris (estimasi) | Page File | Status |
|---|---|---|---|---|---|---|
| 1 | Tabel 1 | Peningkatan Kekayaan Orang Superkaya di Indonesia | 13 | ~10 | `06_Harta_Pejabat.py` | ⏳ |
| 2 | Tabel 2 | Kekayaan Anggota DPR RI berdasarkan Fraksi Partai Politik | 24 | ~10 | `07_Oligarki_Parpol.py` | ⏳ |
| 3 | Tabel 3 | *(Judul belum teridentifikasi — cek hal. 24)* | 24 | — | `07_Oligarki_Parpol.py` | 🔍 |
| 4 | Tabel 4 | Dimensi Eksploitasi dan Mekanisme Kontrol Bisnis Ojek Online | 48 | ~8 | `13_Gig_Economy_Ojol.py` | ⏳ |
| 5 | Tabel 5a | Rata-rata Kekayaan Anggota DPR & DPD berdasarkan Dapil | 24 | ~30 | `07_Oligarki_Parpol.py` | ⏳ |
| 6 | Tabel 5b | Simulasi Pajak Kekayaan Berdasarkan Ambang Batas Kekayaan | 71 | ~8 | `17_Pajak_Kekayaan.py` | ⏳ |
| 7 | Tabel 7a | Kapan Anak Muda Bisa Memiliki Rumah? | 54 | ~5 | `14_Ketimpangan_Gender.py` | ⏳ |
| 8 | Tabel 7b | Penghapusan Pajak yang Membebani Kelas Menengah Bawah | 76 | ~6 | `17_Pajak_Kekayaan.py` | ⏳ |
| 9 | Tabel 13 | Ilustrasi Skema Insentif Berbasis Langganan | 55 | ~5 | `14_Ketimpangan_Gender.py` | ⏳ |

---

## 🔍 Item Perlu Verifikasi Visual (Cek PNG Render)

Beberapa item membutuhkan konfirmasi visual dari PDF sebelum bisa ditentukan tipe chartnya:

| No | ID PDF | Hal. | Pertanyaan |
|---|---|---|---|
| 1 | Gambar X | 25 | Apakah ini choropleth map atau bar chart per provinsi? |
| 2 | Gambar 11 | 27–28 | Ada dua referensi Gambar 11 di hal. berbeda — perlu konfirmasi nomor asli |
| 3 | Gambar 38 | 69 | Apakah ini flowchart / diagram atau ada data kuantitatif? |
| 4 | Gambar 44 | 78 | Apakah ini flow diagram atau ada komponen chart? |
| 5 | Tabel 3 | 24 | Judul tidak tertangkap teks — perlu buka PDF hal. 24 |
| 6 | Gambar 51 | 74 | Penomoran ganjil (51) — kemungkinan typo di PDF, perlu verifikasi |

---

## 📁 Struktur Folder Pages (18 files)

```
pages/
├── 01_Framework_Oligarki.py         ← Gambar 1
├── 02_Kekayaan_Triliuner.py         ← Gambar 2, 3
├── 03_Sektor_Ekstraktif.py          ← Gambar 4
├── 04_Ketimpangan_Historis.py       ← Gambar 5
├── 05_Komparasi_Global.py           ← Gambar 6
├── 06_Harta_Pejabat.py              ← Gambar 7, 8 + Tabel 1
├── 07_Oligarki_Parpol.py            ← Gambar 9, 10, X + Tabel 2, 3, 5a
├── 08_Ketimpangan_Regional.py       ← Gambar 11, 12
├── 09_Upah_Tabungan.py              ← Gambar 13, 14, 15
├── 10_Pajak_Pendapatan.py           ← Gambar 16
├── 11_GenZ_Ketenagakerjaan.py       ← Gambar 17, 18, 19, 20, 21, 22, 23
├── 12_UMR_Kebutuhan.py              ← Gambar 24
├── 13_Gig_Economy_Ojol.py           ← Gambar 25, 26 + Tabel 4
├── 14_Ketimpangan_Gender.py         ← Gambar 27-32 + Tabel 7a, 13
├── 15_TNI_Polri.py                  ← Gambar 33, 34
├── 16_Reformasi_Fiskal.py           ← Gambar 35, 36, 37, 38
├── 17_Pajak_Kekayaan.py             ← Gambar 39-43, 51 + Tabel 5b, 7b
└── 18_Pembiayaan_Parpol.py          ← Gambar 44, 45
```

---

## 🚀 Prioritas Pengerjaan yang Disarankan

Mulai dari chart yang datanya **bisa di-extract otomatis** dan **paling impactful** untuk embed WordPress:

| Prioritas | Page | Alasan |
|---|---|---|
| 🔴 1 | `02_Kekayaan_Triliuner.py` | Data time series sederhana, high impact |
| 🔴 2 | `06_Harta_Pejabat.py` | Data LHKPN publik, mudah dicari |
| 🔴 3 | `17_Pajak_Kekayaan.py` | Data survei, kemungkinan ada di CSV hasil extract |
| 🟡 4 | `07_Oligarki_Parpol.py` | Scatter/bubble chart menarik secara visual |
| 🟡 5 | `11_GenZ_Ketenagakerjaan.py` | Relevan, banyak chart per halaman |
| 🟢 6 | `14_Ketimpangan_Gender.py` | Kompleks, tapi konten penting |
| 🟢 7 | `01_Framework_Oligarki.py` | Infografik — render PNG dulu |

---

## � Urutan Lengkap per Halaman — Semua Gambar & Tabel

> Gabungan semua item (chart, infografik, tabel) **diurutkan berdasarkan halaman PDF**.  
> Tipe: 📊 chart interaktif · 🖼️ infografik · 📋 tabel  
> Status: ⏳ belum · ✅ selesai · 🔍 perlu verifikasi visual

| No | Hal. | ID | Judul | Tipe | Page File | Status |
|---|---|---|---|---|---|---|
| 1 | 9 | Gambar 1 | Framework Oligarki dan Ketimpangan Ekonomi di Indonesia | 🖼️ infografik | `01_Framework_Oligarki.py` | ⏳ |
| 2 | 12 | Gambar 3 | Total Kekayaan 50 Triliuner di Indonesia (2019–2025) | 📊 bar/line | `02_Kekayaan_Triliuner.py` | ✅ |
| 3 | 13 | Tabel 1 | Peningkatan Kekayaan Orang Superkaya di Indonesia | 📋 tabel | `06_Harta_Pejabat.py` | ⏳ |
| 4 | 14–16 | Gambar 4 | Lini Bisnis / Sektor Ekstraktif Sumber Kekayaan 50 Superkaya | 📊 treemap/pie | `03_Sektor_Ekstraktif.py` | ⏳ |
| 5 | 16 | Gambar 2 | Proyeksi Median Kekayaan 50 Superkaya hingga 2050 | 📊 line | `02_Kekayaan_Triliuner.py` | ⏳ |
| 6 | 16 | Gambar 5 | Ketimpangan Pendapatan dan Kekayaan, Indonesia 1965–2024 | 📊 line area | `04_Ketimpangan_Historis.py` | ⏳ |
| 7 | 17 | Gambar 6 | Superkaya Indonesia vs Triliuner Terkaya Berbagai Negara | 📊 bar horizontal | `05_Komparasi_Global.py` | ⏳ |
| 8 | 20 | Gambar 7 | Total Harta Pejabat Publik Kabinet (2019–2025) | 📊 bar grouped | `06_Harta_Pejabat.py` | ⏳ |
| 9 | 21 | Gambar 8 | Klasemen Pejabat Terkaya Kabinet Merah Putih 2025 | 📊 bar horizontal | `06_Harta_Pejabat.py` | ⏳ |
| 10 | 23 | Gambar 9 | Peta Partai Politik: Jumlah Kursi vs Konsentrasi Kekayaan | 📊 scatter/bubble | `07_Oligarki_Parpol.py` | ⏳ |
| 11 | 24 | Tabel 2 | Kekayaan Anggota DPR RI berdasarkan Fraksi Partai Politik | 📋 tabel | `07_Oligarki_Parpol.py` | ⏳ |
| 12 | 24 | Tabel 3 | *(Judul belum teridentifikasi — cek PDF hal. 24)* | 📋 tabel | `07_Oligarki_Parpol.py` | 🔍 |
| 13 | 24 | Tabel 5a | Rata-rata Kekayaan Anggota DPR RI & DPD RI per Dapil | 📋 tabel | `07_Oligarki_Parpol.py` | ⏳ |
| 14 | 25 | Gambar 10 | Perbandingan Rata-Rata Kekayaan Elite vs Masyarakat Umum | 📊 bar comparison | `07_Oligarki_Parpol.py` | ⏳ |
| 15 | 25 | Gambar X | Distribusi Kekayaan Seluruh Pejabat Publik per Dapil | 📊 choropleth/bar | `07_Oligarki_Parpol.py` | 🔍 |
| 16 | 27–28 | Gambar 11 | Ketimpangan dan Kemiskinan Regional berdasarkan Pulau | 📊 map/bar | `08_Ketimpangan_Regional.py` | ⏳ |
| 17 | 28 | Gambar 12 | Distribusi Pendapatan dan Kekayaan di Indonesia | 📊 distribution/area | `08_Ketimpangan_Regional.py` | ⏳ |
| 18 | 29 | Gambar 13 | Peningkatan Rata-Rata Upah Buruh Nasional | 📊 line | `09_Upah_Tabungan.py` | ⏳ |
| 19 | 29 | Gambar 14 | Simpanan Bank Umum Berdasarkan Jumlah Nominal | 📊 bar/pie | `09_Upah_Tabungan.py` | ⏳ |
| 20 | 30 | Gambar 15 | Rata-rata Simpanan Bank Umum Berdasarkan Nominal Tabungan | 📊 bar | `09_Upah_Tabungan.py` | ⏳ |
| 21 | 31 | Gambar 16 | Proporsi Pendapatan 1% Teratas vs PPh Badan terhadap PDB | 📊 line dual-axis | `10_Pajak_Pendapatan.py` | ⏳ |
| 22 | 34 | Gambar 17 | Generasi Muda yang Terhimpit Sistem Oligarki | 🖼️ infografik | `11_GenZ_Ketenagakerjaan.py` | ⏳ |
| 23 | 35 | Gambar 18 | Peluang Kerja Generasi Muda | 🖼️ infografik | `11_GenZ_Ketenagakerjaan.py` | 🔍 |
| 24 | 35 | Gambar 19 | Stabilitas Posisi Elite: Minimnya Mobilitas Sosial | �️ infografik | `11_GenZ_Ketenagakerjaan.py` | 🔍 |
| 25 | 36 | Gambar 20 | Faktor Kesenjangan Upah antara Gen Z dan Non-Gen Z | 📊 bar | `11_GenZ_Ketenagakerjaan.py` | ⏳ |
| 26 | 37 | Gambar 21 | Perlindungan Pekerja di Indonesia | 📊 bar/radar | `11_GenZ_Ketenagakerjaan.py` | ⏳ |
| 27 | 38 | Gambar 22 | Cuti Tidak Berbayar Generasi Muda | 📊 bar | `11_GenZ_Ketenagakerjaan.py` | ⏳ |
| 28 | 39 | Gambar 23 | Generasi Muda Menanggung Beban Ekonomi yang Timpang | 🖼️ infografik | `11_GenZ_Ketenagakerjaan.py` | ⏳ |
| 29 | 43 | Gambar 24 | UMR yang Tidak Cukup untuk Menghidupi Keluarga | 📊 bar comparison | `12_UMR_Kebutuhan.py` | ⏳ |
| 30 | 46 | Gambar 25 | Mekanisme Pembagian Komisi Platform vs Pengemudi | 📊 waterfall/bar | `13_Gig_Economy_Ojol.py` | ⏳ |
| 31 | 47 | Gambar 26 | Siklus Kehidupan Pengemudi Ojol | 🖼️ infografik | `13_Gig_Economy_Ojol.py` | ⏳ |
| 32 | 48 | Tabel 4 | Dimensi Eksploitasi dan Mekanisme Kontrol Bisnis Ojek Online | 📋 tabel | `13_Gig_Economy_Ojol.py` | ⏳ |
| 33 | 52 | Gambar 27 | Simulasi Beban Ganda Ibu Bekerja | 📊 bar comparison | `14_Ketimpangan_Gender.py` | ⏳ |
| 34 | 52 | Gambar 28 | Simulasi Nilai Ekonomi Kerja Ibu WFH | 📊 bar comparison | `14_Ketimpangan_Gender.py` | ⏳ |
| 35 | 53 | Gambar 29 | Identifikasi Masalah yang Dihadapi Perempuan di Sistem Oligarki | 🖼️ infografik | `14_Ketimpangan_Gender.py` | ⏳ |
| 36 | 54 | Gambar 30 | Lebih Banyak Perempuan Bekerja di Sektor Informal | 📊 bar/line | `14_Ketimpangan_Gender.py` | ⏳ |
| 37 | 54 | Gambar 31 | Kesenjangan Upah Berdasarkan Gender | 📊 line | `14_Ketimpangan_Gender.py` | ⏳ |
| 38 | 54 | Tabel 7a | Kapan Anak Muda Bisa Memiliki Rumah? | 📋 tabel | `14_Ketimpangan_Gender.py` | ⏳ |
| 39 | 54 | Tabel 8 | Kapan Anak DPRD (Studi Kasus 1.1) Bisa Membeli Rumah? | 📋 tabel | `14_Ketimpangan_Gender.py` | ⏳ |
| 40 | 55 | Gambar 32 | Banyak Perempuan Putus Asa Mencari Kerja | 📊 bar | `14_Ketimpangan_Gender.py` | ⏳ |
| 41 | 55 | Tabel 13a | Ilustrasi Skema Insentif Berbasis Langganan | 📋 tabel | `14_Ketimpangan_Gender.py` | ⏳ |
| 42 | 59 | Gambar 33 | Ketimpangan Tunjangan Kinerja di Lingkungan TNI | 📊 bar | `15_TNI_Polri.py` | ⏳ |
| 43 | 59 | Gambar 34 | Ketimpangan Tunjangan Kinerja di Lingkungan Polri | 📊 bar | `15_TNI_Polri.py` | ⏳ |
| 44 | 62 | Gambar 35 | Oligarki dalam Pakaian Demokrasi: Bagaimana Elite Mengakuisisi Partai | 🖼️ infografik | `16_Reformasi_Fiskal.py` | ⏳ |
| 45 | 64 | Gambar 36 | Peta Parpol Dikuasai Oligarki Politik | 📊 bubble/bar | `16_Reformasi_Fiskal.py` | ⏳ |
| 46 | 65 | Tabel 13b | Identifikasi Masalah Perempuan *(nomor duplikat — cek PDF)* | 📋 tabel | `16_Reformasi_Fiskal.py` | 🔍 |
| 47 | 68 | Gambar 37 | Rekomendasi: Mengurangi Ketimpangan dan Pengaruh Oligarki | 🖼️ infografik | `16_Reformasi_Fiskal.py` | ⏳ |
| 48 | 69 | Gambar 38 | Reformasi Fiskal melalui Tata Kelola Pajak yang Akuntabel | 🖼️ infografik | `16_Reformasi_Fiskal.py` | 🔍 |
| 49 | 70 | Gambar 39 | Dukungan Publik terhadap Penerapan Pajak Kekayaan | 📊 bar/pie | `17_Pajak_Kekayaan.py` | ⏳ |
| 50 | 70 | Gambar 40 | Persepsi Publik terhadap Dampak Pajak Kekayaan | 📊 bar/pie | `17_Pajak_Kekayaan.py` | ⏳ |
| 51 | 71 | Tabel 5b | Simulasi Pajak Kekayaan Berdasarkan Ambang Batas *(nomor duplikat dgn hal.24)* | 📋 tabel | `17_Pajak_Kekayaan.py` | ⏳ |
| 52 | 71–72 | Gambar 41 | Potensi Pajak Kekayaan 50 Triliuner (2019–2026) | 📊 bar/line | `17_Pajak_Kekayaan.py` | ⏳ |
| 53 | 72 | Gambar 42 | Pajak Kekayaan Pejabat Eksekutif dan Legislatif | 📊 bar | `17_Pajak_Kekayaan.py` | ⏳ |
| 54 | 72 | Tabel 6 | *(Judul belum teridentifikasi — cek PDF hal. 72)* | 📋 tabel | `17_Pajak_Kekayaan.py` | 🔍 |
| 55 | 72 | Tabel 9 | *(Kemungkinan duplikat Tabel 5 — perlu verifikasi)* | 📋 tabel | `17_Pajak_Kekayaan.py` | 🔍 |
| 56 | 74 | Gambar 51 | Persepsi Publik Dampak Pajak *(penomoran ganjil, kemungkinan typo)* | 📊 bar/pie | `17_Pajak_Kekayaan.py` | 🔍 |
| 57 | 75 | Gambar 43 | Skema Tax Benefit untuk Mengurangi Ketimpangan Ekonomi | 🖼️ infografik | `17_Pajak_Kekayaan.py` | ⏳ |
| 58 | 76 | Tabel 7b | Penghapusan Pajak yang Membebani Kelas Menengah Bawah *(nomor duplikat dgn hal.54)* | 📋 tabel | `17_Pajak_Kekayaan.py` | ⏳ |
| 59 | 78 | Gambar 44 | Alur Pengesahan Aturan Pembiayaan Publik Partai Politik | 🖼️ infografik | `18_Pembiayaan_Parpol.py` | 🔍 |
| 60 | 78–79 | Gambar 45 | Donasi Korporasi ke Partai Politik | � bar/line | `18_Pembiayaan_Parpol.py` | ⏳ |

> ⚠️ **Catatan penomoran PDF:** Beberapa nomor tabel duplikat (Tabel 5, 7, 13 muncul 2× di halaman berbeda). Perlu verifikasi langsung dari PDF.  
> 🔍 = perlu konfirmasi visual dari PNG render PDF
