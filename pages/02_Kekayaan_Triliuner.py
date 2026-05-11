import streamlit as st
import pandas as pd
from pathlib import Path
import streamlit.components.v1 as components
from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

st.set_page_config(page_title="Total Kekayaan 50 Triliuner", layout="wide", page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png")
apply_embed_mode()
render_sidebar()

chart_header("Total Kekayaan 50 Triliuner di Indonesia", "Dalam triliun rupiah | Gambar 3 — Hal. 12")

_G3_CHART = Path(__file__).resolve().parent.parent / "embed" / "02_Kekayaan_Triliuner.html"
_G3_PLOTLY = Path(__file__).resolve().parent.parent / "embed" / "02_Kekayaan_Triliuner_plotly.html"

tab_chart, tab_plotly = st.tabs(["Versi Chart.js", "Versi Plotly Alternatif"])

with tab_chart:
    components.html(_G3_CHART.read_text(encoding="utf-8"), height=640, scrolling=True)
    chart_footer("Data Forbes 50 orang terkaya di Indonesia (2026), diolah oleh peneliti")
    with st.expander("🔗 Kode Embed WordPress — Gambar 3 (Chart.js)"):
        st.code("""<!-- Gambar 3: Total Kekayaan 50 Triliuner di Indonesia — Versi Chart.js -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/02_Kekayaan_Triliuner.html"
  width="100%" height="640" frameborder="0"
  style="border-radius:32px; background:#f3efff;"
  loading="lazy">
</iframe>""", language="html")

with tab_plotly:
    components.html(_G3_PLOTLY.read_text(encoding="utf-8"), height=640, scrolling=True)
    chart_footer("Data Forbes 50 orang terkaya di Indonesia (2026), diolah oleh peneliti")
    with st.expander("🔗 Kode Embed WordPress — Gambar 3 (Plotly)"):
        st.code("""<!-- Gambar 3: Total Kekayaan 50 Triliuner di Indonesia — Versi Plotly -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/02_Kekayaan_Triliuner_plotly.html"
  width="100%" height="640" frameborder="0"
  style="border-radius:32px; background:#f3efff;"
  loading="lazy">
</iframe>""", language="html")

# ── Data ─────────────────────────────────────────────────────────────
DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "gambar03_kekayaan_triliuner.csv"
df = pd.read_csv(DATA_PATH)
df["tahun"] = df["tahun"].astype(str)

# ── Catatan data ──────────────────────────────────────────────────────
with st.expander("📋 Data lengkap"):
    st.dataframe(
        df.rename(columns={
            "tahun": "Tahun",
            "total_kekayaan": "Total Kekayaan (T Rp)",
            "sektor_ekstraktif": "Sektor Ekstraktif (T Rp)",
            "persen_ekstraktif": "% Sektor Ekstraktif",
        }),
        use_container_width=True,
        hide_index=True,
    )

with st.expander("🔗 Kode Embed WordPress — Gambar 3"):
    st.code("""<!-- Gambar 3: Total Kekayaan 50 Triliuner di Indonesia -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/02_Kekayaan_Triliuner.html"
  width="100%" height="520" frameborder="0"
  style="border-radius:8px; box-shadow:0 2px 8px rgba(0,0,0,0.1);"
  loading="lazy">
</iframe>""", language="html")

# ── Grid 50 Triliuner ────────────────────────────────────────────────
st.divider()
chart_header("50 Orang Terkaya Indonesia — Diurutkan berdasarkan CAGR", "Hal. 6–7 (spread overview)")
_GRID_PATH = Path(__file__).resolve().parent.parent / "assets" / "gambar03_triliuner_grid.html"
with open(_GRID_PATH, "r", encoding="utf-8") as _f:
    components.html(_f.read(), height=1700, scrolling=True)

with st.expander("🔗 Kode Embed WordPress — Grid 50 Triliuner"):
    st.code("""<!-- Grid 50 Orang Terkaya Indonesia (CAGR Ranking) -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/02_Kekayaan_Triliuner_grid.html"
  width="100%" height="1700" frameborder="0"
  style="border-radius:8px; box-shadow:0 2px 8px rgba(0,0,0,0.1);"
  loading="lazy">
</iframe>""", language="html")

# ── Tabel 1 — Hal. 13 ────────────────────────────────────────────────
st.divider()
chart_header("Peningkatan Kekayaan Orang Superkaya di Indonesia", "Tabel 1 — Hal. 13")

_T1_PATH = Path(__file__).resolve().parent.parent / "data" / "page013_tabel1.csv"
_df_t1 = pd.read_csv(_T1_PATH)
_df_t1.columns = ["#", "Nama", "Kekayaan 2026 (T Rp)", "CAGR (%)"]
_df_t1["Kekayaan 2026 (T Rp)"] = _df_t1["Kekayaan 2026 (T Rp)"].apply(lambda x: f"Rp {x:,.2f} T")
_df_t1["CAGR (%)"] = _df_t1["CAGR (%)"].apply(lambda x: f"+{x:.1f}%" if x > 0 else f"{x:.1f}%")
st.dataframe(_df_t1, use_container_width=True, hide_index=True, height=420)

with st.expander("🔗 Kode Embed WordPress — Tabel 1"):
    st.code("""<!-- Tabel 1: Peningkatan Kekayaan Orang Superkaya di Indonesia -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/02_Kekayaan_Triliuner_tabel1.html"
  width="100%" height="500" frameborder="0"
  style="border-radius:8px; box-shadow:0 2px 8px rgba(0,0,0,0.1);"
  loading="lazy">
</iframe>""", language="html")

# ── Infografik: Proyeksi 2050 — 111 Juta Penduduk ───────────────────────
st.divider()
chart_header("Proyeksi Kekayaan 50 Superkaya vs 111 Juta Penduduk (2050)", "Infografik — Hal. 16")

_INFO = Path(__file__).resolve().parent.parent / "embed" / "02_Kekayaan_Triliuner_infografik_proyeksi.html"
_INFO_D3 = Path(__file__).resolve().parent.parent / "embed" / "02_Kekayaan_Triliuner_infografik_proyeksi_d3race.html"

tab_d3, tab_static = st.tabs(["Versi Alternatif D3 Race", "Versi Statis (Chart)"])

with tab_d3:
    components.html(_INFO_D3.read_text(encoding="utf-8"), height=620, scrolling=True)
    chart_footer("Dummy illustratif — Ganti dengan data resmi sebelum rilis")
    with st.expander("🔗 Kode Embed WordPress — Proyeksi 2050 (D3 Race)"):
        st.code("""<!-- Eksperimen D3.js: Bar Chart Race Kekayaan 50 Triliuner (Dummy) -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/02_Kekayaan_Triliuner_infografik_proyeksi_d3race.html"
  width="100%" height="620" frameborder="0"
  style="border-radius:32px; background:#1d0d2f;"
  loading="lazy">
</iframe>""", language="html")

with tab_static:
    components.html(_INFO.read_text(encoding="utf-8"), height=660, scrolling=True)
    chart_footer("Forbes, diolah CELIOS (2026)")
    with st.expander("🔗 Kode Embed WordPress — Proyeksi 2050 (Statis)"):
        st.code("""<!-- Infografik: Proyeksi Kekayaan 50 Superkaya vs 111 Juta Penduduk — Versi Statis -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/02_Kekayaan_Triliuner_infografik_proyeksi.html"
  width="100%" height="660" frameborder="0"
  style="border-radius:32px; background:#49138d;"
  loading="lazy">
</iframe>""", language="html")

# ── Gambar 2 — Hal. 16 ────────────────────────────────────────────────
st.divider()
chart_header("Proyeksi Kekayaan 50 Superkaya hingga 2050", "Gambar 2 — Hal. 16")

_G2_STATIC = Path(__file__).resolve().parent.parent / "embed" / "02_Kekayaan_Triliuner_gambar2.html"
_G2_ANIM = Path(__file__).resolve().parent.parent / "embed" / "02_Kekayaan_Triliuner_gambar2_anim.html"

tab_g2_anim, tab_g2_static = st.tabs(["Versi Animasi (Loop)", "Versi Statis"])

with tab_g2_anim:
    components.html(_G2_ANIM.read_text(encoding="utf-8"), height=560, scrolling=True)
    chart_footer("Forbes & Global Wealth Report, diolah CELIOS (2026)")
    with st.expander("🔗 Kode Embed WordPress — Gambar 2 (Animasi)"):
        st.code("""<!-- Gambar 2: Proyeksi Kekayaan 50 Superkaya hingga 2050 — Versi Animasi -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/02_Kekayaan_Triliuner_gambar2_anim.html"
  width="100%" height="560" frameborder="0"
  style="border-radius:20px; background:#f7f7f7;"
  loading="lazy">
</iframe>""", language="html")

with tab_g2_static:
    components.html(_G2_STATIC.read_text(encoding="utf-8"), height=560, scrolling=True)
    chart_footer("Forbes & Global Wealth Report, diolah CELIOS (2026)")
    with st.expander("🔗 Kode Embed WordPress — Gambar 2 (Statis)"):
        st.code("""<!-- Gambar 2: Proyeksi Kekayaan 50 Superkaya hingga 2050 -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/02_Kekayaan_Triliuner_gambar2.html"
  width="100%" height="560" frameborder="0"
  style="border-radius:20px; background:#f7f7f7;"
  loading="lazy">
</iframe>""", language="html")
