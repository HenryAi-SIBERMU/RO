import streamlit as st
from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

st.set_page_config(page_title="Pembiayaan Parpol", layout="wide", page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png")
apply_embed_mode()
render_sidebar()

chart_header("Alur Pengesahan Aturan Pembiayaan Publik Partai Politik", "Gambar 44 — Hal. 78")
st.info("⏳ Data belum diinput. Lihat PDF hal. 78.")

chart_header("Donasi Korporasi ke Partai Politik", "Gambar 45 — Hal. 78/79")
st.info("⏳ Data belum diinput. Lihat PDF hal. 78–79.")
chart_footer("KPU, PPATK, diolah CELIOS (2026)")
