import streamlit as st
from layout import UI

try:
    st.set_page_config(
        page_title="Streamlit App",
        page_icon="public/logo.png",
        layout="wide",
        initial_sidebar_state="expanded",
    )
except Exception as e:
    st.error(f"An error occurred: {e}")


# Define UI
ui = UI(session=st.session_state)
