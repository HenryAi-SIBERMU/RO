import streamlit as st
import pandas as pd
from pathlib import Path
import streamlit.components.v1 as components

from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

st.set_page_config(
    page_title="Ketimpangan Historis Indonesia",
    layout="wide",
    page_icon=str(Path(__file__).resolve().parent.parent / "assets" / "logo_celios.png")
)
apply_embed_mode()
render_sidebar()

chart_header(
    "Ketimpangan Pendapatan dan Kekayaan, Indonesia, 1965-2024",
    "Proporsi 1% teratas terhadap total | Gambar 5 — Hal. 16"
)

G5_CHARTJS = Path(__file__).resolve().parent.parent / "embed" / "04_Ketimpangan_Historis_gambar5.html"
G5_PLOTLY = Path(__file__).resolve().parent.parent / "embed" / "04_Ketimpangan_Historis_gambar5_plotly.html"

tab_chartjs, tab_plotly = st.tabs(["Versi Chart.js", "Versi Plotly Alternatif"])

with tab_chartjs:
    components.html(G5_CHARTJS.read_text(encoding="utf-8"), height=620, scrolling=True)
    chart_footer("World Inequality Database (2024), diolah CELIOS")
    with st.expander("🔗 Kode Embed WordPress — Gambar 5 (Chart.js)"):
        st.code("""<!-- Gambar 5: Ketimpangan Pendapatan dan Kekayaan (Chart.js) -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/04_Ketimpangan_Historis_gambar5.html"
  width="100%" height="620" frameborder="0"
  style="border-radius:24px; background:#f7f5fc;"
  loading="lazy">
</iframe>""", language="html")

with tab_plotly:
    components.html(G5_PLOTLY.read_text(encoding="utf-8"), height=620, scrolling=True)
    chart_footer("World Inequality Database (2024), diolah CELIOS")
    with st.expander("🔗 Kode Embed WordPress — Gambar 5 (Plotly)"):
        st.code("""<!-- Gambar 5: Ketimpangan Pendapatan dan Kekayaan (Plotly) -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/04_Ketimpangan_Historis_gambar5_plotly.html"
  width="100%" height="620" frameborder="0"
  style="border-radius:24px; background:#f7f5fc;"
  loading="lazy">
</iframe>""", language="html")

# ── Catatan data ──────────────────────────────────────────────────────
DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "gambar05_ketimpangan_wid.csv"
df = pd.read_csv(DATA_PATH)

with st.expander("📋 Data lengkap (1965-2024)"):
    st.dataframe(
        df.rename(columns={
            "tahun": "Tahun",
            "pendapatan_top1": "Pendapatan 1% Teratas (%)",
            "kekayaan_top1": "Kekayaan 1% Teratas (%)",
        }),
        use_container_width=True,
        hide_index=True,
        height=400,
    )
