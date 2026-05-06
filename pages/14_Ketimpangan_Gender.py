import streamlit as st
from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

st.set_page_config(page_title="Ketimpangan Gender", layout="wide", page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png")
apply_embed_mode()
render_sidebar()

chart_header("Simulasi Beban Ganda Ibu Bekerja", "Gambar 27 — Hal. 52")
st.info("⏳ Data belum diinput. Lihat PDF hal. 52.")

chart_header("Simulasi Nilai Ekonomi Kerja Ibu WFH", "Gambar 28 — Hal. 52")
st.info("⏳ Data belum diinput. Lihat PDF hal. 52.")

chart_header("Lebih Banyak Perempuan Bekerja di Sektor Informal", "Gambar 30 — Hal. 54")
st.info("⏳ Data belum diinput. Lihat PDF hal. 54.")

chart_header("Kesenjangan Upah Berdasarkan Gender", "Gambar 31 — Hal. 54")
st.info("⏳ Data belum diinput. Lihat PDF hal. 54.")

chart_header("Banyak Perempuan Putus Asa Mencari Kerja", "Gambar 32 — Hal. 55")
st.info("⏳ Data belum diinput. Lihat PDF hal. 55.")
chart_footer("BPS, Survei CELIOS (2026)")
