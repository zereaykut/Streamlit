import streamlit as st 
import plotly.express as px
import geopandas as gpd
import pandas as pd
from utils.utils import load_data

def main():

    st.title("Home")

    df = load_data()
    with st.expander("DataFrame"):
        st.dataframe(df)

    fig = px.scatter_mapbox(df, lat="lat", lon="lng", hover_name="city", hover_data=["country", "population"], color_discrete_sequence=["fuchsia"], zoom=1,height=700)
    fig.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(fig)


if __name__ == '__main__':
    main()