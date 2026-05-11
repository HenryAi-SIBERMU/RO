import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_footer

st.set_page_config(
    page_title="Komparasi Global Superkaya", 
    layout="wide", 
    page_icon=str(Path(__file__).resolve().parent.parent / "assets" / "logo_celios.png")
)
apply_embed_mode()
render_sidebar()

# ── Sisipan: Perbandingan Kekayaan ────────────────────────────────────
st.divider()
st.markdown("### Perbandingan Kekayaan: Superkaya vs Buruh")

_SISIPAN = Path(__file__).resolve().parent.parent / "embed" / "05_Komparasi_Global_sisipan.html"
components.html(_SISIPAN.read_text(encoding="utf-8"), height=900, scrolling=True)

chart_footer("Data CELIOS (2026)")

with st.expander("🔗 Kode Embed WordPress — Sisipan Perbandingan"):
    st.code("""<!-- Sisipan: Perbandingan Kekayaan Superkaya vs Buruh -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/05_Komparasi_Global_sisipan.html"
  width="100%" height="900" frameborder="0"
  style="border-radius:8px; box-shadow:0 2px 8px rgba(0,0,0,0.1);"
  loading="lazy">
</iframe>""", language="html")

# ── Load HTML Infografik ──────────────────────────────────────────────
st.divider()
st.markdown("### Gambar 6: Superkaya Indonesia vs Global")

HTML_PATH = Path(__file__).resolve().parent.parent / "embed" / "05_Komparasi_Global_gambar6.html"
components.html(HTML_PATH.read_text(encoding="utf-8"), height=2320, scrolling=True)

chart_footer("Data Forbes (2026), diolah oleh peneliti")

# ── Keterangan ────────────────────────────────────────────────────────
st.markdown("""
<div style="
    background: linear-gradient(to right, rgba(240, 248, 255, 0.95), rgba(240, 248, 255, 0.8));
    border: 2px solid #2196F3;
    border-radius: 6px;
    padding: 16px 20px;
    margin: 10px 0 20px 0;
    font-size: 13px;
    line-height: 1.8;
    color: #000000;
    box-shadow: 0 2px 4px rgba(33, 150, 243, 0.1);
">
<strong>Grafik menampilkan individu/keluarga dengan kekayaan bersih (net worth) tertinggi di masing-masing negara.</strong> Ranking ini menunjukkan bahwa 3 orang terkaya Indonesia (R. Budi & Keluarga Hartono, Prajogo Pangestu, dan Widjaja family) memiliki kekayaan yang sebanding atau bahkan melebihi orang terkaya dari negara-negara lain di Asia, Timur Tengah, Afrika, dan Amerika Latin.
</div>
""", unsafe_allow_html=True)

# ── Catatan data ──────────────────────────────────────────────────────
with st.expander("📋 Daftar 20 Orang Terkaya (Indonesia vs Global)"):
    st.markdown("""
    | Rank | Nama | Negara | Kekayaan (T Rp) |
    |---|---|---|---|
    | 1 | R. Budi & Keluarga Hartono | 🇮🇩 Indonesia | Rp650 |
    | 2 | Prajogo Pangestu | 🇮🇩 Indonesia | Rp483 |
    | 3 | Widjaja family | 🇮🇩 Indonesia | Rp478 |
    | 4 | Pham Nhat Vuong | 🇻🇳 Vietnam | Rp468 |
    | 5 | Jay Y. Lee | 🇰🇷 Korea Selatan | Rp456 |
    | 6 | Gina Rinehart | 🇦🇺 Australia | Rp430 |
    | 7 | Michael Platt | 🇬🇧 Inggris | Rp353 |
    | 8 | Dhanin Chearavanont | 🇹🇭 Thailand | Rp336 |
    | 9 | Prince Alwaleed Bin Talal Alsaud | 🇸🇦 Saudi Arabia | Rp336 |
    | 10 | Enrique Razon Jr. | 🇵🇭 Filipina | Rp279 |
    | 11 | Johann Rupert & family | 🇿🇦 Afrika Selatan | Rp272 |
    | 12 | Terry Gou | 🇹🇼 Taiwan | Rp258 |
    | 13 | Hussain Sajwani | 🇦🇪 UAE | Rp258 |
    | 14 | Jason Chang | 🇹🇼 Taiwan | Rp240 |
    | 15 | Robert Kuok | 🇲🇾 Malaysia | Rp240 |
    | 16 | Hamdi Ulukaya | 🇹🇷 Turki | Rp228 |
    | 17 | Nassef Sawiris | 🇪🇬 Mesir | Rp162 |
    | 18 | Vyacheslav Kim | 🇰🇿 Kazakhstan | Rp132 |
    | 19 | Marcos Galperin | 🇦🇷 Argentina | Rp122 |
    | 20 | Lorinc Meszaros | 🇭🇺 Hungaria | Rp88 |
    """)

with st.expander("🔗 Kode Embed WordPress — Gambar 6"):
    st.code("""<!-- Gambar 6: Superkaya Indonesia vs Triliuner Global -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/05_Komparasi_Global_gambar6.html"
  width="100%" height="2320" frameborder="0"
  style="border-radius:32px; background:#5a26b6;"
  loading="lazy">
</iframe>""", language="html")
