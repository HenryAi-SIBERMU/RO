import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

BASE_DIR = Path(__file__).resolve().parent.parent
_G44 = BASE_DIR / "embed" / "16_Reformasi_Fiskal_gambar44.html"
_G45 = BASE_DIR / "embed" / "16_Reformasi_Fiskal_gambar45_plotly.html"

st.set_page_config(page_title="Pembiayaan Parpol", layout="wide", page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png")
apply_embed_mode()
render_sidebar()

chart_header("Alur Pengesahan Aturan Pembiayaan Publik Partai Politik", "Gambar 44 — Hal. 78")
components.html(_G44.read_text(encoding="utf-8"), height=1050, scrolling=False)
chart_footer("Diolah oleh peneliti")
with st.expander("🔗 Kode Embed WordPress — Gambar 44"):
    st.code("""<!-- Gambar 44: Alur Pengesahan Aturan Pembiayaan Publik Partai Politik -->
<iframe src="https://henryai-sibermu.github.io/RO/embed/16_Reformasi_Fiskal_gambar44.html"
  width="100%" height="1050" frameborder="0"
  style="border-radius:32px; background:#f7f4ff;" loading="lazy"></iframe>""", language="html")

chart_header("Donasi Korporasi ke Partai Politik", "Gambar 45 — Hal. 78/79")
components.html(_G45.read_text(encoding="utf-8"), height=760, scrolling=False)
chart_footer("KPU, PPATK, diolah CELIOS (2026)")
with st.expander("🔗 Kode Embed WordPress — Gambar 45"):
    st.code("""<!-- Gambar 45: Donasi Korporasi ke Partai Politik (World Map) -->
<iframe src="https://henryai-sibermu.github.io/RO/embed/16_Reformasi_Fiskal_gambar45_plotly.html"
  width="100%" height="760" frameborder="0"
  style="border-radius:32px; background:#f7f4ff;" loading="lazy"></iframe>""", language="html")
