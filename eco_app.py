import numpy as np
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

# Title
st.title("**Tuma App**")
st.write("This app is about...")

# Create menu of options
with st.sidebar:
    options = option_menu(
        menu_title="Main Menu",
        options=["Home", "Economic Inputs", "Technical Inputs", "Results"],
        icons=["house", "clipboard-data", "tv", "calculator"],
    )

# Economic inputs
if options == "Economic Inputs":
    discount_rate = st.number_input("Enter the discount rate: ")
    inflation = st.number_input("Enter the inflation: ")
    oil_price = st.number_input("Enter the oil price: ")
    taxes = st.number_input("Enter the taxes: ")
    capex = st.number_input("Enter the initial investment")

elif options == "Technical Inputs":
    time = st.number_input("Enter the time for the project in years:")
    wells_type = st.selectbox(
        "Choose the well type", ("Horizontal", "Directional", "Vertical")
    )
    if wells_type == "Horizontal":
        q = st.number_input("Enter the flow rate for a horizontal well: ")
    elif wells_type == "Directional":
        q = st.number_input("Enter the flow rate for a directional well: ")
    elif wells_type == "Vertical":
        q = st.number_input("Enter the flow rate for a vertical well: ")

    wo_type = st.selectbox(
        "Choose the workover type",
        ("Upsizing", "Acid Stimulation", "Hydraulic fracturing"),
    )
    if wo_type == "Upsizing":
        dq = st.number_input("Enter the enhanced percentage of flow rate: ")
    elif wo_type == "Acid Stimulation":
        dq = st.number_input("Enter the enhanced percentage of flow rate: ")
    elif wo_type == "Hydraulic fracturing":
        dq = st.number_input("Enter the enhanced percentage of flow rate: ")

    df = pd.DataFrame(
        np.random.randn(20, 11), columns=[f"Year {i}" for i in range(int(time) + 1)]
    )
    df["Well Type"] = wells_type
    st.dataframe(df)
