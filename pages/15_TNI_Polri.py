import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

BASE_DIR = Path(__file__).resolve().parent.parent
_G33 = BASE_DIR / "embed" / "15_TNI_Polri_gambar33_plotly.html"
_G34 = BASE_DIR / "embed" / "15_TNI_Polri_gambar34_plotly.html"

st.set_page_config(page_title="TNI & Polri", layout="wide", page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png")
apply_embed_mode()
render_sidebar()

chart_header("Ketimpangan Tunjangan Kinerja di Lingkungan TNI", "Gambar 33 — Hal. 59")
components.html(_G33.read_text(encoding="utf-8"), height=520, scrolling=True)
chart_footer("Peraturan Presiden Nomor 102 Tahun 2018")
with st.expander("🔗 Kode Embed WordPress — Gambar 33"):
    st.code("""<!-- Gambar 33: Ketimpangan Tunjangan Kinerja TNI -->
<iframe src="https://henryai-sibermu.github.io/RO/embed/15_TNI_Polri_gambar33_plotly.html"
  width="100%" height="520" frameborder="0"
  style="border-radius:32px; background:#f7f4ff;" loading="lazy"></iframe>""", language="html")

chart_header("Ketimpangan Tunjangan Kinerja di Lingkungan Polri", "Gambar 34 — Hal. 59")
components.html(_G34.read_text(encoding="utf-8"), height=520, scrolling=True)
chart_footer("Peraturan Presiden Nomor 103 Tahun 2018")
with st.expander("🔗 Kode Embed WordPress — Gambar 34"):
    st.code("""<!-- Gambar 34: Ketimpangan Tunjangan Kinerja Polri -->
<iframe src=\"https://henryai-sibermu.github.io/RO/embed/15_TNI_Polri_gambar34_plotly.html\"
  width=\"100%\" height=\"520\" frameborder=\"0\"
  style=\"border-radius:32px; background:#f7f4ff;\" loading=\"lazy\"></iframe>""", language="html")
