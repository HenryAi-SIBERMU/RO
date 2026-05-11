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

_G7 = Path(__file__).resolve().parent.parent / "embed" / "06_Harta_Pejabat_gambar7.html"
components.html(_G7.read_text(encoding="utf-8"), height=560, scrolling=True)

chart_footer("Data Laporan Harta Kekayaan Penyelenggara Negara (2026), diolah CELIOS")

with st.expander("🔗 Kode Embed WordPress — Gambar 7"):
    st.code("""<!-- Gambar 7: Total Harta Pejabat Publik Kabinet (2019–2025) -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/06_Harta_Pejabat_gambar7.html"
  width="100%" height="560" frameborder="0"
  style="border-radius:12px; box-shadow:0 8px 24px rgba(86,31,139,0.15);"
  loading="lazy">
</iframe>""", language="html")

st.divider()
chart_header("Klasemen Pejabat Terkaya Kabinet Merah Putih 2025", "Gambar 8 — Hal. 21")
st.info("⏳ Data belum diinput. Lihat PDF hal. 21.")
chart_footer("LHKPN KPK, diolah CELIOS (2026)")
