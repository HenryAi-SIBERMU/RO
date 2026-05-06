import streamlit as st
from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

st.set_page_config(page_title="Upah & Tabungan", layout="wide", page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png")
apply_embed_mode()
render_sidebar()

chart_header("Peningkatan Rata-Rata Upah Buruh Nasional", "Gambar 13 — Hal. 29")
st.info("⏳ Data belum diinput. Lihat PDF hal. 29.")

chart_header("Simpanan Bank Umum Berdasarkan Jumlah Nominal", "Gambar 14 — Hal. 29")
st.info("⏳ Data belum diinput. Lihat PDF hal. 29.")

chart_header("Rata-rata Simpanan Bank Umum Berdasarkan Nominal Tabungan", "Gambar 15 — Hal. 30")
st.info("⏳ Data belum diinput. Lihat PDF hal. 30.")
chart_footer("Kemnaker, OJK, diolah CELIOS (2026)")
