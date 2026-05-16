import streamlit as st
from pathlib import Path

# Lookup: keyword (lowercase) → (label, page_file, keterangan)
_CHART_INDEX = {
    "gambar 1":  ("Framework Oligarki",      "pages/01_Framework_Oligarki.py",     "Hal. 9"),
    "gambar 2":  ("Kekayaan Triliuner",       "pages/02_Kekayaan_Triliuner.py",     "Hal. 16"),
    "gambar 3":  ("Kekayaan Triliuner",       "pages/02_Kekayaan_Triliuner.py",     "Hal. 12"),
    "gambar 4":  ("Sektor Ekstraktif",        "pages/03_Sektor_Ekstraktif.py",      "Hal. 14–16"),
    "gambar 5":  ("Ketimpangan Historis",     "pages/04_Ketimpangan_Historis.py",   "Hal. 16"),
    "gambar 6":  ("Komparasi Global",         "pages/05_Komparasi_Global.py",       "Hal. 17"),
    "gambar 7":  ("Harta Pejabat",            "pages/06_Harta_Pejabat.py",          "Hal. 20"),
    "gambar 8":  ("Harta Pejabat",            "pages/06_Harta_Pejabat.py",          "Hal. 21"),
    "gambar 9":  ("Oligarki Parpol",          "pages/07_Oligarki_Parpol.py",        "Hal. 23"),
    "gambar 10": ("Oligarki Parpol",          "pages/07_Oligarki_Parpol.py",        "Hal. 25"),
    "gambar 11": ("Ketimpangan Regional",     "pages/08_Ketimpangan_Regional.py",   "Hal. 27–28"),
    "gambar 12": ("Ketimpangan Regional",     "pages/08_Ketimpangan_Regional.py",   "Hal. 28"),
    "gambar 13": ("Upah & Tabungan",          "pages/09_Upah_Tabungan.py",          "Hal. 29"),
    "gambar 14": ("Upah & Tabungan",          "pages/09_Upah_Tabungan.py",          "Hal. 29"),
    "gambar 15": ("Upah & Tabungan",          "pages/09_Upah_Tabungan.py",          "Hal. 30"),
    "gambar 16": ("Pajak Pendapatan",         "pages/10_Pajak_Pendapatan.py",       "Hal. 31"),
    "gambar 17": ("Gen Z & Pekerjaan",        "pages/11_GenZ_Ketenagakerjaan.py",   "Hal. 34"),
    "gambar 18": ("Gen Z & Pekerjaan",        "pages/11_GenZ_Ketenagakerjaan.py",   "Hal. 35"),
    "gambar 19": ("Gen Z & Pekerjaan",        "pages/11_GenZ_Ketenagakerjaan.py",   "Hal. 35"),
    "gambar 20": ("Gen Z & Pekerjaan",        "pages/11_GenZ_Ketenagakerjaan.py",   "Hal. 36"),
    "gambar 21": ("Gen Z & Pekerjaan",        "pages/11_GenZ_Ketenagakerjaan.py",   "Hal. 37"),
    "gambar 22": ("Gen Z & Pekerjaan",        "pages/11_GenZ_Ketenagakerjaan.py",   "Hal. 38"),
    "gambar 23": ("Gen Z & Pekerjaan",        "pages/11_GenZ_Ketenagakerjaan.py",   "Hal. 39"),
    "gambar 24": ("UMR & Kebutuhan",          "pages/12_UMR_Kebutuhan.py",          "Hal. 43"),
    "gambar 25": ("Gig Economy",              "pages/13_Gig_Economy_Ojol.py",       "Hal. 46"),
    "gambar 26": ("Gig Economy",              "pages/13_Gig_Economy_Ojol.py",       "Hal. 47"),
    "gambar 27": ("Ketimpangan Gender",       "pages/14_Ketimpangan_Gender.py",     "Hal. 52"),
    "gambar 28": ("Ketimpangan Gender",       "pages/14_Ketimpangan_Gender.py",     "Hal. 52"),
    "gambar 29": ("Ketimpangan Gender",       "pages/14_Ketimpangan_Gender.py",     "Hal. 53"),
    "gambar 30": ("Ketimpangan Gender",       "pages/14_Ketimpangan_Gender.py",     "Hal. 54"),
    "gambar 31": ("Ketimpangan Gender",       "pages/14_Ketimpangan_Gender.py",     "Hal. 54"),
    "gambar 32": ("Ketimpangan Gender",       "pages/14_Ketimpangan_Gender.py",     "Hal. 55"),
    "gambar 33": ("TNI & Polri",              "pages/15_TNI_Polri.py",              "Hal. 59"),
    "gambar 34": ("TNI & Polri",              "pages/15_TNI_Polri.py",              "Hal. 59"),
    "gambar 35": ("Reformasi Fiskal",         "pages/16_Reformasi_Fiskal.py",       "Hal. 62"),
    "gambar 36": ("Reformasi Fiskal",         "pages/16_Reformasi_Fiskal.py",       "Hal. 64"),
    "gambar 37": ("Reformasi Fiskal",         "pages/16_Reformasi_Fiskal.py",       "Hal. 68"),
    "gambar 38": ("Reformasi Fiskal",         "pages/16_Reformasi_Fiskal.py",       "Hal. 69"),
    "gambar 39": ("Pajak Kekayaan",           "pages/17_Pajak_Kekayaan.py",         "Hal. 70"),
    "gambar 40": ("Pajak Kekayaan",           "pages/17_Pajak_Kekayaan.py",         "Hal. 70"),
    "gambar 41": ("Pajak Kekayaan",           "pages/17_Pajak_Kekayaan.py",         "Hal. 71–72"),
    "gambar 42": ("Pajak Kekayaan",           "pages/17_Pajak_Kekayaan.py",         "Hal. 72"),
    "gambar 43": ("Pajak Kekayaan",           "pages/17_Pajak_Kekayaan.py",         "Hal. 75"),
    "gambar 44": ("Pembiayaan Parpol",        "pages/18_Pembiayaan_Parpol.py",      "Hal. 78"),
    "gambar 45": ("Pembiayaan Parpol",        "pages/18_Pembiayaan_Parpol.py",      "Hal. 78–79"),
    "tabel 1":   ("Harta Pejabat",            "pages/06_Harta_Pejabat.py",          "Hal. 13"),
    "tabel 2":   ("Oligarki Parpol",          "pages/07_Oligarki_Parpol.py",        "Hal. 24"),
    "tabel 3":   ("Oligarki Parpol",          "pages/07_Oligarki_Parpol.py",        "Hal. 24"),
    "tabel 4":   ("Gig Economy",              "pages/13_Gig_Economy_Ojol.py",       "Hal. 48"),
    "tabel 5":   ("Pajak Kekayaan",           "pages/17_Pajak_Kekayaan.py",         "Hal. 71"),
    "tabel 6":   ("Pajak Kekayaan",           "pages/17_Pajak_Kekayaan.py",         "Hal. 72"),
    "tabel 7":   ("Pajak Kekayaan",           "pages/17_Pajak_Kekayaan.py",         "Hal. 76"),
}

def render_sidebar():
    if st.query_params.get("embed") == "true":
        return
    base_dir = Path(__file__).resolve().parent.parent
    logo_path = base_dir / "assets" / "logo_celios.png"

    with st.sidebar:
        if logo_path.exists():
            st.image(str(logo_path), use_column_width=True)

        st.markdown("**Celios — Ketimpangan Ekonomi**")
        st.markdown("---")

        # ── Search box ──────────────────────────────────────────────
        query = st.text_input(
            "🔍 Cari Gambar / Tabel",
            placeholder="cth: gambar 39, tabel 5",
            label_visibility="collapsed",
        )
        if query:
            q = query.strip().lower()
            results = [
                (k, v) for k, v in _CHART_INDEX.items()
                if q in k or q.replace(" ", "") in k.replace(" ", "")
            ]
            if results:
                for key, (label, page, hal) in results:
                    st.page_link(page, label=f"📌 {key.title()} → {label} ({hal})")
            else:
                st.caption("Tidak ditemukan.")
            st.markdown("---")
        # ─────────────────────────────────────────────────────────────

        st.page_link("app.py", label="Dashboard Utama")

        st.markdown("### Seksi A — Kekayaan")
        st.page_link("pages/01_Framework_Oligarki.py", label="Framework Oligarki")
        st.page_link("pages/02_Kekayaan_Triliuner.py", label="Kekayaan Triliuner")
        st.page_link("pages/03_Sektor_Ekstraktif.py", label="Sektor Ekstraktif")
        st.page_link("pages/04_Ketimpangan_Historis.py", label="Ketimpangan Historis")
        st.page_link("pages/05_Komparasi_Global.py", label="Komparasi Global")

        st.markdown("### Seksi B — Pejabat Publik")
        st.page_link("pages/06_Harta_Pejabat.py", label="Harta Pejabat")
        st.page_link("pages/07_Oligarki_Parpol.py", label="Oligarki Parpol")

        st.markdown("### Seksi C — Pendapatan")
        st.page_link("pages/08_Ketimpangan_Regional.py", label="Ketimpangan Regional")
        st.page_link("pages/09_Upah_Tabungan.py", label="Upah & Tabungan")
        st.page_link("pages/10_Pajak_Pendapatan.py", label="Pajak Pendapatan")

        st.markdown("### Seksi D-F — Ketenagakerjaan")
        st.page_link("pages/11_GenZ_Ketenagakerjaan.py", label="Gen Z & Pekerjaan")
        st.page_link("pages/12_UMR_Kebutuhan.py", label="UMR & Kebutuhan")
        st.page_link("pages/13_Gig_Economy_Ojol.py", label="Gig Economy")
        st.page_link("pages/14_Ketimpangan_Gender.py", label="Ketimpangan Gender")

        st.markdown("### Seksi G-H — Kebijakan")
        st.page_link("pages/15_TNI_Polri.py", label="TNI & Polri")
        st.page_link("pages/16_Reformasi_Fiskal.py", label="Reformasi Fiskal")
        st.page_link("pages/17_Pajak_Kekayaan.py", label="Pajak Kekayaan")
        st.page_link("pages/18_Pembiayaan_Parpol.py", label="Pembiayaan Parpol")

        st.markdown("---")

        st.markdown("### Dokumentasi")
        st.page_link("pages/21_Chart_Inventory.py", label="Chart Inventory")

        st.markdown("### Dataset")
        st.page_link("pages/20_Dataset.py", label="Data Files (CSV)")
