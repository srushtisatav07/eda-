
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="House Price EDA",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 House Price Exploratory Data Analysis")
st.write(
    "An interactive dashboard to explore the Ames Housing Dataset."
)

st.sidebar.header("Upload Dataset")
uploaded_file = st.sidebar.file_uploader(
    "Upload train.csv",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
elif "train.csv" in __import__("os").listdir():
    df = pd.read_csv("train.csv")
else:
    st.info("Please upload the Ames Housing train.csv dataset to begin.")
    st.stop()

required_columns = [
    "SalePrice", "OverallQual", "GrLivArea",
    "Neighborhood", "YearBuilt"
]

if not all(col in df.columns for col in required_columns):
    st.error("This file does not contain the required House Price columns.")
    st.stop()

st.success("Dataset loaded successfully!")

st.header("Dataset Overview")

col1, col2, col3 = st.columns(3)
col1.metric("Total Houses", len(df))
col2.metric("Total Features", len(df.columns))
col3.metric("Average Sale Price", f"${df['SalePrice'].mean():,.0f}")

st.subheader("Dataset Preview")
st.dataframe(df.head(10), use_container_width=True)

st.subheader("Missing Values")
missing = df.isnull().sum()
missing = missing[missing > 0].sort_values(ascending=False)

if len(missing) > 0:
    st.bar_chart(missing.head(10))
else:
    st.write("No missing values found.")

st.header("House Price Analysis")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Sale Price Distribution")
    fig, ax = plt.subplots()
    sns.histplot(df["SalePrice"], kde=True, ax=ax)
    ax.set_xlabel("Sale Price")
    st.pyplot(fig)
    plt.close(fig)

with col2:
    st.subheader("Living Area vs Sale Price")
    fig, ax = plt.subplots()
    sns.scatterplot(
        data=df,
        x="GrLivArea",
        y="SalePrice",
        hue="OverallQual",
        palette="viridis",
        ax=ax
    )
    st.pyplot(fig)
    plt.close(fig)

st.subheader("Average Price by Neighbourhood")
neighbourhood = (
    df.groupby("Neighborhood")["SalePrice"]
    .mean()
    .sort_values(ascending=False)
)

st.bar_chart(neighbourhood.head(10))

st.subheader("House Price by Overall Quality")
fig, ax = plt.subplots()
sns.boxplot(
    data=df,
    x="OverallQual",
    y="SalePrice",
    ax=ax
)
ax.set_xlabel("Overall Quality")
ax.set_ylabel("Sale Price")
st.pyplot(fig)
plt.close(fig)

st.header("Correlation Analysis")

numeric_df = df.select_dtypes(include="number")
correlation = numeric_df.corr()["SalePrice"].drop("SalePrice")
correlation = correlation.abs().sort_values(ascending=False)

st.write("Top 10 features correlated with SalePrice:")
st.dataframe(
    correlation.head(10).rename("Correlation").to_frame(),
    use_container_width=True
)

st.subheader("Project Conclusion")
st.write("""
- Overall Quality has a strong relationship with Sale Price.
- Ground Living Area is an important factor in house prices.
- Average house prices vary across neighbourhoods.
- The Sale Price distribution can be explored using a histogram.
- Data visualization helps us understand patterns and relationships.

This project focuses on Exploratory Data Analysis (EDA), not machine learning.
""")

st.caption("Created using Python, Pandas, Matplotlib, Seaborn and Streamlit.")
