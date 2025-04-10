import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Car Advertisement Dashboard", layout="centered")

st.title("🚗 Car Advertisement Dashboard")
st.markdown("Explore and analyze car ad data with interactive visualizations.")

# Load dataset from CSV file
@st.cache_data
def load_data():
    return pd.read_csv("vehicles_us.csv")

df = load_data()

# Data preview
st.subheader("📋 Data Preview")
st.dataframe(df.head())

# Select numeric columns
numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns.tolist()

if numeric_cols:
    # 📊 Histogram
    st.subheader("📊 Histogram")
    hist_column = st.selectbox("Choose a column for histogram", numeric_cols)
    fig1 = px.histogram(df, x=hist_column, nbins=30, title=f"Histogram of {hist_column}")
    st.plotly_chart(fig1)

    # 📈 Scatterplot
    st.subheader("📈 Scatter Plot")
    x_col = st.selectbox("X-axis", numeric_cols, index=0)
    y_col = st.selectbox("Y-axis", numeric_cols, index=1 if len(numeric_cols) > 1 else 0)
    fig2 = px.scatter(df, x=x_col, y=y_col, title=f"{y_col} vs {x_col}")
    st.plotly_chart(fig2)
else:
    st.warning("No numeric columns found for plotting.")

