import streamlit as st
from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

st.set_page_config(page_title="Ketimpangan Regional", layout="wide", page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png")
apply_embed_mode()
render_sidebar()

chart_header("Ketimpangan dan Kemiskinan Regional berdasarkan Pulau", "Gambar 11 — Hal. 27/28")
st.info("⏳ Data belum diinput. Lihat PDF hal. 27–28.")

chart_header("Distribusi Pendapatan dan Kekayaan di Indonesia", "Gambar 12 — Hal. 28")
st.info("⏳ Data belum diinput. Lihat PDF hal. 28.")
chart_footer("BPS, World Inequality Database, diolah CELIOS (2026)")
