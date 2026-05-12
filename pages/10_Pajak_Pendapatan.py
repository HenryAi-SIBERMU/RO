import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

BASE_DIR = Path(__file__).resolve().parent.parent
_G16_chartjs = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar16_chartjs.html"
_G16_plotly  = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar16_plotly.html"

st.set_page_config(page_title="Pajak & Pendapatan", layout="wide", page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png")
apply_embed_mode()
render_sidebar()

chart_header("Proporsi Pendapatan 1% Teratas vs PPh Badan terhadap PDB", "Gambar 16 — Hal. 30")
tab_g16_chartjs, tab_g16_plotly = st.tabs(["Versi Chart.js", "Versi Plotly"])
with tab_g16_chartjs:
    components.html(_G16_chartjs.read_text(encoding="utf-8"), height=680, scrolling=True)
with tab_g16_plotly:
    components.html(_G16_plotly.read_text(encoding="utf-8"), height=680, scrolling=True)
chart_footer("WID.world (2025); Kemenkeu (2025); BPS (2025); Trading Economics (2025), diolah CELIOS")
with st.expander("🔗 Kode Embed WordPress — Gambar 16 (Chart.js)"):
    st.code("""<iframe src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar16_chartjs.html"
  width="100%" height="680" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;" loading="lazy"></iframe>""", language="html")
with st.expander("🔗 Kode Embed WordPress — Gambar 16 (Plotly)"):
    st.code("""<iframe src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar16_plotly.html"
  width="100%" height="680" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;" loading="lazy"></iframe>""", language="html")
