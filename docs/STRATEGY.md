# Strategi Reverse Engineer Visualisasi Data → WordPress Embed
**Project:** CELIOS — Ketimpangan Ekonomi Indonesia 2026  
**Tanggal:** 29 April 2026  
**Status:** Planning

---

## 1. Gambaran Umum

Tujuan utama project ini adalah:
1. **Reverse engineer** semua visualisasi data dari PDF laporan CELIOS
2. **Recreate** sebagai chart interaktif berbasis web
3. **Embed** ke website WordPress CELIOS — baik sebagai dashboard terpadu maupun chart individual per halaman

---

## 2. Arsitektur Sistem

### Pilihan yang Dipilih: Static Build + iframe Embed

```
PDF Laporan
    │
    ▼
[ Ekstraksi Data ] ──→ JSON per chart
    │
    ▼
[ React + Vite + ECharts ]
    │
    ├──→ /dashboard         ← semua chart (1 halaman penuh)
    └──→ /embed/chart-XX    ← tiap chart standalone (untuk iframe)
    │
    ▼
[ Deploy ke Netlify ]
    │
    ├──→ Dashboard URL  : https://celios-charts.netlify.app/
    └──→ Embed URL      : https://celios-charts.netlify.app/embed/chart-01
    │
    ▼
[ WordPress ]
    ├──→ Halaman Dashboard  → embed dashboard URL
    └──→ Halaman/Post lain  → embed chart URL individual via <iframe>
```

### Kenapa Opsi ini?

| Kriteria | Static Build + iframe | Inline Script di WP |
|---|---|---|
| Conflict dengan WP theme/plugin | ✅ Tidak ada | ❌ Sangat rawan |
| Update chart tanpa sentuh WP | ✅ Ya | ❌ Tidak |
| Performance WP | ✅ Tidak terbebani | ❌ JS berat di WP |
| Bisa share URL chart secara independen | ✅ Ya | ❌ Tidak |
| Butuh hosting tambahan | ⚠️ Ya (Netlify free) | ✅ Tidak |

---

## 3. Tech Stack

| Layer | Teknologi | Alasan |
|---|---|---|
| Framework | **React 18 + Vite** | Build cepat, multi-entry support, ekosistem luas |
| Chart Library | **Apache ECharts** (`echarts-for-react`) | Terlengkap untuk laporan ekonomi: bar, line, map, scatter, treemap |
| Styling | **Tailwind CSS** | Utility-first, mudah responsive |
| Data Format | **JSON** per chart | Mudah di-update, bisa di-fetch atau di-import langsung |
| Routing | **React Router v6** | Untuk routing `/dashboard` dan `/embed/:chartId` |
| Build Config | **Vite multi-entry** | Generate HTML terpisah per chart untuk iframe |
| Hosting | **Netlify** (free tier) | Auto-deploy dari Git, HTTPS gratis, CDN global |

---

## 4. Struktur Project

```
celios-charts/
│
├── data/                          ← DATA (hasil ekstraksi dari PDF)
│   ├── chart-01-gini-ratio.json
│   ├── chart-02-pendapatan-desil.json
│   ├── chart-03-...json
│   └── index.json                 ← registry semua chart (id, title, type)
│
├── src/
│   ├── components/
│   │   ├── charts/                ← Reusable chart components
│   │   │   ├── BarChart.jsx
│   │   │   ├── LineChart.jsx
│   │   │   ├── PieChart.jsx
│   │   │   ├── MapChart.jsx
│   │   │   ├── ScatterChart.jsx
│   │   │   └── index.js
│   │   └── ui/
│   │       ├── ChartCard.jsx      ← Wrapper card dengan judul & sumber data
│   │       ├── Legend.jsx
│   │       └── Tooltip.jsx
│   │
│   ├── pages/
│   │   ├── Dashboard.jsx          ← Halaman dashboard (semua chart)
│   │   └── EmbedChart.jsx         ← Halaman embed per chart (minimal UI)
│   │
│   ├── hooks/
│   │   └── useChartData.js        ← Hook untuk load JSON data
│   │
│   ├── utils/
│   │   └── chartConfig.js         ← Helper untuk ECharts option builder
│   │
│   ├── App.jsx                    ← Router setup
│   └── main.jsx
│
├── public/
│   └── favicon.ico
│
├── index.html
├── vite.config.js
├── tailwind.config.js
├── package.json
└── .env                           ← VITE_BASE_URL, dll
```

---

## 5. Alur Kerja (Workflow)

### Phase 1 — Inventarisasi & Ekstraksi Data

- [ ] Buka PDF `CELIOS_Ketimpangan Ekonomi Indonesia 2026.pdf`
- [ ] Catat semua visualisasi: **nomor, judul, tipe chart, sumber data**
- [ ] Ekstraksi data dari tiap chart ke format JSON
- [ ] Tools yang bisa digunakan:
  - **Manual:** Baca angka dari chart, input ke JSON
  - **Tabula** (untuk tabel di PDF)
  - **pdfplumber** (Python, untuk tabel & text)
  - **AI-assisted:** Screenshot chart → extract angka via LLM

**Format JSON standar per chart:**
```json
{
  "id": "chart-01",
  "title": "Gini Ratio Indonesia 2015–2025",
  "type": "line",
  "source": "BPS, diolah CELIOS",
  "unit": "Indeks",
  "xAxis": ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"],
  "series": [
    {
      "name": "Gini Ratio",
      "data": [0.402, 0.397, 0.391, 0.389, 0.380, 0.385, 0.381, 0.375, 0.388, 0.379, 0.372]
    }
  ]
}
```

---

### Phase 2 — Setup Project

```bash
# 1. Buat project
npm create vite@latest celios-charts -- --template react

# 2. Install dependencies
cd celios-charts
npm install echarts echarts-for-react react-router-dom

# 3. Install Tailwind
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p

# 4. Jalankan dev server
npm run dev
```

---

### Phase 3 — Development

**Urutan pengerjaan:**
1. Setup routing (`Dashboard` + `EmbedChart`)
2. Buat komponen `ChartCard` (wrapper universal)
3. Buat komponen chart per tipe (Bar, Line, Pie, dst.)
4. Buat hook `useChartData` untuk load JSON
5. Populate `Dashboard.jsx` dengan semua chart
6. Test tiap embed URL: `/embed/chart-01`, `/embed/chart-02`, dst.

---

### Phase 4 — Deploy ke Netlify

```bash
# Build
npm run build

# Deploy via Netlify CLI
netlify deploy --prod --dir=dist
```

Atau connect repo GitHub ke Netlify untuk **auto-deploy** setiap push.

**Konfigurasi Netlify (`netlify.toml`):**
```toml
[build]
  command = "npm run build"
  publish = "dist"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

---

### Phase 5 — Embed di WordPress

**Per chart individual (di post/halaman WP):**
```html
<!-- Tambahkan di WordPress via Custom HTML block -->
<div style="position:relative; width:100%; padding-bottom:56.25%; overflow:hidden;">
  <iframe 
    src="https://celios-charts.netlify.app/embed/chart-01"
    style="position:absolute; top:0; left:0; width:100%; height:100%; border:none;"
    allowfullscreen
    loading="lazy">
  </iframe>
</div>
```

**Dashboard penuh (di halaman khusus WP):**
```html
<div style="position:relative; width:100%; height:90vh; overflow:hidden;">
  <iframe 
    src="https://celios-charts.netlify.app/"
    style="width:100%; height:100%; border:none;"
    allowfullscreen>
  </iframe>
</div>
```

**Tips WordPress:**
- Gunakan plugin **"Advanced Custom Fields"** atau **"Shortcoder"** untuk buat shortcode embed yang reusable
- Contoh shortcode: `[celios_chart id="chart-01" height="500"]`

---

## 6. Standar Desain Chart

Semua chart harus konsisten mengikuti panduan berikut:

| Elemen | Spesifikasi |
|---|---|
| Font | Inter / system-ui |
| Warna primer | `#1A3A5C` (navy CELIOS) |
| Warna aksen | `#E85D04`, `#2EC4B6`, `#FFBF00` |
| Background embed | `#FFFFFF` atau `#F8F9FA` |
| Breakpoint responsive | Mobile: 375px, Tablet: 768px, Desktop: 1200px |
| Sumber data | Selalu tampilkan di bawah chart (font 11px, warna abu) |
| Logo | Tampilkan logo CELIOS kecil di pojok kanan bawah |

---

## 7. Registry Chart (Diisi saat inventarisasi PDF)

| No | ID | Judul | Tipe | Status |
|---|---|---|---|---|
| 1 | chart-01 | *(isi setelah scan PDF)* | - | ⏳ Pending |
| 2 | chart-02 | *(isi setelah scan PDF)* | - | ⏳ Pending |
| ... | ... | ... | ... | ... |

---

## 8. Checklist Keseluruhan

### Phase 1 — Inventarisasi
- [ ] Scan seluruh PDF dan list semua chart
- [ ] Tentukan tipe tiap chart
- [ ] Ekstrak semua data ke JSON

### Phase 2 — Setup
- [ ] Init project React + Vite
- [ ] Install semua dependencies
- [ ] Setup Tailwind
- [ ] Setup React Router

### Phase 3 — Development
- [ ] Buat komponen `ChartCard`
- [ ] Buat `BarChart.jsx`
- [ ] Buat `LineChart.jsx`
- [ ] Buat `PieChart.jsx`
- [ ] Buat `MapChart.jsx` (jika ada peta)
- [ ] Buat `Dashboard.jsx`
- [ ] Buat `EmbedChart.jsx`
- [ ] Test semua embed URL

### Phase 4 — Deploy
- [ ] Setup `netlify.toml`
- [ ] Deploy ke Netlify
- [ ] Verifikasi semua URL aktif

### Phase 5 — WordPress
- [ ] Embed dashboard di halaman utama WP
- [ ] Embed chart individual di halaman/post terkait
- [ ] Test di mobile & desktop
- [ ] Cek tidak ada conflict dengan WP theme

---

## 9. Referensi

- [Apache ECharts Docs](https://echarts.apache.org/en/index.html)
- [echarts-for-react](https://github.com/hustcc/echarts-for-react)
- [Vite Multi-Entry Build](https://vitejs.dev/guide/build.html#multi-page-app)
- [Netlify Docs](https://docs.netlify.com/)
- [Tabula (PDF table extractor)](https://tabula.technology/)
