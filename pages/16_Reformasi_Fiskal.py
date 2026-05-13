import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

BASE_DIR = Path(__file__).resolve().parent.parent
_G35 = BASE_DIR / "embed" / "16_Reformasi_Fiskal_gambar35.html"
_G36 = BASE_DIR / "embed" / "16_Reformasi_Fiskal_gambar36.html"
_T4  = BASE_DIR / "embed" / "16_Reformasi_Fiskal_tabel4.html"
_G37 = BASE_DIR / "embed" / "16_Reformasi_Fiskal_gambar37.html"
_G38 = BASE_DIR / "embed" / "16_Reformasi_Fiskal_gambar38.html"
_G39 = BASE_DIR / "embed" / "16_Reformasi_Fiskal_gambar39_plotly.html"
_G40 = BASE_DIR / "embed" / "16_Reformasi_Fiskal_gambar40_plotly.html"
_G41 = BASE_DIR / "embed" / "16_Reformasi_Fiskal_gambar41_plotly.html"
_T5  = BASE_DIR / "embed" / "16_Reformasi_Fiskal_tabel5.html"
_G42 = BASE_DIR / "embed" / "16_Reformasi_Fiskal_gambar42.html"
_G43 = BASE_DIR / "embed" / "16_Reformasi_Fiskal_gambar43.html"
_G44 = BASE_DIR / "embed" / "16_Reformasi_Fiskal_gambar44.html"
_G45 = BASE_DIR / "embed" / "16_Reformasi_Fiskal_gambar45_plotly.html"

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
components.html(_G36.read_text(encoding="utf-8"), height=1050, scrolling=False)
chart_footer("CELIOS (2025)")
with st.expander("🔗 Kode Embed WordPress — Gambar 36"):
    st.code("""<!-- Gambar 36: Peta Parpol Dikuasai Oligarki Politik -->
<iframe src="https://henryai-sibermu.github.io/RO/embed/16_Reformasi_Fiskal_gambar36.html"
  width="100%" height="1050" frameborder="0"
  style="border-radius:32px; background:#f0ecfb;" loading="lazy"></iframe>""", language="html")

chart_header("Akumulasi Harta Oligarki Politik", "Tabel 4 — Hal. 65")
components.html(_T4.read_text(encoding="utf-8"), height=820, scrolling=False)
chart_footer("LHKPN KPK dan media (2024)")
with st.expander("🔗 Kode Embed WordPress — Tabel 4"):
    st.code("""<!-- Tabel 4: Akumulasi Harta Oligarki Politik -->
<iframe src="https://henryai-sibermu.github.io/RO/embed/16_Reformasi_Fiskal_tabel4.html"
  width="100%" height="820" frameborder="0"
  style="border-radius:32px; background:#f0ecfb;" loading="lazy"></iframe>""", language="html")

chart_header("Rekomendasi: Mengurangi Ketimpangan & Pengaruh Oligarki", "Gambar 37 — Hal. 68")
components.html(_G37.read_text(encoding="utf-8"), height=1080, scrolling=False)
chart_footer("Diolah oleh peneliti")
with st.expander("🔗 Kode Embed WordPress — Gambar 37"):
    st.code("""<!-- Gambar 37: Rekomendasi Ketimpangan & Pengaruh Oligarki -->
<iframe src="https://henryai-sibermu.github.io/RO/embed/16_Reformasi_Fiskal_gambar37.html"
  width="100%" height="1080" frameborder="0"
  style="border-radius:32px; background:#f8f6fd;" loading="lazy"></iframe>""", language="html")

chart_header("Reformasi Fiskal melalui Tata Kelola Pajak", "Gambar 38 — Hal. 69")
components.html(_G38.read_text(encoding="utf-8"), height=800, scrolling=False)
chart_footer("Analisis Peneliti")
with st.expander("🔗 Kode Embed WordPress — Gambar 38"):
    st.code("""<!-- Gambar 38: Reformasi Fiskal melalui Tata Kelola Pajak -->
<iframe src="https://henryai-sibermu.github.io/RO/embed/16_Reformasi_Fiskal_gambar38.html"
  width="100%" height="800" frameborder="0"
  style="border-radius:32px; background:#f8f6fd;" loading="lazy"></iframe>""", language="html")

chart_header("Dukungan Publik terhadap Penerapan Pajak Kekayaan di Indonesia", "Gambar 39 — Hal. 70")
components.html(_G39.read_text(encoding="utf-8"), height=660, scrolling=True)
chart_footer("Survei Pajak Kekayaan CELIOS, 2025")
with st.expander("🔗 Kode Embed WordPress — Gambar 39"):
    st.code("""<!-- Gambar 39: Dukungan Publik terhadap Penerapan Pajak Kekayaan -->
<iframe src="https://henryai-sibermu.github.io/RO/embed/16_Reformasi_Fiskal_gambar39_plotly.html"
  width="100%" height="660" frameborder="0"
  style="border-radius:32px; background:#f7f4ff;" loading="lazy"></iframe>""", language="html")

chart_header("Persepsi Publik terhadap Dampak Pajak Kekayaan dalam Mengurangi Ketimpangan Ekonomi", "Gambar 40 — Hal. 71")
components.html(_G40.read_text(encoding="utf-8"), height=640, scrolling=True)
chart_footer("Survei Pajak Kekayaan CELIOS, 2025")
with st.expander("🔗 Kode Embed WordPress — Gambar 40"):
    st.code("""<!-- Gambar 40: Persepsi Publik Dampak Pajak Kekayaan -->
<iframe src="https://henryai-sibermu.github.io/RO/embed/16_Reformasi_Fiskal_gambar40_plotly.html"
  width="100%" height="640" frameborder="0"
  style="border-radius:32px; background:#f7f4ff;" loading="lazy"></iframe>""", language="html")

chart_header("Potensi Pajak Kekayaan 50 Triliuner (2019-2026)", "Gambar 41 — Hal. 72")
components.html(_G41.read_text(encoding="utf-8"), height=660, scrolling=True)
chart_footer("Data Forbes 50 orang terkaya 2026, diolah oleh peneliti")
with st.expander("🔗 Kode Embed WordPress — Gambar 41"):
    st.code("""<!-- Gambar 41: Potensi Pajak Kekayaan 50 Triliuner -->
<iframe src="https://henryai-sibermu.github.io/RO/embed/16_Reformasi_Fiskal_gambar41_plotly.html"
  width="100%" height="660" frameborder="0"
  style="border-radius:32px; background:#f7f4ff;" loading="lazy"></iframe>""", language="html")

chart_header("Simulasi Pajak Kekayaan Berdasarkan Ambang Batas Kekayaan", "Tabel 5 — Hal. 73")
components.html(_T5.read_text(encoding="utf-8"), height=620, scrolling=False)
chart_footer("Global Wealth Tax Simulator (2026), diolah CELIOS")
with st.expander("🔗 Kode Embed WordPress — Tabel 5"):
    st.code("""<!-- Tabel 5: Simulasi Pajak Kekayaan -->
<iframe src="https://henryai-sibermu.github.io/RO/embed/16_Reformasi_Fiskal_tabel5.html"
  width="100%" height="620" frameborder="0"
  style="border-radius:32px; background:#f7f4ff;" loading="lazy"></iframe>""", language="html")

chart_header("Pajak Kekayaan Pejabat Eksekutif dan Legislatif", "Gambar 42 — Hal. 74")
components.html(_G42.read_text(encoding="utf-8"), height=900, scrolling=False)
chart_footer("Data Forbes 50 orang terkaya 2026, diolah oleh peneliti")
with st.expander("🔗 Kode Embed WordPress — Gambar 42"):
    st.code("""<!-- Gambar 42: Pajak Kekayaan Pejabat Eksekutif dan Legislatif -->
<iframe src="https://henryai-sibermu.github.io/RO/embed/16_Reformasi_Fiskal_gambar42.html"
  width="100%" height="900" frameborder="0"
  style="border-radius:32px; background:#f7f4ff;" loading="lazy"></iframe>""", language="html")

chart_header("Skema Tax Benefit untuk Mengurangi Ketimpangan Ekonomi", "Gambar 43 — Hal. 75")
components.html(_G43.read_text(encoding="utf-8"), height=950, scrolling=False)
chart_footer("Analisis Peneliti")
with st.expander("🔗 Kode Embed WordPress — Gambar 43"):
    st.code("""<!-- Gambar 43: Skema Tax Benefit -->
<iframe src="https://henryai-sibermu.github.io/RO/embed/16_Reformasi_Fiskal_gambar43.html"
  width="100%" height="950" frameborder="0"
  style="border-radius:32px; background:#f7f4ff;" loading="lazy"></iframe>""", language="html")

chart_header("Alur Pengesahan Aturan Pembiayaan Publik Partai Politik", "Gambar 44 — Hal. 76")
components.html(_G44.read_text(encoding="utf-8"), height=1050, scrolling=False)
chart_footer("Diolah oleh peneliti")
with st.expander("🔗 Kode Embed WordPress — Gambar 44"):
    st.code("""<!-- Gambar 44: Alur Pengesahan Aturan Pembiayaan Publik Partai Politik -->
<iframe src="https://henryai-sibermu.github.io/RO/embed/16_Reformasi_Fiskal_gambar44.html"
  width="100%" height="1050" frameborder="0"
  style="border-radius:32px; background:#f7f4ff;" loading="lazy"></iframe>""", language="html")

chart_header("Donasi Korporasi ke Partai Politik", "Gambar 45 — Hal. 77")
components.html(_G45.read_text(encoding="utf-8"), height=760, scrolling=False)
chart_footer("The International Institute for Democracy and Electoral Assistance")
with st.expander("🔗 Kode Embed WordPress — Gambar 45"):
    st.code("""<!-- Gambar 45: Donasi Korporasi ke Partai Politik (World Map) -->
<iframe src="https://henryai-sibermu.github.io/RO/embed/16_Reformasi_Fiskal_gambar45_plotly.html"
  width="100%" height="760" frameborder="0"
  style="border-radius:32px; background:#f7f4ff;" loading="lazy"></iframe>""", language="html")
