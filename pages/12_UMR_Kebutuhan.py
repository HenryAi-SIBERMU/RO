import streamlit as st
from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

st.set_page_config(page_title="UMR vs Kebutuhan Hidup", layout="wide", page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png")
apply_embed_mode()
render_sidebar()

chart_header("UMR yang Tidak Cukup untuk Menghidupi Keluarga", "Gambar 24 — Hal. 43")
st.info("⏳ Data belum diinput. Lihat PDF hal. 43.")
chart_footer("Kemnaker, BPS, diolah CELIOS (2026)")
