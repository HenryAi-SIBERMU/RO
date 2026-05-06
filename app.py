import streamlit as st

from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar

st.set_page_config(
    page_title="CELIOS — Ketimpangan Ekonomi Indonesia 2026",
    page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Ketimpangan Ekonomi Indonesia 2026")
st.caption("Center of Economic and Law Studies (CELIOS)")
st.info("Pilih visualisasi dari menu di sebelah kiri.")

apply_embed_mode()
render_sidebar()
