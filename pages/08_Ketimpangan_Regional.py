import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

BASE_DIR = Path(__file__).resolve().parent.parent
_G11_profile = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar11.html"
_G11_chartjs = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar11_chartjs.html"
_G11_plotly = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar11_plotly.html"

st.set_page_config(
    page_title="Ketimpangan Regional",
    layout="wide",
    page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png",
)
apply_embed_mode()
render_sidebar()

chart_header(
    "Profil Elite Bisnis: Basis, Lokasi Operasi, dan Sektor",
    "Gambar 11a — Hal. 27",
)
components.html(_G11_profile.read_text(encoding="utf-8"), height=1580, scrolling=True)
chart_footer("Laporan Ketimpangan Ekonomi Indonesia 2026, diolah CELIOS")
with st.expander("🔗 Kode Embed WordPress — Gambar 11a (Profil Elite)"):
    st.code(
        """<!-- Gambar 11a: Profil Elite Bisnis -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar11.html"
  width="100%" height="1580" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;"
  loading="lazy">
</iframe>""",
        language="html",
    )

chart_header(
    "Ketimpangan dan Kemiskinan Regional di Indonesia berdasarkan Pulau",
    "Gambar 11b — Hal. 27",
)
tab_chartjs, tab_plotly = st.tabs(["Versi Chart.js", "Versi Plotly"])
with tab_chartjs:
    components.html(_G11_chartjs.read_text(encoding="utf-8"), height=720, scrolling=True)
with tab_plotly:
    components.html(_G11_plotly.read_text(encoding="utf-8"), height=720, scrolling=True)
chart_footer("Laporan Harta Kekayaan Pejabat Negara 2025, diolah CELIOS")
with st.expander("🔗 Kode Embed WordPress — Gambar 11b (Chart.js)"):
    st.code(
        """<!-- Gambar 11b: Ketimpangan & Kemiskinan Regional — Chart.js -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar11_chartjs.html"
  width="100%" height="720" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;"
  loading="lazy">
</iframe>""",
        language="html",
    )
with st.expander("🔗 Kode Embed WordPress — Gambar 11b (Plotly)"):
    st.code(
        """<!-- Gambar 11b: Ketimpangan & Kemiskinan Regional — Plotly -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar11_plotly.html"
  width="100%" height="720" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;"
  loading="lazy">
</iframe>""",
        language="html",
    )

chart_header("Distribusi Pendapatan dan Kekayaan di Indonesia", "Gambar 12 — Hal. 28")
st.info("⏳ Data belum diinput. Lihat PDF hal. 28.")
chart_footer("BPS, World Inequality Database, diolah CELIOS (2026)")
