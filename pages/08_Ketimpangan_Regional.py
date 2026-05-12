import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar
from components.chart_wrapper import chart_header, chart_footer

BASE_DIR = Path(__file__).resolve().parent.parent
_G11_profile = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar11.html"
_G11_chartjs = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar11_chartjs.html"
_G11_plotly = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar11_plotly.html"
_G12_chartjs = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar12_chartjs.html"
_G12_plotly = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar12_plotly.html"
_G13_chartjs = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar13_chartjs.html"
_G13_plotly = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar13_plotly.html"
_G14_chartjs = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar14_chartjs.html"
_G14_plotly = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar14_plotly.html"
_G15_chartjs = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar15_chartjs.html"
_G15_plotly = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar15_plotly.html"
_G16_chartjs = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar16_chartjs.html"
_G16_plotly = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar16_plotly.html"
_G17 = BASE_DIR / "embed" / "08_Ketimpangan_Regional_gambar17.html"

st.set_page_config(
    page_title="Ketimpangan Regional",
    layout="wide",
    page_icon="c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png",
)
apply_embed_mode()
render_sidebar()

chart_header(
    "Profil Elite Bisnis: Basis, Lokasi Operasi, dan Sektor",
    "Gambar 11a — Hal. 27",
)
components.html(_G11_profile.read_text(encoding="utf-8"), height=1580, scrolling=True)
chart_footer("Laporan Ketimpangan Ekonomi Indonesia 2026, diolah CELIOS")
with st.expander("🔗 Kode Embed WordPress — Gambar 11a (Profil Elite)"):
    st.code(
        """<!-- Gambar 11a: Profil Elite Bisnis -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar11.html"
  width="100%" height="1580" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;"
  loading="lazy">
</iframe>""",
        language="html",
    )

chart_header(
    "Ketimpangan dan Kemiskinan Regional di Indonesia berdasarkan Pulau",
    "Gambar 11b — Hal. 27",
)
tab_chartjs, tab_plotly = st.tabs(["Versi Chart.js", "Versi Plotly"])
with tab_chartjs:
    components.html(_G11_chartjs.read_text(encoding="utf-8"), height=720, scrolling=True)
with tab_plotly:
    components.html(_G11_plotly.read_text(encoding="utf-8"), height=720, scrolling=True)
chart_footer("Laporan Harta Kekayaan Pejabat Negara 2025, diolah CELIOS")
with st.expander("🔗 Kode Embed WordPress — Gambar 11b (Chart.js)"):
    st.code(
        """<!-- Gambar 11b: Ketimpangan & Kemiskinan Regional — Chart.js -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar11_chartjs.html"
  width="100%" height="720" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;"
  loading="lazy">
</iframe>""",
        language="html",
    )
with st.expander("🔗 Kode Embed WordPress — Gambar 11b (Plotly)"):
    st.code(
        """<!-- Gambar 11b: Ketimpangan & Kemiskinan Regional — Plotly -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar11_plotly.html"
  width="100%" height="720" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;"
  loading="lazy">
</iframe>""",
        language="html",
    )

chart_header("Distribusi Pendapatan dan Kekayaan di Indonesia", "Gambar 12 — Hal. 28")
tab_g12_chartjs, tab_g12_plotly = st.tabs(["Versi Chart.js", "Versi Plotly"])
with tab_g12_chartjs:
    components.html(_G12_chartjs.read_text(encoding="utf-8"), height=700, scrolling=True)
with tab_g12_plotly:
    components.html(_G12_plotly.read_text(encoding="utf-8"), height=700, scrolling=True)
chart_footer("World Inequality Database (2019), diolah CELIOS")
with st.expander("🔗 Kode Embed WordPress — Gambar 12 (Chart.js)"):
    st.code(
        """<!-- Gambar 12: Distribusi Pendapatan & Kekayaan — Chart.js -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar12_chartjs.html"
  width="100%" height="700" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;"
  loading="lazy">
</iframe>""",
        language="html",
    )
with st.expander("🔗 Kode Embed WordPress — Gambar 12 (Plotly)"):
    st.code(
        """<!-- Gambar 12: Distribusi Pendapatan & Kekayaan — Plotly -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar12_plotly.html"
  width="100%" height="700" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;"
  loading="lazy">
</iframe>""",
        language="html",
    )

chart_header("Peningkatan Rata-Rata Upah Buruh Nasional", "Gambar 13 — Hal. 28")
tab_g13_chartjs, tab_g13_plotly = st.tabs(["Versi Chart.js", "Versi Plotly"])
with tab_g13_chartjs:
    components.html(_G13_chartjs.read_text(encoding="utf-8"), height=740, scrolling=True)
with tab_g13_plotly:
    components.html(_G13_plotly.read_text(encoding="utf-8"), height=740, scrolling=True)
chart_footer("Sakernas (Agustus 2024 & 2025), diolah CELIOS")
with st.expander("🔗 Kode Embed WordPress — Gambar 13 (Chart.js)"):
    st.code(
        """<!-- Gambar 13: Peningkatan Upah Nasional — Chart.js -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar13_chartjs.html"
  width="100%" height="740" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;"
  loading="lazy">
</iframe>""",
        language="html",
    )
with st.expander("🔗 Kode Embed WordPress — Gambar 13 (Plotly)"):
    st.code(
        """<!-- Gambar 13: Peningkatan Upah Nasional — Plotly -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar13_plotly.html"
  width="100%" height="740" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;"
  loading="lazy">
</iframe>""",
        language="html",
    )

chart_header(
    "Simpanan Bank Umum Berdasarkan Jumlah Nominal", "Gambar 14 — Hal. 29"
)
tab_g14_chartjs, tab_g14_plotly = st.tabs(["Versi Chart.js", "Versi Plotly"])
with tab_g14_chartjs:
    components.html(_G14_chartjs.read_text(encoding="utf-8"), height=760, scrolling=True)
with tab_g14_plotly:
    components.html(_G14_plotly.read_text(encoding="utf-8"), height=760, scrolling=True)
chart_footer("Data Distribusi Simpanan Bank Umum 2014-2025, estimasi dummy oleh CELIOS")
with st.expander("🔗 Kode Embed WordPress — Gambar 14 (Chart.js)"):
    st.code(
        """<!-- Gambar 14: Simpanan Bank Umum — Chart.js -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar14_chartjs.html"
  width="100%" height="760" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;"
  loading="lazy">
</iframe>""",
        language="html",
    )
with st.expander("🔗 Kode Embed WordPress — Gambar 14 (Plotly)"):
    st.code(
        """<!-- Gambar 14: Simpanan Bank Umum — Plotly -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar14_plotly.html"
  width="100%" height="760" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;"
  loading="lazy">
</iframe>""",
        language="html",
    )

chart_header(
    "Rata-rata Simpanan Bank Umum Berdasarkan Nominal", "Gambar 15 — Hal. 29"
)
tab_g15_chartjs, tab_g15_plotly = st.tabs(["Versi Chart.js", "Versi Plotly"])
with tab_g15_chartjs:
    components.html(_G15_chartjs.read_text(encoding="utf-8"), height=720, scrolling=True)
with tab_g15_plotly:
    components.html(_G15_plotly.read_text(encoding="utf-8"), height=720, scrolling=True)
chart_footer("Data Distribusi Simpanan Bank Umum 2014-2025, estimasi dummy oleh CELIOS")
with st.expander("🔗 Kode Embed WordPress — Gambar 15 (Chart.js)"):
    st.code(
        """<!-- Gambar 15: Rata-rata Simpanan Bank Umum — Chart.js -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar15_chartjs.html"
  width="100%" height="720" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;"
  loading="lazy">
</iframe>""",
        language="html",
    )
with st.expander("🔗 Kode Embed WordPress — Gambar 15 (Plotly)"):
    st.code(
        """<!-- Gambar 15: Rata-rata Simpanan Bank Umum — Plotly -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar15_plotly.html"
  width="100%" height="720" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;"
  loading="lazy">
</iframe>""",
        language="html",
    )

chart_header(
    "Proporsi Pendapatan 1% Teratas vs PPh Badan", "Gambar 16 — Hal. 30"
)
tab_g16_chartjs, tab_g16_plotly = st.tabs(["Versi Chart.js", "Versi Plotly"])
with tab_g16_chartjs:
    components.html(_G16_chartjs.read_text(encoding="utf-8"), height=680, scrolling=True)
with tab_g16_plotly:
    components.html(_G16_plotly.read_text(encoding="utf-8"), height=680, scrolling=True)
chart_footer("WID.world (2025); Kemenkeu (2025); BPS (2025); Trading Economics (2025), diolah CELIOS")
with st.expander("🔗 Kode Embed WordPress — Gambar 16 (Chart.js)"):
    st.code(
        """<!-- Gambar 16: Proporsi Pendapatan 1% vs PPh Badan — Chart.js -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar16_chartjs.html"
  width="100%" height="680" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;"
  loading="lazy">
</iframe>""",
        language="html",
    )
with st.expander("🔗 Kode Embed WordPress — Gambar 16 (Plotly)"):
    st.code(
        """<!-- Gambar 16: Proporsi Pendapatan 1% vs PPh Badan — Plotly -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar16_plotly.html"
  width="100%" height="680" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;"
  loading="lazy">
</iframe>""",
        language="html",
    )

chart_header(
    "Generasi Muda yang Terhimpit Sistem Oligarki", "Gambar 17 — Hal. 31"
)
components.html(_G17.read_text(encoding="utf-8"), height=700, scrolling=True)
chart_footer("Diolah oleh peneliti")
with st.expander("🔗 Kode Embed WordPress — Gambar 17"):
    st.code(
        """<!-- Gambar 17: Generasi Muda yang Terhimpit Sistem Oligarki -->
<iframe
  src="https://henryai-sibermu.github.io/RO/embed/08_Ketimpangan_Regional_gambar17.html"
  width="100%" height="700" frameborder="0"
  style="border-radius:32px; background:#f5f3ff;"
  loading="lazy">
</iframe>""",
        language="html",
    )

