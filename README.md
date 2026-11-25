# 🏠 House Price Exploratory Data Analysis (EDA)

## 📌 Project Overview

This project focuses on performing Exploratory Data Analysis (EDA) on the Ames Housing Dataset to understand the factors that influence residential house prices.

The project uses Python libraries to clean, analyze, summarize, and visualize housing data. An interactive dashboard is also developed using Streamlit.

**This project focuses on data analysis and visualization, not machine learning.**

## 🎯 Objectives

- Understand the structure of the housing dataset.
- Identify and analyze missing values.
- Detect duplicate records and possible outliers.
- Study the distribution of house prices.
- Analyze relationships between house prices and other features.
- Visualize important patterns using graphs and charts.
- Build an interactive EDA dashboard.

## 📂 Dataset

**Dataset:** Ames Housing Dataset

**Source:** Kaggle – House Prices: Advanced Regression Techniques

**File:** `train.csv`

The dataset contains approximately 1,460 rows and 81 columns, describing different features of residential properties.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit
- Google Colab
- Jupyter Notebook

## 📊 Exploratory Data Analysis

The following analysis was performed:

1. Dataset inspection and understanding.
2. Statistical summary of numerical features.
3. Missing value analysis.
4. Duplicate and data quality checks.
5. Sale price distribution analysis.
6. Outlier detection using boxplots.
7. Correlation analysis.
8. House price comparison across neighbourhoods.
9. Overall quality versus sale price analysis.
10. Final EDA dashboard with four visualizations.

## 📈 Key Findings

- Overall Quality has a strong positive correlation with SalePrice.
- Ground Living Area is an important factor associated with house prices.
- House prices vary across different neighbourhoods.
- SalePrice has a right-skewed distribution.
- Data quality checks help identify missing values and possible inconsistencies.

## 🌐 Interactive Dashboard

An interactive dashboard is developed using Streamlit.

It allows users to:
- Upload the housing dataset.
- View dataset information.
- Explore missing values.
- Analyze house price distributions.
- Visualize living area versus sale price.
- Compare average prices across neighbourhoods.
- Explore correlation results.

## 🚀 How to Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/srushtisatav07/eda-.git
```

### 2. Open the project folder

```bash
cd eda-
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

### 5. Upload the dataset

Upload the `train.csv` file using the dashboard's sidebar.

## 📁 Project Structure

```text
eda-/
│
├── app.py
├── requirements.txt
├── README.md
└── Copy_of_Untitled3 (1).ipynb
```

## 👩‍💻 Author

**Srushti Satav**

GitHub: [@srushtisatav07](https://github.com/srushtisatav07)

## 📌 Conclusion

This project demonstrates how Exploratory Data Analysis can be used to understand real-world housing data through data cleaning, statistical analysis, and visualization.

It provides insights into the factors associated with house prices and presents the findings through an interactive dashboard.

---

⭐ If you find this project useful, feel free to explore the repository!
