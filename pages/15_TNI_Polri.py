import streamlit as st
from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

st.set_page_config(page_title="TNI & Polri", layout="wide", page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png")
apply_embed_mode()
render_sidebar()

chart_header("Ketimpangan Tunjangan Kinerja di Lingkungan TNI", "Gambar 33 — Hal. 59")
st.info("⏳ Data belum diinput. Lihat PDF hal. 59.")

chart_header("Ketimpangan Tunjangan Kinerja di Lingkungan Polri", "Gambar 34 — Hal. 59")
st.info("⏳ Data belum diinput. Lihat PDF hal. 59.")
chart_footer("Perpres/Peraturan Internal, diolah CELIOS (2026)")
