import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

BASE_DIR = Path(__file__).resolve().parent.parent
_G24_plotly = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar24_plotly.html"

st.set_page_config(page_title="UMR vs Kebutuhan Hidup", layout="wide", page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png")
apply_embed_mode()
render_sidebar()

chart_header("UMR yang Tidak Cukup untuk Menghidupi Keluarga", "Gambar 24 — Hal. 43")
components.html(_G24_plotly.read_text(encoding="utf-8"), height=1000, scrolling=True)
chart_footer("Kemenaker 2025; diolah peneliti")
with st.expander("🔗 Kode Embed WordPress — Gambar 24 (Plotly)"):
    st.code("""<!-- Gambar 24: UMR yang Tidak Cukup untuk Menghidupi Keluarga — Plotly -->
<iframe src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar24_plotly.html"
  width="100%" height="1000" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;" loading="lazy"></iframe>""", language="html")
