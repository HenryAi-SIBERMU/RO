import streamlit as st
import os

def render_sidebar():
    if st.query_params.get("embed") == "true":
        return
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    logo_path = os.path.join(base_dir, "assets", "logo_celios.png")
    
    st.markdown("""
    <style>
    .sidebar-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #66BB6A;
        text-align: center;
        padding-bottom: 20px;
        margin-bottom: 0px;
        border-bottom: 1px solid #ffffff11;
    }
    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        if os.path.exists(logo_path):
            st.image(logo_path, use_column_width=True)
            
        st.markdown('<div class="sidebar-title">Celios - Ketimpangan Ekonomi</div>', unsafe_allow_html=True)
        st.markdown("---")
        
        st.page_link("app.py", label="Dashboard Utama", icon="📊")
        
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
