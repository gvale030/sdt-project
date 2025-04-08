import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Car Advertisement Dashboard", layout="centered")

st.title("🚗 Car Advertisement Dashboard")
st.markdown("Testing dataset loading...")

# Show directory contents (to debug Render)
st.write("📁 Files in current directory:", os.listdir())

@st.cache_data
def load_data():
    try:
        return pd.read_csv("car_ads.csv")
    except FileNotFoundError:
        st.error("❌ File 'car_ads.csv' not found. Make sure it's committed to GitHub.")
        return pd.DataFrame()

df = load_data()

if df.empty:
    st.warning("⚠️ No data loaded.")
else:
    st.success("✅ Data loaded successfully.")
    st.dataframe(df.head())



