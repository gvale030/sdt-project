import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Car Advertisement Dashboard", layout="centered")

st.title("🚗 Car Advertisement Dashboard")
st.markdown("Explore and analyze car ad data with interactive visualizations.")

# Load dataset from CSV file
@st.cache_data
def load_data():
    return pd.read_csv("vehicles_us.csv")  # Make sure this file is in your repo

df = load_data()

st.subheader("📋 Data Preview")
st.dataframe(df.head())

# Select numeric columns
numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns.tolist()

if numeric_cols:
    # 📊 Histogram
    st.subheader("📊 Histogram")
    hist_column = st.selectbox("Choose a column for histogram", numeric_cols)
    fig1, ax1 = plt.subplots()
    ax1.hist(df[hist_column].dropna(), bins=30, edgecolor='black')
    ax1.set_title(f"Histogram of {hist_column}")
    ax1.set_xlabel(hist_column)
    ax1.set_ylabel("Frequency")
    st.pyplot(fig1)

    # 📈 Scatterplot
    st.subheader("📈 Scatter Plot")
    x_col = st.selectbox("X-axis", numeric_cols, index=0)
    y_col = st.selectbox("Y-axis", numeric_cols, index=1 if len(numeric_cols) > 1 else 0)
    fig2, ax2 = plt.subplots()
    ax2.scatter(df[x_col], df[y_col], alpha=0.6)
    ax2.set_xlabel(x_col)
    ax2.set_ylabel(y_col)
    ax2.set_title(f"{y_col} vs {x_col}")
    st.pyplot(fig2)
else:
    st.warning("No numeric columns found for plotting.")
