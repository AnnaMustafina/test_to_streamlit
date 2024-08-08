
import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Добро пожаловать на демо-страничку отчёта 👋")

st.sidebar.success("Можно выбрать вкладки")

st.markdown(
    """
    Эта страничка будет заполняться разными отчётами. В зависимости от того, кто к ней обратиться
"""
)
