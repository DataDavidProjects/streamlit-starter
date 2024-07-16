import streamlit as st
from loguru import logger


class Sidebar:
    def __init__(self):
        logger.debug("Sidebar initialized.")
        self.render_sidebar()

    def render_sidebar(self):
        st.sidebar.write("This is the sidebar of the application.")
