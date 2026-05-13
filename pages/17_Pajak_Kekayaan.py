import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

BASE_DIR = Path(__file__).resolve().parent.parent
_G39 = BASE_DIR / "embed" / "16_Reformasi_Fiskal_gambar39_plotly.html"
_G40 = BASE_DIR / "embed" / "16_Reformasi_Fiskal_gambar40_plotly.html"
_G41 = BASE_DIR / "embed" / "16_Reformasi_Fiskal_gambar41_plotly.html"
_G42 = BASE_DIR / "embed" / "16_Reformasi_Fiskal_gambar42.html"
_T5  = BASE_DIR / "embed" / "16_Reformasi_Fiskal_tabel5.html"
_G43 = BASE_DIR / "embed" / "16_Reformasi_Fiskal_gambar43.html"

st.set_page_config(page_title="Pajak Kekayaan", layout="wide", page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png")
apply_embed_mode()
render_sidebar()

chart_header("Dukungan Publik terhadap Penerapan Pajak Kekayaan di Indonesia", "Gambar 39 — Hal. 70")
components.html(_G39.read_text(encoding="utf-8"), height=660, scrolling=True)
chart_footer("Survei Pajak Kekayaan CELIOS, 2025")
with st.expander("🔗 Kode Embed WordPress — Gambar 39"):
    st.code("""<!-- Gambar 39: Dukungan Publik terhadap Penerapan Pajak Kekayaan -->
<iframe src="https://henryai-sibermu.github.io/RO/embed/16_Reformasi_Fiskal_gambar39_plotly.html"
  width="100%" height="660" frameborder="0"
  style="border-radius:32px; background:#f7f4ff;" loading="lazy"></iframe>""", language="html")

chart_header("Persepsi Publik terhadap Dampak Pajak Kekayaan dalam Mengurangi Ketimpangan Ekonomi", "Gambar 40 — Hal. 70")
components.html(_G40.read_text(encoding="utf-8"), height=640, scrolling=True)
chart_footer("Survei Pajak Kekayaan CELIOS, 2025")
with st.expander("🔗 Kode Embed WordPress — Gambar 40"):
    st.code("""<!-- Gambar 40: Persepsi Publik Dampak Pajak Kekayaan -->
<iframe src="https://henryai-sibermu.github.io/RO/embed/16_Reformasi_Fiskal_gambar40_plotly.html"
  width="100%" height="640" frameborder="0"
  style="border-radius:32px; background:#f7f4ff;" loading="lazy"></iframe>""", language="html")

chart_header("Potensi Pajak Kekayaan 50 Triliuner (2019–2026)", "Gambar 41 — Hal. 71/72")
components.html(_G41.read_text(encoding="utf-8"), height=660, scrolling=True)
chart_footer("Data Forbes 50 orang terkaya 2026, diolah oleh peneliti")
with st.expander("🔗 Kode Embed WordPress — Gambar 41"):
    st.code("""<!-- Gambar 41: Potensi Pajak Kekayaan 50 Triliuner -->
<iframe src="https://henryai-sibermu.github.io/RO/embed/16_Reformasi_Fiskal_gambar41_plotly.html"
  width="100%" height="660" frameborder="0"
  style="border-radius:32px; background:#f7f4ff;" loading="lazy"></iframe>""", language="html")

chart_header("Pajak Kekayaan Pejabat Eksekutif dan Legislatif", "Gambar 42 — Hal. 72")
components.html(_G42.read_text(encoding="utf-8"), height=900, scrolling=False)
chart_footer("Data Forbes 50 orang terkaya 2026, diolah oleh peneliti")
with st.expander("🔗 Kode Embed WordPress — Gambar 42"):
    st.code("""<!-- Gambar 42: Pajak Kekayaan Pejabat Eksekutif dan Legislatif -->
<iframe src="https://henryai-sibermu.github.io/RO/embed/16_Reformasi_Fiskal_gambar42.html"
  width="100%" height="900" frameborder="0"
  style="border-radius:32px; background:#f7f4ff;" loading="lazy"></iframe>""", language="html")

chart_header("Simulasi Pajak Kekayaan Berdasarkan Ambang Batas Kekayaan", "Tabel 5 — Hal. 71")
components.html(_T5.read_text(encoding="utf-8"), height=620, scrolling=False)
chart_footer("Global Wealth Tax Simulator (2026), diolah CELIOS")
with st.expander("🔗 Kode Embed WordPress — Tabel 5"):
    st.code("""<!-- Tabel 5: Simulasi Pajak Kekayaan -->
<iframe src="https://henryai-sibermu.github.io/RO/embed/16_Reformasi_Fiskal_tabel5.html"
  width="100%" height="620" frameborder="0"
  style="border-radius:32px; background:#f7f4ff;" loading="lazy"></iframe>""", language="html")

chart_header("Skema Tax Benefit untuk Mengurangi Ketimpangan Ekonomi", "Gambar 43 — Hal. 75")
components.html(_G43.read_text(encoding="utf-8"), height=950, scrolling=False)
chart_footer("Analisis Peneliti")
with st.expander("🔗 Kode Embed WordPress — Gambar 43"):
    st.code("""<!-- Gambar 43: Skema Tax Benefit -->
<iframe src="https://henryai-sibermu.github.io/RO/embed/16_Reformasi_Fiskal_gambar43.html"
  width="100%" height="950" frameborder="0"
  style="border-radius:32px; background:#f7f4ff;" loading="lazy"></iframe>""", language="html")

chart_header("Penghapusan Pajak yang Membebani Kelas Menengah", "Tabel 7 — Hal. 76")
st.info("⏳ Data belum diinput. Lihat PDF hal. 76.")
chart_footer("Simulasi CELIOS, Forbes, diolah CELIOS (2026)")
