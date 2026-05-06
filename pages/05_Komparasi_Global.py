import streamlit as st
from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

st.set_page_config(page_title="Komparasi Global", layout="wide", page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png")
apply_embed_mode()
render_sidebar()

chart_header("Superkaya Indonesia vs Triliuner Terkaya Berbagai Negara", "Gambar 6 — Hal. 17")
st.info("⏳ Data belum diinput. Lihat PDF hal. 17.")
chart_footer("Forbes, diolah CELIOS (2026)")
