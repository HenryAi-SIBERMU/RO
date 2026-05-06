import streamlit as st
from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

st.set_page_config(page_title="Gen Z & Ketenagakerjaan", layout="wide", page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png")
apply_embed_mode()
render_sidebar()

chart_header("Faktor Kesenjangan Upah antara Gen Z dan Non-Gen Z", "Gambar 20 — Hal. 36")
st.info("⏳ Data belum diinput. Lihat PDF hal. 36.")

chart_header("Perlindungan Pekerja di Indonesia", "Gambar 21 — Hal. 37")
st.info("⏳ Data belum diinput. Lihat PDF hal. 37.")

chart_header("Cuti Tidak Berbayar Generasi Muda", "Gambar 22 — Hal. 38")
st.info("⏳ Data belum diinput. Lihat PDF hal. 38.")
chart_footer("Survei CELIOS (2026)")
