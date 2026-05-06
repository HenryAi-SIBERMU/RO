import streamlit as st


def _is_embed() -> bool:
    return st.query_params.get("embed") == "true"


def chart_header(title: str, subtitle: str = ""):
    if _is_embed():
        return
    st.markdown(f"### {title}")
    if subtitle:
        st.caption(subtitle)


def chart_footer(source: str):
    if _is_embed():
        return
    st.markdown(
        f"<p style='font-size:11px; color:#888; margin-top:4px;'>Sumber: {source}</p>",
        unsafe_allow_html=True
    )
