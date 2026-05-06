import streamlit as st
from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

st.set_page_config(page_title="Reformasi Fiskal", layout="wide", page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png")
apply_embed_mode()
render_sidebar()

chart_header("Peta Parpol Dikuasai Oligarki Politik", "Gambar 36 — Hal. 64")
st.info("⏳ Data belum diinput. Lihat PDF hal. 64.")

chart_header("Rekomendasi: Mengurangi Ketimpangan & Pengaruh Oligarki", "Gambar 37 — Hal. 68")
st.info("⏳ Data belum diinput. Lihat PDF hal. 68.")

chart_header("Reformasi Fiskal melalui Tata Kelola Pajak", "Gambar 38 — Hal. 69")
st.info("⏳ Data belum diinput. Lihat PDF hal. 69.")
chart_footer("CELIOS (2026)")
