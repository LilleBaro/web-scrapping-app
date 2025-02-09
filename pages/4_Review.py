import streamlit as st
import streamlit.components.v1 as components

st.markdown("<h1 style='text-align: center; color: white;'>Review Page</h1>", unsafe_allow_html=True)

components.html(
    """
    <iframe src="https://ee.kobotoolbox.org/i/ulFuflUv" width="800" height="600" frameborder="0"></iframe>
    """,
    height=600,
    width=800
) 