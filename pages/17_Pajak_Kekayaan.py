import streamlit as st
from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

st.set_page_config(page_title="Pajak Kekayaan", layout="wide", page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png")
apply_embed_mode()
render_sidebar()

chart_header("Dukungan Publik terhadap Penerapan Pajak Kekayaan", "Gambar 39 — Hal. 70")
st.info("⏳ Data belum diinput. Lihat PDF hal. 70.")

chart_header("Persepsi Publik terhadap Dampak Pajak Kekayaan", "Gambar 40 — Hal. 70")
st.info("⏳ Data belum diinput. Lihat PDF hal. 70.")

chart_header("Potensi Pajak Kekayaan 50 Triliuner (2019–2026)", "Gambar 41 — Hal. 71/72")
st.info("⏳ Data belum diinput. Lihat PDF hal. 71–72.")

chart_header("Pajak Kekayaan Pejabat Eksekutif dan Legislatif", "Gambar 42 — Hal. 72")
st.info("⏳ Data belum diinput. Lihat PDF hal. 72.")

chart_header("Simulasi Pajak Kekayaan Berdasarkan Ambang Batas", "Tabel 5 — Hal. 71")
st.info("⏳ Data belum diinput. Lihat PDF hal. 71.")

chart_header("Penghapusan Pajak yang Membebani Kelas Menengah", "Tabel 7 — Hal. 76")
st.info("⏳ Data belum diinput. Lihat PDF hal. 76.")
chart_footer("Simulasi CELIOS, Forbes, diolah CELIOS (2026)")
