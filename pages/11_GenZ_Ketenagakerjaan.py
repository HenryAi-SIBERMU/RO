import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

BASE_DIR = Path(__file__).resolve().parent.parent
_G17          = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar17.html"
_G18_chartjs  = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar18_chartjs.html"
_G18_plotly   = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar18_plotly.html"
_G19_plotly   = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar19_plotly.html"
_G20_plotly   = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar20_plotly.html"
_G21a_plotly  = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar21a_plotly.html"
_G21b_plotly  = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar21b_plotly.html"
_G21c_plotly  = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar21c_plotly.html"
_G21d_plotly  = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar21d_plotly.html"
_G21e_plotly  = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar21e_plotly.html"
_G21f_plotly  = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar21f_plotly.html"
_G22_plotly   = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar22_plotly.html"
_G23          = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar23.html"
_G23b         = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar23b.html"

st.set_page_config(page_title="Gen Z & Ketenagakerjaan", layout="wide", page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png")
apply_embed_mode()
render_sidebar()

chart_header("Generasi Muda yang Terhimpit Sistem Oligarki", "Gambar 17 — Hal. 34")
components.html(_G17.read_text(encoding="utf-8"), height=700, scrolling=True)
chart_footer("Diolah oleh peneliti")
with st.expander("🔗 Kode Embed WordPress — Gambar 17"):
    st.code("""<iframe src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar17.html"
  width="100%" height="700" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;" loading="lazy"></iframe>""", language="html")

chart_header("Gen Z Paling Lama Menganggur", "Gambar 18 — Hal. 32")
tab_g18_chartjs, tab_g18_plotly = st.tabs(["Versi Chart.js", "Versi Plotly"])
with tab_g18_chartjs:
    components.html(_G18_chartjs.read_text(encoding="utf-8"), height=640, scrolling=True)
with tab_g18_plotly:
    components.html(_G18_plotly.read_text(encoding="utf-8"), height=640, scrolling=True)
chart_footer("Sakernas Agustus 2025; diolah peneliti")
with st.expander("🔗 Kode Embed WordPress — Gambar 18 (Chart.js)"):
    st.code("""<!-- Gambar 18: Gen Z Paling Lama Menganggur — Chart.js -->
<iframe src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar18_chartjs.html"
  width="100%" height="640" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;" loading="lazy"></iframe>""", language="html")
with st.expander("🔗 Kode Embed WordPress — Gambar 18 (Plotly)"):
    st.code("""<!-- Gambar 18: Gen Z Paling Lama Menganggur — Plotly -->
<iframe src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar18_plotly.html"
  width="100%" height="640" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;" loading="lazy"></iframe>""", language="html")

chart_header("Lulusan Sarjana dan Gen Z Menjadi Pekerja Kasar", "Gambar 19 — Hal. 33")
components.html(_G19_plotly.read_text(encoding="utf-8"), height=640, scrolling=True)
chart_footer("Sakernas Agustus 2025; diolah peneliti")
with st.expander("🔗 Kode Embed WordPress — Gambar 19 (Plotly)"):
    st.code("""<!-- Gambar 19: Lulusan Sarjana dan Gen Z menjadi Pekerja Kasar — Plotly -->
<iframe src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar19_plotly.html"
  width="100%" height="640" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;" loading="lazy"></iframe>""", language="html")

chart_header("Dekomposisi Kesenjangan Upah Gen Z", "Gambar 20 — Hal. 34")
components.html(_G20_plotly.read_text(encoding="utf-8"), height=820, scrolling=True)
chart_footer("Sakernas Agustus 2025; diolah peneliti")
with st.expander("🔗 Kode Embed WordPress — Gambar 20 (Plotly)"):
    st.code("""<!-- Gambar 20: Dekomposisi Kesenjangan Upah Gen Z — Plotly -->
<iframe src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar20_plotly.html"
  width="100%" height="820" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;" loading="lazy"></iframe>""", language="html")

chart_header("Ketersediaan Jaminan Kesehatan di Tempat Kerja", "Gambar 21a — Hal. 35")
components.html(_G21a_plotly.read_text(encoding="utf-8"), height=620, scrolling=True)
chart_footer("Sakernas Agustus 2025; diolah peneliti")
with st.expander("🔗 Kode Embed WordPress — Gambar 21a (Plotly)"):
    st.code("""<iframe src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar21a_plotly.html"
  width="100%" height="620" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;" loading="lazy"></iframe>""", language="html")

chart_header("Ketersediaan Jaminan Kecelakaan di Tempat Kerja", "Gambar 21b — Hal. 35")
components.html(_G21b_plotly.read_text(encoding="utf-8"), height=620, scrolling=True)
chart_footer("Sakernas Agustus 2025; diolah peneliti")
with st.expander("🔗 Kode Embed WordPress — Gambar 21b (Plotly)"):
    st.code("""<iframe src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar21b_plotly.html"
  width="100%" height="620" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;" loading="lazy"></iframe>""", language="html")

chart_header("Ketersediaan Jaminan Kematian di Tempat Kerja", "Gambar 21c — Hal. 35")
components.html(_G21c_plotly.read_text(encoding="utf-8"), height=620, scrolling=True)
chart_footer("Sakernas Agustus 2025; diolah peneliti")
with st.expander("🔗 Kode Embed WordPress — Gambar 21c (Plotly)"):
    st.code("""<iframe src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar21c_plotly.html"
  width="100%" height="620" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;" loading="lazy"></iframe>""", language="html")

chart_header("Ketersediaan Jaminan Hari Tua di Tempat Kerja", "Gambar 21d — Hal. 36")
components.html(_G21d_plotly.read_text(encoding="utf-8"), height=620, scrolling=True)
chart_footer("Sakernas Agustus 2025; diolah peneliti")
with st.expander("🔗 Kode Embed WordPress — Gambar 21d (Plotly)"):
    st.code("""<iframe src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar21d_plotly.html"
  width="100%" height="620" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;" loading="lazy"></iframe>""", language="html")

chart_header("Ketersediaan Jaminan Pensiun di Tempat Kerja", "Gambar 21e — Hal. 36")
components.html(_G21e_plotly.read_text(encoding="utf-8"), height=620, scrolling=True)
chart_footer("Sakernas Agustus 2025; diolah peneliti")
with st.expander("🔗 Kode Embed WordPress — Gambar 21e (Plotly)"):
    st.code("""<iframe src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar21e_plotly.html"
  width="100%" height="620" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;" loading="lazy"></iframe>""", language="html")

chart_header("Ketersediaan Jaminan Kehilangan Pekerjaan", "Gambar 21f — Hal. 36")
components.html(_G21f_plotly.read_text(encoding="utf-8"), height=620, scrolling=True)
chart_footer("Sakernas Agustus 2025; diolah peneliti")
with st.expander("🔗 Kode Embed WordPress — Gambar 21f (Plotly)"):
    st.code("""<iframe src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar21f_plotly.html"
  width="100%" height="620" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;" loading="lazy"></iframe>""", language="html")

chart_header("Cuti Tidak Berbayar Generasi Muda", "Gambar 22 — Hal. 37")
components.html(_G22_plotly.read_text(encoding="utf-8"), height=500, scrolling=True)
chart_footer("Sakernas Agustus 2025; diolah peneliti")
with st.expander("🔗 Kode Embed WordPress — Gambar 22 (Plotly)"):
    st.code("""<iframe src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar22_plotly.html"
  width="100%" height="500" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;" loading="lazy"></iframe>""", language="html")

chart_header("Generasi Muda Menanggung Beban Ekonomi yang Timpang", "Gambar 23 — Hal. 38")
components.html(_G23.read_text(encoding="utf-8"), height=720, scrolling=True)
chart_footer("Diolah oleh peneliti")
with st.expander("🔗 Kode Embed WordPress — Gambar 23"):
    st.code("""<iframe src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar23.html"
  width="100%" height="720" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;" loading="lazy"></iframe>""", language="html")

chart_header("Apakah Meritokrasi Masih Dianggap Penting di Indonesia?", "Gambar 23b — Hal. 38")
components.html(_G23b.read_text(encoding="utf-8"), height=860, scrolling=True)
chart_footer("Diolah oleh peneliti")
with st.expander("🔗 Kode Embed WordPress — Gambar 23b"):
    st.code("""<iframe src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar23b.html"
  width="100%" height="860" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;" loading="lazy"></iframe>""", language="html")
