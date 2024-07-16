import streamlit as st
from loguru import logger
from ..actions.api import API


class Main:
    def __init__(self):
        logger.debug("Main initialized.")
        self.api = API()
        self.render_main()

    def render_main(self):
        st.write("---")
        st.write("This is the main of the application.")
        if st.button("Call API"):

            self.api.call_api()
        st.write("---")
