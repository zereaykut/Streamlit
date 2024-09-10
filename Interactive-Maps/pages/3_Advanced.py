import streamlit as st 
import plotly.express as px
import geopandas as gpd
import pandas as pd
from utils.utils import load_data

def main():

    st.title("Advanced")
    
    df = load_data()
    with st.expander("DataFrame"):
        st.dataframe(df)
    
    selected = st.selectbox("Select", ["country", "city"])
    if selected == "country":
        selected_list = df[selected].unique().tolist()
        param = "Ghana"
    else:
        selected_list = df[selected].unique().tolist()
        param = "Bremen"
    selecteds = st.multiselect(selected, selected_list, default=[param])
    gdf = df[df[selected].isin(selecteds)]
    with st.expander(f"DataFrame {selected}"):
        st.dataframe(gdf)

    fig = px.scatter_mapbox(gdf, lat="lat", lon="lng", hover_name="city", hover_data=["country", "population"], color_discrete_sequence=["fuchsia"], zoom=2, height=700)
    fig.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(fig)

if __name__ == '__main__':
    main()