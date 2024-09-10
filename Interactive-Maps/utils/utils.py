import streamlit as st
import pandas as pd

def load_data():
    data = st.file_uploader("Upload a CSV File", type=["csv","txt"])
    if data is None:
        data = "data/worldcities.csv"
    return pd.read_csv(data)