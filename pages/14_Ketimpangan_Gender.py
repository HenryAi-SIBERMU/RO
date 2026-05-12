import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

BASE_DIR = Path(__file__).resolve().parent.parent
_G27 = BASE_DIR / "embed" / "14_Ketimpangan_Gender_gambar27_plotly.html"
_G28 = BASE_DIR / "embed" / "14_Ketimpangan_Gender_gambar28_plotly.html"
_G30   = BASE_DIR / "embed" / "14_Ketimpangan_Gender_gambar30_plotly.html"
_G31_1 = BASE_DIR / "embed" / "14_Ketimpangan_Gender_gambar31_1_plotly.html"
_G31_2 = BASE_DIR / "embed" / "14_Ketimpangan_Gender_gambar31_2_plotly.html"
_G31_3 = BASE_DIR / "embed" / "14_Ketimpangan_Gender_gambar31_3_plotly.html"
_G32   = BASE_DIR / "embed" / "14_Ketimpangan_Gender_gambar32_plotly.html"

st.set_page_config(page_title="Ketimpangan Gender", layout="wide", page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png")
apply_embed_mode()
render_sidebar()

chart_header("Kurva Akumulasi Beban Ganda & Nilai Ekonomi Ibu Bekerja", "Gambar 27 — Hal. 52")
components.html(_G27.read_text(encoding="utf-8"), height=660, scrolling=True)
chart_footer("Perhitungan peneliti berdasarkan data BPS dan Sakernas, 2025")
with st.expander("🔗 Kode Embed WordPress — Gambar 27"):
    st.code("""<!-- Gambar 27: Kurva Akumulasi Beban Ganda & Nilai Ekonomi Ibu Bekerja -->
<iframe src="https://henryai-sibermu.github.io/RO/embed/14_Ketimpangan_Gender_gambar27_plotly.html"
  width="100%" height="660" frameborder="0"
  style="border-radius:32px; background:#f7f4ff;" loading="lazy"></iframe>""", language="html")

chart_header("Simulasi 2: Simulasi Nilai Ekonomi Kerja Ibu WFH", "Gambar 28 — Hal. 52")
components.html(_G28.read_text(encoding="utf-8"), height=660, scrolling=True)
chart_footer("Diolah oleh penulis (2026)")
with st.expander("🔗 Kode Embed WordPress — Gambar 28"):
    st.code("""<!-- Gambar 28: Kurva Produktivitas & Nilai Ekonomi Ibu WFH -->
<iframe src="https://henryai-sibermu.github.io/RO/embed/14_Ketimpangan_Gender_gambar28_plotly.html"
  width="100%" height="660" frameborder="0"
  style="border-radius:32px; background:#f7f4ff;" loading="lazy"></iframe>""", language="html")

chart_header("Lebih Banyak Perempuan Bekerja di Sektor Informal", "Gambar 30 — Hal. 54")
components.html(_G30.read_text(encoding="utf-8"), height=720, scrolling=True)
chart_footer("Sakernas Agustus 2025, diolah oleh peneliti")
with st.expander("🔗 Kode Embed WordPress — Gambar 30"):
    st.code("""<!-- Gambar 30: Lebih Banyak Perempuan Bekerja di Sektor Informal -->
<iframe src="https://henryai-sibermu.github.io/RO/embed/14_Ketimpangan_Gender_gambar30_plotly.html"
  width="100%" height="720" frameborder="0"
  style="border-radius:32px; background:#f7f4ff;" loading="lazy"></iframe>""", language="html")

chart_header("Kesenjangan Upah Berdasarkan Gender", "Gambar 31 — Hal. 54")
components.html(_G31_1.read_text(encoding="utf-8"), height=640, scrolling=True)
chart_footer("Sakernas Agustus 2025, diolah oleh peneliti")
with st.expander("🔗 Kode Embed WordPress — Gambar 31 (Distribusi Upah)"):
    st.code("""<!-- Gambar 31 (1): Perbedaan Distribusi Upah per Jam -->
<iframe src=\"https://henryai-sibermu.github.io/RO/embed/14_Ketimpangan_Gender_gambar31_1_plotly.html\"
  width=\"100%\" height=\"640\" frameborder=\"0\"
  style=\"border-radius:32px; background:#f7f4ff;\" loading=\"lazy\"></iframe>""", language="html")

components.html(_G31_2.read_text(encoding="utf-8"), height=640, scrolling=True)
chart_footer("Sakernas Agustus 2025, diolah oleh peneliti")
with st.expander("🔗 Kode Embed WordPress — Gambar 31 (Jam Kerja/Minggu)"):
    st.code("""<!-- Gambar 31 (2): Rata-rata Jam Kerja per Minggu -->
<iframe src=\"https://henryai-sibermu.github.io/RO/embed/14_Ketimpangan_Gender_gambar31_2_plotly.html\"
  width=\"100%\" height=\"640\" frameborder=\"0\"
  style=\"border-radius:32px; background:#f7f4ff;\" loading=\"lazy\"></iframe>""", language="html")

components.html(_G31_3.read_text(encoding="utf-8"), height=640, scrolling=True)
chart_footer("Sakernas Agustus 2025, diolah peneliti")
with st.expander("🔗 Kode Embed WordPress — Gambar 31 (Profil Upah per Usia)"):
    st.code("""<!-- Gambar 31 (3): Profil Upah Berdasarkan Usia -->
<iframe src=\"https://henryai-sibermu.github.io/RO/embed/14_Ketimpangan_Gender_gambar31_3_plotly.html\"
  width=\"100%\" height=\"640\" frameborder=\"0\"
  style=\"border-radius:32px; background:#f7f4ff;\" loading=\"lazy\"></iframe>""", language="html")

chart_header("Banyak Perempuan Putus Asa Mencari Kerja", "Gambar 32 — Hal. 55")
components.html(_G32.read_text(encoding="utf-8"), height=660, scrolling=True)
chart_footer("Sakernas Agustus 2025, diolah oleh peneliti")
with st.expander("🔗 Kode Embed WordPress — Gambar 32"):
    st.code("""<!-- Gambar 32: Banyak Perempuan Putus Asa Mencari Kerja -->
<iframe src=\"https://henryai-sibermu.github.io/RO/embed/14_Ketimpangan_Gender_gambar32_plotly.html\"
  width=\"100%\" height=\"660\" frameborder=\"0\"
  style=\"border-radius:32px; background:#f7f4ff;\" loading=\"lazy\"></iframe>""", language="html")
