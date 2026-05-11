import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

BASE_DIR = Path(__file__).resolve().parent.parent
_G11_embed = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar11.html"

st.set_page_config(
    page_title="Ketimpangan Regional",
    layout="wide",
    page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png",
)
apply_embed_mode()
render_sidebar()

chart_header(
    "Profil Elite Bisnis: Basis, Lokasi Operasi, dan Sektor",
    "Gambar 11 — Hal. 27",
)
components.html(_G11_embed.read_text(encoding="utf-8"), height=1580, scrolling=True)
chart_footer("Laporan Ketimpangan Ekonomi Indonesia 2026, diolah CELIOS")
with st.expander("🔗 Kode Embed WordPress — Gambar 11"):
    st.code(
        """<!-- Gambar 11: Profil Elite Bisnis -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar11.html"
  width="100%" height="1580" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;"
  loading="lazy">
</iframe>""",
        language="html",
    )

chart_header("Ketimpangan dan Kemiskinan Regional berdasarkan Pulau", "Gambar 11 (versi map) — Hal. 27/28")
st.info("⏳ Data belum diinput. Lihat PDF hal. 27–28.")

chart_header("Distribusi Pendapatan dan Kekayaan di Indonesia", "Gambar 12 — Hal. 28")
st.info("⏳ Data belum diinput. Lihat PDF hal. 28.")
chart_footer("BPS, World Inequality Database, diolah CELIOS (2026)")
