import streamlit as st
from loguru import logger


class Header:
    def __init__(self):
        logger.debug("Header initialized.")
        self.render_header()

    def render_header(self):
        st.write("This is the header of the application.")
