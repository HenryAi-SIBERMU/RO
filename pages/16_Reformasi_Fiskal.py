import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

BASE_DIR = Path(__file__).resolve().parent.parent
_G35 = BASE_DIR / "embed" / "16_Reformasi_Fiskal_gambar35.html"

st.set_page_config(page_title="Reformasi Fiskal", layout="wide", page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png")
apply_embed_mode()
render_sidebar()

chart_header("Oligarki dalam Pakaian Demokrasi: Bagaimana Elite Mengakuisisi Partai", "Gambar 35 — Hal. 61")
components.html(_G35.read_text(encoding="utf-8"), height=660, scrolling=True)
chart_footer("Analisis Peneliti")
with st.expander("🔗 Kode Embed WordPress — Gambar 35"):
    st.code("""<!-- Gambar 35: Oligarki dalam Pakaian Demokrasi -->
<iframe src="https://henryai-sibermu.github.io/RO/embed/16_Reformasi_Fiskal_gambar35.html"
  width="100%" height="660" frameborder="0"
  style="border-radius:32px; background:#f7f4ff;" loading="lazy"></iframe>""", language="html")

chart_header("Peta Parpol Dikuasai Oligarki Politik", "Gambar 36 — Hal. 64")
st.info("⏳ Data belum diinput. Lihat PDF hal. 64.")

chart_header("Rekomendasi: Mengurangi Ketimpangan & Pengaruh Oligarki", "Gambar 37 — Hal. 68")
st.info("⏳ Data belum diinput. Lihat PDF hal. 68.")

chart_header("Reformasi Fiskal melalui Tata Kelola Pajak", "Gambar 38 — Hal. 69")
st.info("⏳ Data belum diinput. Lihat PDF hal. 69.")
chart_footer("CELIOS (2026)")
