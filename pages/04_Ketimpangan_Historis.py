import streamlit as st
from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

st.set_page_config(page_title="Ketimpangan Historis", layout="wide", page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png")
apply_embed_mode()
render_sidebar()

chart_header("Ketimpangan Pendapatan dan Kekayaan, Indonesia 1965–2024", "Gambar 5 — Hal. 16")
st.info("⏳ Data belum diinput. Lihat PDF hal. 16.")
chart_footer("World Inequality Database, diolah CELIOS (2026)")
