import re
import streamlit as st
from pathlib import Path
from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar

def strip_emoji(text: str) -> str:
    return re.compile(
        "[\U00010000-\U0010ffff\U0001F300-\U0001F9FF"
        "\U00002600-\U000027BF\U0000FE00-\U0000FE0F\u200d]+",
        flags=re.UNICODE,
    ).sub("", text)

st.set_page_config(page_title="Dokumentasi", layout="wide")
apply_embed_mode()
render_sidebar()

st.title("Dokumentasi")
st.markdown("---")

docs_dir = Path(__file__).resolve().parent.parent / "docs"

tab1, tab2 = st.tabs(["Strategi & Arsitektur", "Chart Inventory"])

with tab1:
    f = docs_dir / "STRATEGY.md"
    if f.exists():
        st.markdown(f.read_text(encoding="utf-8"))
    else:
        st.error("STRATEGY.md tidak ditemukan.")

with tab2:
    f = docs_dir / "CHART-INVENTORY.md"
    if f.exists():
        st.markdown(strip_emoji(f.read_text(encoding="utf-8")))
    else:
        st.error("CHART-INVENTORY.md tidak ditemukan.")
