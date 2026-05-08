import streamlit as st
from pathlib import Path
from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar

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
        st.markdown(f.read_text(encoding="utf-8"))
    else:
        st.error("CHART-INVENTORY.md tidak ditemukan.")
