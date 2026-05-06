import streamlit as st
from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

st.set_page_config(page_title="Gig Economy & Ojol", layout="wide", page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png")
apply_embed_mode()
render_sidebar()

chart_header("Mekanisme Pembagian Komisi Platform vs Pengemudi", "Gambar 25 — Hal. 46")
st.info("⏳ Data belum diinput. Lihat PDF hal. 46.")

chart_header("Dimensi Eksploitasi dan Mekanisme Kontrol Bisnis Ojol", "Tabel 4 — Hal. 48")
st.info("⏳ Data belum diinput. Lihat PDF hal. 48.")
chart_footer("Survei CELIOS (2026)")
