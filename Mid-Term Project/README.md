# 📘 **BMW Sales Analysis & FastAPI Prediction Service**

This project combines **data analysis**, **machine learning model
training**, and a **FastAPI-based prediction API** to classify BMW car
sales using features such as engine size, mileage, and price.\
It also provides a **Dockerized environment** for easy deployment.

------------------------------------------------------------------------

## 🚀 **Project Structure**

    ├── mid_term_project.py       # Data cleaning, EDA, model training & evaluation
    ├── main.py                   # FastAPI application to serve predictions
    ├── dockerfile                # Docker setup for deployment
    ├── Decision_Tree.pkl         # Trained Decision Tree model (required for API)
    └── README.md                 # Project documentation

------------------------------------------------------------------------

## 📊 **1. Data Analysis & Model Training**

The file **mid_term_project.py** performs:

### ✔ Data Loading & Cleaning

-   Reads BMW sales dataset (2010-2024)
-   Converts year column to datetime
-   Checks missing values & data types

### ✔ Exploratory Data Analysis (EDA)

-   Histograms of numerical variables
-   Sales trends by region
-   Scatter plots (Price vs. Sales Volume)
-   Correlation heatmaps (numeric + categorical)

### ✔ Feature Engineering

-   One-hot encoding for categorical features
-   Statistical feature importance using ROC-AUC

### ✔ Model Training

Trains and evaluates multiple ML models:

#### 🔹 Regression Models (Predicting Sales Volume)

-   Linear Regression
-   Decision Tree Regressor
-   Random Forest Regressor

Metrics computed: - MAE
- RMSE
- R² Score

#### 🔹 Classification Models (Predicting Sales Classification)

-   Logistic Regression
-   Decision Tree Classifier
-   Random Forest Classifier

Metrics computed: - Precision
- Recall
- Accuracy
- Confusion Matrix

A final **Decision Tree model** is saved as:
`Decision_Tree.pkl`

------------------------------------------------------------------------

## ⚡ **2. FastAPI Prediction Service**

The FastAPI application in **main.py**:

### 🔹 Loads the trained Decision Tree model

### 🔹 Defines Input Schema

``` json
{
  "Engine_Size_L": 3.0,
  "Mileage_KM": 20000,
  "Price_USD": 45000
}
```

### 🔹 `/predict` Endpoint Output

``` json
{
  "predicted_sales_classification": "High"
}
```

------------------------------------------------------------------------

## 🐳 **3. Docker Deployment**

### Build Docker Image

``` bash
docker build -t bmw-sales-api .
```

### Run the Container

``` bash
docker run -p 8000:8000 bmw-sales-api
```

### Access API Docs

👉 `http://localhost:8000/docs`

------------------------------------------------------------------------

## 📦 **4. Requirements**

``` bash
pip install pandas numpy matplotlib seaborn scikit-learn FastAPI uvicorn
```

------------------------------------------------------------------------

## 📜 **License**

This project is for academic and learning purposes.
