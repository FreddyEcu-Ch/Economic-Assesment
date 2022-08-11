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
    time = int(st.number_input("Enter the time for the project in years:"))
    values = [
        st.number_input(f"Enter the value for year {i}: ")
        for i, year in enumerate(range(time + 1))
    ]

    wells_type = st.selectbox(
        "Choose the well type", ("Horizontal", "Directional", "Vertical")
    )
    if wells_type == "Horizontal":
        q = st.number_input(f"Enter the flow rate for a {wells_type} well: ")
    elif wells_type == "Directional":
        q = st.number_input(f"Enter the flow rate for a {wells_type} well: ")
    elif wells_type == "Vertical":
        q = st.number_input(f"Enter the flow rate for a {wells_type} well: ")

    wo_type = st.selectbox(
        "Choose the workover type",
        ("Upsizing", "Acid Stimulation", "Hydraulic fracturing"),
    )
    if wo_type == "Upsizing":
        dq = st.number_input(
            f"Enter the enhanced percentage of flow rate due to {wo_type}: "
        )
    elif wo_type == "Acid Stimulation":
        dq = st.number_input(
            f"Enter the enhanced percentage of flow rate due to {wo_type}: "
        )
    elif wo_type == "Hydraulic fracturing":
        dq = st.number_input(
            f"Enter the enhanced percentage of flow rate due to {wo_type}: "
        )

    # Table of years
    st.subheader("Timeline")
    values_dict = {f"Year {i}": [value] for i, value in enumerate(values)}
    print(values_dict)
    df = pd.DataFrame(values_dict, columns=[f"Year {i}" for i in range(time + 1)])
    df["Well Type"] = wells_type
    st.dataframe(df)
