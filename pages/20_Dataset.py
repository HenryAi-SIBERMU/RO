import streamlit as st
import pandas as pd
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

    for f in csv_files:
        try:
            df = pd.read_csv(f)
            if df.empty:
                continue
            with st.expander(f"`{f.name}` — {len(df)} baris × {len(df.columns)} kolom"):
                st.dataframe(df, use_container_width=True, hide_index=True)
        except Exception:
            pass
