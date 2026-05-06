import streamlit as st
from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

st.set_page_config(page_title="Harta Pejabat Publik", layout="wide", page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png")
apply_embed_mode()
render_sidebar()

chart_header("Total Harta Pejabat Publik Kabinet (2019–2025)", "Gambar 7 — Hal. 20")
st.info("⏳ Data belum diinput. Lihat PDF hal. 20.")

st.divider()
chart_header("Klasemen Pejabat Terkaya Kabinet Merah Putih 2025", "Gambar 8 — Hal. 21")
st.info("⏳ Data belum diinput. Lihat PDF hal. 21.")
chart_footer("LHKPN KPK, diolah CELIOS (2026)")
