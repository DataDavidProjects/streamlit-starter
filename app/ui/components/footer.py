import streamlit as st
from loguru import logger


class Footer:
    def __init__(self):
        logger.debug("Footer initialized.")
        self.render_footer()

    def render_footer(self):
        st.write("This is the footer of the application.")
