import streamlit as st
import plotly.graph_objects as go
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

# ── Warna (matching PDF) ──────────────────────────────────────────────
COLOR_TOTAL      = "#9B8FD8"   # light purple — tall bars
COLOR_EKSTRAKTIF = "#2B1B8F"   # dark navy   — shorter bars
COLOR_ORANGE     = "#FFC107"   # amber/yellow — persentase line
COLOR_BG         = "#F2EEFF"   # light lavender background

# ── Data ─────────────────────────────────────────────────────────────
DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "gambar03_kekayaan_triliuner.csv"
df = pd.read_csv(DATA_PATH)
df["tahun"] = df["tahun"].astype(str)

def fmt_rp(v):
    return "Rp" + f"{int(v):,}".replace(",", ".")

# ── Figure ────────────────────────────────────────────────────────────
fig = go.Figure()

# Bar 1 — Total Kekayaan (light purple, taller)
fig.add_trace(go.Bar(
    name="Total Kekayaan",
    x=df["tahun"],
    y=df["total_kekayaan"],
    marker_color=COLOR_TOTAL,
    marker_line_width=0,
    text=[fmt_rp(v) for v in df["total_kekayaan"]],
    textposition="outside",
    textfont=dict(size=10, color="#4B3FA0", family="Arial"),
    hovertemplate="<b>%{x}</b><br>Total: <b>%{text}</b> triliun<extra></extra>",
))

# Bar 2 — Kekayaan dari Sektor Ekstraktif (dark navy, shorter)
fig.add_trace(go.Bar(
    name="Kekayaan dari Sektor Ekstraktif",
    x=df["tahun"],
    y=df["sektor_ekstraktif"],
    marker_color=COLOR_EKSTRAKTIF,
    marker_line_width=0,
    text=[fmt_rp(v) for v in df["sektor_ekstraktif"]],
    textposition="inside",
    textfont=dict(size=9, color="white", family="Arial"),
    hovertemplate="<b>%{x}</b><br>Sektor Ekstraktif: <b>%{text}</b> triliun<extra></extra>",
))

# Scatter — Persentase Sektor Ekstraktif (orange line + labels)
fig.add_trace(go.Scatter(
    name="Persentase Sektor Ekstraktif",
    x=df["tahun"],
    y=df["persen_ekstraktif"],
    mode="lines+markers+text",
    line=dict(color=COLOR_ORANGE, width=2.5),
    marker=dict(color=COLOR_ORANGE, size=9, symbol="circle"),
    text=[f"<b>{v:.1f}%</b>" for v in df["persen_ekstraktif"]],
    textposition="top center",
    textfont=dict(size=10, color=COLOR_ORANGE, family="Arial Black"),
    yaxis="y2",
    hovertemplate="<b>%{x}</b><br>Proporsi Ekstraktif: <b>%{y:.1f}%</b><extra></extra>",
))

# ── Layout ────────────────────────────────────────────────────────────
fig.update_layout(
    barmode="group",
    bargap=0.3,
    bargroupgap=0.08,
    plot_bgcolor=COLOR_BG,
    paper_bgcolor="white",
    legend=dict(
        orientation="h",
        y=-0.18,
        x=0,
        xanchor="left",
        font=dict(size=12, family="Arial"),
        bgcolor="rgba(0,0,0,0)",
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor="#E0D8F8",
        gridwidth=1,
        zeroline=False,
        showticklabels=False,
        range=[0, 6000],
    ),
    yaxis2=dict(
        overlaying="y",
        side="right",
        showticklabels=False,
        showgrid=False,
        range=[0, 100],
        zeroline=False,
    ),
    xaxis=dict(
        type="category",
        tickfont=dict(size=12, color="#333", family="Arial"),
        showgrid=False,
    ),
    margin=dict(t=100, b=100, l=20, r=60),
    height=520,
)

st.plotly_chart(fig, use_container_width=True)

chart_footer("Data Forbes 50 orang terkaya di Indonesia (2026), diolah oleh peneliti")

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
components.html(_INFO.read_text(encoding="utf-8"), height=620, scrolling=True)

chart_footer("Forbes, diolah CELIOS (2026)")

with st.expander("🔗 Kode Embed WordPress — Infografik Proyeksi 2050"):
    st.code("""<!-- Infografik: Proyeksi Kekayaan 50 Superkaya vs 111 Juta Penduduk -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/02_Kekayaan_Triliuner_infografik_proyeksi.html"
  width="100%" height="620" frameborder="0"
  style="border-radius:8px; box-shadow:0 2px 8px rgba(0,0,0,0.1);"
  loading="lazy">
</iframe>""", language="html")

# ── Gambar 2 — Hal. 16 ────────────────────────────────────────────────
st.divider()
chart_header("Proyeksi Kekayaan 50 Superkaya hingga 2050", "Gambar 2 — Hal. 16")

_G2 = Path(__file__).resolve().parent.parent / "embed" / "02_Kekayaan_Triliuner_gambar2.html"
components.html(_G2.read_text(encoding="utf-8"), height=560, scrolling=True)

chart_footer("Forbes, diolah CELIOS (2026)")

with st.expander("🔗 Kode Embed WordPress — Gambar 2"):
    st.code("""<!-- Gambar 2: Proyeksi Kekayaan 50 Superkaya hingga 2050 -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/02_Kekayaan_Triliuner_gambar2.html"
  width="100%" height="560" frameborder="0"
  style="border-radius:8px; box-shadow:0 2px 8px rgba(0,0,0,0.1);"
  loading="lazy">
</iframe>""", language="html")
