import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

st.set_page_config(page_title="Oligarki & Parpol", layout="wide", page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png")
apply_embed_mode()
render_sidebar()

_G9_embed = Path(__file__).resolve().parent.parent / "embed" / "07_Oligarki_Parpol_gambar9.html"
_G10_chartjs = Path(__file__).resolve().parent.parent / "embed" / "07_Oligarki_Parpol_gambar10_chartjs.html"
_G10_plotly = Path(__file__).resolve().parent.parent / "embed" / "07_Oligarki_Parpol_gambar10_plotly.html"
_T2_embed = Path(__file__).resolve().parent.parent / "embed" / "07_Oligarki_Parpol_tabel2.html"

chart_header("Peta Partai Politik: Jumlah Kursi vs Konsentrasi Kekayaan", "Gambar 9 — Hal. 23")
components.html(_G9_embed.read_text(encoding="utf-8"), height=880, scrolling=True)
chart_footer("LHKPN KPK (2025), diolah CELIOS")
with st.expander("🔗 Kode Embed WordPress — Gambar 9"):
    st.code("""<!-- Gambar 9: Peta Partai Politik Berbasis Jumlah Kursi dan Konsentrasi Kekayaan -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/07_Oligarki_Parpol_gambar9.html"
  width="100%" height="880" frameborder="0"
  style="border-radius:32px; background:#fff;"
  loading="lazy">
</iframe>""", language="html")

chart_header("Perbandingan Rata-Rata Kekayaan Elite vs Masyarakat Umum", "Gambar 10 — Hal. 25")
tab_chartjs, tab_plotly = st.tabs(["Versi Chart.js", "Versi Plotly"])
with tab_chartjs:
    components.html(_G10_chartjs.read_text(encoding="utf-8"), height=1180, scrolling=True)
with tab_plotly:
    components.html(_G10_plotly.read_text(encoding="utf-8"), height=1200, scrolling=True)
chart_footer("LHKPN KPK (2025), diolah CELIOS")
with st.expander("🔗 Kode Embed WordPress — Gambar 10 (Chart.js)"):
    st.code("""<!-- Gambar 10: Kekayaan Elit vs Publik (Chart.js) -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/07_Oligarki_Parpol_gambar10_chartjs.html"
  width="100%" height="1180" frameborder="0"
  style="border-radius:32px; background:#f6f4ff;"
  loading="lazy">
</iframe>""", language="html")
with st.expander("🔗 Kode Embed WordPress — Gambar 10 (Plotly)"):
    st.code("""<!-- Gambar 10: Kekayaan Elit vs Publik (Plotly) -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/07_Oligarki_Parpol_gambar10_plotly.html"
  width="100%" height="1200" frameborder="0"
  style="border-radius:32px; background:#f6f4ff;"
  loading="lazy">
</iframe>""", language="html")

chart_header("Distribusi Kekayaan Seluruh Pejabat Publik per Dapil", "Gambar X — Hal. 25")
st.info("⏳ Data belum diinput. Lihat PDF hal. 25.")

chart_header("Kekayaan Anggota DPR RI berdasarkan Fraksi Partai Politik", "Tabel 2 — Hal. 24")
components.html(_T2_embed.read_text(encoding="utf-8"), height=1580, scrolling=True)
chart_footer("LHKPN KPK (2026), diolah CELIOS")
with st.expander("🔗 Kode Embed WordPress — Tabel 2"):
    st.code("""<!-- Tabel 2: Kekayaan Anggota DPR RI berdasarkan Fraksi Partai Politik -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/07_Oligarki_Parpol_tabel2.html"
  width="100%" height="1580" frameborder="0"
  style="border-radius:32px; background:#5526b5;"
  loading="lazy">
</iframe>""", language="html")

chart_footer("LHKPN KPK, diolah CELIOS (2026)")
