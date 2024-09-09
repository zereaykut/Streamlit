import streamlit as st 
import pandas as pd 
from pygwalker.api.streamlit import StreamlitRenderer

st.set_page_config(
    page_title="Streamlit Pygwalker",
    layout="wide"
)

def load_data(data):
    return pd.read_csv(data)

def main():
    st.title("Streamlit PyGWalker App")
    st.subheader("Home")
    with st.form("upload_form"):
        data_file = st.file_uploader("Upload a CSV File", type=["csv","txt"])
        submitted = st.form_submit_button("Submit")

    if submitted:
        df = load_data(data_file)
        st.dataframe(df)
        pyg_app = StreamlitRenderer(df)
        pyg_app.explorer()   
    
if __name__ == "__main__":
    main()