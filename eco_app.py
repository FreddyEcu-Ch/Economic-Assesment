import numpy as np
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

# Title
st.title("**Economic Assessment App**")
st.write("This app is about...")

# Create menu of options
with st.sidebar:
    options = option_menu(
        menu_title="Main Menu",
        options=["Home", "Economic Inputs", "Technical Inputs", "Results"],
        icons=["house", "clipboard-data", "tv", "calculator"],
    )

