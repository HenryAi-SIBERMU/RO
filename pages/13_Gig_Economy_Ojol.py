import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

BASE_DIR = Path(__file__).resolve().parent.parent
_G25_plotly = BASE_DIR / "embed" / "13_Gig_Economy_Ojol_gambar25_plotly.html"
_G26        = BASE_DIR / "embed" / "13_Gig_Economy_Ojol_gambar26.html"

st.set_page_config(page_title="Gig Economy & Ojol", layout="wide", page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png")
apply_embed_mode()
render_sidebar()

chart_header("Mekanisme Pembagian Komisi antara Platform dan Pengemudi Ojek Online", "Gambar 25 — Hal. 46")
components.html(_G25_plotly.read_text(encoding="utf-8"), height=660, scrolling=True)
chart_footer("Wawancara kualitatif dengan Pengemudi Ojek Online, 2026")
with st.expander("🔗 Kode Embed WordPress — Gambar 25 (Plotly)"):
    st.code("""<!-- Gambar 25: Mekanisme Pembagian Komisi Ojek Online — Plotly -->
<iframe src="https://henryai-sibermu.github.io/RO/embed/13_Gig_Economy_Ojol_gambar25_plotly.html"
  width="100%" height="660" frameborder="0"
  style="border-radius:32px; background:#0f0520;" loading="lazy"></iframe>""", language="html")

chart_header("Siklus Kehidupan Pengemudi Ojol", "Gambar 26 — Hal. 47")
components.html(_G26.read_text(encoding="utf-8"), height=620, scrolling=True)
chart_footer("Ilustrasi CELIOS berdasarkan temuan lapangan, 2026")
with st.expander("🔗 Kode Embed WordPress — Gambar 26"):
    st.code("""<!-- Gambar 26: Siklus Kehidupan Pengemudi Ojol -->
<iframe src="https://henryai-sibermu.github.io/RO/embed/13_Gig_Economy_Ojol_gambar26.html"
  width="100%" height="620" frameborder="0"
  style="border-radius:32px; background:#0f0520;" loading="lazy"></iframe>""", language="html")

chart_header("Dimensi Eksploitasi dan Mekanisme Kontrol Bisnis Ojol", "Tabel 4 — Hal. 48")
st.info("⏳ Data belum diinput. Lihat PDF hal. 48.")
chart_footer("Wawancara kualitatif dengan Pengemudi Ojek Online, 2026")
