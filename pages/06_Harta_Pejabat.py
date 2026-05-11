import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

st.set_page_config(page_title="Harta Pejabat Publik", layout="wide", page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png")
apply_embed_mode()
render_sidebar()

chart_header("Total Harta Pejabat Publik Kabinet (2019–2025)", "Gambar 7 — Hal. 20")

_G7_chartjs = Path(__file__).resolve().parent.parent / "embed" / "06_Harta_Pejabat_gambar7.html"
_G7_plotly = Path(__file__).resolve().parent.parent / "embed" / "06_Harta_Pejabat_gambar7_plotly.html"
_G8_chartjs = Path(__file__).resolve().parent.parent / "embed" / "06_Harta_Pejabat_gambar8.html"
_G8_plotly = Path(__file__).resolve().parent.parent / "embed" / "06_Harta_Pejabat_gambar8_plotly.html"

tab_chartjs, tab_plotly = st.tabs(["Versi Chart.js", "Versi Plotly"])

with tab_chartjs:
    components.html(_G7_chartjs.read_text(encoding="utf-8"), height=560, scrolling=True)
    chart_footer("Data Laporan Harta Kekayaan Penyelenggara Negara (2026), diolah CELIOS")
    with st.expander("🔗 Kode Embed WordPress — Gambar 7 (Chart.js)"):
        st.code("""<!-- Gambar 7: Total Harta Pejabat Publik Kabinet (2019–2025) — Versi Chart.js -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/06_Harta_Pejabat_gambar7.html"
  width="100%" height="560" frameborder="0"
  style="border-radius:32px; background:#fff;"
  loading="lazy">
</iframe>""", language="html")

with tab_plotly:
    components.html(_G7_plotly.read_text(encoding="utf-8"), height=560, scrolling=True)
    chart_footer("Data Laporan Harta Kekayaan Penyelenggara Negara (2026), diolah CELIOS")
    with st.expander("🔗 Kode Embed WordPress — Gambar 7 (Plotly)"):
        st.code("""<!-- Gambar 7: Total Harta Pejabat Publik Kabinet (2019–2025) — Versi Plotly -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/06_Harta_Pejabat_gambar7_plotly.html"
  width="100%" height="560" frameborder="0"
  style="border-radius:32px; background:#fff;"
  loading="lazy">
</iframe>""", language="html")

st.divider()
chart_header("Klasemen Pejabat Terkaya Kabinet Merah Putih 2025", "Gambar 8 — Hal. 21")

tab_g8_chartjs, tab_g8_plotly = st.tabs(["Replika PDF (Statis)", "Versi Interaktif (Filter)"])

with tab_g8_chartjs:
    components.html(_G8_chartjs.read_text(encoding="utf-8"), height=2300, scrolling=True)
    chart_footer("LHKPN (2025), diolah CELIOS")
    with st.expander("🔗 Kode Embed WordPress — Gambar 8 (Replika Statis)"):
        st.code("""<!-- Gambar 8: Klasemen Pejabat Publik Terkaya Kabinet Merah Putih 2025 — Replika Statis -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/06_Harta_Pejabat_gambar8.html"
  width="100%" height="2320" frameborder="0"
  style="border-radius:32px; background:#5a26b6;"
  loading="lazy">
</iframe>""", language="html")

with tab_g8_plotly:
    components.html(_G8_plotly.read_text(encoding="utf-8"), height=2300, scrolling=True)
    chart_footer("LHKPN (2025), diolah CELIOS")
    with st.expander("🔗 Kode Embed WordPress — Gambar 8 (Interaktif)"):
        st.code("""<!-- Gambar 8: Klasemen Pejabat Publik Terkaya Kabinet Merah Putih 2025 — Versi Interaktif -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/06_Harta_Pejabat_gambar8_plotly.html"
  width="100%" height="2320" frameborder="0"
  style="border-radius:32px; background:#5a26b6;"
  loading="lazy">
</iframe>""", language="html")
