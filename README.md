# 📊 Retail Sales Analysis & Visualization Dashboard

## 📌 Overview

This project presents a comprehensive analysis of retail and warehouse sales data to uncover trends in product performance, supplier dynamics, and inventory behavior. It combines exploratory data analysis (EDA) with an interactive visualization dashboard built using PyQt5.

---

## 🎯 Objectives

* Analyze monthly sales trends and seasonality
* Identify top-performing products and categories
* Evaluate supplier performance and diversity
* Detect inefficient inventory patterns (high transfers, low sales)
* Support data-driven retail decision-making

---

## 🛠️ Tech Stack

* **Python** (Pandas, NumPy)
* **Matplotlib / Seaborn** – Data visualization
* **PyQt5** – Interactive dashboard
* **EDA Techniques** – Statistical and visual analysis

---

## 📂 Project Structure

```
retail-sales-analysis/
│
├── data/                  # Input dataset
├── assets/                # Generated visualizations
├── src/                   # Source code
│   ├── main.py
│   ├── preprocessing.py
│   ├── eda.py
│   ├── visualization.py
│   ├── data_description.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Features

### 🔹 Data Preprocessing

* Missing value handling
* Data cleaning and filtering
* Feature engineering:

  * Total Sales
  * Transfer Ratio
  * Month Name

### 🔹 Exploratory Data Analysis

* Product performance analysis
* Supplier contribution and diversity
* Inventory flow and inefficiencies
* Correlation and trend analysis

### 🔹 Dashboard

Interactive GUI built with PyQt5:

* Product insights
* Supplier performance
* Inventory analysis
* Strategic visualizations

---

## 📊 Key Insights

* A small percentage of products generate the majority of revenue (Pareto principle)
* Alcohol categories dominate overall sales
* Significant number of SKUs have low or zero sales
* Some products show high transfers but low sales → inefficiency

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the dashboard

```bash
python src/main.py
```

---

## 📸 Sample Visualizations

Check the Visualizations appended in the repository.

---

## 🚀 Future Improvements

* Add machine learning for sales prediction
* Integrate real-time data sources
* Deploy as a web-based dashboard

---

## 📄 License

This project is for academic and educational purposes.

