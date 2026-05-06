import streamlit as st


def chart_header(title: str, subtitle: str = ""):
    st.markdown(f"### {title}")
    if subtitle:
        st.caption(subtitle)


def chart_footer(source: str):
    st.markdown(
        f"<p style='font-size:11px; color:#888; margin-top:4px;'>Sumber: {source}</p>",
        unsafe_allow_html=True
    )
