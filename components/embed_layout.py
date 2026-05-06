import streamlit as st


def apply_embed_mode():
    params = st.query_params
    is_embed = params.get("embed") == "true"

    if is_embed:
        st.markdown("""
            <style>
                #MainMenu {visibility: hidden;}
                header {visibility: hidden;}
                footer {visibility: hidden;}
                section[data-testid="stSidebar"] {display: none;}
                .block-container {padding-top: 1rem !important;}
            </style>
        """, unsafe_allow_html=True)
