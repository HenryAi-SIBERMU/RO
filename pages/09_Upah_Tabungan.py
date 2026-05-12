import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

BASE_DIR = Path(__file__).resolve().parent.parent
_G13_chartjs = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar13_chartjs.html"
_G13_plotly  = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar13_plotly.html"
_G14_chartjs = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar14_chartjs.html"
_G14_plotly  = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar14_plotly.html"
_G15_chartjs = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar15_chartjs.html"
_G15_plotly  = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar15_plotly.html"

st.set_page_config(page_title="Upah & Tabungan", layout="wide", page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png")
apply_embed_mode()
render_sidebar()

chart_header("Peningkatan Rata-Rata Upah Buruh Nasional", "Gambar 13 — Hal. 29")
tab_g13_chartjs, tab_g13_plotly = st.tabs(["Versi Chart.js", "Versi Plotly"])
with tab_g13_chartjs:
    components.html(_G13_chartjs.read_text(encoding="utf-8"), height=740, scrolling=True)
with tab_g13_plotly:
    components.html(_G13_plotly.read_text(encoding="utf-8"), height=740, scrolling=True)
chart_footer("Sakernas (Agustus 2024 & 2025), diolah CELIOS")
with st.expander("🔗 Kode Embed WordPress — Gambar 13 (Chart.js)"):
    st.code("""<iframe src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar13_chartjs.html"
  width="100%" height="740" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;" loading="lazy"></iframe>""", language="html")
with st.expander("🔗 Kode Embed WordPress — Gambar 13 (Plotly)"):
    st.code("""<iframe src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar13_plotly.html"
  width="100%" height="740" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;" loading="lazy"></iframe>""", language="html")

chart_header("Simpanan Bank Umum Berdasarkan Jumlah Nominal", "Gambar 14 — Hal. 29")
tab_g14_chartjs, tab_g14_plotly = st.tabs(["Versi Chart.js", "Versi Plotly"])
with tab_g14_chartjs:
    components.html(_G14_chartjs.read_text(encoding="utf-8"), height=760, scrolling=True)
with tab_g14_plotly:
    components.html(_G14_plotly.read_text(encoding="utf-8"), height=760, scrolling=True)
chart_footer("Data Distribusi Simpanan Bank Umum 2014-2025, estimasi dummy oleh CELIOS")
with st.expander("🔗 Kode Embed WordPress — Gambar 14 (Chart.js)"):
    st.code("""<iframe src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar14_chartjs.html"
  width="100%" height="760" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;" loading="lazy"></iframe>""", language="html")
with st.expander("🔗 Kode Embed WordPress — Gambar 14 (Plotly)"):
    st.code("""<iframe src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar14_plotly.html"
  width="100%" height="760" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;" loading="lazy"></iframe>""", language="html")

chart_header("Rata-rata Simpanan Bank Umum Berdasarkan Nominal Tabungan", "Gambar 15 — Hal. 30")
tab_g15_chartjs, tab_g15_plotly = st.tabs(["Versi Chart.js", "Versi Plotly"])
with tab_g15_chartjs:
    components.html(_G15_chartjs.read_text(encoding="utf-8"), height=720, scrolling=True)
with tab_g15_plotly:
    components.html(_G15_plotly.read_text(encoding="utf-8"), height=720, scrolling=True)
chart_footer("Data Distribusi Simpanan Bank Umum 2014-2025, estimasi dummy oleh CELIOS")
with st.expander("🔗 Kode Embed WordPress — Gambar 15 (Chart.js)"):
    st.code("""<iframe src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar15_chartjs.html"
  width="100%" height="720" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;" loading="lazy"></iframe>""", language="html")
with st.expander("🔗 Kode Embed WordPress — Gambar 15 (Plotly)"):
    st.code("""<iframe src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar15_plotly.html"
  width="100%" height="720" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;" loading="lazy"></iframe>""", language="html")
