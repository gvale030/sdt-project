import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Car Advertisement Explorer", layout="centered")

st.title("🚗 Car Advertisement Dashboard")
st.markdown("Explore and analyze car ad data with visualizations.")

# Upload CSV
uploaded_file = st.file_uploader("Upload your car ads dataset (.csv)", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📋 Preview of Data")
    st.dataframe(df.head())

    # Column selection for plots
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    if numeric_cols:
        st.subheader("📊 Histogram")
        hist_col = st.selectbox("Select column for histogram", numeric_cols, index=0)
        fig1, ax1 = plt.subplots()
        ax1.hist(df[hist_col].dropna(), bins=20, edgecolor='black')
        ax1.set_title(f"Histogram of {hist_col}")
        st.pyplot(fig1)

        st.subheader("📈 Scatter Plot")
        x_col = st.selectbox("Select X-axis", numeric_cols, index=0)
        y_col = st.selectbox("Select Y-axis", numeric_cols, index=1 if len(numeric_cols) > 1 else 0)
        fig2, ax2 = plt.subplots()
        ax2.scatter(df[x_col], df[y_col], alpha=0.7)
        ax2.set_xlabel(x_col)
        ax2.set_ylabel(y_col)
        ax2.set_title(f"{y_col} vs {x_col}")
        st.pyplot(fig2)
    else:
        st.warning("No numeric columns found for visualizations.")
else:
    st.info("Please upload a CSV file to get started.")
