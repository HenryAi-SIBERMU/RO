import streamlit as st
from pathlib import Path

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
