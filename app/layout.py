from ui.components.header import Header
from ui.components.sidebar import Sidebar
from ui.components.main import Main
from ui.components.footer import Footer
import streamlit as st
from loguru import logger


class UI(Sidebar, Header, Main, Footer):
    def __init__(self, session: st.session_state):
        logger.debug("UI initialized.")
        st.logo("https://www.streamlit.io/images/brand/streamlit-mark-color.png")
        Sidebar.__init__(self)
        Header.__init__(self)
        Main.__init__(self)
        Footer.__init__(self)
        self.session = session
