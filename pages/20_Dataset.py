import streamlit as st
from pathlib import Path
from components.embed_layout import apply_embed_mode
from components.sidebar import render_sidebar

st.set_page_config(page_title="Dataset", layout="wide")
apply_embed_mode()
render_sidebar()

st.title("Dataset — Data Files")
st.markdown("---")

data_dir = Path(__file__).resolve().parent.parent / "data"
csv_files = sorted([f for f in data_dir.iterdir() if f.suffix == ".csv"])

if not csv_files:
    st.info("Belum ada file data.")
else:
    st.markdown(f"Total **{len(csv_files)} file CSV** tersedia.")
    st.markdown("")

    for f in csv_files:
        size_kb = f.stat().st_size / 1024
        col1, col2, col3 = st.columns([4, 1, 1])
        col1.markdown(f"`{f.name}`")
        col2.markdown(f"`{size_kb:.1f} KB`")
        col3.download_button(
            label="Download",
            data=f.read_bytes(),
            file_name=f.name,
            mime="text/csv",
            key=f"dl_{f.name}",
        )
