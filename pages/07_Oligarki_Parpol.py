import streamlit as st
from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

st.set_page_config(page_title="Oligarki & Parpol", layout="wide", page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png")
apply_embed_mode()
render_sidebar()

chart_header("Peta Partai Politik: Jumlah Kursi vs Konsentrasi Kekayaan", "Gambar 9 — Hal. 23")
st.info("⏳ Data belum diinput. Lihat PDF hal. 23.")

chart_header("Perbandingan Rata-Rata Kekayaan Elite vs Masyarakat Umum", "Gambar 10 — Hal. 25")
st.info("⏳ Data belum diinput. Lihat PDF hal. 25.")

chart_header("Distribusi Kekayaan Seluruh Pejabat Publik per Dapil", "Gambar X — Hal. 25")
st.info("⏳ Data belum diinput. Lihat PDF hal. 25.")

chart_header("Kekayaan Anggota DPR RI berdasarkan Fraksi Partai", "Tabel 2 — Hal. 24")
st.info("⏳ Data belum diinput. Lihat PDF hal. 24.")
chart_footer("LHKPN KPK, diolah CELIOS (2026)")
