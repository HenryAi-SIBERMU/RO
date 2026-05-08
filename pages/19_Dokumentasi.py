import streamlit as st
from pathlib import Path
from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar

st.set_page_config(page_title="Dokumentasi", layout="wide")
apply_embed_mode()
render_sidebar()

st.title("Dokumentasi — Strategi & Arsitektur")
st.markdown("---")

strategy_path = Path(__file__).resolve().parent.parent / "docs" / "STRATEGY.md"
if strategy_path.exists():
    st.markdown(strategy_path.read_text(encoding="utf-8"))
else:
    st.error("STRATEGY.md tidak ditemukan.")
