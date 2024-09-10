import streamlit as st 
import pandas as pd 
import plotly.express as px 
import pydeck as pdk
from utils.utils import load_data

def main():

    st.title("Teams")

    df = load_data()
    with st.expander("DataFrame"):
        st.dataframe(df)

    initial_view = pdk.ViewState(latitude=54.5260,longitude=15.2551,zoom=2,pitch=5)
    heatmap_layer = pdk.Layer("HeatmapLayer",data=df,
                            opacity=0.9,
                            get_position=["lng","lat"],
                            threshold=0.2,
                            get_weight="population",
                            pickable=True)

    scatter_layer = pdk.Layer("ScatterplotLayer",data=df,
                            get_position=["lng","lat"],
                            auto_highlight=True,
                            get_radius="population/100",
                            get_fill_color=[255,140,0],
                            get_line_color=[0,0,0],
                            pickable=True)

    # Maps
    all_layers = {"heatmap":heatmap_layer,"scatter":scatter_layer}
    selected_layer = st.sidebar.selectbox("Select Layer",list(all_layers.keys()))

    # Plot
    st.pydeck_chart(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state=initial_view,
            layers=all_layers[selected_layer],
            tooltip={"text":"{country}\n{population}"}
            )
        )

if __name__ == '__main__':
    main()