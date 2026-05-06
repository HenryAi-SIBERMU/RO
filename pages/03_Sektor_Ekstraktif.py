import streamlit as st
from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

st.set_page_config(page_title="Sektor Ekstraktif", layout="wide", page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png")
apply_embed_mode()
render_sidebar()

chart_header("Lini Bisnis Sumber Kekayaan 50 Superkaya di Indonesia", "Gambar 4 — Hal. 14/16")
st.info("⏳ Data belum diinput. Lihat PDF hal. 14 & 16.")
chart_footer("Forbes, diolah CELIOS (2026)")
