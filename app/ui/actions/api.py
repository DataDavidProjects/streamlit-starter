import streamlit as st
from loguru import logger
import numpy as np


class API:
    def __init__(self):
        logger.debug("API initialized.")

    def call_api(self):
        data = np.random.randn(10, 20)
        return st.write(data)
