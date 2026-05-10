import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

st.set_page_config(page_title="Sektor Ekstraktif", layout="wide")
apply_embed_mode()
render_sidebar()

chart_header("Sektor Ekstraktif sebagai Sumber Kekayaan Elite", "Gambar 4 — Hal. 14–16")

_HTML = Path(__file__).resolve().parent.parent / "embed" / "03_Sektor_Ekstraktif.html"
components.html(_HTML.read_text(encoding="utf-8"), height=520, scrolling=True)

chart_footer("Forbes, diolah CELIOS (2026)")

with st.expander("🔗 Kode Embed WordPress — Gambar 4"):
    st.code("""<!-- Gambar 4: Sektor Ekstraktif sebagai Sumber Kekayaan Elite -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/03_Sektor_Ekstraktif.html"
  width="100%" height="480" frameborder="0"
  style="border-radius:8px; box-shadow:0 2px 8px rgba(0,0,0,0.1);"
  loading="lazy">
</iframe>""", language="html")
