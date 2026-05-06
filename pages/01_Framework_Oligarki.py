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

with st.expander("🔗 Kode Embed WordPress"):
    st.code("""<!-- Gambar 1: Framework Oligarki dan Ketimpangan Ekonomi -->
<div style="position:relative; width:100%; padding-top:75%; overflow:hidden; border-radius:8px; box-shadow:0 2px 8px rgba(0,0,0,0.1);">
  <iframe
    src="https://[YOUR-APP].streamlit.app/Framework_Oligarki?embed=true"
    style="position:absolute; top:0; left:0; width:100%; height:100%; border:none;"
    allowfullscreen
    loading="lazy">
  </iframe>
</div>""", language="html")
