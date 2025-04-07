import streamlit as st
import pandas as pd

st.set_page_config(page_title="Car Advertisement Explorer", layout="centered")

st.title("🚗 Car Advertisement Dashboard")
st.markdown("Explore and analyze car advertisement data easily!")

# Upload dataset
uploaded_file = st.file_uploader("vehicles_us.csv", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("📋 Preview of the Data")
    st.dataframe(df.head())

    st.subheader("📊 Summary Statistics")
    st.write(df.describe())

    st.subheader("🔎 Column Names")
    st.write(df.columns.tolist())
else:
    st.info("Please upload a CSV file to get started.")
