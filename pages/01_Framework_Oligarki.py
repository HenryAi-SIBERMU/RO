import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_footer

st.set_page_config(page_title="Framework Oligarki", layout="wide", page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png")
apply_embed_mode()
render_sidebar()

HTML_PATH = Path(__file__).resolve().parent.parent / "assets" / "gambar01_framework_v2.html"
with open(HTML_PATH, "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=1100, scrolling=True)

chart_footer("Dielaborasi oleh peneliti berdasarkan Wright Mills et al., dalam Bugiaccini dkk (2024)")

with st.expander("🔗 Kode Embed WordPress — Gambar 1"):
    st.code("""<!-- Gambar 1: Framework Oligarki dan Ketimpangan Ekonomi -->
<iframe
  src="https://ro-dvwjkrbnwirub7872387.streamlit.app/Framework_Oligarki?embed=true"
  width="100%" height="1200" frameborder="0"
  style="border-radius:8px; box-shadow:0 2px 8px rgba(0,0,0,0.1);"
  allowfullscreen loading="lazy">
</iframe>""", language="html")
