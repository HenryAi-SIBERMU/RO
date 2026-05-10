import streamlit as st
import plotly.graph_objects as go
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

# ── Warna (matching PDF) ──────────────────────────────────────────────
COLOR_PENDAPATAN = "#A52A2A"   # maroon/brown - pendapatan
COLOR_KEKAYAAN   = "#7B3CBA"   # purple - kekayaan
COLOR_BG         = "#FAFAFA"   # light gray background

# ── Data ─────────────────────────────────────────────────────────────
DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "gambar05_ketimpangan_wid.csv"
df = pd.read_csv(DATA_PATH)

# ── Figure ────────────────────────────────────────────────────────────
fig = go.Figure()

# Line 1 — Pendapatan Nasional sebelum pajak (Maroon)
fig.add_trace(go.Scatter(
    name="Pendapatan Nasional sebelum pajak | Proporsi 1% teratas",
    x=df["tahun"],
    y=df["pendapatan_top1"],
    mode="lines",
    line=dict(color=COLOR_PENDAPATAN, width=3),
    hovertemplate="<b>%{x}</b><br>Pendapatan 1% teratas: <b>%{y:.1f}%</b><extra></extra>",
))

# Line 2 — Kekayaan bersih pribadi (Purple)
fig.add_trace(go.Scatter(
    name="Kekayaan bersih pribadi | Proporsi 1% teratas",
    x=df["tahun"],
    y=df["kekayaan_top1"],
    mode="lines",
    line=dict(color=COLOR_KEKAYAAN, width=3),
    hovertemplate="<b>%{x}</b><br>Kekayaan 1% teratas: <b>%{y:.1f}%</b><extra></extra>",
))

# ── Layout ────────────────────────────────────────────────────────────
fig.update_layout(
    plot_bgcolor=COLOR_BG,
    paper_bgcolor="white",
    legend=dict(
        orientation="v",
        yanchor="top",
        y=0.98,
        xanchor="right",
        x=0.98,
        font=dict(size=11, family="Arial"),
        bgcolor="rgba(255,255,255,0.95)",
        bordercolor="#DDD",
        borderwidth=1,
    ),
    showlegend=True,
    yaxis=dict(
        title="Proporsi terhadap total (%)",
        showgrid=True,
        gridcolor="#E0E0E0",
        gridwidth=1,
        zeroline=False,
        range=[12, 24],
        tickfont=dict(size=11, color="#333"),
    ),
    xaxis=dict(
        title="Tahun",
        showgrid=True,
        gridcolor="#E0E0E0",
        gridwidth=1,
        tickfont=dict(size=11, color="#333"),
        dtick=10,  # interval 10 tahun
    ),
    margin=dict(t=40, b=60, l=60, r=40),
    height=520,
    hovermode="x unified",
)

st.plotly_chart(fig, use_container_width=True)

# ── Keterangan (di luar chart tapi styling matching) ─────────────────
st.markdown("""
<div style="
    background: linear-gradient(to right, rgba(240, 248, 255, 0.95), rgba(240, 248, 255, 0.8));
    border: 2px solid #2196F3;
    border-radius: 6px;
    padding: 16px 20px;
    margin: -10px 0 20px 0;
    font-size: 13px;
    line-height: 1.8;
    color: #000000;
    box-shadow: 0 2px 4px rgba(33, 150, 243, 0.1);
">
Kelompok 1% teratas di Indonesia menguasai sekitar <strong style="color: #000000;">20–21%</strong> total kekayaan dan sekitar <strong style="color: #000000;">17–18%</strong> dari pendapatan nasional sebelum pajak. Artinya, segelintir orang super kaya menikmati hampir seperlima dari seluruh kekayaan dan pendapatan yang dihasilkan sebelum redistribusi melalui pajak (lihat Gambar 5).
</div>
""", unsafe_allow_html=True)

chart_footer("World Inequality Database (2024), diolah CELIOS")

# ── Catatan data ──────────────────────────────────────────────────────
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

with st.expander("🔗 Kode Embed WordPress — Gambar 5"):
    st.code("""<!-- Gambar 5: Ketimpangan Pendapatan dan Kekayaan, Indonesia 1965-2024 -->
<iframe
  src="https://celios-ketimpangan.streamlit.app/Ketimpangan_Historis?embed=true"
  width="100%" height="550" frameborder="0"
  style="border-radius:8px; box-shadow:0 2px 8px rgba(0,0,0,0.1);"
  loading="lazy">
</iframe>""", language="html")
